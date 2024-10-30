// Solución: Ejercicio 1

let calificacion = parseInt(prompt("Ingrese su calificación entre 0 y 100: "));

if (calificacion >= 90 && calificacion <= 100) {
  console.log("¡Felicidades!, Tu calificación es Excelente");
} else if (calificacion >= 80 && calificacion <= 89) {
  console.log("¡Felicidades!, Tu calificación es Buena");
} else if (calificacion >= 70 && calificacion <= 79) {
  console.log(
    "Tu calificación es Aceptable, esfuerzate un poco más, puedes hacerlo mejor"
  );
} else if (calificacion >= 60 && calificacion <= 69) {
  console.log(
    "Tu calificación es Insuficiente, debes volver a repasar el contenido"
  );
} else if (calificacion <= 59) {
  console.log(
    "Tu calificación es deficiente, tienes que tomar clases para reforzas la deficiencias"
  );
}

// Solución: Ejercicio 2

let años = parseInt(prompt("Ingrese su edad: "));

if (años < 12) {
  console.log("Eres un niño/a");
} else if (años >= 12 && años <= 17) {
  console.log("Eres adolescente");
} else if (años >= 18 && años <= 65) {
  console.log("Ers un Adulto");
  if (años >= 18 && años <= 25) {
    console.log("Tambien eres un Adulto Joven");
  }
} else if (años >= 65) console.log("Eres Adulto Mayor");

// Solucion: Ejercicio 3

let salario = Number.parseFloat(prompt("Ingrese su salario mensual: "));

if (salario < 1300000) {
  console.log("No se aplica impuesto a tu salario");
} else if (salario >= 1300000 && salario <= 2500000) {
  let descuento = salario * 0.1;
  let descuentoAplicado = salario - descuento;
  console.log("Tu descuento es: " + new Intl.NumberFormat().format(descuento));
  console.log(
    "Tu salario Final es: " + new Intl.NumberFormat().format(descuentoAplicado)
  );
} else if (salario > 2500000) {
  let descuento = salario * 0.2;
  let descuentoAplicado = salario - descuento;
  console.log("Tu descuento es: " + new Intl.NumberFormat().format(descuento));
  console.log(
    "Tu salario Final es: " + new Intl.NumberFormat().format(descuentoAplicado)
  );
}

// Solución: Ejercicio 4

console.log("Tienes 5 intentos para adivinar el número");
let numeroAleatorio = Math.floor(Math.random() * 50);
let intentosRealizados = 0;

while (intentosRealizados < 5) {
  let numeroIngresado = parseInt(prompt("Adivina el número (entre 1 y 50): "));
  intentosRealizados++;
  if (numeroIngresado > numeroAleatorio) {
    console.log("El número es menor");
  } else if (numeroIngresado < numeroAleatorio) {
    console.log("El número es mayor");
  } else if (numeroIngresado === numeroAleatorio) {
    console.log(
      `¡Felicidades, adivinaste el número en ${intentosRealizados} intentos realizados`
    );
    break;
  }
}
console.log(`¡Lo siento, el número era ${numeroAleatorio}`);
