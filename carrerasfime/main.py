def add(filename, siglas, carrera):
    with open(filename, 'a') as f_obj:
        f_obj.write(f'\n{siglas} {carrera}')

def sacacarrera(linea):
    siglas = ''
    carrera = ''
    counter = 0
    for c in linea:
        if c == ' ':
            counter=1
        if counter != 1:
            siglas+=c
        if counter == 1:
            carrera+=c
    carrera = carrera[1:]
    return(siglas, carrera)


def search(filename, carrera):
    with open(filename) as f_obj:
        lines = f_obj.readlines()
        # print(lines)
        # Forma noob:
        # for line in f_obj:
        # # print(line)
        # print(line.rstrip())
    for line in lines:
        if line.rstrip() != '':
            siglatxt, carreratxt = sacacarrera(line.rstrip())
            if carreratxt == carrera:
                return siglatxt

def printfile(filename):
    with open(filename) as f_obj:
        lines = f_obj.readlines()
        # print(lines)
        # Forma noob:
        # for line in f_obj:
        # # print(line)
        # print(line.rstrip())
    for line in lines:
        if line.rstrip() != '':
            print(line.rstrip())

option=0
while option!= 4:
    option = int(input("Selecciona una opcion\n1 -> Ver todas las carreras con sus siglas\n2 -> Agregar una carrera dada sus siglas y su nombre\n3 -> Dado el nombre de la carrera imprimir las siglas\n4 -> Exit\n"))
    if option == 1:
        printfile("programaseducativos.txt")
        print()

    elif option == 2:
        siglas = input("Sigla: ")
        nombre = input("Nombre: ")
        add('programaseducativos.txt', siglas, nombre)
        print()
    elif option == 3:
        nombre = input("Nombre: ")
        siglas = search('programaseducativos.txt', nombre)
        print(f"Sigla: {siglas}")
        print()
    elif option == 4:
        print("Que tenga un buen dia\n")
    else:
        print("Opcion no disponible\n")
