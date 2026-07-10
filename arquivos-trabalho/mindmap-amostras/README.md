# Amostras de mindmap — Glicólise

**Função:** comparar 3 engines de renderização de mindmap para o fechamento da Etapa 1.

**Critério canonizado em 2026-05-22:** 1 mindmap por resumo, ao final da E1, modo "revisão visual rápida" — o aluno deve conseguir, olhando só o mapa, identificar todos os pontos vistos na E1.

**Tema-piloto:** Glicólise. Estrutura compartilhada nos 3 arquivos:
- Centro: "Glicólise — converter glicose em piruvato + 2 ATP + 2 NADH"
- 3 ramos primários (espelhando PARTES da E1):
  - PARTE I — Fase preparatória (consome 2 ATP)
  - PARTE II — Fase de geração (rende 4 ATP + 2 NADH)
  - PARTE III — Regulação e destinos
- Sub-ramos com enzimas-chave, regulação, produtos.

---

## Como escolher

Davi olha os 3 arquivos source, **idealmente renderiza pelo menos 1**, e decide:
- Qual visual encaixa melhor na "estética apostila NEBLI"?
- Qual densidade de informação cabe confortavelmente em ~⅓ de página?
- Qual é menos trabalho de autoria/manutenção?

## Arquivos

| Arquivo | Engine | Render |
|---|---|---|
| `amostra-1-mermaid.mmd` | Mermaid mindmap (radial) | `npx @mermaid-js/mermaid-cli -i amostra-1-mermaid.mmd -o amostra-1.svg` |
| `amostra-2-graphviz.dot` | Graphviz twopi (radial nó-aresta) | `dot -Ktwopi -Tsvg amostra-2-graphviz.dot -o amostra-2.svg` (ou `dot -Kneato`) |
| `amostra-3-typst-blocks.typ` | Typst nativo (blocos hierárquicos, sem lib externa) | `typst compile amostra-3-typst-blocks.typ amostra-3.pdf` |

## Comparação resumida

| Critério | Mermaid | Graphviz | Typst-blocks |
|---|---|---|---|
| Visual | Radial limpo, cores tema, "moderno apostila" | Radial técnico, controle preciso de arestas | Hierárquico em blocos coloridos, sem arestas |
| Dependência externa | mermaid-cli (Node + npm) | graphviz (binary, mais leve) | nenhuma — Typst puro |
| Autoria | DSL simples, indentação = hierarquia | DSL mais verboso, controle de attrs | sintaxe Typst direta, helper customizável |
| Paleta NEBLI | precisa CSS theme injetado | configurável via attrs nativos | nativo (helpers já usam navy/teal/gold) |
| Quebra/scaling em PDF | SVG embutido, escala bem | SVG embutido, escala bem | nativo Typst, integra perfeito ao layout |
| Risco de bug | mermaid-cli falha silencioso em label longo | "labels truncados" reportado no `#mapa-parte` antigo | bug = bug visual conhecido, fácil debugar |

**Palpite de partida:** Typst-blocks ganha em integração (sem dep externa, paleta nativa, controle visual fino). Mermaid ganha em rapidez de autoria. Graphviz fica pra quando precisar de relação enzimática complexa com setas (não é esse caso aqui).

Davi decide.
