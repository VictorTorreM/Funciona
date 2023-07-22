import os

import shutil
import send2trash


"""
print(os.getcwd())


archivo = open("curso.txt","w")

archivo.write("texto de prueba")

archivo.close

print(os.listdir())




shutil.move("curso.txt","C:\\Users\\Víctor\\Desktop")


send2trash.send2trash("curso.txt")



"""



ruta = "C:\\Mi_Gran_Directorio"
for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")
    
