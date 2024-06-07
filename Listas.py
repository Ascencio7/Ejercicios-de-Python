"""
    Crear un programa acceda a una lista y agregue un elemento a la misma
"""

#Inicializamos la lista con texto
frutas = ["Manzana", "Platano", "Naranja"]

#Mostrar la lista inicial completa:
print(f"\nLista inicial: {frutas}")

#Acceder a un elemento de la lista
print(f"\nMostrando el primer elemento: {frutas[0]}")
#La posición 0 es el primer elemento: Manzana
print(f"Mostrando el segundo elemento: {frutas[1]}")
#La posición 0 es el primer elemento: Platano
print(f"Mostrando el tercer elemento: {frutas[2]}")
#La posición 0 es el primer elemento: Naranja

#Agregar un elemento a la lista:
frutas.append("Pera")

print("\nMostrando la lista con el elemento agregado:")
print(frutas, "\n")