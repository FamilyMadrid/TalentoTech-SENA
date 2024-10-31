// Creación de Funciones Matemáticas
// Función Sumar
function suma(a, b) {
  return a + b;
}
console.log(suma());

// Función Restar
function resta(a, b) {
  return a - b;
}
console.log(resta(10, 5));

// Función Multiplicación
function multiplicar(a, b) {
  return a * b;
}
console.log(multiplicar(4, 4));

// Función Dividir
function dividir(a, b) {
  if (b === 0) {
    return "¡ERROR! No se puede dividir por cero";
  }
  return a / b;
}
console.log(dividir(50, 2));

// Implementar un Calculadora Simple

let seguir;
console.log("----------Calculadora----------\n");

do {
  let a = parseFloat(prompt("Introduce el primer número: "));
  let b = parseFloat(prompt("Introduce el segundo número: "));
  let seleccion = prompt(
    "\n--------------\n*Seleccione una opción*\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n\nEscribe: "
  );
  let resultado;
  let operacion;

  // Función Sumar
  function suma(a, b) {
    return a + b;
  }

  // Función Restar
  function resta(a, b) {
    return a - b;
  }

  // Función Multiplicación
  function multiplicar(a, b) {
    return a * b;
  }

  // Función Dividir
  function dividir(a, b) {
    if (b === 0) {
      return "¡ERROR! No se puede dividir por cero";
    }
    return a / b;
  }

  switch (seleccion) {
    case "1":
      resultado = suma(a, b);
      operacion = "+";
      console.log(a, operacion, b, "=", resultado);
      break;
    case "2":
      resultado = resta(a, b);
      operacion = "-";
      console.log(a, operacion, b, "=", resultado);
      break;
    case "3":
      resultado = multiplicar(a, b);
      operacion = "*";
      console.log(a, operacion, b, "=", resultado);
      break;
    case "4":
      resultado = dividir(a, b);
      operacion = "/";
      console.log(a, operacion, b, "=", resultado);
      break;
    default:
      console.log("Operación no válida");
  }
  seguir = prompt("¿Desea continuar? (s/n:");
} while (seguir.toLowerCase() === "s");
