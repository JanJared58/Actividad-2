print("Programa que cuente cuantos caracteres hay en un texto.\n")

texto=str(input("Ingrese el texto: "))
caracter = str(input("Ingrese el caracter: "))
cuenta=0

for i in texto:
    if i == caracter:
        cuenta += 1

print(f"El caracter {caracter} aparece {cuenta} veces en el texto.")

  