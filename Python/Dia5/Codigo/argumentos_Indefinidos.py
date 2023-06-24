def suma(*args):
    total = 0
    for arg in args:
        total += arg**2
    return total
        

def suma_absolutos(*args):
    total = 0
    for numero in args:
        if numero <= 0:
            numero = numero* -1
            total += numero
        else:
            total += numero
    return total
        

def numeros_persona(nombre,*args):
    suma_numeros = 0
    for numero in args:
        suma_numeros += numero
    return print(f"{nombre}, la suma de tus números es {suma_numeros}")
    
nombre = "Federico"
numeros_persona("nombre",75,20,65)