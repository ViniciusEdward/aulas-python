import os
os.system("cls || clear")

qntd_de_notas = 2

def media(n1, n2, qntd_de_notas):
    media = (n1 + n2) /qntd_de_notas
    return media

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

media = media(num1, num2, qntd_de_notas)

print(f"Média: {media}")

