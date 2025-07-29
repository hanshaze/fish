
import { pump_geyser } from "./main.js";
import { getBalance } from "./swap.js";
import dotenv from "dotenv";
import { decodePrivateKey } from "./encode_decode_wallet.js";
import readlineSync from 'readline-sync';
dotenv.config()
const encodedPrivateKey = process.env.ENCODED_PRIVATE_KEY; // or load from file
if (!encodedPrivateKey) {
  console.error("Error: ENCODED_PRIVATE_KEY is not set in environment variables.");
  process.exit(1);
}

let password;
try {
  password = readlineSync.question('Enter bot password: ', { hideEchoBack: true });
} catch (err) {
  console.error("Error reading password input:", err.message);
  process.exit(1);
}

let decodedPrivateKeyTemp;
try {
  decodedPrivateKeyTemp = decodePrivateKey(encodedPrivateKey, password);
  if (!decodedPrivateKeyTemp) {
    throw new Error("Decoded private key is empty or invalid.");
  }
} catch (err) {
  console.error("Error decoding private key:", err.message);
  process.exit(1);
}
export const decodedPrivateKey = decodedPrivateKeyTemp;
// console.log(decodedPrivateKey)
// getBalance()
pump_geyser()

