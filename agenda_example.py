def buscar(nombre):
  with open("agenda.txt") as archivo: 
        linea = archivo.readline()
        while linea:
          if nombre in linea:
            print(linea, end='')
            print(archivo.readline(), end='')
            print(archivo.readline(), end='')
          linea = archivo.readline()

def agregar():
  with open("agenda.txt", 'a') as archivo:
      for i in range(3):
        archivo.write(input('') + '\n')
  print("El beneficiario ha sido agregado")

def borrar(cedula):
  with open("agenda.txt") as archivo:
      lineas = archivo.readlines()
      for index, linea in enumerate(lineas):
        linea = linea[0:len(linea)-1]
        if linea == cedula:
          del lineas[index-1]
          del lineas[index]
          del lineas[index-1]
  with open("agenda.txt", "w+") as archivo:
    for linea in lineas:
      archivo.write(linea)
  print("El usuario ha sido eliminado del listado")


while True:
  print("""Menu Principal
  1. Ver listado
  2. Ver listado filtrado
  3. Agregar beneficiario
  4. Buscar beneficiario
  5. Borrar beneficiario
  6. Salir""")

  opcion = int(input())
  datos = []

  if opcion==1:
    try:
      with open("agenda.txt") as archivo:
        lineas = archivo.readlines()
        print("\nListado de beneficiarios\n")
        for linea in lineas:
          print(linea, end='')
    except:
      print('No hay datos guardados')
  
  if opcion==2:
    letra = input("Digite la letra por la que empiezan los beneficiarios: ")
    print("Listado filtrado de beneficiarios:\n")
    with open("agenda.txt") as archivo:
        linea = archivo.readline()
        while linea:
          if linea.startswith(letra):
            print(linea, end='')
            print(archivo.readline(), end='')
            print(archivo.readline(), end='')
          linea = archivo.readline()

  if opcion==3:
    print("\nDigite la información del beneficiario a agregar:")
    agregar()

  if opcion==4:
    nombre = input("Digite el nombre y apellido del beneficiario a buscar:")
    buscar(nombre)

  if opcion==5:
    cedula = input("Digite la cedula del beneficiario a borrar: ")
    borrar(cedula)

  if opcion==6:
    print("Hasta pronto")
    break
