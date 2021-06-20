def menu(): # Printing menu
  print("Menu Principal")
  print("1. Ver listado")
  print("2. Ver listado filtrado")
  print("3. Agregar beneficiario")
  print("4. Buscar beneficiario")
  print("5. Borrar beneficiario")
  print("6. Salir")

def buscarporcedula(cedula_buscar): # dada una celula returna 0 si ya estaba registrado alguien con esa cedula, en otro caso 1
  archivo = open('agenda.txt', 'r')
  for linea in archivo.readlines():
    if cedula_buscar+'\n' == linea:
      print(f"Ya estaba registrado un beneficiario con la cedula {cedula_buscar}")
      print()
      return 0
  return 1

def ver_listado(): # simplemente imprime el listado
  print()
  print("Listado de beneficiarios")
  print()
  archivo = open('agenda.txt', 'r')
  for linea in archivo.readlines():
    linea = linea.replace('\n','')
    print(linea)
  print()

def ver_listado_filtrado(caracter):
  print()
  print("Listado filtrado de beneficiarios:")
  print()
  archivo = open('agenda.txt', 'r')
  visible = 0
  for linea in archivo.readlines():
    linea = linea.replace('\n', '')
    if 0 < visible <= 2 :
      visible-=1
      print(linea)
    elif linea[0] == caracter.upper() or linea[0] == caracter.lower() :
      print(linea)
      visible=2
  print()

def buscar_beneficiario(nombre):
  archivo = open('agenda.txt', 'r')
  visible = 0
  print()
  for linea in archivo.readlines():
    linea = linea.replace('\n', '')
    if 0 < visible <= 2:
      visible -= 1
      print(linea)
    elif linea == nombre:
      print(linea)
      visible = 2

  print()

def agregarbeneficiario():
  archivo = open('agenda.txt', 'a+')
  name = input("Nombre y apellido del beneficiario: ")
  cedula = input("Cedula: ")
  if buscarporcedula(cedula) == 1:
    celular = input("Celular: ")
    add = name+'\n'+cedula+'\n'+celular+'\n'
    archivo.write(add)

def borrar_beneficiario(cedula):
  eliminado = False
  position = -99
  f = open("agenda.txt", "r")
  lines = f.readlines()
  f.close()
  b = int(len(lines))/3
  for i in range(1,int(b)+1):
    j = 3*i-2
    if lines[j]==cedula+'\n':
      position = j
      print("\nEl usuario ha sido eliminado del listado\n")
      eliminado = True
  f = open("agenda.txt", "w")
  for i, line in enumerate(lines):
    if i < position-1 or i > position+1:
      f.write(line)
  f.close()

  if eliminado == False:
    print("No se elimino a nadie del listado\n")

option = 1

while option !=6:
  menu()
  option=int(input())
  if option == 1:
    ver_listado()
  if option == 2:
    caracter = input("Digite la letra por la que empiezan los beneficiarios: ")
    if len(caracter)==1and caracter.isdigit()==False:
      ver_listado_filtrado(caracter)
    else:
      print("No escribio un caracter valido\n")
  if option == 3:
    agregarbeneficiario()
  if option == 4:
    name = input("Digite el nombre y apellido del beneficiario a buscar: ")
    buscar_beneficiario(name)
  if option == 5:
    cedula = input("Digite la cedula del beneficiario a borrar: ")
    borrar_beneficiario(cedula)
  if option == 6:
    print("\nHasta pronto\n\n")
