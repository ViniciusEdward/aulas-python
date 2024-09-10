import os 
os.system("cls || clear")

lista_numero = []
soma = 0
positivo = 0
negativo = 0

for i in range(10):
    numero = int(input(f"Digite a {i+1}ª número: "))
    lista_numero.append(numero)
    if numero >= 0:
        positivo +=1
        soma += numero
    else:
        negativo += 1

os.system("cls || clear")
for i, numero in enumerate(lista_numero):
    print(f"{i+1}ª nota: {numero}")
print(f"Soma dos números positivos: {soma}")
print(f"Quantidade de positivos: {positivo}")
print(f"Quantidade de negativo: {negativo}")