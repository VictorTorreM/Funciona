def devolver_distintos(num1,num2,num3):
    suma = num1 + num2 + num3
    lista = [num1,num2,num3]
    if suma >15:
        return max(lista)
        
    elif suma < 10:
        
        return min(lista)
    
    elif suma <= 15 and suma >= 10:
        lista.pop(lista.index(max(lista)))
        lista.pop(lista.index(min(lista)))
        return lista
    


print(devolver_distintos(1,10,2))