# DECKS-EXTERNOS-MAPA.md â€” bancos de anatomia/histologia importados pro Anki

> **Status:** referÃªncia viva (criado 2026-07-13). Onde vivem no Anki: pasta **`ReferÃªncias Externas`** (irmÃ£ do `AnKing Step Deck`, que fica de fora por dependÃªncia de scripts).
> **Papel:** reservatÃ³rio de cards prontos â€” sobretudo **Image Occlusion (IO)** de anatomia e **micrografias de histologia** â€” de onde o pipeline puxa card Ã  altura pros **deck-aula** e **deck-prova**. Espelha o papel do AnKing na curadoria: fonte de onde se dessuspende/copia o que cobre a aula, nunca dump em massa.
> **Regra de crÃ©dito (herda `card-mirror-dossie-50-anking`):** proveniÃªncia = linha de crÃ©dito no card, nÃ£o muda a autoria do julgamento de curadoria. Card puxado daqui entra no deck-aula pelo mesmo gate absoluto: **sÃ³ se o conceito estÃ¡ explicado na E1 daquela aula**.
> **Guia operacional aprofundado:** `referencias-externas/GUIA-CARDS-EXTERNOS-PARA-DECK-AULA.md` define quando usar BlueLink, Dope, Dorian, Histology e LLU antes de criar NEBLIcard autoral.

---

## 1. Os 5 decks â€” o que sÃ£o e como se puxa deles

| Deck | Cards | Note type | Natureza | Como buscar | ForÃ§a espacial |
|---|---|---|---|---|---|
| **Dope Anatomy** | 3186 | `Anatomy` (custom IO: `OccludedImage` + `1a..20a` + `Clinical/Origin/Insertion/Innervation/Actions/Plate`) | IO sobre **placas do Netter/Atlas**, ricamente anotado (origem, inserÃ§Ã£o, inervaÃ§Ã£o, aÃ§Ã£o, correlato clÃ­nico por estrutura) | **por tag** `Dope::Anatomy::<RegiÃ£o>` **ou subdeck** | IlustraÃ§Ã£o idealizada â€” Ã³tima pra aprender o esquema limpo |
| **University of Michigan â€“ BlueLink Atlas** | 2992 | `Image Occlusion Enhanced+` (campos de texto **vazios**) | IO sobre **fotos de dissecÃ§Ã£o de cadÃ¡ver REAIS** | **sÃ³ por tag** `BlueLink::<RegiÃ£o>` â€” **keyword NÃƒO funciona** (texto vazio) | â˜… MÃ¡xima: peÃ§a anatÃ´mica real, treina o olho pra prova prÃ¡tica/lÃ¢mina macro |
| **100 Concepts (Dorian)** | 303 | `Cloze` (228) + `Image Q/A` (16) | **Correlatos clÃ­nicos** de anatomia (Colles, kyphosisâ€¦), cloze curto + imagem no Extra | keyword **ou** tag `*Anatomy_Clinical_Correlates::Dorian_Original::<RegiÃ£o>` | Baixa (Ã© clÃ­nica) â€” serve de **gancho** pro `#clinica-box` |
| **Histology** | 6023 | `Cloze-AnKingMaster-v3 (Histology)` (campos B&B/Pathoma/Sketchy/etc) | Histologia geral estilo AnKing, cloze + imagem no Extra | keyword **ou** tag `H::<Tecido>` (ConnectiveTissue, EpithelialTissue, Bone, Blood, Cartilageâ€¦) | MÃ©dia-alta (imagem no Extra) |
| **LLU Histology** | 149 | `AnKingOverhaul (LLU Histology)` | **Micrografias reais com cloze** ("This is a magnified image of {{c1::elastic cartilage}}") | keyword | â˜… Alta: reconhecimento de **lÃ¢mina real** ao microscÃ³pio |

**Note types novos que entraram no Anki** (relevantes pra fazer NEBLIcard indistinguÃ­vel â€” ver `regras-neblicard-anking-nivel`): o `Anatomy` do Dope Ã© um IO customizado com labels numerados `1a..20a`; o `Image Occlusion Enhanced+` do BlueLink Ã© o IO clÃ¡ssico. Pra card autoral de anatomia, o padrÃ£o a imitar Ã© o **BlueLink/IOE+** (foto real, mÃ¡scara) e o **Histology/LLU** (micrografia + cloze curto).

---

## 2. Mapa deck â†’ aulas NEBLI (cruzamento por assunto)

Contagem de cards que batem cada tema (busca por keyword; BlueLink por tag de regiÃ£o):

| Tema da P3/P4 | Dope | BlueLink | Dorian | Histology | LLU | **Fonte recomendada** |
|---|---:|---:|---:|---:|---:|---|
| **CoraÃ§Ã£o** (Circulat. I/II) | 253 | tag Heart=107 | 6 | 414 | 9 | Dope (cÃ¢maras/valvas) + BlueLink Heart (peÃ§a real) |
| **Vasos â€” anatomia** (grandes vasos) | 859 | tag SupMediastinum=113 | 83 | 518 | 10 | Dope Thorax + BlueLink SuperiorMediastinum |
| **Vasos â€” histologia** (tÃºnicas) | 98 | 0 | 1 | **1229** | 13 | **Histology** (tÃºnica Ã­ntima/mÃ©dia/adventÃ­cia) |
| **Sistema linfÃ¡tico â€” anatomia** | 113 | tags Pelvic/Abdomen | 8 | 907 | 12 | Dope + Histology p/ ducto/vasos linf. |
| **Ã“rgÃ£os linfÃ¡ticos** (baÃ§o/timo/linfonodo) | 133 | â€” | 14 | **356** | 28 | **Histology + LLU** (arquitetura de lÃ¢mina) |
| **Tecido nervoso** (neurÃ´nio/glia/mielina) | 138 | tag Brain=240 | 5 | **780** | 1 | **Histology** (tecido) + Dope Nervous (macro) |
| **Sangue** (eritro/leuco/plaqueta) | 0 | 0 | 0 | **963** | 0 | **Histology** (esfregaÃ§o) |

**Leitura da tabela:**
- **Anatomia macro (CirculatÃ³rio/LinfÃ¡tico)** â†’ Dope (esquema) + BlueLink (peÃ§a real). Os dois se complementam: aprende no Dope limpo, confirma no BlueLink cadÃ¡ver.
- **Histologia (vasos, Ã³rgÃ£os linfÃ¡ticos, tecido nervoso, sangue)** â†’ **Histology** Ã© o cavalo de batalha (cobre tudo), **LLU** entra pra reconhecimento de lÃ¢mina real (poucos mas visuais).
- **Embriologia (gametogÃªnese, gastrulaÃ§Ã£o/neurulaÃ§Ã£o)** â†’ **NENHUM dos 5 cobre.** Continua dependendo do AnKing Step Deck (tag embryology) + fonte prÃ³pria.
- **P4 (DNA reparo, metab. aminoÃ¡cidos/lipÃ­deos)** â†’ fora do escopo destes decks (sÃ£o anatomia/histo). AnKing.

---

## 3. Como usar no pipeline (deck-aula e deck-prova)

1. **Curadoria por aula** (fluxo `CURADORIA-ANKING.md`): alÃ©m do AnKing, buscar em `ReferÃªncias Externas` a regiÃ£o/tecido da aula. Ex.: aula "Histologia dos vasos" â†’ `deck:"ReferÃªncias Externas::Histology" tunica` + `deck:"...LLU Histology" vessel`.
2. **PreferÃªncia espacial (anato/histo):** priorizar **IO real** (BlueLink) e **micrografia real** (LLU) sobre ilustraÃ§Ã£o, porque prova prÃ¡tica e lÃ¢mina cobram reconhecimento do real. Dope entra pra fixar o esquema idealizado primeiro.
3. **Gate absoluto mantido:** card sÃ³ vai pro deck-aula se o conceito estÃ¡ na E1 daquela aula. Estes decks **elevam o teto de profundidade** disponÃ­vel, nÃ£o relaxam o gate.
4. **CrÃ©dito:** card puxado ganha linha de proveniÃªncia (Dope/BlueLink/LLU/Histology); nÃ£o vira card "NEBLI-autoral".
5. **BlueLink sÃ³ por tag** â€” lembrar sempre; keyword retorna 0.

### Comando operacional (copia sem tocar no original)

Use `flashcards/scripts/copiar_externos_para_deck.py` para duplicar cards externos aprovados para a Ã¡rvore `NEBLI::`, preservando note type, campos, imagens e tags de origem. O original em `ReferÃªncias Externas` fica intocado.

Exemplo BlueLink/cadÃ¡ver para coraÃ§Ã£o:

```bash
python flashcards/scripts/copiar_externos_para_deck.py ^
  --source BlueLink ^
  --tag "BlueLink::Heart" ^
  --deck "NEBLI::UC02::P3::Anatomia::Circulatorio I" ^
  --slug anato-05-circulatorio-linfatico-I ^
  --dry-run
```

Depois da leitura card-a-card, rodar sem `--dry-run` para copiar os aprovados. Tags adicionadas na cÃ³pia: `NEBLI::<slug>`, `NEBLI::externo`, `NEBLI::<source>`.

Para Dope/Netter-style por query:

```bash
python flashcards/scripts/copiar_externos_para_deck.py ^
  --source Dope ^
  --query "deck:\"Referencias Externas::Dope Anatomy\" tag:Dope::Anatomy::Thorax" ^
  --deck "NEBLI::UC02::P3::Anatomia::Circulatorio I" ^
  --slug anato-05-circulatorio-linfatico-I ^
  --dry-run
```

---

## 4. Lacunas (o que estes decks NÃƒO cobrem)

- **Embriologia** â€” zero. Fonte: AnKing `#Embryology` + material prÃ³prio.
- **BioquÃ­mica/Bio molecular (P4)** â€” zero (decks sÃ£o anatomia/histo).
- **Fisiologia** â€” Dorian toca clÃ­nica, mas mecanismo fisiolÃ³gico nÃ£o Ã© o forte; AnKing/B&B seguem sendo a rÃ©gua.
