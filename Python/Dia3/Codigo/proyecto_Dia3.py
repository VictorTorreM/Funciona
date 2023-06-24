#Pido el texto inicial y lo tranformo a minusc

texto = input("Introduce tu texto porfavor: ")

textop = texto.lower()



#combierto el texto en una lista

lista = list(textop)

#Separo las palabras por espacios
lista_palabra = textop.split(" ")

#Pido las letras y las transformo en minusc 

letra1 = input("Introduce la primera letra: ")
letra2 = input("Introduce la segunda letra: ")
letra3 = input("Introduce la tercera letra: ")

letra1p = letra1.lower()
letra2p = letra2.lower()
letra3p = letra3.lower()

#Compruebo e imprimo la cantidad de veces que aparece cada letra 

print("La letra <"+ letra1p + "> aparece " + str(textop.count(letra1p)) + " veces")
print("La letra <"+ letra2p + "> aparece " + str(textop.count(letra2p)) + " veces")
print("La letra <"+ letra3p + "> aparece " + str(textop.count(letra3p)) + " veces")

#Compruebo cuantas palabras hay en el texto  

print("Hay <" + str(len(lista_palabra)) + "> palabras" )

print("El texto comienza en <"+ lista[0] +">"+ " y termina en <" + lista[-1] +">")

#Le doy la vuelta al texto 

lista_palabra.reverse()

print("El texto al reves es <"+ str(" ".join(lista_palabra)) +">")


python = "python" in lista_palabra
 
dic = {True:"Aparece",False:"No aparece"}


print("La palabra 'Python' " + dic[python] + " en el texto")