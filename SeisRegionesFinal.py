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
            indice_maximo = (i,j)
        if matriz[i][j]  < minimo:
            minimo = matriz[i][j]
            indice_minimo = (i, j) # Tuple

mes_maximo = indice_maximo[1] +1
region_maximo = indice_maximo[0]+1
mes_minimo = indice_minimo[1] +1
region_minimo = indice_minimo[0] +1

print(f"\nEl mes {mes_maximo} la region {region_maximo}  obtuvo la temperatura maxima de {maximo}")
print(f"El mes {mes_minimo} la region {region_minimo}  obtuvo la temperatura minima de {minimo}")


region_con_mayor_promedio=0
promedio_mayor=0
for i in range(6):
        if promedios[i] > promedio_mayor:
            promedio_mayor = promedios[i]
            region_con_mayor_promedio = i

print(f"\nLa region {region_con_mayor_promedio+1} es la que tiene el mayor promedio ({promedio_mayor})")
