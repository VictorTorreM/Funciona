#Los strings son inmutables, se pueden concatenar e incluso multiplicar

n1 = "Hola "

print(n1 * 3)

# Con """ puedes hacer saltos de linea dentro de un string con el enter

poema = """Oh el mar 
hogar del calamar """

print(poema)

#Para comprobar si dentro de un string existe algun caracter o palabra concreta (Es un valor buleano[si,no])

print("mar"in poema)

print("sal"not in poema)

#Para conocer el largo de una String con len("Texto" o variable)

print(len(poema))