# Los diccionarios no tienen un orden específico ni tampoco un índice
#Si quieres almacenar datos para encontrarlos sin hacer falta de saber el lugar exacto sino la relación con otro concepto
#La sintaxis es {clave,valor,clave2,valor2} . las claves NO SE PUEDEN REPETIR , los VALORES SI 

diccionario = {"c1":"Valor1","c2":"Valor2"}
print(type(diccionario))
print(diccionario)

#Para consultar el valor de una clave
#Solo hace falta saber el valor

resultado = diccionario["c1"]
print(resultado)

#Ejemplo practico

cliente = {"nombre":"juan","Apellido":"Fuentes","peso":76,"altura":186}

consulta = (cliente["nombre"])

print(consulta)

#Un diccionario puede incluir listas o incluso diccionarios dentro de uno mimso 

dic1 = {"c1":55,"c2":[10,20,30],"c3":{"s1":"Macarrones","s2":"tomate"}}

print(dic1["c3"]["s2"])

#Ejercicio práctico 

dic2 = {"c1":["a","b","c"],"c2":["d","e","f"]}

print(dic2["c2"][1].upper())


#Para agragar elementos a un diccionario ya creado 

dic3 = {1:"a",2:"b"}
print(dic3)
dic3[3] = "c"
print(dic3)

dic3[2] = "B"
print(dic3)

#Para ver SOLO las CLAVES de un diccionario 

print(dic3.keys())

#Para ver SOLO los VALORES de un diccionario

print(dic3.values())

#Para imprimirlo TODO

print(dic3.items())