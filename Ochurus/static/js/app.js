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
        password: {
            required: true,
            minlength: 8,
            maxlength: 16
        },
        first_name: {
            required: true,

        },
        last_name: {
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
        password: {
            required: "Este campo no puede estar vacio",
            minlength: 8,
            maxlength: 16
        },
        first_name: {
            required: "Este campo no puede estar vacio",
        },
        last_name: {
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
$("#formularioRegCampeon").validate({
    errorClass: 'is-invalid',
    rules: {
        nombre: {
            required: true,
        },
        rol: {
            required: true,
        },
        popularidad: {
            required: true,
            maxlength: 2
        },
        porcentaje_victorias: {
            required: true,
            maxlength: 2
        },
        porcentaje_derrotas: {
            required: true,
            maxlength: 2
        }
    },
    messages: {
        nombre: {
            required: "Este campo no puede estar vacio"
        },
        rol: {
            required: "Este campo no puede estar vacio"
        },
        popularidad: {
            required: "Este campo no puede estar vacio",
            maxlength: "Debe tener maximo 2 digitos"
        },
        porcentaje_victorias: {
            required: "Este campo no puede estar vacio",
            maxlength: "Debe tener maximo 2 digitos"
        },
        porcentaje_derrotas: {
            required: "Este campo no puede estar vacio",
            maxlength: "Debe tener maximo 2 digitos"
        }
    }
})
$("#formularioRegistrarStaff").validate({
    errorClass: 'is-invalid',
    rules: {
        username: {
            required: true,
            maxlength: 25,
            minlength: 3
        },
        email: {
            required: true,
            email: true
        },
        password: {
            required: true,
            minlength: 8,
            maxlength: 16
        },
        first_name: {
            required: true,

        },
        last_name: {
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
        username: {
            required: "Este campo no puede estar vacio",
            minlength: "Debe contener al menos 3 carácteres",
            maxlength: "No puede ser de mas de 25 carácteres"
        },
        email: {
            required: "Este campo no puede estar vacio",
            email: "Debe ser en formato de email"
        },
        password: {
            required: "Este campo no puede estar vacio",
            minlength: 8,
            maxlength: 16
        },
        first_name: {
            required: "Este campo no puede estar vacio",
        },
        last_name: {
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

