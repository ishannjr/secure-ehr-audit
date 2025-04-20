from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

address = "0x7F8cf765ecb16DFF7be0CF00f3B58CB48279EA1f"  # Replace with deployed address
abi =    [
  {
    anonymous: false,
    inputs: [ [Object], [Object], [Object], [Object] ],
    name: 'RecordAdded',
    type: 'event'
  },
  {
    inputs: [ [Object] ],
    name: 'records',
    outputs: [ [Object], [Object], [Object], [Object] ],
    stateMutability: 'view',
    type: 'function',
    constant: true
  },
  {
    inputs: [ [Object], [Object], [Object] ],
    name: 'addRecord',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function'
  },
  {
    inputs: [ [Object] ],
    name: 'getRecord',
    outputs: [ [Object], [Object], [Object], [Object] ],
    stateMutability: 'view',
    type: 'function',
    constant: true
  },
  {
    inputs: [],
    name: 'getRecordCount',
    outputs: [ [Object] ],
    stateMutability: 'view',
    type: 'function',
    constant: true
  }
]

contract = web3.eth.contract(address=address, abi=abi)
account = web3.eth.accounts[0]

def add_audit_record(patient_id, user_id, action):
    tx = contract.functions.addRecord(patient_id, user_id, action).buildTransaction({
        'from': account,
        'nonce': web3.eth.getTransactionCount(account)
    })
    signed_tx = web3.eth.account.signTransaction(tx, private_key="0xYourPrivateKey")
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)

def get_all_records():
    count = contract.functions.getRecordCount().call()
    records = []
    for i in range(count):
        record = contract.functions.getRecord(i).call()
        records.append({
            "timestamp": record[0],
            "patientId": record[1],
            "userId": record[2],
            "action": record[3]
        })
    return records