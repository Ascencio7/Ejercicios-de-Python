# Se importa la libreria para los números random
import random

# Se definen las dimensiones de la matriz
filas = 10
columnas = 6

# Se inicializa la matriz con numeros aleatorios entre 10 y 99
matriz = [[random.randint(10,99) for _ in range(columnas)] for _ in range(filas)]

# Se inicializan los contadores de los pares e impares
pares = 0
impares = 0

# Se recorre la matriz para contar pares e impares
for fila in matriz:
    for num in fila:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

# Se muestra la matriz
print("\nMatriz generada de 10x6:")
for fila in matriz:
    print(" ".join(map(str, fila)))

# Se muestra el resultado
print(f"\nTotal de pares: {pares}")
print(f"Total de impares: {impares}")
print("\nFin del programa.\n")