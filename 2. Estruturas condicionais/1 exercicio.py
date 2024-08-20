import os
os.system("cls || clear")

# Solicitando dados
nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

# Calculando 
media = (nota1 + nota2 + nota3) / 3

# Exibindo
print(f"\nNome: {nome}")
print(f"Idade: {idade} anos")
print(f"Média: {media}")

if media >= 7:
     print("APROVADO")
else:
     print("REPROVADO")




