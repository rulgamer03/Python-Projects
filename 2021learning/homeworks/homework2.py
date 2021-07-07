def factoring(n): #descomposición en factores primos
  text= str(n) + ' = '
  for i in range(1,n+1,2):      # recorre los impares
    if i==1: i=2          # salvo el 1 que será 2
    counter = 0
    while n%i == 0:
      n /= i
      counter+=1
    if counter == 1:
      text += str(i)+ ' × '
    elif counter >1:
      text += str(i) + '^' + str (counter) + ' × '
  text += '1'
  return text


def myfactoring(n): #descomposición en factores primos
  for i in range(1,n+1,2):      # recorre los impares
    if i==1: i=2          # salvo el 1 que será 2
    while n%i == 0:
      n /= i
      print(i)

def primo(num):
    if num == 1:
      return True
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

"""
a = -2
a = 20
if primo(a):
    print("Es primo")
else:
    print("No es primo\nSus factores son:")
    factorize(a)
"""
a = -2

while a != -9:
    a = int(input("Write a positive number : (write -9 to end) "))
    if a > 0:
        if primo(a):
            print("Es primo")
        else:
            print("No es primo\nSus factores son:")
            print(factoring(a))
            print("\nSus factores son:")
            myfactoring(a)
            print("\n")
