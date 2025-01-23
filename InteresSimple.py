# Crear un programa que encuentre el total en monto de interés simple que se obtiene en una inversión de
# $10,000 a una tasa de interes mensual de 5% a un plazo de 60 dias.
# I = Pin
# I interes simple, P = capital, i = tasa de interes, n = tiempo

P = float(input("\nIngrese su capital: "))
i = float(input("Ingrese la tasa de interés: "))
n = float(input("Ingrese el tiempo: "))

I = P * i * n
I = round(I, 2) # se usa para redondear el resultado

print("\nEl total en monto de interés simple es:", I)