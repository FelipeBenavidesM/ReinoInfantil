
function abrir_modal(url) {
    $('#Modal').load(url, function () {
        $(this).modal('show');
    });
}


function cerrar_modal() {
    $('#Modal').modal('hide');
}


function abrir_modal_alumno(url) {
    $('#Modal').load(url, function () {
        $(this).modal('show');
        modal()
    });
}


function activarBoton() {
    if ($('#boton_creacion').prop('disabled')) {
        $('#boton_creacion').prop('disabled', false);
    } else {
        $('#boton_creacion').prop('disabled', true);
    }
}


function NotificacionError(mensaje) {
    Swal.fire({
        title: 'Error!',
        text: mensaje,
        icon: 'error'
    })
}


function NotificacionSuccess(mensaje) {
    Swal.fire({
        title: 'Buen Trabajo!',
        text: mensaje,
        icon: 'success'
    })
}





