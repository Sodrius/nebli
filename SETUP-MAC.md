# NEBLI num computador novo (Mac) — passo a passo

Escrito em 26/09/2026, ao migrar do Windows para o Mac. O Git leva **código, regras e relatórios**. O Anki vem pelo **AnkiWeb**. O que é grande, pessoal ou com direitos autorais **não está no Git** (lista abaixo).

## 1. Instalar
- Git, Python 3.11+, GitHub CLI (`gh auth login`), Anki desktop (mesma versão principal do Windows).
- Anki → Ferramentas → Complementos → Obter: **AnkiConnect** (código `2055492159`). Reiniciar o Anki.

## 2. Baixar o projeto
```bash
git clone https://github.com/Sodrius/nebli.git
cd nebli
pip3 install -r requirements.txt
python3 -m unittest discover -s nebli/tests      # deve passar sem Anki aberto
```
O clone é grande (~400 MB de histórico). Depois, ler `CLAUDE.md` → `flashcards/projeto/README.md`.

## 3. Anki: coleção e add-on
1. No Anki do Mac, entre com a conta AnkiWeb e **sincronize** (baixar). Traz decks `NEBLI::…`, AnKing e Referências Externas. A primeira sincronização é longa (mídia). Não use "Substituir a coleção" do lado errado: **baixar** do AnkiWeb, nunca enviar do Mac vazio.
2. O perfil precisa se chamar **Davi** (os scripts conferem).
3. Copie o add-on que coloca o total de cards no nome dos decks:
   ```bash
   cp -R anki-addon/nebli_decks "$HOME/Library/Application Support/Anki2/addons21/"
   ```
   Reinicie o Anki. Sem ele, os nomes ficam canônicos (`NEBLI::UC03::…`), o que também funciona.
4. Confirme a ligação: com o Anki aberto, `python3 -m nebli.preflight --catalog --output /tmp/catalogo.json`.
5. **Escrita no Anki só pelo helper** (`from nebli.decks import Anki, escrita`), que usa o lock e espera os nomes voltarem ao canônico. Regras em `flashcards/projeto/OPERACAO-CODEX-CLAUDE.md`, seção "Mexer em decks".

## 4. Compilar uma E1
```bash
python3 typst-build/gerar_main.py <tema-card.yml> --somente-e1 --out typst-build/_par_<slug>/main.typ
python3 typst-build/precompile-check.py --somente-e1     # dentro da pasta _par_<slug>
python3 -c "import typst; typst.compile('main.typ', output='saida.pdf', root='../..', font_paths=['../../fonts'])"
```
As fontes (Merriweather, Montserrat) estão em `fonts/`. Sem `font_paths`, o PDF sai com fonte errada.

## 5. O que NÃO veio pelo Git (trazer à parte se precisar)
| Item | Onde está | Para que serve |
|---|---|---|
| `figuras/**/*.png` (~3 GB) e PDFs de slides | só no PC Windows | recompilar E1 antigas; não é preciso para decks novos |
| `arquivos-trabalho/livros/` (Robbins, Trabulsi…) | Drive de Davi, pasta Livros `1ZYH9ezNk8lH4h0ArsX2PgdOpsnf4N-ss` | consulta de capítulo; o Robbins (501 MB) não abre pelo conector, baixar pelo navegador |
| Dados das corridas (`arquivos-trabalho/**/*.json`, `.txt`, `.apkg`, PDFs de E1) | só no PC Windows | snapshots, planos, backups de deck (ex.: backup do deck de Edema antes/depois do piloto). Só copie se quiser auditar; **nunca** restaure card apagado a partir deles |
| `config/publicacoes-uc.json` | local; modelo em `config/publicacoes-uc.example.json` | upload de APKG está pausado |
| Memória automática do Claude Code | local a cada máquina | não migra; o que importa está em `flashcards/projeto/FEEDBACKS.md`, `README.md` e `MEMORY.md` |
| Conectores (Drive, Gmail…) | conta claude.ai | reconectar no Claude Code do Mac |
| Tesseract (`flashcards/scripts/io_from_slide.py` aponta `C:\Program Files\…`) | instalar com `brew install tesseract` e ajustar o caminho | só OCR de slides |

## 6. Repositório público
O repositório `Sodrius/nebli` é **público**. Por isso o `.gitignore` deixa fora conteúdo de cards do AnKing, texto de slides, livros, pacotes `.apkg` e estado pessoal. Antes de qualquer push novo, conferir `git status` e não forçar (`git add -f`) arquivo ignorado.

## 7. Estado do trabalho (26/09/2026)
Ver `MEMORY.md` (estado), `flashcards/projeto/FILA-UC03-P2-UC08-P1.md` (aulas) e `arquivos-trabalho/deck-aula-edema-congestao-2026-09-25/LACUNAS-PROPOSTAS.md` (decisão pendente sobre o deck de Edema).
