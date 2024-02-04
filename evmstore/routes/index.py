from flask import Blueprint, render_template, request, make_response, jsonify
from config import Config
from web3 import Web3

bp = Blueprint("index", __name__, url_prefix="/")

ALCHEMY_API_KEY = Config.ALCHEMY_API_KEY
PRIVATE_KEY = Config.PRIVATE_KEY
ABI = Config.ABI
ADDRESS = Config.ADDRESS
state = Config.STATE


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return make_response(jsonify({"success": True}), 200)
    else:
        web3 = Web3(Web3.HTTPProvider(ALCHEMY_API_KEY))
        contract = web3.eth.contract(address=ADDRESS, abi=ABI)
        data = contract.functions.retrieveData().call()
        state.set_ledger_entries(data)
        return render_template("index.html", data=data)
