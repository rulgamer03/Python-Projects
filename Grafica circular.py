import matplotlib.pyplot as plt

a = input("Escribe el numero de personas que usan vehiculo: \n")
A = int(a)

while A < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    a = input("Escribe el numero de personas que usan vehiculo: \n")
    A = int(a)

b = input("Escribe el numero de personas que usan motocicleta: \n")
B = int(b)

while B < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    b = input("Escribe el numero de personas que usan motocicletas: \n")
    B = int(b)

c = input("Escribe el numero de personas que usan bicicletas: \n")
C = int(c)

while C < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    c = input("Escribe el numero de personas que usan bicicletas: \n")
    C = int(c)

d = input("Escribe el numero de personas que usan el metro: \n")
D = int(d)

while D < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    d = input("Escribe el numero de personas que usan el metro: \n")
    D = int(d)

Dato1 = float(A/(A+B+C+D)*100)
Dato2 = float(B/(A+B+C+D)*100)
Dato3 = float(C/(A+B+C+D)*100)
Dato4 = float(D/(A+B+C+D)*100)
print(Dato1, Dato2, Dato3, Dato4)
medios_transporte= "Vehiculo", "Motocicleta", "Bicicleta", "Metro"
sizes= [Dato1, Dato2,Dato3, Dato4]

fig1, ax1 =plt.subplots()
ax1.pie(sizes, labels=medios_transporte, autopct='%1.1f%%', shadow=True, startangle=90)

ax1.axis('equal')

plt.title("Principal Medio de transporte")
plt.legend()
plt.savefig('Grafica_pastel.png')
plt.show()
