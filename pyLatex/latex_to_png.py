from sympy import *
x = Symbol('x', odd=True)
expr = sin(sqrt(x**2 + 20)) + 1
preview(expr, viewer='file', filename='output.png')
preview(r'$$\int_0^1 e^x\,dx$$', viewer='file', filename='test.png', euler=False)
