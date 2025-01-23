# Se pide el numero de empleados
n = int(input("\nNumero de empleados: "))

# Inicializar las listas 
nombres = []
edades = []
salarios = []

# Registrar los datos del empleado
for i in range(n):
    print(f"\nEmpleado {i + 1}:")
    nombre = input(" Nombres: ")
    edade = int(input(" Edad: "))
    salario = float(input(" Salario: $"))
    
    # Agregar los datos a la lista
    nombres.append(nombre)
    edades.append(edade)
    salarios.append(salario)
    
# Determinar el empleado que mas gana
mayorSalario = salarios.index(max(salarios)) # Obtiene el salario mas alto
nombreMayorSalario = nombres[mayorSalario]
salarioMayor = salarios[mayorSalario] # Se obtiene el indice del empleado

# Imprimir los resultados
print("\nResultados")
print(f"\nEl empleado que mas gana es '{nombreMayorSalario}' con un salario de ${salarioMayor:.2f}")
print("\n")