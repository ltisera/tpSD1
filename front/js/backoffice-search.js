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

const author = user.username;
const params = new URLSearchParams(window.location.search);
const titleSearchField = params.get("title") || "";
const categorySearchField = params.get("category") || "";
document.querySelector("#title").value = titleSearchField;
document.querySelector("#category").value = categorySearchField;

// ====== MODAL FORM ======
const title = document.getElementById("edit-titulo");
const id = document.getElementById("edit-id-input");
const description = document.getElementById("edit-descripcion");
const time = document.getElementById("edit-tiempoEnMinutos");
const category = document.getElementById("edit-categoria");
const steps = document.getElementById("edit-pasos");
const ingredients = document.getElementById("edit-ingredientes");
const image1 = document.getElementById("edit-foto1");
const image2 = document.getElementById("edit-foto2");
const image3 = document.getElementById("edit-foto3");
const image4 = document.getElementById("edit-foto4");
const image5 = document.getElementById("edit-foto5");

function clearForm() {
  id.value = "";
  titulo.value = "";
  description.value = "";
  time.value = "";
  category.value = "";
  steps.value = "";
  ingredients.value = "";
  image1.value = "";
  image2.value = "";
  image3.value = "";
  image4.value = "";
  image5.value = "";
}
function fillForm({
  titulo,
  descripcion,
  tiempoEnMinutos,
  categoria,
  pasos,
  ingredientes,
  foto1,
  foto2,
  foto3,
  foto4,
  foto5,
  idReceta,
}) {
  id.value = idReceta;
  title.value = titulo;
  description.value = descripcion;
  time.value = tiempoEnMinutos;
  category.value = categoria;
  steps.value = pasos;
  ingredients.value = ingredientes;
  image1.value = foto1;
  image2.value = foto2;
  image3.value = foto3;
  image4.value = foto4;
  image5.value = foto5;
}

/// ====== MODAL FORM ======

const recipeList = document.querySelector("#recipes-list");
fetch("/api/recipes", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    categoria: categorySearchField,
    creador: author,
    titulo: titleSearchField,
  }),
})
  .then((res) => res.json())
  .then((data = []) => {
    buildRecipeList(data.recetas);

    const recipesEditButtons = document.querySelectorAll(".recipe-edit-button");
    const recipesDeleteButtons = document.querySelectorAll(
      ".recipe-delete-button"
    );

    recipesEditButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        const id = e.target.getAttribute("data-recipeid");
        fetch("/api/recipes", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            idReceta: id,
          }),
        })
          .then((res) => res.json())
          .then((res) => {
            console.log(res.recetas[0]);
            clearForm();
            fillForm({ ...res.recetas[0], idReceta: id });
            editModal.showModal();
          });
      });
    });
    recipesDeleteButtons.forEach((button) => {
      button.addEventListener("click", (e) => {
        const id = e.target.getAttribute("data-recipeid");
        fetch("/api/recipe", {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            idReceta: id,
          }),
        }).then(() => {
          window.location.reload();
        });
      });
    });
  })
  .catch((err) => console.log(err));

document.querySelector("#user-name").textContent = "Hola, " + user.username;
