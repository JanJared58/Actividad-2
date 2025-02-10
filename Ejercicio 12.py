print("Programa que ordena una lista.\n")

lista=[]
op='s'

while op=='s':
    num=int(input("Ingrese el numero: "))
    lista.append(num)
    op=input("¿Desea a agregar otro numero a la lista?(s/n): ")

lista.sort()

print("Lista ordenada de menor a mayor: ", lista)
