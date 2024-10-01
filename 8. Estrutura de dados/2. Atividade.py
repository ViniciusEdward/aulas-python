import os
os.system("cls || clear")
from dataclasses import dataclass

# Estrutura de dados.
@dataclass
class Familia:
    qntd_filhos : int
    #media_filhos : int

@dataclass
class Salario:
    salario : int
    #media_salario : int
    

QNTD_FAMILIARES = 1
lista_familia = []
lista_salario = []
contador = 0

while True :
    print("""
        \t=== MENU ===
        A - Adicionar família
        E - Exibir resultados
        S - Sair  
          """)
   
    resposta = input("Deseja inserir mais uma família: ").upper()
   
    match resposta:
        case "A":
            familia = Familia(
                qntd_filhos = int(input("Quantos filhos você tem: "))
                
                )
            salariofamilia = Salario(
                salario = float(input("Diga quanto você ganha: "))
            )
            contador += 1
            lista_familia.append(familia)
            lista_salario.append(salariofamilia)

        case "E":
            maior_salario = max(lista_salario)
            menor_salario = min(lista_salario)
            print(f"Maior salário: {maior_salario}")
            print(f"Menor salário: {menor_salario}")
            print(f"Total de famílias que responderam a pesquisa: {contador}")
            break

        case "S":
            print("Você selecionou a opção de saída")
            break

        case _:
            print("Opção inválida")

# Definindo arquivo para salvar os dados.
#nome_do_arquivo = "pesquisa_prefeitura.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
#with open(nome_do_arquivo, "a") as arquivo_familia:
    # Percorrendo vetor/lista.
    #for familia in lista_familia, lista_salario:
        # Escrevendo no arquivo uma linha de cada vez.
        #arquivo_familia.write(f"\n")

#arquivo_familia.close()

