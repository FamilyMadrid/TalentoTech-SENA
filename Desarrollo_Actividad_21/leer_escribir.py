#Leer y escribir en un archivo de texto existente
with open("Saludo.txt", "r") as archivo:
    mensaje = archivo.read()
    mensaje += "\n Programa Ivan Madrid"
#Modifica contenido
with open("Saludo.txt", "w") as archivo:
    archivo.write(mensaje)