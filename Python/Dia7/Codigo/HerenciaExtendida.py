class Animal:
    def __init__(self,edad,color):
        self.edad  = edad
        self.color = color
        
    def hablar(self):
        print("Hola dsadsadsa")

    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):
    
    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo
    
    
    def hablar(self):
        print("pio")
    
    
    def volar(self,metros):
        print(f"Voló {metros} M")


piolin = Pajaro(3,"amarillo",60)
mi_animal = Animal(3,"rojo")





class Padre:
    def hablar(self):
        print("hola")
        
class Madre:
    def reir(self):
        print("HAHAH")
    def hablar(self):
        print("Quetal")



class Hijo(Padre,Madre):
    pass



class Nieto(Hijo):
    pass

mi_nieto = Nieto()

print(Nieto.__mro__)