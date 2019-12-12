let burger_El = document.querySelector("#burger_svg");
let meny_El = document.querySelector("#meny");
meny_El.style.display = "none";
burger_El.addEventListener("click", function() {
  let visning = meny_El.style.display;
  if (visning == "none") {
    meny_El.style.display = "block";
    gsap.to("#Line_1", {
      rotation: 43,
      duration: 1
    });
    gsap.to("#Line_2", {
      opacity: 0,
      duration: 1
    });
    gsap.to("#Line_3", {
      rotation: -43,
      duration: 1
    });
    gsap.from("#meny", {
      opacity: 0,
      duration: 0.5,
      x: 300
    });
  } else {
    meny_El.style.display = "none";
    gsap.to("#Line_1", {
      rotation: 0,
      duration: 1
    });
    gsap.to("#Line_2", {
      opacity: 1,
      duration: 1
    });
    gsap.to("#Line_3", {
      rotation: 0,
      duration: 1
    });
  }
});
