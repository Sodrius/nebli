# PLANO — Deck-prova UC19 Farmacologia Básica (29/10/2026, F-20261029-CLAUDE-04)

Prova: **30/11 (turma B)**, no e-Disciplinas; recuperação 01/12. Executor: Claude. Este plano é a norma do deck-prova até ele ser entregue; mudança só por feedback de Davi.

## 0. O pedido (literal)

> monta um plano para fazermos um deck-prova de farmáco independente das minhas aulas, mas cobrindo tudo da apostila e tudo dos materiais extras
> quero descartar o que já temos, tá ruim

> ótimo
> vou querer principalmente anking
> também quero que seja realmente cobridno tudo e um pouco mais

> registra o plano com mais detalhe para seguir essas duas especificações
> planeja bem como irá fazer

> pode usar lâmina de vez em quando e pode suspsneder e marcar

O que isso quer dizer:
- **Deck-prova independente:** o deck é organizado pelo assunto da prova, não pelas aulas. A base é a apostila mais os materiais extras. As lâminas não organizam o deck e só entram de vez em quando.
- **Duas especificações**, que viram gates duros na seção 2:
  - **E1, principalmente AnKing;**
  - **E2, cobrir tudo e um pouco mais.**
- **O deck atual sai:** 258 cards, sendo 108 já estudados, 112 autorais e 51 suspensos. Ele é suspenso e marcado com `NEBLI::retirado::deck-prova`, com backup e sem apagar.
- **Os decks-aula da UC19 param.** FC III (16/11), FC IV (23/11) e Farmacodinâmica II (09/11) não ganham deck próprio. O deck-prova já cobre esses assuntos pela apostila e pelos extras.

**Diferença para o §12b do MEMORY:** lá, "deck-prova" é a revisão do conjunto dos decks-aula de uma prova. Aqui, é um deck construído para a prova.

## 1. Fontes e papel de cada uma

| Fonte | Onde | Tamanho | Papel |
|---|---|---|---|
| Apostila Guia de Farmacocinética (J. Taba) | pessoal `UC19/Outros` | 21 pág., 5 aulas, 17 capítulos + exercícios | **base** da farmacocinética |
| Objetivos cognitivos e exemplos de questões (Emer, Stephen, De Nucci) | `UC19/Outros` | 9 pág. | **base**: roteiro oficial do que cai (FD 1–9; FC a–f) |
| Questões orientadoras de farmacodinâmica 2026 | `UC19/Outros` | 40 questões, 10 delas casos clínicos | **base** da farmacodinâmica e calibração |
| Questões orientadoras de farmacocinética | `UC19/Outros` | 40 questões com gabarito comentado | **base** e calibração |
| Todas as questões (grupos TA/TB + 107 B) | `UC19/Outros` | 91 pág., ~205 questões, quase todas de FC | calibração: cada questão tem card que a responde |
| De Nucci, "Fundamentos da Farmacologia", cap. 1 | `UC19/Outros` | 18 pág. | **base**: texto do professor de FC |
| Resumo da aula 1 | `UC19/Outros` | 8 pág. | **base** dos fundamentos e alvos |
| Uma breve história do estudo dos fármacos & Nobel (= Material Complementar I da turma) | `UC19/Outros` | 21 pág. | só o que os objetivos e as questões pedem (phármakon, Paracelso, descoberta de fármacos) |
| Ementa | turma e pessoal | 2 pág., **só imagem** | ler pelas páginas renderizadas; confere o escopo |
| Cronograma | turma e pessoal | 3 pág. | escopo e datas (lido) |
| Rang & Dale, 7ª ed. | `Não compartilhar/Menores/Bibliografia principal - medicina/` | caps. de princípios, alvos, absorção/distribuição, metabolismo/excreção, farmacocinética | **confirma** e permite o "um pouco mais" só quando há card de acervo (MEMORY §5: o livro nunca origina autoral) |
| Lâminas: Introdução (69), FC I (186), FC II (153), Oral (46), Clearance II (46), Tipos de medicamento (61) | pessoal `UC19/0x` | — | **de vez em quando**: figura real quando o acervo não tem, ou para conferir um termo; cada uso é registrado com motivo |
| ≥ 1 vídeo de canal que Davi acompanha (Ninja Nerd, Osmosis, Shomu) | `canais/` | — | calibração do aprofundamento (gate de canais) |

O texto de todos os PDFs já foi extraído nesta sessão, sem leitura de julgamento ainda. Cada arquivo de `UC19/Outros`, das pastas pessoais e da pasta da turma entra em `fontes-decl.json`, lido ou descartado com motivo. Exemplo de descarte: as duas cópias das lâminas de Introdução são idênticas.

## 2. As duas especificações como gates duros (gate `deck_prova`, novo)

### E1 — Principalmente AnKing
1. **Acervo:** 515 notas AnKing nas seções de farmacologia geral. Essas seções entram em `SECOES_DA_AULA`:
   - FirstAid 05_Pharm::01_PK_PD;
   - B&B 02_Basic_Pharmacology;
   - Pixorize 03::01_General_Pharm;
   - Bootcamp Pharmacology 01_PD e 02_PK;
   - SketchyPharm 09_Foundations e !General_Pharmacology;
   - Physeo 15_Pharm_Fundamentals;
   - NinjaNerd 16_Pharmacokinetics;
   - OME General_Pharmacology.

   O resto do Ninja Nerd "Basics" (antiepilépticos, diuréticos etc.) é fármaco clínico e fica fora. Somam-se Ankisthesia 07 Pharmacological Principles (55 notas), AnKing-MCAT (Henderson-Hasselbalch, pKa, cinética de primeira ordem e de ordem zero, logaritmo) e as buscas por palavra-chave e por significado em **todos** os acervos (catálogo dinâmico).
2. **Ordem para cada item:** AnKing → Referência Externa → organizador com vários clozes num card de acervo vizinho → autoral.
3. **Teto de autoral: 20% dos cards, sem `AUTORAL_EXCECAO` no modo prova.** Se cobrir tudo exigir mais, paro e pergunto a Davi. Esse é o conflito entre E1 e o F-20261029-CLAUDE-02, e a decisão é dele.
4. **Autoral só para o que o AnKing não tem e o material cobra.** Candidatos previstos:
   - classificação brasileira de medicamentos (referência, genérico, similar), equivalência farmacêutica × bioequivalência;
   - MRT;
   - Vd extrapolado × Vd área;
   - a forma como a apostila e o De Nucci encadeiam clearance → Css → dose;
   - mecanismos "sem alvo" (manitol, antiácido, quelante);
   - antagonismo farmacocinético e químico.

   Cada autoral passa pelo molde dos exemplares (GUIA-2), pela leitura dos anti-exemplares (GUIA-3) e pelo revisor independente.
5. **Card AnKing em inglês fica como está.** O termo brasileiro que a prova usa vai no Extra quando difere (por exemplo, "depuração" = clearance).

### E2 — Cobrir tudo e um pouco mais
1. **Tudo = `matriz-prova.json`**, montada antes de qualquer busca, com uma linha por item de cada fonte base:
   - os 9 objetivos de farmacodinâmica e todos os subitens do roteiro de farmacocinética (a.i–f.ii.3, cerca de 60);
   - os 17 capítulos da apostila;
   - as seções do De Nucci;
   - as 40 + 40 questões orientadoras;
   - as cerca de 205 questões do banco e os exemplos dos professores;
   - os tópicos do resumo da aula 1.

   Cada linha diz o que é preciso **decorar, explicar, distinguir, e-se ou organizar** (o mesmo vocabulário do mapa de profundidade) e o trecho literal da fonte.
2. **Gate de cobertura:** toda linha da matriz aponta para ≥ 1 card do plano, ou fica `fora` com motivo de uma lista fechada:
   - `eco` (repete outra linha);
   - `fora-do-escopo` (citação ilustrativa);
   - `calculo-sem-conceito` (conta pura cujo conceito já tem card).
3. **Gate de questões:** cada questão (orientadora, banco, exemplo de professor) lista os cards que bastam para respondê-la. Na E6, a revisão com raciocínio responde por escrito uma amostra de 40 questões (todas as 10 de caso clínico + 30 sorteadas), usando só o deck vivo. O que travar vira card.
4. **Um pouco mais = toda nota das 515 decidida.** Cada nota entra ou vai para `EXCLUIDOS` com motivo de uma lista fechada:
   - `duplica <nid que fica>` (o mesmo fato em outra fonte AnKing; fica a mais clara, com imagem);
   - `clinico-especifico` (indicação, efeito adverso ou esquema de um fármaco sem princípio geral);
   - `autonomico` (UC de outra prova);
   - `toxicologia-especifica`.
   - `lote-N` (a nota entra noutro lote; a rodada final confere) e `outra-uc` (fisiologia ou bioquímica sem princípio farmacológico), acrescentados em 30/10 ao montar o lote 1.

   Fato de farmacologia geral que o material não cita, mas que o AnKing tem, **entra** (é o "um pouco mais"), marcado com a cor da rubrica `A-step` ou `R-detalhe`.
5. **Rang & Dale** confirma cada bloco e aponta o que falta. O que falta só entra com card de acervo.

### Lâminas de vez em quando
- A lâmina nunca define bloco nem ordem.
- Entra em dois casos: como figura real no verso, quando o acervo não tem a imagem (curva dose-resposta, curva de Schild, gráfico log C × t, platô de infusão), ou para conferir um termo do professor.
- Cada uso fica em `imagens-batem.json` (o veredito "imagem bate") e em `fontes-decl.json` (`uso_laminas`, com motivo). Não há cota: "de vez em quando".

## 3. Estrutura do deck: 3 lotes, 13 blocos na ordem lógica

Decks: `NEBLI::UC19::P1::Farmacologia::Deck-prova 1 — Farmacodinâmica`, `… 2 — Farmacocinética` e `… 3 — Farmacocinética quantitativa`. Cada lote é uma corrida do pipeline: `deck-prova-uc19-<n>-<slug>-2026-10-xx`.

| Lote | Bloco | Itens (o que a prova cobra) | Fontes base |
|---|---|---|---|
| 1 | 1 Fundamentos | farmacologia, fármaco × medicamento × remédio, PD × PK, toxicologia, phármakon/Paracelso, descoberta de fármacos | Objetivos FD 1; FD q1–10; resumo aula 1; história |
| 1 | 2 Alvos e especificidade | receptores (4 famílias), canais, enzimas, transportadores, ação sem alvo (manitol, antiácido, quelante), DNA (cisplatina, doxorrubicina), estrutura-função, convencional × biofármaco | FD 2–3; FD q11–20 |
| 1 | 3 Agonismo e curvas | dose-resposta graduada e quantal, efeito terapêutico/tóxico/letal, janela e índice terapêutico, afinidade, eficácia, potência, EC50/Emax, agonista pleno, parcial, inverso e tendencioso, atividade constitutiva | FD 4–6; FD q21–28 |
| 1 | 4 Antagonismo e alosterismo | competitivo reversível × irreversível (aspirina, omeprazol, iMAO), não competitivo, fisiológico, funcional, farmacocinético, químico; ortostérico × alostérico (PAM/NAM); quiralidade | FD 7–8; FD q26–30 |
| 1 | 5 Perda de resposta | dessensibilização, taquifilaxia, tolerância, refratariedade, resistência | FD 9 |
| 1 | (casos) | os 10 casos clínicos das orientadoras: cada um aponta o princípio que testa (GUIA-4: caso é exemplo) | FD q31–40 |
| 2 | 6 Química e membranas | ácido/base fracos, Henderson-Hasselbalch, ionização × pH, lipossolubilidade, difusão × transporte, captura iônica (estômago, urina), quiralidade em PK | Roteiro FC a; apostila A2 |
| 2 | 7 Vias e medicamentos | enteral, parenteral e outras vias, com vantagens e limites; formas farmacêuticas; liberação modificada, depósito, transdérmico; tipos de medicamento; equivalência e bioequivalência | Roteiro FC b.iv–vii; apostila A1 (caps. 1–6); lâminas Oral e Tipos (de vez em quando) |
| 2 | 8 Absorção e biodisponibilidade | fatores de absorção, pH estômago × intestino, primeira passagem, P-gp e transportadores intestinais, F, idade e doença | Roteiro FC b; apostila A2 caps. 1–2; De Nucci |
| 2 | 9 Distribuição | ligação a proteínas, perfusão, BHE, placenta, sinusóide × músculo × cérebro, redistribuição, linfático, Vd e compartimentos | Roteiro FC c; apostila A2 caps. 3–4 |
| 2 | 10 Metabolismo | por que metabolizar, ativação × inativação, pró-fármaco, fase I × II, CYPs principais, indução e inibição (exemplos cobrados), farmacogenética (NAT2, CYP2D6, CYP2C19 clopidogrel), idade | Roteiro FC d; apostila A4 cap. 2; FC q2–7, 21–25 |
| 2 | 11 Excreção e clearance | renal (filtração, secreção, reabsorção, pH urinário), biliar e êntero-hepática, pulmonar, leite/suor; eliminação × excreção; Cl = taxa/C, aditividade, Cl = E × Q, alta × baixa extração, fluxo e ligação | Roteiro FC e; apostila A2 cap. 5 e A4; FC q11–20 |
| 3 | 12 PK quantitativa | primeira ordem, ke, t½, log C × t, bolus em 1 e 2 compartimentos, AUC, Vd1/Vdextrap/Vdarea, oral (ka, Cmax, tmax, F pela razão de AUCs), infusão (Css = taxa/Cl, platô, ~4–5 t½), dose de ataque, doses repetidas (acúmulo, pico-vale), MRT | Roteiro FC f.i; apostila A3; De Nucci; banco de questões |
| 3 | 13 Fora da primeira ordem | ordem zero / Michaelis-Menten (fenitoína, etanol), saturação de proteínas (salicilato), absorção dose-dependente | Roteiro FC f.ii |

- **Peso:** os fundamentos e o raciocínio vêm antes do cálculo. Cálculo vira card de **relação** (o que acontece com Css se Cl cai à metade), não conta pura. Isso segue o F-20261022-CLAUDE-02: pouca fórmula, muito raciocínio, clearance em cadeia.
- **Fármaco por nome** só como exemplo que o material cobra (atropina, aspirina, omeprazol, cetoconazol, rifampicina, fenitoína). Erro já cometido: tabela de fármacos no lugar de agonismo, antagonismo e curvas (anti-exemplar da FA01).
- **Estimativa:** lote 1 com 130–180 cards, lote 2 com 150–200, lote 3 com 70–110, total de 350–500. A 40 novos por dia, são 9–13 dias de estudo.

## 4. Como vou fazer, passo a passo

### P0 — Preparar (uma vez, antes do lote 1)
1. **Registro:** F-20261029-CLAUDE-04 em FEEDBACKS (feito); MEMORY §12b reescrito no lugar (feito); ESTADO-ATUAL com a reivindicação "Com Claude: deck-prova UC19" (feito).
2. **Pipeline v11, modo prova** (seção "Como mudar o pipeline"):
   - **No spec:** `MODO = "prova"` e `MATRIZ = "matriz-prova.json"`.
   - **Novo `nebli/base_prova.py`:** monta `fontes/slides.pdf`, a **base da prova**. Cada página é um excerto literal (fonte + página + texto puxado do PDF por âncoras, nunca digitado), na ordem dos blocos da seção 3, e grava `fontes/slides.txt` com `===== página N =====`. Assim os gates que já existem para lâmina valem para a base, sem contornar nada: compreensão por bloco, ordem do deck, fidelidade bloco a bloco, exemplo × princípio (os 10 casos clínicos são `exemplo`).
   - **Gate `deck_prova`:**
     - matriz 100% (linha → card ou `fora` com motivo da lista);
     - toda questão → cards;
     - as 515 notas decididas, com motivo da lista;
     - autoral ≤ 20% sem exceção;
     - uso de lâmina com motivo;
     - toda fonte base com ≥ 1 excerto na base.
   - **Testes** em `nebli/tests/test_gates.py`: o gate reprova uma linha da matriz sem card, uma questão sem card, uma nota de seção sem decisão e autoral a 21%, e não passa com matriz vazia.
   - `PIPELINE_VERSAO = 11` no molde; v10 arquivada em `arquivo/` com hash; histórico no EXECUCAO.
3. **Leitura obrigatória v10 inteira** (GUIAS 1–4, MEMORY, pipeline, rubrica, calibração, FEEDBACKS até F-…-04) registrada na E0 do lote 1.

### Para cada lote (E0–E8, como em todo deck)
- **E0:** abre a corrida, faz a leitura obrigatória e confere os comentários de Davi nos cards UC19 atuais. O que ele elogiou ou corrigiu ali calibra o deck novo.
- **E1:**
  - lê inteiras as fontes base do lote;
  - lê o Rang & Dale nos capítulos do lote (extraídos em `livros/`) e um vídeo de canal;
  - preenche `fontes-decl.json` com cada arquivo lido ou descartado;
  - monta a base da prova do lote (`nebli.base_prova`).
- **E2:**
  - preenche `compreensao-aula.json` sobre a base: o que esta parte da prova ensina, onde se encaixa, `processo` e `aprender` por bloco, `reconstrucoes` a partir das questões;
  - monta a `matriz-prova.json` do lote;
  - posta no chat um resumo curto.
- **E3:** `mapa-de-profundidade.json` (todo card nasce de uma linha da matriz), `escopo.json`, `motivacoes.json` congelado.
- **E4:**
  - percorre as seções inteiras (todas as 515 notas lidas pela frente e pelo verso);
  - busca por palavra-chave com sinônimos PT/EN (por exemplo depuração/clearance, biodisponibilidade/bioavailability, taquifilaxia/tachyphylaxis);
  - busca por significado de cada linha da matriz em todos os acervos.
- **E5:**
  - `spec.py` com `acervo()` primeiro (reaproveita a cópia NEBLI viva e o histórico dos 108 cards já estudados quando o fato continua) e `EXCLUIDOS` com motivo da lista;
  - autoral só para lacuna, com o revisor independente cego;
  - `imagens-batem.json`.
- **E6:**
  - retira o deck antigo **do mesmo lote** logo antes do apply (lote 1 → "Introdução à farmacologia e mecanismos de ação"; lote 2 → "Farmacocinética I e II", menos o que vai para o lote 3; lote 3 → o restante), com `nebli.retira`: suspende e marca `NEBLI::retirado::deck-prova`, com backup, sem apagar;
  - cards novos entram suspensos (Davi dessuspende);
  - uma janela curta de escrita (`nebli.decks.escrita`), nunca na nota em tela;
  - lê o despejo vivo e faz a revisão com raciocínio (amostra de questões respondida só com o deck).
- **E7:**
  - fidelidade bloco a bloco à base;
  - formatação final por agente independente (`formatacao-final-parecer.json`);
  - as 4 conferências do GUIA-4: ler só as frentes em ordem, conferir o peso por bloco, tapar o nome do fármaco nos casos, e ver se o título resume o deck.
- **E8:**
  - gates 100% (o do revisor pode ficar abaixo de 90%, pela regra de Davi);
  - pacote UC19 no Drive, ESTADO-ATUAL, commit/push, sync com Davi ocioso;
  - relato no formato do §11.

Davi pode mandar feedback entre os lotes. O feedback é aplicado antes do lote seguinte.

### Rodada final (depois do lote 3)
1. `python3 -m nebli.analise_prova "NEBLI::UC19::P1"`: repetição entre lotes, ordem, princípio antes do detalhe, peso do cálculo.
2. **Conferência de todas as questões** (as cerca de 285), não só da amostra: cada uma respondida com cards vivos. Lacuna vira card no lote certo.
3. Pergunto a Davi se apago os 258 retirados (`nebli.apaga_retirados deck-prova`, com backup) ou se ficam suspensos.

## 5. Datas-alvo
| Etapa | Alvo |
|---|---|
| P0 (modo prova + gate + testes) | 30/10 |
| Lote 1 Farmacodinâmica entregue | 31/10 |
| Lote 2 Farmacocinética entregue | 03/11 |
| Lote 3 PK quantitativa + rodada final | 06/11 |

Isso deixa mais de três semanas de estudo antes de 30/11 (a 40 novos por dia, 350–500 cards levam 9–13 dias).

## 6. Riscos e como trato
- **AnKing com o mesmo fato em 5 fontes** (B&B, Bootcamp, Pixorize, First Aid, Sketchy): deduplicação por significado (`nebli.semantica`). Fica a nota mais clara e com imagem; as outras viram `duplica <nid>`. Sem repetição (MEMORY §3).
- **Termos brasileiros que o AnKing não tem** (genérico × similar, bioequivalência pela ANVISA): são os autorais previstos. Se passarem de 20%, pergunto antes.
- **Ementa só em imagem:** ler pela renderização das páginas na E1.
- **Revisor independente oscilando** (61: 39–89%): corrijo defeitos reais e instalo pela regra de Davi; não gasto rodadas atrás de oscilação.
- **Davi no Anki:** uma janela de escrita por lote; sync só com ele ocioso.
- **Codex em paralelo:** reivindicação no ESTADO; Tabs dos cards novos ficam para o Codex (instalação sem Tab).
