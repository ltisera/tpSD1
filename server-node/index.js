// ======== LIBRERIAS =========
const path = require("path");
const cors = require("cors");
const express = require("express");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");
const app = express();

// ======== CONFIGURACION =========
const port = 3000;
const SERVER_JWT_SECRET = "secret1234";
app.use(cors());
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded());
// https://expressjs.com/en/starter/static-files.html
app.use(
  "/backoffice",
  authRequired,
  express.static(path.resolve(__dirname, "../front/backoffice"))
);
app.use(express.static(path.resolve(__dirname, "../front")));

// ======== RUTAS =========
// Pasar datos a python y esperar respuesta
// Si la respuesta es correcta, setear cookie y redirigir a backoffice
// Si la respuesta es incorrecta, redirigir a login
app.post("/api/login", (req, res) => {
  console.log(req.body);
  const serverResponse = true;
  if (serverResponse) {
    res.cookie("user", buildAuthCookie(req.body));
    res.redirect("/backoffice");
  } else {
    res.redirect("/login");
  }
});
app.post("/api/register", (req, res) => {
  console.log(req.body);
  res.redirect("/");
});

const server = app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

server.on("close", () => {
  console.log("Server closed");
});

// ====== MIDDLEWARES ======

function authRequired(req, res, next) {
  if (req.cookies && req.cookies.user) {
    const authCookie = req.cookies.user;
    try {
      jwt.verify(authCookie, SERVER_JWT_SECRET);
      next();
    } catch (err) {
      res.redirect("/login");
    }
  } else {
    res.redirect("/login");
  }
}

// ====== UTILS ======
function buildAuthCookie(user) {
  const payload = {
    id: user.id,
    username: user.username,
    email: user.email,
  };
  const token = jwt.sign(payload, SERVER_JWT_SECRET);
  return token;
}
