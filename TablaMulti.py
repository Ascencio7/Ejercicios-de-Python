"""
    Ejercicio que pide un número determinado para imprimir una tabla de multiplicar
    con el bucle 'FOR'
"""

num = int(input("\nIngrese el número de la tabla: "))

print("\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
print("\nFin del programa.\n")