""" 
    Crear un programa que calcule el área de un circulo
"""
#Declarar las variables
PI = 3.14159
S = 0
R = 0

#Pedir el valor del radio

R = float(input("\nIngrese el radio del circulo: "))

S = PI * R * R
S = round(S, 2)

print(f"\nLa superficie del círculo es: {S}")
print("Fin del programa.\n")