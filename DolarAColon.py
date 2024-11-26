# Declarar las variables
Colon = 8.75 # definir la variable para el valor de los colones

# pedir el valor de los dolares a convertir
dolar = float(input("\nIngrese la cantidad de dolar a convertir: "))

# realizar la conversion
conversor = dolar * Colon

# redondear el resultado a dos decimales y mostrarlo al usuario
conversor = round(conversor,2)

# mostrar el resultado final al usuario
print(f"\n${dolar} dolares equivale a {conversor} colones.")