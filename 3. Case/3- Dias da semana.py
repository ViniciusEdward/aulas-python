import os
os.system("cls || clear")

print("""
1 - DOMINGO
2 - SEGUNDA-FEIRA
3 - TERÇA-FEIRA
4 - QUARTA-FEIRA
5 - QUINTA-FEIRA
6 - SEXTA-FEIRA
7 - SÁBADO
      """)

opcao = input("Qual dia da semana? (1 | 2 | 3 | 4 | 5 | 6 | 7): ")

match(opcao):
    case "1":
        print("\nDOMINGO | FINAL DE SEMANA")

    case "2":
        print("\nSEGUNDA-FEIRA | DIA ÚTIL")

    case "3":
        print("\nTERÇA-FEIRA | DIA ÚTIL")

    case "4":
        print("\nQUARTA-FEIRA | DIA ÚTIL")

    case "5":
        print("\nQUINTA-FEIRA | DIA ÚTIL")

    case "6":
        print("\nSEXTA-FEIRA | DIA ÚTIL")

    case "7":
        print("\nSÁBADO | FINAL DE SEMANA")

    case _:
        print("\nOpção inválida")