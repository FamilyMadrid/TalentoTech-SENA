#Escribir texto en un archivo
lista = ["Samir", "Lorena", "Maria", "Juan"]

# Abrir el archivo en modo escritura
with open("escribir.txt", "w") as archivo:
    for linea in lista:
        archivo.write(linea + "\n")