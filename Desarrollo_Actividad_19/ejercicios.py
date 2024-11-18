puntos = int(input("Cuantos puntos deseea procesar: "))

primer_cuadrante = 0
segundo_cuadrante = 0
tercero_cuadrante = 0
cuarto_cuadrante = 0
i = 0

for i in range(puntos):
    print(f"\nPunto {i + 1}")
x = float(int("Ingresa la coordenada x: "))
y = float(int("Ingresa la coordenada y: "))

if x > 0 and y > 0:
    primer_cuadrante += 1
elif x < 0 and y > 0:
    segundo_cuadrante += 1
elif x < 0 and y < 0:
    tercero_cuadrante += 1
elif x > 0 and y < 0:
    cuarto_cuadrante += 1
else:
    print("El punto esta en el eje 0 o en el origen, no pertenece a ningún cuadrante")

print(f"\nResultados")
print(f"\nPuntos del primer cuadrante: {primer_cuadrante}")
print(f"\nPuntos del segundo cuadrante: {segundo_cuadrante}")
print(f"\nPuntos del tercero cuadrante: {tercero_cuadrante}")
print(f"\nPuntos del cuarto cuadrante: {cuarto_cuadrante}")



