""""
Escreva um algoritmo que solicite duas notas para um aluno.
Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritmética do aluno.
"""
import os
os.system("cls || clear")

soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite uma nota: "))
        if nota >= 0 and nota <= 10:
            break
    soma += nota
    
media = soma / QUANTIDADE_NOTAS    
print(f"Média: {media}")

