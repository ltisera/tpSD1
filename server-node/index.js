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
const PROTO_PATH_RECIPES = path.resolve(
  __dirname,
  "../grpc-server/proto/receta.proto"
);

const packageDefinitionRecipes = protoLoader.loadSync(PROTO_PATH_RECIPES, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const recipesProto = grpc.loadPackageDefinition(packageDefinitionRecipes);
const recipesGrpcClient = new recipesProto.servicioReceta(
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
app.post("/api/register", (req, res) => {
  const { password, email, name, user } = req.body;
  createUser({ password, email, username: user }, (err, response) => {
    if (err) {
      console.error(err);
      res.redirect("/login");
    } else {
      if (response.mensaje === "Usuario Existente") {
        res.cookie("user", buildAuthCookie(response));
        return res.redirect("/backoffice");
      }
      res.redirect("/login");
    }
  });
});
app.post("/api/login", (req, res) => {
  const { password, email } = req.body;
  loginUser({ password, email }, (err, response) => {
    if (err) {
      console.error(err);
      return res.redirect("/login");
    }
    if (response.mensaje === "INVALIDO") {
      return res.redirect("/login?error=INVALID_CREDENTIALS");
    }
    if (response.mensaje === "NO_EXISTE_EL_USUARIO") {
      return res.redirect("/login?error=USER_NOT_FOUND");
    }
    res.cookie("user", buildAuthCookie(response));
    res.redirect("/backoffice");
  });
});
app.post("/api/recipes", (req, res) => {
  getRecipes(req.body, (error, response) => {
    if (error) {
      res.json([]);
    } else {
      res.json(response);
    }
  });
});
app.post("/api/recipe", (req, res) => {
  createRecipe(req.body, (error, response) => {
    if (error) {
      res.json([]);
    } else {
      res.json(response);
    }
  });
});
app.patch("/api/recipe", (req, res) => {
  editRecipe(req.body, (error, response) => {
    if (error) {
      res.json([]);
    } else {
      res.json(response);
    }
  });
});
app.delete("/api/recipe", (req, res) => {
  deleteRecipe(req.body, (error, response) => {
    if (error) {
      res.json([]);
    } else {
      res.json(response);
    }
  });
});
app.get("/api/favs", (req, res) => {
  const { username } = jwt.decode(req.cookies.user);
  traerRecetasFavoritas(
    {
      usuario: username,
    },
    (error, response) => {
      if (error) {
        res.json([]);
      } else {
        res.json(response);
      }
    }
  );
});
app.patch("/api/favs", (req, res) => {
  const { username } = jwt.decode(req.cookies.user);
  agregarRecetaFavorita(
    {
      idReceta: req.body.idReceta,
      usuario: username,
    },
    (error, response) => {
      if (error) {
        res.json([]);
      } else {
        res.json(response);
      }
    }
  );
});
app.delete("/api/favs", (req, res) => {
  const { username } = jwt.decode(req.cookies.user);
  eliminarRecetaFavorita(
    {
      idReceta: req.body.idReceta,
      usuario: username,
    },
    (error, response) => {
      if (error) {
        res.json([]);
      } else {
        res.json(response);
      }
    }
  );
});
const server = app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

server.on("close", () => {
  console.log("Server closed");
});

// ====== GRPC CLIENT ======
function eliminarRecetaFavorita(
  recipe = {
    idReceta: "",
    usuario: "",
  },
  callback
) {
  recipesGrpcClient.eliminarRecetaDeFavoritos(recipe, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}
function traerRecetasFavoritas(
  request = {
    username: "",
  },
  callback
) {
  recipesGrpcClient.traerRecetasFavoritas(request, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}
function agregarRecetaFavorita(
  recipe = {
    idReceta: "",
  },
  callback
) {
  recipesGrpcClient.agregarRecetaAFavoritos(recipe, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}
function createUser(
  userdata = {
    username: "",
    email: "",
    password: "",
    tipo: "usuario",
  },
  callback
) {
  usersGrpcClient.crearUsuario(userdata, callback);
}
function loginUser(
  userdata = {
    username: "",
    email: "",
    password: "",
    tipo: "",
  },
  callback
) {
  usersGrpcClient.loguearUsuario(userdata, callback);
}
function deleteRecipe(
  recipe = {
    idReceta: "",
  },
  callback
) {
  recipesGrpcClient.eliminarReceta(recipe, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}
function createRecipe(
  recipe = {
    titulo: "",
    descripcion: "",
    tiempoEnMinutos: "",
    categoria: "",
    pasos: "",
    foto1: "",
    foto2: "",
    foto3: "",
    foto4: "",
    foto5: "",
    ingredientes: "",
  },
  callback
) {
  recipesGrpcClient.crearReceta(recipe, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}
function editRecipe(
  recipe = {
    titulo: "",
    descripcion: "",
    tiempoEnMinutos: "",
    categoria: "",
    pasos: "",
    foto1: "",
    foto2: "",
    foto3: "",
    foto4: "",
    foto5: "",
    ingredientes: "",
  },
  callback
) {
  recipesGrpcClient.editarReceta(recipe, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}

function getRecipes(
  filters = {
    tiempoEnMinutosMIN: "",
    tiempoEnMinutosMAX: "",
    categoria: "",
    creador: "",
    titulo: "",
    ingredientes: "",
    idReceta: "",
  },
  callback
) {
  recipesGrpcClient.traerRecetasPor(filters, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
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
