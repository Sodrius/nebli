# Meta-análise — 33 apostilas históricas NEBLI

**Data:** 2026-05-25
**Escopo:** 33 PDFs em `resumos-gerados/apostilas-historicas/` cobrindo UC01 (Biologia Celular 9, Bioquímica 15, Fisiologia de membranas 8), UC02 (BMC 1), Ligas (TCP 1).
**Insumo:** 66 relatórios (33 Tier 2 Sonnet + 33 Tier 3 Opus) em `arquivos-trabalho/apostilas-historicas/`.
**Avaliadores:** revisor-pdf-didatico (Sonnet 4.6) + revisor-pdf-profundo (Opus 4.7), ambos rodando como `general-purpose` com `model` override + prompt inline.

**Achado mais importante de identidade:** dos 33 PDFs analisados, **todos são output do próprio pipeline NEBLI** (cabeçalho "NEBLI · APOSTILA", autor declarado "Davi Sousa — Turma 114"). Os "autores" rotulados no INDICE são os professores das aulas-fonte, não autores dos resumos. Isso transforma o exercício de "auditoria externa" em **auto-calibração do pipeline NEBLI** — o que aumenta o valor estratégico: todo erro é nosso, todo acerto é replicável.

**Limitação metodológica admitida:** 40 dos 66 relatórios reportam que a análise visual (T2.13, T3.8) ficou degradada porque o sandbox bloqueou `pdftoppm`. Os agents inferiram layout via metadata JSON (palavras/imagens/densidade por página) + legendas do .txt. Bugs visuais reportados são reais (todos confirmáveis por inspeção), mas a cobertura visual é incompleta — uma camada de polimento estético pode ter passado batida.

---

## 1. Sumário quantitativo

### Distribuição de vereditos

| Tier | APROVAR | APROVAR COM RESSALVAS/RESERVAS | BLOQUEAR |
|---|---|---|---|
| T2 didático (Sonnet) | **18** (55%) | **15** (45%) | 0 |
| T3 profundo (Opus) | 0 | **33** (100%) | 0 |

**Leitura:** Tier 2 aprova sem ressalvas mais da metade — o pipeline está sólido na superfície didática. Tier 3 reserva 100% — sempre há **algo** de mecanística, estrutura visual ou bug de pipeline a corrigir. Nenhum BLOQUEAR foi disparado: não há resumos catastróficos no corpus.

### Score médio T2 por slug (ranking)

**Top 8:**
- 4.50 — `LIGA-TCP`
- 4.50 — `UC01-FMEMB-03-potencial-de-repouso`
- 4.50 — `UC01-FMEMB-05-conducao-do-impulso-nervoso-e-potencial-de-acao`
- 4.50 — `UC01-FMEMB-08-sinalizacao-celular-i-e-ii`
- 4.40 — `UC01-BC-01-membrana-plasmatica`
- 4.40 — `UC01-BIOQ-05-proteinas-i`
- 4.40 — `UC01-FMEMB-01-compartimentos-e-homeostase`
- 4.40 — `UC01-FMEMB-04-propriedades-passivas-da-membrana-plasmatica`

**Bottom 8:**
- 4.10 — `UC01-BIOQ-10-enzimas-i`
- 4.10 — `UC01-BIOQ-13-carboidratos`
- 4.10 — `UC01-BIOQ-18-cadeia-respiratoria`
- 4.10 — `UC01-FMEMB-02-sistemas-de-transporte-na-membrana`
- 4.00 — `UC02-BMC-01-celulas-do-sangue`
- 3.90 — `UC01-BIOQ-04-aminoacidos`
- 3.80 — `UC01-BIOQ-16-gliconeogenese` ← marcado "resumo ruim" no nome original; confirmado mas só por **margem pequena** (3.80 vs média 4.22)
- 3.75 — `UC01-BC-20-estrutura-dos-acidos-nucleicos`

**Média geral T2:** 4.22 / 5. **Mediana:** 4.30. Distribuição compactada no quartil superior — o pipeline raramente desce, mas também não atinge 5 perfeito.

### Distribuição por disciplina

| Disciplina | n | Score médio | Observação |
|---|---|---|---|
| Fisiologia de membranas | 8 | **4.43** | Disciplina mais consistentemente alta |
| Biologia Celular | 9 | 4.17 | Boa, mas com piso mais baixo (BC-20 ácidos nucleicos) |
| Bioquímica | 14 | 4.15 | Mais densa — gliconeogênese e aminoácidos puxam para baixo |
| BMC (UC02) | 1 | 4.00 | n=1, dado isolado |
| Liga TCP | 1 | 4.50 | n=1, dado isolado |

**Leitura:** Fisiologia de membranas é onde o pipeline NEBLI está mais maduro — texto dialógico fluído, mecanismo antes do nome, conclusão integradora forte. Bioquímica é o eixo de maior carga cognitiva e por isso onde os defeitos mecanísticos mais aparecem.

---

## 2. Os 10 erros mais frequentes

Ranqueados por incidência cruzando os 66 relatórios. Cada um com nome curto, mecânica do erro, contagem de incidência (frequência X/33 com base em grep cruzando didáticos e profundos), e 3 citações literais de relatórios distintos.

### #1 — Paridade de distratoras E2 Aplicação quebrada (Q26–Q30) [28/66 menções, ~17/33 PDFs]

**Mecânica:** distratoras de Q26–Q30 saem com 10–15 palavras enquanto a correta tem 30–50. Ratio frequente: 1.5×–2.8× (limite canônico ≤1.25×). Aluno detecta a alternativa correta apenas por tamanho.

**Citações:**
- `UC01-BC-07-divisao-celular`: "Q28 com ratio 1,73 e Q30 com ratio 1,49"
- `UC01-BIOQ-08-hemoglobina-i-e-ii`: "Q26/Q28 com ratio ~1,4–1,6"
- `UC01-FMEMB-01-compartimentos-e-homeostase`: "Q26-Q30 Aplicação PRESENTE com ratios 2.4–5.2"
- `UC01-BIOQ-16-gliconeogenese`: "correta 70 palavras vs distratoras 25–30, ratio ≈ 2.8"

**Diagnóstico:** este é **o erro #1 do `errosComuns_nebli.md`** — confirmado massivamente. A regra "escrever as 5 distratoras ANTES da correta com 25-35 palavras de mecanismo plausível" não está sendo executada pelo QUESTIONADOR de forma consistente.

### #2 — Siglas/termos densos sem `#sigla()` na 1ª aparição [29/66 menções, ~17/33 PDFs]

**Mecânica:** NADH, ADP, Pi, cAMP, AMPc, CoA, NADP⁺, FAD, FADH₂, GDP, ENaC, Gs, AQP3, BiP, PIP3, PDE5, MBP, HbA1c — aparecem em prosa sem footnote `#sigla()` na 1ª ocorrência. Especialmente comum em cascatas de sinalização e metabolismo.

**Citações:**
- `UC01-BIOQ-15-introducao-ao-metabolismo`: "faltam Pi/CoA/NADH/FADH₂"
- `UC01-FMEMB-08-sinalizacao-celular-i-e-ii`: "cascatas RTK com 6 siglas novas sem footnote"
- `UC01-FMEMB-09-transporte-de-agua`: "ENaC/DP/Gs/AQP3/AQP10 sem `#sigla()`"
- `UC02-BMC-01-celulas-do-sangue`: "HbA1c, MBP, PDGF, ICAM, PTI, CIVD"

**Diagnóstico:** **erro #2 do `errosComuns_nebli.md`** — confirmado. O REDATOR-E1 declara siglas no início mas escapa em cascatas longas (sinalização, metabolismo). O cross-check `grep '#sigla(' etapa1.typ` proposto no errosComuns ainda não foi automatizado.

### #3 — Bug template "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" fantasma [13/66 menções]

**Mecânica:** após a remoção canônica da Etapa 4 em 2026-05-22, o helper de gabarito continuou imprimindo o header "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" em todos os PDFs gerados depois. Páginas afetadas: gabarito da E2.

**Citações:**
- `UC01-BIOQ-05-proteinas-i`: "Header da página do gabarito diz 'ETAPA 4 — QUESTÕES DE FUNDAMENTOS' (lixo de versão pré-2026-05-22)"
- `UC01-BIOQ-14-glicolise`: "página 58 (gabarito) ainda exibe header zumbi"
- `UC01-FMEMB-06-transmissao-sinaptica`: "header do gabarito ainda diz 'ETAPA 4 — FUNDAMENTOS'"
- `UC01-BC-07-divisao-celular`: "Header fóssil — página de gabarito ainda traz ETAPA 4"

**Diagnóstico:** bug determinístico do template (`nebli_v2_apostila.typ` ou helper `gabarito-page`). Fix de 1 linha. **Maior ROI de qualquer correção isolada** porque corrige 13+ PDFs já gerados em uma única edição de template.

### #4 — Gabarito da E2 em layout quebrado / colunas embaralhadas [16/66 menções]

**Mecânica:** o gabarito sai em grade 3-5 colunas com ordem zigue-zague: Q06 depois de Q08, Q11 fora da grade etc. Em alguns casos, classificação "Consolidação/Integração/Aplicação" sai trocada do corpo da E2.

**Citações:**
- `UC01-BC-07-divisao-celular`: "**gabarito errado em 13 de 30 questões objetivas (43%)** — bloqueador prático"
- `UC01-BIOQ-02-ph-e-tampoes`: "Gabarito (pág 41) embaralha ordem em 3 colunas — Q06/Q07 caem depois de Q08-Q10"
- `UC01-FMEMB-03-potencial-de-repouso`: "gabarito (pág 64) com layout de colunas quebrado (Q11/Q22/Q28 fora da grade)"
- `UC01-BIOQ-07-purificacao-de-proteinas`: "Q08 'líquida líquida', Q28 'recombinante recombinante alvo recombinante' triplicado"

**Diagnóstico:** o helper `gabarito-page` está com chunking quebrado quando contagens de categoria não são múltiplas de 5. Não é só estético: em UC01-BC-07 chegou a marcar a letra errada (gabarito impresso ≠ alternativa correta do enunciado) em 43% das questões — **risco pedagógico real**.

### #5 — Cadeia mecanística ≥5 atores sem figura [11/66 menções]

**Mecânica:** a regra canônica "cadeia ≥5 reações enzimáticas = figura obrigatória" está sendo violada em pontos críticos. Cascatas de sinalização (RTK → Ras → MAPK → ERK → fator de transcrição) e regulações (PFK-2/F-2,6-BP) aparecem como muros de prosa.

**Citações:**
- `UC01-BIOQ-11-enzimas-ii`: "cascata AMPc-PKA SEM figura (viola canônico)"
- `UC01-FMEMB-08-sinalizacao-celular`: "pág 18 sem figura (535 palavras, mais densa do PDF)"
- `UC01-BC-06-nucleo`: "figura de fluxo Ran-GTP/GDP ausente — viola regra canônica"

**Diagnóstico:** o REDATOR-E1 ou não tem figura disponível no `MAPA_CONTEUDO.txt` correspondente, ou esqueceu de chamar `#figura-nebli` no parágrafo. A solução é dupla: (a) ORQUESTRADOR garantir slide de cascata no MAPA; (b) REDATOR-E1 inserir SVG esquemático quando o slide não tem.

### #6 — Variação de registro homogênea entre subtópicos vizinhos [22/66 menções, T2.7]

**Mecânica:** subtópicos consecutivos abrem no mesmo registro (todos com pergunta ingênua direta, todos com analogia, todos com integração-anterior). O texto fica previsível a partir da metade da E1.

**Citações:**
- `UC01-FMEMB-06-transmissao-sinaptica`: "estrutura idêntica nas 9 seções torna leitura previsível a partir da metade"
- `UC01-BC-05-compartimentos-iii`: "tom dialógico é consistentemente bom, mas não muda de ritmo entre seções bioquímicas e casos clínicos graves"
- `UC01-BIOQ-17-ciclo-de-krebs`: "PARTE II tem registro repetitivo entre as etapas 3–8 (estrutura especular)"

**Diagnóstico:** o REDATOR-E1 internalizou "abertura por pergunta ingênua" como receita única em vez de rotacionar entre os 5 registros canônicos (enquadramento, integração-anterior, integração-posterior, analogia concreta, ponto-de-quebra).

### #7 — Conclusão integradora travada na camada 3 [13/66 menções, T2.9]

**Mecânica:** a `#conclusao-box` costura "estrutura → mecanismo → clínica" mas não atinge a 4ª camada (projeção para tema seguinte ou princípio unificador metabiológico). Quem usa a conclusão como revisão rápida perde o gancho narrativo para o próximo resumo.

**Citações:**
- `UC01-FMEMB-03-potencial-de-repouso`: "síntese clínica (digoxina, hipercalemia) fica nos boxes da E1 mas não reaparece na Conclusão"
- `UC01-BIOQ-14-glicolise`: "Conclusão sem camada clínica/projeção para Krebs"
- `UC01-BIOQ-04-aminoacidos`: "conclusão tem 3 camadas mas falta 4ª camada prospectiva ligando ao próximo resumo (proteínas I)"

**Diagnóstico:** o REDATOR-E1 não está incluindo a "promessa de continuidade" como item canônico da conclusão.

### #8 — Vocabulário de prova nos boxes ("cai na prova", "pegadinha") [10/66 menções, T2.6]

**Mecânica:** ainda aparecem boxes com voz prescritiva-de-prova em vez de mecanística. Frases típicas: "aparece todo ano em prova", "pegadinha clássica", "memorize o gesto físico", "regra de ouro para a P2", "dica clínica do hemograma".

**Citações:**
- `UC01-BIOQ-08-hemoglobina-i-e-ii`: "pegadinhas clássicas da P2 e do Enare"
- `UC01-BC-07-divisao-celular`: "aparece todo ano em prova — substituir por voz mecanística pura"
- `UC02-BMC-01-celulas-do-sangue`: "pegadinha em prova (p.22) e dica clínica do hemograma (p.19)"

**Diagnóstico:** regra canônica explícita no `redator-e1.md` (T2.6) mas violada em ~10 boxes do corpus. Bom candidato a check automático: `grep -i 'prova\|pegadinha\|examinador\|cai em' etapa1.typ` deve voltar 0.

### #9 — Pré-requisitos usados sem retomada de 1–2 frases [9/66 menções, T2.3]

**Mecânica:** ΔG/Lei de Laplace/Nernst/Ran-GTP/SRP/translocon/efeito Bohr aparecem sem âncora explícita de 1 frase. Aluno em dificuldade fecha o PDF para revisar pré-requisito.

**Citações:**
- `UC01-BIOQ-03-lipideos`: "Box SDR usa Lei de Laplace sem retocar tensão superficial"
- `UC01-FMEMB-05-conducao-impulso`: "screening eletrostático em §3.3 p.30"
- `UC01-FMEMB-03-potencial-de-repouso`: "derivação de Nernst introduz potencial químico/ln/zF sem justificar"

**Diagnóstico:** mesmo o REDATOR-E1 com baseline "aluno sabe pouco" deixa pré-requisitos cruzados sem ponte. Tema Card Seção C deveria listar pré-requisitos nominais com 1 frase pronta para colar.

### #10 — Numeração de página/sumário inconsistente / Etapa 4–5 fantasma [9/66 menções]

**Mecânica:** sumário lista "Etapas 4 e 5" que não existem no PDF (resíduo pré-canônico 2026-05-22). Numeração de pé mostra "44" em PDF de 41 páginas (helper conta páginas-fantasma da Etapa 4 removida).

**Citações:**
- `UC01-BIOQ-04-aminoacidos`: "sumário lista Etapas 4 e 5 que não existem no PDF (resíduo pré-canônico)"
- `UC01-BC-06-nucleo`: "pág 38 do PDF imprime '42' no rodapé (decorrência da remoção da Etapa 4 sem reset do contador)"
- `UC01-BIOQ-05-proteinas-i`: "Footer marca '44' mas PDF tem 41 páginas"

**Diagnóstico:** mesmo bug-família do #3 e #4 — template `nebli_v2_apostila.typ` ficou com hooks legados após remoção da E4. Fix conjunto em uma única revisão do template.

---

## 3. O que ficou bom — padrões replicáveis (extraído de T3.9)

Cada subagente Tier 3 listou ≥3 técnicas que o autor "fez bem". Cruzando os 33 relatórios profundos, 15 técnicas recorrentes — agrupadas em famílias:

### Família A — Aberturas didáticas

1. **Pergunta-pivô bactéria↔eucarionte** (vista em `BC-06-nucleo`, exemplar paradigmático de Cat 2 EXEMPLARES) — confronto procarioto×eucarioto explicita o "porquê" da estrutura nova.
2. **Pergunta ingênua "anti-óbvia"** (vista em `FMEMB-02-sistemas-transporte`) — "por que precisamos discutir transporte?" derruba a fantasia de obviedade antes de construir o mecanismo real.
3. **Abertura por desconstrução de expectativa do aluno** (vista em `FMEMB-01-compartimentos-homeostase`, p.3) — nomeia a fantasia ingênua e derruba em 1 frase.
4. **Abertura por contraste cotidiano duplo** (vista em `BIOQ-15-intro-metabolismo`) — "glicose no copo vs glicose na célula".
5. **Abertura por zoom em 3 níveis** (vista em `BIOQ-13-carboidratos`) — mesa → órgão → biosfera.
6. **Abertura por caricatura popular** (vista em `BIOQ-03-lipideos`) — derruba a caricatura "gordura é vilã" antes de classificar.
7. **Confusão-nomeada → mecanismo → batismo técnico** (vista em `BIOQ-04-aminoacidos`, zwitteríon) — nomeia a confusão, explica o mecanismo, e só então usa o termo técnico.

### Família B — Boxes de quebra de confusão

8. **Box anti-confusão com título-negação** ("Despolarização não é inversão", "Cinesina-Cresce/Dineína-Direto") — vista em `FMEMB-04-passivas`, `BC-02-citoesqueleto`. Padronizar como `#confusao-prevista()` ou regra canônica de título de box.
9. **Box de inversão de polaridade** ("aluno acha X — é exatamente o oposto") — vista em `BC-07-divisao-celular`. Particularmente útil em PFK-1, glucagon-insulina, regulação alostérica.
10. **Box anti-extrapolação imediatamente após o segundo subtipo** (não no fim da seção) — vista em `BIOQ-11-enzimas-ii`. Vacina contra o erro mental no momento exato em que ele se forma.
11. **Box-rescue para confusões antecipáveis** (vista em `BIOQ-02-ph-e-tampoes`, "Ka/pKa inversos") — virar helper canônico `#confusao-prevista()`.

### Família C — Conclusões e mini-resumos

12. **Mantra de 3 perguntas portáteis na conclusão integradora** (vista em `BIOQ-15-intro-metabolismo`) — "onde está o ATP? onde estão os elétrons? por que é espontâneo?". Permite o aluno autoavaliar.
13. **Promessa-resgate** (vista em `BIOQ-13-carboidratos`) — 3 ganchos concretos no intro + 3 respostas verbatim na conclusão.
14. **Hat-trick integrador** (vista em `FMEMB-09-transporte-agua`) — molécula → célula → órgão + ponte para temas vizinhos como camada 4.
15. **Mini-resumo encadeado com setas** (vista em `FMEMB-04-passivas`) — 2-4 linhas em cadeia causal ao fim de cada subseção; hoje NEBLI só faz Resumindo no fim.
16. **Resumindo aritmético com a conta visível** (vista em `BIOQ-14-glicolise`) — `4 − 2 = +2 ATP` ao fim de cada sub-tópico.

### Família D — Integração clínica

17. **Clínica injetada em 1 frase entre travessões** (vista em `BIOQ-04-aminoacidos`) — warfarina, loratadina em 8-12 palavras inline, não em box. NEBLI tende a guardar para Etapa 2 / clínica-box.
18. **Box farmacológico com cadeia mecanística completa** (vista em `BIOQ-08-hemoglobina`, `FMEMB-02-transporte`) — armadilha diagnóstica + conduta + diagnóstico definitivo em 4-6 linhas.
19. **Patologia em parágrafo único com cadeia causal completa** (vista em `BIOQ-05-proteinas-i`, anemia falciforme) — em vez de box, fluxo causal denso de 6-8 frases. Formalizar como regra `redator-e1.md`.
20. **Clínica-em-duas-pontas: defeito molecular + tecido vulnerável + por que ESSE tecido** (vista em `BC-06-nucleo`, progéria generalizada).

### Família E — Anti-jargão e ancoragem

21. **Nome formal no fim** (vista em `BIOQ-18-cadeia-respiratoria`) — função primeiro, nome técnico como recompensa. Canônico NEBLI executado com disciplina.
22. **Frase-âncora aforística ≤15 palavras** (vista em `FMEMB-08-sinalizacao`) — "Calmodulina é sensor, CaMKII é enzima". Mnemônico embutido no mecanismo.
23. **Fármaco-âncora inline** (vista em `BIOQ-04-aminoacidos`) — droga citada entre travessões sem virar box.

---

## 4. Análise visual transversal

Limitada por bloqueio do `pdftoppm` em 40/66 relatórios. Sinais robustos mesmo assim, via metadata JSON:

### 4.1 — Distribuição de figuras

- **Concentração em E1, deserto em E2/E3.** Padrão recorrente: 15–20 imagens nas 15–20 primeiras páginas; 0–2 imagens nas 15–25 páginas seguintes. Casos: `BIOQ-17-krebs` (zero figuras pp.28–51), `BIOQ-18-cadeia-respiratoria` ("deserto visual" pp.15–40), `BC-05-compartimentos-iii` (zero pp.22–43), `BIOQ-08-hemoglobina` (zero nas últimas 17 páginas).
- **Implicação:** as cascatas E2/E3 com 5+ atores deveriam ter pelo menos figuras esquemáticas, mas saem como prosa. Decisão editorial pendente.

### 4.2 — Tabelas com layout quebrado

Reportado em 11+ relatórios:
- `BIOQ-07-purificacao`: tabela das 3 cromatografias renderizada como ASCII com células quebradas.
- `BIOQ-11-enzimas-ii`: tabela 4 tipos p.7 com quebra horrenda da palavra "estacionária".
- `FMEMB-03-potencial-repouso`: tabela de concentrações iônicas com células deslocadas entregando dados errados ao aluno.
- `BIOQ-15-intro-metabolismo`: 4 cenários ΔH×ΔS×T em prosa corrida; pedia tabela 2×2.
- `FMEMB-09-transporte-agua`: tabela segmentar 3.1 quebrada.

**Diagnóstico:** o helper `#table()` Typst pode estar sendo usado com larguras `auto` que colapsam em conteúdos longos. Padronizar largura mínima por coluna.

### 4.3 — Resumindo em 2 páginas comprimido

Reportado em 6+ relatórios — quando o tema é denso (Krebs, glicólise, gliconeogênese, cadeia respiratória), o Resumindo de 1 página vira 2 com metade vazia ou aglomerado de fontes. Decisão canônica 2026-05-20 (Davi flexibilizou para 2 páginas) está sendo aplicada, mas o resultado visual é desigual.

### 4.4 — Capa com inconsistências

- `BIOQ-13-carboidratos`: capa exibe "Bloco: P2 — Função 1", violando regra explícita do `CLAUDE.md` ("Proibido no PDF qualquer página: bloco/prova").
- `BIOQ-14-glicolise`: "Glicólise" navy sobre fundo branco fora do banner — flutua visualmente.

**Diagnóstico:** o helper de capa está renderizando metadados YAML que deveriam estar suprimidos.

### 4.5 — Numeração de página dessincronizada

Reportado em 4+ relatórios — `BC-06-nucleo`, `BIOQ-05-proteinas-i`, `BIOQ-04-aminoacidos`. O rodapé conta páginas que existiram na Etapa 4 (removida em 2026-05-22) mas não estão mais no PDF.

---

## 5. Comparação com os 7 erros do `errosComuns_nebli.md`

| # | Erro | Status no corpus histórico | Diagnóstico |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | **PRESENTE em ~17/33 PDFs** | Erro recorrente, regra "5 distratoras antes da correta" não está sendo executada |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **PRESENTE em ~17/33 PDFs** | Erro recorrente, cross-check automatizado pendente |
| 3 | Subagentes Opus customizados loopando | **N/A** — fix aplicado 2026-05-25 não testado neste corpus | Fix carregado mas não validado em produção |
| 4 | Heredoc atômico ENAMETOOLONG | **N/A** — bug Windows, não detectável em PDF | Workaround documentado |
| 5 | `questao-ce` exige tupla | **AUSENTE no corpus** | Erro não-presente nos PDFs auditados (Davi pode ter corrigido na geração) |
| 6 | Termo-notas abaixo do alvo | **PARCIAL — ~8/33 PDFs abaixo de 6** | A maioria dos PDFs históricos está ACIMA do alvo (10-22 footnotes). O problema é heterogeneidade: alguns têm 3, outros 25 |
| 7 | Tema-card com teto E1 errado | **AUSENTE / parcial** — `BC-20`, `FMEMB-03`, `FMEMB-05`, `BIOQ-14` tocam ou ultrapassam o teto 22 com folga justificável | Erro raro com o teto canônico atual |

**Erros novos a incluir no `errosComuns_nebli.md` (Phase F detalha):**
- Header "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" fantasma no gabarito (bug template).
- Gabarito em layout de colunas embaralhadas / classificação fora-de-grade (bug helper `gabarito-page`).
- Cadeia ≥5 atores sem figura nas seções de cascata (regra canônica não executada).
- Vocabulário de prova nos boxes ("cai em prova", "pegadinha") — tem regra T2.6 mas continua vazando.
- Conclusão integradora travada na camada 3 (falta projeção/continuidade).
- Variação de registro homogênea entre subtópicos vizinhos (5 registros canônicos não rotacionam).
- Capa com metadados-bloco vazando (violação do `CLAUDE.md`).
- Distratoras das E2-Q26 a E2-Q30 saem 1.5–2.8× mais curtas que a correta.
- Numeração de página inflada (helper conta Etapa 4 fantasma).
- Pré-requisitos cruzados sem âncora de 1 frase (Lei de Laplace, Nernst, ΔG, Ran-GTP).

---

## 6. Recomendações priorizadas para os próximos resumos NEBLI

**Priorizadas por impacto × custo de correção:**

### Tier 1 — Bugs determinísticos do template (correção 1 linha cada, impacto em N PDFs)

1. **Apagar header "ETAPA 4 — QUESTÕES DE FUNDAMENTOS" do helper de gabarito.** Tocar 13+ PDFs com 1 edição em `typst-template/nebli_v2_apostila.typ`.
2. **Reset do contador de páginas após remoção da E4.** Atual: rodapé conta páginas-fantasma. Fix: usar `counter(page).update(<atual>)` no fim da E3.
3. **Suprimir bloco/prova/turma na capa.** Já é canônico no `CLAUDE.md` mas o helper de capa não está respeitando. 1 if no template.
4. **Corrigir chunking do gabarito.** Layout em 3-5 colunas embaralha quando contagens não são múltiplas. Refatorar para 1 coluna vertical com agrupador de categoria, OU forçar largura fixa.

### Tier 2 — Regras canônicas que existem mas vazam (atualizar prompts dos agents)

5. **Reescrever as 5 distratoras ANTES da correta, com 25-35 palavras de mecanismo plausível em cada.** Já está no `errosComuns_nebli.md`; precisa virar **gate hard** no QUESTIONADOR — script que falha o pipeline se ratio > 1.25.
6. **`grep -i 'prova\|pegadinha\|examinador\|cai em' etapa1.typ` deve voltar 0.** Adicionar ao `precompile-check.py` como T1.x bloqueante.
7. **`grep` de siglas usadas em prosa cruzado com `#sigla(` declarado.** Já proposto no `errosComuns_nebli.md`; implementar no `precompile-check.py`.
8. **Cadeia ≥5 atores SEM figura → bloqueio.** Heurística: contar `→`/`->`/`=>` em parágrafos da E1; se ≥4 sem `#figura-nebli` no parágrafo anterior, warn.

### Tier 3 — Novas regras editoriais a entrar no `redator-e1.md`

9. **Conclusão integradora obrigatoriamente em 4 camadas:** princípio → mecanismo → clínica → **projeção para o próximo resumo**. Hoje a 4ª camada é opcional; tornar obrigatória.
10. **Rotacionar 5 registros canônicos entre subtópicos vizinhos.** Adicionar ao prompt do REDATOR-E1: "subtópicos consecutivos NÃO podem abrir no mesmo registro; rotacione entre enquadramento, integração-anterior, integração-posterior, analogia, ponto-de-quebra".
11. **Box de quebra de confusão com título-negação.** Família B do §3 — codificar como sub-padrão do `#atencao-box` com helper `#confusao-prevista(titulo: "X não é Y", aluno_acha: ..., mecanismo: ...)`.
12. **Clínica inline entre travessões.** Família D do §3 — REDATOR-E1 pode (deve) citar fármacos/casos em 8-12 palavras inline, não só em boxes.

### Tier 4 — Novos exemplares positivos a entrar no `EXEMPLARES.md`

13. **Exemplar "Pergunta bactéria↔eucarionte"** (de `BC-06-nucleo`, p.3) — Cat 2.
14. **Exemplar "Mantra de 3 perguntas portáteis"** (de `BIOQ-15-intro-metabolismo`, conclusão) — Cat 12.
15. **Exemplar "Patologia em parágrafo único com cadeia causal completa"** (de `BIOQ-05-proteinas-i`, anemia falciforme p.18) — Cat 9 ou nova categoria.
16. **Exemplar "Resumindo aritmético"** (de `BIOQ-14-glicolise`, "4-2=+2 ATP") — Cat 8.

---

## 7. Apêndice — Tabela de relatórios

Todos os relatórios em `arquivos-trabalho/apostilas-historicas/`:

| Slug | Veredito T2 | Veredito T3 | Score T2 |
|---|---|---|---|
| LIGA-TCP | APROVAR | APROVAR COM RESERVAS | 4.50 |
| UC01-BC-01-membrana-plasmatica | APROVAR | APROVAR COM RESERVAS | 4.40 |
| UC01-BC-02-citoesqueleto | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.10 |
| UC01-BC-03-compartimentos-intracelulares-i | APROVAR | APROVAR COM RESERVAS | 4.30 |
| UC01-BC-04-compartimentos-intracelulares-ii | APROVAR | APROVAR COM RESERVAS | 4.30 |
| UC01-BC-05-compartimentos-intracelulares-iii | APROVAR | APROVAR COM RESERVAS | 4.30 |
| UC01-BC-06-nucleo | APROVAR | APROVAR COM RESERVAS | 4.30 |
| UC01-BC-07-divisao-celular | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.10 |
| UC01-BC-20-estrutura-dos-acidos-nucleicos | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 3.75 |
| UC01-BIOQ-02-ph-e-tampoes | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.30 |
| UC01-BIOQ-03-lipideos | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.10 |
| UC01-BIOQ-04-aminoacidos | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 3.90 |
| UC01-BIOQ-05-proteinas-i | APROVAR | APROVAR COM RESERVAS | 4.40 |
| UC01-BIOQ-06-proteinas-ii | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.30 |
| UC01-BIOQ-07-purificacao-de-proteinas | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.10 |
| UC01-BIOQ-08-hemoglobina-i-e-ii | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.10 |
| UC01-BIOQ-10-enzimas-i | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.10 |
| UC01-BIOQ-11-enzimas-ii | APROVAR | APROVAR COM RESERVAS | 4.30 |
| UC01-BIOQ-13-carboidratos | APROVAR | APROVAR COM RESERVAS | 4.10 |
| UC01-BIOQ-14-glicolise | APROVAR | APROVAR COM RESERVAS | 4.30 |
| UC01-BIOQ-15-introducao-ao-metabolismo | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.20 |
| UC01-BIOQ-16-gliconeogenese | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 3.80 |
| UC01-BIOQ-17-ciclo-de-krebs | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.20 |
| UC01-BIOQ-18-cadeia-respiratoria | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.10 |
| UC01-FMEMB-01-compartimentos-e-homeostase | APROVAR | APROVAR COM RESERVAS | 4.40 |
| UC01-FMEMB-02-sistemas-de-transporte-na-membrana | APROVAR | APROVAR COM RESERVAS | 4.10 |
| UC01-FMEMB-03-potencial-de-repouso | APROVAR | APROVAR COM RESERVAS | 4.50 |
| UC01-FMEMB-04-propriedades-passivas-da-membrana-plasmatica | APROVAR | APROVAR COM RESERVAS | 4.40 |
| UC01-FMEMB-05-conducao-do-impulso-nervoso-e-potencial-de-acao | APROVAR | APROVAR COM RESERVAS | 4.50 |
| UC01-FMEMB-06-transmissao-sinaptica | APROVAR | APROVAR COM RESERVAS | 4.40 |
| UC01-FMEMB-08-sinalizacao-celular-i-e-ii | APROVAR | APROVAR COM RESERVAS | 4.50 |
| UC01-FMEMB-09-transporte-de-agua | APROVAR | APROVAR COM RESERVAS | 4.20 |
| UC02-BMC-01-celulas-do-sangue | APROVAR COM RESSALVAS | APROVAR COM RESERVAS | 4.00 |
