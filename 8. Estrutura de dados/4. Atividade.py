import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
BIBLIOTECA00 = create_engine("sqlite:///biblioteca.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=BIBLIOTECA00)
session = Session()

# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column("Email", String)
    senha = Column("Senha", String)
    cpf = Column("CPF", String)
    data_de_nascimento = Column("Data de nascimento", String)

    # Definindo atributos da classe.
    def __init__(self, email: str, senha:str, cpf:str, data_de_nascimento:str):
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento 

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=BIBLIOTECA00)
def limpar_terminal():
    import os
    os.system("cls || clear")

def biblioteca():
    print("""=== BIBLIOTECA SENAI ===
    1 - Criar cadastro para comprar um livro
    2 - Comprar um livro
    3 - Alugar um livro
    4 - Devolução de um livro
    5 - Estoque de livros
    6 - Carrinho de compras
    0 - Sair do sistema
    (Para comprar/alugar um livro, primeiro faça seu cadastro, depois solicite ver o estoque e coloque o id do livro que deseja)
    """)

def cadastro():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    cpf = input("Digite seu cpf: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")
    novo_usuario = Usuario(email=email, senha=senha, cpf=cpf, data_de_nascimento=data_de_nascimento)
    session.add(novo_usuario)  
    session.commit()
    print("Cadastro realizado com sucesso.")

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = session.query(Usuario).filter(Usuario.email == email, Usuario.senha == senha).first()
    if usuario:
        print(f"Bem-vindo(a), {usuario.email}!")
        return usuario
    else:
        print("E-mail ou senha incorretos. Tente novamente.")
        return None

def calcular_preco(preco, forma_de_pagamento):
    desconto = preco * 0.1
    if forma_de_pagamento == "A":
        return preco - desconto
    return preco + desconto

def compras_de_livros(carrinho, carrinho_de_livros):
    livros = {
        '123': ('Anabele', 150.00),
        '456': ('Chucky', 170.00),
        '789': ('It - A coisa', 190.00),
        '111': ('Diário de um banana', 150.00),
        '112': ('Auto da compadecida', 150.00),
        '113': ('A troca', 150.00),
        '101': ('Romeu e Julieta', 150.00),
        '102': ('Orgulho e preconceito', 150.00),
        '103': ('A culpa é das estrelas', 150.00),
    }

    codigo = input("Digite o código do livro que deseja: ")
    if codigo in livros:
        nome, preco = livros[codigo]
        print(f"Livro escolhido: {nome}")
        print(f"Valor do livro: R$ {preco:.2f}")
        forma_de_pagamento = input("Digite a forma de pagamento(À vista (A) e Crédito (C)): ").upper()
        total_a_pagar = calcular_preco(preco, forma_de_pagamento)
        carrinho.append(total_a_pagar)
        carrinho_de_livros.append(nome)
        print(f"Total à pagar: R$ {total_a_pagar:.2f}")
    else:
        print("Código do livro inválido!")


def alugar_um_livro(carrinho_de_livros):
    livros = {
    '123': ('Anabele'),
    '456': ('Chucky'),
    '789': ('It - A coisa'),
    '111': ('Diário de um banana'),
    '112': ('Auto da compadecida'),
    '113': ('A troca'),
    '101': ('Romeu e Julieta'),
    '102': ('Orgulho e preconceito'),
    '103': ('A culpa é das estrelas'),
}

    codigo = input("Digite o código do livro que deseja: ")
    if codigo in livros:
        nome = livros[codigo]
        print(f"\nLivro à ser alugado: {nome}")
        print("Você tem um mês de aluguel. Após esse um mês, você vai pagar uma taxa de R$5,00 por cada semana de atraso")
        carrinho_de_livros.append(nome)
    else:
        print("Código do livro inválido!")

def devolucao_de_um_livro():
    livros = {
    '123': ('Anabele'),
    '456': ('Chucky'),
    '789': ('It - A coisa'),
    '111': ('Diário de um banana'),
    '112': ('Auto da compadecida'),
    '113': ('A troca'),
    '101': ('Romeu e Julieta'),
    '102': ('Orgulho e preconceito'),
    '103': ('A culpa é das estrelas'),
}

    codigo = input("Digite o código do livro que deseja devolver: ")
    motivo = input("Fale sobre o motivo de sua insatisfação com o livro: ")
    if codigo in livros:
        nome = livros[codigo]
        print(f"\nLivro à ser devolvido: {nome}")
        print("Agradecemos por ter devolvido ao invés de ter jogado fora. Esse livro vai ser doado para pessoas de baixa renda")
    else:
        print("Código do livro inválido!")

def estoque_de_livro():
    print("""
    Estoque de livros:
    Livros de terror: 
    Anabele (123), Chucky (456), It - A coisa (789)
          
    Livros de humor: 
    Diário de um banana (111), Auto da compadecida (112), A troca (113)
          
    Livros de romance: 
    Romeu e Julieta (101), Orgulho e preconceito (102), A culpa é das estrelas (103)
    """)

def exibir_carrinho(carrinho, carrinho_de_livros):
    soma = sum(carrinho)
    for livro in carrinho_de_livros:
        print(f"\nLivros escolhidos: {livro}")
    print(f"Total à pagar: {soma:.2f}")

limpar_terminal()
biblioteca()
carrinho = []
carrinho_de_livros = []
while True:
    opcao = input("\nDigite o que deseja: ")
    match(opcao):
        case '1':
            cadastro()

        case '2':
            login()
            
        case '3':
            compras_de_livros(carrinho, carrinho_de_livros)

        case '4':
            alugar_um_livro(carrinho_de_livros)
            
        case '5':
            devolucao_de_um_livro()
            break
            
        case '6':
            estoque_de_livro()
            
        case '7':
            exibir_carrinho(carrinho, carrinho_de_livros)
            break

        case _:
            print("Saindo do sistema")
            break