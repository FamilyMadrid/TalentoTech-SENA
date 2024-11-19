# Programa presentación en pantalla

def presentacion():
    print("Durante esta sesión vamos a cargar dos valores por parte del usuario.")
    print("Se realizará la operación suma y resta")
    print("++++++++++++++++++++++++++++++++++++++++++++++")

def operaciones():
    valor_1 = int(input("Ingrese el primer valor: "))
    valor_2 = int(input("Ingrese el segundo valor: "))
    suma = valor_1 + valor_2
    resta = valor_1 - valor_2
    print(f"La suma de los dos números es: {suma}")
    print(f"La resta de los dos números es: {resta}")

def finalizar():
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("Gracias por usar este programa... Dios te bendiga")

# Principal
presentacion()
operaciones()
finalizar()