import os 
os.system("cls || clear")

data_de_nascimento = int(input("Digite sua data de nascimento: "))

def idade():
    idade_pessoa = 2024 - data_de_nascimento
    print(f"Idade: {idade_pessoa}")

idade()
print("--- FIM ---")        
