document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("changeTextButton");
  button.addEventListener("click", function () {
    const introSection = document.getElementById("intro");
    introSection.innerHTML =
      "<h1>Texto cambiado</h1><p> Ivan Marid - El texto ha cambiado despues de hacer clic en el botón!!</p>";
  });
});

document.getElementById('button-nav'). addEventListener('click', function(){
    document.querySelector('nav').classList.toggle('nav-open');
})
