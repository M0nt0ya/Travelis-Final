function openImgPer(){
    var image = document.getElementById('image');
    var source = image.src;
    window.open(source);
}

function openImgPort(){
    var image = document.getElementById('imagen-portada');
    var source = image.src;
    window.open(source);
}

function validarImagen() {
    var cambio_img = document.getElementById('cambio-img');

    if (cambio_img.files && cambio_img.files[0]) {
        var visor = new FileReader();
        visor.onload = function(e){
            document.getElementById('Imagen-perfil').innerHTML = '<img src="' + e.target.result + '" style="width: 166px; height: 166px; position: relative; border-radius: 50%; box-shadow: 0 0 6px 0 #719af1; margin-top: 6px;" id="image" onclick="openImgPer()">';
        };
        visor.readAsDataURL(cambio_img.files[0])
    };
};

function validarImagenPort() {
    var cambio_img_port = document.getElementById('cambio-img-port');

    if (cambio_img_port.files && cambio_img_port.files[0]) {
        var visorPor = new FileReader();
        visorPor.onload = function(e){
        document.getElementById('div-imagen-portada').innerHTML = '<img src="' + e.target.result + '" style="display: block; position: relative; width: 100%; height: 13.5rem; background-image: linear-gradient(45deg, #BC3CFF, #317FFF); border-radius: 0 0 20px 20px; background-repeat: no-repeat; background-position: center; background-size: cover;" id="imagen-portada" onclick="openImgPort()">';
        };
        visorPor.readAsDataURL(cambio_img_port.files[0])
    };
};