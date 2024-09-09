import os 
os.system("cls || clear")
"Fazer um programa que solicita o preço de um produto que inflaciona esse preço em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100."

def media():
    soma = 0
    for i in range(2):
        nota = int(input("Digite sua nota: "))
        soma += nota
        media = soma / 2
    print(f"\nMédia: {media}")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    
    

media()
print("--- FIM ---")                          