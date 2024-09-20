import os 
os.system("cls || clear")

pares = 0
impares = 0
positivos = 0
negativos = 0
contador = 0
lista_numeros = []

def verif_pares_impares(lista_numeros):
    pares = 0
    impares = 0
    for cada_numero in lista_numeros:
        if cada_numero % 2 == 0: 
            pares += 1
        else:
            impares += 1
    return pares, impares

def verif_positivos_negativos(lista_numeros):
    positivos = 0
    negativos = 0
    for cada_numero in lista_numeros:
        if cada_numero >0:
            positivos += 1
        else:
            negativos += 1
    return positivos, negativos

while True:
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)
    contador += 1

    if numero == 0:
        break

quantidade_de_pares, quantidade_de_impares = verif_pares_impares(lista_numeros)
quantidade_de_positivos, quantidade_de_negativos = verif_positivos_negativos(lista_numeros)

print("\n=== Exibindo Resultados ===")
print(f"Quantidade de números positivos: {quantidade_de_positivos}")
print(f"Quantidade de números negativos: {quantidade_de_negativos}")
print(f"Quantidade de números pares: {quantidade_de_pares}")
print(f"Quantidade de números impares: {quantidade_de_impares}")
print(f"Quantidade de números inseridos: {contador}")