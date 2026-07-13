# DECKS-EXTERNOS-MAPA.md — bancos de anatomia/histologia importados pro Anki

> **Status:** referência viva (criado 2026-07-13). Onde vivem no Anki: pasta **`Referências Externas`** (irmã do `AnKing Step Deck`, que fica de fora por dependência de scripts).
> **Papel:** reservatório de cards prontos — sobretudo **Image Occlusion (IO)** de anatomia e **micrografias de histologia** — de onde o pipeline puxa card à altura pros **deck-aula** e **deck-prova**. Espelha o papel do AnKing na curadoria: fonte de onde se dessuspende/copia o que cobre a aula, nunca dump em massa.
> **Regra de crédito (herda `card-mirror-dossie-50-anking`):** proveniência = linha de crédito no card, não muda a autoria do julgamento de curadoria. Card puxado daqui entra no deck-aula pelo mesmo gate absoluto: **só se o conceito está explicado na E1 daquela aula**.

---

## 1. Os 5 decks — o que são e como se puxa deles

| Deck | Cards | Note type | Natureza | Como buscar | Força espacial |
|---|---|---|---|---|---|
| **Dope Anatomy** | 3186 | `Anatomy` (custom IO: `OccludedImage` + `1a..20a` + `Clinical/Origin/Insertion/Innervation/Actions/Plate`) | IO sobre **placas do Netter/Atlas**, ricamente anotado (origem, inserção, inervação, ação, correlato clínico por estrutura) | **por tag** `Dope::Anatomy::<Região>` **ou subdeck** | Ilustração idealizada — ótima pra aprender o esquema limpo |
| **University of Michigan – BlueLink Atlas** | 2992 | `Image Occlusion Enhanced+` (campos de texto **vazios**) | IO sobre **fotos de dissecção de cadáver REAIS** | **só por tag** `BlueLink::<Região>` — **keyword NÃO funciona** (texto vazio) | ★ Máxima: peça anatômica real, treina o olho pra prova prática/lâmina macro |
| **100 Concepts (Dorian)** | 303 | `Cloze` (228) + `Image Q/A` (16) | **Correlatos clínicos** de anatomia (Colles, kyphosis…), cloze curto + imagem no Extra | keyword **ou** tag `*Anatomy_Clinical_Correlates::Dorian_Original::<Região>` | Baixa (é clínica) — serve de **gancho** pro `#clinica-box` |
| **Histology** | 6023 | `Cloze-AnKingMaster-v3 (Histology)` (campos B&B/Pathoma/Sketchy/etc) | Histologia geral estilo AnKing, cloze + imagem no Extra | keyword **ou** tag `H::<Tecido>` (ConnectiveTissue, EpithelialTissue, Bone, Blood, Cartilage…) | Média-alta (imagem no Extra) |
| **LLU Histology** | 149 | `AnKingOverhaul (LLU Histology)` | **Micrografias reais com cloze** ("This is a magnified image of {{c1::elastic cartilage}}") | keyword | ★ Alta: reconhecimento de **lâmina real** ao microscópio |

**Note types novos que entraram no Anki** (relevantes pra fazer NEBLIcard indistinguível — ver `regras-neblicard-anking-nivel`): o `Anatomy` do Dope é um IO customizado com labels numerados `1a..20a`; o `Image Occlusion Enhanced+` do BlueLink é o IO clássico. Pra card autoral de anatomia, o padrão a imitar é o **BlueLink/IOE+** (foto real, máscara) e o **Histology/LLU** (micrografia + cloze curto).

---

## 2. Mapa deck → aulas NEBLI (cruzamento por assunto)

Contagem de cards que batem cada tema (busca por keyword; BlueLink por tag de região):

| Tema da P3/P4 | Dope | BlueLink | Dorian | Histology | LLU | **Fonte recomendada** |
|---|---:|---:|---:|---:|---:|---|
| **Coração** (Circulat. I/II) | 253 | tag Heart=107 | 6 | 414 | 9 | Dope (câmaras/valvas) + BlueLink Heart (peça real) |
| **Vasos — anatomia** (grandes vasos) | 859 | tag SupMediastinum=113 | 83 | 518 | 10 | Dope Thorax + BlueLink SuperiorMediastinum |
| **Vasos — histologia** (túnicas) | 98 | 0 | 1 | **1229** | 13 | **Histology** (túnica íntima/média/adventícia) |
| **Sistema linfático — anatomia** | 113 | tags Pelvic/Abdomen | 8 | 907 | 12 | Dope + Histology p/ ducto/vasos linf. |
| **Órgãos linfáticos** (baço/timo/linfonodo) | 133 | — | 14 | **356** | 28 | **Histology + LLU** (arquitetura de lâmina) |
| **Tecido nervoso** (neurônio/glia/mielina) | 138 | tag Brain=240 | 5 | **780** | 1 | **Histology** (tecido) + Dope Nervous (macro) |
| **Sangue** (eritro/leuco/plaqueta) | 0 | 0 | 0 | **963** | 0 | **Histology** (esfregaço) |

**Leitura da tabela:**
- **Anatomia macro (Circulatório/Linfático)** → Dope (esquema) + BlueLink (peça real). Os dois se complementam: aprende no Dope limpo, confirma no BlueLink cadáver.
- **Histologia (vasos, órgãos linfáticos, tecido nervoso, sangue)** → **Histology** é o cavalo de batalha (cobre tudo), **LLU** entra pra reconhecimento de lâmina real (poucos mas visuais).
- **Embriologia (gametogênese, gastrulação/neurulação)** → **NENHUM dos 5 cobre.** Continua dependendo do AnKing Step Deck (tag embryology) + fonte própria.
- **P4 (DNA reparo, metab. aminoácidos/lipídeos)** → fora do escopo destes decks (são anatomia/histo). AnKing.

---

## 3. Como usar no pipeline (deck-aula e deck-prova)

1. **Curadoria por aula** (fluxo `CURADORIA-ANKING.md`): além do AnKing, buscar em `Referências Externas` a região/tecido da aula. Ex.: aula "Histologia dos vasos" → `deck:"Referências Externas::Histology" tunica` + `deck:"...LLU Histology" vessel`.
2. **Preferência espacial (anato/histo):** priorizar **IO real** (BlueLink) e **micrografia real** (LLU) sobre ilustração, porque prova prática e lâmina cobram reconhecimento do real. Dope entra pra fixar o esquema idealizado primeiro.
3. **Gate absoluto mantido:** card só vai pro deck-aula se o conceito está na E1 daquela aula. Estes decks **elevam o teto de profundidade** disponível, não relaxam o gate.
4. **Crédito:** card puxado ganha linha de proveniência (Dope/BlueLink/LLU/Histology); não vira card "NEBLI-autoral".
5. **BlueLink só por tag** — lembrar sempre; keyword retorna 0.

---

## 4. Lacunas (o que estes decks NÃO cobrem)

- **Embriologia** — zero. Fonte: AnKing `#Embryology` + material próprio.
- **Bioquímica/Bio molecular (P4)** — zero (decks são anatomia/histo).
- **Fisiologia** — Dorian toca clínica, mas mecanismo fisiológico não é o forte; AnKing/B&B seguem sendo a régua.
