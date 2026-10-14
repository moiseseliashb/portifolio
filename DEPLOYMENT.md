# Alojamento na Vercel

1. Importa este repositório na Vercel, mantendo a raiz do projeto na raiz do
   repositório.
2. Em **Settings > Environment Variables**, define `SECRET_KEY` para os
   ambientes Production, Preview e Development. Usa um valor aleatório forte;
   não o guardes no Git.
3. Mantém `FLASK_DEBUG` ausente ou define-o como `0` em produção.
4. Faz o deploy. A Vercel usa `pyproject.toml` para localizar `run:app` e
   `requirements.txt` para instalar as dependências Python.

Os ficheiros servidos diretamente pela CDN da Vercel estão em
`public/static/`. Para alterar o CSS, edita `app/static/css/input.css` e corre
`npm ci` seguido de `npm run build:css`; o CSS gerado em `public/static/css/`
deve ser incluído no commit do deploy.
