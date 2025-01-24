# Se define el diccionario donde se guardara todo los datos
registros = { 
    "dui":[],
    "nombres": [],
    "salario":[],
    "puesto":[]
}

# Se define la cantidad de los registros
cant = int(input("\n¿Cuántos registros desea crear?: "))

# Se llena mediante un bucle
for i in range(cant):
    print(f"\nEmpleado N°{i+1}")
    dui = input("Ingrese DUI: ")
    nombre = input("Ingrese nombre: ")
    salario = float(input("Ingrese salario: $"))
    puesto = input("Ingrese puesto: ")
    
    # Se agregan las variables al diccionario registros
    registros["dui"].append(dui)
    registros["nombres"].append(nombre)
    registros["salario"].append(salario)
    registros["puesto"].append(puesto)
    
print("\nRegistros")   
 
# Se imprimen los datos
for i in range(cant):
    print(f"\nEmpleado N°{i+1}")
    print(f"DUI: {registros['dui'][i]}")
    print(f"Nombre: {registros['nombres'][i]}")
    print(f"Salario: ${registros['salario'][i]}")
    print(f"Puesto: {registros['puesto'][i]}")
    print("\n")