lista = ["José", 33, 56.7,True, "jose@gmail.com"]
lista.append("casa")
print(lista)
lista.extend(["Jardin", 56])
print(lista)
lista.insert(0, "Juan")
print(lista)
lista.remove(True)
print(lista)
r = lista.count("Juan")
print(r)
numeros =[2,3,5,37,6,78,87,67]
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
del numeros[5]
print(numeros)
numeros.pop()
print(numeros)
numeros[1]=99
print(numeros)
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
print(x)
