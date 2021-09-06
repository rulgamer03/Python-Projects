def primo(num):
    if num == 1:
        return True
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

for i in range(1,100):
    if primo(i):
        print(i)
