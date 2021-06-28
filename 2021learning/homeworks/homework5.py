from decimal import *

def factorial(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# e_aproximaton
x = int(input("What is the value of x\n"))
n = int(input("What is the value of n\n"))
e = 0

for i in range(n):
    e += Decimal(x**i)/Decimal(factorial(i))

print(e)
