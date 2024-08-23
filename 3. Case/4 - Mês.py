import os
os.system("cls || clear")

print("""
1 - JANEIRO
2 - FEVEREIRO
3 - MARÇO
4 - ABRIL
5 - MAIO
6 - JUNHO
7 - JULHO
8 - AGOSTO
9 - SETEMBRO
10 - OUTUBRO
11 - NOVEMBRO
12 - DEZEMBRO
     """)

opcao = input("Escolha o mês: (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12): ")

match(opcao):
    case "1":
        print("\nVOCÊ ESCOLHEU O MÊS DE JANEIRO.")

    case "2":
        print("\nVOCÊ ESCOLHEU O MÊS DE FEVEREIRO.")

    case "3":
        print("\nVOCÊ ESCOLHEU O MÊS DE MARÇO.")

    case "4":
        print("\nVOCÊ ESCOLHEU O MÊS DE ABRIL.")

    case "5":
        print("\nVOCÊ ESCOLHEU O MÊS DE MAIO.")

    case "6":
        print("\nVOCÊ ESCOLHEU O MÊS DE JUNHO.")

    case "7":
        print("\nVOCÊ ESCOLHEU O MÊS DE JULHO.")

    case "8":
        print("\nVOCÊ ESCOLHEU O MÊS DE AGOSTO.")

    case "9":
        print("\nVOCÊ ESCOLHEU O MÊS DE SETEMBRO.")  
  
    case "1O":
        print("\nVOCÊ ESCOLHEU O MÊS DE OUTUBRO.") 
   
    case "11":
        print("\nVOCÊ ESCOLHEU O MÊS DE NOVEMBRO.")

    case "12":
        print("\nVOCÊ ESCOLHEU O MÊS DE DEZEMBRO.")    

    case _:
        print("\nOpção inválida")