# Declarando la lista vacia 
lista = list()
lstNombres = []
lstEdades = []
lstEstaturas = []
i = 0
x = 0
# Son 5 estudiantes se hace un bucle
for i in range(5):
    lstNombres.append(input("\nIngresa el nombre: "))
    lstEdades.append(input("Edad: "))
    lstEstaturas.append(input("Estatura: "))
    print("\n")
    
# Se imprime los valores registrados los 3 datos por cada estudiante

for i in range(5):
    print("\nEstudiantes N°", x+1, " :")
    print("Nombre: " + lstNombres[x] + ", Edad: " + str(lstEdades[x]) + " Estatura: " + str(lstEstaturas[x]))