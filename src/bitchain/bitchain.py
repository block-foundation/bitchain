import hashlib
import json
from time import time


class Bitchain:
    """
    A simple Python blockchain implementation for educational purposes.
    """
    def __init__(self):
        """
        Constructor for the Bitchain class. Initializes an empty chain and a
        list of pending transactions.
        Also adds the genesis block to the chain.
        """
        self.chain = []
        self.pending_transactions = []

        # Add the genesis block
        self.new_block(
            previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."  # noqa E501
            proof=100
        )

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block in the blockchain.

        :param proof: The proof returned by the Proof of Work algorithm
        :param previous_hash: Hash of the previous Block in the chain
        :return: New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):
        """
        Returns the last block in the blockchain.

        :return: Block
        """
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions.

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: The amount
        :return: The index of the Block that will hold this transaction
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        self.pending_transactions.append(transaction)

        return self.last_block['index'] + 1

    def hash(self, block):
        """
        Creates a SHA-256 hash of a Block.

        :param block: Block
        :return: str
        """
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


def main():
    """
    Main function to interact with the blockchain.
    """
    blockchain = Bitchain()

    # Add transactions and blocks
    blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
    blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
    blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
    blockchain.new_block(12345)

    blockchain.new_transaction("Mike", "Alice", '1 BTC')
    blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
    blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
    blockchain.new_block(6789)

    # Print the chain
    print("Genesis block: ", blockchain.chain)


if __name__ == '__main__':
    main()
