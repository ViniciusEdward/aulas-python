import os
os.system("cls || clear")

# Pedindo dados
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))

# Exibindo
print(f"\nNúmero 1: {numero1}")
print(f"Número 2: {numero2}")

# Resultado final
if (numero1 > numero2):
    print(f"\nMaior:  {numero1}")
    print(f"\nMenor:  {numero2}")

if (numero1 < numero2):
    print(f"\nMaior: {numero2}")
    print(f"\nMenor:  {numero1}")

if (numero1 == numero2):
    print("\nPrimeiro e segundo número são iguais")
