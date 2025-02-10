print("Programa que suma digitos de un numero entero.\n")

digitos= str(input("Ingrese el numero: "))
suma=0

for i in digitos:
    suma= suma + int(i)

print(f"La suma de los digitos es: {suma}")
