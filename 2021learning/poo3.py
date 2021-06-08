# https://www.youtube.com/watch?v=lg9p0yWgXYk&list=PLh7JzoyIyU4JVOeKkiNYPkAWBq0Aszxc-&index=2

import  random
class Zombi:

    def __init__(self):
        self.calle = random.randint(10,20)
        self.direccion = random.choice(["izquierda", "derecha"])
        self.velocidad = random.randint(1,3)

    def moverse(self):
        if self.direccion == "izquierda":
            self.calle -= self.velocidad
        else:
            self.calle += self.velocidad

    def no_visible(self):
        if self.calle < 0 or self.calle > 40:
            return True
        else:
            return False

z = Zombi()
print(z.calle)
print(z.direccion)
z.moverse()
print(z.calle)
print(z.no_visible())

print("----\n")
for i in range(12): #Velocidad es random
    print(z.calle)
    z.moverse()
