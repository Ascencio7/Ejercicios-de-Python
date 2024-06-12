""" 
    Escribir un programa que muestre el último digito de un número ingresado.
"""

print("\nÚltimo digito de un número ingresado.")

num = float(input("\nIngrese el número: "))

lastDigit = num % 10

print(f"\nEl último digito de {num} es: {lastDigit}")
print("Fin del programa.\n")