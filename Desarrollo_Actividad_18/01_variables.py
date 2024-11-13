# 1. Declaración de variables:
# a. Crea variables de tipo string, int, float y boolean. 
# b. Captura por teclado los valores.
# c. Imprime cada una de las variables en la consola.

# Creación de variables
nombre = "Ivan"
apellido = "Madrid"
edad = 39
peso = 67
estatura = 1.64
meta_ingresos = 2.400
estoy_casado = True
tengo_hija = False

# Captura valores por teclado

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en Kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))
meta_ingreso = float(input("Ingresa tu meta salarial en dolares: "))

print(f"Mi nombre es: {nombre} {apellido}, tengo {edad} años y mi meta salarial es de {meta_ingreso:.2f} dolares")

print(nombre)
print(apellido)
print(edad)
print(peso)
print(estatura)
print(f"{meta_ingresos:.3f}")
print(estoy_casado)
print(tengo_hija)