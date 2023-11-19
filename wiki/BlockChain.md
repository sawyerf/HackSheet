<picture>
    <source height="100px" srcset="https://github.com/sawyerf/HackSheet/assets/28403617/3debb8d5-b32d-4310-b82f-36208eae701f#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://github.com/sawyerf/HackSheet/assets/28403617/22329e5d-3b27-41eb-b88c-19671e11c482#gh-light-mode-only">
</picture>

---

- [Web3.py](#web3py)
- [Usefull link](#usefull-link)
  
# Web3.py

Library to interact with Ethereum blockchain:
- [web3.py](https://pypi.org/project/web3/)
- [py-solc-x](https://pypi.org/project/py-solc-x/)
- [solc-select](https://github.com/crytic/solc-select)

### Create new instance of web3.py
> Note: You need to have a RPC_URL to connect to the blockchain

```py
from web3 import Web3

w3_instance = Web3(Web3.HTTPProvider("<RPC_URL>")
assert w3_instance.is_connected()
```

### Get storage at address (usefull to get private variables):
> Note: You need to have a web3 instance (see previous snippet)

```py
storage = w3_instance.eth.get_storage_at("<ADDRESS>", <INT_INDEX>)

# Example:
storage = w3_instance.eth.get_storage_at("0xfce177A183CDff53910b5399Ee3ADcC982c1b5bE", 0)
```

### Get block information:

```py
w3_instance.eth.get_block(<INT_INDEX>, <BOOL_FULL_TRANSACTION>)
w3_instance.eth.get_block(0, True)
```

### Get contract instance:

```py
from solcx import compile_source

contract_code = open("MyContract.sol", "r").read()
compiled = compile_source(
   contract_code,
    output_values=['abi', 'bin']
)

contract_interface = compiled['<stdin>:MyContract']
bytecode = contract_interface['bin']
abi = contract_interface['abi']
contract = w3_instance.eth.contract(address=contract_address, abi=abi, bytecode=bytecode)
```

### Get public variables or view/pure functions:
> Note: You need to have a contract instance (see previous snippet)

```py
contract.functions.solver().call()
```

### Call transact function (my_awesome_function):
> Transact function need to be called with a private key and a caller address

```py
private_key = "<PRIVATE_KEY>"
caller = "<CALLER_ADDRESS>"

Chain_id = w3_instance.eth.chain_id
nonce = w3_instance.eth.get_transaction_count(caller)

tx_data = {"chainId": Chain_id, "from": caller, "nonce": nonce}
call_function = contract.functions.my_awesome_function().build_transaction(tx_data)

signed_tx = w3_instance.eth.account.sign_transaction(call_function, private_key=private_key)
send_tx = w3_instance.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3_instance.eth.wait_for_transaction_receipt(send_tx)
print(tx_receipt)
```

### You can also call payable function you just need to add the value, and gas in the tx_data:
> Note: Gas and gasPrice need to be calculated before.

```py
tx_data = {'nonce': nonce, 'to': contract_address, 'value': 500000000000000000, 'gas': <INT_GAS>, 'gasPrice': <INT_GAS_PRICE> }
```

# Usefull link

- [Etherum transaction vizualiser](https://github.com/avan-pra/graph-blockren)
- [Slither a smart contract analyzer](https://github.com/crytic/slither)
- [Web3.py doc](https://web3py.readthedocs.io/en/stable/quickstart.html)