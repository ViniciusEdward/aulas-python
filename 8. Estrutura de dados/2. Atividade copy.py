import os
os.system("cls || clear")

# Estrutura de dados.
lista_familia = []
lista_salario = []
contador = 0

def mediafilhos(n1, n2):
    return n1 / n2 

def mediasalario(n1, n2):
    return n1 / n2 

def maiorsalario(n1):
    return max(n1) 

def menorsalario(n1):
    return min(n1)

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
            qntd_filhos = int(input("Quantos filhos você tem: "))
            salario = float(input("Diga quanto você ganha: "))

            contador += 1
            lista_familia.append(qntd_filhos)
            lista_salario.append(salario)

        case "E":
            maior_salario = maiorsalario(lista_salario)
            menor_salario = menorsalario(lista_salario)
            soma_salario = sum(lista_salario)
            soma_filhos = sum(lista_familia)
            media_filhos = mediafilhos(soma_filhos, contador)
            media_salario = mediasalario(soma_salario, contador)
            print(f"Total de famílias que responderam a pesquisa: {contador}")
            print(f"Média do salário da população: R${media_salario:.2f}")
            print(f"Média do número de filhos: {media_filhos:.2f}")
            print(f"Maior salário: R${maior_salario:.2f}")
            print(f"Menor salário: R${menor_salario:.2f}")
            break

        case "S":
            print("Você selecionou a opção de saída")
            break

        case _:
            print("Opção inválida")

# Definindo arquivo para salvar os dados.
nome_do_arquivo = "pesquisa_prefeitura.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "w") as arquivo_familia:
    # Percorrendo vetor/lista.
    for i in range(1):
        #Escrevendo no arquivo uma linha de cada vez.
        arquivo_familia.write(f"""
Total de famílias que responderam: {contador} 
Média salarial: {media_salario:.2f} 
Média do número de filhos: {media_filhos:.2f}
Maior salário: R${maior_salario:.2f} 
Menor salário: R${menor_salario:.2f}""")

arquivo_familia.close()

