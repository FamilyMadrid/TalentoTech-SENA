numeros_mayores_mil = 0
numeros_menores_mil = 0
cantidad_valores_ingresados = int(input("¿Cuantos valores desea ingresar?: "))
for x in range(cantidad_valores_ingresados):
    valor_ingresado = int(input("Ingrese un valor: "))
    if valor_ingresado >= 1000:
        numeros_mayores_mil = numeros_mayores_mil + 1 
    else:
        numeros_menores_mil = numeros_menores_mil + 1 
        
        
print(f"La cantidad de números ingresados mayores o iguales a 1000 son: {numeros_mayores_mil}")
print(f"La cantidad de números ingresados menores a 1000 son: {numeros_menores_mil}")