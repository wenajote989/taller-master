
let url = "https://apis.digital.gob.cl/fl/feriados"
$.get(url, function(respuesta){

   /* respuesta.forEach(function(item) {
        console.log(item)
    });*/
    let feriado = respuesta[respuesta.length -15]
    

    $("#feriado").text(feriado.nombre + " - "
    + feriado.fecha)
    
})
