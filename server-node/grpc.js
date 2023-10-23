const path = require("path");
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

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
    usuario: "",
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

function traerUsuariosQueSigo({ usuario = "" }, callback) {
  usersGrpcClient.traerUsuariosQueSigo({ usuario }, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}
function traerUsuariosQueMeSiguen({ usuario = "" }, callback) {
  usersGrpcClient.traerUsuariosQueMeSiguen({ usuario }, (err, response) => {
    callback(err, response);
    if (err) {
      console.error(err);
    } else {
      console.log(response);
    }
  });
}

function seguirUsuario(
  { usuarioQueSigue = "", usuarioSeguido = "" },
  callback
) {
  usersGrpcClient.seguirUsuario(
    { usuarioQueSigue, usuarioSeguido },
    (err, response) => {
      callback(err, response);
      if (err) {
        console.error(err);
      } else {
        console.log(response);
      }
    }
  );
}
function dejarDeSeguirUsuario(
  { usuarioQueSigue = "", usuarioSeguido = "" },
  callback
) {
  usersGrpcClient.dejarDeSeguirUsuario(
    { usuarioQueSigue, usuarioSeguido },
    (err, response) => {
      callback(err, response);
      if (err) {
        console.error(err);
      } else {
        console.log(response);
      }
    }
  );
}

module.exports = {
  getRecipes,
  editRecipe,
  createRecipe,
  deleteRecipe,
  loginUser,
  createUser,
  agregarRecetaFavorita,
  traerRecetasFavoritas,
  eliminarRecetaFavorita,
  traerUsuariosQueSigo,
  seguirUsuario,
  dejarDeSeguirUsuario,
  traerUsuariosQueMeSiguen,
};
