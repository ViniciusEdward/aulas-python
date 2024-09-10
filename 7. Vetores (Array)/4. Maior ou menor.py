import os 
os.system("cls || clear")

lista_numero = []

for i in range(5):
    nota = int(input(f"Digite a {i+1}ª número: "))
    lista_numero.append(nota)
    
maior_numero = max(lista_numero)
menor_numero = min(lista_numero)

os.system("cls || clear")
for i, nota in enumerate(lista_numero):
    print(f"{i+1}ª nota: {nota}")

print(f"\nMaior: {maior_numero}")
print(f"Menor: {menor_numero}")