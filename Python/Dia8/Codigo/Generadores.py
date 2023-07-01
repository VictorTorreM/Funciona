
"""
def funcion():
    lista = []
    
    for x in range(1,5):
        lista.append(x*10)
    return lista

def generador():
    for x in range(1,5):
        yield x * 10


print(funcion())


g= generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

"""
"""

def mi_generador():
    x = 1
    yield x
    
    x += 1
    yield x
    x += 1
    yield x
    
g= mi_generador()

print(next(g))
print(next(g))
print(next(g))

"""
"""
def mi_generador():
    x = 0
    while True:
        x += 1
        yield x
    
generador = mi_generador()

while True:
    print(next(generador))


""" 


def g():
    x = 0
    while True:
        x += 1
        yield x*7
    

generador= g()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
