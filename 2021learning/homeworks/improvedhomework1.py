position = -2  # First start with a negative number to enter in the while


def fib(n):
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n+1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn


while position < 0:
    position = int(input("What is the position? : "))

item = fib(position)
print(f"The item {position} in the Fibonacci series is {item}")
#  if you don't want to use the "item" variable ->
print(f"The item {position} in the Fibonacci series is {fib(position)}")
