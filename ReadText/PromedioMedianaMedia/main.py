def calculate_moda(datos):
    repeticiones = 0

    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n

    moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia

    for i in datos:
        n = datos.count(i) # Devuelve el número de veces que x aparece enla lista.
        if n == repeticiones and i not in moda:
            moda.append(i)

    if len(moda) != len(datos):
        print(f"\nLa moda es {moda}")
    else:
        print('\nNo hay moda')

def calulate_mediana(datos):
    datos.sort() #.sort Ordena los ítems dela lista

    if len(datos) % 2 == 0:
        n = len(datos)
        mediana = (datos[int(n / 2 - 1)] + datos[int(n / 2)]) / 2
    else:
        mediana = datos[int(len(datos) / 2)]

    print(f"\nLa mediana es {mediana}")



filename = 'numeros.txt'
numeros = []
with open(filename) as f_obj:
    lines = f_obj.readlines()
    # print(lines)
    # Forma noob:
    # for line in f_obj:
        # # print(line)
        # print(line.rstrip())
print("Datos: ")
for line in lines:
    if line.rstrip()!='':
        print(line.rstrip())
        numeros.append(int(line.rstrip()))

numeros.sort()
print(f"\nDatos ordenados: \n{numeros}")

if len(numeros)>0:
    print(f"\nEl promedio de los numeros en el archivo es {sum(numeros)/len(numeros)}")
    calculate_moda(numeros)
    calulate_mediana(numeros)

"""
import random
for i in range (0, 900):
    print(random.randrange(12))
"""





