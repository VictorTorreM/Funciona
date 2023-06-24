def funcion_pepi(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra)
    lista = list(set(lista))
    return print(sorted(lista))

funcion_pepi("entretenido")