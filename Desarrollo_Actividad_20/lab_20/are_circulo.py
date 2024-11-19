import math

def area_circulo(radio):
    return math.pi * radio ** 2

radio = int(input("Ingrese el valor del radio: "))
print(f"El área del circulo con radio {radio} es: {area_circulo(radio):.2f}")