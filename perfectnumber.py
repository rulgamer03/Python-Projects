def perfectnumber(x):
    total = 0
    for i in range(1,x):
        if x % i == 0:
            total+=i
            
    return total == x
    

#print(perfectnumber(8))
for i in range(1,500):
    if perfectnumber(i):
        print(f"{i} is perfect")
    else:
        print(f"{i} is not perfect")
