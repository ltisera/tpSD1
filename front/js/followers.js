const followingList = document.querySelector("#siguiendo-lista");
const followersCount = document.querySelector("#followers-count");

getFollowers().then((followers) => {
  followersCount.textContent =
    "Estas siguiendo a " + followers.usuarios.length + " usuario(s)";
  followers.usuarios.forEach((follower) => {
    const followerItem = document.createElement("li");
    followerItem.innerHTML = `<a href="/profile?author=${follower}">${follower}</a>`;
    followingList.appendChild(followerItem);
  });
});
