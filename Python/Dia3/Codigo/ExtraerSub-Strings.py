
#Para extraer desde un caracter hasta  otro (Sin  incluir ) por ejemplo [2:6] coge desde el 2 hasta eL 5 porque el 6 no lo coge, si no se completa python
#comprende que es hasta el final.

texto = "ABCDEFGHIJKLMNOPQRSTVWXYZ"
fragmento = texto[2:5]
print(fragmento)

#Con [x:x:2] haces que solo coja cada 2 caracteres
print(texto[0::2])


#Puedes hacer que le de la vuelta al texto que quieras con [x:x:-1]

print(texto[::-1])