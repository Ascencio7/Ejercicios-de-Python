"""
    Crear un programa que encuentre el total en monto de interés simple que se obtiene en una inversión de
    $n a una tasa de interes mensual de n% a un plazo de n dias.
    
    I = Pin
    
    I interes simple, P = capital, i = tasa de interes, n = tiempo"""

#  Declaramos nuestras variables a utilizar
P = float(input("\nIngresa tu capital: $"))
i = float(input("Ingresa la tasa de interes: "))
n = int(input("Ingresa el plazo de los dias: "))

# Calculamos el interés simple
I = P * i * n 

# Redondeamos el resultado
I = round(I, 2)

# Mostramos el resultado
print(f"\nEl total en monto de interes simple del {i}% es de: ${I}")
print("Fin del programa.\n")