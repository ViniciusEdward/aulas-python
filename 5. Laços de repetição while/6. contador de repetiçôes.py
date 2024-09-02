import os
os.system("cls || clear ")

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador += 1

    resposta = input("Deseja inserir mais uma nota: ").upper()

    if resposta == "N":
        break

media = nota / contador
print(f"Média: {media:.2f}")    

