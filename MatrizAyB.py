# Se inicia una función para leer una matriz
def leer_matriz(filas, columnas, nombre):
    print(f"\nIngrese los elementos de la matriz {nombre}: ")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Se inicia una funcion para verificar si dos matrices son identicas
def son_identicas(matriz_a, matriz_b):
    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[0])):
            if matriz_a[i][j] != matriz_b[i][j]:
                return False
    return True

# Se solicitan las dimenciones de las matrices
filas = int(input("\nIngrese el numero de filas: "))
columnas = int(input("Ingrese el numero de las columnas: "))

# Se leen las matrices
matriz_a = leer_matriz(filas, columnas, "A")
matriz_b = leer_matriz(filas, columnas, "B")

# Se verifica si las matrices son identicas
if son_identicas(matriz_a, matriz_b):
    print("\nLas matrices son identicas.")
else:
    print("\nLas matrices no son identicas.")