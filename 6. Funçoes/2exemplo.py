import os
os.system("cls || clear")

def somar(n1, n2):
    soma = n1 + n2
    return soma

primeiro_numero = float(input("Digite um número: "))
segundo_numero = float(input("Digite um número: "))

soma = somar(primeiro_numero, segundo_numero)

print(f"Soma: {soma}")