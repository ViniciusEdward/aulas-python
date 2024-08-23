import os
os.system("cls || clear")

qntd_parcelas = 0
valor_a_prazo = 0
valor_a_vista = 0

print("""
1 - PAGAMENTO À VISTA
2 - PAGAMENTO À PRAZO
     """)

opcao = input("Escolha a opção: ")

match(opcao):
    case "1":
        print("\nVOCÊ ESCOLHEU PAGAMENTO À VISTA.")
        print("VOCÊ GANHOU 10% DE DESCONTO")
        valor_a_vista = 100 - 10
        print(f"VALOR À VISTA: R${valor_a_vista:.2f}")

    case "2":
        print("\nVOCÊ ESCOLHEU PAGAMENTO À PRAZO.")   
        print("VOCÊ PODE PARCELAR ATÉ 6X")
        qntd_parcelas = int(input("ESCOLHA QUANTAS PARCELAS DESEJA: "))
        valor_a_prazo = 100 / qntd_parcelas
        print(f"VALOR PELO PAGAMENTO À PRAZO: R${valor_a_prazo:.2f}")   

    case _:
        print("\nOpção inválida")

