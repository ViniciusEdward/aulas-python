import os
os.system("cls || clear")

numero = int(input("Escreva um número para exibir a tabuada: "))

for i in range(1,11):
    print(f"{numero} * {i}= {numero * i} ")