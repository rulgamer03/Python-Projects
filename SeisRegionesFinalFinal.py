filas = 6
columnas = 12
matriz = []
promedios = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input(f"Region {i+1}, Mes {j+1} "))
        matriz[i].append(valor)

print("\nRegistros mensuales de temperatura (las regiones son las filas y los meses son las columnas)\n")
for fila in matriz:
    print ("[", end = " ")
    for elemento in fila:
        print("{:8.2f}". format(elemento), end=" ")
    print("]")
print()

print("Promedio anual por region")
for i in range(filas):
    suma = 0
    for j in range(columnas):
        suma += matriz[i][j]
    promedio=round(suma/12,2)
    print(f"La region {i + 1} tuvo un promedio de {promedio}")
    promedios.append([])
    promedios[i] = promedio


maximo = matriz[0][0]
minimo = matriz[0][0]
indice_maximo=(0,0)
indice_minimo=(0,0)

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > maximo:
            maximo = matriz[i][j]
        if matriz[i][j]  < minimo:
            minimo = matriz[i][j]

print()
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] == maximo:
            print(f"El mes {j+1} la region {i+1}  obtuvo la temperatura MAXIMA de {maximo}")
        elif matriz[i][j] == minimo:
            print(f"El mes {j+1} la region {i+1}  obtuvo la temperatura MINIMA de {minimo}")


print()

region_con_mayor_promedio=0
promedio_mayor=0
for i in range(6):
        if promedios[i] > promedio_mayor:
            promedio_mayor = promedios[i]
            region_con_mayor_promedio = i

for i in range(6):
        if promedios[i] == promedio_mayor:
            print(f"\nLa region {i + 1} es la que tiene el mayor promedio ({promedio_mayor})")
