numeros = [1, 2, 3, 4, 5, 6]

def sumar(lista):
    if lista == []:
        return 0
    else:
        return lista[0]+sumar(lista[1:])

print(sumar(numeros))
