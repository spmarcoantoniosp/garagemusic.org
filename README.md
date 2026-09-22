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

## Captura de e-mail

O destino do formulário da home mora no dict `CAPTURA`, no topo do `build.py`
— é o único lugar. As mensagens que o visitante lê saem de lá também, via
`data-*` no `<form>`; o `assets/site.js` só as lê.

| Campo | O que faz |
|---|---|
| `para` | Endereço que recebe. Hoje `music@garagecriativa.com.br` |
| `endpoint` | URL do formulário hospedado. **Vazio hoje** |
| `extra` | Campos que o serviço exigir junto do e-mail |
| `assunto` | Assunto do e-mail no modo carta |

**Com `endpoint` vazio** o site entra em *modo carta*: abre o programa de
e-mail do visitante com a mensagem pronta para `para`. Chega de verdade, mas
depende de o visitante apertar enviar — e não constrói lista com descadastro.

**Para ligar o envio automático**, cole a URL do formulário hospedado em
`endpoint` e rode `python3 build.py`. O site faz `POST` com o campo `email`;
o que o serviço pedir além disso entra em `extra` (ex.: `access_key` no
Web3Forms). Se o `POST` falhar, cai no modo carta sozinho.

Em nenhuma das duas rotas o formulário finge que enviou — essa era a falha
anterior.


## Pendências conhecidas

- O formulário de captura está em **modo carta** (abre o e-mail do visitante
  para `music@garagecriativa.com.br`). Funciona, mas perde quem não termina o
  envio e não gera lista com descadastro. Falta a URL do formulário hospedado
  em `CAPTURA["endpoint"]` — ver *Captura de e-mail* acima.
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
