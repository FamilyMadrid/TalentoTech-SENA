// Ejercicio 1: Verificación de Calificaciones

let calificacion = parseInt(prompt("Ingrese una calificación entre 0 y 100: "));

if (calificacion > 100 || calificacion < 0) {
  console.log("Ingresa un valor del 0 al 100: ");
} else if (calificacion >= 90) {
  console.log("Aprobado con Honores");
} else if (calificacion >= 70) {
  console.log("Aprobado");
} else {
  console.log("Reprobado");
}

// Ejercicio 2: Determinación de número Par o Impar

let numero = parseInt(prompt("Ingrese un número: "));

if (numero % 2 === 0) {
    console.log("El número es Par")
} else {
    console.log("EL número es Impar")
}

// Ejercicio 3: Evaluación de descuentos

let montoTotal = parseInt(prompt("Ingrese el monto total de su compra: "));

if (montoTotal > 100) {
    let descuento = montoTotal * 0.10;
    console.log("EL descuento es de: " + descuento + " dolares");
    let totalPagar = montoTotal - descuento;
    console.log("El total a pagar son: " + totalPagar + " dolares");
} else {
    console.log("Lo sentimos, no es posible aplicar un descuento")
}

// Ejercicio 4: Juego de Adivinanza de Números

let x = Math.floor(Math.random()*10) + 1;
let number = parseInt(prompt("Ingrese un número del 1 al 10: "));

if (number === x) {
    console.log("¡Felicidades, adivinaste el número!")
} else {
    console.log("Lo siento, el número era " + x)
}
