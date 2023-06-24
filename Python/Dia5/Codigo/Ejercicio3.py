def verificar_duplicados_consecutivos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

lista = [1,1,0,1,32,0,3,21,1,3,3,21,3,1,31,2,35,4]

print(verificar_duplicados_consecutivos(*lista))  # True
