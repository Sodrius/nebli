# Plano de continuação dos decks — 14/10/2026 (Claude)

Pedido de Davi: “replaneja a continuação da geração de decks do anki, para seguirmos fazendo vários / integra os vários feedbacks que dei em sessões anteriores, erros recorrentes e coisas que são prioridade (completude do deck, organização das ideias, profundidade e qualidade dos cards autorais) / deixa pronto para eu continuar a geração com qualidade de outra sessão / adiciona no plano uma revisão final depois de geramos todos os decks / a próxima aula que deve ser gerada é inflamação crônica, que ficou ruim e apaguei”.

**Lugar deste documento:** as regras continuam no [MEMORY](../../MEMORY.md), que prevalece em caso de conflito; os comandos estão no [roteiro](EXECUCAO-DECK-AULA.md); o percurso card+Tab está no [PLANO-CARDS-TABS](PLANO-CARDS-TABS.md) (Codex, 14/10). Este plano define **a ordem do trabalho, os controles de qualidade C1–C7 que faltavam entre as regras e a entrega, e a revisão final**. Não cria regra nova de preferência. Quando um controle virar regra estável, ela é reescrita no MEMORY e este plano é arquivado.

## 1. Por que os últimos decks falharam (com evidência)

| # | Defeito recorrente | Evidência concreta | Controle |
|---|---|---|---|
| 1 | **Cloze esconde paráfrase, não nome.** A resposta é um sintagma abstrato, que pode ser adivinhado pela gramática ou dito de dez formas. | 62 (13/10): “{{mediator production}}”, “{{collateral tissue damage}}”, “{{recruit more leukocytes}}”, “{{injury, recruitment, repair}}”, “{{self-perpetuating}}”, “{{insidiously}}”, “{{cytokine secretion}}”. | C3 |
| 2 | **Nome importante só no Extra.** O processo virou card e o termo que Davi precisa recuperar ficou no verso. | 62: IFN-γ/TLR (ativação M1), IL-10/TGF-β (M2), MIF, MBP no Extra. Davi: “às vezes sei o processo e preciso saber o nome de estruturas importantes”. | C2 |
| 3 | **A mesma ideia em vários cards.** | 62: `ic-def`, `ic-nao-resolvida`, `ic-persiste`, `ic-sem-aguda` e `ic-causa-infec` giram todos em torno de “estímulo persiste → lesão e reparo coexistem”. | C4 |
| 4 | **Faltam cards organizadores.** A tríade virou um cloze triplo longo; não havia card que recuperasse os conjuntos que estruturam a aula. | 62: `ic-triade` com três lacunas numa frase; ausência de conjuntos (causas, M1×M2, braços do macrófago). | C2 |
| 5 | **Especificidade sem mecanismo geral; exemplo virando card; detalhe acima do ciclo básico.** | Granulomatosa (125 → refeita), P2 da UC03 com repetição/detalhe, Radio/Pato P1, Diagnóstico radiológico, UC19 FA01. | C1 |
| 6 | **Gate e “auditoria” aprovaram deck que Davi reprovou.** | 62: gates 56/56 e auditoria item a item em 13/10, deck apagado por Davi em 14/10. | C6 |
| 7 | **Metatexto e frente de imagem fraca.** | 62 `ic-img`: “Panel A shows {{chronic}}… panel B shows {{acute}}”. | C3 |
| 8 | **Processo.** Suspender em vez de apagar, numeração não refeita (granulomatosa); afirmar o que não foi feito. | F-20261013-CODEX-04; MEMORY de 02/10. | MEMORY §1/§10 |

Busca rápida feita em 14/10 (`nebli.busca_acervos`): o AnKing tem 135 notas com “chronic inflammation”, quase todas de órgão/doença (Hashimoto, ectasia ductal, cistite glandular). O núcleo geral de Patologia é pouco coberto: **nessa área, autoral ser maioria é legítimo**, e o controle decisivo é a qualidade da escrita (C3), não a proporção. A proporção alta continua sendo gatilho para refazer a busca por frases e sinônimos (MEMORY §5).

## 2. As três prioridades em critérios verificáveis

**Completude.** Ao sair da aula + deck + Tabs, Davi consegue fazer tudo o que a lista de capacidades (C1) diz. Cada capacidade central tem ao menos um card que a recupera; item de prova e exercício da aula sempre tem card; menção no Extra ou no Tab não conta. Completude se mede por capacidades cobertas, não por número de cards.

**Organização das ideias.** O Browser conta a aula em blocos, na ordem das lâminas: cada bloco abre com o card de princípio, segue com mecanismos e nomes, e tem o seu **card organizador** quando a aula nomeia um conjunto (tríade, classificação curta, M1×M2, partes de uma estrutura). Formato do organizador: §6 do MEMORY e exemplo C/I/D no PLANO-CARDS-TABS.

**Profundidade e qualidade dos autorais.** Profundidade vem do Tab e da cadeia de cards (por que, como, em que condição, com que consequência) e de alguns cards de aprofundamento básico relevante (MEMORY §2: pertinência, importância, custo de revisão), não de curiosidades ou listas laterais. Completude é do conjunto; cada card segue pequeno e focal. Autoral de qualidade: uma frase com sujeito concreto e um processo, cloze num **nome** (termo, célula, mediador, estrutura, direção ou número quando ele é o alvo), escrita de modo que Davi não a distinga do AnKing.

## 3. Controles por aula (C1–C7), encaixados no roteiro

Cada controle produz um registro curto na corrida. Os registros C1, C2 e C6 ficam no `percurso-aula.md`; C3–C5 em `REVISAO-DE-QUALIDADE.md`. Nada disso dispensa os passos do roteiro.

- **C1 — Capacidades (passo 2, antes da busca).** Depois de ver as lâminas e as provas, escrever de 8 a 15 capacidades de saída no formato “explicar…”, “nomear…”, “organizar…”, “reconhecer…”, cada uma ligada a um bloco do percurso e às fontes. Separar o núcleo (mecanismo geral transferível) dos exemplos (ilustração no Extra/Tab) e dos subtemas com aula própria (cronograma).
- **C2 — Nomes e conjuntos (passo 2).** Lista de todos os termos que a aula nomeia (células, mediadores, estruturas, achados, classificações) com decisão: card, Tab ou fora, e o motivo. Para cada conjunto nomeado na aula, decidir se ele ganha card organizador. Agrupar lacunas pela utilidade de recuperação (exemplo C/I/D: c1 o item mais cobrado, c2 os outros dois juntos). Detalhe de aprofundamento em dúvida vai para **Casos de fronteira** no `percurso-aula.md` (exigido pelo gate) e para o relato.
- **C3 — Teste da resposta oculta (passo 4, em cada autoral).** (a) A resposta é um nome que um livro usaria, ou um número/direção que é o alvo? Paráfrase (“mediator production”, “collateral damage”, “recruit more leukocytes”) reprova. (b) Dá para acertar só pela gramática ou pelo bom senso? Reprova. (c) A frente tem contexto suficiente para uma única resposta? (d) Sem metatexto (“panel”, “figure”, “slide”). (e) Os 2–3 espelhos AnKing têm a mesma função de pergunta? Cada autoral recebe uma linha “C3 ok” ou a reescrita feita.
- **C4 — Uma ideia, um lugar (passo 4).** Agrupar as frentes pela relação que cobram. Duas cobrando a mesma relação → fundir ou retirar, salvo ganho declarado (`DUPLICACAO`). Cards organizadores não contam como repetição dos cards de processo.
- **C5 — Busca registrada (passo 3).** AnKing por frases e sinônimos de cada capacidade, cópia NEBLI viva primeiro (`sh()`); externos depois. Cada autoral aponta para a busca que não achou. Patologia geral: esperar poucos AnKing e compensar com C3.
- **C6 — Leitura como Davi (passo 5, depois do despejo).** Ler o deck vivo na ordem, só frente e resposta, e escrever de 10 a 15 linhas do que daria para explicar da aula apenas com aquilo. Comparar com C1: capacidade ausente, bloco sem princípio ou salto lógico → corrigir antes de entregar. Depois, ler os pares card+Tab por bloco (PLANO-CARDS-TABS §§4–5).
- **C7 — Tab (passo 5).** O Tab do card de princípio de cada bloco desenvolve a fundação; os seguintes retomam brevemente e aprofundam o ciclo básico além da aula, com fonte (livro da UC). Enquanto o gerador não receber o percurso automaticamente (pendência do PLANO-CARDS-TABS), o executor lê cada bloco e refaz os Tabs que repetem a introdução, saltam um passo ou ficam rasos. Antes de revisar Tabs de uma aula já entregue: `python3 -m nebli.explicacoes ruins` (marcas X de Davi).

**Calibração contínua:** a primeira aula feita com este plano (a 62) é o piloto. Davi a estuda e marca X/comentários enquanto a próxima é feita. A cada 3 decks, ou quando ele comentar, ler `ruins` e os comentários, registrar no FEEDBACKS → MEMORY e ajustar os controles.

## 4. Próxima aula: 62 Inflamação crônica, reconstruída do zero

- **Situação viva (14/10):** o deck `NEBLI::UC03::P3::Patologia::Inflamação crônica` não existe mais. **12 cards de outras aulas** ainda têm as tags da 62 (`NEBLI::2026-uc03-patologia-62-inflamacao-cronica`, `NEBLI::ordem::pt62-*`): 7 em Ativação de linfócitos T (Th1, Th17, IFN-γ, M1×2, M2×2), 2 em Inflamação granulomatosa (gigantócito por fusão de macrófagos, fibrose substitui parênquima), 1 em IM37 (eotaxina, suspenso) e 2 em Inflamação aguda (MBP, suspensos). **Primeiro passo:** decidir no spec novo quais reassociar por `sh()` (provavelmente M1/M2, Th1 e IFN-γ como princípio dado na 45) e tirar, via `nebli.decks.escrita()`, as tags da 62 das que não voltarem, sem tocar no resto dessas notas.
- **Corrida:** `arquivos-trabalho/deck-aula-uc03-pt62-inflamacao-cronica-2026-10-14/`, prefixo `pt62` (as tags órfãs saem antes, para o prefixo ficar livre). Copiar `fontes/`, `livros/` e `visual/` da corrida de 13/10 (lâminas I e II, transcrições, exercícios, palavras-cruzadas, provas, monitoria/apostila, Robbins). **Rever as lâminas** mesmo assim. O `spec.py` antigo serve como anti-exemplo, não como base.
- **Destino:** P3 (prova em 06/11) → entra **disponível**, não suspensa.
- **Fronteiras:** granulomatosa (47, feita) tem granuloma, gigantócito e fibrose; aguda (38) tem neutrófilos e eosinófilos/MBP; Ativação de linfócitos T (45) tem os subtipos Th; reparo e cicatrização (65) e hipersensibilidade (64) vêm depois. Na 62 entra o princípio de cada um, na medida em que explica a inflamação crônica, e o resto fica em linha de Extra/Tab.
- **Hipótese de percurso (conferir nas lâminas antes de usar; nada aqui está decidido):**
  1. *O que é e por que persiste.* Definição (inflamação, lesão e reparo simultâneos); vias de início (após aguda não resolvida ou insidiosa); causas agrupadas pelo mecanismo (infecção persistente, exposição prolongada a agente tóxico, autoimunidade/hipersensibilidade). Organizador candidato: as causas.
  2. *Como se reconhece.* Tríade C/I/D no formato de Davi; diferença histológica para a aguda (célula predominante, vasos, fibrose). Imagem só se reconhecer for objetivo da lâmina.
  3. *Macrófago, a célula central.* Sistema fagocítico mononuclear (monócito → macrófago), vida longa, ativação, M1 × M2 (sinais e produtos nomeados), produtos que explicam os três braços (lesão, recrutamento, fibrose/angiogênese), persistência (recrutamento, proliferação local, retenção/MIF). Organizadores candidatos: M1×M2 e os três braços.
  4. *Linfócitos.* Circuito T–macrófago (citocinas nomeadas nos dois sentidos); Th1/Th2/Th17 pelo que recrutam (por `sh()` da 45 quando já existir); plasmócitos; tecido linfoide terciário × MALT.
  5. *Outras células.* Eosinófilos (eotaxina, MBP), mastócitos, neutrófilos sob agressão persistente: cada um pela pergunta mecanística que a aula faz.
  6. *Ponte.* Fibrose como consequência (a 65 detalha) e o granuloma como forma especial (a 47).
- **Entrega:** roteiro completo + C1–C7; relato no chat (MEMORY §11) com o antes/depois em relação à versão apagada (o que mudou nos defeitos 1–4 da §1).

## 5. Fila depois da 62

Mudança de prioridade proposta (suposição até Davi confirmar): **a P3 da UC03 vem antes das aulas antigas da P1/P2**, porque é o que ele estuda agora, os decks entram disponíveis e a prova é em 06/11. As aulas antigas entram suspensas e não têm pressa.

1. **UC03 P3 sem deck, só as já dadas** (conferir lâminas na pasta pessoal e no drive da turma; aula sem lâminas = ainda não dada ou material ausente → pular e anotar): 61 Patologia da infecção viral (lâminas na pasta pessoal) · 57 Princípios gerais dos vírus · 58 Multiplicação viral e antivirais · 59 Patogênese da infecção viral · 51 Distúrbios do sistema imune · 64 Hipersensibilidade · 63 Resposta imune a vírus e fungos · 55 Prática de micologia · 60 Prática de virologia · GR4 · RD Contrastes. Ordem: cronológica da grade; em cada componente, o princípio antes (57 → 58 → 59 → 61). Conferir antes no ESTADO-ATUAL o que o Codex reivindicou (IM37 está com ele).
2. **Análise do deck-prova UC03 P3** (`nebli.analise_prova`, MEMORY §12b) assim que a P3 estiver completa, antes de 06/11.
3. Fila do ESTADO-ATUAL: UC03 P1 (09 Lesão celular, corrida aberta; 08, 10, 11…), P2 (40 Prática 3), UC21, UC02, UC01, conforme a ordem de Davi (UC03 → UC19 → UC21 → UC02 → UC01).

Cadência: um deck por vez, entregue e relatado, e então o próximo, sem esperar resposta (MEMORY §1).

## 6. Revisão final, depois de todos os decks

Duas camadas. A primeira já é regra (MEMORY §12b): **análise de cada deck-prova** quando a prova fecha. A segunda é nova, **a revisão final do conjunto**, feita por UC quando todas as aulas dela tiverem deck, e uma última vez sobre todas as UCs no fim:

1. **Inventário vivo × cronograma:** toda aula tem deck ou ausência justificada; nenhum deck órfão; tags de aula sem nota (como as 12 da 62) limpas.
2. **Capacidades:** para cada aula, reler o C1 contra o deck vivo; listar as que estão sem card.
3. **Repetição** dentro da prova, entre provas e entre UCs (`nebli.analise_prova "NEBLI::UCxx"` e pares entre UCs que compartilham tema, como inflamação × histologia ou farmacologia × microbiologia).
4. **Progressão:** a prova e a UC ensinam em ordem lógica; quando a ordem do curso é bagunçada, cards-ponte de princípio (sem reorganizar decks).
5. **Autorais:** C3 em todos os autorais das aulas feitas antes deste plano (são os mais prováveis de ter paráfrase no cloze); refazer a busca nas aulas com autoral alto.
6. **Organizadores:** cada aula tem os conjuntos que a estruturam (C2).
7. **Tabs:** `ruins` de toda a coleção, reescrever os marcados com X e ler uma amostra por aula; Tabs de estilo antigo só se Davi pedir.
8. **Cores e carga:** cor coerente com o motivo; dessuspensos por semana de aula comparados à meta de 40 novos/dia, como informação para Davi, sem cortar cobertura.
9. **Comentários de Davi:** protocolo do MEMORY §10.
10. **Técnico:** `nebli.gates` em todas as corridas, `nebli.ordem verificar`, pacote de cada UC republicado, sync.

Saída: `arquivos-trabalho/revisao-final-<UC>-<data>/RELATORIO.md`, com o julgamento por aula, as correções aplicadas pelos specs (`retira`, `recolor`, `delta`, Tabs afetados) e a lista do que exige decisão de Davi. Apagar notas só com autorização dele e backup.

## 7. Retomar em outra sessão

Pedido curto: **“continua”** ou **“faz a inflamação crônica”**. A sessão nova lê `CLAUDE.md` → ESTADO-ATUAL (Retomar aqui aponta para cá) → este plano §4 → roteiro do passo 0. Se quiser ser explícito:

> Lê o CLAUDE.md do NEBLI e o PLANO-CONTINUACAO-DECKS. Faz a 62 Inflamação crônica do zero, com os controles C1–C7, e segue a fila do §5 até eu mandar parar.

## 8. Coordenação e pendências técnicas

- **Codex (14/10):** atalho X no Tab, PLANO-CARDS-TABS e as regras de cards organizadores/percurso no MEMORY. Não editar esses arquivos enquanto ele trabalha neles; reler antes de gravar.
- **Pendente, não implementado** (não afirmar como pronto): gerador de Tab recebendo o percurso/bloco; check no lint para resposta de cloze genérica (C3a: termos como “production”, “damage”, “activation”, “recruitment” sozinhos ou sintagma verbal); X no tablet.
