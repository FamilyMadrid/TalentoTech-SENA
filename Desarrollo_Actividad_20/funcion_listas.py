# Funcion con parámetros de tipo lista

def suma(lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x]
        return suma

def mayor(lista):
    recorrer = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > recorrer:
            recorrer = lista[x]
    return recorrer


# Principal
lista_de_valores = [12, 3, 6, 78, 45, 24, 776]
print(f"La lista completa es: {lista_de_valores}")
print("La suma de todos los elementos es: ", sum(lista_de_valores))
print("El número mayor de la lista es: ", mayor(lista_de_valores))