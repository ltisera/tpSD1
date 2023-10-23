/**
 * Inserta la barra de navegación arriba del todo
 *
 * Agrega botones para login, logout y backoffice (recetas del usuario)
 */
const nav = document.createElement("nav");
nav.innerHTML = `<nav class="container">
<ul>
  <li>
    <a href="/" class="contrast"><strong>ChefEnCasa</strong></a>
  </li>
</ul>
<ul>
  <li>
    <a href="/followers" class="secondary">Seguidores</a>
  </li>
  <li>
    <a href="/backoffice" class="secondary">Mis recetas</a>
  </li>
  <li>
    <a href="/login" id="login-link">Login</a>
  </li>
</ul>
</nav>`;
document.body.prepend(nav);

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

const loginLinkItem = document.querySelector("#login-link");
const user = readAuthUserInfo("user");
if (user) {
  loginLinkItem.textContent = "Logout";
  document.cookie = "";
}
