"""
    Ejercicio que pide un número determinado para imprimir una tabla de multiplicar
    con el bucle 'FOR'
"""

num = int(input("\nIngrese el número de la tabla: "))

for num in range(1, 11, 1):
    print(f"{num} x {num} = {num * num}")
    
print("\nFin del programa.\n")