const container = document.querySelector('.tabla-bus');
const asientos = document.querySelectorAll('.row .imgVacia:not(.ocupado)');
const costo = document.getElementById('costo');

function costoAsientosSeleccionados() {
  const asientosSeleccionados = document.querySelectorAll('.row .imgVacia.seleccionado');
  const totalAsientosSeleccionados = asientosSeleccionados.length;
  costo.innerText = totalAsientosSeleccionados * 10;
}

container.addEventListener('click', (e) => {
  if (e.target.classList.contains('imgVacia') && !e.target.classList.contains('ocupado')) {
    !e.target.classList.toggle('seleccionado');
  }
  costoAsientosSeleccionados();
});
