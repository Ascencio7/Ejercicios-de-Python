""" 
    Escribir un programa que determine si el número ingresado de 4 digitos 
    es positivo o negativo.
"""

print("\nNúmero positivo de 4 dígitos.")

# Solicitar al usuario que ingrese el número
num = int(input("\nIngrese el número: "))

# Verificar si el número es de 4 digitos, positivo o negativo
if 1000 <= num <= 9999:
    print("\nEl número es de 4 digitos.")
    print("Fin del programa.\n")
elif -9999 <= num <= -1000:
    print("\nEl número es negativo.")
    print("Fin del programa.\n")
else:
    print("\nEl número no es de 4 digitos.")
    print("Fin del programa.\n")