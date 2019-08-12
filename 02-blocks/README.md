# Atividade: Blocos

Esta atividade tem como objetivo implementar o modelo de dados responsável por representar um bloco em nosso blockchain, além de implementar o método responsável pela criação destes blocos.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas em sala de aula será realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize o sistema operacional Linux e a  IDE de sua preferência (sugestão: Visual Studio Code).

Ao finalizar a atividade, chame o professor para que seja realizada a avaliação. As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários.

## Descrição

A estrutura para representar um bloco deve seguir o seguinte modelo:

```json
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'nonce': 324984774000,
    'merkleRoot': "13c8bbf1dde38d5f86bfc48a5c027df0d8eb19c8a647de49976755e1b35b31ca",
    'previousHash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```

Onde:

- `index`: índice do bloco, que representa a profundidade do bloco no blockchain (o bloco genesis tem `index` 0);
- `timestamp` : data (formato unix) de criação do novo bloco;
- `transactions` : lista de transações incluídas no bloco;
- `nonce` : por enquanto pode deixar esse atributo com valor 0;
- `merkleRoot` : por enquanto pode deixar esse atributo com valor 0;
- `previousHash` : *hash* do cabeçalho do bloco anterior. O cabeçalho é formado pelos campos `index`, `timestamp`, `nonce`, `merkelRoot` e `previousHash`.

A assinatura do método já está presente na classe `Blockchain`:

```python
@staticmethod
def createBlock(self, nonce=0, previousHash=None)
```
Note que o construtor foi definido, assim como algumas atributos e métodos da classe `Blockchain`:

- `chain` : uma lista de blocos, representando o blockchain;
- `memPool` : o *memory pool*, responsável por armazenar, temporariamente, transações que aidna não foram incluídas em um bloco;
- `createGenesisBlock()` : método responsável por criar o primeiro bloco do blockchain, também conhecido como o bloco Genêsis.

## Dicas

-

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
