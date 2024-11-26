#Abrir archivos binarios
with open("logo_upc.png", "rb") as archivo:
    datos_binarios = archivo.read()
with open("copia_logo_upc.png", "wb") as archivo_copia:
    archivo_copia.write(datos_binarios)