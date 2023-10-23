const followersList = document.querySelector("#seguidores-lista");
const followersCount = document.querySelector("#followers-count");

getFollowers().then((followers) => {
  followersCount.textContent =
    "Tenes " + followers.usuarios.length + " seguidor(es)";
  followers.usuarios.forEach((follower) => {
    const followerItem = document.createElement("li");
    followerItem.innerHTML = `<a href="/profile?author=${follower}">${follower}</a>`;
    followersList.appendChild(followerItem);
  });
});
