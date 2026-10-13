# ESTADO-ATUAL — onde estamos (atualizar ao fim de cada deck)

Regras: [MEMORY](MEMORY.md). Como fazer: [EXECUCAO-DECK-AULA](flashcards/projeto/EXECUCAO-DECK-AULA.md). Histórico de levas, filas antigas e perguntas já resolvidas até 13/10: `arquivo/2026-10-13-reorganizacao/ESTADO-ATUAL.md` (consulta, não fila).

Ao concluir cada deck: atualizar **Retomar aqui**, **Quem está com o quê**, a **Fila** e as **Perguntas para Davi** (data · aula · pergunta · suposição adotada).

## Retomar aqui

- 13/10 — **Davi pediu agora: 62 Inflamação crônica** (Claude, em produção). Pendente da P1: Tab da aula 03 com 14 cards em `revisar`/desatualizado (limite de uso da sessão interrompeu; rodar `python3 -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc03-patologia-03-diagnostico-patologico"'`) e republicar o pacote da UC03 depois.

- **PRÓXIMA SESSÃO — começar por aqui (13/10, fim do dia):** (1) conferir `python3 -m nebli.explicacoes resumo` das 5 aulas da P1 (`revisar: 0`; rodar `gerar` de novo se sobrar) e `python3 -m nebli.gates` de 02, 03, 04, 05, 06 (esperado 56/56 ou 54/54 por aula) → `python3 -m nebli.artefatos entrega` não é necessário para essas: basta republicar o pacote (`python3 -m nebli.package_uc --uc UC03 --output arquivos-trabalho/pacote-uc03-<data>/NEBLI - UC03.apkg` + `nebli.entrega "UC03" --nome x --uc-apkg ...`) e sincronizar. (2) **09 Lesão celular**: corrida já aberta e com fontes lidas em texto (`arquivos-trabalho/deck-aula-uc03-pt09-lesao-celular-2026-10-13/`; lâminas Ib 27 e Ia 47, transcrições Ia/Ib, palavras-cruzadas e gabarito, bibliografia, em `fontes/turma/*.txt`). Falta: ver as lâminas, escrever `spec.py` com `ESCOPO` + `inventario.py` + `fontes-decl.json` e seguir EXECUCAO-DECK-AULA do passo 1. Prefixo livre sugerido: `pt09`; lesson `2026-uc03-patologia-09-lesao-celular`. Pasta pessoal da aula só tem “etapas 1 a 3” (material NEBLI, não é base), slides e transcrição. (3) Depois, a fila abaixo; ao fechar cada aula, relatar e seguir. (4) Quando Davi pedir: `python3 -m nebli.analise_prova "NEBLI::UC03::P2"` e `P3`; correções por `python3 -m nebli.enxuga <corrida> <nid>:<motivo>` (`--simular` antes; `--devolver <nid>` desfaz).
- 13/10 — **Regras novas desta sessão (F-20261013-CLAUDE-03):** Tab em texto corrido do princípio ao card (não mais quatro rótulos); `z` refaz (reiniciar o Anki); `ESCOPO` obrigatório no spec (`pre` confere princípio antes do detalhe); só questão de **prova** obriga card (apoio pode ser excluído com motivo); ciclo básico, sem semiologia/fisiopatologia elevada; análise do deck-prova/UC (`nebli.analise_prova`).

- 13/10 — **Análise da UC03 P1 aplicada** (F-20261013-CLAUDE-03; `arquivos-trabalho/analise-nebli-uc03-p1-2026-10-13/RELATORIO.md`): 403 → 296 notas, tirando detalhe acima do ciclo básico, clínica, exemplos e repetições (02: 75, 03: 79, 04: 81, 05: 65, 06: 43, contando compartilhados); 2 questões de prova devolvidas à 03 e 1 à 04. Tabs da P1 sendo regenerados no formato novo (texto corrido do princípio ao card). **Falta:** amostra dos Tabs novos, gates completos das 5 aulas, pacote da UC, sync. **Depois:** análise da P2 quando Davi pedir (ele relatou repetição e detalhe demais lá).

- **Próximo com Claude: UC03 P1 — 09 Lesão celular, necrose e apoptose** (Patologia; pasta pessoal `UC03/Patologia/09 - Lesão celular, necrose e apoptose`, turma `Patologia/Aula 03 - Mecanismos de Lesão Celular: Necrose e Apoptose`). Ainda sem corrida. Entra suspensa (aula antiga).
- 13/10 — **06 Correlação pato-radio 1 ENTREGUE** (Claude, direto, sem agente): `deck-aula-uc03-pr01-correlacao-pat-rad-1-2026-10-11`; 34 notas/41 cards (verde 25, azul 10, rosa 6; AnKing 18, autorais 23) + 9 compartilhados; suspensa; Tab 52/52; gates 56/56; `NEBLI - UC03.apkg` republicado (sha 3f1d1783…); sync feito.
- 13/10 — Ferramentas para economizar tokens (F-20261013-CLAUDE-01): `nebli.artefatos`, resumo curto no `package_uc`, vídeos dispensados aceitos pelos gates. Regras e roteiro reorganizados (F-20261013-CLAUDE-02).

## Quem está com o quê

| Executor | Aula / corrida | Estado |
|---|---|---|
| Codex | PT Inflamação granulomatosa (`deck-aula-uc03-pt-granulomatosa-2026-10-10`) | em revisão por Codex em 13/10, a pedido de Davi: mecanismo geral primeiro, menos especificidades e clínica ilustrativa (F-20261013-CODEX-02) |
| Codex | IM37 Inflamação — início e resolução (`deck-aula-uc03-im37-inflamacao-inicio-resolucao-2026-10-11`) | aberta; gates 20/52 |
| Codex | 62 Inflamação crônica (`deck-aula-uc03-pt62-inflamacao-cronica-2026-10-13`) | assumida a pedido de Davi após limite do Claude; concluir depois da revisão da granulomatosa |
| Claude | 09 Lesão celular | próxima (corrida aberta com fontes) |

Livre: 08 Reconhecimento imune inato fica para quem seguir a sequência de Imunologia (Codex, se continuar).

## Fila

1. **UC03 P1 (aulas antigas, entram suspensas):** 08 Reconhecimento inato · 09 Lesão celular · 10 Ação hormonal · 11 Acúmulos e adaptação · 12 RM · 13 Envelhecimento · 14 Declaração de óbito · 15 GR1 · 16 Regulação hormonal e massa corpórea · 17 Reconhecimento adaptativo · 18 Recombinação · 20 MHC · 22 Mecanismos efetores. Feitas: 02, 03, 04, 05, 06.
2. **UC03 P2 sem deck:** 40 Prática 3 (36 Prática 2 sem material).
3. **UC21** (caso + perguntas = verde; resto azul/rosa; amplo, foco em entender o caso e casos similares).
4. **UC02** (como as provas: muita lâmina para reconhecer + toda a teoria).
5. Análise do deck-prova (`nebli.analise_prova`) da UC03 P2 e P3 e revisão geral dos decks antigos pelas regras atuais (quando Davi pedir).
6. **UC01.**

Prova próxima de referência: UC03 P3 em 06/11 (grade da Turma A).

## Decks UC03 existentes (corridas)

P1: rd02 Diagnóstico radiológico · pt03 Diagnóstico patológico · rd04 Radiografia e US · rd05 TC · pr01 Correlação 1. P2: bq25 Integração I · mb27 Fisiologia bacteriana · mb28 Prática 1 · bm29 Operon · mb30 Controle microbiológico · im31 Complemento · mb32 Antibióticos · bq33 Integração II · mb34 Genética bacteriana · mb35 Patogenicidade · pt38 Inflamação aguda · mb39 Homem-ambiente · micro01 Morfologia · pat05 Edema (refação) · pat06 Ambiental · pr02 Correlação 2 · gr02 GR2 diabetes. P3: mb12 Fungos · im45 Linfócitos T · mb44 Micoses cutâneas · bm46 Eucariotos I · mb48 Micoses subcutâneas · im49 Células B · mb50 Micoses sistêmicas · bm52 Eucariotos II · bm54 RNAs não codificadores · gr03 GR3. UC19: fa01 Introdução. UC08: 9 aulas (P1/P2).

## Perguntas para Davi (abertas)

- 13/10 · 06 Correlação 1 · (1) Lâmina 22: os aglomerados de células no líquido pleural são de tumor ou reativos? Ficou sem card. (2) Broncograma aéreo (a apostila diz que cai; não está nas lâminas): incluir? (3) Da pneumonia lobar só hepatização vermelha e cinzenta (congestão e resolução fora): ok? **Suposição:** como está.
- 12/10 · Radiologia · Cards de reconhecer o método (RX, TC, US, RM) numa imagem? **Suposição:** não.
- 12/10 · Retiradas · 8 notas retiradas ainda com tag de outra aula (UC08 AN01/AN02/BT03/BT04, Operon): apagar ou devolver à aula? **Suposição:** mantidas suspensas.
- 10/10 · Micoses subcutâneas · Cards de “reconhecer sem legenda” com as fotos clínicas das lâminas? **Suposição:** não, até pedido.
- 10/10 · Complemento · Nomenclatura C4b2a da aula mantida (AnKing usa C4b2b; verso explica): ok? **Suposição:** sim.
- 10/10 · Operon · lacI<sup>S</sup> dominante (dedução, não está na aula) azul; consenso TTGACA/TATAAT rosa: ok? **Suposição:** sim.
- 09/10 · UC03 · A grade do drive é da Turma A; a árvore do Anki segue outra divisão (Fungos na P3). Sua turma é outra? **Suposição:** sigo a árvore do Anki e a data 06/11.

## Pendências conhecidas (não bloqueiam a fila)

- `nebli/tests/test_entrega.py` tem 1 falha anterior a 13/10 (arquivo `entrega.py` não alterado nesta sessão).
- Gate não confere Extra vivo × plano (observado em 11/10); `card-mirror` não acha o conjunto de calibração (ajustar caminho se voltar a ser usado).
- Micoses subcutâneas: cards de imagem G8 (linfocutânea, corpos escleróticos) exigem recortar lâminas, se Davi quiser.
- 113 comentários antigos aparecem como “pendentes” no canal por causa de marcadores CORRIGIDO antigos.
- Ideias de melhoria de 11/10 (add-on de um clique, estudo autorais × AnKing, pesquisa de ciência cognitiva para o Tab): `arquivo/2026-10-13-reorganizacao/PLANO-MELHORIAS-2026-10-11.md`; executar só sob pedido.
