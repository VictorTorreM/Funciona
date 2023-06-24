texto = "Este es el texto de Viti"

print(texto)

#Cambia los strings a mayusc se escribe .upper()
resultado = texto.upper()
print(resultado)
 #Si usas texto[2].upper() cogera el 2 caracter y lo pondrá en mayusc
 
 #Cambia el texto a minusc
 
resultado = texto.lower()
print(resultado) 

#Separa cada palabra en elementos por defecto se usa como separador los espacios 
# pero lo puedes cambiar poniendo un caracter en concreto entre parentesis

resultado = texto.split()

print(resultado)

#Para unir se usa   lo que quieres entre palabras.join() por ejemplo un "-" tambien se puede con espacios

a = "Hola"
b = "Soy"
c = "Viti"
d = "-".join([a,b,c])
print(d)

#Buscar un determinado caracter dentro de una string 
#La diferencia entre find e index es que find no da un error si no encuentra lo que busca, devuelve -1 por ejemplo

resultado = texto.find("g")
print(resultado)

#Para reemplazar palabras o caracteres se usa .replace("Lo que quieres cambiar","cambio") por ejemplo
#Importante que diferencia entre mayusc y minus

resultado = texto.replace("Viti","gochon")
print(resultado)

resultado = texto.replace("e","o")
print(resultado)

#para cambiar los espacios por -

resultado = texto.replace(" ","-")
print(resultado)