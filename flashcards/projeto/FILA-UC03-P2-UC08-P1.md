# Fila de decks: UC03 P2 e UC08 P1

Lista compartilhada aberta em 24/09. Estado/propriedade por aula abaixo; regras gerais em README.md. Registros de cores/contagens antigos são históricos, não padrão para novas corridas.

## Modo vigente após feedback de 25/09/2026
- **E1 + cards** para novas execuções. A antiga exceção “só deck/sem E1” terminou. Não refazer retrospectivamente todas as E1 nem bandeiras sem pedido.
- AnKing → externos → autoria excepcional; não duplicar informação sem ganho. Verde = manter a longo prazo; azul = aprender, menor custo de esquecer; branco = incerteza real. BANDEIRAS-E-PROGRESSAO.md rege o julgamento; média ~50 verdes é referência, não cota.
- Fontes, bibliografia e canais em README; ler FEEDBACKS e CONTRATO. APKG local por UC comprimido sem flags no arquivo; **sem upload** até nova autorização.
- Decks apagados só são refeitos quando a aula é explicitamente solicitada/atribuída; seleção nova desde fontes atuais. Nunca restaurar plan/recibo/APKG antigo.
- Dicas gerais vão para FEEDBACKS e documento canônico; abaixo manter o log da execução, sem outra versão das regras.
- **25/09: este lote serviu para aprender.** Davi: "fizemos esses todos para aprender... depois vou apagar tudo e vamos refazer todos os decks". Primeiro o piloto E1 + cards de Edema (Claude); depois de calibrado, Davi apaga os decks e todos são refeitos pela rota nova, a partir das fontes atuais. Não restaurar nada destes decks. Contagens e cores abaixo são histórico.

## Divisão Claude × Codex

A divisão segue **blocos de assunto**, para que aulas que compartilham cards fiquem com o mesmo executor.

| Executor | Bloco | Aulas |
|---|---|---|
| **Claude** | UC03 Microbiologia + Bioquímica/Biologia Molecular; UC08 Fisiologia | Antibióticos, Morfologia, Patogenicidade, Controle, Homem–ambiente, Operon, Integração I e II, Grand Round 2, Motilidade I e II |
| **Codex** | UC03 Patologia + Imunologia; UC08 Anatomia + Biologia Tecidual | Inflamação aguda, Edema, Patologia ambiental, Complemento, Inflamação início/resolução, Correlação pat-rad 2, Vascularização, Esôfago/estômago/delgado, Intestino grosso, Estrutura do estômago, Intestinos |

Regras para não se baterem:

1. Cada executor trabalha **só no seu bloco**, na ordem da sua coluna. Se acabar o bloco, pergunta a Davi antes de pegar do outro.
2. Ao começar uma aula, marcar o estado `em andamento — <data>`; ao terminar, `feito` com a contagem.
3. Cada corrida tem sua pasta `arquivos-trabalho/deck-aula-<slug>-<data>/`.
4. **Escrita no Anki, um de cada vez.** Antes de aplicar, criar `arquivos-trabalho/ANKI-ESCRITA.lock` com executor, aula e horário; apagar ao terminar a verificação. Se o arquivo existir, esperar. Curadoria e busca (somente leitura) podem correr em paralelo.
5. **Cards de fronteira** (ex.: complemento × patogenicidade; LPS/parede × complemento): antes de criar, procurar a mesma origem e recuperação na coleção viva. Se já existe, associar os **card IDs/clozes pertinentes**, sem duplicar. Tag de nota pode complementar, mas não prova seleção dos irmãos nem aparição no deck físico da outra aula; conferir a consulta exata.
6. No log de calibração, registrar quem fez cada aula, para comparar a qualidade dos dois.

## Datas

| Prova | Data (planilha) |
|---|---|
| UC03 P2 | 02/10 (sex), 14h |
| UC08 P1 | 05/10 (seg), 14h |

## Fila do Claude

"Q" = questões firmes de provas antigas da UC03 (`referencias-externas/uc03/consultar.py`, sem ecos). "E1 antiga" = PDF "etapas 1 a 3" já no Drive, usado só como fonte.

| # | UC | Aula (conteúdo/pasta) | Data | Material no Drive | Livro | Q | Estado |
|---|---|---|---|---|---|---|---|
| C1 | UC03 | Antibióticos e resistência (32) | 10/09 | slides (enviados em 24/09) | Trabulsi | 24 | **feito 24/09, aprovado por Davi** ("agora sim gostei") — 85 notas/112 cards, 40 verdes, 12 rosas |
| C2 | UC03 | Morfologia e estrutura bacteriana (26) | 03/09 | slides + E1 antiga | Trabulsi | 11 | **instalado e sincronizado 24/09** — 69 notas/99 cards, 37 verdes, 16 rosas; aguarda revisão |
| C3 | UC03 | Patogenicidade bacteriana (35) | 15/09 | 4 PDFs (virulência, estafilo/estrepto, BGP, BGN) | Trabulsi | 11 | **instalado e sincronizado 24/09** — 141 notas/188 cards + 19 associadas; 107 verdes, 27 rosas; aguarda revisão. vídeos entregues no chat |
| C4 | UC03 | Operon em procariotos (29) | 08/09 | slides + exercícios + E1 antiga | Harper | 7 | **instalado e sincronizado 24/09** — 37 notas/57 cards: 13 AnKing, 25 MCAT, 19 autorais; 0 verdes, 6 rosas; 1 associada (Genética); aguarda revisão |
| C5 | UC03 | Integração metabólica II (33) | 18/09 | transcrição + E1 antiga; sem slide | Harper | 4 | **instalado e sincronizado 24/09** — 115 notas/148 cards: 138 AnKing, 6 MCAT, 4 autorais; 34 verdes, 15 rosas; aguarda revisão |
| C6 | UC03 | Controle microbiológico (30) | 10/09 | slides (enviados em 24/09) | Trabulsi | 1 | **instalado e sincronizado 24/09** — 29 notas/30 cards: 18 AnKing, 12 autorais; 0 verdes, 4 rosas; aguarda revisão |
| C7 | UC03 | Homem–ambiente–micro-organismo (39) | 17/09 | slides de microbiota (enviados em 24/09) | Trabulsi | 1 | **instalado e sincronizado 24/09** — 29 notas/35 cards: 20 AnKing, 15 autorais; 11 verdes, 5 rosas; 6 associadas (Patogenicidade/Fisiologia); aguarda revisão |
| C8 | UC03 | Integração metabólica I (25) | 01/09 | transcrição + E1 antiga; sem slide | Harper | 0 | **instalado e sincronizado 24/09** — 37 notas/50 cards novos: 41 AnKing, 9 autorais; 7 verdes, 6 rosas; + 27 notas da Integração II associadas; aguarda revisão |
| C9 | UC08 | Motilidade e absorção intestinal I (FI 08) | 14/09 | slide Aula-1 (6 lâminas, chegou 24/09) | Margarida | — | **instalado e sincronizado 24/09** — 25 notas/33 cards: 26 AnKing, 7 autorais; 9 verdes, 2 rosas; 4 associadas; aguarda revisão |
| C10 | UC08 | Motilidade e absorção intestinal II (FI 09) | 28/09 | slide Aula-2 (15 lâminas, chegou 24/09) | Margarida | — | **instalado e sincronizado 24/09** — 40 notas/53 cards: 44 AnKing, 9 autorais; 2 verdes, 6 rosas; 1 associada; aguarda revisão |
| C11 | UC03 | Grand Round 2, DM (21) | 29/09 | slides + caso clínico (pasta do Drive) | Harper | 3 | **v2 refeito 25/09 a pedido de Davi** a partir da pasta do Drive + provas GR/BQ — 67 cards próprios (+9 AnKing, +3 autorais, −1 autoral LADA), 23 verdes, 6 azuis; + associações da Integração I/II e Motilidade II; sincronizado. Relatório em `deck-aula-grand-round-2-v2-2026-09-25/` |

## Fila do Codex

| # | UC | Aula (conteúdo/pasta) | Data | Material no Drive | Livro | Q | Estado |
|---|---|---|---|---|---|---|---|
| X1 | UC08 | Vascularização das vísceras (AN 07) | 11/09 | slides + roteiro + questões orientadoras | Netter | — | feito — 24/09/2026 (Codex; 52 notas/96 cards; APKG UC08 local) |
| X2 | UC03 | Patologia da inflamação aguda (38) | 11/09 | transcrição + E1 antiga; sem slide separado | Robbins | 19 | feito — 24/09/2026 (Codex; do zero; 41 notas/60 cards + 1 associada; 8 rosas, 5 verdes; APKG UC03 local) |
| X3 | UC08 | Esôfago, estômago e intestino delgado (AN 01) | 03/08 | slides + E1 antiga + 2 extras | Netter | — | feito — 24/09/2026 (Codex; 51 notas/60 cards novos + 1 associada; 8 rosas; APKG UC08 local, sincronizado) |
| X4 | UC03 | Edema e congestão (23) | 27/08 | slide **compartilhado** com Patologia ambiental + E1 antiga | Robbins | 14 | feito — 24/09/2026 (Codex; 30 notas/36 cards novos + 1 nota/2 cards associados; 3 rosas, 8 verdes; APKG UC03 local, sincronizado). Piloto E1 + cards (Claude, 25/09) **reprovado — "excessivamente clínico" (F-C20)**; deck restaurado ao estado do Codex no mesmo dia (36 cards, bandeiras como antes). E1 do piloto só local. Pasta `deck-aula-edema-congestao-2026-09-25/` |
| X5 | UC08 | Estrutura geral do estômago (BT 03) | 17/08 | slides + E1 antiga + roteiro prático BT | Junqueira | — | feito — 24/09/2026 (Codex; 27 notas/35 cards; 10 verdes, 1 rosa; APKG UC08 local, sincronizado) |
| X6 | UC03 | Patologia ambiental (24) | 03/09 | slide **compartilhado** com Edema + E1 antiga | Robbins | 5 | **feito 24/09 (Claude assumiu do Codex)** — 20 notas/24 cards: 16 AnKing, 8 autorais; 4 verdes, 4 rosas; sincronizado |
| X7 | UC08 | Intestino grosso e canal anal (AN 02) | 10/08 | slides + E1 antiga + 2 extras | Netter | — | **feito 24/09 (Claude assumiu do Codex)** — 43 notas/45 cards: 21 AnatoKing, 12 AnKing, 1 MCAT, 1 Dorian, 10 autorais; 8 verdes, 6 rosas; 7 associadas; sincronizado |
| X8 | UC03 | Sistema complemento (31) | 08/09 | slides + E1 antiga | Abbas | 9 | **feito 24/09 (Claude assumiu do Codex; do zero)** — 39 notas/46 cards: 38 AnKing, 8 autorais; 3 verdes, 4 rosas; 2 associadas; sincronizado |
| X9 | UC08 | Intestinos (BT 04) | 24/08 | slides + E1 antiga + roteiro prático BT | Junqueira | — | **feito 24/09 (Claude assumiu do Codex; do zero)** — 36 notas/43 cards: 20 AnKing, 4 Histology, 5 LLU, 9 autorais; 7 verdes, 4 rosas; 2 associadas; sincronizado |
| X10 | UC03 | Inflamação: início e resolução (37) | 17/09 | slides + E1 antiga | Abbas | 4 | **feito 24/09 (Claude assumiu do Codex)** — 47 notas/61 cards: 49 AnKing, 12 autorais; 14 verdes, 6 rosas; 25 notas de X2/Patogenicidade associadas; sincronizado 25/09 |
| X11 | UC03 | Correlação patológica-radiológica 2 (19) | 01/09 | slides + E1 antiga | Robbins | 0 | **feito 25/09 (Claude assumiu do Codex)** — 52 notas/71 cards: 58 AnKing, 2 Lightyear, 11 autorais; 27 verdes, 7 rosas; 2 associadas (X1); sincronizado |

**Edema × Patologia ambiental:** o PDF de slides é o mesmo (4.936.174 B), mas foram aulas separadas. Cada deck usa só a sua parte do slide. A divisão sai da E1 antiga de cada aula e do tema; nenhum card da parte da outra aula entra por arrasto.

## Fora da fila

| UC | Aula | Motivo |
|---|---|---|
| UC03 | Fisiologia bacteriana (27) | já no Anki (45 cards, Claude); aguarda feedback |
| UC03 | Genética bacteriana (34) | já no Anki (44 cards); aguarda feedback |
| UC03 | Prática 1: morfologia e assepsia (28) | pasta vazia |
| UC03 | Práticas 2 (36) e 3 (40) | pastas vazias; fora da lista da P2 na planilha |
| UC03 | Grand Round 3 (42) | planilha associa à P2, mas é em 13/10; pasta vazia |
| UC08 | Esôfago e estômago: secreções e digestão (FI 05) | Davi, 24/09: secreção é P2 |
| UC08 | Intestino: secreções e digestão (FI 06) | Davi, 24/09: secreção é P2 |

## Dicas de Davi durante o lote

Davi vai dando dicas enquanto os decks são feitos. **Cada dica é incorporada, não só anotada**, para melhorar aos poucos o pipeline, a seleção e o entendimento mútuo:

1. Aplicar na aula em curso e, se couber, corrigir as aulas já fechadas do lote.
2. Registrar aqui: data, dica literal, executor e o que mudou.
3. Se for regra geral, gravar no arquivo canônico certo (README, EXECUCAO-DECK-AULA ou ACERVOS-REFERENCIA), para o outro executor também seguir. Dica que vale só para uma aula fica só aqui.
4. Antes de começar cada aula, reler esta seção.

| Data | Dica (literal ou resumo fiel) | Executor | Incorporada em |
|---|---|---|---|
| 24/09 | "vou dando dicas durante e quero que essas sejam incorporadas para melhorarmos paulatinamente o pipeline, a seleção e o nosso entendimento mútuo" | Claude | esta seção |
| 24/09 | "sempre se atentar à bibliografia": Robbins, Trabulsi, Junqueira, Margarida, Harper e Netter; "não precisa pôr tudo deles"; Davi avisa o livro de cada matéria e quando mudar | Claude | README § Bibliografia por matéria |
| 24/09 | Edema e congestão divide o slide com Patologia ambiental, mas foram aulas separadas | Claude | fila (X4/X6) |
| 24/09 | Secreções na UC08 são da P2 (FI 05 e FI 06 fora); motilidade é P1 | Claude | fila |
| 24/09 | Imunologia = Abbas. Livros novos na pasta Livros do Drive; os que faltarem, achar substituto | Claude | README § Bibliografia por matéria |
| 24/09 | "o foco é usar todas as fontes: prova + slide + E1 + livro + vídeos do assunto no YT + step 1 daquilo (que isso fique mt claro sempre)" | Claude | README § Fontes de TODA aula; Modo deste lote |
| 24/09 | Mais decks em Referências Externas (AnatoKing, USMLE Lab Values) | Claude | ACERVOS-REFERENCIA |
| 24/09 | "gosto da sua postura de me perguntar coisas sempre" | Claude | README (Perguntar) |
| 24/09 | Poder ajustar à mão quantos cards do NEBLI por dia ou semana | Claude | preset único `NEBLI` + `flashcards/scripts/nebli_novos.py`; README; EXECUCAO passo 8 |
| 25/09 | "estamos fazendo para aprender... se precisar de mais de 35 cards eu dou um jeito, a gnt nn diminui pra caber" | Claude | FEEDBACKS F-C18; README Tamanho/Rotina; BANDEIRAS |
| 25/09 | Aprovou: uma aula por vez assim que o material cair no Drive, de preferência antes da aula; prova antiga no começo; cor no plano com a seleção; E1 do tamanho da aula (calibração em outra conversa) | Claude | README; EXECUCAO; BANDEIRAS; FEEDBACKS |

## Feedback cruzado Claude × Codex

Davi repassa o feedback que dá a um executor para o outro ("pra os dois irem se calibrando com erros do outro"). Todo item aqui vale para **os dois**, não só para quem errou.

| Data | Sobre | Feedback de Davi | Regra para os dois |
|---|---|---|---|
| 24/09 | Codex (aula dele) | "cards autorais muito secos... tem que ser curtos, mas não sem vida" | Frente curta com contexto concreto (organismo/droga/contraste da aula), nunca uma definição seca; Extra com o porquê. README, "Autoral curto, mas com vida" |
| 24/09 | Claude (Antibióticos) | "foram muitos cards... aprende a discernir melhor" e, depois: "rosa não é o que a aula não traz, mas sim aquilo que ela traz e que não vale ser guardado a longo prazo. coisas que ela não traz saem do repertório... o que não dá é sair da aula" | O que a aula não trouxe **sai** (exceto o que provavelmente foi falado em aula). Rosa = da aula, sem valor a longo prazo. Sem subdeck "além". README "O que entra e o que é rosa" |
| 24/09 | os dois | "ao ir fazendo, tem que já pôr no Anki para eu poder revisar também" / "ainda não vejo a aula no anki" | Instalar logo depois do check **e sincronizar** (`sync`). README "Instalar cedo e sincronizar" |
| 24/09 | Claude (Antibióticos) | "agora sim gostei. faltou só o rosa" (havia 5 rosas em 112) | Marcar ativamente o rosa em toda aula: rótulos óbvios de classe, listas de nomes pouco usadas, limiares/terminologia, detalhe de toxicidade além do que o slide destaca. Ficou em 12/112 (~11%) |
| 24/09 | os dois | "só vejo o deck da uc08" | Faltava o deck-pai `NEBLI::UC03` (sobra da limpeza) e o Anki escondia o ramo. Criar todos os ancestrais depois de instalar e conferir a árvore. EXECUCAO passo 8 |
| 24/09 | os dois | "o que eu precisar fazer manualmente não pede, só não vamos fazer" | Nunca pedir passo manual; alternativa automática ou pular e registrar. README "Sem pedir trabalho manual" |
| 24/09 | os dois | "lembra que tem deck de referência externa também... faz um mapeamento do onde cada um pode entrar e como agrega... analisar os cards que repetem entre decks" | Descobrir acervos externos dinamicamente a cada aula. Mapa dos nove acervos e auditoria de identidade/perguntas entre sete decks estão em `arquivos-trabalho/deck-aula-inflamacao-aguda-2026-09-24/`. Antes de criar em aulas sobrepostas, procurar a nota viva e associá-la por tag se a pergunta for a mesma. |

## Calibração do pipeline (log por aula)

Ao fechar cada aula, registrar: executor, contagem (notas/cards; AnKing/outros/autorais; verdes/rosas), livro e capítulo consultados, custo aproximado, correções de Davi e a regra que mudou, com o arquivo onde ela foi gravada.

| Data | Executor | Aula | Resultado | Ajuste no pipeline |
|---|---|---|---|---|
| 25/09 | Claude | X4 Edema — ajuste pequeno 1 (cor) | Deck restaurado (36 cards) → 20 sem bandeira coloridos com motivo: 11 verdes, 9 azuis. Deck: 24 verdes, 12 azuis, 0 sem bandeira. Só flags; campos e agendamento conferidos iguais; sincronizado | Primeiro passo da calibração incremental (F-C20). 5 pares repetidos anotados para Davi decidir; nada removido. Motivos em `bandeiras.py`/`bandeiras-journal.jsonl` |
| 25/09 | Claude | X4 Edema e congestão — **piloto E1 + cards (reprovado, desfeito)** | Deck 36 → 24 cards (+2 compartilhados): 20 AnKing/21 cards, 3 autorais (12,5%), 15 autorais em PT do Codex removidos; 23 verdes, 3 azuis, 0 sem bandeira; E1 nova (9 subtópicos, 4.749 palavras, 13 p.) + Antes da aula + Resumindo; guia com 4 vídeos conferidos; APKG UC03 local verificado. Robbins não lido | Cor decidida no plano com motivo por card (primeira aula assim). Provas lidas antes do mapa. Frente causa → mecanismo (formato das provas) nos 5 mecanismos. Imagem errada do AnKing (noz-moscada = paracetamol) trocada pela do slide. Greek em texto cai em fonte substituta: usar modo matemático. Relatório em `REVISAO-DE-QUALIDADE.md` da pasta |
| 25/09 | Claude | C11 v2 Grand Round 2 | 53 → 67 cards: +9 AnKing (7 verdes), +3 autorais com lâmina, +2 associações, −1 autoral (LADA); 7 rosas de X11 migrados para azul | Davi: "refaz o deck do GR2 com base no que há no drive". Slides idênticos aos de 24/09; o ganho veio das lâminas só de imagem (lipotoxicidade, octeto da DM2, ilhota, AGE na membrana basal) e da prova GR 2024 (AGEs). Autoral de LADA excluído: nem slide nem caso sustentavam. Verso AnKing com erro factual ("amylin is derived from insulin") corrigido na cópia. Pasta de aula compartilhada por link baixa sem conector (`drive.usercontent.google.com/download?id=`); a pasta de provas é privada (401) |
| 25/09 | Claude | X11 Correlação patológica-radiológica 2 | 52 notas/71 cards: 58 AnKing, 2 Lightyear, 11 autorais (15%); 27 verdes, 7 rosas; 2 notas de X1 (veia porta, anastomoses portocava) associadas. Robbins ausente; StatPearls NBK470283 e NBK557460 conferiram os padrões de imagem. Pacotes UC03 (1.159 cards) e UC08 (365) regenerados localmente, verificados, sem upload. | Aula de caso com slide só de imagem (28/33 lâminas) e **slide inacessível nesta sessão** (sem conector do Drive, Chrome desconectado): recorte pelas legendas das 17 lâminas na E1 antiga. Autorais só na correlação de imagem (US/TC do hemangioma, fases, esteatose, CHC com washout, cirrose), com imagens de cards AnKing e crédito. Lightyear (anestesia) serviu de acervo para dupla irrigação e os quatro sítios colaterais. Removidos dos versos: link de venda Physeo, Mallory-Weiss, hipervitaminose A, hemangioma cerebral/sóleo. Relatório na pasta X11 |
| 24–25/09 | Claude | X10 Inflamação: início e resolução | 47 notas/61 cards: 49 AnKing, 12 autorais (20%); 14 verdes, 6 rosas; 25 notas de X2/Patogenicidade associadas | Sobreposição com X2 resolvida só por associação (nenhuma cópia duplicada). Autorais acima de 15% em PRR/TLR/NOD/RIG-I, NET e inflamação neurogênica, sem AnKing no nível da aula. Aplicado em 24/09, sincronizado em 25/09. Relatório na pasta X10 |
| 24/09 | Claude | X6–X9 (Patologia ambiental, Intestino grosso, Complemento, Intestinos BT) | contagens na coluna Estado da fila do Codex | Assumidas do Codex quando ele ficou sem tokens; Complemento e Intestinos refeitos do zero. Pastas `deck-aula-<slug>-2026-09-24/` |
| 24/09 | Codex | X5 Estrutura geral do estômago | 27 notas/35 cards: 24 AnKing, 7 Histology, 2 LLU Histology, 2 autorais visuais; 10 verdes, 1 rosa. Junqueira cap. 15 consultado; prova UC08 P1 não localizada. APKG UC08 local com 191 cards, sincronizado. Custo de API não medido. | Roteiro prático levou a duas ampliações antes do fechamento: célula mucosa do colo e transição esofagogástrica. Histology e LLU forneceram imagens inspecionadas. Nenhuma nota NEBLI equivalente para associar. Relatório na pasta X5. |
| 24/09 | Codex | X4 Edema e congestão | 30 notas/36 cards novos: 21 AnKing, 15 autorais; 1 nota/2 cards de X2 associados; 8 verdes, 3 rosas. Robbins cap. 4 indisponível; Clinical Methods e StatPearls consultados. APKG UC03 local com 789 cards, sincronizado. Custo de API não medido. | Slide dividido em duas aulas: só seção anterior a “Patologia Ambiental” entrou. Uma cópia de Budd–Chiari foi retirada por escopo antes do pacote final. Vídeo Osmosis consultado por legendas; acervos externos redescobertos e sem ganho líquido. Relatório na pasta X4. |
| 24/09 | Codex | X3 Esôfago, estômago e intestino delgado | 51 notas/60 cards novos: 13 AnKing, 31 AnatoKing, 12 Dope, 2 Dorian, 2 autorais; 1 nota de X1 associada; 8 rosas, 0 verdes. Netter pranchas 237–239, 276–279, 294; prova UC08 P1 não localizada. APKG UC08 local com 156 cards e sincronização concluída. Cerca de 22 min de execução; custo de API não medido. | Primeiro uso de AnatoKing copiado exigiu Header preenchido; retomada por journal sem duplicar os 12 AnKing já instalados. Corrigidas duas rosas inicialmente atribuídas às funções centrais dos esfíncteres. Relatório na pasta X3. |
| 24/09 | Claude | Grand Round 2 (DM) | 48 notas/53 cards novos (45 AnKing, 8 autorais = 15%); 16 verdes, 6 rosas; 15 notas da Integração II associadas | Aula de caso, deck compacto. Slides (43 lâminas) + caso clínico (DM1 tardio/LADA). Entraram: AGEs/RAGE, nefropatia, retinopatia, catarata, neuropatia, pé diabético, Charcot, osteomielite, escore de cálcio, angioTC × cateterismo, AVC na TC, exames do caso (HbA1c, frutosamina, peptídeo C, anti-GAD), GLP-1, insulinas basal/rápida, glucagon na hipoglicemia grave. Fora: fármacos por classe, metas e critérios de síndrome metabólica, manejo de cetoacidose, aortopatia. O PDF "Grand Round 2.pdf" em outra pasta é o guia de 2025 (mesmo caso); não ampliou o recorte (imunologia do GAD/perforina não está nos slides de 2026) |
| 24/09 | Claude | Motilidade I (UC08) | 25 notas/33 cards: 26 AnKing, 7 autorais (21%); 9 verdes, 2 rosas; 4 notas associadas | Slide curto (inervação intrínseca × extrínseca, plexos, reflexos curto/longo, ACh/VIP/NO, Chagas, tônica × fásica, esfíncteres, contração/relaxamento do liso). Acalasia entrou só como mecanismo da perda do plexo; diagnóstico e tratamento fora; versos de Chagas enxugados (chagoma/Romaña). Sem prova antiga de UC08 no banco; Margarida não aberta. O título diz "absorção", mas o slide não traz absorção |
| 24/09 | Claude | Motilidade II (UC08) | 40 notas/53 cards: 44 AnKing, 9 autorais (17%); 2 verdes, 6 rosas; 1 associada (grelina, do Codex) | Ondas lentas/Cajal/potenciais em pico, mastigação (V3), deglutição (fases, peristalse 1ª e 2ª), relaxamento receptivo, esvaziamento e hormônios (só papel motor: secretina, CCK, GIP, GLP, PYY, grelina, gastrina; secreção é P2), delgado, cólon, evacuação, vômito. Fora: MMC/motilina, fármacos antieméticos, doenças |
| 24/09 | Claude | Integração metabólica I | 37 notas/50 cards novos (41 AnKing, 9 autorais = 18%); 7 verdes, 6 rosas; 27 notas da Integração II associadas (mesma nota, dois tags) | A "transcrição" do Drive é transcrição real com as lâminas embutidas (86 p.); imagens dos autorais extraídas dela. Recorte: reservas por tecido, fígado (GLUT2/glicoquinase, PFK-1/F-2,6-BP, fosforilase regulada por glicose, aminoácidos→ureia, lipídios), músculo (epinefrina/AMP/Ca²⁺, fibras I/II, fosfocreatina, Cori), coração, adiposo (HSL, UCP1), cérebro, rim, hemácia, porta. Fora: estrutura do glicogênio, doenças de depósito, ciclo da ureia detalhado, síndrome metabólica (só citada no fim). Sem prova antiga classificada |
| 24/09 | Claude | Homem–ambiente–micro-organismo (microbiota) | 29 notas/35 cards: 20 AnKing, 15 autorais (43%); 11 verdes, 5 rosas; 6 notas de outras aulas associadas | Slide de microbiota (Profa. Carla Taddei, 43 lâminas). AnKing cobre a flora por sítio e vitamina K/IgA; não cobre residente × transitória, antagonismo, sucessão no recém-nascido, fator bífido, pró/prebiótico, teoria da higiene, disbiose → autorais com lâmina. Fora: DGGE/sequenciamento, eixo cérebro-intestino em detalhe, tabela de contagens por segmento. **Bug corrigido:** a tag `NEBLI::author::authored-<chave>` não é por aula; a chave 'antagonismo' colidiu com um autoral de Antibióticos (renomeada). Usar chaves com prefixo da aula |
| 24/09 | Claude | Controle microbiológico | 29 notas/30 cards: 18 AnKing, 12 autorais (40%); 0 verdes (tag FA de desinfecção é toda LowerYield), 4 rosas | AnKing tem só ~20 notas de desinfecção (First Aid 52); nada de pasteurização, filtração, UV, calor seco, cloro/HOCl, álcool 70% ou hierarquia de resistência, que são o núcleo do slide → autorais com a lâmina. MCAT sem nada. Fora: lâminas introdutórias 1-16 (microbiota, transmissão, crescimento), antibióticos. GBS: AnKing diz 36-38 semanas, slide 35-37 (nota no verso). Lister entrou no verso do card de Semmelweis. Trabulsi não aberto (PDF grande, conector) |
| 24/09 | Claude | Integração metabólica II | 115 notas/148 cards: 138 AnKing, 6 MCAT, 4 autorais (3%); 34 verdes, 15 rosas (10%) | O arquivo "transcrição" do Drive é o slide (49 lâminas). Recorte: insulina/glucagon, célula β, estado absortivo (glicoquinase, glicogênio, PFK-2, lipogênese, CPT-I), pós-absortivo e jejum (lipólise, gliconeogênese, alanina/glutamina, corpos cetônicos), DM1 × DM2 como a aula traz. Fora: fármacos, complicações crônicas, critérios diagnósticos, cetoacidose como manejo. Ciclo de Cori (lactato) fica para Integração I. **Achado:** o campo `Bootcamp` (e `Sketchy`) do AnKing é link de vídeo; tinha ficado em 273 cópias dos meus decks (Morfologia→Operon). Limpei todas com backup (`lote-.../before-limpar-links.json`). Regra: zerar todos os campos de recurso nas cópias. Harper ausente; slide cita Stryer e Marzzoco, não localizados |
| 24/09 | Claude | Operon em procariotos | 37 notas/57 cards: 13 AnKing, 25 MCAT, 19 autorais (33%); 0 verdes (nenhum HY literal no tema), 6 rosas; 1 associada (AT-rich, Genética) | AnKing só tem 7 notas de lac (CAP/glicose). O núcleo da aula (mutantes de Jacob-Monod, diploide parcial, cis/trans, IPTG/X-gal, σ −10/−35) não existe em AnKing nem MCAT: autorais acima de 15% por isso, todos com lâmina do slide. MCAT: links Khan Academy removidos do verso. Harper ausente; substituto OpenStax Biology 2e §16.2 (NCBI bloqueou por captcha). trp só como exemplo de co-repressor (no slide o tipo aparece sem nome); atenuação fora |
| 24/09 | Claude | Patogenicidade bacteriana | 141 notas/188 cards (174 AnKing, 14 autorais = 7%) + 19 notas de outras aulas associadas; 107 verdes, 27 rosas | A aula de 4 h tem 4 PDFs: virulência + estafilo/estrepto + BGP + BGN. Todos contam como "da aula". Fora: endocardite, Jones, vacinas, tratamento, algoritmos de laboratório (bacitracina/optochina), Actinomyces/Nocardia/antraz. Autorais com figura do slide (MSCRAMM, coagulase, Lancefield, tétano neonatal, quorum) |
| 24/09 | Claude | Morfologia bacteriana | 69 notas/99 cards: 85 AnKing, 2 MCAT, 12 autorais (8 notas); 37 verdes, 16 rosas; 5 associadas (Genética/Antibióticos) | 1ª aula feita já com a regra "só o que a aula traz": as 14 questões orientadoras do slide delimitaram o recorte. Endotoxina/sepse, algoritmos de identificação, vacinas e estrutura interna do esporo ficaram fora |
| 24/09 | Claude | Antibióticos (v3, final) | 85 notas/112 cards, todos da aula: 101 AnKing, 2 MCAT, 9 autorais (8%); 42 verdes, 5 rosas; 52 notas fora da aula removidas; sincronizado | Rosa corrigido (da aula, sem valor a longo prazo); o que a aula não trouxe saiu. Livro (Trabulsi) e figuras do slide não conferidos: exigiriam ação manual |
| 24/09 | Claude | Antibióticos (v2) | 137 notas/176 cards: 108 da aula + 68 além (rosa); 165 AnKing, 2 MCAT, 9 autorais (5%); 41 verdes, 69 rosas; 5 notas de Genética/Fisiologia associadas | 1ª versão com 178 cards sem separação → Davi: "não ficou claro o que é da aula". Erro: tratei Step 1 do mesmo assunto (toxicidades, inversos, espectros) como aula. Correção: escopo `aula`/`alem` em subdeck |
| 24/09 | Claude | — | fila aberta | lote só com deck; tamanho normal + rosa; apagados refeitos do zero; divisão por blocos Claude/Codex |
| 24/09 | Codex | X2 Patologia da inflamação aguda | 41 notas/60 cards: 48 AnKing, 12 autorais (8 notas); 1 nota anterior associada; 5 verdes, 8 rosas. Robbins ausente; StatPearls consultado. APKG UC03 local e sincronização concluídos. | Extras herdados fora do recorte removidos; figuras e tabela da aula sustentaram os autorais; nove acervos externos mapeados, nenhum com ganho líquido em X2; auditoria de 462 notas NEBLI sem duplicidade física entre decks. Ver relatório da corrida. |
| 24/09 | Codex | X1 Vascularização das vísceras | 52 notas/96 cards: 46 AnKing, 47 Dope, 2 Dorian, 1 autoral; 28 verdes, 13 rosas. Netter indicado pela aula, capítulo integral não consultado. APKG UC08 local verificado, sem upload. | Card Dope da gástrica direita excluído por contradição frente/Extra; dois AnKing de drenagem linfática retal acrescentados após revisão visual do slide 45. |
