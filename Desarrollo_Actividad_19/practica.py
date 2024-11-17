# Escribe un programa que imprima números del 1 al 5 utilindo el bucle While en Python.

# contador = 1
# while contador <= 10:
#     print(contador)
#     contador += 2

# Ejemplo con entrada de usuario: Un programa que solicita una contraseña hasta que el usuario la escriba correctamente:

# contraseña_correcta = 850904
# contraseña_usuario = int(input("Ingrese la contraseña: "))

# while contraseña_usuario != contraseña_correcta:
#     print("La contraseña ingresada es incorrecta")
#     contraseña_usuario = int(input("Ingrese la contraseña nuevamente: ")) 

# print("Contraseña correcta")


# Como salir de un bucle infinito: Controlando bucles con break y continue

# while True: # Bucle infinito
#     entrada = input("Escribe 'salir' para terminar: ")
#     if entrada == "salir":
#         break
# print("Bucle terminado.")

# Ejemplo con continue:

# contador = 0
# while contador < 5:
#     contador += 1
#     if contador == 3:
#         continue # Saltamos la iteración cuando contador es 3
#     print(contador)

# Crea un bucle que sume números hasta que el usuario escriba "0"

suma_de_numeros = 0

while True:
    try:
        numero_usuario = float(input("Ingrese un número para sumar, o '0' para terminar: "))
        if numero_usuario == 0:
            print(f"Terminaste el programa, el número es: {numero_usuario}")
            break
        suma_de_numeros = suma_de_numeros + numero_usuario
    except ValueError:
        print("El valor ingresado no es acepta, ingrese un número")
print(f"La suma de los número es: {suma_de_numeros}")