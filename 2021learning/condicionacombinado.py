# Condicionales combinados

edad = int(input("Digite su edad: "))

if edad > 0 and edad < 200:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")

else:
    print("Edad incorrecta")

    
