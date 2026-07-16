# Guia de cards externos para deck-aula NEBLI

> Criado em 2026-07-14. Objetivo: quando o AnKing nao cobrir bem um conceito que precisa virar card, saber **qual fonte externa usar antes de criar NEBLIcard autoral**. Especialmente importante para anatomia e histologia, onde o AnKing e fraco em reconhecimento visual real.

## Regra de prioridade

Ordem obrigatoria para preencher lacuna de cards:

1. **AnKing curado**, quando cobre bem o conceito.
2. **Referencias Externas ja importadas no Anki**, quando o AnKing nao cobre ou cobre mal:
   - BlueLink para anatomia cadaverica real.
   - Dope Anatomy para atlas/Netter-style e relacoes espaciais.
   - Histology / LLU para micrografia e estruturas em corte histologico.
   - 100 Concepts (Dorian) para correlato clinico anatomico.
3. **NEBLIcard autoral**, so se AnKing + externos nao cobrirem.

Se o card externo existe e esta dentro da E1, ele deve ser preferido a autorar do zero. Autoria fica para lacuna real.

## Fontes externas mapeadas no Anki

### BlueLink Atlas

- Query base: `tag:BlueLink::*`
- Volume vivo visto no Anki: **2992 notes**.
- Modelo: `Image Occlusion Enhanced+`.
- Natureza: **fotos reais de dissecção de cadaver** com mascara IO.
- Campos relevantes: `Image`, `Question Mask`, `Answer Mask`, `Sources`.
- Busca: **por tag**, nao por keyword. Os campos textuais sao praticamente vazios.
- Uso preferencial:
  - anatomia macro;
  - prova pratica;
  - reconhecer estrutura em peca real;
  - complementar Dope/Netter, que e limpo demais.
- Tags uteis vistas:
  - `BlueLink::Heart` (~107)
  - `BlueLink::SuperiorMediastinum+RootOfNeck` (~113)
  - `BlueLink::DeepBack+SpinalCord` (~109)
  - `BlueLink::PectoralRegion+SuperficialBack` (~68)
  - `BlueLink::Lungs+VentilationPathway` (~56)
  - `BlueLink::PosteriorMediastinum` (~47)

Regra: em deck de anatomia macro, sempre tentar incluir um bloco BlueLink quando houver regiao correspondente. O aluno precisa ver a peca real, nao so esquema.

### Dope Anatomy

- Query base: `tag:Dope::*`
- Volume tagueado vivo visto no Anki: **1135 notes** por tags `Dope::*` nesta colecao.
- Modelo: `Anatomy`.
- Natureza: atlas/Netter-style com IO custom, labels numerados e campos ricos.
- Campos relevantes:
  - `Title`
  - `OccludedImage`
  - `Clinical`
  - `Comment`
  - `Plate`
  - `1a`, `2a`, ... labels de estruturas.
- Uso preferencial:
  - aprender relacao espacial limpa;
  - origem/insercao/inervacao/acao;
  - anatomia regional em esquema antes de peca real;
  - completar lacunas de AnKing em anatomia pura.
- Tags uteis:
  - `Dope::Anatomy::Thorax`
  - `Dope::Anatomy::Abdomen`
  - `Dope::Anatomy::Head_and_Neck`
  - `Dope::Anatomy::Upper_Limb`
  - `Dope::Anatomy::Lower_Limb`
  - `Dope::Anatomy::Pelvis_and_Perineum`
  - `Dope::Anatomy::Back_and_Spinal_Cord`
  - `Dope::Anatomy::Mixed_Bag`

Regra: Dope ensina mapa limpo; BlueLink confirma no cadaver. Para anatomia, os dois juntos sao melhores que AnKing sozinho.

### 100 Concepts (Dorian)

- Query base: `tag:*Anatomy_Clinical_Correlates::*`
- Volume vivo visto no Anki: **244 notes**.
- Modelos: `Cloze-b12d6` e alguns `Image Q/A`.
- Natureza: correlatos clinicos de anatomia.
- Uso preferencial:
  - ganchos clinicos de anatomia;
  - lesoes de nervos, fraturas, sindromes compressivas;
  - cards de aplicacao quando a E1 ja abriu o mecanismo.
- Tags uteis:
  - `*Anatomy_Clinical_Correlates::Dorian_Original::Thorax`
  - `::Abdomen`
  - `::Head_&_Neck`
  - `::Upper_Limb`
  - `::Lower_Limb`
  - `::Pelvis`
  - `::Breast`
  - `::Misc`

Regra: Dorian nao substitui card anatomico basico. Ele entra como camada clinica se estiver ancorado na E1.

### Histology

- Query base: `tag:H::*`
- Volume vivo visto no Anki por tags `H::*`: **1667 notes**.
- Modelo: `Cloze-AnKingMaster-v3 (Histology / ploirodon)`.
- Natureza: cloze de histologia com imagem no Extra.
- Uso preferencial:
  - conceito histologico geral;
  - tecido, matriz, celula, camada;
  - cards com imagem no Extra no padrao AnKing;
  - complemento de funcao/origem/estrutura.
- Tags uteis vistas:
  - `H::EpithelialTissue`
  - `H::ConnectiveTissue`
  - `H::MuscleTissue`
  - `H::NervousSystem`
  - `H::Blood`
  - `H::Bone`
  - `H::Cartilage`
  - `H::AdiposeTissue`
  - `H::Hemopoiesis`

Regra: quando o objetivo e "saber o tecido/estrutura e por que importa", buscar Histology antes de autorar.

### LLU Histology

- Query pratica: procurar por termos + `"magnified image"` ou por tags `@Medical_School::Histology::*` / `#FDN1_Block::Histology_Practical`.
- Volume probe visto: ~99 notes com `"magnified image"`; amostra com modelos `AnKingOverhaul (LLU Histology / SLin_LLUSOM)` e variantes.
- Natureza: micrografia real com cloze do tipo "This is a magnified image of {{c1::...}}".
- Uso preferencial:
  - reconhecimento visual de lamina real;
  - prova pratica de histologia;
  - estruturas que precisam ser vistas, nao so descritas.

Regra: para histologia, sempre separar dois tipos de card:

1. **Identificacao visual no corte**: IO ou cloze com micrografia real.
2. **Funcao/origem/relacao**: cloze normal com imagem no Extra.

Exemplo para corpusculo de Hassall:

- Card visual: micrografia de timo com IO cobrando `Hassall corpuscle`.
- Card conceitual: `Hassall corpuscles are found in the thymic {{c1::medulla}}.`
- Extra: imagem/micrografia + nota curta sobre celulas epiteliorreticulares e maturacao/seleção.

## Pipeline por tipo de aula

### Anatomia macro

1. Buscar AnKing para conceitos Step 1 de alto rendimento.
2. Buscar Dope por regiao para esquema limpo.
3. Buscar BlueLink por tag regional para cadaver real.
4. Buscar Dorian se houver correlato clinico natural.
5. Autorar so o que continuar descoberto.

Deck-aula ideal:

- cloze/QA de relacao e funcao;
- IO Dope/atlas para mapa limpo;
- IO BlueLink/cadaver para reconhecimento real;
- poucos Dorian para clinica ancorada.

### Histologia

1. Buscar `tag:H::<tecido>` para cloze com imagem no Extra.
2. Buscar LLU/micrografia para reconhecimento pratico.
3. Se estrutura do slide nao existir, criar IO sobre micrografia boa (Junqueira/OpenStax/slide), com asset hasheado e caixas justas.
4. Sempre parear visual + conceito:
   - visual: "que estrutura e esta no corte?"
   - conceito: "qual funcao/origem/relacao?"

Deck-aula ideal:

- IO/micrografia para estruturas cobradas visualmente;
- cloze normal para funcao, origem e comparacao;
- imagem no Extra na maioria dos cards.

Para micrografia sem rotulo textual, usar `flashcards/scripts/io_manual_from_image.py` em vez de OCR. Esse e o caminho para estruturas como corpusculo de Hassall, polpa branca/vermelha, tunicas vasculares, tipos de cartilagem, osteon, glomerulo etc.

Exemplo:

```bash
python flashcards/scripts/io_manual_from_image.py micro_timo.png ^
  --slug histo-11-hassall ^
  --header "<b>Thymus</b> - identify the highlighted structure" ^
  --box "Hassall corpuscle:420,310,80,65"
```

Depois aplicar com `io_apply.py` apos validar o preview.

### Embriologia

Os decks externos de anatomia/histo quase nao ajudam. Usar:

1. AnKing embryology quando houver.
2. Imagem limpa/slide para processo visual.
3. NEBLIcard autoral ou IO de esquema quando AnKing nao cobrir a coreografia.

### Bioquimica/Biologia molecular

Referencias externas de anatomia/histo nao cobrem. Usar:

1. AnKing.
2. Imagem irma do AnKing/Physeo/Pixorize/Sketchy quando autorar.
3. NEBLIcard autoral com imagem no Extra se lacuna real.

## Comando padrao para copiar externos

Usar `flashcards/scripts/copiar_externos_para_deck.py`.

BlueLink:

```bash
python flashcards/scripts/copiar_externos_para_deck.py ^
  --source BlueLink ^
  --tag "BlueLink::Heart" ^
  --deck "NEBLI::UC02::P3::Anatomia::Circulatorio I" ^
  --slug anato-05-circulatorio-linfatico-I ^
  --dry-run
```

Dope:

```bash
python flashcards/scripts/copiar_externos_para_deck.py ^
  --source Dope ^
  --query "tag:Dope::Anatomy::Thorax" ^
  --deck "NEBLI::UC02::P3::Anatomia::Circulatorio I" ^
  --slug anato-05-circulatorio-linfatico-I ^
  --dry-run
```

Histology:

```bash
python flashcards/scripts/copiar_externos_para_deck.py ^
  --source Histology ^
  --query "tag:H::NervousSystem" ^
  --deck "NEBLI::UC02::P3::Histologia::Tecido nervoso" ^
  --slug histo-10-tecido-nervoso ^
  --dry-run
```

Dorian:

```bash
python flashcards/scripts/copiar_externos_para_deck.py ^
  --source Dorian ^
  --query "tag:*Anatomy_Clinical_Correlates::Dorian_Original::Thorax" ^
  --deck "NEBLI::UC02::P3::Anatomia::Circulatorio I" ^
  --slug anato-05-circulatorio-linfatico-I ^
  --dry-run
```

Depois do `--dry-run`, selecionar card-a-card contra a E1. Rodar sem `--dry-run` apenas nos aprovados ou com query ja refinada.

## Canon de qualidade

- Card externo copiado nao e `NEBLI::neblicard-autoral`; e `NEBLI::externo`.
- Original externo fica intocado.
- Proveniencia e credito de imagem ficam preservados.
- Card so entra se o conceito estiver na E1 ou se a E1 for patchada antes.
- Para histologia e anatomia, **imagem nao e luxo**: e parte do conteudo testado.
