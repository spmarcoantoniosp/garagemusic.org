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

  /* Captura de e-mail. O endereco de destino e o assunto ficam aqui: o
     FormSubmit repassa o cadastro por e-mail, sem backend proprio. */
  var DESTINO = 'https://formsubmit.co/ajax/facilitadores@garagecriativa.com.br',
      ASSUNTO = 'Garage Music #garagemusic - novo cadastro';

  var f = document.getElementById('captura');
  if (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var i = f.querySelector('input[type=email]'),
          b = f.querySelector('button'),
          isca = f.querySelector('input[name=_honey]');
      if (!i) { return; }
      if (i.value.indexOf('@') < 1) {
        i.style.borderColor = '#DF892B';
        i.focus();
        return;
      }
      if (isca && isca.value) { return; }  /* a isca so e preenchida por robo */

      b.disabled = true;
      b.textContent = 'Enviando...';
      fetch(DESTINO, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          email: i.value,
          _subject: ASSUNTO,
          _template: 'table',
          _captcha: 'false'
        })
      }).then(function (r) {
        if (!r.ok) { throw new Error(r.status); }
        return r.json();
      }).then(function (d) {
        if (String(d.success) !== 'true') { throw new Error(d.message || 'recusado'); }
        f.innerHTML = '<div class="ok">Feito. Voce vai ser o primeiro a saber quando sair material novo.</div>';
      })['catch'](function () {
        b.disabled = false;
        b.textContent = 'Avise-me';
        var erro = f.parentNode.querySelector('.erro');
        if (!erro) {
          erro = document.createElement('p');
          erro.className = 'micro erro';
          erro.setAttribute('role', 'alert');
          f.parentNode.insertBefore(erro, f.nextSibling);
        }
        erro.textContent = 'Nao deu para enviar agora. Tente de novo em instantes, ou '
                         + 'escreva para facilitadores@garagecriativa.com.br.';
      });
    });
  }
})();

var base = 19;
function aplica(v) { document.documentElement.style.setProperty('--base', v + 'px'); }
function ajusta(d) { base = Math.min(26, Math.max(16, base + d)); aplica(base); }
function reset() { base = 19; aplica(base); }
