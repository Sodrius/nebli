# PLANO — deck-aula de alta qualidade (espacial-first + indistinguível + calibrado ao Davi)

> **Status:** proposta para aprovação (2026-07-13). Não executar até Davi liberar.
> **Norte:** o deck-aula existe pra **reter** o que a E1 ensinou, no nível que a FMUSP cobra e com base pro Step 1 — priorizando **visão espacial** em anatomia e histologia. Constrói sobre o que já é canônico: gate absoluto E1↔card, profundidade elevada (CANON 2026-07-12), card-mirror indistinguível, curadoria AnKing de 2 camadas.

## O que mudou a nosso favor (por que dá pra subir o teto agora)

Entraram 5 bancos-fonte em `Referências Externas` (ver `referencias-externas/DECKS-EXTERNOS-MAPA.md`):
- **BlueLink** — Image Occlusion de **fotos de cadáver reais** (busca só por tag de região).
- **LLU Histology** — **micrografias reais com cloze** ("This is a magnified image of {{c1::…}}").
- **Dope Anatomy** — IO de placas Netter, ricamente anotado.
- **Histology (AnKing-style)** — cloze denso, cobre vasos/linfático/tec. nervoso/sangue.
- **100 Concepts (Dorian)** — correlato clínico (gancho).

E o **canal de comentários** (add-on `nebli_comentarios` + campo `NEBLI_Comentario`) transforma o julgamento do Davi em sinal de curadoria card-a-card.

## Os 5 eixos de qualidade (o que passa a valer em todo deck-aula)

### Eixo 1 — Espacial-primeiro para anato/histo (o mais importante aqui)
Regra nova: **todo subtópico de anatomia ou histologia da E1 exige ≥1 card de IMAGEM REAL** no deck-aula — não só cloze de texto.
- Anatomia → Image Occlusion do **BlueLink** (peça real) e/ou **Dope** (Netter). BlueLink se puxa **por tag de região** (`BlueLink::<Região>`), nunca keyword.
- Histologia → cloze de micrografia do **LLU** e/ou imagem do **Histology**.
- Razão: prova prática e lâmina cobram **reconhecimento visual**, não definição. Card de texto sozinho não constrói o mapa espacial.
- Ordem pedagógica no deck: primeiro o esquema idealizado (Dope/Netter limpo) → depois a peça/lâmina real (BlueLink/LLU). Aprende no limpo, confirma no real.

### Eixo 2 — Profundidade no teto do AnKing (dentro do escopo do slide)
`profundidade = max(AnKing, slide/banco/bibliografia)` para cada mecanismo (CANON 2026-07-12). O cloze denso do deck **Histology** é a régua de "até onde ir" num mecanismo histológico. Foco no slide define O QUE entra; a fonte AnKing define ATÉ QUE PROFUNDIDADE. Aprofundamento entra sempre **ancorado na E1** (gate absoluto) — nada de card órfão.

### Eixo 3 — card-mirror obrigatório no lote
Todo NEBLIcard autoral (last-resort, quando nenhum banco cobre a lacuna tipo-a) roda no **card-mirror** (dossiê de 50 AnKings reais) até ficar indistinguível — inglês, Extra com imagem, IO visual, sem redundância (regra `regras-neblicard-anking-nivel`). Com mais decks reais agora, o discriminador tem mais material de treino.

### Eixo 4 — Canal de comentários como sinal de treino (o diferencial novo)
Os comentários do Davi card-a-card (`ler_comentarios.py`) viram **regra de curadoria acumulável**:
- "card RUIM" + porquê → padrão a evitar (ex.: "cloze apaga o rótulo, não o mecanismo") vira item de poda.
- "card BOM" + porquê → padrão a repetir.
- "aprofundar"/"reformular" → ação direta naquele card + regra pro futuro.
A qualidade sobe a cada aula porque a curadoria se calibra ao que **o Davi** valoriza, não a um padrão genérico. Padrões recorrentes viram entrada no `flashcards/CURADORIA-ANKING.md`.

### Eixo 5 — Gate E1↔card + revisor-completude mútua
A qualidade do deck fica presa à da E1: card só entra se o conceito está explicado na E1; e a E1 ganha 1-3 frases se um bom card exige (loop Card→E1). O **revisor-completude** (Sonnet) audita os dois sentidos e dá as 3 notas 0-10 (E1×slide, E2×E1, cards×E1) antes de fechar.

## Pipeline de curadoria por aula (upgrade do fluxo atual)

1. **Cobertura E1 → checklist de conceitos** (`gerar_checklist.py`), marcando quais são **espaciais** (anato/histo) — esses exigem card de imagem real (Eixo 1).
2. **Roteamento de fonte por conceito** (usar `DECKS-EXTERNOS-MAPA.md`): para cada conceito, decidir a fonte — BlueLink/Dope (anato), LLU/Histology (histo), AnKing (mecanismo/Step 1), Dorian (gancho clínico).
3. **Busca dirigida** (`buscar_tags_lote.py` no AnKing + busca por região/tecido nos decks externos) → pool → matriz conceito×card com coluna "In E1?" e coluna "espacial? tem imagem real?".
4. **Curadoria 2 camadas** (tag grossa PURA/IMPURA/RUÍDO → card fino keep/drop) — 30–50 cards muito bem curados por aula, precisão > recall.
5. **Lacuna tipo-a → NEBLIcard autoral** (só quando nenhum banco cobre) → **card-mirror** até indistinguível (Eixo 3).
6. **Revisor-completude mútua** (Eixo 5) → 3 notas + patches de E1 e add/drop de cards.
7. **Aplicar** (`aplicar_curadoria_anking.py`), reposicionar na ordem do cronograma, dessuspender no orçamento (15→50/dia).
8. **Loop de comentários** (Eixo 4): a cada rodada de revisão, `ler_comentarios.py --sync` → responder + destilar padrões → alimentar a curadoria da próxima aula.

## Métricas de fechamento (auditáveis, convite não gate)
- **Cobertura espacial:** % de subtópicos anato/histo com ≥1 card de imagem real. Meta: 100%.
- **cards×E1 (0-10):** todos os subtópicos da E1 cobertos? Meta ≥7.
- **Indistinguibilidade:** NEBLIcards autorais passaram no card-mirror? (sim/não por card).
- **Comentários resolvidos:** pendentes zerados antes de fechar a aula.

## O que fica de fora destes decks (lacunas conhecidas)
- **Embriologia** (gametogênese, gastrulação/neurulação) → AnKing `#Embryology` + material próprio.
- **P4 bioquímica/bio molecular** → AnKing; decks externos são anato/histo.

## Piloto sugerido (quando liberar)
**Tecido nervoso** ou **Histologia dos vasos** (P3, espaciais, cobertos por LLU+Histology+BlueLink). Roda o pipeline acima ponta a ponta, mede as 4 métricas, e serve de molde pros deck-aula seguintes.
