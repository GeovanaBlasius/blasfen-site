# Site Blasfen — Planejamento, padrões e checklist

Atualizado em 02/10/2026. Este arquivo documenta como o site foi estruturado e o que ainda falta.
A pasta `docs/` não vai para a hospedagem.

---

## 1. Planejamento e arquitetura de informação

### 1.1 Objetivo e público

- **Quem visita:** comprador, gerente de manutenção ou dono de indústria (alimentícia, florestal, agrícola, metalúrgica) do Alto Vale do Itajaí e de SC.
- **Ação desejada:** pedir uma recomendação técnica, pelo WhatsApp (principal) ou pelo formulário.
- **O site não vende on-line.** Toda jornada termina em contato com a equipe.

### 1.2 Jornadas mapeadas

| Perfil | Entrada | Caminho | Conversão |
|---|---|---|---|
| Sabe o que precisa ("óleo de corte solúvel") | Google → página da linha | Linha → produtos da linha → FAQ | WhatsApp com mensagem já citando a linha |
| Tem um problema, não sabe o produto | Página inicial | Abertura → Linhas de produto → banner "Não sabe qual lubrificante usar?" | Formulário de contato → página de Obrigado |
| Quer conferir a empresa antes de comprar | Indicação / Instagram | Início → A Blasfen → Marcas | Telefone ou WhatsApp no topo |
| Pesquisa técnica | Google → artigo do blog | Artigo → linha relacionada | WhatsApp com mensagem "li um artigo" |

O que foi implementado para encurtar essas jornadas:

- WhatsApp visível em todas as páginas: barra superior, botão do cabeçalho, botão flutuante e chamada no fim de cada página.
- Mensagem pronta no WhatsApp conforme a página (ex.: "quero uma recomendação para a linha Florestal"). O atendente já sabe o assunto.
- Formulário curto (6 campos), com segmento em lista e consentimento LGPD, que leva para uma página de **Obrigado**. Isso permite medir a conversão.
- No máximo 2 cliques da página inicial até qualquer linha de produto.

### 1.3 Mapa do site

```
Início  /
├── A Blasfen  /sobre
├── Produtos  /produtos/
│   ├── Desengraxantes  /produtos/desengraxantes
│   ├── Metalworking  /produtos/metalworking
│   ├── Graxas e Lubrificantes Especiais  /produtos/graxas-lubrificantes-especiais
│   ├── Pastas de Montagem  /produtos/pastas-de-montagem
│   ├── Indústria de Plásticos  /produtos/industria-plasticos
│   ├── Florestal  /produtos/florestal
│   └── Eco Spray Desengripante  /produtos/eco-spray-desengripante
├── Blog Técnico  /blog/
│   ├── Óleo de corte integral ou solúvel  /blog/oleo-corte-integral-vs-soluvel
│   └── NSF-H1 na indústria alimentícia  /blog/nsf-h1-industria-alimenticia
├── Contato  /contato
│   └── Obrigado (não indexada)  /obrigado
├── Política de Privacidade  /politica-de-privacidade
├── Termos de Uso  /termos-de-uso
└── 404 (não indexada)
```

### 1.4 Wireframes (celular primeiro)

Página inicial, celular (390 px):

```
┌──────────────────────────┐
│ ☎ (47) 3300  ◯ 9199-4462 │  barra superior
├──────────────────────────┤
│ [LOGO]        (☾) [≡]    │  cabeçalho fixo
├──────────────────────────┤
│ (• Distribuidor autoriz.)│
│ TÍTULO GRANDE            │  abertura
│ texto de apoio           │
│ [ Ver linhas ]           │
│ [ Falar c/ consultor ]   │
│ ┌──────────────────────┐ │
│ │ foto + selo NSF-H1   │ │
│ └──────────────────────┘ │
│           (v)            │
├──────────────────────────┤
│ [ foto ]                 │  quem somos
│ título + texto           │
│ (●) diferencial ×3       │
├──────────────────────────┤
│ ┌ card linha ──────────┐ │  linhas (1 por linha)
│ │ foto (●) nome, tags  │ │  ×7
│ └──────────────────────┘ │
│ (segmentos em pílulas)   │
├──────────────────────────┤
│ marcas ×3 (faixa clara)  │
├──────────────────────────┤
│ banner consultoria + CTA │
├──────────────────────────┤
│ perguntas (sanfona) ×5   │
├──────────────────────────┤
│ faixa laranja + CTA      │
├──────────────────────────┤
│ rodapé (1 coluna)        │
└──────────────────────────┘
```

Computador (1200 px): abertura em 2 colunas (texto | foto); quem somos em 2 colunas (foto | texto); linhas em grade de 3 colunas, com a 7ª em destaque horizontal; perguntas em 2 colunas (título | sanfona); rodapé em 4 colunas.

Página de linha de produto:

```
[trilha: Início / Produtos / Linha]
[foto larga]
ícone · NOME DA LINHA · descrição · segmentos
[ produtos da linha em cards ]
[ perguntas frequentes ]
[ faixa: falar com consultor técnico → WhatsApp com a linha ]
```

---

## 2. Design system

Tudo está em `css/style.css`, como variáveis no início do arquivo.

### Cores

| Token | Escuro | Claro | Uso |
|---|---|---|---|
| `--bg` | `#15171A` | `#F6F5F2` | fundo da página |
| `--bg-2` | `#1D2023` | `#FFFFFF` | blocos e cards |
| `--line` | `#2C3034` | `#E3E1DC` | divisórias |
| `--text` | `#EEECE8` | `#16191C` | texto principal |
| `--muted` | `#A3AAAF` | `#4F575D` | texto secundário |
| `--accent` | `#EF7418` | `#E06A10` | botões e ícones (laranja do logo) |
| `--accent-text` | `#EF7418` | `#A84C08` | laranja usado em **texto** (contraste AA) |

Contrastes medidos (WCAG AA exige 4,5:1 para texto normal): texto principal 15,2:1 no escuro e 16,2:1 no claro; texto secundário 7,6:1 e 6,8:1; laranja de texto 6,1:1 e 5,2:1; texto do botão laranja 6,5:1.

### Tipografia

- Fonte única: **Inter Tight** (Google Fonts), pesos 400, 500, 600 e 700.
- Títulos: H1 de 2,4 a 4,4 rem conforme a tela; H2 de 1,9 a 2,9 rem; H3 de 1,25 a 1,5 rem. Peso 600 e espaçamento levemente fechado.
- Texto: 17 px, entrelinha 1,6, até cerca de 64 caracteres por linha.

### Componentes padronizados

- **Botões:** `.btn--primary` (laranja, ação principal), `.btn--ghost` (contorno, ação secundária), `.btn--dark` (sobre a faixa laranja). Todos arredondados.
- **Cards de linha:** `.product-card` dentro de `.lines-grid`, com ícone em círculo laranja.
- **Pílulas:** `.tag` (características) e `.segment-list` (segmentos).
- **Seções:** espaçamento vertical de 104 px (64 px nas seções compactas). Margem lateral de 24 px no celular.
- **Raio dos cantos:** 4 px em campos, 10–18 px em cards, 22–24 px em fotos e banners, 999 px em botões e pílulas.

---

## 3. Checklist técnico

Legenda: ✅ feito no código · ⚙️ configurar na hospedagem · 👤 depende da Blasfen

### UI/UX e acessibilidade

- ✅ Layout responsivo, testado em 390 px e 1366 px, sem rolagem lateral.
- ✅ Contraste AA nos dois temas (ver tabela acima).
- ✅ Navegação por teclado: "Pular para o conteúdo" é o primeiro item do Tab e o foco aparece em links, botões e campos.
- ✅ Texto alternativo em todas as imagens. O formulário tem rótulos ligados aos campos e `autocomplete`.
- ✅ Respeita "reduzir movimento" do sistema operacional.
- ✅ Um H1 por página e títulos em ordem (H1 → H2 → H3).

### Performance (Core Web Vitals)

- ✅ Imagens em WebP, com `loading="lazy"` abaixo da dobra.
- ✅ Largura e altura declaradas em todas as imagens. CLS medido: **0**.
- ✅ Imagem principal com `preload` e `fetchpriority="high"` (LCP).
- ✅ JavaScript com `defer`; o script de tema é mínimo e evita o "piscar" do tema.
- ✅ Minificação de HTML, CSS e JS pelo `tools/build.py`.
- ✅ Cache de 1 ano para CSS, JS e imagens, com versão automática no link (`?v=`).
- 👤 Fotos reais em boa resolução (mínimo de 1600 px de largura para a abertura), exportadas em WebP.

### SEO on-page

- ✅ Título até 60 caracteres e descrição até 160 caracteres em todas as páginas.
- ✅ URLs amigáveis (`/produtos/metalworking`), com redirecionamento 301 das antigas `.html`.
- ✅ `canonical`, Open Graph e `sitemap.xml` com as URLs amigáveis.
- ✅ Dados estruturados: LocalBusiness, WebSite, FAQPage (início e linhas), Product, Article, BreadcrumbList.
- ⚙️ Cadastrar o site no **Google Search Console** e enviar `https://www.blasfenlubrificantes.com.br/sitemap.xml`.
- 👤 Criar ou atualizar o **Perfil da Empresa no Google** (Google Meu Negócio) com o mesmo endereço e telefone do site.

### Infraestrutura e segurança

- ✅ `.htaccess`: HTTPS obrigatório, domínio com www, compressão, cache, bloqueio de listagem de pastas e de arquivos internos.
- ✅ Cabeçalhos de segurança: HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy e Permissions-Policy.
- ✅ Site estático, sem banco de dados: não há superfície para injeção de SQL. A CSP limita scripts ao próprio domínio e ao Google Analytics (proteção contra XSS).
- ⚙️ Hospedagem com servidor no Brasil, compatível com `.htaccess` (Apache ou LiteSpeed) e com uptime garantido de 99,9% ou mais.
- ⚙️ Certificado SSL ativo (Let's Encrypt é gratuito na maioria das hospedagens).
- ⚙️ Backup automático diário da hospedagem e cópia do site no GitHub.
- ⚙️ Senhas: painel da hospedagem, domínio (Registro.br) e e-mail com senha forte e verificação em duas etapas.
- ⚙️ Confirmar o FormSubmit: o primeiro envio do formulário manda um e-mail de ativação para contato@blasfenlubrificantes.com.br.

### Analytics e LGPD

- ✅ Aviso de cookies com "Aceitar" e "Recusar". O Analytics só carrega depois do aceite, com IP anonimizado.
- ✅ "Preferências de cookies" no rodapé de todas as páginas, para mudar a escolha.
- ✅ Política de Privacidade atualizada (seção de cookies) e nova página de Termos de Uso.
- ✅ Consentimento obrigatório no formulário de contato.
- ✅ Eventos de conversão prontos: `contato_whatsapp`, `contato_telefone`, `contato_email`, `envio_formulario` e `generate_lead` (página de Obrigado).
- ⚙️ Criar a propriedade **GA4**, copiar o ID (`G-XXXXXXXXXX`) e colar em `js/main.js`, na linha `var BLASFEN_GA_ID = '';`. Depois, marcar `generate_lead` e `contato_whatsapp` como eventos-chave no GA4.
- 👤 Revisão jurídica rápida da Política de Privacidade e dos Termos de Uso.

---

## 4. Como publicar

1. Na pasta do site: `pip install minify-html rcssmin rjsmin` (só na primeira vez).
2. Rode `python tools/build.py`. Ele gera a pasta `dist/`.
3. Envie **o conteúdo** de `dist/` para a pasta raiz da hospedagem (`public_html`), incluindo o arquivo oculto `.htaccess`.
4. Abra o site, teste um link antigo `.html` (deve redirecionar), o formulário e o botão de WhatsApp.

Para visualizar no computador, abra os arquivos da pasta do projeto (não a `dist/`). A `dist/` usa caminhos de servidor e só funciona depois de publicada.
