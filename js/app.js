$("#formularioIndex").validate({
    errorClass: "is-invalid",
    rules: {
        email: {
            required: true,
            email: true
        },
        contrasena: {
            required: true,
            minlength: 8,
            maxlength: 16
        }
    },
    messages: {
        email: {
            required: "Este campo no puede estar vacio",
            email: "Este campo debe ser en formato email"
        },
        contrasena: {
            required: "Este campo no puede estar vacio",
            minlength: "Debe ser mayor a 8 caracteres",
            maxlength: "Debe ser menor a 16 caracteres"
        }
    }
})
$("#formularioRegistrar").validate({
    errorClass: 'is-invalid',
    rules: {
        email: {
            required: true,
            email: true
        },
        contrasena: {
            required: true,
            minlength: 8,
            maxlength: 16
        },
        nombre: {
            required: true,

        },
        apellido: {
            required: true,
        },
        ciudad: {
            required: true,
            minlength: 8,
            maxlength: 16
        },
        telefono: {
            required: true,
            minlength: 9
        }

    },
    messages: {
        email: {
            required: "Este campo no puede estar vacio",
            email: "Debe ser en formato de email"
        },
        contraseña: {
            required: "Este campo no puede estar vacio",
            minlength: 8,
            maxlength: 16
        },
        nombre: {
            required: "Este campo no puede estar vacio",
        },
        apellido: {
            required: "Este campo no puede estar vacio"

        },
        ciudad: {
            required: "Este campo no puede estar vacio"

        },
        telefono: {
            required: "Este campo no puede estar vacio",
            minlength: "Debe tener un minimo de 9 caracteres"
        }

    }
})
$(".correcto").click(function () {
    swal("Perfecto!");
});
$(".incorrecto").click(function () {
    swal("Mal!");
});
