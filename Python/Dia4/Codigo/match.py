##Es como un switch case en java
"""
serie = "N-02"


match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe estre producto")"""
        

cliente = {"nombre":"Federico",
           "edad":45,
           "ocupacion":"instructor"}


pelicula= {"titulo":"Matrix",
           "Ficha_tecnica":{"prota":"Keanu reeves",
                            "Director":"Lana y lilly wachowski"}}

elementos = [cliente,pelicula,"libro"]

##Puede detectar patrones 


for e in elementos:
    match e:
        case {"nombre":nombre,
              "edad":edad,
              "ocupacion":ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo":titulo,
              "Ficha_tecnica":{"prota":prota,
                               "Director":director}}:
            print("Es una pelicula")
            print(titulo,prota,director)
        case _:
            print("No se que es eso")