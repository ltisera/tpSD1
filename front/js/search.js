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
 * http://localhost:3000/?author=pepe&category=Almuerzo -> Recetas de pepe y categoría Almuerzo
 * ```
 *
 * @important Finalmente los inserta en el elemento con id `recipes-list`.
 *
 */

const formContainer = document.querySelector("#form-container");
const form = document.createElement("form");
form.innerHTML = `<form action="/" method="get" class="form">
<hgroup class="w-large">
  <label for="title">Titulo</label>
  <input type="text" name="title" id="title" />
</hgroup>
<hgroup>
  <label for="author">Creador</label>
  <input type="text" name="author" id="author" />
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
<hgroup class="w-medium">
  <label for="min-temp">Tiempo mínimo (min.)</label>
  <input type="number" min="0"  id="min-temp" name="min-temp"/>
</hgroup>
<hgroup class="w-medium">
  <label for="max-temp">Tiempo mínimo (máx.)</label>
  <input type="number" min="0"  id="max-temp" name="max-temp"/>
</hgroup>
<button type="reset" class="secondary">Limpiar</button>
<button type="submit">Buscar</button>
</form>`;
formContainer.appendChild(form);

const params = new URLSearchParams(window.location.search);
const title = params.get("title") || "";
const author = params.get("author") || "";
const category = params.get("category") || "";
const minTemp = params.get("min-temp") || "";
const maxTemp = params.get("max-temp") || "";
document.querySelector("#title").value = title;
document.querySelector("#author").value = author;
document.querySelector("#category").value = category;
document.querySelector("#min-temp").value = minTemp;
document.querySelector("#max-temp").value = maxTemp;

const recipeList = document.querySelector("#recipes-list");

const fetchRecipes = async () => {
  const recipes = await fetch("/api/recipes", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      categoria: category,
      creador: author,
      titulo: title,
      tiempoEnMinutosMIN: minTemp,
      tiempoEnMinutosMAX: maxTemp,
    }),
  }).then((res) => res.json());

  if (recipes.recetas.length === 0) {
    recipeList.innerHTML += `<h2>No se encontraron recetas</h2>
    <p>Intenta con otros filtros</p>
    `;
  }
  buildRecipeList(recipes.recetas);

  const addFavouriteButtons = document.querySelectorAll(".add-favourite");
  addFavouriteButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      const recipeId = event.target.getAttribute("data-favourite-recipe-id");
      fetch("/api/favs", {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          idReceta: recipeId,
        }),
      })
        .then((res) => res.json())
        .then(() => {
          window.location.reload();
        });
    });
  });

  const removeFavouriteButtons = document.querySelectorAll(".remove-favourite");
  removeFavouriteButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      const recipeId = event.target.getAttribute("data-favourite-recipe-id");
      fetch("/api/favs", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          idReceta: recipeId,
        }),
      })
        .then((res) => res.json())
        .then(() => {
          window.location.reload();
        });
    });
  });
};

fetchRecipes();
