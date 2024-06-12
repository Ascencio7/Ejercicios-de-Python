""" 
    Escribir un programa que ingrese los nombres a una lista.
"""
nombres = []

print("\nLista de Nombres")
#Pedir cuántos registros realizará:
cant = int(input("\n¿Cuántos registros realizará?: "))
print("\n")

for i in range(cant):
    nombres.append(input(f"Ingrese el {i + 1}° nombre: "))
    nombres[i]
    
print("\nLista de los nombres ingresados:")
print(nombres)
print("Fin del programa.\n")