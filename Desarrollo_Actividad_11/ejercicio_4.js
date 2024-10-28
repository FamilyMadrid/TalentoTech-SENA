// Solicitar al usua// General un número aleatorio entre 1 y 10
let numeroAleatorio = Math.floor(Math.random()*10) + 1;

// Solicitar al usuario que adivine el número
let adivinanza = parseInt(prompt("Adivina el número (entre 1 y 10):"));

// Verificar si la adivinanza es correcta
if (adivinanza === numeroAleatorio) {
    console.log("¡Felicidades, adivinaste el número!");
} else {
    console.log("Lo siento, el número era " + numeroAleatorio);
}