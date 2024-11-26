#Operadores con conjuntos

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {1, 2, 3, 4}
D = {3, 4, 5, 6}

interseccion = A & B
diferencia = A - B
diferencia_2 = B - A
diferencia_simetrica = A ^ B
igualdad = A == C
C.add(5)
C.update([4, 1, 6, 7, 8])
C.remove(5)
C.pop()

print(f"La intersección de A y B {interseccion}")
print(f"La diferencia de A y B {diferencia}")
print(f"La diferencia de B y A {diferencia_2}")
print(f"La diferencia simétrica de A y B {diferencia_simetrica}")
print(f"El conjunto A es igual al C?: {igualdad}")
print(f"El conjunto C contiene: {C}")
print(f"El conjunto D contiene: {D}")
print(f"El conjunto C contiene: {C}")
print(C.pop())
print(f"El conjunto C contiene: {C}")
