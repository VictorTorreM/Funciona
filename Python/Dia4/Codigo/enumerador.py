listadsadsa = ["a","b","c"]

indice = 0

#for indice,intem in enumerate(range(50,55)):
#    print(indice, intem)


lista = list("python")
print(lista)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
lista = (list(enumerate(lista_nombres)))

for indice,nombre in lista:
    if nombre.startswith("M"):
        
        print(indice)
    
        