const addPackageBtn = document.getElementById("addPackage");
const getPackageBtn = document.getElementById("getPackage");

addPackageBtn.addEventListener("click", () => {
  const span = addPackageBtn.querySelector("span");
  span.classList.remove("visually-hidden");
});

getPackageBtn.addEventListener("click", () => {
  const span = getPackageBtn.querySelector("span");
  span.classList.remove("visually-hidden");
});