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
//... other logic Please contact to @hanshaze  thanks