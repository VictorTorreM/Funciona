#Son como las listas e inmutables 
#Ocupan mennos espacio (Son más eficientes) y al no poder ser modificados son a prueba de daños
#La sintaxis es    nombre = (cosa,cosa,cosa) *No hacen falta los paréntesis*
mi_tuple = (1,2,3,4)

#Pueden tener lo que sea dentro 

t = (12,33.3,"hola")

print(type(mi_tuple))

#Se puede seccionar 

print(mi_tuple[0])


#No se pueden modificar los tuples
#Se pueden anidar

t2 = (1,2,(3,5),4)

print(t2[2][1])

#Se puede transformar en listas

t2 = list(t2)
print(type(t2))

t2 = tuple(t2)
print(type(t2))

#Se puede asignar el contenido de un tuple a diferentes variables igual que con diccionarios y listas (debe tener el mismo numero de variables y valores) 


t3 = (1,2,3)

x,y,z = t3

print(x,y,z)


#
t4 = (1,2,3,1)

#Puedes contar las veces que aparece un valor dentro de un tupple

print(t4.count(1))
#Puedes consultar en que posicion se encuentra un valor 

print(t4.index(2))