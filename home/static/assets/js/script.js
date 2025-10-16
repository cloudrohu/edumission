document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeBtn = document.getElementById('close-btn');

    // 📱 Open Mobile Menu
    menuBtn.addEventListener('click', () => {
      mobileMenu.classList.remove('translate-x-full');
      mobileMenu.classList.add('translate-x-0');
    });

    // ❌ Close Mobile Menu
    closeBtn.addEventListener('click', () => {
      mobileMenu.classList.remove('translate-x-0');
      mobileMenu.classList.add('translate-x-full');
    });

    // Optional: Close menu when clicking outside panel
    document.addEventListener('click', (e) => {
      if (!mobileMenu.contains(e.target) && !menuBtn.contains(e.target)) {
        mobileMenu.classList.remove('translate-x-0');
        mobileMenu.classList.add('translate-x-full');
      }
    });
  });

    const container = document.getElementById('servicesContainer');
  document.getElementById('nextBtn').addEventListener('click', () => {
    container.scrollBy({ left: 350, behavior: 'smooth' });
  });
  document.getElementById('prevBtn').addEventListener('click', () => {
    container.scrollBy({ left: -350, behavior: 'smooth' });
  });

   const wrapper = document.getElementById('testimonialWrapper');
  const dots = document.querySelectorAll('.dot');
  let currentIndex = 0;
  const totalSlides = dots.length;

  function showSlide(index) {
    wrapper.style.transform = `translateX(-${index * 100}%)`;
    dots.forEach(dot => dot.classList.remove('opacity-80'));
    dots.forEach(dot => dot.classList.add('opacity-30'));
    dots[index].classList.add('opacity-80');
    dots[index].classList.remove('opacity-30');
    currentIndex = index;
  }

  // Dot Click
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      showSlide(i);
      resetAutoScroll();
    });
  });

  // Auto Scroll
  let autoScroll = setInterval(() => {
    let next = (currentIndex + 1) % totalSlides;
    showSlide(next);
  }, 4000);

  function resetAutoScroll() {
    clearInterval(autoScroll);
    autoScroll = setInterval(() => {
      let next = (currentIndex + 1) % totalSlides;
      showSlide(next);
    }, 4000);
  }