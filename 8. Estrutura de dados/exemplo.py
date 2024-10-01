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

# Definindo arquivo para salvar os dados.
nome_arquivo = "Lista_de_alunos_Senai.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_arquivo, "w") as arquivo_alunos:

# Percorrendo vetor 
    for aluno in lista_alunos:
    # Escrevendo no arquivo uma linha de cada vez.
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")
arquivo_alunos.close()
print("\n=== Dados dos alunos salvo com sucesso ===")


# Lendo dados de um arquivo.
lista_alunos = []

print("\n=== Acessando dados de um arquivo ===")
with open(nome_arquivo, "r") as arquivo_origem:
    for linha in arquivo_origem:
        nome, idade = linha.strip().split(",")
        lista_alunos.append(Aluno(nome = nome, idade = int(idade)))

# Fechar conexão com o arquivo.
arquivo_alunos.close()
print("\n=== Exibindo dados dos alunos do arquivo ===")
for aluno in lista_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")