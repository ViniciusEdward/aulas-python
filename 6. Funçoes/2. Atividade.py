import os
os.system("cls || clear")

def exibir_tabuada(numero):
    """Função para exibir a tabuada de um número."""
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    """Função principal do programa."""
    try:
        numero = int(input("Informe um número para ver a tabuada: "))
        exibir_tabuada(numero)
    except ValueError:
        print("Por favor, informe um número inteiro válido.")

if __name__ == "__main__":
    main()