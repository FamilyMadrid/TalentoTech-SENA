# Escribir un programa que permita al usuario ingresar el nombre de un estudiante y su calificación. Si el estudiante ya existe en el diccionario, actualizar la calificación; si no existe, agragarlo al diccionario. Finalmente, mosrar todos los estudiantes y sus calificaciones. 

estudiantes = {}

while True:
    # Solicitar el nombre del estudiante y su caificación
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break #Termina el bluce si el usuario escribe salir
    
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    
    # Verificar si el estudiante ya existe en el diccionario
    if nombre in estudiantes:
        print(f"{nombre} ya existe en el diccionario. Actualizando la calificación.")
    else:
        print(f"{nombre} no existe en el diccionario. Agregando al diccionario.")
        
    # Aregar o actualizar la calificación en el diccionario
    estudiantes[nombre] = calificacion
    
    # Mostrar todos los estudiantes y sus nombres
    
print(f"\nEstudiantes y sus calificaciones")
for nombre, calificaciones in estudiantes.items():
    print(f"{nombre}: {calificacion}")
    
    