import os
os.system("cls || clear")

def calculo_peso(n1,n2):
    calculo = n1 / (pow(n2, 2))

def peso():

    if imc < 18.5:
        print("\nAbaixo do peso.")
        print("Consulte um nutricionista.")

    elif imc > 18.5 and imc < 24.99:
        print("\nPeso normal.")
        print("Mantenha hábitos saúdaveis.")

    elif imc > 25 and imc < 29.99:
        print("\nSobrepeso.")
        print("Dieta balanceada e atividade física.")

    elif imc > 30 and imc < 34.99:
        print("\nObesidade grau 1.")
        print("Procure orientação de um profissional de saúde.")

    elif imc > 35 and imc < 39.99:
        print("\nObesidade grau 2.")
        print("Consulte um médico para a avaliação e orientação.")

    elif imc >40:
        print("\nObesidade grau 3.")
        print("Busque assitência médica imediatamente.")

peso = 

pesokg = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
print(f"IMC: {imc:.2f}")

peso()