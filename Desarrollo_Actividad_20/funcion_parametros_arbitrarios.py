# Función con parámetros arbitrarios
def promedio(*numeros): # Se coloca el asterisco para que la función sepa que recibira una lista de números
    return sum(numeros)/len(numeros)
print(f"El promedio es: {promedio(10, 20, 30,)}")
print(f"El promedio es: {promedio(4, 7, 9, 2, 3, 8)}")