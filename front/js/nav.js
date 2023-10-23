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
const loginLinkItem = document.querySelector("#login-link");

if (user) {
  loginLinkItem.textContent = "Logout";
  document.cookie = "";
}
