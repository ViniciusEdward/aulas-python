import os
os.system("cls || clear")

# DADOS
login = "viniciusedward@gmail.com"
senha_salva = "03072007"

# SOLICITANDO LOGIN
usuario = input("Digite seu login: ")
senha = input("Digite sua senha: ")

# EXIBINDO
if login == usuario and senha_salva == senha:
    input("Bem vindo!")
else:
        input("Login ou senha inválidos")


