# Se declara la tabla o matriz
tabla = []
listaAnterior = []

# Se recorre la lista anterior
for x in range(5):
    listaAnterior.append(input("\nIngresa el nombre: "))
    listaAnterior.append(input("Ingresa la edad: "))
    listaAnterior.append(input("Ingresa la estatura: "))
    print("\n")
    
    # Ya despues de llenar la lista anterior se agrega a la tabla
    tabla.append(listaAnterior)
    
""" 
    Hasta aqui se tiene una tabla con 5 items y cada item es una lista
    que posee 3 registros.
"""