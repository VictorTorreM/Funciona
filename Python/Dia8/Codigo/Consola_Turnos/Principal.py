from Numeros import *

bucle = True
while bucle == True:
    try:
        
        eleccion = int(input("Escoja su sección: \nCosmética-(1)\nFarmacia-(2)\nPerfumería-(3)\nSalir-(4)\n"))
        
        match eleccion:
            case 1:
                generador_numero_c()
                otro = input("\nDesea escoger otro turno? S/N\n").lower()
                if otro == "s":
                    eleccion = 0
                else:
                    bucle = False
            case 2:
                generador_numero_f()
                otro = input("\nDesea escoger otro turno? S/N\n").lower()
                if otro == "s":
                    eleccion = 0
                else:
                    bucle = False
            case 3:
                generador_numero_p()
                otro = input("\nDesea escoger otro turno? S/N\n").lower()
                if otro == "s":
                    eleccion = 0
                else:
                    bucle = False
            case 4:
                bucle = False
    
            case 0:
                eleccion = int(input("Escoja su sección: \nCosmética-(1)\nFarmacia-(2)\nPerfumería-(3)\nSalir-(4)\n"))
    except ValueError:
        print("Introduzca un numero")