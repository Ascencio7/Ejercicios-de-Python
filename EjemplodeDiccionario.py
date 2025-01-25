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

# Funcion para buscar el numero de dui
while True:
    preg = input("¿Desea buscar un registro? (si/no): ").strip().lower()
    
    if preg == "no":
        print("\nFin del programa.\n")
        break
    elif preg == "si":
        dui = input("\nIngrese el numero de DUI: ").strip()
        encontrado = False # Se supone que no esta encontrado al inicio
        
        for i in range(cant):
            if registros["dui"][i] == dui:
                print(f"\nEmpleado N°{i+1}")
                print(f"DUI: {registros['dui'][i]}")
                print(f"Nombre: {registros['nombres'][i]}")
                print(f"Salario: ${registros['salario'][i]}")
                print(f"Puesto: {registros['puesto'][i]}")
                encontrado = True
                break # Se sale del bucle cuando ya se encontro el dato
        if not encontrado:
            print("\nNo se encontró el registro.")
    else:
        print("\nDebe ingresar 'si' o 'no'.")