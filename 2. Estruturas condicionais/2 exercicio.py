import os
os.system("cls || clear")

# Pedindo dados
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))

# Calculando
soma = numero1 + numero2
produto = numero1 * numero2
media = soma / 2

# Exibindo
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")

if (numero1 > numero2):
    print(f"\nMaior:  {numero1}")

if (numero1 < numero2):
    print(f"\nMaior:  {numero2}")

if (numero1 > numero2):
    print(f"\nMenor: {numero2}")

if (numero1 < numero2):
    print(f"\nMenor:  {numero1}")

if (numero1 == numero2):
    print("\nPrimeiro e segundo número são iguais")
