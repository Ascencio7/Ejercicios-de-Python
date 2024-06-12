""" 
    Si una empresa de comestibles tiene su tope de ventas promedio en 1000 articulos
    para el 1° trimestre de 2020, leer la información de artículos vendidos correspondiente
    a un vendedor, calcular su promedio y determinar si alcanzó el promedio de ventas de la 
    empresa.
"""

print("\nPromedio de 1000 articulos de Sar S.A de C.V.")

#El código del vendedor
code = input("\nCódigo del vendedor: ")
nameWor = input("Nombre del vendedor: ")

saleJan = int(input("\nArticulos vendidos de Enero: "))
saleFebruary = int(input("Articulos vendidos de Febrero: "))
saleMarch = int(input("Articulos vendidos de Marzo: "))

prom = (saleJan + saleFebruary + saleMarch) / 3

if prom >= 1000:
    print("\n¡Meta alcanzada!")
    print(f"Vendedor: {nameWor} - Código: {code}:")
    print(f"Promedio de articulos vendidos: {prom}")
    print("Fin del programa.\n")
else:
    print("\n¡Meta no alcanzada!")
    print(f"Vendedor: {nameWor} - Código: {code}:")
    print(f"Promedio de articulos vendidos: {prom}")
    print("Fin del programa.\n")