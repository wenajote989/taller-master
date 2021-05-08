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


$("#GUARDAR").click(function() {
    if($("#form_inicio").valid() == false) {
        return;
    }
    let usuario = $("#usuario").val()
    let contra = $("#contra").val()

})


$.validator.addMethod("terminaPor", function(value, element, parametro){
    if(value.endsWith(parametro)){
        return true;
    }
    return false;
}, "Debe terminar por {0}")

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