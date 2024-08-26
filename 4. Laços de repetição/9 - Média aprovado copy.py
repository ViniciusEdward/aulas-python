import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
parcial = 0

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    parcial = parcial + nota


media = parcial / QUANTIDADE_NOTAS

print(f"\nMédia: {media}")

if media >= 7:
    print("APROVADO")
elif media < 4:
    print("REPROVADO")
else:
    print("RECUPERAÇÃO")

