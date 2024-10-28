// Solicitar al usuario monto total de su compra

let montoTotal = parseInt(prompt("Ingrese el monto total de su compra: "));

if (montoTotal > 100){
    let descuento = (montoTotal * 0.1).toFixed(1);
    console.log("EL descuento es: ", descuento);
    let montoTotalDescuento = montoTotal - descuento;
    console.log("El monto total menos el descuento es: ",  montoTotalDescuento.toFixed(1))
} else {
    console.log("No es posible aplicarle un descuento");
}
