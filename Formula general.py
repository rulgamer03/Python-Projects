# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:00:18 2020

@author: angel
"""
import cmath
import math
a = input("Escribe el valor de a: \n")
A = float(a)

b = input("Escribe el valor de b: \n")
B = float(b)

c = input("Escribe el valor de c: \n")
C = float(c)

x1=0
x2=0
discriminante=B**2-(4*A*C)
if discriminante<0:
    print("El valor de x1 es ")
    x1 = ((-B+cmath.sqrt(discriminante))/(2*A))
    print(x1)
    print("El valor de x2 es ")
    x2 = ((-B-cmath.sqrt(discriminante))/(2*A))
    print(x2)

elif discriminante>=0:
    print("El valor de x1 es ")
    x1 = ((-B+math.sqrt(discriminante))/(2*A))
    print(x1)
    print("El valor de x2 es ")
    x2 = ((-B-math.sqrt(discriminante))/(2*A))
    print(x2)