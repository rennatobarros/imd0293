# Atividade: Blocos

Esta atividade tem como objetivo implementar o modelo de dados responsável por representar um bloco em nosso blockchain, além de implementar o método responsável pela criação destes blocos.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas em sala de aula será realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize o sistema operacional Linux e a  IDE de sua preferência (sugestão: Visual Studio Code).

Ao finalizar a atividade, chame o professor para que seja realizada a avaliação. As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários.

## Descrição

A assinatura do método já está presente na classe `Blockchain`:

```python
@staticmethod
def createBlock(self, nonce=0, previousHash=None)
```
Note que o construtor foi definido, assim como algumas atributos e métodos da classe `Blockchain`:

`chain` : uma lista de blocos, representando o blockchain;
`memPool` : o *memory pool*, responsável por armazenar, temporariamente, transações que aidna não foram incluídas em um bloco;
`createGenesisBlock()` : método responsável por criar o primeiro bloco do blockchain, também conhecido como o bloco Genêsis.

## Dicas

-

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
