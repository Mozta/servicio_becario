archivo=open("Tabla.txt","r+")
content=archivo.read()
finDelArchivo=archivo.tell()

archivo.write("Nuevo texto en linea 1")
archivo.seek(finDelArchivo)
newContent=archivo.read()

archivo.close()

print (newContent)
