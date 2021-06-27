from decimal import *
pi = 0
n = int(input("What is the value of n: \n"))
for k in range(n):
    pi += (1/Decimal(16))**k * (Decimal(4)/(8*k+1) -
          Decimal(2)/(8*k+4) -
          Decimal(1)/(8*k+5) -
          Decimal(1)/(8*k+6))
print(pi)
