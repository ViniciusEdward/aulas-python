import os 
os.system("cls || clear")

lista_numero = []
pares = 0
impares = 0

for i in range(6):
    nota = int(input(f"Digite a {i+1}ª número: "))
    lista_numero.append(nota)
    if nota % 2 == 0:
        pares += 1
    else:
        impares += 1

os.system("cls || clear")
print("=== Exibindo resultado ===")
for i, nota in enumerate(lista_numero):
    print(f"{i+1}ª nota: {nota}")
print(f"\nPares: {pares}")
print(f"Impares: {impares}")