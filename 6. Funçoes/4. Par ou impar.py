import os 
os.system("cls || clear")


def contar_pares_impares():
    pares = 0
    impares = 0
    
    for i in range(6):
        numero = int(input("Digite um número para verificar se é par ou impar: "))
        if numero % 2 == 0:
            pares += 1

        else:
            impares += 1
    
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

contar_pares_impares()
    