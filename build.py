#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador do site garagemusic.org.

Todo o conteudo do site esta neste arquivo, nas listas LOJA, ARTIGOS e DICAS.
Para publicar algo novo: acrescente um item na lista, rode `python3 build.py`
e faca o push. Cabecalho, rodape, navegacao e sitemap saem sozinhos.

    python3 build.py

Saida: index.html, store/index.html, artigos/index.html, dicas/index.html,
       404.html, sitemap.xml
"""

import os, datetime

RAIZ = os.path.dirname(os.path.abspath(__file__))
DOMINIO = "https://garagemusic.org"
HOJE = "2026-09-20"

# =====================================================================
# 1. LOJA — um item por ebook. O codigo (cod) casa com assets/checkouts.js
# =====================================================================

LOJA = [
    dict(cod="LH-801", titulo="Cinco Notas",
         inv="Cinco formas. Dez exercícios. Seis réguas",
         sub="A pentatônica menor no contrabaixo: cinco formas no braço e dez exercícios com alvo.",
         preco="R$ 47",
         capa="img/LH-801/vitrine-720x1040-cinco-notas.png"),

    dict(cod="LH-806", titulo="As Outras Cinco",
         inv="Duas pentatônicas. Doze exercícios. Zero desenho novo",
         sub="Pentatônica maior e escala de blues: o mesmo desenho, outra tônica, doze exercícios.",
         preco="R$ 47",
         capa="img/LH-806/vitrine-720x1040-as-outras-cinco.png"),

    dict(cod="LH-807", titulo="A Linha Que Anda",
         inv="Quatro tempos. Três caminhos. Doze exercícios",
         sub="Walking bass a partir da cifra: o esqueleto do compasso e doze exercícios com alvo.",
         preco="R$ 47",
         capa="img/LH-807/vitrine-720x1040-a-linha-que-anda.png"),

    dict(cod="LH-808", titulo="Onde Está o Arquivo",
         inv="Cinco campos. Três estados. Cinco pastas",
         sub="Nomear, versionar e recuperar projeto de áudio: cinco campos, três estados, doze exercícios.",
         preco="R$ 47",
         capa="img/LH-808/vitrine-720x1040-onde-esta-o-arquivo.png"),

    dict(cod="LH-809", titulo="O Que Vai na Bag",
         inv="Sete categorias. Cinco falhas. Doze exercícios",
         sub="O kit, os cinco modos de falha e o teste de dez minutos antes de sair de casa.",
         preco="R$ 47",
         capa="img/LH-809/vitrine-720x1040-o-que-vai-na-bag.png"),

    dict(cod="LH-810", titulo="Sem Ensaio",
         inv="Seis movimentos. Doze exercícios. Cinco sinais",
         sub="Decidir a linha de baixo no culto, em tempo real: seis movimentos e doze exercícios.",
         preco="R$ 47",
         capa="img/LH-810/vitrine-720x1040-sem-ensaio.png"),
]

PACK = dict(
    cod="KIT-MUSIC", titulo="Biblioteca Garage Music",
    inv="Seis ebooks. 219 páginas. Setenta exercícios",
    sub="Os seis ebooks de contrabaixo da casa: escalas, walking bass, arquivo, kit e o culto sem ensaio. "
        "Sai por menos do que a soma dos avulsos.",
    preco="R$ 127", risco="economia de R$ 155 sobre os seis avulsos",
)

INVENTARIO = [("6", "Ebooks"), ("219", "Páginas"), ("36", "Movimentos"),
              ("70", "Exercícios"), ("36", "Réguas")]

# =====================================================================
# 2. ARTIGOS — texto longo. etq: estudo | tecnica | equipamento |
#    historia | oficina | usado | ficha
#    Sem 'url' o item aparece como pauta declarada, sem link.
# =====================================================================

ARTIGOS = [
    dict(data="20 set 2026", etq="ficha", url="a-mesma-nota-em-tres-regioes/",
         titulo="A mesma nota em três regiões do braço",
         desc="Onde o Mi cai no baixo de 4, 5 e 6 cordas, e por que a casa não é a informação — "
              "a nota é. Tabela de transposição entre os três instrumentos.",
         corpo="""
<p class="lead">Quem aprendeu de ouvido decora caminho: a música começa naquela casa,
a mão vai para aquele lugar. Funciona até a banda subir meio tom. O que sustenta a
mudança não é lembrar da casa — é saber onde a nota está, e ela está em mais de um lugar.</p>

<h2>A afinação padrão, nos três instrumentos</h2>
<p>Todas em quartas justas, da corda grave para a aguda:</p>
<table>
<thead><tr><th>Instrumento</th><th>Cordas, da grave para a aguda</th></tr></thead>
<tbody>
<tr><td>4 cordas</td><td>Mi &middot; Lá &middot; Ré &middot; Sol</td></tr>
<tr><td>5 cordas</td><td><b>Si</b> &middot; Mi &middot; Lá &middot; Ré &middot; Sol</td></tr>
<tr><td>6 cordas</td><td><b>Si</b> &middot; Mi &middot; Lá &middot; Ré &middot; Sol &middot; <b>Dó</b></td></tr>
</tbody></table>
<p>O de 5 acrescenta um Si grave abaixo do Mi. O de 6 acrescenta esse mesmo Si e mais um
Dó agudo acima do Sol. O miolo — Mi, Lá, Ré, Sol — é igual nos três. É por isso que
qualquer desenho aprendido no de 4 cabe inteiro nos outros dois.</p>

<h2>Onde está o Mi</h2>
<p>Tomando o Mi como exemplo, ele aparece assim ao longo do braço. A coluna da direita
diz de qual Mi se trata, porque dois Mi na mesma altura não são a mesma nota.</p>
<table>
<thead><tr><th>Corda</th><th>Casa</th><th>Região</th><th>Altura</th></tr></thead>
<tbody>
<tr><td>Mi (4ª, ou 5ª no baixo de 5/6)</td><td>solta</td><td>pestana</td><td>Mi grave</td></tr>
<tr><td>Si (só no de 5 e 6)</td><td>5</td><td>primeira posição</td><td>Mi grave, o mesmo</td></tr>
<tr><td>Lá</td><td>7</td><td>meio do braço</td><td>Mi uma oitava acima</td></tr>
<tr><td>Ré</td><td>2</td><td>primeira posição</td><td>Mi uma oitava acima, o mesmo</td></tr>
<tr><td>Mi</td><td>12</td><td>oitava</td><td>Mi uma oitava acima, o mesmo</td></tr>
<tr><td>Sol</td><td>9</td><td>região aguda</td><td>duas oitavas acima</td></tr>
<tr><td>Ré</td><td>14</td><td>região aguda</td><td>duas oitavas acima, o mesmo</td></tr>
<tr><td>Dó (só no de 6)</td><td>4</td><td>primeira posição</td><td>duas oitavas acima, o mesmo</td></tr>
</tbody></table>
<p>Repare no que a tabela mostra: o Mi da oitava do meio está em <b>três lugares</b> —
Lá na casa 7, Ré na casa 2 e Mi na casa 12. Mesma nota, mesma altura, três regiões.
Qual delas usar não é questão de certo e errado; é questão de onde a mão já está e
para onde ela vai em seguida.</p>

<h2>A conta que transpõe entre os instrumentos</h2>
<p>Como as cordas estão em quartas justas, andar uma corda em direção ao agudo vale
<b>cinco casas</b>. Isso dá duas regras de bolso:</p>
<ul>
<li>Um desenho que começa na corda Si, casa <i>N</i>, cai na corda Mi na casa <i>N</i> menos 5.
Si na casa 5 é o mesmo Mi da corda Mi solta.</li>
<li>Um desenho que usa a corda Dó do baixo de 6 cabe na corda Sol somando 5 casas.
Dó na casa 4 é o mesmo Mi da corda Sol na casa 9.</li>
</ul>
<p>A exceção é a corda Sol para a corda Dó no baixo de seis, que também é quarta justa —
nesse ponto o instrumento não quebra o padrão. Guitarra quebra, entre a terceira e a
segunda corda. Baixo não.</p>

<h2>O que fazer com isso</h2>
<p>Da próxima vez que você travar porque a música mudou de tom, não procure a casa.
Procure a nota, e depois escolha entre as três regiões em que ela mora. É o mesmo trabalho
que um desenho de escala faz: tira a decisão da memória da música e coloca no braço.</p>
"""),

    dict(data="20 set 2026", etq="equipamento", url="impedancia-antes-de-ligar/",
         titulo="Impedância antes de ligar",
         desc="A conta que decide se a cabeça aguenta o gabinete. Quatro ohms, oito ohms, "
              "associação em série e em paralelo — e o erro que queima amplificador.",
         corpo="""
<p class="lead">É a conta mais barata que existe em equipamento de baixo, e a que mais
custa quando não é feita. Dois minutos lendo a traseira da cabeça e a do gabinete
resolvem o assunto para sempre.</p>

<h2>O que a cabeça está dizendo</h2>
<p>Toda cabeça traz uma <b>impedância mínima</b>. Escrito assim: “500 W em 4 Ω, 300 W em 8 Ω,
mínimo 4 Ω”. Leia como um limite de baixo, não como uma sugestão. Quanto menor a impedância
do que está ligado na saída, mais corrente o amplificador precisa entregar. Abaixo do mínimo
ele entra em proteção — quando tem proteção — ou esquenta até o dano.</p>
<p>Ir acima do mínimo é seguro. Um gabinete de 8 Ω numa cabeça de mínimo 4 Ω funciona,
só entrega menos potência. Ir abaixo é o problema.</p>

<h2>As duas contas</h2>
<p>Dois gabinetes ligados ao mesmo canal quase sempre ficam em <b>paralelo</b> — é como
a maioria das saídas de cabeça e das entradas duplas de gabinete é feita. Em paralelo a
impedância <i>cai</i>:</p>
<table>
<thead><tr><th>Combinação em paralelo</th><th>Resultado</th></tr></thead>
<tbody>
<tr><td>8 Ω + 8 Ω</td><td>4 Ω</td></tr>
<tr><td>8 Ω + 4 Ω</td><td>2,7 Ω</td></tr>
<tr><td>4 Ω + 4 Ω</td><td>2 Ω</td></tr>
</tbody></table>
<p>A regra é: divida o valor pela quantidade, quando as impedâncias são iguais. Quando são
diferentes, multiplique as duas e divida pela soma — 8 vezes 4 dá 32, dividido por 12 dá 2,7.
Em <b>série</b>, que é raro em baixo e precisa de cabo
próprio, a impedância <i>sobe</i> e basta somar: 8 Ω + 8 Ω dá 16 Ω.</p>

<h2>O erro clássico</h2>
<p>Cabeça de mínimo 4 Ω, um gabinete 4 Ω ligado, e alguém empresta um segundo gabinete 4 Ω
para o show grande. Os dois em paralelo dão 2 Ω — metade do mínimo. A cabeça pode aguentar
o som passando, ou pode desligar no meio da segunda música. Nenhum dos dois é o plano.</p>
<p>Com dois gabinetes de 8 Ω o mesmo arranjo dá 4 Ω e está dentro. Por isso, quando a ideia
é empilhar dois gabinetes um dia, comprar os dois em 8 Ω é a decisão que se toma antes,
não depois.</p>

<h2>Valvulado é outro assunto</h2>
<p>Em amplificador valvulado a saída tem transformador e a regra muda: o casamento precisa
ser feito nos dois sentidos, e há um terceiro cuidado — <b>nunca ligar valvulado sem carga</b>.
Cabeça valvulada tocando sem gabinete conectado danifica o transformador de saída. A seletora
de impedância na traseira existe justamente para casar; use a posição que corresponde ao que
está ligado.</p>

<h2>O que conferir antes de ligar</h2>
<ul>
<li>O mínimo impresso na traseira da cabeça.</li>
<li>A impedância de cada gabinete, também impressa na traseira.</li>
<li>Se forem dois, a conta em paralelo — e se o resultado está acima do mínimo.</li>
<li>Se for valvulado, a posição da seletora e se há gabinete conectado.</li>
</ul>
"""),

    dict(data="20 set 2026", etq="tecnica", url="ganho-e-volume/",
         titulo="Ganho e volume não são a mesma coisa",
         desc="O que cada botão faz no caminho do sinal, onde o clipping nasce e como achar "
              "o ponto de ganho sem depender do ouvido de quem está na mesa.",
         corpo="""
<p class="lead">Os dois aumentam o som, e é por isso que a confusão sobrevive. Só que um
decide o <i>tom</i> e o outro decide o <i>tamanho</i> — e usar o errado é o motivo mais comum
de um baixo chegar sujo na mesa sem ninguém saber por quê.</p>

<h2>Onde cada um mora no caminho do sinal</h2>
<table>
<thead><tr><th>Botão</th><th>Onde age</th><th>O que decide</th></tr></thead>
<tbody>
<tr><td><b>Ganho</b> (gain, input)</td><td>na entrada, antes do pré</td>
<td>o quanto o pré é empurrado — e, portanto, se o som satura ou fica limpo</td></tr>
<tr><td><b>Volume</b> (master, output)</td><td>na saída, depois do pré</td>
<td>o quanto sai para o gabinete, sem mexer no caráter do som</td></tr>
</tbody></table>
<p>É por isso que o clipping nasce no ganho. Subir o volume de um sinal já distorcido só
entrega distorção mais alta.</p>

<h2>Achar o ponto de ganho sem chutar</h2>
<p>A cabeça tem um LED de pico ou de clip. Ele não é decoração, é o instrumento de medida:</p>
<ul>
<li>Volume no mínimo. Ganho no mínimo.</li>
<li>Toque a passagem mais forte que você vai tocar de verdade — não um dedilhado educado.
Slap, se você usa slap. A corda mais grave, se é ela que estoura.</li>
<li>Suba o ganho até o LED piscar <b>só</b> nessas notas mais fortes. Se ele fica aceso, passou.</li>
<li>Agora suba o volume até o palco. O LED não deve mudar de comportamento.</li>
</ul>
<p>Se você quer saturação como som, o caminho é o mesmo — a diferença é que o ponto de
parada passa a ser o ouvido, e não o LED. O que não funciona é saturar sem querer e
chamar isso de volume.</p>

<h2>Baixo ativo pede o pad</h2>
<p>Instrumento ativo entrega um sinal bem mais quente que um passivo. Numa cabeça com chave
de <b>pad</b> — geralmente &minus;10 ou &minus;15 dB — essa chave existe para isso. Sem ela,
o ganho fica travado quase no mínimo e você perde toda a faixa útil do botão.</p>
<p>Pilha fraca no ativo, aliás, aparece primeiro como som mole e sujo, não como silêncio.
Antes de culpar o cabo, troque a bateria.</p>

<h2>E o que sai para a mesa</h2>
<p>A saída de DI costuma ter uma chave <b>pré/pós</b>. Em pós, vai o seu som já com equalização
e ganho; em pré, vai o sinal cru do instrumento e quem decide o resto é o técnico. Nenhuma das
duas é a certa sempre — mas vale saber em qual você está antes de reclamar do som da casa.</p>
"""),

    dict(etq="oficina", titulo="Setup: altura das cordas, tensão e relevo",
         desc="O ajuste que a maioria paga para fazer e dá para conferir em casa com uma "
              "régua de aço."),

    dict(etq="historia", titulo="Por que o Precision tem esse nome",
         desc="O trastejamento chegou depois do contrabaixo acústico, e mudou o que se "
              "esperava de um baixista dentro da banda."),
]

# =====================================================================
# 3. DICAS — nota curta, de leitura rápida.
# =====================================================================

DICAS = [
    dict(data="20 set 2026", etq="tecnica", titulo="A corda nova cai de afinação por três dias",
         desc="Não é defeito e não adianta apertar mais a tarracha. A corda está acomodando o "
              "enrolamento; estique cada uma puxando pelo meio do braço, reafine e repita "
              "três ou quatro vezes antes de desistir."),

    dict(data="20 set 2026", etq="equipamento", titulo="Cabo mudo quase sempre é o plug, não o cabo",
         desc="Antes de comprar outro, teste com o plug torcido enquanto o som está aberto. "
              "Se chiar ou voltar, é solda no plug — conserto de cinco minutos."),

    dict(data="20 set 2026", etq="tecnica", titulo="Afinador de pedal não serve no palco cheio",
         desc="Ele serve, mas não com a banda tocando: o microfone e as harmônicas de outros "
              "instrumentos confundem a leitura. Afine no silêncio e confira no intervalo."),

    dict(data="20 set 2026", etq="oficina", titulo="Decida o nome do arquivo antes de gravar",
         desc="Nome depois da gravação vira “mix final 2 OK agora vai”. Decida a regra antes: "
              "projeto, data, versão. Seis meses depois o que você procura é a versão, "
              "não a data."),

    dict(data="20 set 2026", etq="equipamento", titulo="O teste de dez minutos antes de sair de casa",
         desc="Ligue tudo montado como vai ficar no palco, com o cabo que você vai levar. "
              "A falha aparece em casa ou aparece na passagem de som — e só uma das duas dá tempo."),

    dict(data="20 set 2026", etq="estudo", titulo="Toque o exercício mais devagar do que você consegue",
         desc="Se dá para tocar sem errar, o metrônomo está rápido demais para aprender e "
              "lento demais para treinar. O ponto útil é onde você acerta com atenção, não no automático."),
]

ETQ_NOME = {"estudo": "Estudo", "tecnica": "Técnica", "equipamento": "Equipamento",
            "historia": "História", "oficina": "Oficina", "usado": "Usado",
            "ficha": "Ficha técnica"}

# =====================================================================
# Partes comuns
# =====================================================================

def head(titulo, desc, prof, extra=""):
    p = "../" * prof
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Garage Music">
<meta name="theme-color" content="#0B0B0D">
<link rel="icon" href="{p}img/logo-garage-music.png">
<link rel="stylesheet" href="{p}assets/fonts.css">
<link rel="stylesheet" href="{p}assets/base.css?v=2">
{extra}</head>
<body>
'''


def topo(atual, prof, cta=None):
    p = "../" * prof
    itens = [("", "Início"), ("artigos/", "Artigos"), ("dicas/", "Dicas"), ("store/", "Store")]
    links = ""
    for destino, rotulo in itens:
        cls = []
        if destino == atual:
            cls.append("on")
        if destino == "store/":
            cls.append("venda")
        c = f' class="{" ".join(cls)}"' if cls else ""
        links += f'<a href="{p}{destino}"{c}>{rotulo}</a>'

    bloco_cta = ""
    if cta:
        bloco_cta = (f'<div class="topoCta" id="topoCta"><span class="p">{cta["preco"]}</span>'
                     f'<a class="btn js-checkout" data-cod="{cta["cod"]}" href="#">{cta["rotulo"]}</a></div>')

    return f'''<div class="topo"><div class="wrap">
  <a class="marca" href="{p}"><img src="{p}img/logo-garage-music.png" alt="Garage Music" width="1200" height="197"></a>
  <nav class="nav">{links}</nav>
  {bloco_cta}<div class="az">
    <span>Texto</span>
    <button type="button" onclick="ajusta(-1)" aria-label="Diminuir o tamanho do texto">A&minus;</button>
    <button type="button" onclick="ajusta(1)" aria-label="Aumentar o tamanho do texto">A+</button>
    <button type="button" onclick="reset()" aria-label="Voltar ao tamanho padrão">Padrão</button>
  </div>
</div></div>
'''


def rodape(prof):
    p = "../" * prof
    return f'''<footer><div class="wrap">
  <img src="{p}img/logo-garage-music.png" alt="Garage Music" width="1200" height="197">
  <nav class="rod-nav">
    <a href="{p}">Início</a><a href="{p}artigos/">Artigos</a><a href="{p}dicas/">Dicas</a><a href="{p}store/">Store</a>
  </nav>
  <p class="rod">Aqui só entra o que foi testado. Cada ebook declara o que entrega, o que não entrega
  e o inventário contado no arquivo — não estimado.</p>
  <p class="rod">Pagamento, entrega e reembolso processados pela Hotmart. Garantia de 7 dias.</p>
  <p class="rod"><a href="https://instagram.com/garage.music" rel="noopener">@garage.music</a></p>
  <p class="end">© 2026 Garage Music</p>
</div></footer>
<script src="{p}assets/checkouts.js"></script>
<script src="{p}assets/site.js"></script>
</body></html>
'''


def card_produto(it, prof):
    p = "../" * prof
    return f'''<article class="card">
  <img src="{p}{it["capa"]}" width="720" height="1040" loading="lazy" alt="Capa de {it["titulo"]}">
  <div class="card-corpo">
    <p class="card-inv">{it["inv"]}</p>
    <h3>{it["titulo"]}</h3>
    <p class="card-sub">{it["sub"]}</p>
    <div class="card-pe">
      <span class="card-preco">{it["preco"]}</span>
      <a class="btn btn-s js-checkout" data-cod="{it["cod"]}" href="#">Comprar</a>
    </div>
  </div>
</article>'''


def linha_texto(it, tipo="artigo"):
    """tipo='artigo': o texto mora em pagina propria, entao a linha e um link
       (ou uma pauta declarada, quando ainda nao tem 'url').
       tipo='dica': a dica inteira ja esta na linha; nao ha para onde ir."""
    etq = f'<span class="etq etq-{it["etq"]}">{ETQ_NOME[it["etq"]]}</span>'
    miolo = (f'<div><h3 class="lt-t">{it["titulo"]}</h3>'
             f'<p class="lt-d">{it["desc"]}</p></div>')

    if tipo == "dica":
        return (f'<div class="linha-txt lt-nota">\n'
                f'  <div class="lt-meta">{etq}<span class="lt-data">{it["data"]}</span></div>\n'
                f'  {miolo}\n</div>')

    tem = "url" in it
    if tem:
        return (f'<a class="linha-txt" href="{it["url"]}">\n'
                f'  <div class="lt-meta">{etq}<span class="lt-data">{it["data"]}</span></div>\n'
                f'  {miolo}\n  <span class="lt-ir">Ler &rarr;</span>\n</a>')
    return (f'<div class="linha-txt lt-fila">\n'
            f'  <div class="lt-meta">{etq}<span class="lt-data">na fila</span></div>\n'
            f'  {miolo}\n  <span class="lt-ir">Em produção</span>\n</div>')


# =====================================================================
# Paginas
# =====================================================================

def pagina_home():
    h = head("Garage Music — contrabaixo, equipamento e estudo",
             "Toque com base. Estudo, equipamento e ebooks de contrabaixo, feitos a partir de execução própria.",
             0)
    h += topo("", 0)
    h += '''<header class="hero">
  <div class="hero-bg"><img src="img/hero-bg.jpg" alt=""></div>
  <div class="wrap">
    <p class="kicker">Baixo · equipamento · estudo</p>
    <h1 class="hero-wm"><span class="g">garage</span><span class="m">MUSIC</span></h1>
    <p class="frase"><b>Toque com base.</b> Aqui a gente estuda, testa e <em>mostra como chegou</em>.</p>
    <div class="hero-acoes">
      <a class="btn" href="store/">Ver a Store</a>
      <a class="btn btn-s btn-l" href="artigos/">Começar pelos artigos</a>
    </div>
  </div>
</header>

<section class="sec">
  <div class="wrap">
    <p class="sec-num">Por onde entrar</p>
    <h2>Três portas</h2>
    <div class="regua"></div>
    <div class="portas">
      <a class="porta" href="artigos/">
        <div class="p">Texto longo</div>
        <span class="t">Artigos</span>
        <p class="d">Assunto destrinchado até o fim: braço, equipamento, sinal, história do instrumento.
        Com tabela e diagrama quando a conversa pede.</p>
        <span class="mais">Ir para os artigos &rarr;</span>
      </a>
      <a class="porta" href="dicas/">
        <div class="p">Nota curta</div>
        <span class="t">Dicas</span>
        <p class="d">O que resolve agora: o cabo que chia, a corda que cai de afinação,
        o metrônomo no andamento errado. Leitura de um minuto.</p>
        <span class="mais">Ir para as dicas &rarr;</span>
      </a>
      <a class="porta" href="store/">
        <div class="p">Ebooks em PDF</div>
        <span class="t">Store</span>
        <p class="d">Seis ebooks de contrabaixo, do desenho no braço ao domingo sem ensaio.
        Entrega imediata e garantia de sete dias.</p>
        <span class="mais">Ir para a Store &rarr;</span>
      </a>
    </div>
  </div>
</section>

<section class="sec escura">
  <div class="wrap">
    <p class="sec-num">Na Store</p>
    <h2>Seis ebooks de contrabaixo</h2>
    <div class="regua"></div>
    <p class="lead">Guias curtos em PDF, feitos a partir de execução própria. Cada um declara o que
    entrega, o que não entrega, e traz o inventário contado no arquivo — não estimado.</p>
    <div class="inv" style="margin-top:30px">'''
    for n, r in INVENTARIO:
        h += f'<div class="cel"><div class="n">{n}</div><div class="r">{r}</div></div>'
    h += '''</div>
    <div class="hero-acoes" style="margin-top:34px">
      <a class="btn" href="store/">Ver os seis ebooks</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap dupla">
    <div>
      <p class="sec-num">Por que existe</p>
      <h2>Conhecimento musical honesto virou artigo raro.</h2>
      <div class="regua"></div>
      <p class="lead">Num mercado de atalho, quem estuda sozinho gasta mais tempo filtrando
      promessa do que praticando. Aqui a regra é curta: só afirma o que testou, e nunca vende atalho.</p>
      <p class="nota">Toque com base.</p>
    </div>
    <div class="captura">
      <h3>Um aviso, sem enrolação</h3>
      <p>Artigo novo, ebook novo, e nada além disso.</p>
      <form id="captura" novalidate>
        <input type="email" name="email" placeholder="seu@email.com" aria-label="Seu e-mail" required>
        <input type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true" hidden>
        <button class="btn btn-s" type="submit">Avise-me</button>
      </form>
      <p class="micro">Sem spam. Dá para sair em um clique.</p>
    </div>
  </div>
</section>
'''
    h += rodape(0)
    return h


def pagina_store():
    h = head("Store — Garage Music",
             "Seis ebooks de contrabaixo em PDF: pentatônicas, walking bass, arquivo de áudio, "
             "kit do músico e o culto sem ensaio. Entrega imediata.",
             1)
    h += topo("store/", 1, cta=dict(cod="KIT-MUSIC", preco="R$ 127", rotulo="Levar os seis"))
    h += f'''<header class="capa-vit">
  <div class="wrap">
    <p class="kicker">Catálogo · 6 títulos</p>
    <h1>Do desenho no braço ao domingo sem ensaio.</h1>
    <p class="capa-sub">Ebooks curtos em PDF, feitos a partir de execução própria. Cada um declara o que
    entrega e o que não entrega, e traz o inventário contado no arquivo — não estimado.</p>
  </div>
</header>

<section class="sec">
  <div class="wrap">
    <p class="sec-num">Comprar em conjunto</p>
    <h2>A coleção</h2>
    <div class="regua"></div>
    <article class="pack">
      <div>
        <p class="card-inv">{PACK["inv"]}</p>
        <h3>{PACK["titulo"]}</h3>
        <p class="card-sub">{PACK["sub"]}</p>
        <div class="card-pe">
          <span class="card-preco">{PACK["preco"]} <span class="nota" style="font-weight:400">· {PACK["risco"]}</span></span>
          <a class="btn js-checkout" data-cod="{PACK["cod"]}" href="#">Baixar os seis ebooks em PDF</a>
        </div>
      </div>
      <div class="pack-capas">'''
    for it in LOJA:
        h += (f'<img src="../{it["capa"]}" width="720" height="1040" loading="lazy" '
              f'alt="{it["titulo"]}">')
    h += '''</div>
    </article>
  </div>
</section>

<section class="sec escura">
  <div class="wrap">
    <p class="sec-num">Avulsos</p>
    <h2>Um tema por ebook</h2>
    <div class="regua"></div>
    <div class="grade">'''
    for it in LOJA:
        h += card_produto(it, 1)
    h += '''</div>
  </div>
</section>

<div class="faixa"><span>Entrega imediata em PDF · Garantia de 7 dias</span></div>

<section class="sec">
  <div class="wrap">
    <p class="sec-num">O limite</p>
    <h2>O que estes ebooks não entregam</h2>
    <div class="regua"></div>
    <p class="lead">Não são curso de leitura de partitura nem teoria para quem está começando no
    instrumento. Pressupõem que você já toca e quer parar de depender de música ensaiada.</p>
  </div>
</section>
'''
    h += rodape(1)
    return h


def pagina_lista(tipo, itens, titulo, kicker, h1, sub, atual):
    h = head(f"{titulo} — Garage Music", sub, 1)
    h += topo(atual, 1)
    h += f'''<header class="capa-vit">
  <div class="wrap">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="capa-sub">{sub}</p>
  </div>
</header>

<section class="sec">
  <div class="wrap">
'''
    for it in itens:
        h += linha_texto(it, tipo) + "\n"
    h += '''  </div>
</section>

<section class="sec escura">
  <div class="wrap">
    <p class="sec-num">Aplicar em cima do instrumento</p>
    <h2>Os ebooks levam isso até o braço</h2>
    <div class="regua"></div>
    <p class="lead">O que aqui é leitura, na Store vira exercício com alvo declarado e régua de
    conferência. Seis ebooks em PDF, entrega imediata.</p>
    <div class="hero-acoes" style="margin-top:30px"><a class="btn" href="../store/">Ver a Store</a></div>
  </div>
</section>
'''
    h += rodape(1)
    return h


def pagina_artigo(it, anterior, proximo):
    """Pagina de texto longo. prof=2 porque mora em /artigos/<slug>/."""
    h = head(f'{it["titulo"]} — Garage Music', it["desc"], 2)
    h += topo("artigos/", 2)
    h += f'''<header class="capa-vit capa-art">
  <div class="wrap">
    <p class="art-meta"><span class="etq etq-{it["etq"]}">{ETQ_NOME[it["etq"]]}</span>
      <span class="lt-data">{it["data"]}</span></p>
    <h1>{it["titulo"]}</h1>
    <p class="capa-sub">{it["desc"]}</p>
  </div>
</header>

<article class="sec"><div class="wrap"><div class="artigo">
{it["corpo"].strip()}
</div></div></article>

<section class="sec escura">
  <div class="wrap">
    <p class="sec-num">Aplicar em cima do instrumento</p>
    <h2>Os ebooks levam isso até o braço</h2>
    <div class="regua"></div>
    <p class="lead">O que aqui é leitura, na Store vira exercício com alvo declarado e régua
    de conferência. Seis ebooks em PDF, entrega imediata.</p>
    <div class="hero-acoes" style="margin-top:30px"><a class="btn" href="../../store/">Ver a Store</a></div>
  </div>
</section>

<section class="sec"><div class="wrap"><nav class="vizinhos">'''
    if anterior:
        h += (f'<a class="viz" href="../{anterior["url"]}"><span class="p">&larr; Anterior</span>'
              f'<span class="t">{anterior["titulo"]}</span></a>')
    else:
        h += '<span></span>'
    if proximo:
        h += (f'<a class="viz viz-d" href="../{proximo["url"]}"><span class="p">Próximo &rarr;</span>'
              f'<span class="t">{proximo["titulo"]}</span></a>')
    h += '''</nav>
<p style="margin-top:30px"><a href="../">&larr; Todos os artigos</a></p>
</div></section>
'''
    h += rodape(2)
    return h


def pagina_404():
    h = head("Página não encontrada — Garage Music", "Esta página não existe.", 0)
    h += topo("", 0)
    h += '''<header class="capa-vit">
  <div class="wrap">
    <p class="kicker">Erro 404</p>
    <h1>Essa página não está aqui.</h1>
    <p class="capa-sub">Ou o endereço mudou, ou o link veio errado. As três portas do site continuam abertas.</p>
  </div>
</header>
<section class="sec"><div class="wrap"><div class="portas">
  <a class="porta" href="/artigos/"><div class="p">Texto longo</div><span class="t">Artigos</span></a>
  <a class="porta" href="/dicas/"><div class="p">Nota curta</div><span class="t">Dicas</span></a>
  <a class="porta" href="/store/"><div class="p">Ebooks em PDF</div><span class="t">Store</span></a>
</div></div></section>
'''
    h += rodape(0)
    return h


def sitemap():
    urls = [("/", "1.0"), ("/store/", "0.9"), ("/artigos/", "0.8"), ("/dicas/", "0.8")]
    urls += [(f'/artigos/{a["url"]}', "0.7") for a in ARTIGOS if "url" in a]
    x = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, p in urls:
        x.append(f'  <url><loc>{DOMINIO}{u}</loc><lastmod>{HOJE}</lastmod><priority>{p}</priority></url>')
    x.append('</urlset>')
    return "\n".join(x) + "\n"


def escreve(caminho, conteudo):
    p = os.path.join(RAIZ, caminho)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"  {caminho:28} {len(conteudo.encode('utf-8')):>7,} bytes")


if __name__ == "__main__":
    print("garagemusic.org — build")
    escreve("index.html", pagina_home())
    escreve("store/index.html", pagina_store())
    escreve("artigos/index.html", pagina_lista(
        "artigo", ARTIGOS, "Artigos", "Texto longo",
        "O assunto destrinchado até o fim.",
        "Braço, equipamento, sinal e história do instrumento. Com tabela e diagrama quando a conversa pede.",
        "artigos/"))
    escreve("dicas/index.html", pagina_lista(
        "dica", DICAS, "Dicas", "Nota curta",
        "O que resolve agora.",
        "Leitura de um minuto para o problema que aparece na hora: o cabo que chia, a corda que cai de afinação, o metrônomo no andamento errado.",
        "dicas/"))
    pub = [a for a in ARTIGOS if "url" in a]
    for i, a in enumerate(pub):
        escreve(f'artigos/{a["url"]}index.html',
                pagina_artigo(a, pub[i - 1] if i else None,
                              pub[i + 1] if i + 1 < len(pub) else None))
    escreve("404.html", pagina_404())
    escreve("sitemap.xml", sitemap())
    print(f"\n  {len(LOJA)} ebooks · {len(pub)} artigos publicados "
          f"({len(ARTIGOS) - len(pub)} na fila) · {len(DICAS)} dicas")
