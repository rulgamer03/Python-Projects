import numpy as np
import matplotlib.pyplot as plt
# ingreso
fx = lambda x: np.sqrt(x)* np.sin(x) # fx es una funcion lambda que depende de x
a= 1 # intervalo
b = 3 # intervalo
tramos = 4
muestras = tramos + 1
xi = np.linspace(a,b, muestras)
print(xi)
# xi es la distribucion de los puntos entre a y b con la cantidad de muestras
fi = fx(xi)
#salida
muestraslinea = muestras * 10 # el * 10 es para lograr la linea
xk = np.linspace(a,b, muestraslinea)
fk = fx(xk)
plt.plot(xi,fi, 'ro') # Marcados por un punto ROJO "ro"
plt.plot(xk,fk, 'g') # linea verde
plt.fill_between(xk,fk)
plt.show()
