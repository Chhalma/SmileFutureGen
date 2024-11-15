// scripts.js

function scrollToSection(event, sectionId) {
    event.preventDefault(); // Prevent default anchor click behavior
    document.getElementById(sectionId).scrollIntoView({ behavior: "smooth" }); // Scroll to the specified section smoothly
}

window.onscroll = function() {toggleBackToTopButton()};

function toggleBackToTopButton() {
  const backToTopBtn = document.getElementById("backToTopBtn");
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    backToTopBtn.style.display = "block";
  } else {
    backToTopBtn.style.display = "none";
  }
}

// Smooth scroll to top
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
