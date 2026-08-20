# Relatório de fechamento — Reconhecimento inato (`imuno-02-reconhecimento-inato`)

PDF: `resumos-gerados/IMUNO-02-RECONHECIMENTO-INATO.pdf` (42 páginas · 6,7 MB) · cópia leve: `resumos-gerados/leves/` (1,95 MB, 3,4× menor).
Estrutura: capa p1 · sumário p2 (1 pág.) · **E1 p3–p24 (22 págs., no teto)** · Resumindo p25 (1 pág.) · E2 p26–p39 · E3 p40–p42 · gabarito consolidado p42.

## Gates técnicos

| Gate | Resultado |
|---|---|
| `precompile-check.py` (9 validações + 4 regras da E2) | **0 erros**, 1 warning |
| Paridade Q01–Q30, banda dupla 0.80–1.25 | **30/30 PASS** — média 1.07, máx 1.23, mín 0.91 |
| C/E sempre 4 itens (I–IV) | 10/10 OK |
| Mapa de Confusões (≥4 por subtópico) | 12 subtópicos × 5 confusões = **60** |
| `verificar_gabarito_resumo.py` | gabarito consistente com `etapa2.typ`, 0 avisos |
| `auditar_pdf.py` | 0 erros — acentuação 3,4–3,9%, 17 paths de figura existem, Merriweather+Montserrat embarcados (8 faces) |
| `pos_pipeline_check.py` | 0 erros — sem fóssil de E4, capa sem bloco/prova, numeração coerente, sem página em branco |
| Validação visual (capa, E1 c/ figura, Resumindo, gabarito) | OK |

**Warning não-bloqueante:** "palavras E1: 669". **Falso-positivo do script** — `check_palavras_e1` delimita o miolo pela primeira ocorrência de "Resumindo", e o helper `#mini-resumo` imprime "Resumindo até aqui:", cortando a contagem no 1º mini-resumo (p5). E1 real ≈ 6,8 mil palavras em 22 páginas.

## Paridade Q01–Q30 (correta ÷ maior distratora)

```
Q01 33/31=1.06 PASS   Q02 29/30=0.97 PASS   Q04 27/29=0.93 PASS   Q05 31/34=0.91 PASS
Q07 31/30=1.03 PASS   Q08 32/29=1.10 PASS   Q10 29/29=1.00 PASS   Q11 31/32=0.97 PASS
Q13 34/30=1.13 PASS   Q14 30/27=1.11 PASS   Q16 28/28=1.00 PASS   Q17 34/32=1.06 PASS
Q19 32/30=1.07 PASS   Q20 28/28=1.00 PASS   Q22 32/30=1.07 PASS   Q23 30/28=1.07 PASS
Q25 27/28=0.96 PASS   Q26 32/31=1.03 PASS   Q27 28/30=0.93 PASS   Q29 30/31=0.97 PASS
Q03·Q06·Q09·Q12·Q15·Q18·Q21·Q24·Q28·Q30 — C/E, paridade não se aplica
```
Nenhuma remediação foi necessária (ordem invertida de redação funcionou de primeira: distratoras 25–35 palavras escritas antes da correta).

## Gabarito — sorteio e guarda anti-degeneração

Sorteio real por script com guarda. MC: **A=6 · B=4 · C=3 · D=4 · E=3** (máx 30%, teto ~40%). Nenhuma corrida ≥4 letras iguais. C/E: nenhuma string degenerada (sem CECE/ECEC/CCCC/EEEE), sem bloco de 5 C ou 5 E ao longo das 10 strings. A guarda só reposicionou a correta entre alternativas equivalentes — nenhuma resposta foi engenheirada para caber numa letra.

## Formatos da E2

20 múltipla escolha · **10 Certo/Errado** (Q03, Q06, Q09, Q12, Q15, Q18, Q21, Q24, Q28, Q30 — 1/3 das 30, distribuídas pelas três categorias) · **3 "assinale a incorreta"** (Q05, Q14, Q22, com `*incorreta*` sinalizado no stem).

## Tabela auditável de figuras

| Figura | PARTE | Origem | Mecanismo que carrega | Largura |
|---|---|---|---|---|
| slide-03 | I (1.1) | slide do professor | repertório completo **porque** aleatório → exige seleção | 55% |
| slide-05 | I (1.2) | slide | o mesmo reconhecimento se abre em 2 desfechos; estado homeostático decide | 62% |
| slide-07 | I (1.3) | slide | APC leva antígeno **e** laudo do tecido ao órgão linfoide | 64% |
| slide-06 | I (1.3) | slide | mapa orientador: PRR/inata × receptor clonal/adquirida, com a ponte | 74% |
| slide-08 | I (1.4) | slide | 6 famílias de PRR pelo eixo **localização** → DAMP/PAMP convergem | 80% |
| slide-09 | II (abertura) | slide | mapa orientador das 4 estratégias efetoras | 70% |
| slide-10 | II (2.1) | slide | IFN protege o **vizinho**, não a produtora | 62% |
| slide-11 | II (2.2) | slide | 3 tempos da citotoxicidade; efetora sai íntegra | 74% |
| slide-12 | II (2.3) | slide | 7 etapas da fagocitose, cada uma um problema mecânico distinto | 68% |
| slide-13 | II (2.4) | slide | 3 classes de mediador com mecanismos distintos | 58% |
| slide-14 | II (2.4) | slide | padrão de nomenclatura das citocinas (referência, não decoreba) | 55% |
| slide-16 | III (3.1) | slide | ligantes típicos dos TLR — leitura pela coluna da localização | 80% |
| slide-17 | III (3.1) | slide | RLR/NLR citoplasmáticos × CLR de membrana, mesma lógica | 76% |
| slide-18 | III (3.2) | slide | cruzamento MyD88/TRIF e o leque de desfechos | 78% |
| slide-19 | III (3.3) | slide (artigo) | demonstra o **cruzamento**, não os nomes — por isso menor | 58% |
| slide-20 | III (3.4) | slide | NOD→NF-κB × NLRP/IPAF/AIM2→plataforma | 74% |
| slide-21 | III (3.4) | slide | montagem do NLRP3 e a cadeia sinal→caspase-1→clivagem→liberação | 70% |

**Larguras recalibradas deliberadamente** após a 1ª compilação (E1 saía com 23 páginas, 1 acima do teto): não foi corte cego, foi re-justificação por peso de conteúdo — tabelas densas e o esquema-mecanismo mantidos em 74–80%; esquemas médios rebaixados a 55–68%. Resultado: 22 páginas exatas.

**Figuras descartadas pelo filtro de utilidade pedagógica (regra 15):** slide-01 (capa da aula, sem mecanismo), slide-02 (objetivos do tema — meta-conteúdo), slide-04 (redundante com slide-03, mesmo mecanismo), slide-15 (citação de Ehrlich de 1908 — bonita, mas é história da ciência sem mecanismo verbalizável), slide-22 ("Em resumo" — o conteúdo virou o último parágrafo de 3.4 e a conclusão integradora, em prosa).

## Cobertura E1 → E2 (tabela subtópico → questões)

| Subtópico | Questões que o cobrem | n |
|---|---|---|
| 1.1 Receptor pronto e receptor sorteado | Q01, Q04, Q18, Q19 | 4 |
| 1.2 O que decide entre tolerar e responder | Q11, Q23, Q29 | 3 |
| 1.3 A ponte da apresentação de antígenos | Q14, Q23, Q29 | 3 |
| 1.4 DAMP, PAMP e as famílias de PRR | Q03, Q11, Q13, Q14, Q15, Q22 | 6 |
| 2.1 Salvar o vizinho: interferons do tipo I | Q08, Q12, Q25, Q28, Q30 | 5 |
| 2.2 Eliminar a célula doente: citotoxicidade | Q05, Q13, Q18 | 3 |
| 2.3 Limpar a área: a fagocitose em etapas | Q06, Q15, Q16, Q20, Q27 | 5 |
| 2.4 Chamar socorro: citocinas e febre | Q09, Q20, Q21, Q24, Q25 | 5 |
| 3.1 Os toll-like receptors e onde eles moram | Q01, Q02, Q11, Q19, Q22 | 5 |
| 3.2 Do ligante ao núcleo: MyD88 e TRIF | Q07, Q12, Q17, Q30 | 4 |
| 3.3 Por que a mesma via dá saídas diferentes | Q12 (item III), Q21 | 2 |
| 3.4 O inflamassoma e a maturação da IL-1β | Q10, Q17, Q24, Q26 | 4 |

Todos os 12 subtópicos ≥2. **3.3 saiu com 1 na 1ª passada** e foi corrigido antes de fechar: o item III de Q12 (que duplicava conteúdo de inflamassoma já testado em Q10/Q17/Q26) foi trocado por um item sobre o leque de desfechos de um mesmo receptor — o "truque do 4º item de C/E" previsto no `ROLES.md`.

## Passe de aprofundamento da E1 — 12 injeções (≈1 por subtópico)

| Subtópico | Aprofundamento injetado |
|---|---|
| 1.1 | por que alvos "indescartáveis" (LPS, flagelina, dsRNA) tornam um repertório fixo suficiente |
| 1.2 | tolerância é aprendizado ativo e por isso **reversível** — a lógica de retirar o freio do linfócito antitumoral |
| 1.3 | como o "laudo" viaja fisicamente: PRR ligado → coestimulação alta + programa de migração |
| 1.4 | exemplos concretos de DAMP: ATP extracelular, urato, DNA mitocondrial com herança CpG bacteriana |
| 2.1 | lógica temporal — IFN compra os dias de que a adquirida precisa; falha isolada da via = suscetibilidade viral |
| 2.2 | apoptose contém o conteúdo e por isso **não** gera nova onda de DAMP num tecido já inflamado |
| 2.3 | NADPH-oxidase e doença granulomatosa crônica: perder só a última etapa anula o resultado |
| 2.4 | mediadores lipídicos dispensam transcrição (segundos); anti-IL-6 e CSF como terapêutica |
| 3.1 | **por que** os sensores de ácido nucleico são endolisossomais — a localização é o mecanismo de discriminação do próprio |
| 3.2 | MyD88 não toca fator de transcrição: IRAK → TRAF6 → NF-κB; e o HIV mirando o NF-κB como medida de centralidade |
| 3.3 | anatomia do citoplasma; dois ligantes da mesma classe no mesmo TLR dão respostas distintas |
| 3.4 | exigência dos dois sinais como trava de segurança; ganho de função em NLRP3 e o eixo do urato na gota |

Fonte do calibre: sem Anki vivo nesta corrida (sessão remota, sem AnkiConnect em localhost). O aprofundamento nasceu do slide + das duas referências que o próprio professor projetou (Takeuchi & Akira 2010; Schroder & Tschopp 2010) + Abbas/Janeway.

## Índice de completude (0–10)

| Eixo | Nota | Justificativa em 1 linha |
|---|---|---|
| **E1 × slide** | **9** | Os 22 slides com conteúdo estão cobertos (inclusive a recapitulação 3–7 e a tabela de ligantes), e as 12 injeções levam a E1 um degrau além sem sair do recorte da aula. |
| **E2 × E1** | **9** | 12/12 subtópicos com ≥2 questões, mediana 4,5; nenhum subtópico órfão e nenhum conceito da E2 fora da E1. |
| **Cards × E1** | **n/a** | Não avaliável nesta corrida — sem AnkiConnect no ambiente remoto; nenhum card foi curado, selecionado ou aplicado. |

**Fontes → E1: 22/22 slides com conteúdo incorporados** (5 descartados pelo filtro de figura continuam cobertos em prosa).
**E1 → cards: não medido** (deck-aula pendente, ver abaixo).

## Densidade por PARTE (paridade ≤ ±20%)

PARTE I ≈ 2 350 palavras (4 subtópicos) · PARTE II ≈ 2 400 (4) · PARTE III ≈ 2 100 (4). Desvio máximo em relação à média: **−7%**. Dentro da faixa.

## Erros recorrentes do `ERROS.md` checados

1 paridade banda dupla ✔ · 2 siglas com `#sigla` (25 declaradas) ✔ · 3 sem subagente Opus ✔ · 4 heredoc (Linux, sem ENAMETOOLONG) ✔ · 5 `questao-ce` com tuplas ✔ · 6 termo-notas: **8** (homeostasia, citotoxicidade celular, desgranulação, quimiotaxia, opsonização, explosão respiratória, pleiotrópicas, inflamassoma) ✔ · 7 teto 22 declarado ✔ · 8 sem `#etapa-header` duplicado ✔ · 9 gabarito column-major conferido visualmente ✔ · 10 sem fóssil de E4 ✔ · 11 numeração coerente (42/42) ✔ · 12 cadeia ≥4 setas com figura adjacente ✔ (slide-18 foi reposicionado para ficar colado à caixa MyD88/TRIF) · 13 conclusão em 4 camadas ✔ · 14 registros rotacionados, nenhum par vizinho igual ✔ · 15 sem markdown bold ✔ · 16 boxes dentro da cota (PARTE I: 1 gold + 1 vermelho; PARTE II: 0 + 2 clínicas; PARTE III: 1 gold + 1 vermelho + 1 clínica) ✔ · 18 mapa de Integração gravado antes da redação ✔ · 19 título da capa (20 chars → 30pt, cabe na faixa) ✔ · 20 nenhum `#termo-nota` com termo repetido na prosa ✔

Auto-check de perguntas terminais na E1: **0** (`grep -cE '\?$'`). Nenhuma pergunta âncora/retórica.

## Pendências desta corrida

- **Deck-aula não montado.** O passo 11 do `/resumo` (curadoria AnKing → externos → NEBLIcards → `montar_deck_aula.py` → sync) exige AnkiConnect em `localhost`, inalcançável de sessão remota. O pedido foi "roda as etapas 1 a 3", que o PDF entrega por inteiro; o deck fica para uma corrida na máquina do Davi.
- **`typst` e `poppler-utils` não vinham no container remoto** — instalados nesta sessão (typst 0.13.1 via release musl; poppler via apt). Se o ambiente remoto for usado de novo, vale um hook de SessionStart.
- **Falso-positivo em `auditar_pdf.check_palavras_e1`** (colisão de "Resumindo até aqui:" do `#mini-resumo` com o delimitador "Resumindo"): candidato a correção de 1 linha no script — buscar `"Resumindo\n"` ou o banner, não a substring solta.
- **Header em atraso na 1ª página de cada etapa** (p3 mostra "SUMÁRIO", p42 mostra "ETAPA 3"): comportamento de `state().get()` do Typst, pré-existente no template. Não tocado — mudança no `typst-template/` exige aval do Davi com amostra antes/depois.
