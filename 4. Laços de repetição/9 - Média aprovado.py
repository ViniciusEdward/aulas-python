import os
os.system("cls || clear")

parcial = 0

for i in range(3):
    nota = float(input("Digite uma nota: "))
    parcial = parcial + nota


media = parcial / 3

print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("APROVADO")
elif media < 4:
    print("REPROVADO")
else:
    print("RECUPERAÇÃO")

