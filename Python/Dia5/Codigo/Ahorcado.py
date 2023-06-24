import random
import string
vida = 6 
Lista_palabras = ["calamar","estomago","sombrero","orangutan"]



def elegir_palabra(Lista_palabras):
    empezar = ""
    while empezar != "Y":
        empezar = input("Quieres jugar? Y/N \n").upper()
        
    if empezar == "Y":
        return random.choice(Lista_palabras)

def dividir_palabra(palabra):
    palabra_separada = []
    for letra in palabra:
        palabra_separada.append(letra)
    return palabra_separada



def guiones(palabra_separada):
    
    
    renglones = []
    for letra in palabra_separada:
        renglones.append("-")
    return renglones

palabra_para_adivinar = dividir_palabra(elegir_palabra(Lista_palabras))

palabra_secreta = guiones(palabra_para_adivinar)

print(f"La palabra que tienes que adivinar es : \n{guiones(dividir_palabra(palabra_secreta))}")

def adivinar(vidas,renglones,palabrafinal):
    while vidas > 0:
        intento = "321321"
        while intento not in string.ascii_lowercase and len(intento) != 1:
            intento = input("Introduce una letra: ").lower()
            
            
        if intento in palabrafinal:
            posicion = palabrafinal.index(intento)
            print(palabrafinal.index(intento))
            
            for nletra in palabrafinal:
                renglones.pop(posicion)
                renglones.insert(posicion,intento)
                
            print(f"Te quedan {vidas} intentos")
            print(renglones)
        else:
            vidas = vidas -1
            print(f"Te quedan {vidas} intentos")
    print(palabrafinal)
    return print(renglones)




adivinar(6,palabra_secreta,palabra_para_adivinar)