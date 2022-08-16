const fecha_ida = document.getElementById('fecha_ida');
const boton = document.getElementById('boton1');

boton.addEventListener('click', (e) => {
  e.preventDefault();
  if (fecha_ida.value == '') {
    Swal.fire({
      title: 'Error!',
      text: "El campo ida se encuentran vacio",
      icon: 'warning',
      confirmButtonText: 'OK'
    });
  };
});