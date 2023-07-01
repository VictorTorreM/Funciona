"""
def suma():
    n1 = int(input("Numero 1 "))
    n2 = int(input("Numero 2 "))
    print(n1 + n2)
    print("Gracuas por sumar"+ n1)
    
"""


def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"ingresasnte el numero {numero}")
            break
    print("Gracias")
    
pedir_numero()



"""
try:
    #codigo que queremos probar
    suma()
except TypeError:
    #codigo a ejecutar si hay un error
    print("Estas intentado concatenar tipos distintos")
except ValueError:
    print("Ese non es un numero cateto")
else:
    #codigo a ejecutar si no hay un error 
    print("Buena no eres down")
finally:
    #codigo que se va a ejecutar de todos modos
    print("Eso fue todo")
"""