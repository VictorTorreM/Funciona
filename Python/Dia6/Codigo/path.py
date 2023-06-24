from pathlib import Path

base = Path.home()

guia = Path(base ,"Europa","España",Path( "Barcelona","Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")


#print(guia.parent)



guia3 = Path(Path.home(),"Europa")

#Con **/* busca dentro de todos los directorios

for txt in Path(guia3).glob("**/*.txt"):
    print(txt)

