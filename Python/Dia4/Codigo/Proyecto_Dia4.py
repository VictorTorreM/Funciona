from random import *

Nombre_Jugador= input("Hola introduce tu nombre para poder jugar: ")

print(f"Hola {Nombre_Jugador},he pensado un numero entre el 1 y el 100, tienes 8 intentos para adivinarlo ")

sn = input("Empezamos s/n ").lower()

numero_secreto = randint(1,100)
# print(numero_secreto)
turno = 1
if sn == "n":
    print("Que te follen vas jugar igual")
    
while turno <9:
    numero = int(input(f"Turno {turno}: "))
    turno += 1
    if numero not in range(1,101):
        print("Introduce un numero valido")
        continue
    if numero > numero_secreto:
        print("El numero que buscas es menor")
    if numero < numero_secreto:
        print("El numero que buscas es mayor")
    if numero == numero_secreto:
        turno -= 1
        print(f"Enhorabuena {Nombre_Jugador} has acertado el numero secreto en solo {turno} turnos")
        break
    if turno == 9:
        print(f"No has podido adivinar el numero en los turnos establecidos eres un puto subnormal de mierda {Nombre_Jugador} \nEl numero es {numero_secreto}")           

         
    