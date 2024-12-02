from web3 import Web3
import json
import time

# Connect to the Ganache blockchain
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
assert web3.is_connected(), "Failed to connect to Ethereum network"

# Set default account from Ganache
web3.eth.default_account = web3.eth.accounts[0]

# Load the contract ABI (replace this with your own ABI)
contract_abi = json.loads('''[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_uniqueID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_hashCode",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_unlockTime",
				"type": "uint256"
			}
		],
		"name": "storeHashCode",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_uniqueID",
				"type": "string"
			}
		],
		"name": "getUnlockTime",
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
		"inputs": [
			{
				"internalType": "string",
				"name": "_uniqueID",
				"type": "string"
			}
		],
		"name": "hashCodeExists",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "hashcodes",
		"outputs": [
			{
				"internalType": "string",
				"name": "hashCode",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "unlockTime",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_uniqueID",
				"type": "string"
			}
		],
		"name": "revealHashCode",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]''')  # Replace with your contract ABI

# Contract address (replace this with your deployed contract's address)
contract_address = "0xB02140ebd675A7Fe8aaBB7ed1e3081Eadd89023d"  # Replace with actual address

# Initialize the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Example data to store
# unique_id = "x1"
# hash_code = "0x123abdd..."  # Example hashcode
# unlock_time = int(time.time()) + 120  # Unlock in 2 minutes

# # Store hash code
def store_hash(unique_id, hash_code, unlock_time):
    try:
        tx_hash = contract.functions.storeHashCode(unique_id, hash_code, unlock_time).transact({'gas': 500000})
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction successful! Hash stored with ID '{unique_id}' and unlock time {unlock_time}")
    except Exception as e:
        print(f"Error storing hash: {e}")

# Retrieve unlock time



def retrive_hash(unique_id):
    unlock_time_for_id = contract.functions.getUnlockTime(unique_id).call()
    print(f"Unlock time for hashcode with ID '{unique_id}': {unlock_time_for_id}")
    if time.time() >= unlock_time_for_id:
        revealed_hash = contract.functions.revealHashCode(unique_id).call()
        print(f"Revealed hashcode for ID '{unique_id}': {revealed_hash}")
        return revealed_hash
    else:
        print("Hashcode is still locked.")
        return None
  
		
	
	
		
	
    # unlock_time_for_id = contract.functions.getUnlockTime(unique_id).call()
    # if time.time() >= unlock_time_for_id:
    #     revealed_hash = contract.functions.revealHashCode(unique_id).call()
    #     print(f"Revealed hashcode for ID '{unique_id}': {revealed_hash}")
    #     return revealed_hash
    # else:
    #     print("Hashcode is still locked.")
    #     return None
    # exists = contract.functions.hashCodeExists(unique_id).call()
    # if exists:
    #     print(f"Hash code with ID '{unique_id}' exists.")
    # else:
    #     print(f"Hash code with ID '{unique_id}' does not exist.")
    # if exists:
    #     unlock_time_for_id = contract.functions.getUnlockTime(unique_id).call()
    #     print(f"Unlock time for hashcode with ID '{unique_id}': {unlock_time_for_id}")
    # else:
    #     print(f"No unlock time for '{unique_id}' because the ID does not exist.")
	
     

    
	
	# Get unlock time if exists
	
		
 	
d = retrive_hash('q1')	
print(d)	
# 

# store_hash('x1', 'xxxxxxxxxx', 1730505605)
		
	
		