import os 
os.system("cls || clear")

def par(n1):
    if n1 % 2 == 0:
        print("Par")
    else:
        print("Impar")
        return par

numero = int(input("Digite um número para verificar se é par ou impar: "))

resposta = par(numero)