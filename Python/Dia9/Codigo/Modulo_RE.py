import re



texto = "Si necesitas ayuda llama al (763)-000-1239 las 24 horas del dia al servicio de ayuda online"


"""
patron = "ayuda"

busqueda = re.findall(patron,texto)

for n in re.finditer(patron,texto):
    print(n.span())
"""



texto2 = "llama al 674-879-3213 ya mismo"

patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

resultado2 = re.search(patron, texto2)

#print(resultado2.group())


#clave = input("Clave: ")

#patron = r"\D{1}\w{7}"

#chequear = re.search(patron, clave)

#print(chequear)


texto3 = "No atendemos los lunes por la tarde"

mail = "pepitojuarez@gmail.com.br"

buscar = re.findall(r"[^\s]+",texto3)



patron = re.search(r"\w{1,}@\w{1,}.com|com.br",mail)


print(patron)





