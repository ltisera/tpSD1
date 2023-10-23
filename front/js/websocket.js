const ws = new WebSocket("ws://localhost:4004", "ws");
const KAFKA_TOPIC_NEWS = "novedades";
const KAFKA_TOPIC_USER_POPULARITY = "PopularidadUsuario";
const KAFKA_TOPIC_RECIPE_COMMENTS = "RecetaComentarios";
const KAFKA_TOPIC_RECIPE_POPULARITY = "RecetaPopularidad";

ws.onmessage = (obj) => {
  const { message, topic } = JSON.parse(obj.data);
  if (topic === KAFKA_TOPIC_NEWS) {
    new Toastify({
      text: "Nueva receta: " + message.titulo,
      avatar: message.imagen,
      duration: 3000,
      gravity: "top", // `top` or `bottom`
      position: "left", // `left`, `center` or `right`,
      callback: function () {
        location.reload();
      },
    }).showToast();
  }
  if (topic === KAFKA_TOPIC_USER_POPULARITY) {
    console.log(message);
    new Toastify({
      text:
        message.puntaje > 0
          ? `${message.nombre_usuario} ganó un seguidor`
          : `${message.nombre_usuario} perdió un seguidor`,
      duration: 3000,
      gravity: "top", // `top` or `bottom`
      position: "left", // `left`, `center` or `right`,
      callback: function () {},
    }).showToast();
  }
  console.log({ message, topic });
};
