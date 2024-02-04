from flask import Blueprint, render_template, request, redirect, make_response, jsonify
from config import Config
from web3 import Web3
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware
from evmstore.views.state import State

bp = Blueprint("add", __name__, url_prefix="/add")

ALCHEMY_API_KEY = Config.ALCHEMY_API_KEY
PRIVATE_KEY = Config.PRIVATE_KEY
ABI = Config.ABI
ADDRESS = Config.ADDRESS
state = Config.STATE


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        web3 = Web3(Web3.HTTPProvider(ALCHEMY_API_KEY))
        account: LocalAccount = Account.from_key(PRIVATE_KEY)
        web3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
        web3.eth.default_account = account.address
        contract = web3.eth.contract(address=ADDRESS, abi=ABI)
        data = contract.functions.retrieveData().call()
        amount = request.form.get("amount")
        description = request.form.get("description")
        try:
            tx_hash = contract.functions.storeData(int(amount), description).transact()
            tx_hash = web3.eth.wait_for_transaction_receipt(tx_hash)[
                "transactionHash"
            ].hex()
        except ValueError as ve:
            return ve
        return render_template("index.html", tx_hash=tx_hash, data=data)
    else:
        return redirect("/")
