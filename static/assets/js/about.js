// FAQ Toggle Logic
    document.querySelectorAll('.faq-toggle').forEach(btn => {
        btn.addEventListener('click', () => {
        const content = btn.nextElementSibling;
        content.classList.toggle('hidden');
        btn.querySelector('i').classList.toggle('fa-chevron-down');
        btn.querySelector('i').classList.toggle('fa-chevron-up');
    });
});