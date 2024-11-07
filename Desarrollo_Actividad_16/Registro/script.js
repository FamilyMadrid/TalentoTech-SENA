function mostrarImagen(event) {
    let imagen = document.getElementById('ver-imagen');
    if (imagen) {
        imagen.src = URL.createObjectURL(event.target.files[0]);
    }
}

document.getElementById('registro-form').addEventListener('submit', function(event){
    event.preventDefault(); // Evita que el formulario se envíe

    let nombre = document.getElementById('nombre').value.trim();
    let correo = document.getElementById('email').value.trim();
    let password = document.getElementById('email').value.trim();
    let imagen = document.getElementById('imagen').files[0];

    if(nombre === '' || correo === '' || password === '') {
        alert('Por favor complete todos los campos obligatorios.');
        return;
    }

    if(imagen && !['image/jpeg', 'image/png'].includes(imagen.type)) {
        alert('Solo se permiten imágenes en formato JPG o PNG.');
        return;
    }

    alert('Formulario enviado exitosamente.');
});