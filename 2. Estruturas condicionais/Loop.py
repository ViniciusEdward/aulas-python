import os
os.system("cls || clear")

# DADOS
login = "viniciusedward@gmail.com"
senha_salva = "03072007"

# SOLICITANDO LOGIN

while True:     
    usuario = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

# EXIBINDO
    if login == usuario and senha_salva == senha:
        print("Bem vindo!")
        break
    else:
            os.system("cls || clear")
            print("Login ou senha inválidos")
