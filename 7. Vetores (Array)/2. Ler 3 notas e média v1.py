import os 
os.system("cls || clear")
soma = 0

lista_notas = []

for i in range(3):
    nota = int(input("Dite uma nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma /3    

print("\n=== Exibindo resultados ===")
for i, nota in enumerate(lista_notas):
    print(f"{i+1}ª nota: {nota}")

print(f"Média: {media:.2f}")