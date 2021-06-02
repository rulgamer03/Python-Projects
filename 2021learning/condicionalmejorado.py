# Condicionales combinados

edad = int(input("Digite su edad: "))

if 0<edad<200:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

else:
    print("Edad incorrecta")
