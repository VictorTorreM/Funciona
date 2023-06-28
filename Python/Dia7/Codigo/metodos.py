"""
class Pajaro:
    alas = True
    
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        
    
    def piar(self):
        print("pio, mi color es {}".format(self.color))
        
        
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        

piolin = Pajaro("amarillo","canario")

piolin.piar()

"""
class Alarma:
    
    def postergar(self,cantidad_minutos):
        print(f"hola{cantidad_minutos}")
caca = Alarma()
caca.postergar(12)


