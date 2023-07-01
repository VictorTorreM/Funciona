def decorador_mensajes(func):
    
    generador = func()
    def wrapper():
        if  True:
            print("Su turno es:")
            numero = next(generador)
            print(numero)
            print("Será atendido enseguida")
    return wrapper



@decorador_mensajes
def generador_numero_p():
    x = 0
    while True:
        x += 1
        yield f"P {str(x).zfill(2)}"

@decorador_mensajes
def generador_numero_f():
    x= 0
    while True:
        x += 1
        yield f"F {str(x).zfill(2)}"

@decorador_mensajes
def generador_numero_c():
    x = 0
    while True:
        x = x+1
        yield f"C {str(x).zfill(2)}"
        
