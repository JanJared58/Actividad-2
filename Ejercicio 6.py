print("Programa que genera la tabla de multiplicar.\n")

tabla=int(input("Ingrese el numero: "))

for i in range(1, 11):
    print(f"{tabla}x{i} = " + str(tabla*i))


