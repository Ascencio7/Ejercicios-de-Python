""" 
    Escribir un programa que pida un número de 3 digitos y que verifique si lo es o no.
"""

print("\nPrograma que verifica si el número ingresado es de 3 digitos.")

num = int(input("\nIngrese el número entero: "))

if num >= 100 and num <= 999:
    print(f"\nEl número {num} es de tres digitos.")
    print("Fin del programa.\n")
else:
    print(f"\nEl número {num} no es de tres digitos.")
    print("Fin del programa.\n")