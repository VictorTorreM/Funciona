#solo admiten elementos UNICOS y no están ordenados en indices, no admite ni listas ni diccionarios pero si tuples 

#se puede hacer con

mi_set = set([1,2,3,4,5])

print(type(mi_set))

print(mi_set)
# o de la siguiente manera

otro_set = {1,2,3}

print(type(otro_set))

print(otro_set)

#No se pueden modificar los elementos de un set 

set_repe = set([1,2,3,1,1,1,1,1,2,5])
print(set_repe)

set_tuple= set([1,2,3,(1,2)])

print(set_tuple)

#Para ver el largo de los sets 

print("Set con tuple: ")
print(len(set_tuple))

#Se pude saber si un valor se encuentra en un set (devuelve un  booleanos )

print(2 in mi_set)

#unir sets

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)

print(s3)

# Para agregar valores a los sets
s1.add(4)

print(s1)

#para eliminar

s1.remove(3)
print(s1)

#Hace lo mismo que remove pero si no existe el valor que quieres eliminar no da error

s1.discard(6)

#Pop elimina un elemento aleatorio

sorteo = s1.pop()

print(sorteo)

#Para vaciar el set 

s1.clear()