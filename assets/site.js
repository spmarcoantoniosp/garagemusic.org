/* Liga cada botao ao checkout do seu codigo, controla o CTA da barra
   e o tamanho do texto. Um arquivo para todas as paginas. */
(function () {
  var mapa = window.CHECKOUTS || {};
  document.querySelectorAll('.js-checkout').forEach(function (a) {
    var url = mapa[a.getAttribute('data-cod')];
    if (url) {
      a.href = url;
      a.setAttribute('rel', 'noopener');
    } else {
      a.setAttribute('aria-disabled', 'true');
      a.removeAttribute('href');
    }
  });

  var alvo = document.querySelector('.capa-vit, .hero'),
      topoCta = document.getElementById('topoCta');
  if (alvo && topoCta && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (e) {
      topoCta.classList.toggle('on', !e[0].isIntersecting);
    }, { rootMargin: '-60px 0px 0px 0px' }).observe(alvo);
  }

  var f = document.getElementById('captura');
  if (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var i = f.querySelector('input');
      if (i && i.value.indexOf('@') > 0) {
        f.innerHTML = '<div class="ok">Feito. Voce vai ser o primeiro a saber quando sair material novo.</div>';
      } else if (i) {
        i.style.borderColor = '#DF892B';
        i.focus();
      }
    });
  }
})();

var base = 19;
function aplica(v) { document.documentElement.style.setProperty('--base', v + 'px'); }
function ajusta(d) { base = Math.min(26, Math.max(16, base + d)); aplica(base); }
function reset() { base = 19; aplica(base); }
