const sortByButton = document.querySelector(".sort-by-button");
const sortByList = document.querySelector(".sort-by-list");

sortByButton.addEventListener("click", () => {
  sortByList.classList.toggle("show-sort-by-list");
});

const offersButton = document.querySelector(".all-offers-menu-button");
const offersList = document.querySelector(".all-offers-menu-list");

offersButton.addEventListener("click", () => {
  offersList.classList.toggle("show-all-offers-menu-list");
});
