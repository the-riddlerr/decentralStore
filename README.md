# Evm Store

- Basic Evm Store
- Go to the deployed link to play with it or setup locally

## What you will need

- Python 3.8 or above
- Create a virtual environment and install the dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

- Create a .env file in the root directory and add the following variables
- `ALCHEMY_API_KEY=Your alchemy api key`
- `PRIVATE_KEY=Your private key`

If you don't have a Private key, the generate one using the following command

```bash
python -c "from web3 import Web3; w3 = Web3(); acc = w3.eth.account.create(); print(f'private key={w3.to_hex(acc.key)}, account={acc.address}')"
```

Your newly created public key will not have any funds so better to get some sepolia eth from alchemy faucet. It's free.

## Running the server locally

- Firstly we need to export some environment variables

```bash
export FLASK_APP=evmstore
export FLASK_ENV=development
```

- Now we can run the server

```bash
flask run
```
