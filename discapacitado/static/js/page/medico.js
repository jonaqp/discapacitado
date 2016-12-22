$(document).ready(function () {
    "use strict";

    $('.select_ciex').select2({
        ajax: {
            url: "/api/v1/catalogo/cie/lista_json/",
            dataType: 'json',
            delay: 500,
            data: function (params) {
                return {
                    q: params.term, // search term
                    page: params.page
                };
            },
            processResults: function (data, params) {
                params.page = params.page || 1;
                return {
                    results: data,
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },
        theme: "bootstrap",
        minimumInputLength: 3
    });

    $('.select_renaes').select2({
        ajax: {
            url: "/api/v1/establecimiento/lista_json/",
            dataType: 'json',
            delay: 500,
            data: function (params) {
                return {
                    q: params.term, // search term
                    page: params.page
                };
            },
            processResults: function (data, params) {
                params.page = params.page || 1;
                return {
                    results: data,
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },
        theme: "bootstrap",
        minimumInputLength: 3
    });


    $('.select_discapacidad').select2({
        ajax: {
            url: "/api/v1/catalogo/cie/lista_json/",
            dataType: 'json',
            delay: 500,
            data: function (params) {
                return {
                    q: params.term, // search term
                    page: params.page
                };
            },
            processResults: function (data, params) {
                params.page = params.page || 1;
                return {
                    results: data,
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },
        theme: "bootstrap",
        minimumInputLength: 3
    });


    $('.select_deficiencia').select2({
        ajax: {
            url: "/api/v1/catalogo/deficiencia/lista_json/",
            dataType: 'json',
            delay: 500,
            data: function (params) {
                return {
                    q: params.term, // search term
                    page: params.page
                };
            },
            processResults: function (data, params) {
                params.page = params.page || 1;
                return {
                    results: data,
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },
        theme: "bootstrap",
        minimumInputLength: 3
    });
    $('.select_cpt').select2({
        ajax: {
            url: "/api/v1/catalogo/procedimiento/lista_json/",
            dataType: 'json',
            delay: 500,
            data: function (params) {
                return {
                    q: params.term, // search term
                    page: params.page
                };
            },
            processResults: function (data, params) {
                params.page = params.page || 1;
                return {
                    results: data,
                    pagination: {
                        more: (params.page * 30) < data.total_count
                    }
                };
            },
            cache: true
        },
        theme: "bootstrap",
        minimumInputLength: 3
    });


    $("#id_referencia_establecimiento").on('change', function () {
        var _this = $(this).val();
        if (_this != '01') {
            $("#id_establecimiento_servicio").prop("disabled", false);
        } else {
            $("#id_establecimiento_servicio").prop("disabled", true);
            $(".select_renaes").html("");
        }
        return false;
    })


/***********************VALIDACION FORMSET*******************************/

    var $btn_select_ciex = $('#btn-select-ciex');
    var $select_ciex = $('#id_ciex_form_select');
    $btn_select_ciex.on('click', function () {
        if ($select_ciex.val()) {
            addToFormset(
                '#tbody-ciex-formset-parent', '#tbody-ciex-formset-empty', 'paciente_pacienteciex_paciente_consulta', function (node) {
                    node.find('input.cls_codigo_ciex').val($select_ciex.val());
                    node.find('input.cls_descripcion_ciex').val($select_ciex.find(':selected').text());
                    $select_ciex.val('');
                });
        }
    });

    var $btn_select_discapacidad = $('#btn-select-discapacidad');
    var $select_discapacidad = $('#id_discapacidad_form_select');
    $btn_select_discapacidad.on('click', function () {
        if ($select_discapacidad.val()) {
            addToFormset(
                '#tbody-discapacidad-formset-parent', '#tbody-discapacidad-formset-empty', 'paciente_pacientediscapacidad_paciente_consulta', function (node) {
                    node.find('input.cls_codigo_discapacidad').val($select_discapacidad.val());
                    node.find('input.cls_descripcion_discapacidad').val($select_discapacidad.find(':selected').text());
                    $select_discapacidad.val('');
                });
        }
    });

    var $btn_select_deficiencia = $('#btn-select-deficiencia');
    var $select_deficiencia = $('#id_deficiencia_form_select');
    $btn_select_deficiencia.on('click', function () {
        if ($select_deficiencia.val()) {
            addToFormset(
                '#tbody-deficiencia-formset-parent', '#tbody-deficiencia-formset-empty', 'paciente_pacientedeficiencia_paciente_consulta', function (node) {
                    node.find('input.cls_codigo_deficiencia').val($select_deficiencia.val());
                    node.find('input.cls_descripcion_deficiencia').val($select_deficiencia.find(':selected').text());
                    $select_deficiencia.val('');
                });
        }
    });

    var $btn_select_cif = $('#btn-select-cif');
    var $select_cif = $('#id_cif_form_select');
    $btn_select_cif.on('click', function () {
        if ($select_cif.val()) {
            addToFormset(
                '#tbody-cif-formset-parent', '#tbody-cif-formset-empty', 'paciente_pacientecif_paciente_consulta', function (node) {
                    node.find('input.cls_codigo_cif').val($select_cif.val());
                    node.find('input.cls_descripcion_cif').val($select_cif.find(':selected').text());
                    $select_cif.val('');
                });
        }
    });

    var $btn_select_cpt = $('#btn-select-cpt');
    var $select_cpt = $('#id_cpt_form_select');
    $btn_select_cpt.on('click', function () {
        if ($select_cpt.val()) {
            addToFormset(
                '#tbody-cpt-formset-parent', '#tbody-cpt-formset-empty', 'paciente_pacienteprocedimiento_paciente_consulta', function (node) {
                    node.find('input.cls_codigo_cpt').val($select_cpt.val());
                    node.find('input.cls_descripcion_cpt').val($select_cpt.find(':selected').text());
                    $select_cpt.val('');
                });
        }
    });


});