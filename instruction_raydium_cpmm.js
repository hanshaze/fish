import { Connection, PublicKey } from "@solana/web3.js";
import BN from "bn.js";
import dotenv from "dotenv";
import { getAssociatedTokenAddress } from "@solana/spl-token";

dotenv.config();

const COMMITMENT_LEVEL = "confirmed";
const RAYDIUM_CPMM_PROGRAM = "CPMMoo8L3F4NbTegBCKVNunggL7H1ZpdTHKxQB5qKP1C";

// Function to create Raydium CPMM swapBaseInput instruction (buy)
export async function createRaydiumCPMMSwapBaseInputInstruction(
  payer,
  authority,
  ammConfig,
  poolState,
  inputTokenAccount,
  outputTokenAccount,
  inputVault,
  outputVault,
  inputTokenProgram,
  outputTokenProgram,
  inputTokenMint,
  outputTokenMint,
  observationState,
  amountIn,
  minimumAmountOut
) {
  // Convert amounts to proper format
  const amountInBN = new BN(amountIn);
  const minimumAmountOutBN = new BN(minimumAmountOut);

  // Convert string addresses to PublicKey objects
  const payerPubkey = typeof payer === 'string' ? new PublicKey(payer) : payer;
  const authorityPubkey = typeof authority === 'string' ? new PublicKey(authority) : authority;
  const ammConfigPubkey = typeof ammConfig === 'string' ? new PublicKey(ammConfig) : ammConfig;
  const poolStatePubkey = typeof poolState === 'string' ? new PublicKey(poolState) : poolState;
  const inputTokenAccountPubkey = typeof inputTokenAccount === 'string' ? new PublicKey(inputTokenAccount) : inputTokenAccount;
  const outputTokenAccountPubkey = typeof outputTokenAccount === 'string' ? new PublicKey(outputTokenAccount) : outputTokenAccount;
  const inputVaultPubkey = typeof inputVault === 'string' ? new PublicKey(inputVault) : inputVault;
  const outputVaultPubkey = typeof outputVault === 'string' ? new PublicKey(outputVault) : outputVault;
  const inputTokenProgramPubkey = typeof inputTokenProgram === 'string' ? new PublicKey(inputTokenProgram) : inputTokenProgram;
  const outputTokenProgramPubkey = typeof outputTokenProgram === 'string' ? new PublicKey(outputTokenProgram) : outputTokenProgram;
  const inputTokenMintPubkey = typeof inputTokenMint === 'string' ? new PublicKey(inputTokenMint) : inputTokenMint;
  const outputTokenMintPubkey = typeof outputTokenMint === 'string' ? new PublicKey(outputTokenMint) : outputTokenMint;
  const observationStatePubkey = typeof observationState === 'string' ? new PublicKey(observationState) : observationState;

  // Debug logging for bug fixing
  console.log({
    input: amountInBN.toString(),
    minOut: minimumAmountOutBN.toString(),
    poolState: poolStatePubkey.toBase58(),
    inputVault: inputVaultPubkey.toBase58(),
    outputVault: outputVaultPubkey.toBase58(),
    payer: payerPubkey.toBase58(),
    authority: authorityPubkey.toBase58(),
    ammConfig: ammConfigPubkey.toBase58(),
    inputTokenAccount: inputTokenAccountPubkey.toBase58(),
    outputTokenAccount: outputTokenAccountPubkey.toBase58(),
    inputTokenMint: inputTokenMintPubkey.toBase58(),
    outputTokenMint: outputTokenMintPubkey.toBase58(),
    observationState: observationStatePubkey.toBase58(),
  });

  // Create the instruction structure based on IDL account order
  const instruction = {
    keys: [
      {
        pubkey: payerPubkey, // payer
        isSigner: true,
        isWritable: true, // Changed from false to true based on IDL
      },
      {
        pubkey: authorityPubkey, // authority
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: ammConfigPubkey, // ammConfig
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: poolStatePubkey, // poolState
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: inputTokenAccountPubkey, // inputTokenAccount
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: outputTokenAccountPubkey, // outputTokenAccount
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: inputVaultPubkey, // inputVault
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: outputVaultPubkey, // outputVault
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: inputTokenProgramPubkey, // inputTokenProgram
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: outputTokenProgramPubkey, // outputTokenProgram
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: inputTokenMintPubkey, // inputTokenMint
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: outputTokenMintPubkey, // outputTokenMint
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: observationStatePubkey, // observationState
        isSigner: false,
        isWritable: true,
      },
    ],
    programId: new PublicKey(RAYDIUM_CPMM_PROGRAM),
    data: createSwapBaseInputInstructionData(amountInBN, minimumAmountOutBN),
  };

  return instruction;
}

// Function to create the instruction data for swapBaseInput operation
function createSwapBaseInputInstructionData(amountIn, minimumAmountOut) {
  const swapBaseInputDiscriminator = [143, 190, 90, 218, 196, 30, 51, 222];

  // Convert amounts to little-endian bytes
  const amountInBytes = amountIn.toArray("le", 8);
  const minimumAmountOutBytes = minimumAmountOut.toArray("le", 8);

  // Combine discriminator + amount_in + minimum_amount_out
  const data = [...swapBaseInputDiscriminator, ...amountInBytes, ...minimumAmountOutBytes];

  return Buffer.from(data);
}

// Function to create Raydium CPMM swapBaseOutput instruction (sell)
export async function createRaydiumCPMMSwapBaseOutputInstruction(
  payer,
  authority,
  ammConfig,
  poolState,
  inputTokenAccount,
  outputTokenAccount,
  inputVault,
  outputVault,
  inputTokenProgram,
  outputTokenProgram,
  inputTokenMint,
  outputTokenMint,
  observationState,
  maxAmountIn,
  amountOut
) {
  // Convert amounts to proper format
  const maxAmountInBN = new BN(maxAmountIn);
  const amountOutBN = new BN(amountOut);

  // Convert string addresses to PublicKey objects
  const payerPubkey = typeof payer === 'string' ? new PublicKey(payer) : payer;
  const authorityPubkey = typeof authority === 'string' ? new PublicKey(authority) : authority;
  const ammConfigPubkey = typeof ammConfig === 'string' ? new PublicKey(ammConfig) : ammConfig;
  const poolStatePubkey = typeof poolState === 'string' ? new PublicKey(poolState) : poolState;
  const inputTokenAccountPubkey = typeof inputTokenAccount === 'string' ? new PublicKey(inputTokenAccount) : inputTokenAccount;
  const outputTokenAccountPubkey = typeof outputTokenAccount === 'string' ? new PublicKey(outputTokenAccount) : outputTokenAccount;
  const inputVaultPubkey = typeof inputVault === 'string' ? new PublicKey(inputVault) : inputVault;
  const outputVaultPubkey = typeof outputVault === 'string' ? new PublicKey(outputVault) : outputVault;
  const inputTokenProgramPubkey = typeof inputTokenProgram === 'string' ? new PublicKey(inputTokenProgram) : inputTokenProgram;
  const outputTokenProgramPubkey = typeof outputTokenProgram === 'string' ? new PublicKey(outputTokenProgram) : outputTokenProgram;
  const inputTokenMintPubkey = typeof inputTokenMint === 'string' ? new PublicKey(inputTokenMint) : inputTokenMint;
  const outputTokenMintPubkey = typeof outputTokenMint === 'string' ? new PublicKey(outputTokenMint) : outputTokenMint;
  const observationStatePubkey = typeof observationState === 'string' ? new PublicKey(observationState) : observationState;

  // Debug logging for bug fixing
  console.log({
    maxInput: maxAmountInBN.toString(),
    amountOut: amountOutBN.toString(),
    poolState: poolStatePubkey.toBase58(),
    inputVault: inputVaultPubkey.toBase58(),
    outputVault: outputVaultPubkey.toBase58(),
    payer: payerPubkey.toBase58(),
    authority: authorityPubkey.toBase58(),
    ammConfig: ammConfigPubkey.toBase58(),
    inputTokenAccount: inputTokenAccountPubkey.toBase58(),
    outputTokenAccount: outputTokenAccountPubkey.toBase58(),
    inputTokenMint: inputTokenMintPubkey.toBase58(),
    outputTokenMint: outputTokenMintPubkey.toBase58(),
    observationState: observationStatePubkey.toBase58(),
  });

  // Create the instruction structure based on IDL account order
  const instruction = {
    keys: [
      {
        pubkey: payerPubkey, // payer
        isSigner: true,
        isWritable: true, // Changed from false to true based on IDL
      },
      {
        pubkey: authorityPubkey, // authority
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: ammConfigPubkey, // ammConfig
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: poolStatePubkey, // poolState
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: inputTokenAccountPubkey, // inputTokenAccount
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: outputTokenAccountPubkey, // outputTokenAccount
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: inputVaultPubkey, // inputVault
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: outputVaultPubkey, // outputVault
        isSigner: false,
        isWritable: true,
      },
      {
        pubkey: inputTokenProgramPubkey, // inputTokenProgram
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: outputTokenProgramPubkey, // outputTokenProgram
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: inputTokenMintPubkey, // inputTokenMint
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: outputTokenMintPubkey, // outputTokenMint
        isSigner: false,
        isWritable: false,
      },
      {
        pubkey: observationStatePubkey, // observationState
        isSigner: false,
        isWritable: true,
      },
    ],
    programId: new PublicKey(RAYDIUM_CPMM_PROGRAM),
    data: createSwapBaseOutputInstructionData(maxAmountInBN, amountOutBN),
  };

  return instruction;
}

// Function to create the instruction data for swapBaseOutput operation
function createSwapBaseOutputInstructionData(maxAmountIn, amountOut) {
  // SwapBaseOutput discriminator: [10, 0, 0, 0, 0, 0, 0, 0] - Based on actual transaction data
  const swapBaseOutputDiscriminator = [55, 217, 98, 86, 163, 74, 180, 173];

  // Convert amounts to little-endian bytes
  const maxAmountInBytes = maxAmountIn.toArray("le", 8);
  const amountOutBytes = amountOut.toArray("le", 8);

  // Combine discriminator + max_amount_in + amount_out
  const data = [...swapBaseOutputDiscriminator, ...maxAmountInBytes, ...amountOutBytes];

  return Buffer.from(data);
}

// Helper function to derive PDAs for Raydium CPMM
export function deriveRaydiumCPMMPDAs(token0Mint, token1Mint) {
  let token0MintPubkey = typeof token0Mint === 'string' ? new PublicKey(token0Mint) : token0Mint;
  let token1MintPubkey = typeof token1Mint === 'string' ? new PublicKey(token1Mint) : token1Mint;
  
  // // Sort tokens lexicographically as required by Raydium CPMM
  [token0MintPubkey, token1MintPubkey] = token0MintPubkey.toBase58() < token1MintPubkey.toBase58() 
  ? [token1MintPubkey, token0MintPubkey]
   : [token0MintPubkey, token1MintPubkey];
  
  // Debug logging for PDA derivation
  console.log("PDA Derivation Debug:");
  console.log("token0Mint:", token0MintPubkey.toBase58());
  console.log("token1Mint:", token1MintPubkey.toBase58());

  // Get AMM config (using index 0 for now)
  const [ammConfigId] = getCpmmPdaAmmConfigId(new PublicKey(RAYDIUM_CPMM_PROGRAM), 0);
  console.log("AMM Config ID:", ammConfigId.toBase58());

  // Get pool ID using the correct seeds: ["pool", amm_config_id, mint_a, mint_b]
  const [poolId] = getCpmmPdaPoolId(
    new PublicKey(RAYDIUM_CPMM_PROGRAM),
    ammConfigId,
    token0MintPubkey,
    token1MintPubkey
  );

  console.log("Pool ID:", poolId.toBase58());

  // Get vaults using the correct seeds: ["pool_vault", pool_id, mint]
  const [vaultA] = getPdaVault(new PublicKey(RAYDIUM_CPMM_PROGRAM), poolId, token0MintPubkey);
  const [vaultB] = getPdaVault(new PublicKey(RAYDIUM_CPMM_PROGRAM), poolId, token1MintPubkey);

  // Get observation ID using the correct seeds: ["observation", pool_id]
  const [observationId] = getPdaObservationId(new PublicKey(RAYDIUM_CPMM_PROGRAM), poolId);

  console.log("Vault A:", vaultA.toBase58());
  console.log("Vault B:", vaultB.toBase58());
  console.log("Observation ID:", observationId.toBase58());

  return {
    poolState: poolId,
    token0Vault: vaultA,
    token1Vault: vaultB,
    observationState: observationId,
    baseMint: token0MintPubkey,
    quoteMint: token1MintPubkey,
    ammConfigId: ammConfigId,
  };
}

// Helper functions for PDA derivation (copied from the provided code)
function getCpmmPdaAmmConfigId(programId, index) {
  return PublicKey.findProgramAddressSync(
    [Buffer.from("amm_config"), u16ToBytes(index)],
    programId
  );
}

function getCpmmPdaPoolId(programId, ammConfigId, mintA, mintB) {
  return PublicKey.findProgramAddressSync(
    [Buffer.from("pool"), ammConfigId.toBuffer(), mintA.toBuffer(), mintB.toBuffer()],
    programId
  );
}

function getPdaVault(programId, poolId, mint) {
  return PublicKey.findProgramAddressSync(
    [Buffer.from("pool_vault"), poolId.toBuffer(), mint.toBuffer()],
    programId
  );
}

function getPdaObservationId(programId, poolId) {
  return PublicKey.findProgramAddressSync(
    [Buffer.from("observation"), poolId.toBuffer()],
    programId
  );
}

function u16ToBytes(num) {
  const arr = new ArrayBuffer(2);
  const view = new DataView(arr);
  view.setUint16(0, num, false);
  return new Uint8Array(arr);
}

// Helper function to get context for Raydium CPMM
export async function getContextFromRaydiumCPMM(token0Mint, token1Mint) {
  try {
    // Derive PDAs for Raydium CPMM
    const pdas = deriveRaydiumCPMMPDAs(token0Mint, token1Mint);

    // For Raydium CPMM, we need to fetch pool state and configs
    // This is a simplified version - in practice you'd fetch from on-chain
  return {
      poolState: pdas.poolState,
      token0Vault: pdas.token0Vault,
      token1Vault: pdas.token1Vault,
      observationState: pdas.observationState,
      // You would need to fetch these from on-chain
      ammConfig: "D4FPEruKEHrG5TenZ2mpDGEfu1iUvTiqBxvpU8HLBvC2", // Fetch from on-chain
      authority: "GpMZbSM2GgvTKHJirzeGfMFoaZ8UR2X7F4v8vHTvxFbL", // Fetch from on-chain
    };
  } catch (e) {
    console.error("Failed to fetch context for Raydium CPMM", e);
    throw e;
  }
} 