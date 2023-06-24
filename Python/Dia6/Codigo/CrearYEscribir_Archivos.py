
#Si abres un archivo con w o a y no existe python lo crea 

arhivo = open("Prueba1.txt","a")

#con write puedes poner un string pero con writelines puedes pasar una lista, no escribe en lineas distintas solo las concatena todas juntas.

#arhivo.writelines(["Hola","Mundo","Aqui","Toy"])


#lista = ["Hola","Mundo","Aqui","Toy"]
#for p in lista:
#    arhivo.writelines(p+ "\n")
esctibir = input("Que escribnes")

arhivo.write(esctibir)


arhivo.close()