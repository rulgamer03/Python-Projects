filas = int(input("Introduce numero de filas: "))
columnas = int(input("Introduce numero de columnas: "))

matriz = []
"""
for i in range(filas):
    matriz.append([0] * columnas) # rellenamos de 0

for i in range(filas):
    for j in range(columnas):
        matriz[i][j]= float(input(f"Fila {i+1}, Columna{j+1}"))

"""

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input(f"Fila {i+1}, Columna {j+1} "))
        matriz[i].append(valor)

print()
for fila in matriz:
    print ("[", end = " ")
    for elemento in fila:
        print("{:8.2f}". format(elemento), end=" ")
    print("]")
print()
