const author = new URLSearchParams(window.location.search).get("author") || "";
const recipeList = document.querySelector("#recipes-list");

const fetchRecipes = async () => {
  const recipes = await fetch("/api/recipes", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      creador: author,
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

const profileNameElement = document.querySelector(".headings h2");
const params = new URLSearchParams(window.location.search);
const profileName = params.get("author") || "";
const followBtn = document.querySelector("#follow-btn");
profileNameElement.textContent = `Recetas de ${profileName}`;

const follow = async () => {
  const follow = await fetch("/api/follow", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      usuarioSeguido: profileName,
    }),
  }).then((res) => res.json());
  window.location.reload();
};

followBtn.textContent = "Seguir";
followBtn.addEventListener("click", follow);
