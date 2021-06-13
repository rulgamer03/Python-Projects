letras = ["A", "B", "C", "D", "E"]
numeros = [1,2,3,4,5]

pares = dict(zip(letras, numeros))
print(pares)

a = [1, 2, 3]
b= [10, 20, 30]
c = zip(a,b)
print(c)

for i in c:
    print(i)


d = dict([(1,1), (2,2), (3,3)])
print(d)

d=dict(zip(a,b))
print(d)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
