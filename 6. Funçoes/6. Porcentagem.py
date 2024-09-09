import os 
os.system("cls || clear")
"Fazer um programa que solicita o preço de um produto que inflaciona esse preço em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100."

def porcentagem():
    numero = int(input("Insira o preço do produto: "))
    if numero >= 100:
        print(f"Valor do produto: R$ {numero * 1.2:.2f}")

    elif numero < 100:
        print(f"Valor do produto: R$ {numero * 1.1:.2f}")

porcentagem()
print("--- FIM ---")                          