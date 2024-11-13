# 5. Uso de diccionarios
# a. Crea un diccionario que contenga información sobre una persona(nombre, edad, ciudad y profesión).
# b. Accede y modifica los valores dentro del diccionario.
# c. Agrega un nuevo par clave-valor al diccionario e imprime el diccionario completo.


# a. Crea un diccionario que contenga información sobre una persona(nombre, edad, ciudad y profesión).
persona = {
    "nombre": "Ivan",
    "Apellido": "Madrid", 
    "edad": 39,
    "ciudad": "Valledupar",
    "profesion": "Sotfware Developer"
}

# b. Accede y modifica los valores dentro del diccionario.
print(persona)
persona["nombre"] = "Esteban"
persona["edad"] = 8
print(persona)

# c. Agrega un nuevo par clave-valor al diccionario e imprime el diccionario completo.
print(persona)
persona["pais"] = "Colombia"
print(persona)