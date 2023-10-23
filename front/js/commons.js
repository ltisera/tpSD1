function readAuthUserInfo(name = "") {
  var result = document.cookie.match(new RegExp(name + "=([^;]+)"));
  let userInfo = {
    username: "",
  };
  if (result && result[1]) {
    userInfo = parseJwt(result[1]);
  }
  if (userInfo.username === "") {
    return null;
  }
  return userInfo;
}
function parseJwt(token) {
  var base64Url = token.split(".")[1];
  var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
  var jsonPayload = decodeURIComponent(
    window
      .atob(base64)
      .split("")
      .map(function (c) {
        return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
      })
      .join("")
  );

  return JSON.parse(jsonPayload);
}

var user = readAuthUserInfo("user");

var buildRecipeList = function (recipes = []) {
  recipes.forEach(
    ({
      tiempoEnMinutos,
      categoria,
      creador,
      descripcion,
      foto1,
      foto2,
      foto3,
      foto4,
      foto5,
      idReceta,
      pasos,
      titulo,
      isFav,
    }) => {
      recipeList.innerHTML += ` 
              <article class="gap-4">
                <header class="container" class="recipelist__header">
                <a href="/profile?author=${creador}" class="recipelist__author">Autor: ${creador}</a>
                <a href="/recipe?id=${idReceta}" class="hover">
                  <div class="headings">
                    <h2>${titulo}</h2>
                    <h5>${descripcion}</h5>
                    <p>Listo en ${tiempoEnMinutos} minutos</p>
                  </div>
                </a>
                  <button class='${
                    isFav ? "remove-favourite destructive" : "add-favourite"
                  }' data-favourite-recipe-id="${idReceta}">${
        isFav ? "Quitar de favoritos" : "Agregar a favoritos"
      }</button>
                </header>
                <img src="${foto1}" alt="imagen" />
              </article>
    `;
    }
  );
};
var getFollowers = function (author) {
  return fetch("/api/follow").then((res) => res.json());
};
var stopFollowing = function (author) {
  return fetch("/api/follow", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      usuarioSeguido: author,
    }),
  }).then((res) => res.json());
};
var userFollowsMe = function (author) {
  return getFollowers().then((data) => data.usuarios.includes(author));
};
