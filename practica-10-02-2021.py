import cmath
import math
a = input("Escribe el valor del rendimiento: \n")
A = float(a)
while A < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    a = input("Escribe el valor del rendimiento: \n")
    A = float(a)
b = input("Escribe el valor del precio por litro : \n")
B = float(b)
while B < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    b = input("Escribe el valor del precio por litro : \n")
    B = float(b)

velocidad = 80
presupuesto = 500.00
litrosdisponibles = presupuesto/B
distancia = round(litrosdisponibles * A, 2)
tiempodecimal = round(distancia / velocidad, 2)
partedecimal, horas = math.modf(tiempodecimal)
minutos = round(partedecimal * 60, 2)
print("Con $", presupuesto, "pesos \nse recorren", distancia, "km \nen", horas, "horas", minutos, "minutos")
