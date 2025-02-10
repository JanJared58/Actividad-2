print("Programa para contar vocales en un texto\n")

texto= str(input("Ingrese el texto: "))
cuenta=0
vocales=['a','e','i','o','u','A','E','I','O','U']

for caracter in texto:
    if caracter in vocales:
        cuenta +=1


print(f"El texto tiene {cuenta} vocales.")

