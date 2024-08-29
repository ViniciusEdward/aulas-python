""""
Escreva um algoritmo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritmética do aluno.
"""
import os
os.system("cls || clear")

while True:
    primeira_nota = float(input("Digite a primeira nota: "))
    segunda_nota = float(input("Digite a segunda nota: "))
    if (primeira_nota < 0 or primeira_nota > 10) or (segunda_nota < 0  or segunda_nota > 10):
        print("\nA nota deve ser maior ou menor que 10.")
    else:
        break
media = (primeira_nota + segunda_nota) /2
print(f"Média: {media}")


