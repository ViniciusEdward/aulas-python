import os 
os.system("cls || clear")

lista_numero = []

def verificando_numeros(lista_numero):
    lista_atualizada = []
    for numero in lista_numero:
        if numero <0:
            numero = 0
        lista_atualizada.append(numero)
    return lista_atualizada
    
for i in range(5):
    numero = int(input(f"Digite a {i+1}ª número: "))
    lista_numero.append(numero)
    
lista_numero = verificando_numeros(lista_numero)

print("=== Exibindo resultados ===")
for cada_numero in lista_numero:
    print(cada_numero)
    
for i in range(1):
    print(f"Lista: {lista_numero}")