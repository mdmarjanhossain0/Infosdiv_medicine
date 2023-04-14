const tabButtons = document.querySelectorAll(".tabs-btn");
const tabItems = document.querySelectorAll(".tabs-item");

const setTabs = (index) => {
  for (let i = 0; i < tabButtons.length; i++) {
    if (index == i) {
      tabItems[i].style.display = "block";
      tabButtons[i].style.background = "";
      tabButtons[i].style.boxShadow = "";
      tabButtons[i].classList.add("select-tab")
    } else {
      tabItems[i].style.display = "none";
      tabButtons[i].style.background = "none";
      tabButtons[i].style.boxShadow = "none";
      tabButtons[i].classList.add("tabs-btn");
    }
  }
};

const getIndex = (classLists, element) => {
  return Array.from(classLists).indexOf(element);
};

tabButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const index = getIndex(tabButtons, btn);
    setTabs(index);
  });
});

window.addEventListener("DOMContentLoaded", () => {
  setTabs(0);
});
