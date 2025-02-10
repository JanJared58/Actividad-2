print("Programa para generar numeros de la secuencia de Fibonacci")

n=int(input("Ingrese el numero (1-50): "))

while n<1 or n>50:
    print("Numero invalido. ")
    n=int(input("Ingrese el numero (1-50): "))

a=0
b=1

for i in range (1, n+1):
    print(a)
    c= a+b
    a=b
    b=c

