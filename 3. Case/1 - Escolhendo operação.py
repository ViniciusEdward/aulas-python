import os
os.system("cls || clear")

print("""
1 - + para somar
2 - - para subtração
3 - * para multiplicação
4 - / para divisão
      """)

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
opcao = input("Digite a operação que deseja (+ - * /): ")

match(opcao):
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero

    case "*":
        resultado = primeiro_numero * segundo_numero

    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção inválida")

print(f"Resultado: {resultado}") 

