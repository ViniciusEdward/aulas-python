import os
os.system("cls || clear")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("\nDigite uma nota: "))
        if nota < 0 or nota > 10:
            os.system("cls || clear")
            print("Número inválido, digite um número entre 0 e 10")
        else:
            break

    soma += nota
    
media = soma / QUANTIDADE_NOTAS    
print(f"Média: {media}")

if media >= 7:
    print("Parabéns, você está aprovado!")
elif media >= 5 and media < 7:
    print("Infelizmente você não conseguiu a atingir a nota esperada. Recuperação")
elif media < 5:
    print("Sinto muito. Reprovado")