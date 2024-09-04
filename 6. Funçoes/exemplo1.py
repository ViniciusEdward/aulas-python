import os
os.system("cls || clear")

#Funções retorno

def logo_senai():
    os.system("cls || clear")
    print("""
======================
-       SENAI       -
======================""")

os.system("cls || clear")
logo_senai()
nome = input("Digite seu nome: ")

os.system("cls || clear")
logo_senai()
idade = input("Digite sua idade: ")

os.system("cls || clear")
logo_senai()
nota = input("Digite uma nota: ")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Nota: {nota}")
    