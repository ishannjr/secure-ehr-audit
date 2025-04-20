# Secure Decentralized Audit System

## Setup Instructions

1. Deploy the smart contract in `blockchain/AuditLog.sol` using Ganache or Hardhat.
2. Replace the contract address and ABI in `blockchain_interface.py`.
3. Run the Flask server:
   ```
   cd server
   pip install flask web3
   python app.py
   ```
4. Open `client/index.html` in your browser to log events.