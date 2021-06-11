filas = 6
columnas = 12
import random
# import numpy as np
matriz = []

print("Registros mensuales de Temperatura")
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        # valor = float(input(f"Region {i+1}, Mes {j+1} "))
        valor = random.randint(10, 20)
        matriz[i].append(valor)

print()
for fila in matriz:
    print ("[", end = " ")
    for elemento in fila:
        print("{:8.2f}". format(elemento), end=" ")
    print("]")
print()
# print(matriz)

print("Promedio anual por region")
for i in range(filas):
    suma = 0
    for j in range(columnas):
        suma += matriz[i][j]
    promedio=suma/12
    print(f"region {i+1} tuvo un promedio de {promedio}")
"""
print(np.amin(matriz))
print(np.amax(matriz))
np.where(matriz == np.amin(matriz))
np.where(matriz == np.amax(matriz))
"""
