
let url = "https://apis.digital.gob.cl/fl/feriados"
$.get(url, function(respuesta){

   /* respuesta.forEach(function(item) {
        console.log(item)
    });*/
    var hoy = new Date()
    var fecha = Date(hoy.getFullYear()+'-'+(hoy.getMonth()+1)+'-'+hoy.getDate())
    var i = 0

    while (i < 21) {
        feriado = respuesta[respuesta.length - 14 + i]
        if (Date(feriado.fecha) < fecha){
            i = i + 1
        }else {
            i = 22
        }
    }

    $("#feriado").text(feriado.nombre + " - "
    + feriado.fecha)
    
})
