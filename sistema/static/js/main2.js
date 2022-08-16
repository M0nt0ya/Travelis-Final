const container = document.querySelector('.contenedor');
const tabla = document.querySelector('.tabla-trayecto1');
const datos = document.querySelectorAll('.row .cont-trayecto1');

container.addEventListener('click', (e) => {
  if (e.target.classList.contains('tabla-trayecto1')) {
    !e.target.classList.toggle('seleccionado');
  }
});
