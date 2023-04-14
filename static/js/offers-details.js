const openOffersDetailsBtn = document.querySelector(".offers-card-footer");
const closeOffersDetailsBtn = document.querySelector(".close-offers-details");

const openOffersDetails = () => {
  document.querySelector(".offers-details").style.display = "block";
};

const closeOffersDetails = () => {
  document.querySelector(".offers-details").style.display = "none";
};

openOffersDetailsBtn.addEventListener("click", openOffersDetails);
closeOffersDetailsBtn.addEventListener("click", closeOffersDetails);

const offersDetailsStepsBtn = document.querySelector(
  ".offers-details-steps-btn"
);
const offersDetailsStepsList = document.querySelector(
  ".offers-details-steps-list"
);

offersDetailsStepsBtn.addEventListener("click", () => {
  offersDetailsStepsList.classList.toggle("close-offers-details-steps-list");
});
