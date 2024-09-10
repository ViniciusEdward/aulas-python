import os 
os.system("cls || clear")

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