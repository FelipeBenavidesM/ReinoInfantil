
function registrar() {
    activarBoton()
    $.ajax({
        data: $('#create_form').serialize(),
        url: $('#create_form').attr('action'),
        type: $('#create_form').attr('method'),
        success: function (response) {
            NotificacionSuccess(response.mensaje);
            location.reload('/Educadoras/');
            cerrar_modal_profesor();
        },
        error: function (error) {
            NotificacionError(error.responseJSON.mensaje);
            mostrarError(error);
            activarBoton();
        }
    });
}

