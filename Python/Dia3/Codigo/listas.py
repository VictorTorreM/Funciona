# las listas se escriben entre [] pueden tener tanto numeros y letras, no son inmutables 

otra_lista = ["hola",10,9.32]
lista2 = ["pollo","pimientos",98]
lista3 = otra_lista+ lista2

print(type(otra_lista))

#para ver cuantos elementos tiene una lista

print(len(otra_lista))

#extraer el una posicion en concreto como con los strings

print(otra_lista[0])

#Se pueden concatenar listas tambien

print(otra_lista+lista2)
print(lista3)

#Se pueden alterar los elementos de la lista no como los strings

lista3[0] = "Lentejas"

print(lista3)

#Añadir elementos a la lista original con .append(lo que quieras añadir "texto" o num)
lista3 = lista3.append("macarrones")


#para eliminar un elemento de la lista si no eliges ningun parámetro elimina el último elemento de la lista

lista4 = lista2.pop()
print(lista4)

#Se puede guardar el elemento eliminado en una variable

eliminado = otra_lista.pop(0)

print(eliminado)
print(otra_lista)

#Para ordenar listas (trabaja en el sitio no devuelve nada)
#Por ejemplo no se puede hacer    listaoredenada= listadesordenada.sort()

l1 = ["c","a","d","b","e"]

print(l1)

#Para invertir el orden

l1.reverse()
print(l1)


python = "python" in "Hola esto es el mundo de python"

dic = {True:"Aparece",False:"No aparece"}


print(dic[python])