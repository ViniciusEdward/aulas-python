import os
os.system("cls || clear")

nota = float(input("Digite sua nota: "))

while nota < 0 or nota > 10:
    print("A nota deve ser maior ou menor que 10.")
    nota = float(input("Digite sua nota: "))

print(f"Nota: {nota}")
