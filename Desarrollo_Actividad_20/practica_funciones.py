import math

def area_circulo(radio):
    return math.pi * radio ** 2

radio = int(input("Ingrese el valor del radio: "))

print(f"EL área del circulo es: {area_circulo(radio):.2f}")
