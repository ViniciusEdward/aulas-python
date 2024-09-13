import os 
os.system("cls || clear")

def lista():
    lista_numero = []
    for i in range(5):
        numero = int(input(f"Digite a {i+1}ª número: "))
        if numero <0:
            numero = 0
        lista_numero.append(numero)
    os.system("cls || clear")
    return lista_numero
    
    
listas = lista()

print("=== Exibindo resultados ===")
for i, numero in enumerate(listas):
    print(f"{i+1}ª numero: {numero}")

for i in range(1):
    print(f"\nLista: {listas}")
