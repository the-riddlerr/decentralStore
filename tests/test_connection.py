import os
from web3 import Web3
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware
from dotenv import load_dotenv
import json

load_dotenv()

ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

web3 = Web3(Web3.HTTPProvider(ALCHEMY_API_KEY))
account: LocalAccount = Account.from_key(PRIVATE_KEY)
web3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
web3.eth.default_account = account.address

abi = json.loads(
    """[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "string",
				"name": "description",
				"type": "string"
			}
		],
		"name": "DataStored",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			}
		],
		"name": "storeData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "evmstore",
		"outputs": [
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "numberOfEntries",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "retrieveData",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					}
				],
				"internalType": "struct EvmStorage.Data[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]"""
)
address = "0x800E9AD3aCbf7b80a3f2e06Ac5C2B8565dC4c44c"

print(web3.is_connected())
print(web3.eth.block_number)
contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.retrieveData().call())
try:
    tx_hash = contract.functions.storeData(68, "iloveweb3").transact()
    print(web3.eth.wait_for_transaction_receipt(tx_hash)["transactionHash"].hex())
except ValueError as ve:
    print(ve)
balance = web3.eth.get_balance("0xcf677A9701C5453CCD455AC6BE472BC336Ab17c7")
print(web3.from_wei(balance, "ether"))


my_filter = contract.events.DataStored.create_filter(
    fromBlock=0, argument_filters={"amount": 70}
)
print(my_filter.get_new_entries())
