# PESQUISA — O que é um bom card (empírico + teórico) → como o NEBLI gera NEBLIcards

> **Criado 2026-07-11.** Base de referência que a sessão usa para **gerar NEBLIcards** (cards autorais para lacunas que o AnKing não cobre). Junta três fontes: (1) dissecação de **500 cards reais do AnKing v12**, (2) princípios canônicos de formulação de conhecimento (SuperMemo, Matuschak, Nielsen), (3) estado-da-arte de IA gerando cards. Termina numa **spec de geração + rubrica + anti-padrões**. Método irmão: `PLANO-PESQUISA-CARDS-IA.md` (o plano); este é o **achado**.

---

## Parte 1 — O que os 500 cards do AnKing revelam (empírico)

Amostra estratificada por 26 recursos (FirstAid, Bootcamp, Sketchy, Pixorize, B&B, UWorld, AMBOSS, Costanzo, NinjaNerd, OME…), via `analisar_cards_anking.py --n 500`.

**Estrutura (números duros):**
- **100% cloze deletion** (note type AnKingOverhaul). O AnKing inteiro é cloze. Não há "basic front/back".
- **86% são single-cloze** (1 card por nota; `{{c1}}` só). Multi-cloze cai rápido: 2→10%, 3→2.4%, 4+→1.2%. **A atomicidade é a norma, não a exceção.**
- **Frente curta:** mediana **17 palavras**, p90 30, máx 64. Um prompt = uma pergunta ou uma frase.
- **83% têm campo Extra** (mediana **20 palavras**, p90 65). O Extra é quase universal e **breve** — não é um textão.
- **47% têm imagem.** Usada quando o fato é visual (imagem, histo, ECG, derm, achado radiológico).
- **23% usam hint no cloze** (`{{c1::resposta::dica}}` — a dica escopa o branco).
- **44% carregam mnemônico/sigla.**

**Padrões de craft (leitura qualitativa de 72 cards):**

1. **Dois stems dominam:**
   - **Pergunta-vinheta → [resposta]:** "What is the likely diagnosis in a patient with X, Y, Z? [Diagnóstico]" (cards 2, 12, 21, 61, 67). A vinheta dá as pistas; o cloze apaga o desfecho.
   - **Frase declarativa com o termo-chave apagado:** "heparina tem meia-vida [curta]" (4, 26, 56, 70). A própria frase ensina; o branco é o fato.
2. **O cloze apaga o token de MAIOR valor** — o diagnóstico, a enzima, o número, a **direção** (↑/↓), a palavra discriminante. Nunca apaga palavra de enchimento.
3. **Atomicidade real:** quando há 2+ clozes, são partes **de um mesmo fato** ("AKI causa [acidose] e [hiper]calemia" — um mecanismo, dois brancos), não fatos independentes empilhados.
4. **O Extra carrega o PORQUÊ**, em 3 modos recorrentes:
   - **Mecanismo:** "N₂O inativa a B12 → inibe a metionina sintase" (50); "↓ efluxo do humor aquoso" (25).
   - **Discriminador (anti-confusão):** "vs. dor trocantérica… vs. meralgia" (14); "compare com melena do lado direito" (20); "NF1 = meningioma/astrocitoma; NF2 = meningioma/ependimoma" (57).
   - **Mnemônico:** "Plugged is Painful; Galactocele is Gentle" (40); "ducreyi = you do cry" (58); "SHIP" (45).
5. **Contexto rico, nunca definição nua:** a frente sempre dá pistas de recuperação (a vinheta, o cenário). Card sem sujeito/contexto é raro.
6. **Imagem = a própria pista** quando o reconhecimento é visual (COPD no RX, "snowstorm" da mola hidatiforme, corpos de asbesto).
7. **Tom telegráfico, high-yield**, com setas (→) e siglas. (Para o NEBLI isto **muda** — ver Parte 4: a frente pode ser telegráfica, mas o Extra vai em voz de monitor, causa→mecanismo→consequência.)

---

## Parte 2 — Princípios canônicos (teoria) e o que o corpus confirma

**SuperMemo — 20 regras de formulação de conhecimento** (Wozniak). As que mais pesam para nós, com o veredito do corpus AnKing:
- **R1 Não aprenda o que não entende** · **R2 Aprenda antes de memorizar.** ⇒ **É exatamente o GATE do NEBLI:** card só do que a E1 já ensinou. O card retém; a E1 ensina.
- **R4 Princípio da informação mínima** (formule o mais simples possível). ⇒ confirmado pelos 86% single-cloze.
- **R5 Cloze deletion é fácil e eficaz** · **R8 deleção gráfica vale tanto quanto cloze.** ⇒ o AnKing é 100% cloze; 47% com imagem.
- **R6 Use imagem** · **R7 use mnemônico.** ⇒ 47% imagem, 44% mnemônico.
- **R9 Evite conjuntos** · **R10 evite enumerações** (quebre em cloze/overlap). ⇒ por isso listas viram cards separados ou ganham mnemônico-andaime.
- **R11 Combata interferência** (itens similares confundem; use contexto/exemplo). ⇒ é o **discriminador** do Extra (modo 4b acima).
- **R12 Otimize o texto** (frase compacta que dispara o recall) · **R16 pistas de contexto simplificam o texto.** ⇒ frente curta + hint no cloze.
- **R13 Refira-se a outras memórias** · **R17 redundância não contradiz a informação mínima** (ativo/passivo, passos de derivação). ⇒ vários cards sobre o mesmo mecanismo por ângulos diferentes são OK.
- **R18 Cite fontes.** ⇒ o NEBLIcard leva a tag-âncora `NEBLI::<slug>` e marca de gerado.

Fonte: https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge

**Andy Matuschak — How to write good prompts** (https://andymatuschak.org/prompts/): prompts de recuperação devem construir **entendimento**, não decoreba isolada; escrever prompts que forçam a *conexão* e o *porquê*. ⇒ é o campo **Extra** do NEBLIcard (o mecanismo), e é o que separa nota 2 de nota 3 na rubrica.

**Michael Nielsen — Augmenting Long-Term Memory** (http://augmentingcognition.com/ltm.html): cards devem ser sobre coisas que você *quer entender profundamente*; construir uma teia de cards que se reforçam. ⇒ cobertura mútua E1↔deck.

**Control-Alt-Backspace — Precise cards** (https://controlaltbackspace.org/precise/) e **LeanAnki** (card respondível em ~8s): precisão e brevidade — a frente deve ter **uma** resposta inequívoca.

---

## Parte 3 — Estado da arte: IA gerando cards (para automação futura)

Repos a estudar/reusar (confirmar licença antes de usar código):
- **raine/anki-llm** — bulk-generate + edição in-place via AnkiConnect. https://github.com/raine/anki-llm
- **thiswillbeyourgithub/AnkiAIUtils** — explicações/mnemônicos/ilustrações, foco médico. https://github.com/thiswillbeyourgithub/AnkiAIUtils
- **jasperket/clanki** — servidor **MCP** Anki↔LLM (cloze + basic); candidato a integração direta. https://github.com/jasperket/clanki
- **PromtEngineer/Anki_FlashCard_Generator** (PDF→cards) · **ObsidianToAnki/Obsidian_to_Anki** (markdown→Anki). 
- **Lição transversal:** a maioria gera do texto bruto; o diferencial NEBLI é gerar da **E1 já curada** com **gate de escopo** — precisão que os genéricos não têm.

---

## Parte 4 — Spec de geração do NEBLIcard (o que a sessão segue)

**Quando gerar:** SOMENTE para **lacuna tipo-a** — conceito da E1 que o AnKing genuinamente NÃO cobre (confirmado por probe do termo distintivo = 0). NUNCA para o que o AnKing tem (aí é curadoria). É **last resort** (ver Parte 6).

**Formato (compatível com R9 do FLASHCARDS):**
- **Cloze deletion**, **1 cloze por card** (`{{c1::…}}`). Multi-cloze só se forem partes de UM fato (SuperMemo R4/R10).
- **Frente:** uma frase declarativa NEBLI (ou pergunta focada) com **o token de maior valor** apagado. ≤ ~20 palavras (mediana AnKing = 17). A frase, sozinha, dá contexto de recuperação — nunca definição nua (SuperMemo R16).
- **Extra (obrigatório):** 1–2 frases, **voz de monitor NEBLI**, causa→mecanismo→consequência OU um **discriminador** contra a confusão clássica. ≤ ~35 palavras. É o que carrega o *entendimento* (Matuschak) — sem ele o card é nota ≤1.
- **Imagem:** quando o fato é visual, puxar do slide do professor (`figuras/<slug>/slide-XX.png`) ou de um card AnKing. Opcional, preferível quando ajuda (SuperMemo R6).
- **Origem/auditoria:** tags `NEBLI::<slug>` **+** `NEBLI::gerado` (distingue card autoral de card AnKing curado; permite auditar e reverter).

**Rubrica do NEBLIcard (0–3, gate de qualidade — só entra ≥2):**
| Nota | Card |
|---|---|
| 0 | ambíguo (mais de uma resposta), ou apaga palavra de enchimento |
| 1 | fato nu, sem contexto na frente e/ou sem Extra explicando o porquê |
| 2 | frente contextualizada + cloze no token-chave + Extra com 1 frase de mecanismo — **mas o branco ainda é adivinhável pela frase** |
| 3 | 2 + o cloze apaga **mecanismo/consequência/discriminador** (não o rótulo óbvio) → baixa adivinhabilidade + Extra reconstrói o porquê (+ imagem se visual) |

**Princípio anti-reconhecimento (canônico 2026-07-11, feedback do Davi).** O cloze deve apagar a informação que **exige saber**, não a que se **infere do resto da frase**. Erro clássico: clozar o *rótulo* (o nome da enzima) enquanto a frase já escreve o *mecanismo* inteiro ao lado — aí o Davi acerta por reconhecimento/eliminação, sem conhecer o conteúdo. Preferir apagar o **mecanismo, a consequência, o valor ou o discriminador**, deixando o rótulo/cenário como pista de recuperação. Cada card assim **puxa mais conteúdo** — acertar passa a significar realmente saber. Equilíbrio (não cair no oposto): a frente ainda dá contexto — não vira definição nua nem cloze ambíguo (nota 0). Teste rápido antes de fechar: *"dá pra adivinhar o branco só relendo a frase?"* Se sim, cloze a informação errada — mova o branco para o que precisa ser memorizado.

**Anti-padrões (rejeitar):**
- **Cloze de reconhecimento** — apagar o rótulo óbvio quando o mecanismo já está na frase (adivinhável sem saber). Mova o branco para o mecanismo/consequência.
- **Enumeração empilhada** ("as 5 causas são…") como um card → quebrar ou dar mnemônico-andaime (SuperMemo R9/R10).
- **Definição nua** sem pista de contexto (falha de retrieval cue).
- **Multi-fact cloze** com brancos independentes (força repetir o card inteiro por um sub-item difícil — SuperMemo R4).
- **Extra que só repete a frente** (tem que agregar o porquê).
- **Cloze ambíguo** (vários preenchimentos válidos).
- **Conceito fora da E1** → viola o GATE ABSOLUTO. Nem gerar.
- Vocabulário/escopo **Step 2** (manejo clínico avançado) — calibre é Step 1.

---

## Parte 5 — Como fica o loop de completude mútua

E1 → (curadoria AnKing cobre o tipo-b) → sobra a lacuna tipo-a → **NEBLIcard gerado da E1** cobre. No fim: **todo subtópico da E1 tem card** (AnKing curado OU NEBLIcard) e **todo card mapeia um subtópico da E1** (gate). É a complementaridade que o Davi pediu: o deck contém a E1 e a E1 contém o deck.

---

## Parte 6 — NEBLIcard é LAST RESOURCE (não é o padrão)

**O padrão do deck-aula é o card curado do AnKing.** O AnKing é validado por milhões de estudantes, tem imagem, Extra e formato maduro. **Gerar NEBLIcard é a resposta do pipeline canônico às LACUNAS — e só a elas:** quando, e apenas quando, o AnKing genuinamente não tem aquele conteúdo (lacuna tipo-a, confirmada por probe do termo distintivo). Ordem de prioridade, sempre: **(1) card AnKing curado** → **(2) subtópico coberto?** se sim, pronto → **(3) só se resta lacuna real, gerar NEBLIcard**. Nunca gerar NEBLIcard para o que o AnKing já cobre bem. Menos autoral, mais AnKing — o autoral é o tapa-buraco de precisão, não a fonte.
