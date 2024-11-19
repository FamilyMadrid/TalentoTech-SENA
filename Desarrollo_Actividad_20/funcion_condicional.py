# Programa que muestre el mayor de tres números

def mayor(v1, v2, v3):
    if v1 > v2 and v1 > v3:
        print(f"El número mayor es: {v1}")
    else:
        if v2 > v3:
            print(f"El número mayor es: {v2}")
        else:
            print(f"EL número mayor es: {v3}")

def solicitud():
    print("Vamos a identificar el número mayor dentro de tres números.")
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    mayor(valor1, valor2, valor3)

# Principal
solicitud()