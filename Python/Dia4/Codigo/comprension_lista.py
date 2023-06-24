palabra = "python"

lista = []

for letra in palabra:
    lista.append(letra)
    
print(lista)





###  Otra forma #####

lista2 = [ff for ff in "java"]
print(lista2)

lista3 = [n if n*2 > 10 else "no" for n in range(0,21,2)]
print(lista3)



## Ejmplo Practico ##

pies = [10,20,30,40,50]
metros = [p /3.281 for p in pies]

print(metros)
