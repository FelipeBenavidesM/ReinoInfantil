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
            cerrar_modal();
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
            cerrar_modal();
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
            cerrar_modal();
            location.reload('/Educadoras/');
        },
        error: function (error) {
            NotificacionError(error.responseJSON.mensaje);
            activarBoton();
            mostrarError(error);
        }
    });

}

function mostrarError(errores) {
    //input del rut
    $('#inputRut').html("");
    $("#labelRut").remove();
    let errors = "<label id='labelRut' style='color: red'> "

    for (let item in errores.responseJSON.error.rut_teacher) {
        errors += errores.responseJSON.error.rut_teacher[item]
    }
    errores.responseJSON.error.rut_teacher = " "
    errors += "</label>"
    $('#inputRut').after(errors);


    //input del nombre
    $('#inputFirstName').html("");
    $("#labelName").remove();
    let errorsFN = "<label id='labelName' style='color: red'>"
    for (let item in errores.responseJSON.error.first_name_teacher) {
        errorsFN += errores.responseJSON.error.first_name_teacher[item]
    }
    errorsFN += "</label>"
    $('#inputFirstName').after(errorsFN);

    //input del apellido
    $('#inputLastName').html("").next();
    $("#labelLastName").remove();
    let errorsLN = "<label id='labelLastName' style='color: red'>"
    for (let item in errores.responseJSON.error.last_name_teacher) {
        errorsLN += errores.responseJSON.error.last_name_teacher[item]
    }
    errorsLN += "</label>"
    $('#inputLastName').after(errorsLN);

    //input de la direccion
    $('#inputAddress').html("").next();
    $("#labelAddress").remove();
    let errorsD = "<label id='labelAddress' style='color: red'>"
    for (let item in errores.responseJSON.error.address_teacher) {
        errorsD += errores.responseJSON.error.address_teacher[item]
    }
    errorsD += "</label>"
    $('#inputAddress').after(errorsD);

    //input del numero celular
    $('#inputPhoneNumber').html("").next();
    $("#labelPhone").remove();
    let errorsPN = "<label id='labelPhone' style='color: red'>"
    for (let item in errores.responseJSON.error.phone_number_teacher) {
        errorsPN += errores.responseJSON.error.phone_number_teacher[item]
    }
    errorsPN += "</label>"
    $('#inputPhoneNumber').after(errorsPN);

    //input del correo electronico
    $('#inputEmail').html("").next();
    $("#labelEmail").remove();
    let errorsE = "<label id='labelEmail' style='color: red'>"
    for (let item in errores.responseJSON.error.email_teacher) {
        errorsE += errores.responseJSON.error.email_teacher[item]
    }
    errorsE += "</label>"
    $('#inputEmail').after(errorsE);

}