import os
os.system("cls || clear")
from dataclasses import dataclass

# Estrutura de dados.
@dataclass
class Aluno:
    nome : str
    sobrenome : str
    idade : int
    peso : float
    altura : float


QNTD_ALUNOS = 2
lista_alunos = []

for i in range(QNTD_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        sobrenome = input("Digite seu sobrenome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    lista_alunos.append(aluno)

# Salvar em um arquivo chamado: carteira_de_clientes.txt
nome_arquivo = "carteira_de_clientes.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_arquivo, "a") as arquivo_alunos:
    # Percorrendo vetor 
    for aluno in lista_alunos:
    # Escrevendo no arquivo uma linha de cada vez.
        arquivo_alunos.write(f"{aluno.nome} {aluno.sobrenome}, {aluno.idade}anos, {aluno.peso}kg, {aluno.altura}m\n")
arquivo_alunos.close()
print("\n=== Dados dos alunos salvo com sucesso ===")


# Lendo dados de um arquivo.
# Limpando a lista de alunos.

# Fechar conexão com o arquivo.
arquivo_alunos.close()
print("\n=== Exibindo dados dos alunos do arquivo ===")
for aluno in lista_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Sobrenome: {aluno.sobrenome}")
    print(f"Idade: {aluno.idade}")
    print(f"Peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")