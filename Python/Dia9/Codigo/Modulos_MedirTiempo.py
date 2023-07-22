import timeit

declaracion = """
pruebaf(10)
"""
mi_setup = """
def pruebaf(numero):
    lista = []
    for n in range(1,numero+1):
        lista.append(n)
    return lista
"""

duracion =timeit.timeit(declaracion,mi_setup,number=1000000)

print(duracion)


declaracion2 = """
pruebaw(10)
"""
mi_setup2 = """
def pruebaw(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""
duracion2 =timeit.timeit(declaracion2,mi_setup2,number=1000000)
print(duracion2)