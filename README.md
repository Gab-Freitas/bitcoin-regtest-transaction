# bitcoin-regtest-transaction
This repository contains an implementation for creating Bitcoin transactions using Bitcoin Core RPC in regtest mode. The code creates a transaction with two outputs: a 100 BTC payment to a provided address and an OP_RETURN output with the message 'We are all Satoshi!!'. The transaction is created, broadcasted, and the txid is saved to a file.


# Bitcoin RPC Regtest - Transaction with OP_RETURN

This repository contains a solution for creating and sending Bitcoin transactions using Bitcoin Core RPC in regtest mode. The implementation includes the following steps:

- Connect to a Bitcoin Core node in regtest mode via RPC.
- Create a wallet named "testwallet".
- Generate an address from the wallet.
- Mine blocks to that address.
- Send 100 BTC to a provided address, including an OP_RETURN output with the message: "We are all Satoshi!!".
- Set the transaction fee rate to 21 sats/vB.
- Save the transaction ID (txid) to an `out.txt` file.
