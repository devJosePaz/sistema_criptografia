import hashlib

# Função para gerar o hash da senha
def gerar_hash_senha(senha):
    # Gerando o hash usando o algoritmo SHA-256
    senha_com_hash = hashlib.sha256(senha.encode()).hexdigest()
    return senha_com_hash

# Função para validar a senha
def validar_senha(senha, senha_hash_armazenada):
    # Gerando o hash da senha fornecida e comparando com o armazenado
    if gerar_hash_senha(senha) == senha_hash_armazenada:
        return True
    return False

# Simulando o armazenamento da senha
senha_input = "senhaSegura948"
senha_armazenada = gerar_hash_senha(senha_input)

# Exibindo a senha criptografada
print("Senha criptografada:", senha_armazenada)

# Testando a validação
senha_tentativa = input("Insira sua senha: ")

if validar_senha(senha_tentativa, senha_armazenada):
    print("Acesso concedido!")
else:
    print("Senha inválida!")
