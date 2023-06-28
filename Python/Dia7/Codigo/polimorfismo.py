"""
class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre
        
        
    def hablar(self):
        print(self.nombre + " dice muuu")
        
class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre
        
        
    def hablar(self):
        print(self.nombre + " dice beeee")
        
        

vaca1 = Vaca("Lucia")

oveja1 = Oveja("Nerea")


def animal_habla(animal):
    animal.hablar()
    


animal_habla(vaca1)
"""


class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        

robin = Arquero()
merlin = Mago()
naruto = Samurai()


personajes = [robin,merlin,naruto]

def ataque(lista):
    for item in lista:
        item.atacar()
        
        
ataque(personajes)