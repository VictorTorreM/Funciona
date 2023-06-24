from random import *


#lista inicial

palitos = ["-","--","---","----"]


#mezclar palitos

def mezclar_palitos(lista):
    shuffle(lista)
    return lista



#pedirle intento
def probar_suerte():
    intento = ""
    
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4: ")
    
    return int(intento)

# comprobar intento 

def chequeo(lista,intento):
    if lista[intento - 1 ] == "-":
        print("A lavar los platos")
    else:
        print("Maricon")
    
    print(f"Te ha tocado {lista[intento - 1]}")



"""
palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()

chequeo(palitos_mezclados,seleccion)

"""

####Ejercicio 100####

from random import randint

def lanzar_dados():
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1,d2

def evaluar_jugada(d1,d2):
    suma_dados = d1 + d2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados >6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

d1,d2 = lanzar_dados()
evaluar_jugada(d1,d2)

###Ejercicio 101

#Para quitar el numero mayor de la lista
"""
lista = [1,3,1,3,5,6,7]
num_mayor = max(lista)
index_mayor = lista.index(num_mayor)
lista.pop(index_mayor)
print(lista)

result = []
for n in lista:
    if n not in result:
        result.append(n)
        print(result)
        
        
        
        
"""




def lanzar_moneda():
    
    moneda = randint(1,2)
    jugada = ""
    if moneda == 1:
        jugada = "Cara"
    else:
        jugada = "Cruz"
    
    return jugada
    

lista_numeros = [1,2,3,4,5]
def probar_suerte(jugada,lista_numeros):
    if jugada == "Cara":
        for n in lista_numeros:
            casa = lista_numeros.index(n)
            print(casa)
            lista_numeros.pop(casa)
        return print(f"La lista se autodestruirá {lista_numeros}")
    else:
        return print(f"La lista fue salvada {lista_numeros}")
    
probar_suerte("Cara",lista_numeros)
