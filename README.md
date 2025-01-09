# Projeto de Criptografia de Senhas

Este projeto usa o algoritmo SHA-256 para criptografar senhas e verificar se a senha fornecida corresponde à armazenada.

## Como Funciona

- `gerar_hash_senha(senha)`: Gera o hash da senha usando SHA-256.
- `validar_senha(senha, senha_hash_armazenada)`: Compara o hash da senha fornecida com o hash armazenado.

## Requisitos

- Python 3.x

## Exemplo de Uso

```python
import hashlib

def gerar_hash_senha(senha):
    senha_com_hash = hashlib.sha256(senha.encode()).hexdigest()
    return senha_com_hash

def validar_senha(senha, senha_hash_armazenada):
    if gerar_hash_senha(senha) == senha_hash_armazenada:
        return True
    return False

senha_input = "senhaSegura456"
senha_armazenada = gerar_hash_senha(senha_input)

print("Senha criptografada:", senha_armazenada)

senha_tentativa = input("Insira sua senha: ")

if validar_senha(senha_tentativa, senha_armazenada):
    print("Acesso concedido!")
else:
    print("Senha inválida!")
```
