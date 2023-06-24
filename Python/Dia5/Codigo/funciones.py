#Las funciones nos permiten reutilizar bloques de código de forma sencilla, en otros lugares y sin volver a escribirlo entero.

#La sintaxis es def "nombre_funcion" (): [Una buena practica es añadir una descripcion de cada funcion despues de los :]

def saludar_persona(nombre):
    """
    Esta funcion sirve pa saludar a la people
    """
    print("Hola "+ nombre)
    
    
saludar_persona("Victor")

#Con return podemos almacenar el resultado de la función en una variable 

def multiplicar (numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,10)

print(resultado)

#Relacionar las funciones con otros objetos 

def mira_3_cifras(lista):
    lista_3_cifras = []
    for numero in lista:
        if numero in range(100,1000):
            lista_3_cifras.append(numero)
        else:
            pass
    return lista_3_cifras

def todos_positivos(lista):
    for numero in lista:
        if numero <0:
            return False
    return True



"""
def sumarda(lista1):
    suma = 0
    for  n in lista1:
        if n in range(1,1001):
         suma = suma + n 
    return print(suma)
    
lista1 = [1,2,3]
"""

def suma_menores(lista):
    suma = 0
    for numero in lista:
        if numero in range(1,1000):
            suma = numero + suma
    return suma
     
# lista_numeros = [1,50,500,5000,750]   

def cantidad_pares(lista):
    cuenta = 0
    for n in lista:
        if n%2 == 0:
            cuenta += 1
    return cuenta

lista_numeros = [1,50,502,755,34]
print(cantidad_pares(lista_numeros))
