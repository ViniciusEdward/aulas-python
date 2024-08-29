import os
os.system("cls || clear")

while True:
    nota = float(input("Digite sua nota: "))
    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior ou menor que 10.")
    else:
        break

print(f"Nota: {nota}")
