import os
os.system("cls || clear")

tentativas_maximas = 3
tentativas = 0
crie_login:str
crie_senha:str

print("""
      1 - Deseja criar login?
      2 - Já tenho uma conta.
      """)

opcao = input("Escolha a opção: ")

match(opcao):
    case "1":
        print("Você escolheu a opção de criar uma conta.")
        crie_login = input("\nCrie um login: ")
        crie_senha = int(input("Crie uma senha: "))

    case "2":
        print("Acesse sua conta.")
        login = "vinicius"
        senha = "0320"
        

    case _: 
        print("\nOpção inválida")


while tentativas < tentativas_maximas:
    login = input("\nDigite seu login: ")
    senha = int(input("Digite sua senha: "))
    if crie_login == login and crie_senha == senha:
        print("Bem vindo!")
        break

    else:
        tentativas += 1
        print("Tente novamente...")

    if tentativas == tentativas_maximas:
        print("Número de tentativas excedido.")
        break
    
    os.system("cls || clear")
