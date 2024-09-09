import os 
os.system("cls || clear")
"Fazer um programa que solicita o preço de um produto que inflaciona esse preço em 10% se ele for menor que 100 e em 20% se ele for maior ou igual a 100."


nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma nota: "))

def notas(n1,n2):
    media = (n1 + n2) / 2
    return media
   
    
    
def resultado(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    return media
    
media = notas(nota1, nota2)

print(f"\nMédia: {media}")
resultado = resultado(media)
print("--- FIM ---")                          