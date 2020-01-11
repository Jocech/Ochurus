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