$(function () {
  //$("#buscar2").text('SI');
  $("button").click(function(){
    var element = document.body;
    element.classList.toggle("dark-mode");
  });
  
  $('#buscar').change(function (){
    //$("#buscar2").text('SI')
    let value = $(this).val();
    //console.log("Hola")
    //console.log("El codigo es" + value);
    //$("#buscar2").text(value);

    $.ajax({
      type : 'GET',

      url : '/api/pokemon',

      data: {'tipo':value},

      dataType : 'json'
      
      /*success : function(respuesta) {
        $("#buscar2").text("SI");
        $.each(respuesta, function (i, v) {
          $("#buscar2").text(v.id);
        });
        let htmlString = ''
        $.each(respuesta, function (i, v) {
          htmlString += `<tr id="${v.id}"><td> ... </td> ... 
          <td><button onclick="Pulso('${v.id}')">Borrar</button></td> </tr>` 
        });
        //$("#buscar2").text("SI");
      }*/
    }).done(function (respuesta) {
        alert("Operacion exitosa")
        //$("#buscar2").text("SI");
        let htmlString = ''
        $.each(respuesta, function (i, v) {
          htmlString += `<tr id="${v.id}"><th>Nombre: ${v.nombre} </th><th>, Tipo: ${v.tipo} </th> <th>, Numero: ${v.numero} </th><td><button onclick="Pulso('${v.id}')">Borrar</button></td> </tr>`; 
        });
        $("#buscar3").html(htmlString);
      }).fail(function (jqXHR, textStatus) {
        alert("No existe")
      });
  });
});


$(document).ready(function(){
  $("button").click(function(){
    $("#buscar1").text('SI');
  });
});

  
// Click en el botón
function Pulso(value) {
    // Para poner otra vez funciones jQuery en el DOM actual
    $(function () {
      console.log(value);
      //...
      $.ajax({
        type : 'DELETE',
  
        url : '/api/pokemon/'+value,
  
        data: {'id':value},
  
        dataType : 'json'
        
      }).done(function (respuesta) {
          alert("Operacion exitosa");
        }).fail(function (jqXHR, textStatus) {
          alert("No existe");
        });
    });
  
}