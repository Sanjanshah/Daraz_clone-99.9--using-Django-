// Slider control
let currentSlide = 0;
const slides = document.querySelectorAll('#slider figure img');

function showSlide(n) {
    slides.forEach((slide, index) => {
        slide.style.transform = `translateX(-${n * 100}%)`;
    });
}

// Auto-slide
setInterval(() => {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}, 5000);

// Dropdown control
document.getElementById('help-nav-link').addEventListener('mouseover', () => {
    document.getElementById('nav-help-dropdown').style.display = 'block';
});

document.getElementById('help-nav-link').addEventListener('mouseout', () => {
    document.getElementById('nav-help-dropdown').style.display = 'none';
});

// Cart functionality
document.querySelector('.cart').addEventListener('click', () => {
    // Add cart logic here
    console.log('Cart clicked');
});