import os 
os.system("cls || clear")

qntd_numeros = 5
lista_numeros = []
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(qntd_numeros):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)
    if numero % 2 == 0: 
        pares += 1
    else:
        impares += 1

    if numero <0:
        negativos += 1
    else:
        positivos += 1

print("\n=== Exibindo Resultados ===")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números impares: {impares}")
print(f"Quantidade de números inseridos: {qntd_numeros}")