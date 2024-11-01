const prompt = require("prompt-sync")();

// Ejercicio 1

let calificacion = parseInt(prompt("INgrese una calificación de 1 a 5, donde 1 es muy malo y 5 es Excelente: "));

switch (calificacion) {
    case 1:
        console.log("Evaluaste el producto como muy Malo");
        break;
    case 2:
        console.log("Evaluaste el producto como Malo");
        break;
    case 3:
        console.log("Evaluaste el producto como regular");
        break;
    case 4:
        console.log("Evaluaste el producto como Bueno");
        break;
    case 5:
        console.log("Evaluaste el producto como Excelente");
        break;
    default:
        console.log("Calificación no valida, Ingresa una calificación entre 1 y 5");
}

// Ejercicio 2

let letra = prompt("Ingresa una calificación de letra (A, B, C, D, F): ");
letra = letra.toLowerCase();

switch (letra) {
  case "a":
    console.log("La letra A, representa Excelente");
    break;
  case "b":
    console.log("La letra B, representa Bueno");
    break;
  case "c":
    console.log("La letra C, representa Regular");
    break;
  case "d":
    console.log("La letra D, representa Deficiente");
    break;
  case "f":
    console.log("La letra F, representa Reprobado");
    break;

  default:
    console.log("Calificación no valida, Ingrese (A, B, C, D o F) ");
}

// Ejercicio 3

let valor = parseFloat(prompt("Ingrese el valor en pesos ($) a convertir: "));
let opcion = parseInt(prompt("Escoja la moneda a la cual desea convertirla: \n1.Dolar\n2.Euro\n3.Libras Esterlinas\n\nEscribe tu opción: "));

switch(opcion) {
    case 1: 
    let dolar = (valor / 4300).toFixed(1);
    console.log("El valor es: " + dolar + " dolares");
    break;
    case 2: 
    let euro = (valor / 4808).toFixed(1);
    console.log("El valor es: " + euro + " euros");
    break;
    case 3: 
    let esterlina = (valor / 5700).toFixed(1);
    console.log("El valor es: " + esterlina + " libras esterlinas");
    break;
    default:
        console.log("Ingrese una opción de 1 a 3");
}