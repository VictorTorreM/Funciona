import shutil
import zipfile

"""
mi_zip = zipfile.ZipFile("archivo_comprimido.zip","w")

mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")

mi_zip.close()



zip_abierto= zipfile.ZipFile("archivo_comprimido.zip","r")

zip_abierto.extractall()

"""



carpeta_origen = "C:\\Users\\Víctor\\Desktop\\Mi_Paquete\\pquete_viti"

archivo_destino = "Todo_comprimido"


#shutil.make_archive(archivo_destino,"zip",carpeta_origen)



shutil.unpack_archive("proyecto+Dia+9.zip","proyecto","zip")