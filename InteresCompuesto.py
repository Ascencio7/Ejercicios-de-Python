""" 
    Aplicar el Interes Compuesto en Python
"""

def calcular_interes_compuesto(principal, tasaInteres, tiempo, frecuencia):
    tasaDecimal = tasaInteres / 100 # El porcentaje se convierte en decimal
    montoTotal = principal * (1 + tasaDecimal / frecuencia) ** (frecuencia * tiempo)
    return round(montoTotal, 2) # Aproximar el resultado

# Datos de entrada
capitalInicial = float(input("\nIngresa el capital inicial: $"))
tasa = float(input("Ingresa la tasa de interes anual (%): "))
tiempoYear = int(input("Ingresa el numero de años: "))
frecuenciaCapitalizacion = int(input("Ingresa la frecuencia de capitalizacion por año: "))

# Calculamos el interés compuesto
montoFinal = calcular_interes_compuesto(capitalInicial, tasa, tiempoYear, frecuenciaCapitalizacion)
montoFinal = round(montoFinal, 2)

# Mostramos el resultado
print(f"\nEl monto final despues de {tiempoYear} años sera: ${montoFinal}")