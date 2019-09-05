import hashlib
import json
from time import time
import copy

DIFFICULTY = 4 # Quantidade de zeros (em hex) iniciais no hash válido.

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        self.createBlock(previousHash='0'*64, nonce=0)
        self.mineProofOfWork(self.prevBlock) 

    def createBlock(self, nonce=0, previousHash=None):
        if (previousHash == None):
            previousBlock = self.chain[-1]
            previousBlockCopy = copy.copy(previousBlock)
            previousBlockCopy.pop("transactions", None)

        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time()),
            'transactions': self.memPool,
            'merkleRoot': '0'*64,
            'nonce': nonce,
            'previousHash': previousHash or self.generateHash(previousBlockCopy),
        }

        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, prevBlock):
        # TODO Implemente seu código aqui.
        nonce = 0
        while True:
            nonce += 1
            valid = Blockchain.isValidProof(prevBlock, nonce)
            if valid:
                break

    @staticmethod
    def isValidProof(block, nonce):
        # TODO Implemente seu código aqui.
        meta = str('0'*(DIFFICULTY-1)+'1'+'0'*(64-DIFFICULTY))

        block['nonce'] = nonce
        block_hash = Blockchain.getBlockID(block)

        return (block_hash < meta)

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        # TODO Implemente seu código aqui.
        b = copy.deepcopy(block)
        b.pop('transactions')
        return Blockchain.generateHash(b)

    def printChain(self):
        # Mantenha seu método de impressão do blockchain feito na prática passada.
        for b in reversed(self.chain):
            
            self_hash = Blockchain.getBlockID(b)

            print(' ________________________________________________________________ ')
            print('| {} |'.format(self_hash))
            print('----------------------------------------------------------------- ')
            print('| Indíce:', block['index'])
            print('| Timestamp: ', block['timestamp'])
            print('| Nonce: ', block['nonce'])
            print('| merkleRoot: ', block['merkleRoot'])
            print('| previousHash: ', block['previousHash'])
            print('| ==================================================================================\n\n')

    @property
    def prevBlock(self):
        return self.chain[-1]

# Teste
blockchain = Blockchain()
for x in range(0, 4): 
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)

for x in blockchain.chain :
    print('[Bloco #{} : {}] Nonce: {} | É válido? {}'.format(x['index'], Blockchain.getBlockID(x), x['nonce'], Blockchain.isValidProof(x, x['nonce'])))

