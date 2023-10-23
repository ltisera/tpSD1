const followersList = document.querySelector("#seguidores-lista");

fetch("/api/followers").then((response) => {
  response.json().then((followers) => {
    followers.forEach((follower) => {
      const followerItem = document.createElement("li");
      followerItem.innerHTML = `<a href="/followers/${follower.usuario}">${follower.usuario}</a>`;
      followersList.appendChild(followerItem);
    });
  });
});
