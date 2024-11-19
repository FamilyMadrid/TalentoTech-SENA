def funcion_descuento(precio, descuento):
    precio_final = precio - (precio * 0.1)
    return precio_final

valor = int(input("Ingrese el precio del producto: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: ") or 0.1)
print(f"EL precio final es: {funcion_descuento(valor, porcentaje_descuento)}")

