// Solicitar al usuario que ingrese la calificación
let calificacion = parseInt(prompt("Ingresa una calificación entre y 100: "));

// Se define la condición
if (calificacion < 0 & calificacion > 100) {
    console.log("Ingrese un valor entre 0 y 100")
} else if(calificacion >= 90) {
    console.log("Aprovado con Honores");
} else if (calificacion >= 70) {
    console.log("Aprobado");
} else {
    console.log("Reprobado")
}
