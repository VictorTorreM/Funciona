#Los decoradores son funciones que cambian el 
#comportamiento de otras funciones


def decorar_saludo(funcion):
    
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion


def may(texto):
    print(texto.upper())




def min(texto):
    print(texto.lower())
    
    
    

mayusc_decorada = decorar_saludo(may)


mayusc_decorada("viti")