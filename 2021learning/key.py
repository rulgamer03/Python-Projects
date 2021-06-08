datos = [257, 573, -714, 321, -158, 642, 407, -2]

print(max(datos, key = abs))
print(max(datos))
print(min(datos, key = abs))
print(min(datos))
print(sorted(datos))
print(sorted(datos, reverse=True))
print(sorted(datos, key = abs))

cadenas = ["kkkk", "hhhhhhh", "jjjj", "qqqq", "ttt"]
print(max(cadenas))
print(min(cadenas))
print(max(cadenas, key = len))
print(min(cadenas, key = len))
print(sorted(cadenas, key = len))

numeros = [(7, 20), (6, 30), (4, 50), (8, 10), (5, 40)]
print(max(numeros)) # primero por el indice 0
print(min(numeros)) # primero por el indice 0
print(sorted(numeros))
def indiceuno (secuencia):
    return secuencia[1]

print(max(numeros, key = indiceuno)) # primero por el indice 1
print(min(numeros, key = indiceuno)) # primero por el indice 1
print(sorted(numeros, key = indiceuno))

finales = [(4, 2, 1), (5, 4, 2), (2, 1, 3), (3, 0, 1), (3, 4, 2)]
def suma (secuenciaa):
    return secuenciaa[0]+secuenciaa[1]+secuenciaa[2]

# De menor a mayor, segun la suma de sus elementos
print(sorted(finales, key = suma))
print(sorted(finales, key = sum))

def reverso(tupla):
    return (tupla[2], tupla[1], tupla[0])
# Teniendo en cuenta el tercer elemento, segundo, primero
print(sorted(finales, key = reverso))
ordenada = sorted(finales, key = reverso)
print(ordenada)
