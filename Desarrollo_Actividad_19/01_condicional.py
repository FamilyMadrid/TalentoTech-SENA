# Escribir un programa que solicite al ususario un número por teclado y determine si es par o impar. Mostrar un mensaje adecuado en cada caso. 

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("El número ingresado es Par")
else:
    print("El número ingresado es Impar")
    
