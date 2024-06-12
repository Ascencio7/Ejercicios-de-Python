""" 
    Escribir un programa que sume los últimos dos digitos de un número.
"""

print("\nSuma de los Últimos dos digitos.")

num = float(input("\nIngrese el número: "))

lastDigit = num % 10
penultimateDigit = (num // 10) % 10

suma = lastDigit + penultimateDigit

print(f"\nLa suma de los dos últimos digitos de {num} da como resultado: {suma}")
print("Fin del programa.\n")