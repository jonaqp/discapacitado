$(document).ready(function () {

    $("#id_financiador").on('change', function () {
        var options = $(this).val();
        if (options != '02') {
            $("#id_componente_filiacion").attr("disabled", true);
            $("#id_codigo_componente_filiacion").attr("disabled", true);
        }else{
            $("#id_componente_filiacion").attr("disabled", false);
            $("#id_codigo_componente_filiacion").attr("disabled", false);
        }
    })


});
