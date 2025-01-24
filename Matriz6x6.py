# Se crea la matriz de 6x6 llena de 0
matriz = [[0 for _ in range(6)] for _ in range(6)]

# Se llena las diagonales con 1
for i in range(6):
    matriz[i][i] = 1 # La diagonal principal
    matriz[i][5 - i] = 1 # La diagonal secundaria
    
# Se imprime la matriz
print("\nMatriz de 6x6:")
print("\n")
for fila in matriz:
    print(" ".join(map(str, fila)))