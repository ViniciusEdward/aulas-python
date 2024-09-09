import os
os.system("cls || clear")

soma = 0
for i in range(3):
    nota = float(input("Digite sua nota: "))
    soma += nota

def media():
        media = soma / 3
        print(f"\nMédia: {media:.2f}")
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")
    
media()
print("--- FIM ---")                          