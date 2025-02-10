print("Programa para encontrar el numero mayor y menor de una lista \n")

lista=[]
op='s'

while op=='s':
    num=int(input("Ingrese el numero: "))
    lista.append(num)
    op=input("¿Desea a agregar otro numero a la lista?(s/n): ")

mayor= max(lista)
menor= min(lista)

print(f"El numero mayor en la lista es: {mayor}.")
print(f"El numero menor en la lista es: {menor}")
