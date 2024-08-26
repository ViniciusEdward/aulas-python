import os
os.system("cls || clear")

parcial = 0

for i in range(4):
    nota = int(input("Digite uma nota: "))
    parcial = parcial + nota


media = parcial / 4

print(f"Média: {media}")

#git add.
#git commit -m "aula 26/08"
#git push