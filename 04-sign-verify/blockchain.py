from hashlib import sha256
import json
from time import time
import copy
from bitcoin.wallet import CBitcoinSecret
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage

DIFFICULTY = 4 

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
        nonce = 0
        while self.isValidProof(prevBlock, nonce) is False:
            nonce += 1

        return nonce

    @staticmethod
    def isValidProof(block, nonce):
        block['nonce'] = nonce
        guessHash = Blockchain.getBlockID(block)
        return guessHash[:DIFFICULTY] == '0' * DIFFICULTY 

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        blockCopy = copy.copy(block)
        blockCopy.pop("transactions", None)
        return Blockchain.generateHash(blockCopy)

    def printChain(self):
        for b in reversed(self.chain):
            
            self_hash = Blockchain.getBlockID(b)

            print(' ________________________________________________________________ ')
            print('| {} |'.format(self_hash))
            print('----------------------------------------------------------------- ')
            print('| Indíce:', b['index'])
            print('| Timestamp: ', b['timestamp'])
            print('| Nonce: ', b['nonce'])
            print('| merkleRoot: ', b['merkleRoot'])
            print('| previousHash: ', b['previousHash'])
            print('| ==================================================================================\n\n')

    @property
    def prevBlock(self):
        return self.chain[-1]

    @staticmethod
    def sign(privKey, message):
        secret = CBitcoinSecret(privKey)
        msg = BitcoinMessage(message)
        return SignMessage(secret, msg)
        
    @staticmethod
    def verifySignature(address, signature, message):
        msg = BitcoinMessage(message)
        return VerifyMessage(address, msg, signature)


# Teste
address = '12bWcU834vZsngj8k5NU5LMAhjUeXnvScR'
privKey = 'L5mwTWz6N43dudRwhaiVhdkRS6sRNf1RsB84xBkCNTwTEVPins2A'

message = 'Bora assinar essa mensagem?'

signature = Blockchain.sign(privKey, message)
print('Assinatura gerada: {}'.format(signature))

print('Assinatura válida para mensagem e endereço indicado? {}'.format(Blockchain.verifySignature(address, signature, message)))
