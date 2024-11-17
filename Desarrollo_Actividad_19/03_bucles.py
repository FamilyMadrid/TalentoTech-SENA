# En una empresa trabajan "n" empleados, cuyos sueldos oscilan enter $1.000.000 y $5.000.000, realir un programa que lea los sueldos que cobra cada empleado e informe cuantos empleados cobran entre $1.000.000 y $3.000.000 y cuantos cobran más de $3.000.000. 
# Además el programa debe informar el total que gasta la empresa en sueldos al personal. 

# Solicitar la cantidad de empleados
numero_empleados = int(input("Ingrese la cantidad de empleados: "))

#  Inicialiar los contadores y el acumulador
entre_1m_y_3m = 0
mas_de_3m = 0
total_sueldos = 0

#  Usar el bucle white para procesar los sueldos

contador = 0
while contador < numero_empleados:
    sueldo = float(input(f"Ingrese el sueldo del empleado {contador + 1}: "))
    if 1000000 < sueldo <= 3000000:
        entre_1m_y_3m = entre_1m_y_3m + 1 # Incrementa el contador correspondiente
    elif sueldo > 3000000:
        mas_de_3m = mas_de_3m + 1 # Incrementa el contador correspondiente
    
    total_sueldos = total_sueldos + sueldo # Acumular el sueldo al total
    contador = contador + 1
    
#  Mostrar los resultados

print(f"\nEmpleados que cobran entre $1.000.000 y $3.000.000: {entre_1m_y_3m}")
print(f"Empleados que cobran más de $3.000.000: {mas_de_3m}")
print(f"Total gastado en sueldos: {total_sueldos:,.2f}")

# Explicación paso a paso:
# Entrada del número de empleados (numero_empleados):

# Se pide al usuario ingresar cuántos empleados tiene la empresa para establecer el límite del bucle while.
# Inicialización de variables:

# entre_1m_y_3m: Contador para empleados cuyo sueldo está entre $1.000.000 y $3.000.000.
# mas_de_3m: Contador para empleados con sueldos superiores a $3.000.000.
# total_sueldos: Variable acumuladora para sumar todos los sueldos.
# contador: Variable para controlar el número de iteraciones en el bucle.
# Bucle while:

# Mientras contador < n:
# Solicita el sueldo de un empleado.
# Evalúa si el sueldo está en el rango $1.000.000-$3.000.000 o si es mayor a $3.000.000, actualizando los contadores correspondientes.
# Suma el sueldo al total general (total_sueldos).
# Incrementa el contador para procesar el siguiente empleado.
# Salida de resultados:

# Se imprimen los resultados con la cantidad de empleados en cada rango y el total gastado en sueldos.