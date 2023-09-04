var http = require("http");
const fs =require('fs');

/// variables para despachar los html
const paginaInicio = fs.readFileSync("cliente/index.html");
const paginaRecetas = fs.readFileSync("cliente/recetas.html");


var manejador = function (solicitud, respuesta){
    console.log("Ruta accedida:", solicitud.url);
    if(solicitud.url ==='/'){
        console.log("servi index");
        respuesta.end(paginaInicio);
    }else if(solicitud.url ==='/recetas'){
        console.log("MANDAME LA RECE");
        respuesta.end(paginaRecetas);
    }else{
        respuesta.writeHead(404);
        respuesta.end("Page not found");
    }

};

var servidor = http.createServer(manejador);

servidor.listen(8080);
