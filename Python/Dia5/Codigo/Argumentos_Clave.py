def suma(**kwargs):
    print(type(kwargs))
    




def suma1(num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for arg in args:
        print(f"arg = {arg}") 
    
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [15,50,100,200,400,600]




#suma1(15,50,*args,**kwargs)

def cantidad_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(clave)
        lista.append(valor)
    return lista
    












lista_numeros = [1,2,3,4,5,5,4,3,2,1,80]

def reducir_lista(lista):
    result = []
    
    num_mayor = max(lista)
    index_mayor = lista.index(num_mayor)
    lista.pop(index_mayor)
    
    for numero in lista:    
        if numero not in result:
            result.append(numero)
            
            
    result = list(set(result))
    return result
    










def promedio_lista(lista):
    promedio = 0
    largo = len(lista)
    for n in lista:
        promedio = promedio + n 
    promedio = promedio/largo
    return promedio





from random import randint

def lanzar_moneda():
    
    moneda = randint(1,2)
    jugada = ""
    if moneda == 1:
        jugada = "Cara"
    else:
        jugada = "Cruz"
    
    return jugada
    

lista_numeros = [1,2,3,4,5]
def probar_suerte(jugada,lista):
    if jugada == "Cara":
        lista.clear()
        return print(f"La lista se autodestruirá {lista}")
    
    elif jugada == "Cruz":
        return print(f"La lista fue salvada {lista}")
    
