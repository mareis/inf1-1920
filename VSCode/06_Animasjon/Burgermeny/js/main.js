let burger_El = document.querySelector("#burger_svg");
let meny_El = document.querySelector("#meny");

function reset() {
  meny_El.style.display = "none";
  gsap.set("#meny", { opacity: 1, x: 0 });
}

reset();

burger_El.addEventListener("click", function() {
  let visning = meny_El.style.display;
  if (visning == "none") {
    meny_El.style.display = "block";
    gsap.to("#Line_1", { rotation: 43, duration: 0.8 });
    gsap.to("#Line_2", { opacity: 0, duration: 0.5 });
    gsap.to("#Line_3", { rotation: -43, duration: 0.8 });
    gsap.from("#meny", { opacity: 0, duration: 0.5, x: 300 });
  } else {
    gsap.to("#Line_1", { rotation: 0, duration: 0.8 });
    gsap.to("#Line_2", { opacity: 1, duration: 0.5 });
    gsap.to("#Line_3", { rotation: 0, duration: 0.8 });
    gsap.to("#meny", { opacity: 0, duration: 0.5, x: 300, onComplete: reset });
  }
});
