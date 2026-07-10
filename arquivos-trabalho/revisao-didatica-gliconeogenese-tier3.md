# Revisão profunda — Gliconeogênese · Tier 3 (Opus baseline)

**Data:** 2026-05-25
**Resumo avaliado:** `resumos-gerados/GLICONEOGENESE.pdf` (42 páginas)
**Avaliador:** Opus 4.7 manual (auto-revisão editorial profunda)

---

## T3.1 — Comparação com exemplar canônico

**Exemplar relevante:** `EXEMPLARES.md` categoria 1 (Explicação mecanística parágrafo-por-parágrafo) + categoria 7 (Analogia construtiva).

**Onde a gliconeogênese está NO PADRÃO:**
- Bypass 1 em 2.2 segue o padrão da categoria 1 quase ao pé da letra: cada enzima ganha um parágrafo dedicado, mecanismo antes de nome, ponte para o próximo passo no fim do parágrafo. Comparável ao exemplar 1.1 (receptores ionotrópicos).
- Atencao-boxes em voz de mecanismo (T2.6 score 5) seguem o padrão canônico melhor que muitos exemplares.

**Onde a gliconeogênese está ABAIXO do padrão:**
- **Falta de analogia concreta moderna.** O exemplar 7.1 (lápis dobrado / ligação ao estado de transição) é o ouro do NEBLI. Esta E1 tem zero analogias modernas (videogame, software, infraestrutura). Tem 1 analogia ("cachoeira morro acima" em 2.1) que é batida e fraca. O bypass 1 do piruvato → PEP é candidato natural a uma analogia de "pedágio com troca de moeda em dois compartimentos" ou "sistema de eclusas que precisa baixar água e abrir/fechar comporta numa ordem específica".
- **Sem refinamento histórico (cat 5).** Não menciona Cori (foi prêmio Nobel pelo ciclo de Cori); não menciona como o entendimento da F2,6BP mudou a visão da regulação metabólica nos anos 1980. Essas são deixas que prendem aluno em dificuldade — "isso tem nome, isso ganhou Nobel, então vale a pena entender".

---

## T3.2 — 3 parágrafos mais fracos

### Parágrafo 1: abertura de 1.3 (Onde acontece + 3 precursores)

**Citação literal:** "Você já tem duas peças do quebra-cabeça: *quem* precisa de glicose (cérebro e hemácia) e *quando* a gliconeogênese entra em cena (depois do glicogênio acabar). Falta a terceira: *onde* ela acontece, e *com que matéria-prima*."

**Diagnóstico:** começo expositivo seco, falha em T2.1 (sem pergunta abrindo). É o "deixa eu organizar o que vimos" — não é nem voz de monitor nem pergunta de aluno. É voz de PROFESSOR organizando, que viola o princípio "voz de aluno se perguntando".

**Sugestão de reescrita:**
> "Tem mais duas perguntas que faltam: *onde* essa fábrica de glicose fica, e *com qual matéria-prima*. Se o fígado é o ator principal, por que o rim só assume em jejum prolongado? E se o corpo precisa de glicose, por que não pode usar literalmente qualquer coisa que tem carbono — gordura, proteína, álcool — como matéria-prima?"

### Parágrafo 2: transição em 2.5 (Saldo energético)

**Citação literal:** "Agora dá para fechar a conta. *Quanto custa fabricar uma molécula de glicose a partir de dois piruvatos?* Vamos somar enzima por enzima."

**Diagnóstico:** voz de manual técnico. "Vamos somar enzima por enzima" é instrução, não ensino. Falha em T2.5 — não soa como monitor explicando, soa como livro avisando.

**Sugestão de reescrita:**
> "É hora de fazer aquela conta que o aluno em dificuldade odeia: *quanto custou esse troço todo?* Vou somar enzima por enzima e no final você vai entender por que o livro-texto diz '6 ATP' sem explicar de onde vieram. Spoiler: não vieram todos de ATP — tem GTP no meio, tem NADH no meio, e separar isso é o que diferencia quem entendeu de quem decorou um número."

### Parágrafo 3: subtítulo "Atenção mecanística" em 2.3 (Bypass 2)

**Citação literal:** "*Atenção mecanística:* FBPase-1 é uma enzima *diferente* da PFK-1. Sítio catalítico diferente, regulação oposta. Não é 'a PFK-1 andando para trás' — é uma enzima nova, com mecanismo próprio…"

**Diagnóstico:** o conteúdo está certo, mas a estrutura "Atenção mecanística:" em itálico é um tique que aparece N vezes na E1 (busquei: 3x). Vira ruído. O conteúdo deveria estar dentro do atencao-box canônico OU integrado ao parágrafo principal sem o rótulo.

**Sugestão:** mover para `#atencao-box("FBPase-1 não é a PFK-1 invertida", [...])`. Atualmente só temos 6 atencao-boxes e mais 1 caberia bem na 2.3.

---

## T3.3 — 3 subtópicos mais densos onde o aluno trava

### Subtópico 2.2 (Bypass 1 piruvato → PEP)

**Densidade:** ~700 palavras, 5 passos enzimáticos, 2 compartimentos, 1 figura. **CORRETAMENTE** o mais denso do resumo (é o conceito mais difícil do tema), mas no limite do aceitável.

**Sugestão:** quebrar o subtópico em 3 atos visualmente sinalizados (não tudo num bloco):
- Ato 1 — Por que precisa de 2 passos (já está bom)
- Ato 2 — Os 3 passos físicos (atualmente densos, fragmentar com `#subtopico-menor` se existir, ou negritos numerados)
- Ato 3 — A nuance do lactato (atalho)

Hoje o "Atalho do lactato" aparece como parágrafo final solto e o aluno em dificuldade pode achar que é "mais um detalhe". Promover a parte 3.

### Subtópico 3.2 (F2,6BP como interruptor mestre)

**Densidade:** 4 conceitos novos por parágrafo (F2,6BP, enzima bifuncional, cAMP, PKA, fosforilação alostérica). **PERIGOSO** para aluno em dificuldade.

**Sugestão:** adicionar 1 figura/diagrama esquemático mostrando a dança "insulina → desfosforila → cinase → F2,6BP ↑ → glicólise ON / glucagon → fosforila → fosfatase → F2,6BP ↓ → gliconeogênese ON". Hoje temos a figura slide-38 mas ela é texto do slide, não esquema. Talvez SVG novo? Ou tabela 2x4 com hormônio | estado | bifuncional | F2,6BP | resultado.

### Subtópico 3.4 (von Gierke)

**Densidade:** introduz 4 conceitos novos (G6Pase tipo Ia/Ib, hepatomegalia paradoxal, hiperuricemia via pentoses, acidose láctica via glicólise local) em ~400 palavras.

**Sugestão:** adicionar mini-resumo extra no meio (atualmente tem 1, no fim). Inserir após o passo "G6P se acumula → 3 destinos alternativos" um mini-resumo: "*Em uma seta:* G6P preso → vira lactato (acidose), vira ribose (uricemia), vira glicogênio (hepatomegalia). Três destinos, três sintomas."

---

## T3.4 — Voz fora do padrão

**Casos detectados:**

1. **"O corpo paga 6 ATP/glicose"** (recorrente, ~5x). É antropomorfismo aceitável uma vez, mas vira tique. Substituir variantes por "a célula gasta", "o fígado investe", "essa síntese custa".

2. **"Spoiler:"** (1.2). Linguagem coloquial de redes sociais que destoa do registro pedagógico. Trocar por "Adiante:" ou simplesmente fundir com o próximo parágrafo.

3. **"Esse é o subtópico mais denso do resumo. Leia devagar. Vamos por partes."** (2.2). É META-comentário sobre a própria estrutura do resumo, o que quebra a quarta parede pedagógica. Estilo "guia do leitor". Talvez aceitável uma vez, mas perigoso. Comparar com EXEMPLARES — os exemplares canônicos NÃO usam essa voz.

4. **Falta de auto-referência inversa.** O resumo nunca diz "você vai ver isso em mais detalhe no resumo X" porque a regra é "resumos independentes" (regra 6 do REDATOR-E1). OK.

---

## T3.5 — Veredito final

**O aluno em dificuldade real conseguiria aprender muito com este resumo?** **SIM, em grande parte.**

Razões:
1. **A espinha conceitual está bem montada:** as 4 camadas (por que precisa, como dribla a glicólise, com que substrato, como regula, complicações clínicas) cobrem o tema sem buraco. O aluno em dificuldade que estuda este PDF e os 30 exercícios sai sabendo gliconeogênese.
2. **Mas há 3 espaços de melhoria:** falta analogia concreta moderna que prenda o aluno emocionalmente; falta variação de registro entre subtópicos (regra 1a do REDATOR-E1 não foi totalmente respeitada); falta 1 figura esquemática em 3.2 (F2,6BP) que é o ponto mais antimnemônico do tema.

**Comparado com resumos NEBLI passados que Davi classifica como "zuados":** este resumo está acima da média. Não é exemplar (categoria 7.1 do EXEMPLARES é um patamar acima), mas é robusto. Não merece bloqueio do pipeline.

**Recomendação editorial:** aprovar com as 3 melhorias do Tier 2 + 3 reescritas do T3.2 + adição de 1 figura em 3.2.
