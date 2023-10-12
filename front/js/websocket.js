const ws = new WebSocket("ws://localhost:4004", "ws");

ws.onmessage = (message) => {
  console.log(message.data);
};
