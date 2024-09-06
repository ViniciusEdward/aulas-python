import os 
os.system("cls || clear")

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))

def somar(n1, n2):
        soma = n1 + n2
        return soma

def subtracao_dos(n3, n4):
        subtracao = n3 - n4
        return subtracao

def tabuada_numeros(n5, n6):
        multiplicacao = n5 * n6
        return multiplicacao

def divisao_dos(n7, n8):
        divisao = n7 / n8
        return divisao

soma = somar(numero1, numero2)
subtracao = subtracao_dos(numero1, numero2)
multiplicacao = tabuada_numeros(numero1, numero2)
divisao = divisao_dos(numero1, numero2)

print(f"\nSoma: {soma:.2f}")
print(f"Subtração: {subtracao:.2f}")
print(f"Multiplicação: {multiplicacao:.2f}")
print(f"Divisão: {divisao:.2f}")

        
