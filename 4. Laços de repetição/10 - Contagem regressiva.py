import time
import os
os.system("cls || clear")

numero = int(input("Digite um número: "))

for i in range(numero,-1,-1):
    print(i)
    time.sleep(1)