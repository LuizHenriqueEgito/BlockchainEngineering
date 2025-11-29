import json
import datetime
import hashlib

from dataclasses import dataclass, field, asdict


DIFFICULTY = '00000'

type SHA256 = str


@dataclass(slots=True)
class Block:
    index: int
    proof: int
    previous_hash: SHA256
    timestamp: str = field(
        default_factory=lambda: str(datetime.datetime.now().isoformat())
    )

class Blockchain:
    def __init__(self, difficulty: str = DIFFICULTY):
        self.chain: list[Block] = []
        self.create_block(proof=1, previous_hash='0')
        self.difficulty = difficulty

    def create_block(self, proof: int, previous_hash: str) -> Block:
        block = Block(
            index=len(self.chain) + 1,
            proof=proof,
            previous_hash=previous_hash
        )
        self.chain.append(block)
        return block

    @property
    def previous_block(self) -> Block:
        return self.chain[-1]

    def proof_of_work(self, previous_proof: int) -> int:
        new_proof = 1

        while True:
            candidate = f'{new_proof ** 2 - previous_proof ** 2}'.encode()
            hash_operation = hashlib.sha256(candidate).hexdigest()
            if hash_operation.startswith(self.difficulty):
                return new_proof

            new_proof += 1
    
    @staticmethod
    def hash(block: Block) -> SHA256:
        encoded_block = json.dumps(
            asdict(block),
            sort_keys=True
        ).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def chain_valid(self) -> bool:
        for previous, current in zip(self.chain, self.chain[1:]):
            if current.previous_hash != self.hash(previous):
                return False
            delta = f'{current.proof ** 2 - previous.proof ** 2}'.encode()
            condition = (
                hashlib.sha256(delta)
                .hexdigest()
                .startswith(self.difficulty)
            )
            if not condition:
                return False
        return True
    
    def __repr__(self):
        return f"Blockchain(len_chain={len(self.chain)})"
    

def mine_block(blockchain: Blockchain) -> dict:
    previous_block = blockchain.previous_block
    previous_proof = previous_block.proof
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    return {
        "message": "A block has been MINED",
        "block": asdict(block)
    }

def display_chain(blockchain: Blockchain):
    return {
        "length": len(blockchain.chain),
        "chain": [asdict(block) for block in blockchain.chain]
    }

def valid_blockchain(blockchain: Blockchain):
    is_valid = blockchain.chain_valid()
    return {
        "message": "The blockchain is VALID." if is_valid
                   else "The blockchain is NOT VALID."
    }