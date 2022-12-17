from web3 import Web3
import os

def get_web3_provider():
    RPC_URL = os.getenv("RPC_URL")
    return Web3(Web3.HTTPProvider(RPC_URL))
