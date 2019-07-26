# Atividade: Hashing

Esta atividade tem como objetivo implementar o primeiro método no desenvolvimento do nosso **blockchain**. Este método estático será amplamente utilizado em várias etapas do processo, uma vez que *hashing* é uma das técnicas essenciais para o funcionamento deste modelo de blockchain.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar o módulo `hashlib`.

```bash
pip install hashlib
```

## Descrição

A assinatura do método já está presente na classe `Blockchain`:

```python
@staticmethod
def generateHash(data):
```

Importe o módulo `hashlib` a sua classe e implemente o método `generateHash` para retornar a string referente ao *hash* **SHA256** do argumento passado. Note que o argumento passado pode ser um objeto, portanto serialize o argumento antes (veja em *Dicas*).

## Dicas

Confira a documentação do hashlib: [https://docs.python.org/3/library/hashlib.html]

Usar `json.dumps()` do módulo `json` para serializar o objeto antes, e lembrar de manter a estrutura sempre ordenada (`sort_keys=True`).

```python
json.dumps(data, sort_keys=True)
```

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
