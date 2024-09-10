import os 
os.system("cls || clear")

lista_notas = []

for i in range(3):
    nota = int(input("Dite uma nota: "))
    lista_notas.append(nota)

print(f"\nLista: {lista_notas}")

for i, nota in enumerate(lista_notas):
    print(f"{i+1}ª nota: {nota}")