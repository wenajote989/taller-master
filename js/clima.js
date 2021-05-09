/*
let url = "http://api.openweathermap.org/data/2.5/weather?id=3868121&appid=929f19ec80ed2044abebf443944a9530"

$.get(url, function(respuesta){
let clima = console.log(respuesta)



}, "json")

$("#clima").text(clima.name)
*/
/*JQUERY PARA IMPLEMENTAR LA API JQUERY PARA IMPLEMENTAR LA API*/
    $(document).ready(function(){
        $("#enviar").click(function(){
            let url = "http://api.openweathermap.org/data/2.5/weather?id=3868121&appid=929f19ec80ed2044abebf443944a9530"
            $.get(url, function(respuesta){
                $.each(respuesta.base, function(i, items){
                    $("#categorias").append("<tr><td>"+item.temp + 
                        "</td><td>"+item.temp_max +  
                            "</td><td>"+item.temp_min + "</td></tr>");
                });
            });
        });
    }, "json")


/* esto dio en el resultado de ARC
{
"coord": {
"lon": -71.5518,
"lat": -33.0246
},
"weather": [
  {
"id": 800,
"main": "Clear",
"description": "clear sky",
"icon": "01d"
}
],
"base": "stations",
"main": {
"temp": 291.64,
"feels_like": 290.98,
"temp_min": 289.26,
"temp_max": 294.15,
"pressure": 1018,
"humidity": 55
},
"visibility": 10000,
"wind": {
"speed": 5.14,
"deg": 190
},
"clouds": {
"all": 0
},
"dt": 1620586944,
"sys": {
"type": 1,
"id": 8498,
"country": "CL",
"sunrise": 1620559538,
"sunset": 1620597581
},
"timezone": -14400,
"id": 3868121,
"name": "Viña del Mar",
"cod": 200
}

*/




