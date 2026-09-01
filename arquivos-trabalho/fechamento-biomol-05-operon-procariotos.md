# Relatório de fechamento — biomol-05-operon-procariotos

PDF: `resumos-gerados/BIOMOL-05-OPERON-PROCARIOTOS.pdf` (43 páginas, 23,3 MB) ·
cópia leve: `resumos-gerados/leves/BIOMOL-05-OPERON-PROCARIOTOS.pdf` (3,5 MB, 6,7× menor).
Dial: `profundidade: fundo`. E1 com 21 páginas de miolo (teto 22), 7 748 palavras.

## Gates técnicos

| Gate | Resultado |
|---|---|
| `precompile-check.py` | 0 erro · 1 warning (falso-positivo: TTGACA/TATAAT lidos como siglas) |
| Paridade MC Q01–Q30 | 20/20 na banda 0.80–1.25 · média 1.04 · máx 1.18 · mín 0.85 |
| `check_ce_quatro_itens` | 10/10 C/E com exatamente 4 itens |
| `check_pre_aula` | 1 067 palavras · 42 negritos · 0 interrogações · sem figura/bullet |
| `verificar_gabarito_resumo.py` | consistente (30 itens, 20 MC + 10 C/E) |
| `auditar_pdf.py` | acentuação 3,2–3,4% · 22 paths de figura existem · Merriweather+Montserrat embarcados |
| `pos_pipeline_check.py` | sem fóssil de E4 · capa sem bloco/prova · numeração coerente · sem página em branco |
| Vocabulário banido na E1 | 0 ocorrências |
| Perguntas terminais na E1 | 0 |

## Paridade Q01–Q30 (banda dupla 0.80–1.25)

Q01 1.03 · Q02 0.97 · Q04 1.03 · Q05 0.94 · Q07 0.94 · Q08 1.10 · Q09 1.07 · Q10 1.10 ·
Q11 0.97 · Q13 0.97 · Q14 1.07 · Q16 0.85 · Q17 1.03 · Q19 0.94 · Q20 1.04 · Q22 1.00 ·
Q24 0.93 · Q26 0.97 · Q28 1.07 · Q30 1.03 — **20 PASS, 0 FAIL.**
(C/E não entra na paridade por regra.) Distribuição de letras: A 4 · B 3 · C 4 · D 3 · E 6 —
nenhuma letra acima de 30%, sem corrida de 4 iguais.

## Gabarito C/E — sequências lidas item a item APÓS a redação (ERROS #23)

Q03 CEEC · Q06 ECCE · Q12 CCEE · Q15 ECCE · Q18 CCEC · Q21 CECC · Q23 CCCE · Q25 EECC ·
Q27 CCEE · Q29 CEEC. Sem CCCC/EEEE, sem CECE/ECEC, sem bloco longo. Contagem global 23C/17E.

## Tabela auditável de figuras (22 · todas do slide do professor)

| Figura | PARTE | Origem | Mecanismo que carrega | Largura |
|---|---|---|---|---|
| slide-04 | I | slide | pontuação da transcrição: promotor, +1, terminador | 52% |
| slide-05 | I | slide | mRNA policistrônico com RBS independentes | 64% |
| slide-06 | I | slide | operon como unidade transcricional (exemplo trp) | 62% |
| slide-42 | I | slide | anatomia genérica: elementos cis × produtos trans | 78% |
| slide-15 | I | slide | mapa do operon lac com tamanhos reais em pb | 80% |
| slide-09 | II | slide | repressor ocupando o operador e silenciando os três genes | 72% |
| slide-11 | II | slide | estado sem lactose: tetrâmero no operador | 56% |
| slide-13 | II | slide | estado com indutor: alosteria solta o repressor | 56% |
| slide-19 | II | slide | química do X-Gal → índigo + placa azul/branca | 68% |
| slide-20 | II | slide | operador mutante O^c: repressor sem sítio | 58% |
| slide-21 | II | slide | lacI⁻: operador íntegro, repressor inútil | 58% |
| slide-23 | II | slide | repressor difusível agindo em trans nas duas cópias | 62% |
| slide-22 | II | slide | operador agindo só em cis no diploide parcial | 62% |
| slide-26 | III | slide | operador livre e ainda assim pouco mRNA (promotor fraco) | 60% |
| slide-29 | III | slide | caixas -35 e -10 e o espaçamento de ~17 pb | 72% |
| slide-31 | III | slide | promotores reais alinhados: consenso é frequência | 66% |
| slide-33 | III | slide | as duas divergências do promotor lac, letra a letra | 62% |
| slide-34 | III | slide | sítio CAP a -61, fora do território da RNAP e do repressor | 74% |
| slide-38 | III | slide | dobra de ~90° do DNA pelo dímero de CAP | 54% |
| slide-39 | III | slide | sentido da seta glicose → cAMP → CAP | 56% |
| slide-40 | III | slide | os quatro estados combinatórios do operon | 78% |
| slide-41 | III | slide | ausência de regulação · negativa · positiva no mesmo promotor | 66% |

**Descartadas pelo filtro de utilidade (regra 15):** slide-01/02/03 (capa, objetivos, agenda — não
carregam mecanismo) · slide-07/08/17/18 (histórico e retrato de Jacob/Monod/Lwoff — o gesto
histórico entra em prosa, não em foto) · slide-10/12/14/24/25/27/28/30/32/35/36/37 (repetem
mecanismo já coberto por outra figura escolhida, ou são slides só-texto).

## Densidade por PARTE (paridade ≤ ±20%)

| PARTE | subtópicos | palavras | palavras/subtópico | desvio |
|---|---|---|---|---|
| I | 4 | 1 675 | 419 | −10% |
| II | 6 | 2 769 | 461 | −1% |
| III | 5 | 2 564 | 513 | +11% |

## Cobertura E1 → E2 (todo subtópico com ≥2 questões)

| Subtópico | Questões |
|---|---|
| 1.1 Por que regular / amplitude 1000× | Q10, Q12, Q17 |
| 1.2 Unidade transcricional e policistrônico | Q01, Q15, Q25 |
| 1.3 Cis e trans | Q03, Q11, Q20 |
| 1.4 Peças do operon lac | Q02, Q08, Q16 |
| 2.1 O que o repressor bloqueia | Q02, Q17, Q21 |
| 2.2 Alolactose, alosteria e arranque | Q04, Q06, Q10, Q16 |
| 2.3 X-Gal, IPTG e a placa | Q06, Q12, Q19, Q27 |
| 2.4 O^c e lacI⁻ | Q11, Q19, Q20 |
| 2.5 Diploide parcial | Q09, Q11, Q20 |
| 2.6 lacI^s, lacI^-d e o método | Q09, Q12, Q19, Q29 |
| 3.1 O limite do controle negativo | Q13, Q21, Q28 |
| 3.2 Promotor, sigma e consenso | Q05, Q13, Q22 |
| 3.3 Promotor fraco é projeto | Q13, Q24, Q30 |
| 3.4 CAP-cAMP, PTS e exclusão do indutor | Q07, Q14, Q18, Q24 |
| 3.5 Quatro estados, diauxia, trp e ara | Q21, Q23, Q25, Q28 |

Nenhum subtópico com menos de 2.

## Índice de completude (0–10)

- **E1 × slide — 9.** Cobre as 42 lâminas dentro do recorte (incluindo as duas que o objetivo não
  nomeia: anatomia do promotor e matriz consenso) e vai além em seis pontos mecanísticos que o
  slide só insinua: o que exatamente o repressor trava (escape do promotor, não pouso da RNAP);
  o problema do arranque resolvido pela expressão basal; a estequiometria desigual dos produtos
  de um mRNA policistrônico; os alelos lacI^s e lacI^-d; o eixo PTS → EIIA → adenilato-ciclase e a
  exclusão do indutor; e a atenuação do trp com o operon ara como exceção à dicotomia.
- **E2 × E1 — 9.** Os 15 subtópicos têm 3 ou 4 questões cada, e as questões de previsão
  (Q13 promotor consenso, Q14 EIIA travada fosforilada, Q22 espaçamento de 24 pb, Q20 e Q11
  genótipos duplos) cobram exatamente os aprofundamentos, não só o piso.
- **Cards × E1 — não avaliável nesta corrida.** O AnkiConnect local não é alcançável de uma sessão
  remota (mesma limitação das corridas do fígado e de micro-01), então o passo 11 não rodou.
  O aprofundamento veio das outras fontes canônicas: calibração UC03 por provas antigas + a
  bibliografia declarada pelo próprio slide (Watson cap. 18).

**Fontes → E1: 15/15 conceitos relevantes incorporados** (5 objetivos do documento + 42 lâminas +
7 subquestões do acervo UC03, todos dentro do recorte de um único slug).
**E1 → cards: não medido** (passo 11 bloqueado, ver acima).

## Erros recorrentes checados

#1 paridade OK · #2 siglas declaradas (6, warning só em sequências de DNA) · #4 gravação por
heredoc sem truncamento · #5 `questao-ce` em tuplas de pares · #8 sem `#etapa-header` nas etapas ·
#12 toda cadeia multi-passo com figura adjacente · #13 conclusão com as 4 camadas · #14 registros
de abertura rotacionados sem par vizinho repetido · #15 sem markdown vazado · #16 apenas 2
`atencao-box` no resumo inteiro (cota 1–2 por PARTE) · #18 mapa A+B gravado antes da redação ·
#19 título curto, capa proporcional (validado visualmente) · #20 nenhum `#termo-nota` com termo
repetido · #22 typst e shims de poppler instalados na sessão remota · #23 C/E lidos item a item.

## Pendências desta corrida

- **Passo 11 (deck-aula) não rodou** — AnkiConnect inalcançável da nuvem. Reexecutar numa sessão
  local: `python flashcards/scripts/gerar_checklist.py biomol-05-operon-procariotos` e seguir.
- **Upload pro Drive** continua gated em `rclone config`.
- `figuras/biomol-05-operon-procariotos/_orig/` guarda os PNGs antes do corte de margem branca e
  da remoção do placeholder azul vazio do PowerPoint (feito nesta corrida para as 42 lâminas).
