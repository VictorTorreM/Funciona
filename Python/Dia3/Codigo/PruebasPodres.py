#Pido el texto inicial y lo tranformo a minusc

texto = input("Introduce tu texto porfavor: ")

textop = texto.lower()



#combierto el texto en una lista

lista = list(textop)

lista_palabra = textop.split(" ")

print(lista_palabra)

print(len(lista_palabra))