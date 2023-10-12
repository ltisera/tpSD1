const ws = new WebSocket("ws://localhost:4004", "ws");

ws.onmessage = (obj) => {
  const { message, topic } = JSON.parse(obj.data);
  if (topic === "novedades") {
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
};
