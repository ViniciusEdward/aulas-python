import os 
os.system("cls || clear")
pares = 0
impares = 0
lista_numero = []

def verificar_pares_impares(notas):
    qntd_pares = 0
    qntd_impares = 0

    for nota in notas:
        if nota % 2 == 0:
            qntd_pares += 1
        else:
            qntd_impares += 1
    return qntd_impares, qntd_pares

for i in range(6):
    nota = int(input(f"Digite a {i+1}ª número: "))
    lista_numero.append(nota)

os.system("cls || clear")
print("=== Exibindo resultado ===")
for i, nota in enumerate(lista_numero):
    print(f"{i+1}ª nota: {nota}")
pares, impares = verificar_pares_impares(lista_numero)
print(f"Pares: {pares}")
print(f"Impares: {impares}")