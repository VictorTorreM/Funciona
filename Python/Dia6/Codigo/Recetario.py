import os
from os import system,remove
from pathlib import Path, PureWindowsPath


ruta_recetario = Path.home()/"Recetas"

salir_recetario = False 

#print(ruta_recetario)
elecion = 0



### Primera opcion pregunta categoria(Las muestra) y que receta de esa categoria quiere(Las muestra tambien) leer.
#### De argumentos tiene el n de opcion y la ruta 

def Primera_Opcion(ruta_recetario,elecion):
    for dir in ruta_recetario.iterdir():
            
        print(dir)
    categoria = input("Que categoría quires consultar?\n")
    ruta_recetario = ruta_recetario/categoria
    for txt in ruta_recetario.glob("**/*.txt"):
        print(txt)
    os.chdir(ruta_recetario)
    usuario= input("Que receta quieres leer?\n")
    archivo = open(f"{usuario}.txt","r")
    print(archivo.read())
    archivo.close()
    inicio= input("Volver al inicio? S/N").upper()
    if inicio == "S":
        elecion = 0
        return elecion 
    
### Segunda opcion pregunta de que categoria quieres crear la receta , el nombre y el contenido.
#### De argumentos tiene el n de opcion y la ruta 1

def Segunda_Opcion(ruta_recetario,elecion):

    for dir in ruta_recetario.iterdir():
        print(dir)
    categoria = input("De que categoría será la receta?\n")
    ruta_recetario = ruta_recetario/categoria
    archivo = open(ruta_recetario/input("Como se va a llamar la receta?"),"w")
    contenido= input("Escribe la receta \n")
    archivo.write(contenido)
    inicio= input("Volver al inicio? S/N").upper()
    if inicio == "S":
        elecion= 0
        return elecion

### Tercera opcion pregunta el nombre de una categoria para crearla 

def Tercera_Opcion(ruta_recetario,elecion):
    ruta_Crear = input("Nombre de la categoria a crear:\n")
    carpeta = os.makedirs(f"{ruta_recetario}/{ruta_Crear}")
    inicio= input("Volver al inicio? S/N").upper()
    if inicio == "S":
        elecion= 0
        return elecion


def Cuarta_Opcion(ruta_recetario,elecion):
    
        for dir in ruta_recetario.iterdir():
            
            print(dir)
        categoria = input("Que categoría quires consultar?\n")
        ruta_recetario = ruta_recetario/categoria
        for txt in ruta_recetario.glob("**/*.txt"):
            print(txt)
        receta= input("Qué receta quieres eleminar?"+"\n")
        remove(f"{ruta_recetario}/{receta}.txt")
        inicio= input("Volver al inicio? S/N").upper()
        if inicio == "S":
            elecion= 0
            return elecion


def Quinta_Opcion(ruta_recetario,elecion):
    for dir in ruta_recetario.iterdir():
        print(dir)
        categoria = input("Que categoría quieres eliminar?\n")
        os.rmdir(f"{ruta_recetario}/{categoria}")
        inicio= input("Volver al inicio? S/N").upper()
    if inicio == "S":
        elecion= 0
        return elecion


def Sexta_Opcion(salir_recetario):
    if elecion == 6:
        salir_recetario = True
    return salir_recetario



while salir_recetario == False:

    match elecion:
        case 1:
            
            elecion = Primera_Opcion(ruta_recetario,elecion)
            system("clear")
            
        case 2:
            
            elecion =Segunda_Opcion(ruta_recetario,elecion)
            system("clear")
            
        case 3:
            
            elecion =Tercera_Opcion(ruta_recetario,elecion)
            system("clear")
            
        case 4:
            
            elecion =Cuarta_Opcion(ruta_recetario,elecion)
            system("clear")
            
        case 5:
            
            elecion =Quinta_Opcion(ruta_recetario,elecion)
            system("clear")
            
        case 6:
            
            salir_recetario = Sexta_Opcion(ruta_recetario)
            system("clear")
            
            
        case 0:
            
            elecion = int(input("""Que opcion elijes ?
1 Consultar receta
2 Crear receta
3 Crear categoria
4 Eliminar receta
5 Eliminar categoria
6 Salir
"""))


