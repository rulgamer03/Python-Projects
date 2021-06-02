string="Hello world"
print(string[0])
print(string)
string=string.replace(" ", "_")
print(string)
lista=[string, "Hi world", "My name is ruly", "Have a fantastic day"]
print(lista[1])
print(lista[-1][2])
print(lista[0:3])
stringtwo="Hello Ruly"
stringtwo=stringtwo.replace(stringtwo[3], "_")
print(stringtwo)
stringfinal="Hello Ruly"
stringfinal=stringfinal.replace("l", "_", 1)
# El 1 limita la primera vez
print(stringfinal)

