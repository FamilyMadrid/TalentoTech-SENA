Ejercicio 1: Imprimir números en un rango
Escribe un programa que imprima los números del 1 al 10 usando un bucle for.

```python
Copiar código
for i in range(1, 11):  # El rango va desde 1 hasta 10 (sin incluir el 11)
    print(i)
```

Ejercicio 2: Sumar números en un rango
Escribe un programa que sume todos los números del 1 al 100 e imprima el resultado.

```python
Copiar código
suma = 0
for i in range(1, 101):  # El rango incluye desde 1 hasta 100
    suma += i
print(f"La suma de los números del 1 al 100 es: {suma}")
```

Ejercicio 3: Imprimir los caracteres de un string
Escribe un programa que recorra la palabra "Python" e imprima cada carácter en una línea diferente.

```python
Copiar código
palabra = "Python"
for letra in palabra:
    print(letra)
```

Ejercicio 4: Números pares
Escribe un programa que imprima todos los números pares entre 1 y 20.

```python
Copiar código
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

Ejercicio 5: Tabla de multiplicar
Escribe un programa que solicite un número al usuario e imprima su tabla de multiplicar del 1 al 10.

```python
Copiar código
numero = int(input("Ingrese un número para calcular su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```

Ejercicio 6: Contar vocales en una frase
Escribe un programa que cuente cuántas vocales tiene una frase ingresada por el usuario.

```python
Copiar código
frase = input("Ingrese una frase: ").lower()
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print(f"La frase tiene {contador} vocales.")
```

Ejercicio 7: Imprimir una lista de elementos
Escribe un programa que recorra una lista de frutas e imprima cada una.

```python
Copiar código
frutas = ["manzana", "plátano", "cereza", "naranja"]
for fruta in frutas:
    print(fruta)
```

Ejercicio 8: Cálculo de cuadrados
Escribe un programa que imprima los cuadrados de los números del 1 al 10.

```python
Copiar código
for i in range(1, 11):
    print(f"El cuadrado de {i} es {i ** 2}")
```

Ejercicio 9: Filtrar números mayores
Dada una lista de números, imprime solo aquellos que sean mayores a 5.

```python
Copiar código
numeros = [1, 3, 5, 7, 9, 11]
for numero in numeros:
    if numero > 5:
        print(numero)
```

Ejercicio 10: Imprimir índices y valores
Escribe un programa que recorra una lista e imprima el índice y el valor de cada elemento.

```python
Copiar código
colores = ["rojo", "azul", "verde", "amarillo"]
for indice, color in enumerate(colores):
    print(f"Índice: {indice}, Color: {color}")
```

Consejos:
Experimenta cambiando los rangos y condiciones en los ejercicios.
Si necesitas explicaciones más detalladas sobre alguno de estos ejercicios o tienes dudas, ¡puedes preguntarme! 😊