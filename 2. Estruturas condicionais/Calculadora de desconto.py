import os
os.system("cls || clear")

# DADOS
valor = int(input("Digite um numero: "))

desconto = (valor * 10) /100
total = valor - desconto
print(f"Desconto: {desconto}")
print(f"Total: {total}")