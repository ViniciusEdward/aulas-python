import os 
os.system("cls || clear")

lista_numero = []

for i in range(5):
    numero = int(input(f"Digite a {i+1}ª número: "))
    if numero <0:
        numero = 0
    lista_numero.append(numero)

os.system("cls || clear")
print("=== Exibindo resultados ===")
for i, numero in enumerate(lista_numero):
    print(f"{i+1}ª numero: {numero}")

for i in range(1):
    print(f"\nLista: {lista_numero}")