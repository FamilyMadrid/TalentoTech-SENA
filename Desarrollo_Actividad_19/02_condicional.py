# Escribir un programa que pida ingresar por teclado un número positivo de uno, dos o tres digitos. Mostrar un mensaje indicando si el número tiene uno, dos o tres dígitos. 

# Solicitando al usuario ingresar el número
numero = int(input("Ingrese un número positivo de uno, dos o tres dígitos: "))

# Condicional para selección dígitos
if numero >= 0 and numero < 10:
    print(f"El número ingresado es de un dígito y es: {numero}")
elif numero >= 10 and numero < 100:
    print(f"El número ingresado es de dos dígitos y es: {numero}")
elif numero >= 100 and numero < 1000:
    print(f"El número ingresado es de tres dígitos y es: {numero}")
else:
    print("El número ingresado no es válido. Ingrese un número positivo de uno, dos o tres dígitos")
