# CHEATSHEET — Armadilhas Typst do NEBLI

**Leia ANTES do template canônico.** Esta página resolve 90% dos bugs que apareceram nos resumos #1 a #5 da Geração 20. Quem ignora aqui retrabalha lá.

## 1. Importar o template em CADA etapaN.typ

Errado (faltando import): `#set-etapa("Etapa 1")` direto no topo.
Certo: começar todo `.typ` com
```typst
#import "../typst-template/nebli_v2_apostila.typ": *
```
O `#include` do main.typ NÃO compartilha imports. Sem isso, todos os helpers falham com "unknown variable".

## 2. Equações químicas NUNCA em `$…$`

Errado: `$Ka = ([A⁻][H⁺]) / [HA]$` — Typst trata `Ka`, `HA` como variáveis indefinidas.
Certo:
```typst
#align(center, text(size: 11pt)[K#sub[a] = ([A⁻][H⁺]) / [HA]])
```
Use Unicode (₁ ₂ ⁻ ⁺ → ⇌) + `#sub[]` + `#super[]`. Math mode só para matemática real.

## 3. `<` e `>` em texto markup precisam de escape

Errado dentro de qualquer `[...]`: `(<34 semanas)`, `r₁ < r₂`, `ΔP₁ > ΔP₂`.
Certo: `(\<34 semanas)`, `r₁ \< r₂`, `ΔP₁ \> ΔP₂`.
Sem escape, o Typst lê `<...>` como label-open e quebra com "unclosed label".

## 4. Sintaxe Typst vs Markdown

Errado: `**negrito**` (markdown).
Certo: `*negrito*` (uma estrela só).
Markdown vazado gera warning "no text within stars" e perde a formatação.

## 5. Helper `#sigla` — formato string-content

Errado: `#sigla[ATP][adenosina trifosfato]` — quebra com 2+ siglas ("cannot compare content").
Certo:
```typst
#sigla("ATP", [adenosina trifosfato — moeda energética da célula])
```
Abreviação como string entre aspas, expansão como content entre colchetes.

## 6. Caminho de figura — sempre absoluto a partir do root

Errado: `image("figuras/glicose/slide-08.png")` — falha porque o `.typ` está em `typst-build/`.
Certo: `image("/figuras/glicose/slide-08.png")` — barra inicial = root do projeto Typst.
Vale para `#figura-nebli`, `#figura-lateral`, qualquer chamada de imagem.

## 7. `[X]_Y` após bracket escapado vira subscript

Errado: `\[Na⁺\]_LEC` — Typst interpreta `_LEC` como subscript dentro de markup.
Certo: `"concentração de Na⁺ no LEC"` em prosa, ou `[Na⁺]#sub[LEC]`.

## 8. Write/Edit em arquivo .typ grande TRUNCA silenciosamente

O Write pode (a) deixar NULL bytes no fim ou (b) cortar a última linha no meio de uma palavra.
**Antes de compilar, SEMPRE rodar:**
```bash
python3 typst-build/precompile-check.py
```
O check v2 (2026-05-15) pega NULL bytes E truncamento de última linha.

## 9. Limites do helper `#mapa-parte`

Grid de 5 colunas (nó/seta/nó/seta/nó) só comporta textos curtos:
- `centro` ≤12 palavras
- `no.titulo` ≤3 palavras (ex.: "Necessidade")
- `no.texto` ≤10–12 palavras (frase única curta)
- label da aresta ≤3–4 palavras (ex.: "demanda exige")
- `fecha-com` ≤18 palavras

Texto maior estoura: labels caem dentro dos nós, palavras truncam horizontalmente. **Reescreva o texto** — não aumente a figura, não reduza font, não force quebra em 2 linhas.

## 10. Fonte do corpo é "Merriweather", não "Merriweather Light 18pt"

O template canônico já está corrigido (2026-05-15). Mas se for editar `corpo-fam`, use:
```typst
#let corpo-fam = ("Merriweather",)
```
A versão "Light 18pt" só existe na variante Optical do Google Fonts; gerava warning persistente de fallback.

## 11. `#mapa-parte` exige 3 chaves no nó e tupla simples na aresta

Errado:
```typst
#mapa-parte(
  centro: "...",
  nos: ((titulo: "1.1", texto: [...]),),
  arestas: ((), ()),
)
```

Certo:
```typst
#mapa-parte(
  centro: "...",
  nos: ((id: "1.1", titulo: "Curto", texto: [...]),),
  arestas: (),
)
```

A função usa `no.id` no render e `arestas.at(i).at(2)` no label da aresta. Omitir `id` ou passar tupla "dummy" `()` dentro de `arestas` quebra com **`array index out of bounds`** apontando para uma linha distante — a mensagem é confusa porque o erro nasce no helper, não no chamador.

Regra dos três campos do nó: `id` (curto, ex. "1.1"), `titulo` (≤3 palavras), `texto` (content block, ≤10–12 palavras). Para mapa sem arestas, sempre `arestas: ()` (tupla vazia simples). Ver também a armadilha 9 (limites de tamanho do `#mapa-parte`).

---

**Resumo operacional:** import no topo, `*bold*` não `**bold**`, escapar `\<` e `\>`, equação química em `#align`, `#sigla("X", [Y])`, path absoluto `/figuras/...`, `#mapa-parte` curto e com nós `(id, titulo, texto)`, e SEMPRE `precompile-check.py` antes de `typst compile`.
