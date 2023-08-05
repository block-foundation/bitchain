# Bitchain: A Simple Blockchain Emulator in Python

## Overview

Bitchain is a simple lockchain emulator written in Python. Aimed at fostering education and understanding of blockchain technologies, Bitchain provides a clear and easy-to-understand interface to interact with a blockchain.

## Key Features

- **Block Creation**: Easily create new blocks with customizable data.
- **Transaction Handling**: Simulate transactions between parties in the blockchain.
- **Chain Validation**: Verify the integrity of the blockchain through hash calculations.
- **Persistence**: Keep a record of transactions until they are incorporated into a block.

## Installation

### Requirements

- Python 3.6 or higher
- Git (optional)

To install Bitchain, clone the repository using Git:

``` sh
git clone https://github.com/username/bitchain.git
cd bitchain
```

or:

``` sh
pip install bitchain
```

see: https://pypi.org/project/bitchain/

You can also download the source code as a zip file and extract it.

## Usage

Once you have the Bitchain code on your local machine, you can run it using Python:

``` sh
python3 main.py
```

Bitchain includes a `main` function that creates a simple blockchain, adds transactions to it, and prints out the entire chain.

## Example

Here's a quick example of creating a blockchain, adding transactions, and creating new blocks:

``` python
blockchain = Bitchain()

blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(12345)

blockchain.new_transaction("Mike", "Alice", '1 BTC')
blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(6789)

print("Genesis block: ", blockchain.chain)
```

## Building

``` py
python3 -m pip install --upgrade build
python3 -m build
```

## Documentation

Please refer to the docstrings in the `Bitchain` class for detailed information on the functionality of each method.

## Contributing

We welcome all contributions to Bitchain! Whether it's bug fixes, feature additions, or documentation improvements, your input is greatly appreciated. Please check the CONTRIBUTING.md file for detailed instructions on how to contribute.
