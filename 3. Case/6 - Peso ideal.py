import os
os.system("cls || clear")

print("""
1 - M(MASCULINO)
2 - F(FEMININO)
     """)
    
sexo = input("Escolha o sexo (M ou F): ").upper()

match(sexo):
    case "M":
        altura = float(input("\nQuanto de altura você tem:"))
        formula_m = (72.7 * altura) - 58
        print(f"PESO IDEAL: {formula_m:.2f}")

    case "F":
        altura = float(input("\nQuanto de altura você tem: "))
        formula_f = (62.1 * altura) - 44.7
        print(f"PESO IDEAL: {formula_f:.2f}")
    case _: 
        print("\nOpção inválida") 
    