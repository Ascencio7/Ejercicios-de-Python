"""
    Ejercicio que pide el número de la tabla de multiplicar con el bucle
    while.
"""

num = int(input("\nIngrese el número de la tabla: "))

i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

print("\nFin del programa.\n")