// Ejercicio 1

const numeros = [10, 7, 14, 21];
let sumaTotal = 0;

for (let i = 0; i < numeros.length; i++) {
    sumaTotal += numeros[i];
}

let promedio = sumaTotal / numeros.length;

console.log("Tamaño del Array: ", numeros.length);
console.log("Números dentro del Array: ", numeros);
console.log("La suma total es: ", sumaTotal);
console.log("El promedio es: ", promedio);

// Ejercicio 2

let numero = parseFloat(prompt("Ingrese un número, si quiere parar ingrese un número negativo: "));

while (numero >= 0) {
    numero = parseFloat(prompt("Ingrese otro número, si quiere parar ingrese un número negativo: "));
}

console.log("Terminaste Ingresaste un número negativo para salir");

// Ejercicio 3

let contraseñaCorrecta = "maria123";
let contraseñaIngresada;

do {
    contraseñaIngresada = prompt("Ingresa una contraseña: ");
    if (contraseñaIngresada !== contraseñaCorrecta) {
        console.log("La contraseña ingresada es incorrecta, intenta nuevamente");
    }
} while (contraseñaIngresada !== contraseñaCorrecta);

console.log("Contraseña correcta, Acceso libre");

