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
