# garagemusic.org

Página "em breve" da Garage Music. Single-file autocontido (Space Grotesk
embutida em base64, sem dependências externas).

## Publicação

GitHub Pages serve a branch `main` a partir da raiz. Todo push republica.

```bash
git commit -am "Atualiza site" && git push
```

## Pendências conhecidas

- O formulário de captura **não envia o e-mail para lugar nenhum**: o script
  apenas exibe a mensagem de sucesso. Precisa de um endpoint antes de
  divulgar a página.
- Sem meta tags sociais (og:image etc.).
- `GM_Landing_Page.html` (site completo) está pronto na pasta de origem e
  pode substituir esta página quando for a hora.

## DNS (GoDaddy)

| Tipo  | Nome | Valor             |
|-------|------|-------------------|
| A     | @    | 185.199.108.153   |
| A     | @    | 185.199.109.153   |
| A     | @    | 185.199.110.153   |
| A     | @    | 185.199.111.153   |
| CNAME | www  | spmarcoantoniosp.github.io |
