import os 


ruta = "C:\\Users\\vtorrela\\Desktop\\CAPIBARAS"
elemento = os.path.dirname(ruta)




#Cambiar directorios 
#ruta = os.chdir("Ruta")


#Crear direcotrios
#ruta = os.makedirs("C:\\Users\\vtorrela\\Desktop\\HOLA")


#Devuelve el nombre del archivo de una ruta

# CASA = os.path.basename("RUTA\\ARCHIVO.txt")
# print(CASA) = ARCHIVO.txt

#Devuelve la parte de la ruta 

# CASA = os.path.dirname("RUTA\\ARCHIVO.txt")
# print(CASA) = RUTA\\ARCHIVO\\PODRE

#Devuelve en forma de tuple las dos partes de la ruta

# CASA = os.path.split("RUTA\\ARCHIVO.txt")
# print(CASA) = ("RUTA\\ARCHIVO\\PODRE","ARCHIVO.txt")


#Eliminar directorios 

#os.rmdir("RUTA\\CARPETA")


"""


das


#archivo = open("coso.txt")



#print(archivo.read())
"""



otro_archivo = open("C:\\Users\\vtorrela\\Desktop\\CAPIBARAS\\CAPibaras\\coso.txt")


#con path y las " / " pude funcionar en cualquier sistema operativo
from pathlib import Path

carpeta = Path("C:/Users/vtorrela/Desktop/CAPIBARAS/CAPibaras")
archivo = carpeta / "coso.txt"
mi_archivo = open(archivo)
print(mi_archivo.read())

