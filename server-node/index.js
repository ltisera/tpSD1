// ======== LIBRERIAS =========
const path = require("path");
const cors = require("cors");
const express = require("express");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const app = express();

// ======== CONFIGURACION =========
const PROTO_PATH_USERS = path.resolve(
  __dirname,
  "../grpc-server/proto/usuario.proto"
);

const packageDefinitionUser = protoLoader.loadSync(PROTO_PATH_USERS, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const userProto = grpc.loadPackageDefinition(packageDefinitionUser);
const usersGrpcClient = new userProto.servicioUsuario(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

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
  const { password, email } = req.body;
  createUser({ password, email }, (err, response) => {
    if (err) {
      res.redirect("/login");
    } else {
      res.cookie("user", buildAuthCookie(response));
      res.redirect("/backoffice");
    }
  });
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

// ====== GRPC CLIENT ======
function createUser(
  userdata = {
    username: "",
    email: "",
    password: "",
    tipo: "",
  },
  callback
) {
  usersGrpcClient.crearUsuario(userdata, callback);
}

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
