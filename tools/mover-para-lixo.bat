@echo off
chcp 65001 >nul
REM Move para a pasta lixo tudo o que saiu do site Blasfen em 30/10/2026.
REM Nada é apagado: os arquivos só mudam de lugar. Pode rodar mais de uma vez sem problema.
cd /d "%~dp0.."
echo Pasta do site: %CD%
if not exist "index.html" ( echo ERRO: rode este arquivo de dentro da pasta tools do site. & pause & exit /b 1 )
if not exist "lixo\produtos-retirados" mkdir "lixo\produtos-retirados"
if not exist "lixo\images-sem-uso" mkdir "lixo\images-sem-uso"

REM 1) Blog técnico (retirado do site)
if exist "blog" ( move "blog" "lixo\blog-retirado-2026-10-30" >nul && echo [ok] blog )

REM 2) Linhas que saíram do catálogo (os endereços antigos já redirecionam para /produtos/)
if exist "produtos\eco-spray-desengripante.html" ( move "produtos\eco-spray-desengripante.html" "lixo\produtos-retirados\" >nul && echo [ok] eco-spray-desengripante.html )
if exist "produtos\florestal.html" ( move "produtos\florestal.html" "lixo\produtos-retirados\" >nul && echo [ok] florestal.html )

REM 3) Imagens que nenhuma página usa (originais e fotos substituídas)
if exist "images\958fd54362b2403d9fa2a912851ef3d1.webp" ( move "images\958fd54362b2403d9fa2a912851ef3d1.webp" "lixo\images-sem-uso\" >nul && echo [ok] 958fd54362b2403d9fa2a912851ef3d1.webp )
if exist "images\favicon.png" ( move "images\favicon.png" "lixo\images-sem-uso\" >nul && echo [ok] favicon.png )
if exist "images\nevoa-oleo-usinagem.webp" ( move "images\nevoa-oleo-usinagem.webp" "lixo\images-sem-uso\" >nul && echo [ok] nevoa-oleo-usinagem.webp )
if exist "images\industria-alimenticia-padaria.webp" ( move "images\industria-alimenticia-padaria.webp" "lixo\images-sem-uso\" >nul && echo [ok] industria-alimenticia-padaria.webp )
if exist "images\pexels-nc-farm-bureau-mark-2889193.jpg" ( move "images\pexels-nc-farm-bureau-mark-2889193.jpg" "lixo\images-sem-uso\" >nul && echo [ok] pexels-nc-farm-bureau-mark-2889193.jpg )
if exist "images\pexels-shvetsa-6291408.jpg" ( move "images\pexels-shvetsa-6291408.jpg" "lixo\images-sem-uso\" >nul && echo [ok] pexels-shvetsa-6291408.jpg )
if exist "images\plastico.jpg" ( move "images\plastico.jpg" "lixo\images-sem-uso\" >nul && echo [ok] plastico.jpg )
if exist "images\industria-alimenticia-biscoitos.png" ( move "images\industria-alimenticia-biscoitos.png" "lixo\images-sem-uso\" >nul && echo [ok] industria-alimenticia-biscoitos.png )
if exist "images\industria-alimenticia-frango.png" ( move "images\industria-alimenticia-frango.png" "lixo\images-sem-uso\" >nul && echo [ok] industria-alimenticia-frango.png )
if exist "images\pasta-antigripante-parafuso.png" ( move "images\pasta-antigripante-parafuso.png" "lixo\images-sem-uso\" >nul && echo [ok] pasta-antigripante-parafuso.png )

REM 4) Versão antiga gerada em 02/10 (tinha o blog e o Eco Spray). Gere de novo com: python tools\build.py
if exist "dist" ( move "dist" "lixo\dist-antigo-2026-10-02" >nul && echo [ok] dist antigo )

REM 5) Organização: a lista de pendências vai para docs
if exist "Itens faltantes pro site" ( move "Itens faltantes pro site" "docs\itens-faltantes-pro-site.txt" >nul && echo [ok] Itens faltantes para docs )

echo.
echo Pronto. Confira a pasta lixo.
pause
