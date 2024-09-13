import os 
os.system("cls || clear")
positivos = 0
negativos = 0
lista_numero = []

def verificar_positivos_negativos(notas):
    qntd_positivos = 0
    qntd_negativos = 0
    soma = 0

    for nota in notas:
        if nota >= 0:
            soma += nota
            qntd_positivos += 1
        else:
            qntd_negativos += 1
    return qntd_positivos, qntd_negativos, soma

for i in range(10):
    nota = int(input(f"Digite a {i+1}ª número: "))
    lista_numero.append(nota)

os.system("cls || clear")

print("=== Exibindo resultado ===")
for i, nota in enumerate(lista_numero):
    print(f"{i+1}ª nota: {nota}")

positivos, negativos, soma = verificar_positivos_negativos(lista_numero)

print(f"\nSoma dos números positivos: {soma}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")