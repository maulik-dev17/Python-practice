// NOËL — Christmas party landing page interactions
const eventDate = new Date('{{EVENT_ISO}}');

function updateCountdown() {
  const now = new Date();
  const diff = Math.max(0, eventDate.getTime() - now.getTime());
  const values = {
    days: Math.floor(diff / 86400000),
    hours: Math.floor((diff / 3600000) % 24),
    minutes: Math.floor((diff / 60000) % 60),
    seconds: Math.floor((diff / 1000) % 60)
  };
  Object.entries(values).forEach(([id, value]) => {
    const el = document.getElementById(id);
    if (el) el.textContent = String(value).padStart(2, '0');
  });
}
updateCountdown();
setInterval(updateCountdown, 1000);

// Mobile navigation
const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav-links');
menuToggle?.addEventListener('click', () => {
  const isOpen = nav.classList.toggle('open');
  menuToggle.setAttribute('aria-expanded', String(isOpen));
  menuToggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  menuToggle?.setAttribute('aria-expanded', 'false');
}));

// RSVP demo: validates the form and prepares an email draft in the visitor's mail app.
// Connect a form backend (e.g. Formspree) before publishing to collect responses automatically.
const form = document.getElementById('rsvpForm');
const message = document.getElementById('formMessage');
form?.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const data = new FormData(form);
  const subject = encodeURIComponent('{{RSVP_SUBJECT}} — ' + data.get('name'));
  const body = encodeURIComponent(
    `Name: ${data.get('name')}\nEmail: ${data.get('email')}\nGuests: ${data.get('guests')}\nNote: ${data.get('note') || '—'}`
  );
  message.textContent = 'Your RSVP details are ready. Your email app will open so you can send them.';
  // Replace the address below with the event organizer's email address.
  window.location.href = `mailto:{{ORG_EMAIL}}?subject=${subject}&body=${body}`;
});

// ===== Real-site layer =====
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const toast = (msg) => { const t = $('#toast'); t.textContent = msg; t.classList.add('show'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 3200); };

// Preloader -> hero entrance
document.body.classList.add('loading');
const startSite = () => { $('#preloader')?.classList.add('done'); document.body.classList.remove('loading'); document.body.classList.add('ready'); };
window.addEventListener('load', () => setTimeout(startSite, reduce ? 0 : 1200));
setTimeout(startSite, 3500);

// Scroll: progress bar, sticky header, active nav, back-to-top, hero parallax
const toTop = Object.assign(document.createElement('button'), { className: 'to-top', innerHTML: '↑', ariaLabel: 'Back to top' });
toTop.onclick = () => scrollTo({ top: 0, behavior: 'smooth' }); document.body.appendChild(toTop);
const sections = $$('main section[id]'), links = $$('.nav-links a[href^="#"]:not(.nav-cta)'), art = $('.hero-art');
let ticking = false;
function onScroll() {
  const y = scrollY, max = document.documentElement.scrollHeight - innerHeight;
  $('#progress').style.width = (y / max * 100) + '%';
  $('.site-header').classList.toggle('scrolled', y > 60);
  toTop.classList.toggle('show', y > 700);
  if (art && !reduce && y < 900) art.style.transform = `translateY(${y * -0.08}px)`;
  const cur = sections.filter(s => s.getBoundingClientRect().top < innerHeight * 0.4).pop();
  links.forEach(a => a.classList.toggle('active', !!cur && a.getAttribute('href') === '#' + cur.id));
  ticking = false;
}
addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true }); onScroll();

// Scroll reveal (staggered)
$$('.section-kicker, .intro h2, .intro-text > *, .section-heading, .moment-card, .schedule-head, .timeline-row, .details-card, .details-side, .countdown-section > *, .rsvp-copy, .rsvp-form, .date-strip > div').forEach((el, i) => {
  el.classList.add('reveal'); el.style.setProperty('--d', (i % 4) * 0.12 + 's');
});
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.15 });
$$('.reveal').forEach(el => io.observe(el));

// 3D tilt on cards (desktop pointers only)
if (matchMedia('(hover:hover)').matches && !reduce) $$('.moment-card').forEach(c => {
  c.addEventListener('mousemove', e => { const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; c.style.transform = `perspective(700px) rotateY(${x * 8}deg) rotateX(${-y * 8}deg) translateY(-6px)`; });
  c.addEventListener('mouseleave', () => c.style.transform = '');
});

// Countdown tick animation + "it's today" state
let lastSec = null;
setInterval(() => { const s = $('#seconds'); if (s && s.textContent !== lastSec) { lastSec = s.textContent; s.classList.add('tick'); setTimeout(() => s.classList.remove('tick'), 220); } }, 250);
if (eventDate - Date.now() <= 0) $('.countdown-section h2').innerHTML = '{{PARTY_TIME}}';

// Add to calendar (.ics download)
$('#addCal')?.addEventListener('click', () => {
  const ics = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Noel//Party//EN', 'BEGIN:VEVENT', 'UID:{{SLUG}}@party', 'DTSTAMP:{{ICS_STAMP}}',
    'DTSTART:{{ICS_START}}', 'DTEND:{{ICS_END}}', 'SUMMARY:{{ICS_TITLE}}', 'DESCRIPTION:{{ICS_DESC}}', 'END:VEVENT', 'END:VCALENDAR'].join('\r\n');
  const a = Object.assign(document.createElement('a'), { href: URL.createObjectURL(new Blob([ics], { type: 'text/calendar' })), download: '{{SLUG}}.ics' });
  a.click(); toast('✳ ADDED — SEE YOU THERE!');
});

// RSVP polish
form?.addEventListener('submit', () => { if (form.checkValidity()) { form.classList.add('sent'); toast('✳ THANK YOU — RSVP READY TO SEND'); } });

// Falling particles: snow | confetti | embers | none (chosen per festival)
(function particles() {
  const mode = '{{PARTICLE}}', c = $('#snow'); if (!c || reduce || mode === 'none') return;
  const x = c.getContext('2d'), up = mode === 'embers';
  const cols = mode === 'confetti' ? ['{{RED}}', '{{GOLD}}', '#ffffff', '#5ad1c4', '#ff9ecb'] : up ? ['{{GOLD}}', '{{RED}}', '#ffd9a0'] : ['#ffffff'];
  let w, h, f = [];
  const size = () => { w = c.width = innerWidth; h = c.height = innerHeight;
    f = Array.from({ length: Math.min(90, Math.floor(w / 14)) }, () => ({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 2.4 + .8, s: Math.random() * .9 + .4, d: Math.random() * 6.3, c: cols[Math.floor(Math.random() * cols.length)] })); };
  size(); addEventListener('resize', size);
  (function draw() { x.clearRect(0, 0, w, h);
    f.forEach(p => { p.y += up ? -p.s : p.s; p.d += .02; p.x += Math.sin(p.d) * .5;
      if (p.y > h + 8) { p.y = -8; p.x = Math.random() * w; } if (p.y < -8) { p.y = h + 8; p.x = Math.random() * w; }
      x.globalAlpha = up ? .55 + Math.sin(p.d * 3) * .35 : .8; x.fillStyle = p.c;
      if (mode === 'confetti') { x.save(); x.translate(p.x, p.y); x.rotate(p.d * 2); x.fillRect(-p.r, -p.r * .5, p.r * 2.4, p.r); x.restore(); }
      else { x.beginPath(); x.arc(p.x, p.y, p.r, 0, 6.3); x.fill(); } });
    requestAnimationFrame(draw); })();
})();
