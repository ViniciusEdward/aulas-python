import os
os.system("cls || clear")

soma = 0
soma_adicional = 0

for i in range(3):
    while True:
        nota = float(input(f"Digite {i + 1}º nota: "))
        soma += nota 
        if nota < 0 or nota > 10:
            os.system("cls || clear")
            print("Nota inválida, digite novamente.")
        else:
            break
print("""
1 - S (Adicionar mais uma nota)
2 - P (Mostrar notas inseridas)
3 - N (Calcular média)
     """)
    
adicionar = input("\nDeseja adicionar mais uma nota? (S | P | N): ").upper()

match(adicionar):
    case "S":
        qntd_notas = int(input("Informe a quantidade de notas: "))

        for i in range(qntd_notas):
            while True:
                nota_adicional = float(input(f"\nDigite {i + 4}º nota: "))
                soma_adicional += nota_adicional
                if nota_adicional < 0 or nota_adicional > 10:
                    os.system("cls || clear")
                    print("Nota inválida, digite novamente.")
                else:
                    break
        media = (soma + soma_adicional) / (qntd_notas + 3)
        

    case "P": 
        for i in range(3):
            print(f"Nota: {nota:.2f}")
            media = soma / 3
            soma += nota

    case "N":
        media = soma / 3
        soma += nota

print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("Parabéns, você está aprovado!")
elif media >= 5 and media < 7:
    print("Infelizmente você não conseguiu a atingir a nota esperada. Recuperação")
elif media < 5:
    print("Sinto muito. Reprovado")