x = 1
suma = 0
while x <= 10:
    valor = int(input("Ingrese un valor: "))
    suma = suma + valor
    x = x + 1
    promedio = suma / 10
    
print(f"La suma es {suma}")
print(f"El promedio es {promedio}")