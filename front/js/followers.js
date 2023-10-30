const followingList = document.querySelector("#siguiendo-lista");
const followingCount = document.querySelector("#following-count");
const followersList = document.querySelector("#seguidores-lista");
const followersCount = document.querySelector("#followers-count");

getFollowers().then((followers) => {
  if (!followers?.usuarios?.length) {
    followersCount.textContent = "No te sigue nadie";
    return;
  }
  followersCount.textContent =
    "Te siguen " + followers.usuarios.length + " usuario(s)";
  followers?.usuarios.forEach((follower) => {
    const followerItem = document.createElement("li");
    followerItem.innerHTML = `<a href="/profile?author=${follower}">${follower}</a>`;
    followersList.appendChild(followerItem);
  });
});

getFollowing().then((following) => {
  if (!following?.usuarios?.length) {
    followingCount.textContent = "No seguis a nadie";
    return;
  }
  followingCount.textContent =
    "Seguis a " + following.usuarios.length + " usuario(s)";
  following?.usuarios.forEach((follower) => {
    const followerItem = document.createElement("li");
    followerItem.innerHTML = `<a href="/profile?author=${follower}">${follower}</a>`;
    followingList.appendChild(followerItem);
  });
});
