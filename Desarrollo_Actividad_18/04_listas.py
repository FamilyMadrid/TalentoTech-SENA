# Trabajar con listas
# a. Crea una lista que contenga al menos dieselementos de diferentes tipos.
# b. Accede y modifica elementos de la lista. 
# c. Agrega un nuevo elemento a lista y luego imprime la lista completa.
# d. Elimina un nuevo elemento de la lista y luego imprime la lista completa.

lista_variada = [10, "Ivan", True, 1.64, (2+2), False]

print(lista_variada)
print(lista_variada[4])

# Accediendo y modificando elementtos de la lista
lista_variada[4] = 5
print(lista_variada)

# Agregando elemento e imprimiento la lista
lista_variada.append("Esteban")
print(lista_variada)

# Eliminando nuevo elemento e imprimiendo la lista
lista_variada.pop()
lista_variada.remove("Ivan")
print(lista_variada)
