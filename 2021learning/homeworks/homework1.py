
# Fibonacci series
position = -2  # First start with a negative number to enter in the while


def fib(n):  # Function definition need a number n
    if n == 0 or n == 1:  # if n is 0 we return 0
        return n
    else:
        return fib(n - 1) + fib(n - 2)  # else we use recursivity use the function in the same function


while position != -9:
    position = int(input("What is the position? : (write -9 to end) "))
    if position >= 0:
        item = fib(position)
        print(f"The item {position} in the Fibonacci series is {item}")
        #  if you don't want to use the "item" variable ->
        print(f"The item {position} in the Fibonacci series is {fib(position)}\n")
