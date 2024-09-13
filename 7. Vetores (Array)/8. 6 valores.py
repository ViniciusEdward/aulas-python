import os 
os.system("cls || clear")

qntd_de_numeros = 6
lista_pares_positivos = []

for i in range(qntd_de_numeros):
    while True:
        numero = int(input(f"Digite {i+1}º número: "))
        if numero % 2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("Número inválido. Tente novamente.")
            
print("=== Exibindo resultados ===")
for numero in reversed(lista_pares_positivos):
    print(numero)