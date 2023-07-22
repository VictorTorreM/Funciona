import os
import time
import datetime
import math
import re
from pathlib import Path

inicio = time.time()

ruta = "C:\\Mi_Gran_Directorio"
n_serie= r"N\D{3}-\d{5}"
hoy = datetime.date.today()


nros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo,patron):
    este_archivo = open(archivo,"r")
    texto = este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ""
    
    


def crear_listas():
    for carpeta,subcarpeta,archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a),n_serie)
            if resultado != "":
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0 
    print("-"*50)
    print(f"Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    for a in archivos_encontrados:
        print(f"{a}\t{nros_encontrados[indice]}")
        indice += 1
    print("\n")
    print(f"Números encontrados: {len(nros_encontrados)}")
    final = time.time()
    duracion = final - inicio
    
    print(f"Duracion de la busqueda: {math.ceil(duracion)} Segundos")
    print("-"*50)




crear_listas()

mostrar_todo()














"""
                                    MI INTENTO


ruta = "C:\\Mi_Gran_Directorio"
n_serie= r"^N\D{3}-\d{5}"


def generador_rutas(ruta):
    for root, dirs, files in os.walk(ruta):
        for name in files:
            ruta2= os.path.join(root, name)
            yield ruta2



def abridor(ruta):

    archivo = open(ruta,"r")
    texto = archivo.read()
    archivo.close()
    return texto
    








def buscador(texto,nserie):
    return re.search(texto,nserie)

for n in range (1,41):
    generador = generador_rutas(ruta)
    abierto = abridor(next(generador))
    print(abierto)
    """