from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# Node access params
RPC_URL = "http://alice:password@127.0.0.1:18443"

# Function to send a transaction


def send(rpc, addr, data):
    raw_tx = rpc.createrawtransaction(
        [],
        [{addr: 100}, {"data": data}]
    )
    funded_tx = rpc.fundrawtransaction(raw_tx, {"fee_rate": 21})
    signed_tx = rpc.signrawtransactionwithwallet(funded_tx["hex"])

    txid = rpc.sendrawtransaction(signed_tx["hex"])
    return txid

# Function to list all wallets in the wallet directory


def list_wallet_dir(rpc):
    result = rpc.listwalletdir()
    return [wallet['name'] for wallet in result['wallets']]


def main():
    rpc = AuthServiceProxy(RPC_URL)

    # Check connection
    info = rpc.getblockchaininfo()
    print(info)

    # Create or load the wallet
    wallet_name = "testwallet"
    wallets = list_wallet_dir(rpc)
    if wallet_name not in wallets:
        rpc.createwallet(wallet_name)
    else:
        try:
            rpc.unloadwallet(wallet_name)
        except JSONRPCException:
            pass
        rpc.loadwallet(wallet_name)

    # Generate a new address
    rpc = AuthServiceProxy(f"{RPC_URL}/wallet/{wallet_name}")

    address = rpc.getnewaddress()

    # Mine 201 blocks to the new address to activate the wallet with mined coins
    rpc.generatetoaddress(103, address)

    # Prepare a transaction to send 100 BTC
    addr_to_receive = "bcrt1qq2yshcmzdlznnpxx258xswqlmqcxjs4dssfxt2"
    op_return = "We are all Satoshi!!".encode().hex()

    # Send the transaction
    txid = send(rpc, addr_to_receive, op_return)

    # Write the txid to out.txt
    with open("out.txt", "w") as f:
        f.write(txid + "\n")


if __name__ == "__main__":
    main()
