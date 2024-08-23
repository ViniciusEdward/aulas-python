import os
os.system("cls || clear")

soma = 0

for i in range(5):
    nota = int(input("Digite uma nota: "))
    soma = soma + nota
print(f"Soma = {soma}")