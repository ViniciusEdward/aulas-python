import os
os.system("cls || clear")

"Aluno: Vinicius Edward Da Silva Alves Paixão || Turma 93313"

lista_salario = []
lista_sexo = []
lista_idade = []
qntd_masculino = 0
qntd_feminino = 0
qntd_mulheres_salario = 0
contador = 0

def mediasalario(n1, n2):
    return n1 / n2 

while True :
    print("""
        \t=== MENU ===
        A - Adicionar pessoa
        E - Exibir resultados
        S - Sair  
          """)
   
    resposta = input("Escolha uma das opções acima: ").upper()
   
    match resposta:
        case "A":
            sexualidade = input("Digite M (Masculino) ou F para (Feminino): ").upper()
            idade = int(input("Digite sua idade: "))
            salario = float(input("Diga quanto você ganha: "))
            contador += 1
            lista_salario.append(salario)
            lista_idade.append(idade)
            if sexualidade == "M":
                qntd_masculino += 1
            else:
                qntd_feminino += 1

            if sexualidade == "F" and salario >= 5000:
                qntd_mulheres_salario += 1


        case "E":
            soma_salario = sum(lista_salario)
            maior_idade = max(lista_idade)
            menor_idade = min(lista_idade)
            media_salario = mediasalario(soma_salario, contador)
            print(f"\nTotal de pessoas que responderam a pesquisa: {contador}")
            print(f"Média salarial da população: R${media_salario:.2f}")
            print(f"Maior idade do grupo: {maior_idade} anos")
            print(f"Menor idade do grupo: {menor_idade} anos")
            print(f"Quantos homens responderam: {qntd_masculino}")
            print(f"Quantas mulheres responderam: {qntd_feminino}")
            print(f"Mulheres que recebem mais de R$ 5000,00: {qntd_mulheres_salario}")
            break

        case "S":
            print("\nVocê selecionou a opção de saída")
            break

        case _:
            print("Opção inválida")

# Definindo arquivo para salvar os dados.
nome_do_arquivo = "pesquisa_habitantes.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "w") as arquivo_familia:
    # Percorrendo vetor/lista.
    for i in range(1):
        #Escrevendo no arquivo uma linha de cada vez.
        arquivo_familia.write(f"""
Total de famílias que responderam: {contador} 
Média salarial da população: R${media_salario:.2f}
Maior idade do grupo: {maior_idade} anos 
Menor idade do grupo: {menor_idade} anos
Quantos homens responderam: {qntd_masculino} 
Quantas mulheres responderam: {qntd_feminino} 
Mulheres que recebem mais de R$ 5000,00{qntd_mulheres_salario}""")

arquivo_familia.close()

