#Para importar un metodo a python es:
# from libreria import cosa 
#######IMPORTANTE#########
#El archivo no puede tener un nombre igual a la libreria porque si no no funciona 

from random import *

aleatorio = randint(5,100)

print(aleatorio)

ale = round(uniform(1,5),1)

print(ale)

coso = random()

print(coso)

colores = ["Azul","Rojo","Amarillo","Verde"]

color = choice(colores)

print(color)

numeros = list(range(5,51,5))

shuffle(numeros)
print(numeros)