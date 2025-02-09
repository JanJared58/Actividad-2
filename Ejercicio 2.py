num = int(input("Ingrese un numero de 1 al 20: "))

while num<1 or num>20:
    num = int(input("Ingrese un numero de 1 al 20: "))

result = 1
n=num

while n > 0:
    result = result * n
    n = n - 1

print(f"El factorial es: {result}")
