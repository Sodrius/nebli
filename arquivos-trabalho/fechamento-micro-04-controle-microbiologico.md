# Relatório de fechamento — micro-04-controle-microbiologico

**Resumo:** Controle do crescimento microbiano — esterilização, desinfecção e antissepsia
**Slide:** Profa. Elisabete Vicente (Bete), Dep. Microbiologia ICB/USP, 2023 · 34 páginas
**Dial:** `profundidade: fundo` (pedido: "acima do nível da prova")
**PDF:** `resumos-gerados/MICRO-04-CONTROLE-MICROBIOLOGICO.pdf` — 47 páginas · 78,8 MB
**Cópia leve:** `resumos-gerados/leves/…` — 3,74 MB (21,1× menor)

## Estrutura entregue

capa (1) · Antes da aula (2, p2–4) · sumário (1) · **E1 = 21 páginas** (p6–26, dentro do teto de 22) · Resumindo (1 página, 9 seções) · E2 30 objetivas (p28–44) · E3 5 discursivas (p45–47) · gabarito consolidado.

E1: 3 PARTES · 15 subtópicos · 9.255 palavras de miolo (≈617/subtópico) · 15 figuras, todas do slide.

## Gates técnicos

| Gate | Resultado |
|---|---|
| `precompile-check.py` | 0 erro, 0 warning |
| `auditar_pdf.py` | 0 erro, 0 warning (acentuação 4,25–4,65%; 15 paths de figura existem; Merriweather+Montserrat embarcados; 9.255 palavras na faixa) |
| `pos_pipeline_check.py` | OK (sem fóssil de E4, capa sem bloco/prova, numeração coerente 47/47, sem página em branco) |
| `verificar_gabarito_resumo.py` | OK — 30 itens, 0 aviso |
| `check_pre_aula` | OK — 1.081 palavras, 87 termos plantados, 0 interrogação |
| `check_ce_quatro_itens` | OK — 10 C/E, todas com 4 itens |
| Vocabulário banido | 0 ocorrência em E1/Resumindo |
| Mapa de confusões | 15 subtópicos, ≥4 confusões cada (75 no total) |

## Paridade de distratoras — Q01–Q30 (banda dupla 0,80–1,25)

**20/20 múltipla escolha PASS.** Média 1,01 · mínimo 0,87 (Q30) · máximo 1,14 (Q01). Nenhuma remediação necessária.
As 10 C/E não entram na banda (regra canônica); a sequência de cada uma foi decidida item a item **depois** da redação, conforme `ERROS.md` #23.

```
Q01 C 41p | dist [30,33,34,36] | 1.14   Q16 C/E  EECC
Q02 C/E  CECC                            Q17 E 36p | [32,33,34,36] | 1.00
Q03 B 38p | [36,36,36,39] | 0.97         Q18 B 33p | [31,33,33,34] | 0.97
Q04 C/E  CEEC                            Q19 C/E  ECCE
Q05 E 37p | [32,32,32,34] | 1.09         Q20 C 35p | [28,30,32,33] | 1.06
Q06 D 36p | [35,35,37,40] | 0.90         Q21 D 35p | [32,32,33,34] | 1.03
Q07 C/E  CCEC                            Q22 C/E  ECCC
Q08 A 37p | [29,32,33,33] | 1.12         Q23 B 33p | [29,31,34,36] | 0.92
Q09 C 35p | [35,36,37,38] | 0.92         Q24 E 37p | [29,30,33,34] | 1.09
Q10 C/E  CCEE                            Q25 C/E  CEEE
Q11 E 37p | [32,33,34,38] | 0.97         Q26 C 37p | [30,33,34,36] | 1.03
Q12 B 35p | [29,31,31,32] | 1.09         Q27 B 32p | [30,31,33,35] | 0.91
Q13 C/E  CCEC                            Q28 C/E  CCEE
Q14 D 31p | [29,33,33,34] | 0.91         Q29 D 33p | [30,31,32,33] | 1.00
Q15 A 33p | [31,32,32,34] | 0.97         Q30 A 33p | [35,35,36,38] | 0.87
```

**Gabarito MC:** A=3 · B=5 · C=4 · D=4 · E=4 (máx 25%, teto ~40%). Maior corrida = 2.
**Gabarito C/E:** 23 C · 17 E (57/43). Nenhuma sequência CCCC/EEEE/CECE/ECEC. Dois pares repetidos (Q07=Q13=CCEC; Q10=Q28=CCEE) — não degenerado, declarado aqui.

## Tabela auditável de figuras

| Figura | PARTE | Origem | Mecanismo que carrega | Largura |
|---|---|---|---|---|
| 1 | I (1.1) | slide-21 | Sequência limpeza → rinsagem → desinfecção → rinsagem em corte lateral: por que a ordem é obrigatória | 60% |
| 2 | I (1.2) | slide-31 | Estático × cida + as 4 variáveis (espectro, concentração, tempo, toxicidade) | 56% |
| 3 | I (1.4) | slide-09 | Escada de resistência completa + classes químicas eficazes em cada faixa | 74% |
| 4 | II (2.1) | slide-06 | Desnaturação reversível (leite) × irreversível (ovo) — por que tempo e temperatura são acoplados | 62% |
| 5 | II (2.2) | slide-10 | Autoclave e forno com os dois pares tempo-temperatura | 66% |
| 6 | II (2.2) | slide-11 | Indicador biológico (ampola + tira de esporos) × fita termossensível | 68% |
| 7 | II (2.3) | slide-15 | Flambagem, fervura e pasteurização — os calores que não miram esterilidade | 60% |
| 8 | II (2.4) | slide-13 | Gama, micro-ondas, UV e o espectro com a faixa microbicida 200–300 nm | 72% |
| 9 | II (2.5) | slide-14 | Filtração de líquido (bactérias íntegras retidas na membrana) + cabine com filtro de alta eficiência | 70% |
| 10 | II (2.5) | slide-18 | Cascata 5 → 1,2 → 0,22 µm em vista explodida: por que existem pré-filtros | 44% |
| 11 | II (2.6) | slide-17 | Dessecação, liofilização e a escala 4 °C → −196 °C | 66% |
| 12 | III (3.1) | slide-27 | Protocolo de superfície lido como sequência ("após a limpeza" em toda linha) | 68% |
| 13 | III (3.2) | slide-26 | Classes × concentração de uso × nível de atividade | 64% |
| 14 | III (3.4) | slide-22 | Semmelweis: o experimento natural que fundou a antissepsia (12,24% → 1,27%) | 58% |
| 15 | III (3.5) | slide-12 | Esterilizador por plasma de H₂O₂ — o quarto estado da matéria em atividade | 62% |

**Figuras descartadas pelo filtro de utilidade pedagógica:** `slide-01`/`slide-20` e `slide-07` (fotografia de pira de corpos humanos, febre amarela em Cuba, séc. XIX) — conteúdo histórico legítimo no slide, gratuito no PDF; a incineração é ensinada em prosa. `slide-16` (pasteurização), `slide-24`/`slide-25` (valor D), `slide-03`, `slide-19`, `slide-32`, `slide-33`, `slide-34`: slides de texto puro sem mecanismo visual — o conteúdo entrou como prosa, e o valor D virou tabela nativa. `slide-08` (trituração por micro-ondas) e `slide-29`/`slide-30` (montagens de produtos): baixa carga mecanística.

## Tabela subtópico → questões (cobertura da E1 na E2, piso ≥2)

| Subtópico | Questões | n |
|---|---|---|
| 1.1 Quatro promessas | Q01, Q15, Q24 | 3 |
| 1.2 Estático e cida | Q02, Q19, Q24 | 3 |
| 1.3 Valor D / morte logarítmica | Q03, Q10, Q12, Q24 | 4 |
| 1.4 Escada de resistência | Q04, Q09, Q11, Q19, Q20 | 5 |
| 2.1 Desnaturação | Q05, Q12 | 2 |
| 2.2 Autoclave e forno | Q06, Q10, Q11, Q23, Q25, Q30 | 6 |
| 2.3 Chama, fervura, pasteurização | Q11, Q12, Q29 | 3 |
| 2.4 Radiação | Q13, Q14 | 2 |
| 2.5 Filtração | Q07, Q13, Q15 | 3 |
| 2.6 Frio, dessecação, liofilização | Q16, Q29 | 2 |
| 3.1 Limpar antes | Q17, Q21, Q28 | 3 |
| 3.2 Níveis e Spaulding | Q18, Q19, Q28 | 3 |
| 3.3 Classes químicas | Q08, Q09, Q17, Q20, Q21, Q27 | 6 |
| 3.4 Antissepsia | Q22, Q27 | 2 |
| 3.5 Termossensível / esporocida ≠ esterilizante | Q23, Q24, Q26 | 3 |

**15/15 subtópicos com ≥2 questões.** Nenhum volta para a prancheta.

## Densidade por PARTE

| PARTE | Subtópicos | Palavras (miolo) | Desvio da média |
|---|---|---|---|
| I | 4 | ≈2.360 | −7% |
| II | 6 | ≈3.630 | +13% (6 subtópicos, o maior bloco) |
| III | 5 | ≈2.700 | −5% |

Média por subtópico ≈617 — **acima do alvo de 450–550 do `ERROS.md` F10**. Quebra declarada abaixo.

## Índice de completude (0–10)

- **E1 × slide: 9.** Cobre os 4 blocos do slide (introdução, agentes físicos, agentes químicos, as 7 perguntas de revisão) e vai um degrau acima em sete pontos declarados no Tema Card — mecanismo do vapor saturado e do ar retido, valor D e esterilidade como probabilidade 10⁻⁶, escada de resistência explicada barreira a barreira, por que álcool 70% e não 100%, indicador químico × biológico, limite real do filtro de 0,22 µm e do HEPA por difusão, e o critério de Spaulding, que o slide não traz e é o que transforma tudo em conduta.
- **E2 × E1: 9.** 15/15 subtópicos com ≥2 questões, 17 de Integração com mapa A+B gravado antes da redação, 5 de Aplicação em cenário clínico. Menor cobertura: 2.1, 2.4, 2.6 e 3.4 no piso de 2.
- **Cards × E1: n/a (não avaliável nesta corrida).** O passo 11 (curadoria AnKing + deck-aula) não rodou — sessão remota não alcança o AnkiConnect local, o mesmo bloqueio das corridas `micro-01`, `imuno-07` e do fígado. Como o loop card→E1 não pôde acontecer, o passe de aprofundamento nasceu do slide + bibliografia + calibração UC03 (passo 2b), não de cards.

**Fontes → E1:** 34/34 slides do professor incorporados (28 como conteúdo textual, 15 como figura; 6 descartados por juízo editorial ou por serem capas de seção).
**E1 → cards:** não medido nesta corrida (AnkiConnect inacessível).

## Erros recorrentes checados (`ERROS.md`)

#1 paridade (20/20 PASS) · #2 siglas (DNA e HEPA declarados, únicos do texto) · #4 heredoc atômico usado · #5 `questao-ce` em tuplas de pares · #6 termo-notas: 7 (faixa 6–10) · #7 teto 22 declarado no Tema Card · #8/#15 `auto_fix_etapas` limpo · #9 gabarito column-major OK · #10 sem fóssil de E4 · #11 numeração coerente · #12 nenhuma cadeia ≥4 setas sem figura · #13 conclusão em 4 camadas (princípio unificador → mecanismo nuclear → clínica retomada → projeção para antibióticos) · #14 5 registros de abertura rotacionados, nenhum par vizinho igual · #16/F3 boxes: PARTE I 1, PARTE II 1, PARTE III 3 (2 + 1 clínica) · #19 título de capa cabe na faixa · #20 nenhum `#termo-nota` com o termo repetido · #23 sequências C/E lidas item a item depois da redação.

## Quebras e pendências declaradas

1. **Densidade acima do alvo do F10.** ≈617 palavras/subtópico contra o alvo 450–550. O teto de páginas foi respeitado (21 de 22) e os cinco desperdícios do F10 foram caçados — não há moldura, legenda redundante nem conclusão que reconta. O excedente é conteúdo do dial `fundo`, não gordura. Fica a decisão do Davi se quer o mesmo escopo em menos palavra na próxima.
2. **`revisor-gabarito` não rodou.** Os 9 stubs em `.claude/agents/` declaravam `tools:` em minúsculas (`read`, `bash`, `write`, `edit`, `grep`), o que faz o spawn ser recusado com "zero tools". **Corrigido nesta sessão** (todos normalizados para `Read`/`Bash`/`Write`/`Edit`/`Grep`), mas as definições são carregadas no início da sessão — só vale a partir da próxima. A conferência do gabarito foi feita à mão item a item, como o `ERROS.md` #23 exige nesse caso, e confirmada por `verificar_gabarito_resumo.py`.
3. **Passo 11 (deck-aula) não rodou** — AnkiConnect local inacessível de sessão remota.
4. **Resumindo com 9 seções** (faixa canônica 6–10) em 1 página. A primeira versão saiu com 15 e depois 12 seções e vazava para uma segunda página meio vazia; a redução a 9 devolveu a página única.
5. **Duas sequências C/E repetidas** entre as 10 (Q07=Q13, Q10=Q28). Não é degeneração pelas regras da guarda, mas fica registrado.
