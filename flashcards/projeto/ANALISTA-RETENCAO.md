# Analista de retenção — plano (30/09/2026, não construído)

Pedido de Davi: “um analista para me dizer se, a fim de melhorar a retenção, devo passar mais tempo num card, me forçando a lembrar … ou se preciso tentar pensar menos e fazer mais. analisando os dados de cada card saber isso ia ser bom. um mega agente que sabe analisar esse tipo de coisa (precisamos planejar/pesquisar na net sobre isso, no git, no mundo acadêmico, no reddit, mundo dos cards...)”.

Roda quando Davi pedir (sem monitor contínuo, Q081). Não muda agendador, opções nem cards por conta própria (Q074): entrega diagnóstico e sugestões; Davi decide.

## O que a pesquisa já diz (ponto de partida, a aprofundar)

| Achado | Implicação prática |
|---|---|
| [Pyc & Rawson 2009](https://andymatuschak.org/prompts/Pyc2009.pdf), retrieval effort hypothesis: recuperações difíceis **e bem-sucedidas** fixam mais que as fáceis. Nos experimentos, a dificuldade vinha de **intervalos maiores**, não de ficar mais tempo parado no card. | O esforço útil vem do espaçamento, que o agendador já cria. Forçar a lembrança vale enquanto ela está “quase vindo”. |
| [Kornell, Klein & Rawson](https://sites.williams.edu/nk2/files/2011/08/Retrieval-attempts-enhance-learning-regardless-of-time-spent-trying-to-retrieve.pdf): a **tentativa** de recuperar ajuda, independentemente de quanto tempo se passa tentando. | Travou sem pista? Virar, apertar De novo e aprender a resposta (Tab) rende mais que insistir por 30 s. |
| Comunidade Anki ([fórum](https://forums.ankiweb.net/t/how-long-for-each-active-recall/10798)): ~8–10 s por card em média; card que exige muito mais costuma estar mal formulado. | Tempo longo repetido é sinal do card (reescrever, dividir, explicar), não só do estudante. |
| FSRS ([FSRS Helper](https://github.com/open-spaced-repetition/fsrs4anki-helper), [Expertium: retention](https://expertium.github.io/Retention.html)): estima por card dificuldade (D), estabilidade (S) e probabilidade de lembrar (R) a partir do histórico. | O analista usa D/S/R como base e não reinventa o modelo de memória. |

Hipótese de trabalho, a testar nos dados de Davi: **esforço curto e honesto** (≈5–15 s tentando; sem progresso → virar), com a dificuldade vindo do espaçamento e a compreensão vindo da explicação do Tab. Não é conclusão até os dados dele mostrarem.

## Dados que existem no Anki (sem nada novo para Davi fazer)

- `revlog`: cada resposta com data, botão (De novo/Difícil/Bom/Fácil), **tempo gasto em ms**, intervalo antes/depois, tipo (aprendizado, revisão, reaprendizado, filtrado).
- FSRS, se ativo: D, S, R por card. Conferir no perfil vivo se o FSRS está ligado.
- NEBLI: bandeira, aula, origem (AnKing/autoral), comentários (`NEBLI_Comentario`) e registro de Tabs (`tab-log.jsonl`) de cada card.
- Limite em 30/09: só 116 respostas acessíveis, de um dia. As conclusões por card precisam de **3–6 semanas** de 30 novos/dia.

## Perguntas e como responder

1. **Por card:** classificar cada card revisado em
   - *Difícil que fixa*: tempo alto, acerto e intervalo crescendo → nada a mudar, é esforço bom;
   - *Travado*: tempo alto e erros repetidos (sanguessuga) → ver o Tab, reescrever ou dividir o card (Q084/Q085);
   - *Chute rápido*: tempo muito curto com erros → pouca tentativa, sugerir tentar mais antes de virar;
   - *Fácil demais*: sempre rápido e certo → candidato a azul ou a intervalos maiores (decisão de Davi).
2. **Geral:** o tempo gasto numa revisão prediz acerto na revisão seguinte, **controlando R do FSRS**? Comparar faixas de tempo (ex.: <5 s, 5–15 s, >15 s) quanto à retenção posterior e ao custo em minutos por card retido.
3. **Autoral × AnKing:** autorais têm mais tempo/erro? Se sim, é sinal de escrita pior (liga com o padrão F-20260930-CLAUDE-16).
4. **Tab:** cards em que Davi apertou Tab passam a errar menos depois? Mede o valor da explicação.

## Etapas

1. **Pesquisa dirigida (sessão própria):** artigos (retrieval effort, desirable difficulties, tempo de latência como medida de força da memória, testing effect em medicina), repositórios (open-spaced-repetition, fsrs-benchmark, SRS-analysis), Reddit r/Anki e r/medicalschoolanki, fórum Anki. Guardar fontes lidas e o que cada uma sustenta, sem citar o que não foi lido.
2. **Leitor de dados somente leitura** (`nebli/analise_retencao.py`): revlog + D/S/R + tags NEBLI → tabela por card e resumo geral. Testes com dados sintéticos.
3. **Agente “analista-retencao”** (`.claude/agents/`), que lê a saída, aplica os critérios acima e escreve para Davi um relatório curto: o que mudar no jeito de estudar, quais cards reescrever e com que confiança. Sem alterar a coleção.
4. **Primeira análise real** quando houver ≥ 3 semanas de histórico. Revisar critérios com os resultados e com o que Davi sentir estudando.

Estado: planejado; nenhuma parte construída. Pendência no MEMORY (Uso, entrega e ferramentas).
