filas = 6
columnas = 12
matriz = []
promedios = []
matriz=[
    [    -9.00 ,    -7.00 ,    12.00 ,    19.00 ,    -2.00 ,    15.00 ,    26.00 ,    -9.00 ,    24.00 ,    14.00 ,    -6.00 ,     5.00 , ],
    [    -8.00 ,    11.00 ,    18.00 ,    24.00 ,    -5.00 ,     9.00 ,     2.00 ,    18.00 ,     5.00 ,    -9.00 ,    30.00 ,     5.00 , ],
    [     0.00 ,     0.00 ,    20.00 ,    28.00 ,    26.00 ,    10.00 ,    24.00 ,    25.00 ,     4.00 ,    19.00 ,    26.00 ,     6.00 , ],
    [    -4.00 ,    -3.00 ,    21.00 ,    14.00 ,    21.00 ,     2.00 ,    -8.00 ,    -3.00 ,    17.00 ,     3.00 ,     3.00 ,    18.00 , ],
    [    16.00 ,    24.00 ,     6.00 ,     0.00 ,    15.00 ,    26.00 ,    -3.00 ,    25.00 ,    -5.00 ,    27.00 ,    22.00 ,    20.00 , ],
    [     4.00 ,    30.00 ,    26.00 ,    -5.00 ,    28.00 ,    20.00 ,    -5.00 ,    -3.00 ,    -6.00 ,    -9.00 ,    22.00 ,    11.00 , ]
]

print("\nRegistros mensuales de temperatura (las regiones son las filas y los meses son las columnas)\n")
for fila in matriz:
    print ("", end = " ")
    for elemento in fila:
        print("{:8.2f}". format(elemento), end=" ")
    print("")
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



