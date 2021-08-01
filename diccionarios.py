midiccionario = {
    "Alemania":"Berlin",
    "Francia":"Paris",
    "Reino Unido":"Londres",
    "España":"Madrid"
}
print(midiccionario)
print(midiccionario["España"])
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)


milista = ["España", "Francia", "Reino Unido", "Alemania"]
newdiccionario = {
    milista[0]:"Madrid",
    milista[1]:"Paris"
}
print(newdiccionario)
print(len(newdiccionario))
print(midiccionario.keys())
print(midiccionario.values())

grades ={
    "math": 100,
    "physics": 90,
    "chemestry": 70
}

suma = 0
for grade in grades.values():
    suma += grade

print(suma)
average = suma/len(grades.values())
print(average)
