const userIconBtn = document.querySelector(".header-user-icon");
const gobackIconBtn = document.querySelector(".header-user-icon-2");
const myAccount = document.querySelector(".my-account");
const activityDropdown = document.querySelector(
  ".my-account-activity-right-list"
);

userIconBtn.addEventListener("click", () => {
  myAccount.style.display = "block";
});

gobackIconBtn.addEventListener("click", () => {
  myAccount.style.display = "none";
});

const openActivityButton = document.querySelector(
  ".my-account-activity-right>section"
);

openActivityButton.addEventListener("click", () => {
  activityDropdown.classList.toggle("open-activity-dropdown");
});
