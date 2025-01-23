""" 
    Dado el sueldo de n trabajadores considere un aumento del 15% a cada uno de ellos, 
    si su sueldo es inferior a $800. Imprima el sueldo con el aumento incorporado de cada empleado, 
    asi como también el total de la planilla.
"""

n = int(input("\nIngrese la cantidad de trabajadores: "))

# Inicializar las variables
sueldos = [] # Una lista para almacenar los sueldos
totalPlanilla = 0 # Variable acumuladora para el total de la planilla

# Solicitar y procesar los sueldos
for i in range(n):
    sueldo = float(input(f"\nIngrese el sueldo del trabajador {i+1}: "))
    
    # Se aplica el aumento si el sueldo es menor a $800
    if sueldo < 800:
        sueldo += sueldo * 0.15 # El aumento del 15%
        
    sueldos.append(sueldo) # Guardar el sueldo con el aumento aplicado
    totalPlanilla += sueldo # Sumar al total de la planilla
    
# Se imprime los sueldos actualizados y el total de la planilla
print("\nSueldos actualizados:")
for i, sueldo in enumerate(sueldos, start=1):
    print(f"Trabajador {i}: ${sueldo:.2f}")
    
print(f"\nTotal de la planilla: ${totalPlanilla:.2f}")