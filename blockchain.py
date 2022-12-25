# creating a blockchain

import datetime
import json
import hashlib
import time

# from typing import

## building Blockchain


class Blockchain(object):
    """
    Blockchain class
        funciton
            __init__ : initialize the blockchain
            add_block : add a new block to the blockchain
            get_previous_block : get the previous block
            proof_of_work : proof of work
            hash : hash the block
            is_chain_valid : check if the blockchain is valid
    """

    def __init__(self) -> None:
        """
        initialize the blockchain
        """
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def __str__(self) -> str:
        return self.chain

    def hash(self, block) -> str:
        encoded_block = str(json.dumps(block, sort_keys=True)).encode('utf-8')
        hash = hashlib.sha256(encoded_block).hexdigest()
        return hash

    def create_block(self, proof, previous_hash):
        """
        add a new block to the blockchain
        """
        block = {}
        block["index"] = len(self.chain) + 1
        block["timestamp"] = str(datetime.datetime.now())
        block["proof"] = proof
        block["previous_hash"] = previous_hash
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        get the previous block
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        proof of work :
        proof of work is a Consensus Protocols in blockchain used to defined as finding a number such that the hash of the number, it hard to find because it takes a lot of time, and computing power.
        in this case, we are using sha256 hash function, and we are looking for a number such that the hash of the number starts with 4 zeros.
        if the hash of the new proof and the previous proof starts with 4 zeros, then the proof is valid
        and we can add it to the blockchain
        """
        start_time = time.time()
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        elapsed = time.time() - start_time
        print(' time take to get new_proof using pow : ', elapsed)
        return new_proof

    def get_chain(self):
        return self.chain
    
    def get_length(self):
        return len(self.chain)