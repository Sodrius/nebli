# Relatório de fechamento — Motilidade do TGI

**Slug:** `motilidade-tgi` · **PDF:** `Motilidade do TGI - Etapas 1 a 3 - FGS.pdf` · **34 páginas** · E1 em **14** (teto 15)
**Slide-fonte:** `Aula1_MED_2026_1.pdf` (6 páginas) — Profa. Fran Goulart da Silva, Fisiologia e Biofísica ICB/USP

## 1. Tabela auditável de figuras (ERROS.md F5)

| Figura | PARTE | Origem | Mecanismo que carrega | Largura |
|---|---|---|---|---|
| `fig-tubo` | I · 1.1 | slide-02, recorte esquerdo | onde está o liso (2/3) e onde está o esquelético (1/3) | lateral 27% |
| `fig-fasico-tonico` | I · 1.2 | slide-04, recorte esquerdo (Berne & Levy) | mesmo transiente de Ca²⁺, decaimentos de força distintos | 58% |
| `fig-inervacao` | I · 1.3 | slide-02, recorte direito | divisão de trabalho SNE (mioentérico × submucoso) e SNA | 66% |
| `fig-reflexos` | II · 2.1 | slide-03 integral | arco curto intramural × arco longo vago-vagal | 72% |
| `fig-esfincteres` | II · 2.3 | slide-04, recorte direito | os cinco esfíncteres e a dupla regulação do piloro | 56% |
| `fig-juncao` | III · 3.1 | slide-05, recorte superior esquerdo | varicosidades ao longo do axônio, sem placa motora | lateral 36% |
| `fig-calmodulina` | III · 3.2 | slide-05, faixa inferior | Ca²⁺ → calmodulina → MLCK → miosina ativada | 62% |
| `fig-cascata-ca` | III · 3.2 | slide-05, recorte direito (com limpeza de sangramento) | contração × relaxamento: extrusão e miosina fosfatase | 68% |
| `fig-gpcr` | III · 3.3 | slide-06, recorte da figura interna | Gq/PLCβ/IP₃ e G12/13 → RhoA → Rho-quinase | 70% |

**Curadoria (diretriz 15).** O slide tem 6 páginas, das quais 1 é capa. Em vez de reproduzir slides inteiros, os slides 4 e 5 foram **fatiados por unidade de mecanismo** (dois e três mecanismos distintos cada), o que rendeu 9 figuras a partir de 5 páginas de conteúdo.
**Descartadas:** slide-01 (capa, sem mecanismo) · faixa-título "Distensão do tubo = relaxamento dos esfíncteres" do slide 4 (texto, não mecanismo — migrou para a legenda) · caixa "Outros neuromediadores" do slide 3 (lista, coberta em prosa no 2.1).
**Quebra declarada:** PARTE II ficou com **2** figuras contra a meta heurística de 3. O terceiro candidato era um recorte redundante do slide-03 já usado inteiro em 2.1, e reprovou no filtro da diretriz 15.

## 2. Ratio de paridade Q01–Q30 (banda dupla 0.80–1.25)

**20/20 múltipla escolha dentro da banda. 0 FAIL.** Média 1.02, extremos 0.83 (Q03) e 1.08 (Q18).

```
Q01 correta(B)=11 dist=[11,10,10,9]   maior=11 ratio=1.00 PASS
Q03 correta(B)=10 dist=[12,12,10,10]  maior=12 ratio=0.83 PASS
Q04 correta(D)=12 dist=[12,12,11,10]  maior=12 ratio=1.00 PASS
Q05 correta(B)=11 dist=[13,11,10,8]   maior=13 ratio=0.85 PASS
Q07 correta(E)=13 dist=[14,13,12,11]  maior=14 ratio=0.93 PASS
Q08 correta(B)=10 dist=[11,11,9,8]    maior=11 ratio=0.91 PASS
Q10 correta(D)=14 dist=[14,12,12,10]  maior=14 ratio=1.00 PASS
Q11 correta(C)=27 dist=[29,28,28,27]  maior=29 ratio=0.93 PASS
Q12 correta(E)=26 dist=[28,27,27,26]  maior=28 ratio=0.93 PASS
Q14 correta(A)=24 dist=[23,22,22,20]  maior=23 ratio=1.04 PASS
Q15 correta(B)=24 dist=[24,24,21,19]  maior=24 ratio=1.00 PASS
Q17 correta(B)=24 dist=[25,24,24,23]  maior=25 ratio=0.96 PASS
Q18 correta(C)=28 dist=[26,24,24,23]  maior=26 ratio=1.08 PASS
Q20 correta(E)=20 dist=[21,21,20,19]  maior=21 ratio=0.95 PASS
Q21 correta(C)=21 dist=[25,21,21,21]  maior=25 ratio=0.84 PASS
Q22 correta(E)=23 dist=[26,23,21,19]  maior=26 ratio=0.88 PASS
Q24 correta(C)=22 dist=[24,22,21,19]  maior=24 ratio=0.92 PASS
Q26 correta(A)=24 dist=[24,22,22,21]  maior=24 ratio=1.00 PASS
Q27 correta(B)=22 dist=[22,22,21,17]  maior=22 ratio=1.00 PASS
Q29 correta(C)=22 dist=[22,22,21,19]  maior=22 ratio=1.00 PASS
```
Q02 · Q06 · Q09 · Q13 · Q16 · Q19 · Q23 · Q25 · Q28 · Q30 são Certo/Errado — paridade de comprimento não se aplica.

**Duas remediações direcionais aplicadas** (nunca encurtando a correta): Q08 saiu em 0.73 (correta curta) e a correta foi **enriquecida** de 8 para 10 palavras; Q24 saiu em 0.79 (correta curta) e foi enriquecida de 19 para 22.

**Consolidação decoreba:** média de **11,3 palavras** por alternativa (alvo 10–20), maior alternativa 15. Gate `check_consolidacao_decoreba` passa.

**Gabarito.** MC sorteadas com semente fixa e guarda anti-degeneração: distribuição `A:2 B:7 C:5 D:2 E:4` — maior fatia 35% (teto ~40%), sem corrida de 4 letras iguais. As 10 sequências C/E **não foram sorteadas**: as assertivas foram escritas pelo conteúdo e a sequência real foi lida item a item depois (`ERROS.md` #23), com guarda aplicada — nenhuma `CCCC`/`EEEE`, nenhuma `CECE`/`ECEC`, 21 C contra 19 E no total dos 40 itens.

## 3. Cobertura subtópico → questões (piso 2, CANON 2026-07-01)

| Subtópico | Questões que o cobrem | N |
|---|---|---|
| 1.1 Sincício e marcapasso | Q01 · Q02 · Q11 · Q17 · Q24 · Q29 | 6 |
| 1.2 Fásico e tônico | Q05 · Q12 · Q18 | 3 |
| 1.3 Os dois plexos entéricos | Q03 · Q04 · Q13 · Q14 · Q20 · Q21 · Q26 | 7 |
| 2.1 Reflexo curto intramural | Q13 · Q19 · Q20 · Q22 · Q27 | 5 |
| 2.2 Reflexo longo vago-vagal | Q14 · Q15 · Q16 · Q25 · Q28 | 5 |
| 2.3 Esfíncteres e distensão | Q06 · Q15 · Q16 · Q21 · Q25 · Q26 | 6 |
| 3.1 Junção neuroefetora | Q09 · Q17 · Q23 | 3 |
| 3.2 Cálcio, calmodulina e MLCK | Q07 · Q08 · Q11 · Q12 · Q23 · Q24 | 6 |
| 3.3 Sensibilização ao cálcio | Q10 · Q18 · Q19 · Q22 · Q30 | 5 |

**Nenhum subtópico abaixo do piso.** Mínimo 3, máximo 7.

## 4. Forma da E1

| Bloco | Palavras |
|---|---|
| intro-box | 211 |
| 1.1 · 1.2 · 1.3 | 528 · 452 · 424 |
| 2.1 · 2.2 · 2.3 | 596 · 412 · 552 |
| 3.1 · 3.2 · 3.3 | 331 · 579 · 468 |
| conclusão integradora | 301 |
| **miolo total** | **4.983** (alvo 4.800–5.500, teto 6.000) |

Paridade entre PARTES (diretriz 14): I = 1.404 · II = 1.560 · III = 1.378 → desvios de −3%, +8% e −5% da média. Dentro de ±20%.
Boxes: 1 `confusao-prevista` (1.2) · 2 `atencao-box` (2.3, 3.2) · 2 `clinica-box` (2.1 Chagas, 3.3 acalásia). Dentro da cota de 1–2 pesados por PARTE.
Termo-notas: 9 · Siglas com footnote: 11 · Interrogações terminais: 0.

## 5. Índice de completude (0–10)

- **E1 × slide — 9.** Cobre integralmente os cinco blocos do slide (proporção liso/esquelético, SNE × SNA, reflexos curto e longo, os cinco esfíncteres com a dupla regulação do piloro, e a cascata da junção neuroefetora até RhoA/ROCK) e acrescenta 9 aprofundamentos colados, um por subtópico. Não é 10 porque a caixa "outros neuromediadores" do slide 3 é resolvida em uma frase, sem desdobrar serotonina e GABA.
- **E2 × E1 — 9.** Os 9 subtópicos são cobrados por 3 a 7 questões cada, todos acima do piso de 2, e as distratoras cruzam subtópicos vizinhos em Q11, Q21, Q26, Q27 e Q29.
- **Cards × E1 — não avaliado.** Fora do escopo pedido ("etapas 1 a 3") e inalcançável desta sessão: o AnkiConnect roda em `localhost` na máquina do Davi e sessões na nuvem não o alcançam (`referencias-externas/INFRA-REMOTO.md`).

**Fontes → E1:** 9/9 aprofundamentos previstos no Tema Card foram incorporados (Cajal e onda lenta · estado latch · Hirschsprung · lei do intestino · íleo pós-operatório · relaxamento transitório do EEI · geometria da junção neuroefetora · miosina fosfatase como alvo regulável · nitrato → GMPc → PKG).

## 6. Quebras e ressalvas declaradas

1. **Warning do `precompile-check` no subtópico 3.3 (898 palavras).** É artefato de medição: o check corta do último `#subtopico(` até o fim do arquivo, e o segmento inclui o `#clinica-box` da acalásia (136) e a `#conclusao-box` (301). A prosa real do 3.3 tem **468** palavras, dentro do alvo 450–550.
2. **PARTE II com 2 figuras** em vez de 3 — justificada no item 1.
3. **Deck-aula não montado.** O passo 11 do `/resumo` (curadoria AnKing + `gate_deck_aula_completo.py --verify-anki`) exige AnkiConnect local. Pendente para uma sessão na máquina do Davi.
4. **Upload para o Drive não feito** — `rclone` não está autorizado neste contêiner.
5. **Ambiente remoto:** `typst` e o poppler não vinham no contêiner. Instalados conforme `ERROS.md` #22 (binário estático do Typst; `pdftotext`/`pdfinfo`/`pdffonts` como shims sobre o pymupdf). Shims são de sessão e não foram para o repositório.
