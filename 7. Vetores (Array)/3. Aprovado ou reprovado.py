import os 
os.system("cls || clear")
soma = 0

lista_notas = []

for i in range(4):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma /4   

os.system("cls || clear")
print("=== Exibindo resultados ===")
for i, nota in enumerate(lista_notas):
    print(f"{i+1}ª nota: {nota}")

print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
elif media < 5:
    print("Reprovado")
    