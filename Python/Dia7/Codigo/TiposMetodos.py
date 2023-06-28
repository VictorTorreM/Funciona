class Pajaro:
    
    alas = True
    
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print("pio")
        
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")
        self.piar()
    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")
        
        
    @classmethod
    def poner_huevos(cls,cantidad):
        
        print(f"puso {cantidad}")
        cls.alas = False
        print(Pajaro.alas)
        
        
        
    @staticmethod
    def mirar():
        print("El pajaro mira")





"""
Pajaro.mirar()


piolin.pintar_negro()
piolin.volar(60)
piolin.alas = False
print(piolin.alas)
"""


## Ejercicio que me dio guerra solucionado 
"""
class Personaje:
    
    def __init__(self,cantidad):
        self.cantidad = cantidad
    
    def lanzar_flecha(self):
        self.cantidad =self.cantidad - 1
        print(f"{self.cantidad}")
        
heroe = Personaje(10)

heroe.lanzar_flecha()

"""