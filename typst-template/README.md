# NEBLI · Template Typst (canônico)

Template imutável entre resumos. Para criar um novo resumo:

## 1. Setup

```bash
cd "NEBLI - criador de resumos"
mkdir -p typst-build figuras/[tema]
cp typst-template/nebli_v1.typ typst-build/nebli.typ
```

## 2. Estrutura de arquivos

Crie em `typst-build/`:

- `[tema].typ` — documento principal. Importa `nebli.typ` e chama as funções na ordem: `capa()` → `sumario()` → `#show: pagina-padrao` → conteúdo da Etapa 1 → `#include "etapa2.typ"` ... → `gabarito-page()` → `glossario()` → `resumindo-page()`.
- `etapa1.typ` ... `etapa5.typ` — fragmentos (escritos pelos subagentes).
- `glossario.typ`, `resumindo.typ` — gerados pelo compilador local.

## 3. Funções disponíveis em `nebli.typ`

| Função | Uso |
|--------|-----|
| `capa(titulo, subtitulo, meta)` | Capa NEBLI · UC1 com faixa navy |
| `sumario(estrutura)` | Página de sumário |
| `pagina-padrao(corpo)` | Aplicar via `#show: pagina-padrao` para todo o miolo |
| `etapa-header(titulo)` | Banner navy de cabeçalho de etapa |
| `parte-title(titulo, primeira: false)` | PARTE I/II/III com linha teal |
| `subtopico(titulo)` | Subtópico (1.1, 1.2…) em teal |
| `intro-box(conteudo)` | Caixa cinza de introdução |
| `atencao-box(titulo, conteudo)` | Caixa vermelha de pegadinha |
| `clinica-box(titulo, conteudo)` | Caixa azul de compreensão clínica |
| `sintese-box(numero, conteudo)` | Caixa teal-light de fechamento de subtópico |
| `mini-resumo(conteudo)` | Linha lateral teal no meio do parágrafo |
| `conclusao-box(conteudo)` | Caixa azul de conclusão integradora |
| `figura-nebli(caminho, legenda, largura: 80%)` | Figura centrada com legenda em itálico |
| `badge-consolidacao`, `badge-integracao`, `badge-aplicacao`, `badge-prioritario` | Badges coloridos para questões |
| `questao-mc(numero, badge, enunciado, alts)` | Questão MC. `alts` é tupla de (letra, conteudo) |
| `questao-ce(numero, badge, enunciado, itens)` | Questão C/E. `itens` é tupla de (rom, conteudo) |
| `discursiva(numero, enunciado, modelo, titulo-q: none)` | Questão discursiva com modelo de resposta |
| `prova-block(badge, enunciado, alts, gabarito-letra, justificativa)` | Questão de fundamentos |
| `neblicard(contexto, pergunta, resposta)` | Flashcard |
| `seta` | Seta teal entre eventos (` → `) |
| `cloze(t)` | Destaque amarelo de cloze |
| `gabarito-page(blocos)` | Gabarito consolidado em grid 5 colunas |
| `glossario(intro, termos)` | Glossário em duas colunas |
| `resumindo-page(secoes)` | Revisão final em duas colunas |

## 4. Compilação

```bash
cd typst-build
~/.local/bin/typst compile --root .. [tema].typ ../resumos-gerados/[tema]_[turma].pdf
```

O `--root ..` é necessário para acessar `figuras/` e outras pastas-irmãs.

## 5. Fontes

Default canônico: **DejaVu Sans** (títulos, headers, badges) + **DejaVu Serif** (corpo).

Essas são exatamente as fontes que aparecem nos PDFs HTML antigos do projeto. Os arquivos `.woff2` em `fonts/` do projeto se chamam Montserrat/Merriweather mas correspondem às variantes "Thin"/"Light 18pt" do Google Fonts — não às Regulares clássicas. O WeasyPrint do HTML antigo não conseguia carregá-las e silenciosamente caía em DejaVu, que é o look que ficou estabelecido como "o resumo NEBLI".

Compilação simples, sem `--font-path`:

```bash
typst compile --root .. [tema].typ ...
```

A pasta `typst-template/fonts/` com as Thin/Light continua existindo como referência histórica; se um dia conseguir as Regulares "de verdade", basta colocar as novas TTFs em `typst-template/fonts/` e adicionar `--font-path ../typst-template/fonts` ao comando.

## 6. Paleta canônica

Já definida em `nebli.typ`:

- `navy` `#1B2A4A` — títulos, capa
- `teal` `#2A7A6B` — subtítulos, bordas
- `teal-light` `#E8F5F1` — fundo síntese
- `gold` `#D4920A` — destaque atenção, banner Resumindo
- `red-alert` `#C0392B` — atenção, badge difícil
- `blue-clin` `#2874A6` — clínica, badge integração
- `blue-light` `#5DADE2` — badge consolidação
- `violet` `#7D3C98` — badge aplicação

NÃO redefinir cores entre resumos.
