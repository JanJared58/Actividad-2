print("Programa para determinar si un numero es primo o no.\n")

num= int(input("Ingrese el numero: "))

primo = True

if num <= 1:
    primo = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            primo= False
            break

if primo:
    print(f"El numero {num} es primo.")
else:
    print(f"El numero {num} no es primo.")
    