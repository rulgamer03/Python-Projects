def fibonacciRecursivo(n):
    if n < 2:
        return n 
    #print("C", sum(lista))
    
    return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

def fibonacciIterativo(n):
    if n<2:
        return n
    fn_1 = 1
    fn_2 = 0

    for i in range(n-1):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
    return fn

print('##### Numero de Fibonacci #####')

n = 30
print(fibonacciRecursivo(n))
print(fibonacciIterativo(n))
