/* Aplica o tema salvo antes da página aparecer (evita piscar). */
try { if (localStorage.getItem('blasfen-tema') === 'light') document.documentElement.setAttribute('data-theme', 'light'); } catch (e) {}
