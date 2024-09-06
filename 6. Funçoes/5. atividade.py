import os 
os.system("cls || clear")


def porcentagem():
    numero = int(input("Insira o preço do produto: "))
    if numero >= 100:
        print(f"Valor do produto: {(numero * 0.2) + numero}")

    elif numero < 100:
        print(f"Valor do produto: {(numero * 0.1) + numero}")

porcentagem()
    