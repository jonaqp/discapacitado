$(document).ready(function () {

  $("#id_paciente").select2({
    ajax: {
      url: "/api/v1/paciente/lista/",
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



});
