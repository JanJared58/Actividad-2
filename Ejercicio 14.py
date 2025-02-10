print("Programa que genera numeros aleatorios.\n")

import random
lista=[]

n= int(input("Ingrese la cantidad de numeros aleatorios: "))

for i in range(0, n):
    lista.append(random.randint(1,100))

print(lista)

