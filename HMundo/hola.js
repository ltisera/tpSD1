var http = require("http");

var manejador = function (solicitud, respuesta){
    console.log("Recibi peti");
    respuesta.end("Hola mundo");
};

var servidor = http.createServer(manejador);

servidor.listen(8080);
