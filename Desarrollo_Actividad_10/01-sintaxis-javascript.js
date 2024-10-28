// Parte 1: Declaración de Variables y Tipos de Datos

// Declaración de variables
let nombre = "Ivan";
let edad = 39;
let esEstudiante = true;

// Mostrar valores por consola
console.log("El nombre es:", nombre);
// Imprime: El nombre es: Ivan
console.log("La edad es:", edad);
// Imprime: La edad es: 39
console.log("¿Eres estudiante?:", esEstudiante);
// Imprime: Es estudiante: true

// Parte 2: Operaciones Matemáticas y Comparación

// Declara dos variables numéricas
let a = 30;
let b = 20;

// Realiza las operaciones de suma, resta, multiplicación y división entre "a" y "b".
let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;

console.log("La suma de a + b es:", suma); // Imprime: La suma de a + b es: 50
console.log("La resta de a - b es:", resta); // Imprime: La resta de a - b es: 10
console.log("La multiplicación de a * b es:", multiplicacion); // Imprime: La multiplicación de a * b es: 600
console.log("La división de a / b es:", division); // Imprime: La división de a / b es: 1.5

// Compara los valores de "a" y "b", utilizando los operadores "==", "!=", ">", "<" y muestra por consola.

a == b; // Operador de igualdad
a != b; // Operador de desigualdad
a > b; // Operador mayor que
a < b; // Operador menor que

console.log("a == b:", a == b); // Imprime: a == b: false
console.log("a != b:", a != b); // Imprime: a != b: true
console.log("a > b:", a > b); // Imprime: a > b: true
console.log("a < b:", a < b); // Imprime: a < b: false

// Parte 3: Uso de Operadores Lógicos y Concatenación de Strings

// Declara dos variables booleanas "esMayorDeEdad" y "tieneLicencia"
let esMayorDeEdad = true;
let tieneLicencia = false;

// Usa operadores lógicos ("&&", "||") para determinar si una persona puede conducir
console.log("Con el operador lógico 'AND', puede conducir:",esMayorDeEdad && tieneLicencia);
// Imprime: Con el operador lógico 'AND', puede conducir: false
console.log("Con el operador lógico 'OR', puede conducir:",esMayorDeEdad || tieneLicencia);
// Imprime: Con el operador lógico 'OR', puede conducir: true

// Crea un mensaje de bienvenida utilizando concatenación de string y template literals

// Concatenación de Strings
let saludo = "Bienvenidos";
let grupo = "al Bootcamp";
let horario = 7;

console.log(saludo + " " + grupo + " " + "sobre Programación en jornada de" + " " + horario + " " + "am");
// Imprime: Bienvenidos al Bootcamp sobre Programación en jornada de 7 am

// Templates literals

let totalAprendices = 30;
let finalidad = "desarrolladores";

console.log(`El objetivo del Programa es formar ${totalAprendices} aprendices, para que sean excelentes ${finalidad}`);
// Imprime: El objetivo del Programa es formar a 30 aprendices, para que sean excelentes desarrolladores