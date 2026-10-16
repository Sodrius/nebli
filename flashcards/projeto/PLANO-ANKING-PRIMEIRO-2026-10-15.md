# Plano vigente: decks AnKing-primeiro, calibrados deck a deck (15/10/2026, noite)

Origem: F-20261015-CLAUDE-06 (FEEDBACKS). Substitui, como fila e método, o PLANO-AJUSTE-DECKS-2026-10-15 (que tratava de *mais* cards; o problema real era *autoral demais e ruim*). Regras: MEMORY §5. Roteiro técnico: EXECUCAO-DECK-AULA (vale, com as mudanças abaixo).

## 1. Diagnóstico (medido no Anki vivo em 15/10, notas por aula, campo `NEBLI::origem`)

| Grupo | % autoral |
|---|---|
| UC08 (referência de Davi) | 4–17% (motilidade II: 40%) |
| UC03 P3 Micro (43, 44, 48, 50) | 50–77% |
| UC03 P3 Biomol (46, 52, 54) | 64–77% |
| UC03 P2 Micro (27, 30, 32, 34, 35, 39, 40) | 59–84% (39: 167 de 200) |
| UC03 P1 | apagada por Davi em 15/10 (“basicamente só autoral”) |
| UC19 FA01 | 60% |

Amostra aleatória de autorais (15/10) mostra os mesmos defeitos que Davi aponta:

- **Detalhe de livro que não é alvo da aula:** “Soil holds about {{c1::10⁷}} bacteria and 10⁵ fungi per gram…”; “Oomycetes… belong to the kingdom {{c1::Chromista}}”; “A {{c1::lichen}} is a mutualism…”; “Calico cats are almost always {{c1::female}}”; “Typhoid Mary…”.
- **Cloze em palavra que se completa pelo bom senso:** “…by {{c1::degrading host tissue}}”, “…contamination, penetration and {{c1::multiplication}}”, “…prostration, {{c1::low fever}}…”, “…that {{c1::selectively stimulate}} beneficial bacteria”, “Fungal cells are {{c1::nonmotile}}”.
- **Autoral onde o AnKing tinha cards:** a busca “polyenes” devolve 56 notas AnKing, “coagulase” 13, “diphtheria toxin” 7, “conidia” 6, e mesmo assim esses alvos saíram autorais.

**Causa:** o MEMORY já mandava “AnKing → autoral por último” e “>15% de autoral = auditar”, mas nada obrigava a provar que a busca foi feita. Escrever autoral era o caminho fácil; a busca era por palavra-chave, com um termo por alvo e sem ler as seções do AnKing que cobrem o tema. O problema estava no processo, não na falta de ferramenta. Os gates contavam forma (lint, ordem, Tab), não origem.

## 2. O que a pesquisa (GPT + verificação 15/10) muda

| Fonte | O que é (verificado) | Decisão |
|---|---|---|
| anki-semantic-search (zahiessam) | add-on; busca por palavra-chave + embeddings, fusão RRF, re-ranking cross-encoder, HyDE; MIT; 3 estrelas | **Referência de técnica**: busca híbrida + RRF no nosso `busca_acervos`. Não instalar. |
| Umeboshi (Karimuto) | gera tudo autoral a partir de áudio/slides via skills do Claude Code; não confere AnKing; 2 estrelas | **Descartar**: automatiza justamente o erro. |
| ankify (matthewalton) | plugin Claude Code; `/curate` audita deck contra rubrica, só faz triagem e marca em vez de apagar | **Referência**: triagem só-leitura dos autorais por rubrica (anti-exemplares). |
| pdf-anki (benno094) | Streamlit + OpenAI, gera do PDF | **Descartar**. |
| anki-api (SystemicVoid) | cards em JSON revisados antes de importar | Já temos (spec.py → build → apply). |
| “Anki Tagger” | não encontrado com esse nome; o mais próximo é o add-on High Yield Tags (AnKing-VIP), que mostra quanto de cada tag a seleção cobre | Ideia útil: medir cobertura por seção de recurso. |
| AnkiHub Smart Search | pago, na nuvem; recebe slides/objetivos e devolve cards AnKing; usuário relata “não muito eficaz”; em reconstrução | Opcional, se Davi tiver assinatura: comparar com a nossa matriz. |
| Lecture→Anki (lecturetoanki) | aula → busca por **tags de recurso** do AnKing v12 | **Aplicar**: segunda rota de busca pelas tags. |
| Prática de estudantes (guias/Reddit) | suspender tudo, desuspender AnKing por aula, cards próprios só para o que falta | É exatamente o modelo pedido; confirma o rumo. |

Recursos com tag no AnKing local (28.650 notas): `#FirstAid` 4.428 tags, `#B&B` 1.021, `#Pathoma` 187, `#SketchyMicro` 139, `#SketchyPath` 163, `#NinjaNerd` 230, `#DirtyMedicine` 96, `#Costanzo` 59, `#Bootcamp`, `#Physeo`, `#Pixorize`, `#OME`. Para cada aula, a seção correspondente desses recursos é lida **inteira**, não só os resultados de busca por palavra-chave.

## 3. Pipeline novo (ordem de Davi: material → buscar com afinco → autoral só para lacuna real → revisar)

1. **Material** (gate de fontes atual, sem mudança): lâminas + bibliografia + prova antiga + apostila/monitoria de veterano + tudo da pasta. Amplo e profundo, mas preso à aula.
2. **Inventário de conceitos** na ordem da aula: cada unidade verificável, marcada como *princípio* ou *detalhe* (princípio antes do detalhe: o que é um antibiótico → mecanismo geral → aminoglicosídeo → gentamicina) e com a fonte da aula que a sustenta (lâmina N, prova, apostila). **Item que só existe no livro não origina card autoral**: o livro confirma e aprofunda o que a aula ensina.
3. **Busca com afinco**, em três rotas, registrada em `busca/cobertura.tsv` (conceito · consultas feitas · candidatos lidos · veredito):
   - (a) palavra-chave com sinônimos e frases (atual `busca_acervos`);
   - (b) **seções de recurso**: tags `#FirstAid/#Pathoma/#B&B/#Sketchy*/#NinjaNerd` do tema, lidas inteiras;
   - (c) **busca semântica local** (a construir: embeddings dos 28.650 AnKing gerados uma vez, fundidos com (a) por RRF; inspirado no anki-semantic-search), para achar o card que diz a mesma coisa com outras palavras.
   Veredito por conceito: **coberto** (AnKing entra, com irmãos pertinentes) · **parcial** (AnKing + uma linha de Extra, ou autoral de complemento) · **lacuna**.
4. **Autoral só para lacuna real**, que deve ser pouca e quase sempre detalhe da aula. Cada autoral leva no spec: a fonte da aula, as consultas que não acharam nada e 2–3 espelhos AnKing. Escrita pelos EXEMPLARES/ANTI-EXEMPLARES: uma frase que ensina e um cloze no nome que se decora.
5. **Revisão**: leitura do deck na ordem (um aluno aprenderia a aula?), `REVISAO-AUTORAIS.md` (cada autoral contra o par dos anti-exemplares) e números ao final: % autoral, conceitos cobertos/parciais/lacuna. **Sem teto de autoral** (resposta de Davi), mas **gate duro por autoral**: sem a prova de lacuna em `cobertura.tsv` (busca nos três caminhos, em todos os acervos), o deck reprova e o `apply` não instala.
6. **Pistas visuais**: imagem do AnKing/livro/lâmina que ajude a decorar e organizar (figura no verso, oclusão quando reconhecer é o alvo).
7. **Tab**: não gerar; o Codex gera depois (gates com `NEBLI_SEM_TAB=1`).

Respostas de Davi (15/10): piloto 09; sem teto de autoral, mas autoral só para lacuna e em último do último caso (gate duro); detalhe de livro entra se houver card do AnKing; Step 1 = mais cobrados, mais se for base; clínica pouca e ampla; todos os irmãos; organizador AnKing quando houver, autoral só para classificação da aula; feedback nos cards e no chat, ao fim de cada deck, **esperar antes do próximo, nunca parar no meio**; refazer a P1 antes da P3; sem AnkiHub; modelo local de busca liberado; buscar SEMPRE em todos os acervos externos (gate duro).

## 4. Calibração deck a deck

- Um deck por vez. Davi estuda/folheia e comenta (campo de comentário, bandeiras ou chat).
- Cada comentário → FEEDBACKS (literal) → par real em EXEMPLARES/ANTI-EXEMPLARES → regra reescrita no MEMORY ou check no gate. Nada de regra nova solta.
- Antes do deck seguinte, reler só as entradas novas e o par mais parecido nos anti-exemplares.
- Registro curto por deck no ESTADO-ATUAL: % autoral, cobertos/parciais/lacunas e o que Davi aprovou ou reprovou.

## 5. Fila e decks a refazer

**Ferramenta (feita 15/10):** `nebli.semantica` (índice local de AnKing + todos os acervos externos, busca por significado + palavra com RRF, seções de recurso) e gates duros em `nebli/gates.py::cobertura_anking`, que também bloqueiam o `apply`.

**Todos os decks feitos pelo pipeline antigo serão refeitos.** Ordem: P1 primeiro (Davi julga a qualidade por ela), depois P3, P2, UC19, UC21. O número é a % de autoral medida em 15/10.

- **UC03 P1 (apagada; refazer do zero, na ordem):** 09 Lesão celular (**piloto**) → 02 Diagnóstico radiológico · 03 Diagnóstico patológico · 04 Radiografia e US · 05 TC · 06 Correlação 1 · 07 Organização do sistema imune · 08 Reconhecimento inato · 10 Ação hormonal · 11 Acúmulos e adaptação · 12 RM · 13 Envelhecimento · 14 Declaração de óbito · 15 GR1 · 16 Regulação hormonal · 17 Reconhecimento adaptativo · 18 Recombinação · 20 MHC · 22 Mecanismos efetores.
- **UC03 P3 (em estudo, prova 06/11):** 43 Biologia dos fungos 77% · 54 RNAs não codificadores 77% · 48 Micoses subcutâneas 76% · 47 Inflamação granulomatosa 72% · 52 Eucariotos II 68% · 44 Micoses cutâneas 67% · 46 Eucariotos I 64% · 42 GR3 62% · 61 Infecção viral 60% · 62 Inflamação crônica 57% · 50 Micoses sistêmicas 50% · 45 Linfócitos T 33% · 49 Células B 32%. Ainda sem deck: 51, 53, 55–60, 63, 64.
- **UC03 P2:** 39 Homem-ambiente 84% · 24 Ambiental 78% · 29 Operon 75% · 30 Controle microbiológico 75% · 34 Genética bacteriana 70% · 32 Antibióticos 64% · 40 Prática 3 64% · 27 Fisiologia bacteriana 62% · 35 Patogenicidade 59% · 31 Complemento 57% · 28 Prática 1 52% · 38 Inflamação aguda 51% · 33 Integração II 40% · 26 Morfologia 38% · 25 Integração I 30% · 23 Edema 28% · 19 Correlação 2 24% · 37 Inflamação início/resolução 18% · 21 GR2 16%. Sem deck: 36.
- **UC19:** FA01 Introdução 60%.
- **UC21:** Caso 5 (3%; conferir pelos gates novos, provavelmente só ajuste).
- **UC08:** referência; não refazer. Só a 09 Motilidade II (40%) passa por conferência de busca.
- **UC07:** deck de neuroanatomia direto (Machado, Netter, Kenhub), quando a UC chegar.
