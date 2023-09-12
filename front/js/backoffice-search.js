/**
 * Este script construye la lista de recetas que se muestran en la página de búsqueda.
 *
 * Inserta un formulario de búsqueda adentro de donde haya un elemento con id `form-container`.
 *
 * Para ello, hace una petición al servidor con los parámetros de búsqueda.
 *
 * Los parámetros de búsqueda se obtienen de la URL, por ejemplo:
 * @example
 * ```
 * http://localhost:3000/backoffice/?author=pepe&category=Almuerzo -> Recetas de pepe y categoría Almuerzo
 * ```
 *
 * @important Finalmente los inserta en el elemento con id `recipes-list`.
 *
 */

const formContainer = document.querySelector("#form-container");
const form = document.createElement("form");
form.innerHTML = `<form action="/backoffice" method="get" class="form">
<hgroup>
  <label for="title">Titulo</label>
  <input type="text" name="title" id="title" />
</hgroup>
<hgroup>
  <label for="category">Categoria</label>
  <select name="category" id="category">
    <option value="">Todas</option>
    <option value="desayuno">Desayuno</option>
    <option value="almuerzo">Almuerzo</option>
    <option value="cena">Cena</option>
  </select>
</hgroup>
<button type="reset" class="secondary">Limpiar</button>
<button type="submit">Buscar</button>
</form>`;
formContainer.appendChild(form);

const params = new URLSearchParams(window.location.search);
const title = params.get("title") || "";
const author = user.username;
const category = params.get("category") || "";
document.querySelector("#title").value = title;
document.querySelector("#category").value = category;

const recipeList = document.querySelector("#recipes-list");
fetch("/api/recipes", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    categoria: category,
    creador: author,
    titulo: title,
  }),
})
  .then((res) => res.json())
  .then((data = []) => {
    console.log(data);
    const {} = data;

    data.recetas.forEach(
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
      }) => {
        recipeList.innerHTML += ` <a href="" class="hover">
            <article>
              <header class="container">
                <div class="headings">
                  <h2>${titulo}</h2>
                  <h5>${descripcion}</h5>
                  <small>Autor: ${creador}</small>
                  <p>Listo en ${tiempoEnMinutos} minutos</p>
                </div>
              </header>
              <img src="${foto1}" alt="imagen" />
            </article>
          </a>`;
      }
    );
  })
  .catch((err) => console.log(err));

document.querySelector("#user-name").textContent = "Hola, " + user.username;
