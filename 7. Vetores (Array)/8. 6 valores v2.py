import os 
os.system("cls || clear")

qntd_de_numeros = 6
lista_pares_positivos = []

def valores():
    for i in range(qntd_de_numeros):
        while True:
            numero = int(input(f"Digite {i+1}º número: "))
            if numero % 2 == 0 and numero > 0:
                lista_pares_positivos.append(numero)
                break
            else:
                print("Número inválido. Tente novamente.")
    return lista_pares_positivos        

lista_numeros = valores()

os.system("cls || clear")        
print("=== Exibindo resultados ===")
for i, numero in enumerate (reversed(lista_numeros)):
    print(f"{len(lista_numeros)-i}º - {numero}")