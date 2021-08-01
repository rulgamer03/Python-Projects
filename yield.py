def generaPares(limite):
    for num in range(1,limite):
        yield num*2

devuelvePares=generaPares(10)

for i in devuelvePares:
    print(i)
