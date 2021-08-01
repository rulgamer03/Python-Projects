mitupla = ("Juan",13,1,1995)
print(mitupla)
print(mitupla[1])
milista=list(mitupla)
print(milista)
print(milista[0])

newlista = ["Juan",13,1,1995]
newtupla = tuple(milista)
print("Juan" in newlista)
print("Juan" in newtupla)
print(mitupla.count(13))
print(milista.count(13))

nombre, dia, mes, year = newtupla
print(nombre, dia, mes, year)
