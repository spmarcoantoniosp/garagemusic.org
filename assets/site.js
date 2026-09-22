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

  /* Formulario de aviso. Destino e mensagens vem dos data-* que o build.py
     escreve a partir do dict CAPTURA. Duas rotas:
       data-endpoint preenchido -> POST para o servico de lista;
       data-endpoint vazio      -> modo carta, abre o e-mail do visitante.
     Falha de POST cai na carta. Nenhuma das rotas finge que enviou. */
  var f = document.getElementById('captura');
  if (f) {
    var campo = f.querySelector('input[type=email]'),
        isca = f.querySelector('input[name=site]'),
        botao = f.querySelector('button'),
        aviso = document.getElementById('capturaAviso'),
        txt = function (k) { return f.getAttribute('data-' + k) || ''; },
        extra = {};
    try { extra = JSON.parse(txt('extra') || '{}'); } catch (err) { extra = {}; }

    function diz(chave, classe) {
      if (!aviso) return;
      aviso.className = 'aviso' + (classe ? ' ' + classe : '');
      aviso.textContent = txt(chave);
    }
    function pronto(chave) {
      f.innerHTML = '<div class="ok">' + txt(chave) + '</div>';
      if (aviso) { aviso.textContent = ''; aviso.className = 'aviso'; }
    }
    function carta(email, chave) {
      var corpo = 'Quero receber os avisos da Garage Music.\r\n\r\nMeu e-mail: ' + email;
      window.location.href = 'mailto:' + txt('para') +
        '?subject=' + encodeURIComponent(txt('assunto')) +
        '&body=' + encodeURIComponent(corpo);
      pronto(chave);
    }

    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = campo ? campo.value.trim() : '',
          at = email.lastIndexOf('@');
      if (at < 1 || email.indexOf('.', at) < at + 2 || /\s/.test(email)) {
        if (campo) { campo.style.borderColor = '#DF892B'; campo.focus(); }
        diz('invalido', 'erro');
        return;
      }
      if (campo) campo.style.borderColor = '';
      if (isca && isca.value) { pronto('ok'); return; }   /* robo: sai sem avisar */

      var destino = txt('endpoint');
      if (!destino) { carta(email, 'carta'); return; }

      if (botao) botao.disabled = true;
      diz('enviando', '');
      var dados = new FormData();
      dados.append('email', email);
      Object.keys(extra).forEach(function (k) { dados.append(k, extra[k]); });

      fetch(destino, { method: 'POST', body: dados, headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error(r.status);
          pronto('ok');
        })
        .catch(function () {
          if (botao) botao.disabled = false;
          diz('falhou', 'erro');
          carta(email, 'carta');
        });
    });
  }
})();

var base = 19;
function aplica(v) { document.documentElement.style.setProperty('--base', v + 'px'); }
function ajusta(d) { base = Math.min(26, Math.max(16, base + d)); aplica(base); }
function reset() { base = 19; aplica(base); }
