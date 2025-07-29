// shreds_sniper/main.rs
use crate::common::utils::create_rpc_client;
use crate::core::tx;
use crate::tx::LATEST_BLOCKHASH;
use solana_client::nonblocking::rpc_client::RpcClient;
use {
    anyhow::Context,
    backoff::{future::retry, ExponentialBackoff},
    instruction_account_mapper::{AccountMetadata, Idl, InstructionAccountMapper},
    log::{debug, error, info, warn},
    pump_interface::instructions::PumpProgramIx,
    serde::Serialize,
    serde_json::json,
    serde_json::Value,
    serialization::{serialize_option_pubkey, serialize_pubkey},
    solana_account_decoder_client_types::token::UiTokenAmount,
    solana_sdk::{
        hash::Hash,
        instruction::{AccountMeta, CompiledInstruction, Instruction},
        message::{
            v0::{LoadedAddresses, Message, MessageAddressTableLookup},
            MessageHeader, VersionedMessage,
        },
        native_token,
        pubkey::Pubkey,
        signature::Signature,
        transaction::VersionedTransaction,
        transaction_context::TransactionReturnData,
    },
    solana_transaction_status::{
        ConfirmedTransactionWithStatusMeta, InnerInstruction, InnerInstructions, Reward,
        RewardType, TransactionStatusMeta, TransactionTokenBalance, TransactionWithStatusMeta,
        UiTransactionEncoding, VersionedTransactionWithStatusMeta,
    },
    std::{
        collections::HashMap,
        env,
        sync::Arc,
        time::{Duration, Instant as StdInstant, SystemTime, UNIX_EPOCH},
    },
    tokio::net::TcpListener,
    tokio::sync::mpsc::Sender,
    tokio::sync::Mutex,
    tonic::transport::channel::ClientTlsConfig,
    yellowstone_grpc_proto::convert_from,
};
mod shred_stream;
use crate::token_serializable::convert_to_serializable;
use anyhow::Result;
use chrono::{DateTime, NaiveDateTime, Utc};
use dotenv::dotenv;
use logger::Logger;
use once_cell::sync::Lazy;
use pump_interface::CreateIxArgs;
use reqwest::Client;
use shared_state::PENDING_MINTS;
use shared_state::{BoughtTokenInfo, BuyOrder, SellOrder, BOUGHT_TOKENS};
use shred_stream::shred_subscribe_transactions;
use spl_associated_token_account::id as ata_program_id;
use spl_token::id as spl_token_program_id;
use spl_token::instruction::TokenInstruction;
use std::collections::HashSet;
use std::sync::atomic::Ordering;
use std::sync::RwLock;
use std::time::Instant;
use tokio::signal;
use tokio::sync::mpsc;
use tokio::time::sleep;
static SKIP_CREATORS: Lazy<RwLock<HashSet<Pubkey>>> = Lazy::new(|| RwLock::new(HashSet::new()));
use crate::dex::pump_fun::PUMP_PROGRAM;
use crate::trading_loop::start_trading_loop;
mod common;
mod core;
mod dex;
mod engine;
mod instruction_account_mapper;
mod logger;
mod serialization;
mod services;
mod token_serializable;
mod trade_logger;
mod trading_loop;
const DB_URL: &str = "postgres://postgres:SolanaMEV@localhost:5432/postgres";
const OK_RESPONSE: &str = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n";
const NOT_FOUND: &str = "HTTP/1.1 404 NOT FOUND\r\n\r\n";
const PROGRAM_ID: &str = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P";
const TOKEN_PROGRAM_ID: &str = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA";
const PUMP_FUN_NEWLY_PROGRAM_ID: &str = "TSLvdd1pWpHVjahSpsvCXUbgwsL3JAcvokwaKt1eokM";

const TESTING_MODE: bool = false; // <-- Set to false in production

// The threshold in UI units that we consider “full supply.”
pub const SUPPLY_THRESHOLD_UI: f64 = 1_000_000_000.0;
const SECOND_WAVE_THRESHOLD_SOL: f64 = 0.0;

// 1. Your program IDs (String → Pubkey)
static PUMP_PROGRAM_PUBKEY: Lazy<Pubkey> =
    Lazy::new(|| PUMP_PROGRAM.parse().expect("invalid pump program id"));
static PUMP_NEWLY_PROGRAM_PUBKEY: Lazy<Pubkey> = Lazy::new(|| {
    PUMP_FUN_NEWLY_PROGRAM_ID
        .parse()
        .expect("invalid newly program id")
});

// 2. Your own wallet pubkey
static OUR_PUBKEY: Lazy<Pubkey> = Lazy::new(|| {
    std::env::var("WALLET_PUBKEY")
        .expect("WALLET_PUBKEY unset")
        .parse()
        .expect("invalid wallet pubkey")
});

// 3. All of your env-driven thresholds
static SECOND_WAVE: Lazy<bool> = Lazy::new(|| {
    std::env::var("SECOND_WAVE")
        .map(|v| v.eq_ignore_ascii_case("true"))
        .unwrap_or(false)
});
static MIN_SOL_INFLOW_TRIGGER: Lazy<f64> = Lazy::new(|| {
    env::var("MIN_SOL_INFLOW_TRIGGER")
        .ok()
        .and_then(|v| v.parse().ok())
        .unwrap_or(0.5)
});

static MIN_SOL_OUTFLOW_TRIGGER: Lazy<f64> = Lazy::new(|| {
    env::var("MIN_SOL_OUTFLOW_TRIGGER")
        .ok()
        .and_then(|v| v.parse().ok())
        .unwrap_or(0.5)
});
static MAX_CREATOR_SHARE: Lazy<f64> = Lazy::new(|| {
    std::env::var("MAX_CREATOR_SHARE_PERCENT")
        .unwrap_or_else(|_| "10.0".into())
        .parse()
        .unwrap()
});
static MAX_ACTIVE_TRADES: Lazy<usize> = Lazy::new(|| {
    std::env::var("MAX_ACTIVE_TRADES")
        .unwrap_or_else(|_| "10".into())
        .parse()
        .unwrap()
});
static FALLBACK_SLOT_THRESHOLD: Lazy<u64> = Lazy::new(|| {
    // Look for FALLBACK_SLOT_THRESHOLD in .env, defaulting to 1000
    env::var("FALLBACK_SLOT_THRESHOLD")
        .ok() // ignore missing var
        .and_then(|v| v.parse().ok()) // parse to u64
        .unwrap_or(1000) // fallback if anything goes wrong
});
// 4. Your PDA seed
static BONDING_CURVE_SEED: &'static [u8] = b"bonding-curve";

#[derive(Debug, PartialEq)]
enum TrackerState {
    WaitingForInflows,
    CreatorSold,
    WaitingSecondWave,
    Triggered,
}

struct MintTracker {
    mint: Pubkey,
    creator: Pubkey,
    curve_pda: Pubkey,
    // Accumulate SOL inflow/outflow on the curve
    sol_inflow: f64,
    sol_outflow: f64,
    creator_sold_slot: Option<u64>,
    first_wave_peak_inflow: Option<f64>,
    state: TrackerState,
    register_slot: u64,
    // maybe track when last inflow happened:
    last_inflow_slot: Option<u64>,
}

type TrackerMap = Arc<Mutex<HashMap<Pubkey, MintTracker>>>;
static GLOBAL_TRACKERS: Lazy<TrackerMap> = Lazy::new(|| Arc::new(Mutex::new(HashMap::new())));

pub async fn active_trade_count() -> usize {
    let tokens = BOUGHT_TOKENS.lock().await;
    tokens
        .values()
        .filter(|t| !t.sell_confirmed() && (t.amount() > 0 || t.fallback_amount() > 0))
        .count()
}

#[macro_use]
extern crate lazy_static;

/// Derives the PDA for the bonding curve from the mint and program id.
pub fn get_pda(mint: &Pubkey, program_id: &Pubkey) -> anyhow::Result<Pubkey> {
    let seeds = [b"bonding-curve".as_ref(), mint.as_ref()];
    let (bonding_curve, _bump) = Pubkey::find_program_address(&seeds, program_id);
    Ok(bonding_curve)
}

fn sol_delta_for_curve(
    tx_meta: &VersionedTransactionWithStatusMeta,
    curve_pda: &Pubkey,
) -> Option<f64> {
    // gather all account keys, including address-table lookups
    let keys = match &tx_meta.transaction.message {
        VersionedMessage::Legacy(m) => m.account_keys.clone(),
        VersionedMessage::V0(v0) => {
            let mut k = v0.account_keys.clone();
            k.extend(tx_meta.meta.loaded_addresses.writable.clone());
            k.extend(tx_meta.meta.loaded_addresses.readonly.clone());
            k
        }
    };
    // find the curve index
    let idx = keys.iter().position(|k| k == curve_pda)?;
    let pre = tx_meta.meta.pre_balances[idx] as i64;
    let post = tx_meta.meta.post_balances[idx] as i64;
    let delta_lamports = post - pre;
    // convert to SOL
    Some(delta_lamports as f64 / 1e9)
}

fn apply_sol_flow_rules(
    entry: &mut BoughtTokenInfo,
    delta_sol: f64,
    min_inflow: f64,
    min_outflow: f64,
    slot_delta: u64,
) -> (bool, bool) {
    const EARLY_DRAIN_SLOT_THRESHOLD: u64 = 6;

    if delta_sol > 0.0 {
        entry.add_sol_inflow(delta_sol);
    } else if delta_sol < 0.0 {
        entry.add_sol_outflow(-delta_sol);

        // immediate rug in same or next slot
        if slot_delta <= 1 {
            return (true, true); // 🚨 super-fast rug
        }

        if -delta_sol >= min_outflow {
            return (true, true); // 🚨 strong outflow
        }
    }

    // catch "fake pump then dump" pattern
    if entry.sol_inflow() >= min_inflow {
        if entry.sol_outflow() >= entry.sol_inflow() && slot_delta <= EARLY_DRAIN_SLOT_THRESHOLD {
            return (true, true);
        }

        return (true, true);
    }

    (false, false)
}

fn compute_creator_share_percent(
    post_balances: &[TransactionTokenBalance],
    creator: &Pubkey,
) -> Option<f64> {
    // Sum all UI amounts for this mint
    let mut total: f64 = 0.0;
    let mut creator_amt: f64 = 0.0;
    for tb in post_balances {
        if let Some(ui) = tb.ui_token_amount.ui_amount {
            total += ui;
            // compare owner strings; TransactionTokenBalance.owner is a String
            if tb.owner == creator.to_string() {
                creator_amt += ui;
            }
        }
    }
    if total > 0.0 {
        Some((creator_amt / total) * 100.0)
    } else {
        None
    }
}

async fn try_send_buy_if_allowed(
    mint_str: &str,
    creator: Pubkey,
    use_jito: bool,
    urgent: bool,
    mint_sender: &tokio::sync::mpsc::Sender<BuyOrder>,
) {
    // 2. Check active + pending first
    let max_active: usize = std::env::var("MAX_ACTIVE_TRADES")
        .ok()
        .and_then(|s| s.parse().ok())
        .unwrap_or(10);
    let active = active_trade_count().await;
    let pending = PENDING_MINTS.load(Ordering::Relaxed);
    if active + pending >= max_active {
        debug!(
            "🔔 Skipping buy for {}: active+pending = {}+{} >= {}",
            mint_str, active, pending, max_active
        );
        return;
    }

    // 3. Reserve pending slot
    PENDING_MINTS.fetch_add(1, Ordering::Relaxed);

    // 4. Build and send the BuyOrder
    let order = BuyOrder {
        mint: mint_str.to_string(),
        creator,
        use_jito,
        urgent,
    };
    debug!(
        "🐣 [SHRED BUY] about to send BuyOrder → mint={} use_jito={} urgent={}",
        mint_str, use_jito, urgent
    );
    match mint_sender.send(order).await {
        Ok(()) => debug!("✅ [SHRED BUY] sent BuyOrder → mint={}", mint_str),
        Err(e) => debug!(
            "❌ [SHRED BUY] failed to send BuyOrder for {}: {:?}",
            mint_str, e
        ),
    }
}

fn get_associated_token_address_manual(owner: &Pubkey, mint: &Pubkey) -> Pubkey {
    Pubkey::find_program_address(
        &[
            owner.as_ref(),
            spl_token_program_id().as_ref(),
            mint.as_ref(),
        ],
        &ata_program_id(),
    )
    .0
}

fn current_unix_timestamp() -> u64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs()
}

#[derive(Debug, Serialize, Clone)]
struct TransactionInstructionWithParent {
    instruction: Instruction,
    parent_program_id: Option<Pubkey>,
}

#[derive(Debug, Serialize)]
pub struct DecodedInstruction {
    pub name: String,
    pub accounts: Vec<AccountMetadata>,
    pub data: serde_json::Value,
    #[serde(serialize_with = "serialize_pubkey")]
    pub program_id: Pubkey,
    #[serde(serialize_with = "serialize_option_pubkey")]
    pub parent_program_id: Option<Pubkey>,
}

fn to_camel_case(name: &str) -> String {
    let mut chars = name.chars();
    match chars.next() {
        Some(first_char) => first_char.to_lowercase().collect::<String>() + chars.as_str(),
        None => String::new(),
    }
}

fn get_instruction_name_with_typename(instruction: &TokenInstruction) -> String {
    let debug_string = format!("{:?}", instruction);
    if let Some(first_brace) = debug_string.find(" {") {
        let name = &debug_string[..first_brace]; // Extract name before `{`
        to_camel_case(name)
    } else {
        to_camel_case(&debug_string) // Directly convert unit variant names
    }
}

fn log_decoded_transaction(
    parsed: &ConfirmedTransactionWithStatusMeta,
    instructions: &[TransactionInstructionWithParent],
    signature: &Signature,
) {
    let sig = signature.to_string();
    debug!("🔍 Transaction @ Slot {} | Signature: {}", parsed.slot, sig);

    if let TransactionWithStatusMeta::Complete(meta) = &parsed.tx_with_meta {
        if let Some(logs) = &meta.meta.log_messages {
            debug!("📜 Log messages ({}):", logs.len());
            for line in logs {
                debug!("  ▸ {}", line);
            }
        }

        debug!("📘 Decoded Instructions: {}", instructions.len());
        for (i, instr) in instructions.iter().enumerate() {
            debug!(
                "   {}. Program ID: {} | Parent: {:?} | Data len: {}",
                i + 1,
                instr.instruction.program_id,
                instr.parent_program_id,
                instr.instruction.data.len()
            );
        }

        if let Some(pre) = &meta.meta.pre_token_balances {
            debug!("📉 Pre-token balances:");
            for tb in pre {
                debug!(
                    "   - {} [{}] = {}",
                    tb.owner.clone(),
                    tb.mint,
                    tb.ui_token_amount.ui_amount.unwrap_or(0.0)
                );
            }
        }

        if let Some(post) = &meta.meta.post_token_balances {
            debug!("📈 Post-token balances:");
            for tb in post {
                debug!(
                    "   - {} [{}] = {}",
                    tb.owner.clone(),
                    tb.mint,
                    tb.ui_token_amount.ui_amount.unwrap_or(0.0)
                );
            }
        }
    }
}

fn flatten_transaction_response(
    transaction_with_meta: &VersionedTransactionWithStatusMeta,
) -> Vec<TransactionInstructionWithParent> {
    let mut result = Vec::new();
    let transaction = transaction_with_meta.transaction.clone();
    let ci_ixs = transaction.message.instructions();
    let parsed_accounts = parse_transaction_accounts(
        &transaction.message,
        transaction_with_meta.meta.loaded_addresses.clone(),
    );
    let ordered_cii = match &transaction_with_meta.meta.inner_instructions {
        Some(cii) => {
            let mut cii = cii.clone();
            cii.sort_by(|a, b| a.index.cmp(&b.index));
            cii
        }
        _ => Vec::new(),
    };
    let total_calls: usize = ordered_cii
        .iter()
        .fold(ci_ixs.len(), |acc, cii| acc + cii.instructions.len());
    let mut last_pushed_ix = -1;
    let mut call_index: isize = -1;

    for cii in ordered_cii.iter() {
        while last_pushed_ix != cii.index as i64 {
            last_pushed_ix += 1;
            call_index += 1;
            let ci_ix = &ci_ixs[last_pushed_ix as usize];
            result.push(TransactionInstructionWithParent {
                instruction: compiled_instruction_to_instruction(ci_ix, &parsed_accounts),
                parent_program_id: None,
            });
        }

        for cii_entry in &cii.instructions {
            let parent_program_id =
                parsed_accounts[ci_ixs[last_pushed_ix as usize].program_id_index as usize].pubkey;
            let ix = CompiledInstruction {
                program_id_index: cii_entry.instruction.program_id_index,
                accounts: cii_entry.instruction.accounts.clone(),
                data: cii_entry.instruction.data.clone(),
            };
            result.push(TransactionInstructionWithParent {
                instruction: compiled_instruction_to_instruction(&ix, &parsed_accounts),
                parent_program_id: Some(parent_program_id),
            });
            call_index += 1;
        }
    }

    while call_index < (total_calls as isize - 1) {
        last_pushed_ix += 1;
        call_index += 1;
        let ci_ix = &ci_ixs[last_pushed_ix as usize];
        result.push(TransactionInstructionWithParent {
            instruction: compiled_instruction_to_instruction(ci_ix, &parsed_accounts),
            parent_program_id: None,
        });
    }
    result
}

fn compiled_instruction_to_instruction(
    ci: &CompiledInstruction,
    parsed_accounts: &[AccountMeta],
) -> Instruction {
    let program_id = match parsed_accounts.get(ci.program_id_index as usize) {
        Some(am) => am.pubkey,
        None => {
            debug!(
                "program_id_index {} >= parsed_accounts.len()={} ",
                ci.program_id_index,
                parsed_accounts.len()
            );
            Pubkey::default()
        }
    };
    let accounts: Vec<AccountMeta> = ci
        .accounts
        .iter()
        .filter_map(|&index| {
            if let Some(am) = parsed_accounts.get(index as usize) {
                Some(am.clone())
            } else {
                debug!(
                    "account index {} >= parsed_accounts.len()={} ",
                    index,
                    parsed_accounts.len()
                );
                None
            }
        })
        .collect();

    Instruction {
        program_id,
        accounts,
        data: ci.data.clone(),
    }
}

pub fn parse_transaction_accounts(
    message: &VersionedMessage,
    loaded_addresses: LoadedAddresses,
) -> Vec<AccountMeta> {
    let accounts = message.static_account_keys();
    let readonly_signed_accounts_count = message.header().num_readonly_signed_accounts as usize;
    let readonly_unsigned_accounts_count = message.header().num_readonly_unsigned_accounts as usize;
    let required_signatures_accounts_count = message.header().num_required_signatures as usize;
    let total_accounts = accounts.len();

    let mut parsed_accounts: Vec<AccountMeta> = accounts
        .iter()
        .enumerate()
        .map(|(index, pubkey)| {
            let is_writable = index
                < required_signatures_accounts_count - readonly_signed_accounts_count
                || (index >= required_signatures_accounts_count
                    && index < total_accounts - readonly_unsigned_accounts_count);
            AccountMeta {
                pubkey: *pubkey,
                is_signer: index < required_signatures_accounts_count,
                is_writable,
            }
        })
        .collect();

    parsed_accounts.extend(
        loaded_addresses
            .writable
            .into_iter()
            .map(|pubkey| AccountMeta {
                pubkey,
                is_signer: false,
                is_writable: true,
            }),
    );
    parsed_accounts.extend(
        loaded_addresses
            .readonly
            .into_iter()
            .map(|pubkey| AccountMeta {
                pubkey,
                is_signer: false,
                is_writable: false,
            }),
    );
    parsed_accounts
}

#[tokio::main]
async fn main() -> Result<()> {
    // ─── 0) Init ───
    dotenv().ok();
    env::set_var("RUST_LOG", "info");
    env_logger::init();
    let rpc = create_rpc_client().unwrap();
    tx::spawn_blockhash_refresher(rpc.clone());
    if let Ok(hash) = rpc.get_latest_blockhash() {
        *LATEST_BLOCKHASH.lock().await = hash;
        debug!("[blockhash_refresher] new blockhash: {}", hash);
    } else {
        debug!("[blockhash_refresher] failed to fetch blockhash");
    }
    // ─── 1) Channels ───
    let (mint_tx, mint_rx) = mpsc::channel::<BuyOrder>(100);
    let (sell_tx, sell_rx) = mpsc::channel::<SellOrder>(100);

    // ─── 2) Trading loop ───
    let trading_handle = tokio::spawn(start_trading_loop(mint_rx, sell_rx));

    // ─── 3) Shredstream ───
    let endpoint = env::var("SHREDSTREAM_URL")?;
    let shred_mint_tx = mint_tx.clone();
    let shred_sell_tx = sell_tx.clone();
    tokio::spawn(async move {
        if let Err(e) = shred_subscribe_transactions(endpoint, shred_sell_tx, shred_mint_tx).await {
            error!("❌ shredstream error: {:?}", e);
        }
    });

    // ─── 4) Fallback-sell loop ───
    {
        let sell_tx = sell_tx.clone();
        tokio::spawn(async move {
            const FALLBACK_AFTER_SECS: u64 = 25;
            let mut interval = tokio::time::interval(Duration::from_secs(1));
            loop {
                interval.tick().await;
                let now = Instant::now();
                let mut tokens = BOUGHT_TOKENS.lock().await;
                for (mint, entry) in tokens.iter_mut() {
                    let age_ok = entry
                        .buy_executed_at()
                        .map(|t| now.duration_since(t).as_secs() >= FALLBACK_AFTER_SECS)
                        .unwrap_or(false);
                    if age_ok && !entry.sell_triggered() {
                        entry.set_sell_triggered(true);
                        info!("⏰ Fallback‐sell {} after {}s", mint, FALLBACK_AFTER_SECS);
                        let _ = sell_tx
                            .send(SellOrder {
                                mint: mint.clone(),
                                amount: entry.amount(),
                                use_jito: true,
                                urgent: true,
                            })
                            .await;
                    }
                }
            }
        });
    }

    // ─── 6) Wait for shutdown ───
    tokio::select! {
        _ = trading_handle => {
            warn!("Trading loop ended; shutting down.");
        }
        _ = signal::ctrl_c() => {
            info!("SIGINT received; exiting.");
        }
    }

    // ─── 7) Final unwind ───
    {
        let mut outstanding = Vec::new();
        {
            let tokens = BOUGHT_TOKENS.lock().await;
            for (mint, entry) in tokens.iter() {
                if !entry.sell_triggered() {
                    outstanding.push((mint.clone(), entry.amount()));
                }
            }
        }
        for (mint, amount) in outstanding {
            info!("⏏️  Final unwind: selling {} of {}", amount, mint);
            sell_tx
                .send(SellOrder {
                    mint,
                    amount,
                    use_jito: true,
                    urgent: true,
                })
                .await?;
        }
    }

    // ─── 8) Graceful exit ───
    sleep(Duration::from_secs(1)).await;
    info!("Goodbye.");
    Ok(())
}
