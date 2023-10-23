// ======== LIBRERIAS =========
const path = require("path");
const cors = require("cors");
const express = require("express");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");

const { Kafka } = require("kafkajs");
const { WebSocketServer } = require("ws");
const {
  agregarRecetaFavorita,
  createRecipe,
  createUser,
  deleteRecipe,
  editRecipe,
  eliminarRecetaFavorita,
  getRecipes,
  loginUser,
  traerRecetasFavoritas,
  seguirUsuario,
  traerUsuariosQueSigo,
  dejarDeSeguirUsuario,
} = require("./grpc");
const app = express();

// ======== CONFIGURACION =========
const kafka = new Kafka({
  brokers: [`0.0.0.0:9092`],
  clientId: "node-js",
});
const kafkaProducer = kafka.producer();
const kafkaConsumer = kafka.consumer({ groupId: "node-js" });
const KAFKA_TOPIC_NEWS = "novedades";

const wss = new WebSocketServer({
  port: 4004,
});

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
      const { username } = jwt.decode(req.cookies.user);
      traerRecetasFavoritas(
        {
          usuario: username,
        },
        (err, favRecipesResponse) => {
          res.json({
            recetas: response.recetas.map((recipe) => {
              return {
                ...recipe,
                isFav: favRecipesResponse.recetas.some(
                  (fav) => fav.idReceta === recipe.idReceta
                ),
              };
            }),
          });
        }
      );
    }
  });
});
app.post("/api/recipe", (req, res) => {
  const { username } = jwt.decode(req.cookies.user);
  if (!username) {
    return res.json([]);
  }
  createRecipe(req.body, (error, response) => {
    if (error) {
      res.json([]);
    } else {
      kafkaProducer.send({
        topic: KAFKA_TOPIC_NEWS,
        messages: [
          {
            value: JSON.stringify({
              usuario: username,
              titulo: req.body.titulo,
              imagen: req.body.foto1,
            }),
          },
        ],
      });
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
  if (!username) {
    return res.json([]);
  }
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

app.post("/api/follow", (req, res) => {
  const { username } = jwt.decode(req.cookies.user);
  seguirUsuario(
    {
      usuarioQueSigue: username,
      usuarioSeguido: req.body.usuarioSeguido,
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
app.delete("/api/follow", (req, res) => {
  const { username } = jwt.decode(req.cookies.user);
  dejarDeSeguirUsuario(
    {
      usuarioQueSigue: username,
      usuarioSeguido: req.body.usuarioSeguido,
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

app.get("/api/follow", (req, res) => {
  const { username } = jwt.decode(req.cookies.user);
  traerUsuariosQueSigo(
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

// ================
let connections = [];

const server = app.listen(port, async () => {
  console.log(`Example app listening on port ${port}`);
  await kafkaProducer.connect();
  await kafkaConsumer.connect();
  await kafkaConsumer.subscribe({
    topic: KAFKA_TOPIC_NEWS,
    fromBeginning: true,
  });
  wss.on("connection", async (ws) => {
    connections.push(ws);
  });
  await kafkaConsumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      connections = connections.filter((ws) => ws.OPEN);
      connections.forEach((ws) => {
        ws.send(
          JSON.stringify({
            topic,
            message: JSON.parse(message.value.toString()),
          })
        );
      });
    },
  });
});

server.on("close", async () => {
  connections.forEach((ws) => ws.close());
  await kafkaProducer.disconnect();
  await kafkaConsumer.disconnect();
  wss.close();
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
