import unittest
from bitchain import Bitchain


class TestBitchain(unittest.TestCase):
    """
    A class derived from unittest.TestCase to test the Bitchain class.
    """

    def setUp(self):
        """
        Setup method to initiate the blockchain before each test method is called.
        """
        self.blockchain = Bitchain()

    def test_block_creation(self):
        """
        Test method to ensure that a block is correctly created and added to the chain.
        """
        initial_block_count = len(self.blockchain.chain)
        self.blockchain.new_block(12345)
        self.assertEqual(len(self.blockchain.chain), initial_block_count + 1, "Block was not created")

    def test_transaction_creation(self):
        """
        Test method to ensure that a transaction is correctly created and added to the list of pending transactions.
        """
        initial_transaction_count = len(self.blockchain.pending_transactions)
        self.blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
        self.assertEqual(len(self.blockchain.pending_transactions), initial_transaction_count + 1, "Transaction was not added")

    def test_hashing(self):
        """
        Test method to ensure the hash function produces the correct hash for
        a given block.
        """
        block = {
            'index': 1,
            'timestamp': 0,
            'transactions': [],
            'proof': 100,
            'previous_hash': None,
        }
        expected_hash = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
        self.assertEqual(self.blockchain.hash(block), expected_hash, "Incorrect hash calculation")


if __name__ == '__main__':
    unittest.main()
