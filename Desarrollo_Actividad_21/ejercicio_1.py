# Leer un archivo

with open('Saludo.txt','r') as archivo:
    #Leer cada línea del archivo
    for linea in archivo:
        print(linea.strip())