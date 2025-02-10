print("Programa para sumar los numeros de una lista\n")

lista=[]
op='s'

while op=='s':
    num=int(input("Ingrese el numero: "))
    lista.append(num)
    op=input("¿Desea a agregar otro numero a la lista?(s/n): ")

suma=0
for i in lista:
    suma= suma + i

print(f"La suma de numeros de la lista es de: {suma}")
