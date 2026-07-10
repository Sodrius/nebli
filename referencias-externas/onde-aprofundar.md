# onde-aprofundar.md — mapa slug → plataformas (AnKing v12 · UWorld · B&B · Sketchy · Pathoma)

> **Status:** CANÔNICO v1 (2026-06-30). Plugado no pipeline: `CLAUDE.md` § References + Ordem do PDF (capa) + `ROLES.md` § Orquestrador Seção A.
> **Papel:** ao contrário do `blueprint-step1.md` (calibração invisível), **este arquivo VAI pro PDF** — alimenta o bloco "Onde aprofundar" da capa de cada resumo. É a **exceção escopada** à regra de banimento de vocabulário Step 1: os nomes das plataformas só aparecem neste bloco; o resto do PDF segue limpo.
> **Quem preenche:** a sessão principal (Orquestrador), best-effort, na geração de cada resumo. Davi só manda o tema.

## Como usar

1. Ao gerar um resumo, procure a entrada do `slug`. Se existir, copie a lista de itens pro campo `Onde aprofundar` do Tema Card (`meta`). Se não existir, redija best-effort e **grave a nova entrada aqui**.
2. Cada item é **conteúdo Typst cru** — `*negrito*` permitido (o `gerar_main.py` o emite dentro de um bloco com bullet navy). Não usar `#`, `[`, `]` crus.
3. **Honestidade por plataforma:** se uma plataforma não cobre o tema (ex.: Pathoma em bioquímica básica), escreva `— não cobre este tema`. Referência falsa é pior que ausência.
4. **AnKing = ação, não rótulo.** O item do AnKing diz a **tag exata pra dessuspender** no `Browse`, não "existe conteúdo". Esse é o uso pretendido do deck (unsuspend por tag).

## Fonte-verdade das tags v12 ✅ RESOLVIDO (2026-06-30)

Prefixo real: **`#AK_Step1_v12`**. Export em `flashcards/scripts/anking-v12-export.txt` (coluna 22 = tags). O AnKing **contém** B&B/Sketchy/Pathoma/FirstAid/Physeo/Bootcamp/UWorld como sub-decks (tags `#AK_Step1_v12::#B&B::…`, `::#SketchyBiochem::…`, etc.).

**Para qualquer tema:** `python flashcards/scripts/buscar_tags_anking.py <termo>` devolve as tags que casam, com contagem de cards, agrupadas por deck-recurso. É a fonte do grupo "Dessuspender no AnKing".

## Estrutura do bloco (2 grupos, canônico 2026-06-30)

Em vez de 1 bullet por plataforma (redundante, pois o AnKing as contém), o bloco "Onde aprofundar" tem **2 grupos**, cada item virando um bullet navy na capa:
1. **Assistir/ler** — 1 bullet só, fontes de vídeo/leitura para *aprender* o conteúdo (B&B/Bootcamp, NinjaNerd, Sketchy, UWorld QBank, Pathoma cap.). Recurso que não cobre → "não cobre".
2. **Dessuspender no AnKing v12** — 1 bullet de cabeçalho (`decks sob #AK_Step1_v12::`) + **1 bullet por deck**, mostrando o **caminho de tag** (pra navegar/buscar no `Browse`) com a contagem de cards. Esse é o pedido do Davi: ver o deck a dessuspender, não só o nome amigável, e com variedade de decks.

**Como preencher um slug novo:** rode `python flashcards/scripts/buscar_tags_anking.py <termo>` → ele agrupa por deck-recurso com contagens. Pegue os decks de maior rendimento para os bullets do grupo 2 (caminho com prefixo `#AK_Step1_v12::` removido na capa, recolocado nas "tags exatas" abaixo). Para o grupo 1, cite as mesmas fontes em modo "assistir".

---

## UC01 — Bioquímica

### bioq-glicogenio — Metabolismo do glicogênio

**Bloco da capa (vai pro `meta` — lista, cada item um bullet):**
- `*Assistir/ler* — B&B / Bootcamp (Glycogen) · NinjaNerd (Glycogenesis / -ólise / Regulação) · Sketchy Biochem (Glycogen) · UWorld (Biochem › Metabolism) · Pathoma: não cobre`
- `*Dessuspender no AnKing v12* — decks sob #AK_Step1_v12::`
- `#Bootcamp::Biochemistry::08_Glycogen — 148 cards`
- `#Physeo::05_Biochem::05_Metabolism::07_Glycogen — 93`
- `#SketchyBiochem::01_Metabolism::01_Carbohydrates → Glycogen — 90`
- `#FirstAid::01_Biochem::06_Metabolism::36_Glycogen (+37 storage diseases) — 75`
- `#B&B::04_Biochem::02_Metabolism::04_Glycogen — 63`

**Variedade completa (9 decks, ≈640 cards) — referência, nem tudo entra na capa:**
NinjaNerd 69 (`#NinjaNerd::01_Biochemistry::01_Physiology::13/14/15`) · Pixorize 63 (`#Pixorize::01_Biochemistry::…::23/24_Glyco…` + `07_Glycogen_Storage_Diseases`) · OME 38 (`#OME::PreClinical::Biochemistry::…::Glycogen_Storage_Diseases`). Mecanismo vs. doenças de depósito: o foco de 1º ano é o mecanismo (glicogênese/glicogenólise/regulação); as doenças de depósito (Von Gierke/Pompe/McArdle/Cori) são aprofundamento clínico.

---

## UC02 — Histologia

### histo-09-vasos-sanguineos-linfaticos — Histologia de vasos sanguíneos e linfáticos

**Bloco da capa (vai pro `meta` — lista, cada item um bullet):**
- `*Assistir/ler* — NinjaNerd (Histology: Blood Vessels) · Bootcamp (Anatomy/Histology › Vasculatura) · Pathoma cap. 6 (só a patologia: aterosclerose e vasculites) · Sketchy: não cobre histologia básica`
- `*Dessuspender no AnKing v12* — ordenados por completude no tema; dessuspenda de cima pra baixo:`
- `Cobre melhor · #FirstAid::07_Cardiovascular::02_Anatomy::*Blood_Vessels — 15 cards (as 3 túnicas, artéria × veia, tipos de capilar)`
- `Complementa · #FirstAid::07_Cardiovascular::03_Physiology::20_Capillary_fluid_exchange — 24 cards (troca capilar e edema)`
- `Mais distante · #Bootcamp::Cardiology::23_Stable_Angina_and_Atherosclerosis::02_Atherosclerosis — 30 cards (só o gancho clínico: endotélio → aterosclerose)`
- `Mais distante · #FirstAid::11_Musculoskeletal::*Vasculature::Varicose_Veins — 6 cards (só varizes)`

**Nota de honestidade:** o AnKing v12 é Step 1, logo cobre a *fisiologia/patologia* do vaso (troca capilar, aterosclerose que começa no endotélio, varizes), não a histologia descritiva pura (as 3 túnicas ao microscópio, tipos de capilar por órgão). Para a descrição histológica em si, a fonte real é o slide do professor + Junqueira/Ross (grupo "Onde estudar"). Os cards de aterosclerose entram porque o gancho de aprofundamento do tema é justamente "a aterosclerose nasce no endotélio disfuncional".

---

## UC02 — Anatomia

### anato-05-circulatorio-linfatico-I — Anatomia do sistema circulatório e linfático I

**Bloco da capa (vai pro `meta` — lista, cada item um bullet):**
- `*Assistir/ler* — Ninja Nerd (Heart Anatomy: chambers, valves, coronaries) · Boards & Beyond / Bootcamp (Cardiovascular › Anatomy) · Sketchy Anatomy (Thorax › Heart) · UWorld: pouca anatomia macro pura (só ganchos) · Pathoma: não cobre (é patologia)`
- `*Dessuspender no AnKing v12* (decks sob #AK_Step1_v12::) — ordenados por completude; dessuspenda de cima pra baixo:`
- `Cobre melhor · #SketchyAnatomy::02_Thorax::02_Heart::01_Chambers_of_Heart — 33 cards (câmaras, septos, circuito D/E)`
- `Cobre melhor · #OME::PreClinical::Cardiac::Cardiac_3::Anatomy_of_the_Heart_and_Mediastinum — 28 cards (coração + mediastino + pericárdio)`
- `Complementa · #FirstAid::07_Cardiovascular::02_Anatomy::01_Heart_anatomy — 23 cards (anatomia + irrigação coronária + pericárdio)`
- `Complementa · #SketchyAnatomy::02_Thorax::02_Heart::02_Coronary_Circulation — 23 cards (coronárias e seio coronário)`
- `Mais distante · #FirstAid::02_Immunology::01_Lymphoid_Structures::04_Spleen — 10 cards (baço, linfoide secundário)`
- `Mais distante · #FirstAid::02_Immunology::01_Lymphoid_Structures::05_Thymus — 4 cards (timo, linfoide primário)`

**Nota de honestidade:** o AnKing v12 é Step 1 e cobre bem a *anatomia macro do coração* (câmaras, valvas, coronárias, pericárdio, mediastino — Sketchy Anatomy, OME, First Aid Anatomy). A rede de vasos/microcirculação e o detalhe do sistema linfático (troncos, ductos, cisterna do quilo) aparecem só de raspão nos decks Step 1 — a fonte real desse detalhe é o slide da Profa. Katiúcia + Moore/Netter (grupo "Onde estudar"). Os decks de baço/timo entram como "mais distante" por serem o ângulo imunológico dos órgãos linfoides, não a anatomia macro.

<!-- Próximas entradas: ### <slug> — <título> + Bloco da capa (grupo 1 + grupo 2 com 1 bullet por deck) + Variedade completa. Rodar buscar_tags_anking.py <termo>. -->
