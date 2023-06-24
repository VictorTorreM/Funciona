precios_cafe = [("Capp",1.20),("expreso",1.10),("Cortado",1)]



def cafe_mas_caro(lita_precios):
    
    precio_mayor = 0
    cafe_mas_caro = ""
    
    for cafe,precio in lita_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro= cafe
        else: 
            pass
        
    return(cafe_mas_caro,precio_mayor)


cafe, precio = cafe_mas_caro(precios_cafe)

print(f"el cafe mas caro es {cafe} cuyo precio es {precio}")