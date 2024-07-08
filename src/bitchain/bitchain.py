# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Bitchain Class
=======================

A simple Python blockchain implementation for educational purposes.

Links:
    - None currently provided.

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
import hashlib
import json
from time import time
from typing import Any, Dict, List, Optional

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class Bitchain:
    """
    Bitchain Class
    ==============

    A simple Python blockchain implementation for educational purposes.

    Attributes:
        _chain (List[Dict[str, Any]]): A list of blocks which make up the
            chain.
        _pending_transactions (List[Dict[str, Any]]): A list of transactions
            that are pending to be added to the blockchain.

    """

    # Constructor
    # =========================================================================

    def __init__(self) -> None:
        """
        Constructor for the Bitchain class, initializing the blockchain with
        the genesis block.
        """
        self._chain: List[Dict[str, Any]] = []
        self._pending_transactions: List[Dict[str, Any]] = []

        # Add the genesis block
        self.new_block(
            previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks",  # noqa E501
            proof=100
        )

    # Properties
    # =========================================================================

    @property
    def chain(self) -> List[Dict[str, Any]]:
        """
        Getter for the blockchain's chain.

        Returns:
            List[Dict[str, Any]]: The blockchain's chain.
        """
        return self._chain

    @chain.setter
    def chain(self, value: List[Dict[str, Any]]) -> None:
        """
        Setter for the blockchain's chain.

        Parameters:
            value (List[Dict[str, Any]]): The new value of the blockchain's
                hain.
        """
        self._chain = value

    @chain.deleter
    def chain(self) -> None:
        """
        Deleter for the blockchain's chain, which resets the chain to an
        empty list.
        """
        self._chain = []

    @property
    def pending_transactions(self) -> List[Dict[str, Any]]:
        """
        Getter for the blockchain's pending transactions.

        Returns:
            List[Dict[str, Any]]: The blockchain's pending transactions.
        """
        return self._pending_transactions

    @pending_transactions.setter
    def pending_transactions(self, value: List[Dict[str, Any]]) -> None:
        """
        Setter for the blockchain's pending transactions.

        Parameters:
            value (List[Dict[str, Any]]): The new value of the blockchain's
                pending transactions.
        """
        self._pending_transactions = value

    @pending_transactions.deleter
    def pending_transactions(self) -> None:
        """
        Deleter for the blockchain's pending transactions, which clears all
        pending transactions.
        """
        self._pending_transactions = []

    @property
    def last_block(self) -> Dict[str, Any]:
        """
        Returns the last block in the blockchain.

        Returns:
            Dict[str, Any]: The last block in the chain.
        """
        return self.chain[-1]

    # Methods
    # =========================================================================

    def new_block(
        self,
        proof: int,
        previous_hash: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Creates a new block and adds it to the chain.
        """
        block: Dict[str, Any] = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the list of pending transactions
        self.pending_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(
        self,
        sender: str,
        recipient: str,
        amount: str
    ) -> int:
        """
        Adds a new transaction to the list of pending transactions.

        Parameters:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (str): The amount being transacted.

        Returns:
            int: The index of the block that will hold this transaction.
        """
        transaction: Dict[str, Any] = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }

        self.pending_transactions.append(transaction)

        return self.last_block['index'] + 1

    def hash(self, block: Dict[str, Any]) -> str:
        """
        Creates a SHA-256 hash of a block.

        Parameters:
            block (Dict[str, Any]): A block.

        Returns:
            str: The hex digest of the hash.
        """
        block_string: str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


# =============================================================================
# Module exports
# =============================================================================

__all__ = [
    "Bitchain",
]


# =============================================================================
# Main
# =============================================================================

def main() -> None:
    """
    Main function to interact with the blockchain.
    """
    blockchain = Bitchain()

    # Adding transactions and blocks
    blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
    blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
    blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
    blockchain.new_block(12345)

    blockchain.new_transaction("Mike", "Alice", '1 BTC')
    blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
    blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
    blockchain.new_block(6789)

    # Printing the chain
    print("Genesis block: ", blockchain.chain)


if __name__ == "__main__":
    main()
