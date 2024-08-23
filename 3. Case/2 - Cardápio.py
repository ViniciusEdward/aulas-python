import os
os.system("cls || clear")

print("""
1 - PICANHA | R$ 25,00
2 - LASANHA | R$ 20,00
3 - STROGONOFF | R$ 28,00
4 - BIFE ACEBOLADO | R$ 15,00
5 - PÃO COM OVO | R$ 5,00
      """)

opcao = input("Digite o prato que deseja (1 | 2 | 3 | 4 | 5): ")

match(opcao):
    case "1":
        print("\nPICANHA R$ 25,00")
    case "2":
        print("\nLASANHA R$ 20,00")

    case "3":
        print("\nSTROGONOFF R$ 28,00")

    case "4":
        print("\nBIFE ACEBOLADO R$ 15,00")

    case "5":
        print("\nPÃO COM OVO R$ 5,00")
    case _:
        print("\nOpção inválida")

