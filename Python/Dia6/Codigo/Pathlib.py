from pathlib import Path, PureWindowsPath

#Con Path no hace falta ni abrir ni cerrar el archivo 

carpeta = Path("C:/Users/vtorrela/Desktop/CAPIBARAS/CAPibaras/csoso.txt")


rutawin= PureWindowsPath(carpeta)
#print(carpeta.read_text())

if not carpeta.exists():
    print("No esiste")
else:
    print("Esiste")
    
print(rutawin)