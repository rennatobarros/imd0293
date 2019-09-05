<<<<<<< HEAD
import hashlib, json, time, copy
=======
import hashlib
import json
>>>>>>> 6a23b129ed4351568f66539346af53902062300a

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        # Implemente aqui o método para gerar o bloco Genesis, invocado no construtor da classe,
        # chamando o método createBlock() previamente implementado.
<<<<<<< HEAD
        self.createBlock() 

    def createBlock(self):
        # Implemente aqui o método para retornar um bloco (formato de dicionário)
        # Lembre que o hash do bloco anterior é o hash na verdade do CABEÇALHO do bloco anterior.
        if self.chain:
            previous_block = copy.deepcopy(self.chain[-1])
            previous_block.pop('transactions')
            previousHash = self.generateHash(previous_block)
        else:
            previousHash = '0000000000000000000000000000000000000000000000000000000000000000'

        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time.time()),
            'nonce': 0,
            'merkleRoot': 0000000000000000000000000000000000000000000000000000000000000000,
            'previousHash': previousHash,
            'transactions': []
        }

        self.chain.append(block)
        return block

    @staticmethod
    def generateHash(data):
        # Implemente aqui seu método para retornar a string referente ao hash SHA256 do argumento passado.
        # Confira a documentação do hashlib: https://docs.python.org/3/library/hashlib.html
        # Note que o argumento passado pode ser um objeto, portanto serialize o argumento antes.
        # Dica: Use o json.dumps() do módulo json.
        data_byte = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(data_byte).hexdigest()

    def printChain(self):
        # Implemente aqui um método para imprimir de maneira verbosa e intuitiva o blockchain atual.
        for b in reversed(self.chain):
            
            block = copy.deepcopy(b)
            block.pop('transactions')
            self_hash = self.generateHash(block)

            print(' ________________________________________________________________ ')
            print('| {} |'.format(self_hash))
            print('----------------------------------------------------------------- ')
            print('| Indíce:', block['index'])
            print('| Timestamp: ', block['timestamp'])
            print('| Nonce: ', block['nonce'])
            print('| merkleRoot: ', block['merkleRoot'])
            print('| Transactions: ', b['transactions'])
            print('| previousHash: ', block['previousHash'])
            print('| ==================================================================================\n\n')


=======
        pass 

    def createBlock(self, nonce=0, previousHash=None):
        # Implemente aqui o método para retornar um bloco (formato de dicionário)
        # Lembre que o hash do bloco anterior é o hash na verdade do CABEÇALHO do bloco anterior.
        pass

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
        # Implemente aqui um método para imprimir de maneira verbosa e intuitiva o blockchain atual.
        pass
>>>>>>> 6a23b129ed4351568f66539346af53902062300a

# Teste
blockchain = Blockchain()
for x in range(0, 3): blockchain.createBlock()
blockchain.printChain()

<<<<<<< HEAD


# Testando sua implementação: espera-se um retorno True.

var1 = {
            'nome': "Jon Snow",
            'idade': 18,
        }
expected_hash1 = "4145c81419ee987c94f741936c3277e9b281e2ffc9faa3edb5693128e1ee65c1"
var1_hash = Blockchain.generateHash(var1)
#print('Dados: {}'.format(var1))
#print('Hash   gerado: {}'.format(var1_hash))
#print('Hash esperado: {}'.format(expected_hash1))
#print('Iguais? {}\n'.format(expected_hash1==var1_hash))
=======
>>>>>>> 6a23b129ed4351568f66539346af53902062300a
