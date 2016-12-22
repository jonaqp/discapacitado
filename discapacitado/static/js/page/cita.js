$(document).ready(function () {

    $('#id_paciente').select2({
      theme: "bootstrap",
      minimumInputLength: 3
    });




    $('input[name=seleccion_medico]').on('change', function () {
        var parameter = {
            "tipo_medico": $(this).val()
        };
        $.ajax({
            url: "/cita/lista-medico",
            type: "GET",
            cache: false,
            data: parameter,
            success: function (html) {
                $("#load_list_medico").html(html);
                $('#id_disponibilidad').attr("value", "");
                $('body').find("#load_list_medico_disponibilidad").empty();
            }
        });
    });

    $('body').on('click', '.detalle_lista_medico', function () {
        var parameter = {
            "usuario_id": $(this).attr('data-usuario')
        };
        $.ajax({
            url: "/cita/lista-medico-disponibilidad/",
            type: "GET",
            cache: false,
            data: parameter,
            success: function (html) {
                $("#load_list_medico_disponibilidad").html(html);
                $('#id_disponibilidad').attr("value", "")
            }
        });
    });

    $('body').on('change', '.chk_aplica_disponibilidad', function () {
        var disponibilidad_id = $(this).attr('data-disponibilidad');
        $('#id_disponibilidad').attr("value", disponibilidad_id)

    })


})

