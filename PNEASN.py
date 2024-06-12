""" 
    Escribir un programa que reciba dos números y que el primer número sea
    elevado a la potencia representada por el segundo número.
"""

print("\nElevar el primer número ingresado por el segundo número ingresado:")
numOne = float(input("\nIngrese el primer número: "))
numTwo = float(input("Ingrese el segundo número: "))

pontence = numOne ** numTwo
pontence = round(pontence, 2)

print(f"\nEl primer número: {numOne} elevado al segundo número: {numTwo} da como resultado: {pontence}")
print("Fin del programa.\n")