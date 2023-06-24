nombres = ["Juan","Ana","Carlos","Belen","Fran"]

#Dentro del for usamos una variable interna que puede tener cualquier nombre, por ejemplo salchichon
"""
 for  salchichon in nombres:
    numero_nombre = nombres.index(salchichon) + 1
    print(f"Nombre {numero_nombre} : {salchichon}" )
    
"""
"""
for nombre in nombres:
    if nombre.startswith("A"):
        print(nombre)
        
        
"""
"""
numeros =[1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)




for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
"""
"""
dic = {"clave1":1,"clave2":2,"clave3":3}

for a,b in dic.items():
    print(a,b)
    
"""  
"""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares =0 
cosa = 0
for numero in lista_numeros:
    cosa = numero % 2
    if cosa == 0:
        suma_pares = suma_pares + numero
        print(suma_pares)
    else:
        suma_impares = suma_impares + numero 
        print(suma_impares)
        
                
"""
"""
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:print(f"No tengo mas dinero")

"""
"""
respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres seguir (s/n) " )
else: print("Gracias")
"""
"""
respuesta = "s"

while respuesta== "s":
    pass


print("Hola")
"""
"""
xd = input("Tu nombre: ")

for letra in xd:
    if letra == "r" :
        break
    print(letra)
    """
"""
xd = 50

while xd > -1:
    if xd%5 == 0:
        print(xd)
        xd -= 1
    else: xd -= 1   """

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if int(numero) >= 0:
        print(numero)
    else: break