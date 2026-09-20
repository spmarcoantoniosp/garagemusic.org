# garagemusic.org

Site da Garage Music. Estático, publicado por GitHub Pages a partir da raiz
da branch `main`. Identidade Brand Book v4 — Space Grotesk e Source Sans 3
embutidas em base64, âmbar Rust Brasa como acento, fundo preto.

## Estrutura

| Caminho | O que é |
|---|---|
| `/` | Home — as três portas e o convite para a Store |
| `/artigos/` | Índice de texto longo, com os publicados e a fila |
| `/artigos/<slug>/` | Uma página por artigo |
| `/dicas/` | Notas curtas; o texto inteiro fica no próprio índice |
| `/store/` | Catálogo: seis ebooks avulsos e a Biblioteca |
| `/assets/` | `fonts.css`, `base.css`, `checkouts.js`, `site.js` |
| `/img/LH-8xx/` | Capas 720×1040 de cada ebook |

## Como publicar conteúdo novo

Todo o conteúdo do site mora nas listas `LOJA`, `ARTIGOS` e `DICAS` dentro de
`build.py`. Não edite o HTML gerado — ele é sobrescrito.

```bash
# 1. edite build.py (uma entrada por item)
# 2. gere as páginas
python3 build.py
# 3. publique
git add -A && git commit -m "Publica <o que mudou>" && git push
```

**Dica nova:** acrescente um `dict` em `DICAS` com `data`, `etq`, `titulo` e
`desc`. O texto inteiro da dica é o `desc` — não existe página de detalhe.

**Artigo novo:** acrescente um `dict` em `ARTIGOS`. Com `url` e `corpo` ele é
publicado e ganha página própria; sem esses dois campos ele aparece no índice
como pauta declarada, marcado "em produção". O `corpo` é HTML: `<h2>`, `<p>`,
`<ul>`, `<table>` e a classe `lead` no primeiro parágrafo.

**Etiquetas disponíveis** (sistema obrigatório do Brand Book v4):
`estudo` e `tecnica` saem em aço; `equipamento`, `historia`, `oficina` e
`usado` saem em âmbar; `ficha` sai em branco.

## Captura de e-mail

O formulário da home envia por [FormSubmit](https://formsubmit.co) — sem backend
próprio. `assets/site.js` faz `POST` em JSON para o endpoint AJAX e trata os três
caminhos: e-mail inválido (borda âmbar, sem envio), sucesso (troca o formulário
pela confirmação) e falha de rede (mensagem de erro e botão reabilitado).

| O que | Onde |
|---|---|
| Destino | `DESTINO`, no topo do bloco em `assets/site.js` |
| Assunto | `ASSUNTO` — leva `#garagemusic` para filtrar na caixa |
| Isca anti-robô | campo `_honey`, oculto, no markup dentro de `build.py` |

Para trocar o destino, edite `DESTINO` — e lembre que o novo endereço volta a
exigir a confirmação única. O endereço fica visível no HTML público; o FormSubmit
oferece um token hasheado depois da primeira confirmação, que substitui o
endereço no endpoint e tira o e-mail do alcance dos scrapers.

## Checkouts

`assets/checkouts.js` é o único lugar com URL de Hotmart. O botão lê o código
em `data-cod` e monta o link sozinho. Código que não estiver no mapa deixa o
botão desativado, em vez de levar a lugar nenhum.

| Código | Título | Preço |
|---|---|---|
| LH-801 | Cinco Notas | R$ 47 |
| LH-806 | As Outras Cinco | R$ 47 |
| LH-807 | A Linha Que Anda | R$ 47 |
| LH-808 | Onde Está o Arquivo | R$ 47 |
| LH-809 | O Que Vai na Bag | R$ 47 |
| LH-810 | Sem Ensaio | R$ 47 |
| KIT-MUSIC | Biblioteca Garage Music | R$ 127 |

Levantamento de 20/09/2026, conferido um a um contra a página de checkout
(título e preço batendo).

## Pendências conhecidas

- O formulário de captura **precisa de uma ativação única**: o primeiro envio
  real dispara um e-mail do FormSubmit para `facilitadores@garagecriativa.com.br`
  com um link de confirmação. Enquanto ninguém clicar nesse link, os cadastros
  seguintes não são entregues.
- Sem `og:image`. Falta uma imagem social 1200×630.
- As capas dos ebooks trazem a etiqueta "GUIA", vocabulário da Garage Labs.
  Na torre Garage Music o termo é "ebook" — as capas precisam ser refeitas
  para casar com o texto do site.
- Os dois artigos na fila (`Setup` e `Precision`) ainda não têm corpo.

## DNS (GoDaddy)

| Tipo | Nome | Valor |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | spmarcoantoniosp.github.io |
