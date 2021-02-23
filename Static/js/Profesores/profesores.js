function option(pk) {
    if (pk) {
        editar(pk);
    } else {
        registrar();
    }
}

function registrar() {
    activarBoton()

    $.ajax({
        data: $('#create_form').serialize(),
        url: '/Educadoras/Create/',
        type: $('#create_form').attr('method'),
        success: function (response) {
            NotificacionSuccess(response.mensaje);
            cerrar_modal_profesor();
            location.reload('/Educadoras/');
        },
        error: function (error) {
            NotificacionError(error.responseJSON.mensaje);
            mostrarError(error);
            activarBoton();
        }
    });
}

function eliminar(pk) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/Educadoras/Delete/' + pk,
        type: 'post',
        success: function (response) {
            NotificacionSuccess(response.mensaje);
            cerrar_modal_profesor();
            location.reload('/Educadoras/');
        },
        error: function (error) {
            NotificacionError(error.mensaje);
        }
    });
}

function editar(pk) {
    activarBoton()
    $.ajax({
        data: $('#create_form').serialize(),
        url: '/Educadoras/Update/' + pk + '/',
        type: $('#create_form').attr('method'),
        success: function (response) {
            NotificacionSuccess(response.mensaje);
            cerrar_modal_profesor();
            location.reload('/Educadoras/');
        },
        error: function (error) {
            NotificacionError(error.responseJSON.mensaje);
            mostrarError(error);
            activarBoton();
        }
    });

}