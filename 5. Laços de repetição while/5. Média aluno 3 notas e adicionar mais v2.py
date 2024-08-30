"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota.
Mostre um menu conforme o descrito abaixo:

S – Inserir mais uma nota;
P – Ver quantas notas foram inseridas;
N – Calcular a média aritmética das notas informadas.

O programa deve mostrar a média aritmética para o usuário.

"""

import os, time
os.system("cls || clear")

soma = 0
quantidade_notas = 0


while True:
     print("""
           1 - S (Adicionar mais uma nota)
           2 - P (Mostrar notas inseridas)
           3 - N (Calcular média)
           """)
     resposta = input("\nDeseja adicionar mais uma nota? (S | P | N): ").upper()
     match(resposta):
        case "S":
            nota = float(input(f"Digite uma nota: "))
            soma += nota
            quantidade_notas +=1

        case "P": 
            if quantidade_notas == 0:
                print("Não foi inseridas notas.\n")
                input("Pressione uma tecla para continuar...")
                time.sleep(3)
            else:
                print(f"Quantidade de notas inseridas: {quantidade_notas} \n")
                input("Pressione uma tecla para continuar...")

        case "N":
            if quantidade_notas == 0:
                print("Não foram inseridas notas. \n")
            else:
                break

        case _:
            print("Opção inválida... \n")
            time.sleep(3)

media = soma / quantidade_notas
print(f"\nMédia: {media:.2f}")
