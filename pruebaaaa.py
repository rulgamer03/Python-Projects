import sys
import os


def leer_datosarchivo():
    agendadic = {}
    archivo = open('agenda.txt', 'r')
    lista_archivo = archivo.readlines()
    contador = 0
    nombre = ''
    cedula = ''
    celular = ''
    for linea in lista_archivo:
        contador += 1
        if contador == 1:
            nombre = linea.strip('\n')
            if contador == 2:
                cedula = linea.strip('\n')
            if contador == 3:
                celular = linea.strip('\n')
            agendadic[cedula] = [nombre, celular]
            contador = 0
            nombre = ''
            cedula = ''
            celular = ''
            print(agendadic)
            archivo.close()
    return (agendadic)


def guardardatos_archivo(agendadic):
    archivo = open('agenda.txt', 'w')
    for llave, valor in agendadic.items():
        archivo.write(valor[0] + '\n')
        archivo.write(llave + '\n')
        archivo.write(valor[1] + '\n')
        archivo.close()


def verlistado():
    archivo = open('agenda.txt', 'r')
    print('Listado de beneficiarios')
    print(archivo.read())
    archivo.close()


def verlistadofiltrado(agendadic):
    print("Digite la letra por la que empiezan los beneficiarios:")
    letra = input()
    print('Listado filtrado de beneficiarios:')
    for llave, valor in agendadic.items():
        if valor[0][0] == letra:
            print(valor[0])
            print(llave)
            print(valor[1])


def agregarbeneficiario():
    archivo = open('agenda.txt', 'a+')
    print("Digite la información del beneficiario a agregar:")
    nombre = input()
    cedula = input()
    celular = input()
    archivo.write(nombre + '\n')
    archivo.write(cedula + '\n')
    archivo.write(celular + '\n')
    print('El beneficiario ha sido agregado')
    archivo.close()


def buscarbeneficiario(agendadic):
    print('Digite el nombre y apellido del beneficiario a buscar:')
    buscarnombre = input()
    encontrado = False
    for llave, valor in agendadic.items():
        if valor[0] == buscarnombre:
            print(valor[0])
            print(llave)
            print(valor[1])
            encontrado = True
    if encontrado == False:
        print('beneficiario no encontrado')


def borrarbeneficiario(agendadic):
    print('Digite la cedula del beneficiario a borrar:')
    cedula = input()
    if cedula in agendadic:
        del agendadic[cedula]
        print('El usuario ha sido eliminado del listado')
    else:
        print('beneficiario no existe en la agenda')
    return (agendadic)


def menu():
    print("Menu Principal")
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borrar beneficiario")
    print("6. Salir")

    opcion = int(input())
    if opcion == 1:
        verlistado()
    if opcion == 2:
        agendadic = leer_datosarchivo()
        verlistadofiltrado(agendadic)
    if opcion == 3:
        agregarbeneficiario()
    if opcion == 4:
        agendadic = leer_datosarchivo()
        buscarbeneficiario(agendadic)
    if opcion == 5:
        agendadic = leer_datosarchivo()
        borrarbeneficiario(agendadic)
        guardardatos_archivo(agendadic)
    if opcion == 6:
        print("Hasta pronto")
        sys.exit()
    else:
        menu()


archivo = open('agenda.txt', 'w')
archivo.close()
menu()
