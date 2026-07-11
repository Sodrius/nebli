# PLANO — Pesquisa sistemática: como uma IA faz bons cards (e passa pente fino no pipeline)

> **Criado 2026-07-11.** Plano para chegar ao objetivo declarado do Davi: **o deck contém o conteúdo da E1 e a E1 contém o conteúdo do deck — mutuamente complementares, uma forma de estudo completa e íntegra.** Este documento planeja a pesquisa; a execução vem por fases, cada uma com entregável validável pelo Davi.

## Objetivo

Dois artefatos, complementares e sem lacuna entre si:
1. **E1** — ensina o conteúdo da aula (um tiquinho além do slide).
2. **Deck-aula** — retém a longo prazo tudo que a E1 ensinou, e **nada** que ela não ensinou (gate absoluto, `CLAUDE.md`).

Para isso, preciso destilar — de fontes reais, não de intuição — **o que é um bom card e uma boa explicação**, e construir (a) um gerador de cards NEBLI para as lacunas tipo-a (conteúdo que o AnKing não tem), e (b) um pente-fino que audita o pipeline inteiro de cards.

## Por que agora

A recuradoria das 3 aulas (2026-07-11) provou dois pontos:
- **Lacuna tipo-b** (existe no AnKing, subárvore não puxada) → resolvida pela busca por conteúdo (`descobrir_cards_por_conceito.py`).
- **Lacuna tipo-a** (genuinamente ausente: fotoliase, SOS, tautômero, conta de ATP do palmitato) → **só** cobrível por **card NEBLI gerado da E1**. O banco de questões está vazio pra essas aulas (0-1 questão), então a E1 é a única fonte. Gerar exige antes calibrar o padrão de bom card (memória `calibrar-antes-de-gerar-cards`). É isso que este plano viabiliza.

---

## Fluxo de pesquisa — 4 correntes

### Corrente 1 — Dissecar cards reais do AnKing (fonte primária, offline)
O `flashcards/scripts/anking-v12-export.txt` (92 MB, ~28k notas) é um corpus de cards que milhões de estudantes validaram. É a melhor referência de "bom card" que existe.
- **Amostragem estratificada:** por recurso (FirstAid, Bootcamp, Sketchy, Pixorize, B&B, Physeo) e por formato (cloze simples, cloze múltiplo, básico, image-occlusion, "one by one").
- **Dissecar N≈150 cards** e codificar: atomicidade (1 fato/card?), desenho do cloze (o que é apagado e por quê), uso do campo Extra (explica o *porquê*?), presença/função de imagem, comprimento da frente, uso de mnemônico, e — chave — **como a explicação carrega mecanismo** (causa→consequência) vs pura associação.
- **Saída:** `flashcards/ANALISE-CARDS-ANKING.md` — padrões recorrentes do bom card + tipologia de formatos. Alimenta `EXEMPLARES-CARDS.md` / `ANTI-EXEMPLARES-CARDS.md`.

### Corrente 2 — Princípios canônicos de formulação (literatura)
Fundamentos de spaced repetition e formulação de conhecimento (ler, extrair regras acionáveis, mapear ao contexto NEBLI):
- **SuperMemo — 20 rules of formulating knowledge** (Wozniak): princípio da informação mínima, atomicidade, "só aprenda o que entende", contexto. https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge
- **Andy Matuschak — How to write good prompts** (prompts de recuperação que constroem *entendimento*, não só fatos). https://andymatuschak.org/prompts/
- **Michael Nielsen — Augmenting Long-Term Memory** + **How to make memory systems widespread**. http://augmentingcognition.com/ltm.html · https://michaelnotebook.com/mmsw/
- **Control-Alt-Backspace — Rules for Designing Precise Anki Cards** (aplicação prática, médicos). https://controlaltbackspace.org/precise/
- **LeanAnki — cards respondíveis em 8s** · **MedSchoolInsiders — 13 best practices**. https://leananki.com/creating-better-flashcards/ · https://medschoolinsiders.com/medical-student/anki-flashcard-best-practices-how-to-create-good-cards/
- **Saída:** `flashcards/PRINCIPIOS-CARDS.md` — as regras destiladas, cruzadas com o que o corpus AnKing (Corrente 1) confirma/refuta na prática.

### Corrente 3 — Estado da arte de IA gerando cards (repos + tooling)
Repos GitHub que fazem geração/curadoria de cards com LLM — estudar arquitetura, prompts e formato de saída (o que reusar, o que evitar):
- **raine/anki-llm** — CLI/TUI, bulk-generate + processa campos via LLM, edita in-place por AnkiConnect, TTS. https://github.com/raine/anki-llm
- **thiswillbeyourgithub/AnkiAIUtils** — explicações, mnemônicos, ilustrações, aprendizado adaptativo, foco médico. https://github.com/thiswillbeyourgithub/AnkiAIUtils
- **jasperket/clanki** — servidor **MCP** que liga LLM ↔ Anki (basic + cloze) via AnkiConnect. Candidato a integração direta com o pipeline NEBLI. https://github.com/jasperket/clanki
- **PromtEngineer/Anki_FlashCard_Generator** — gera cards de PDF com LLM. https://github.com/PromtEngineer/Anki_FlashCard_Generator
- **ObsidianToAnki/Obsidian_to_Anki** · **Lammy23/Anki-Flashcard-Importer** — pipelines texto/markdown → Anki (LaTeX, cloze, HTML). https://github.com/ObsidianToAnki/Obsidian_to_Anki · https://github.com/Lammy23/Anki-Flashcard-Importer
- Buscar também: papers sobre qualidade de flashcards gerados por LLM (avaliação humana, taxa de card "ruim", alucinação factual).
- **Saída:** `flashcards/ESTADO-ARTE-IA-CARDS.md` — tabela repo→(o que faz, o que reusar, licença, integra AnkiConnect?) + decisão build-vs-reuse pro gerador NEBLI.

### Corrente 4 — Busca semântica (conserta a polissemia da descoberta)
A busca por conteúdo atual (`descobrir_cards_por_conceito.py`) é keyword e sofre polissemia ("repair" casa hérnia/osso). O conserto é **embeddings**:
- Indexar o texto dos ~28k cards do AnKing num vetor-store local (embeddings de frase); descobrir candidatos por **similaridade semântica** ao conceito da E1, não por token.
- Avaliar custo/latência (modelo de embedding local vs API) e se roda offline junto do export.
- **Saída:** protótipo `descobrir_cards_semantico.py` + comparação de recall/precisão vs a versão keyword nas 3 aulas já curadas (baseline pronto).

---

## Entregáveis finais (depois das 4 correntes)

1. **Rubrica do bom card NEBLI** (0-3, análoga à R6): atomicidade, cloze bem desenhado, Extra com mecanismo, imagem quando cabe, voz NEBLI. Vira gate de qualidade da geração.
2. **Spec de geração** — como transformar uma frase/termo-nota/mini-resumo da E1 num card cloze NEBLI (1 cloze, Extra explicativo, imagem do slide quando houver). Calibrada contra o corpus AnKing (Corrente 1) e validada pelo Davi com 5-8 exemplos antes de gerar em lote.
3. **Pente-fino do pipeline de cards** — auditoria ponta a ponta: gate absoluto (todo card ancorado na E1), dedup semântico, checagem de mecanismo (card raso vs card que reconstrói a ideia), cobertura mútua E1↔deck. (NB: o "passe de revisão do Estágio 3" foi **recusado pelo Davi** em 2026-07-11 na forma antiga; este pente-fino é redesenhado do zero aqui, não é aquele.)
4. **Loop de completude mútua** — verificação automatizável de que todo subtópico da E1 tem card **e** todo card mapeia um subtópico da E1. Zero lacuna nos dois sentidos.

## Fases (cada uma para na validação do Davi)

- **Fase 0 (feito):** busca por conteúdo (`descobrir_cards_por_conceito.py`) + gate absoluto no cânone.
- **Fase 1:** Correntes 1 e 2 (dissecar AnKing + princípios) → rubrica do bom card. **Davi valida a rubrica.**
- **Fase 2:** Corrente 3 (estado da arte) → decisão build-vs-reuse + spec de geração. Gerar 5-8 cards de UMA lacuna tipo-a (ex.: fotoliase + SOS do DNA) → **Davi aprova o padrão**.
- **Fase 3:** geração em lote das lacunas tipo-a das 3 aulas-piloto; pente-fino; medir completude mútua.
- **Fase 4:** Corrente 4 (busca semântica) → elimina polissemia na descoberta; reprocessar as 3 aulas e comparar.

## Estado

- ✅ Fase 0. Baseline pronto: 3 aulas recuradas (biomol-25, bioq-23, bioq-21) + relatórios `descoberta-<slug>.md`.
- ⏳ Fase 1 aguardando ok do Davi para começar a dissecação do corpus AnKing.

## Fontes (verificadas 2026-07-11)

Ver links inline nas Correntes 2 e 3. Repos e ensaios acessados via WebSearch; confirmar licença de cada repo antes de reusar código.
