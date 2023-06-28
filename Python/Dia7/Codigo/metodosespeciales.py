class CD:
    
    
    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor} y tiene {self.canciones} Tracks"
    
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD("Iron Maiden","7th son of a 7th son",25)

print(mi_cd)
