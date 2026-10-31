"""
Build de produção do site Blasfen.

Gera a pasta dist/ pronta para subir na hospedagem:
  - HTML, CSS e JS minificados (sem espaços e comentários)
  - links internos trocados por URLs amigáveis (/produtos/metalworking)
  - caminhos de arquivos absolutos (/css/style.css), para a página 404 funcionar em qualquer endereço
  - CSS e JS com ?v=<hash>, para o cache de 1 ano do .htaccess não servir versão velha

Como usar (na pasta do site):
  pip install minify-html rcssmin rjsmin
  python tools/build.py

Depois envie o CONTEÚDO de dist/ (incluindo o arquivo oculto .htaccess) para a raiz da hospedagem.
"""
import hashlib, os, re, shutil, sys
from pathlib import Path

try:
    import minify_html, rcssmin, rjsmin
except ImportError:
    sys.exit('Instale as dependências: pip install minify-html rcssmin rjsmin')

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
COPY = ['images', 'videos', '.htaccess', 'robots.txt', 'sitemap.xml', 'site.webmanifest', 'llms.txt']
SKIP_DIRS = {'dist', 'tools', 'docs', 'lixo', '.vscode', '.git', 'blog'}  # blog retirado do site; lixo guarda o que saiu do site


def clean_url(rel_path: str) -> str:
    """'produtos/index.html' -> '/produtos/', 'sobre.html' -> '/sobre'."""
    rel_path = rel_path.replace('\\', '/')
    if rel_path == 'index.html':
        return '/'
    if rel_path.endswith('/index.html'):
        return '/' + rel_path[:-len('index.html')]
    if rel_path.endswith('.html'):
        return '/' + rel_path[:-5]
    return '/' + rel_path


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:10]


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    # CSS e JS minificados
    versions = {}
    for src in list(ROOT.glob('css/*.css')) + list(ROOT.glob('js/*.js')):
        rel = src.relative_to(ROOT).as_posix()
        text = src.read_text(encoding='utf-8')
        out = rcssmin.cssmin(text) if src.suffix == '.css' else rjsmin.jsmin(text)
        dest = DIST / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(out, encoding='utf-8')
        versions[rel] = file_hash(dest)

    # Arquivos copiados como estão
    for name in COPY:
        src = ROOT / name
        if src.is_dir():
            shutil.copytree(src, DIST / name)
        elif src.exists():
            shutil.copy2(src, DIST / name)

    # HTML: links amigáveis, caminhos absolutos, versão nos assets, minificação
    pages = [p for p in ROOT.rglob('*.html') if not (set(p.relative_to(ROOT).parts) & SKIP_DIRS)
             and not any(part.startswith('_') for part in p.relative_to(ROOT).parts)]  # ignora pastas de backup (_backup-...)
    for page in pages:
        rel_page = page.relative_to(ROOT).as_posix()
        page_dir = os.path.dirname(rel_page)
        html = page.read_text(encoding='utf-8')

        def fix(match):
            attr, url = match.group(1), match.group(2)
            if re.match(r'^(https?:|mailto:|tel:|#|data:|/)', url):
                return match.group(0)
            path, _, frag = url.partition('#')
            target = os.path.normpath(os.path.join(page_dir, path)).replace('\\', '/')
            if target.endswith('.html'):
                new = clean_url(target)
            else:
                new = '/' + target
                if target in versions:
                    new += '?v=' + versions[target]
            return f'{attr}="{new}{"#" + frag if frag else ""}"'

        html = re.sub(r'\b(href|src|poster)="([^"]+)"', fix, html)
        html = re.sub(r"url\('([^']+)'\)", lambda m: "url('" + ('/' + os.path.normpath(os.path.join(page_dir, m.group(1))).replace('\\', '/') if not m.group(1).startswith(('http', '/')) else m.group(1)) + "')", html)
        html = minify_html.minify(html, minify_css=True, minify_js=False, keep_closing_tags=True,
                                  keep_html_and_head_opening_tags=True)
        dest = DIST / rel_page
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding='utf-8')

    before = sum(f.stat().st_size for f in ROOT.rglob('*') if f.is_file() and f.suffix in ('.html', '.css', '.js') and not (set(f.relative_to(ROOT).parts) & SKIP_DIRS))
    after = sum(f.stat().st_size for f in DIST.rglob('*') if f.is_file() and f.suffix in ('.html', '.css', '.js'))
    print(f'dist/ gerado: {len(pages)} páginas. HTML+CSS+JS: {before/1024:.0f} KB -> {after/1024:.0f} KB')


if __name__ == '__main__':
    main()
