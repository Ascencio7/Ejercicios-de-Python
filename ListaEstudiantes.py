#lista = list()

nombres = []
edades = []
estaturas = []

print("\n")
for i in range(3):
    nombres.append(input(f"Ingrese el nombre del {i + 1}° estudiante: "))
    edades.append(input("Edad: "))
    estaturas.append(input("Estatura: "))
    print("\n")
    

for x in range(3):
    print(f"{x + 1}° Estudiante:\n")
    print(f"Nombre: {nombres[x]}, Edad: {edades[x]}, Estatura: {estaturas[x]}\n")
    
print("\nFin del programa.\n")