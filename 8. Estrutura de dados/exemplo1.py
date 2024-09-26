import os
os.system("cls || clear")
from dataclasses import dataclass
# Estrutura de dados.

@dataclass
class Aluno:
    nome : str
    idade: int

qntd_alunos = 2

lista_alunos = []

for i in range(qntd_alunos):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))  
    )
    lista_alunos.append(aluno)

print("\n=== Exibindo os dados dos alunos ===")
for aluno in lista_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")