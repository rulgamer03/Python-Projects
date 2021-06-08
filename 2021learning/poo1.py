# Programacion orientada a objetos 1
# https://www.youtube.com/watch?v=lg9p0yWgXYk&list=PLh7JzoyIyU4JVOeKkiNYPkAWBq0Aszxc-&index=2
class Persona:
    def __init__(self, nombre_persona, calle=1):
        self.nombre = nombre_persona
        self.calle = calle

    def moverse(self, velocidad):
            self.calle += velocidad



jose = Persona("Jose")
juan = Persona("Juan", 2)
print(jose.nombre)
print(juan.nombre)
print(jose.calle)
print(juan.calle)
jose.moverse(5)
print(jose.calle)
