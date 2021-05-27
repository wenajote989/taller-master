/* terminaPor */
$.validator.addMethod("terminaPor", function(value, element, parametro){
    if(value.endsWith(parametro)){
        return true;
    }
    return false;
}, "Debe terminar por {0}")
/* Fin de terminaPor */

/* Formulacioo inciar sesion y registrar */
$("#form_inicio").validate({
    rules: {
        usuario: {
            required: true,
            minlength: 3,
            maxlength: 20
        },
        contra: {
            required: true
        }
    }
})


$("#guardar").click(function() {
    if($("#form_inicio").valid() == false) {
        return;
    }
    let usuario = $("#usuario").val()
    let contra = $("#contra").val()

})

$("#form_registro").validate({
    rules: {
        usuario2: {
            required: true,
            minlength: 3,
            maxlength: 20
        },
        email: {
            required: true,
            email: true,
            terminaPor: ".com"
        },
        password: {
            required: true
        }
    }
})



$("#guardar2").click(function() {
    if($("#form_registro").valid() == false) {
        return;
    }
    let usuario2 = $("#usuario2").val()
    let email = $("#email").val()
    let password = $("#password").val()
    
})
/* Fin de iniciar sesion y registrar */

/* Formulario de solicitud */
$("#form_solicitud").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 10
        },
        apellido: {
            required: true,
            minlength: 3,
            maxlength: 10
        },
        modelo: {
            required: true,
            minlength: 3,
            maxlength: 15
        },
        patente: {
            required: true,
            minlength: 6,
            maxlength: 7
        },
        email: {
            required: true,
            email: true,
            terminaPor: ".com"
        },
    }
})



$("#guardar3").click(function() {
    if($("#form_solicitud").valid() == false) {
        return;
    }
    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let modelo = $("#modelo").val()
    let patente = $("#patente").val()
    let email = $("#email").val()
    
})
/* Fin formulario de solicitud */