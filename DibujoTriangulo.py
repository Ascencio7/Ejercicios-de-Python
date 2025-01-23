# Pedir al usuario una palabra de 4 letras
while True:
    palabra = input("\nIntroduce una palabra de 4 letras: ") # Se pide la palabra de 4 letras
    if len(palabra) == 4: # Verifica si la palabra es de 4 letras
        break # fin del bucle
    print("\nLa palabra debe tener exactamente 4 letras. Inténtalo de nuevo.") # Si la letra es más de 4 palabras se pide de nuevo

# Número de filas del triángulo
filas = 4  

# Bucle para generar el triángulo con la palabra en el centro
for i in range(1, filas + 1):
    if i == filas:
        print(' ' * (filas - i) + palabra)
    else:
        print(' ' * (filas - i) + '*' * (2 * i - 1))