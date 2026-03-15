/* ── Shared site interactions ── */
(function () {
  // Nav scroll shadow
  const nav = document.querySelector('nav');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 12);
  }, { passive: true });

  // Hamburger toggle
  const ham   = document.querySelector('.hamburger');
  const links = document.querySelector('.nav-links');
  if (ham) {
    ham.addEventListener('click', () => {
      ham.classList.toggle('open');
      links.classList.toggle('open');
    });
    // Close on link click
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        ham.classList.remove('open');
        links.classList.remove('open');
      });
    });
  }

  // Active link
  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    if (a.getAttribute('href') === page) a.classList.add('active');
  });

  // Scroll reveal (IntersectionObserver)
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    reveals.forEach(el => io.observe(el));
  }
})();

/* ── Floating music notes (home page only) ── */
function spawnFloatingNotes(containerId) {
  const wrap = document.getElementById(containerId);
  if (!wrap) return;
  const symbols = ['♩','♪','♫','♬','♭','♯'];
  const colors  = ['rgba(96,165,250,0.55)','rgba(147,197,253,0.45)','rgba(59,130,246,0.5)','rgba(29,78,216,0.6)'];

  setInterval(() => {
    const el = document.createElement('span');
    el.textContent  = symbols[Math.floor(Math.random() * symbols.length)];
    const size  = 12 + Math.random() * 20;
    const left  = 5  + Math.random() * 90;
    const dur   = 5  + Math.random() * 5;
    const delay = Math.random() * 1.5;
    el.style.cssText = `
      position:absolute; left:${left}%; bottom:0;
      font-size:${size}px;
      color:${colors[Math.floor(Math.random() * colors.length)]};
      animation: float-up ${dur}s ${delay}s ease-out forwards;
      pointer-events:none; user-select:none; z-index:0;
    `;
    wrap.appendChild(el);
    setTimeout(() => el.remove(), (dur + delay) * 1000 + 200);
  }, 700);
}
