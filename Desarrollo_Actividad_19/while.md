El bucle while en Python se usa para ejecutar un bloque de código repetidamente mientras una condición sea verdadera. Es muy útil para casos en los que no sabes cuántas veces necesitas repetir algo, pero tienes una condición de parada. 

Sintaxis básica de while

```python
Copiar código
while condición:
```
<!-- Código a ejecutar mientras la condición sea verdadera -->

La condición: Se evalúa antes de cada iteración. Si es True, el bloque de código se ejecuta. Si es False, el bucle termina.

Cuidado con los bucles infinitos: Si la condición siempre es True, el bucle no terminará a menos que lo interrumpas manualmente.

Ejemplo básico
Imprimamos números del 1 al 5:

```python
Copiar código
contador = 1
while contador <= 5:  # Mientras el contador sea menor o igual a 5
    print(contador)
    contador += 1  # Incrementamos el contador
Salida:

Copiar código
1
2
3
4
5
```

Ejemplo con entrada de usuario

Un programa que solicita una contraseña hasta que el usuario la escriba correctamente:

```python

contraseña = "python123"
entrada = ""

while entrada != contraseña:
    entrada = input("Introduce la contraseña: ")

print("¡Acceso concedido!")
```

Controlando bucles con break y continue

break: Sale del bucle inmediatamente.
continue: Salta a la siguiente iteración.
Ejemplo con break:

```python

while True:  # Bucle infinito
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada == "salir":
        break  # Salimos del bucle
print("Bucle terminado.")
```

Ejemplo con continue:

```python
Copiar código
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Saltamos la iteración cuando contador es 3
    print(contador)
Salida:

Copiar código
1
2
4
5
```

Práctica

Crea un bucle que sume números hasta que el usuario escriba "0".

Crea un bucle que genere una tabla de multiplicar hasta que el usuario quiera salir. -->