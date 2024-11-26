#Manejo de exepciones
try:
    with open("exepcion.txt", "r") as archivo:
        mensaje = archivo.read()
        print(mensaje)
except FileNotFoundError:
    print("EL archivo no existe....")
except IOError:
    print("Ocurrió un error al leer el archivo...")