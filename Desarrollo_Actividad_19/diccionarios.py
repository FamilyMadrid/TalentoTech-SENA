# Crear un diccionario con los nombres y calificaciones de tres estudiantes
estudiantes = {
    "Ana": 85,
    "Luis": 92,
    "Carla": 78
}

# Encontrar el estudiante con la calificación más alta
mejor_estudiante = max(estudiantes, key=estudiantes.get)
calificacion_mas_alta = estudiantes[mejor_estudiante]

# Imprimir el nombre del estudiante con la calificación más alta
print(f"El estudiante con la calificación más alta es {mejor_estudiante} con una calificación de {calificacion_mas_alta}")