import hashlib
import time as t
from typing import List

class Blockchain:
    '''
    Chains hash blocks.
    Every next hash is created with use of previous hash in chain. Hence blockchain.
    '''
    def __init__(self) -> None:
        self.blocks = [] # type: List[str]
        self.prevHash = 0

        self.addNewBlock('Hello World!')

    '''
    Turns data into hash block using timestamp, previous hash and
    index of last block in whole blockchain.
    '''
    def hashBlock(self, data: str, timestamp: int, prevHash: str, index: int) -> str:
        hash = ''
        nonce = 0

        # iterate generated hashes untill we get valid one
        while(self.isHashValid(hash) == False):
            input = ''.join([data, str(timestamp), prevHash, str(index), str(nonce)])
            hash = hashlib.sha256(input.encode('utf-8')).hexdigest()
            nonce += 1

        print(nonce)

        return hash

    '''
    Add new data to blockchain as hashed block.
    '''
    def addNewBlock(self, data: str) -> None:
        index = len(self.blocks)
        prevHash = self.lastHash()
        h = self.hashBlock(data, int(t.time()), prevHash, index)
        self.blocks.append(h)

    '''
    Returns last hash in blockchain.
    '''
    def lastHash(self) -> str:
        if len(self.blocks) == 0:
            return ''
        else:
            return self.blocks[-1]

    '''
    Validates hash looking for starting 0's
    '''
    def isHashValid(self, hash: str) -> bool:
        return hash[0:4] == '0'*4 # '0'*difficulty
