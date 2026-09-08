# Tema Card — Regulação da expressão gênica em procariotos: o modelo do operon

## Seção A — Escopo

- **Tema:** Regulação da expressão gênica em bactérias — o modelo do operon
- **Slug:** `biomol-05-operon-procariotos` (entrada em `banco/aulas_uc03.yml`, componente Biologia Molecular)
- **Disciplina:** UC03 · Biologia Molecular (Prof. Alexandre Bruni-Cardoso, IQ-USP)
- **Onde estudar:** Lehninger, *Princípios de Bioquímica*, cap. 28 (Regulação da expressão gênica — o operon lac) · Alberts, *Biologia Molecular da Célula*, cap. 7 (Controle da expressão gênica em bactérias) · Watson, *Biologia Molecular do Gene*, cap. 18
- **Alvo de páginas E1:** piso 2, **teto 15** — alvo real 12–14 · **9 subtópicos** (3 + 3 + 3), 450–550 palavras cada, ~4.700–5.000 palavras de miolo
- **Distribuição E2:** PADRÃO → 10 Consolidação · 15 Integração · 5 Aplicação

### Teto histórico e degrau (substitui o aposentado campo `profundidade:`)

Fonte: `python3 referencias-externas/uc03/consultar.py --slug biomol-05-operon-procariotos` → 7 subquestões (2019 P2, 2024 P2, 2025 P2).

- **Teto histórico desta aula.** A casa cobra: (a) **nomear os componentes regulatórios** do operon lac — lacI, promotor lac, operador, sítio CAP, proteína CAP — e os genes estruturais lacZ/lacY/lacA com seus produtos; (b) **descrever a expressão na presença e na ausência do substrato**, incluindo o análogo não metabolizável; (c) **repressão por catabólito** enunciada como "glicose alta → cAMP baixo → CAP não ativa"; (d) **genótipos de diploide parcial** (I⁺P⁺O^c Z⁺ / I⁻P⁺O⁺Z⁺) classificados em dominante × recessivo, constitutivo × não-indutível, cis × trans; (e) **IPTG e X-Gal** definidos por função no experimento, com leitura de colônia azul × branca em tabela de meios.
- **Degrau que a E1 acrescenta.** (1) *Por que* a iniciação da transcrição é o ponto de controle preferido — meia-vida do mRNA bacteriano em minutos e acoplamento transcrição–tradução; (2) o repressor LacI como **proteína alostérica** com arquitetura resolvida — tetrâmero de dois dímeros, hélice-volta-hélice no N-terminal, sítio do indutor no core, e o **looping de DNA** entre operadores auxiliares que multiplica a repressão; (3) a **origem física da expressão basal** e por que o sistema não funcionaria sem ela; (4) a **anatomia quantitativa do promotor** — −35 TTGACA, −10 TATAAT, espaçamento de 17 pb, σ⁷⁰ como leitor — e o promotor lac como promotor *fraco por desenho*; (5) o mecanismo real da queda do cAMP pelo **sistema fosfotransferase (PTS)** e a **exclusão do indutor** pela EIIA^Glc desfosforilada; (6) a leitura do operon lac como **porta lógica AND**, e a diauxia como o fenótipo de crescimento que ela produz; (7) o dominante-negativo do **LacI^S** explicado pela mistura de subunidades no tetrâmero.

### Hierarquia de fontes aplicada (canônico 2026-09-03)

1. **O slide guiou o fluxo.** A ordem do resumo é a do deck de 46 telas: níveis de regulação e pontuação da transcrição → as quatro lógicas repressor/ativador × indutor/co-repressor → definição de operon, cis e trans → operon lac e metabolismo da lactose → repressor como sensor → Jacob e Monod, mutantes e diploide parcial → anatomia do promotor → CAP-cAMP → regulação integrada.
2. **A prova indicou o quanto ir a mais.** O acervo fixou o teto acima; o degrau declarado é o que a E1 acrescenta por cima dele, sempre como mecanismo.
3. **Livros e outras fontes indicaram assuntos laterais.** Lehninger deu o looping de operadores e o PTS; Alberts deu a lógica de porta AND e a troca de fatores σ; entram como menção lateral integrada à prosa, sem redefinir escopo.

### Recorte slide × tema

O slide cobre **regulação em bactérias com o operon lac como modelo único desenvolvido**, e menciona as quatro lógicas (negativa/positiva × induzível/repressível) sem desenvolver um exemplo de repressão. **Recorte declarado:** o operon trp entra como **exemplo de uma frase** para dar corpo à lógica negativa repressível — o slide a nomeia e ficaria oca sem exemplo — mas não vira subtópico, não ganha figura e não puxa atenuação nem estrutura do mRNA líder. Ficam de fora: regulação em eucariotos (aulas `biomol-07`/`biomol-08`), riboswitches, quorum sensing, e o uso de promotores lac em vetores de expressão além do gancho clínico de duas frases.

### Prioridades desta corrida (do `MEMORY.md` § Diário de revisões)

1. **Registro científico (peso alto, entrada de 2026-09-03).** Termo técnico nomeado na mesma frase em que é definido — "o operador, sequência palindrômica de 21 pb que sobrepõe o início da transcrição", nunca "uma sequência de DNA (chamada operador)". Filtro das três funções aplicado subtópico a subtópico.
2. **Economia de palavra (peso alto, entrada `imuno-07`).** Teto de 15 páginas; 9 subtópicos, nenhum acima de 550 palavras. Cortar moldura e reafirmação; nunca o elo causal.
3. **Consolidação decoreba.** Q01–Q10 como recall direto (nome, número, sequência, qual-é-qual), alternativas de 10–20 palavras.
4. **Figura obrigatória onde há coreografia espacial** (entrada `biocel-07`). O tema é inteiramente espacial — quem se liga onde, em qual molécula de DNA. Toda PARTE tem ≥3 figuras.

## Seção B — Esqueleto das 3 PARTES (9 subtópicos, 13 figuras)

### PARTE I — A gramática da regulação bacteriana (3 subtópicos)

| # | Subtópico | Figuras |
|---|---|---|
| 1.1 | Onde o controle acontece, e por que na largada da transcrição | `slide-04` pontuação da transcrição — 55% |
| 1.2 | Repressor, ativador, indutor, co-repressor: as quatro combinações | `slide-08` regulação negativa induzível — 58% |
| 1.3 | Operon, cis e trans: a unidade que a bactéria transcreve de uma vez | `slide-07` anatomia do operon genérico — 55% (mapa orientador; reduzido de 78% na validação visual para eliminar página órfã) |

### PARTE II — O operon lac: a máquina e a lógica genética que a revelou (3 subtópicos)

| # | Subtópico | Figuras |
|---|---|---|
| 2.1 | Os cinco elementos do operon lac e o açúcar que eles processam | `slide-15` mapa do operon com tamanhos — 72% · `slide-17` metabolismo da lactose — lateral 40% |
| 2.2 | LacI: um sensor alostérico que solta o DNA quando encontra o indutor | `slide-30` tetrâmero e domínios — 52% · `slide-32` indutor desorganiza o HTH — 60% |
| 2.3 | Jacob e Monod: mutantes, diploide parcial e o repressor deduzido | `slide-21` mutantes constitutivos × não-indutíveis — 55% · `slide-29` diploide parcial O^c — 62% |

### PARTE III — Ligar de verdade: promotor, ativador e a integração dos dois açúcares (3 subtópicos)

| # | Subtópico | Figuras |
|---|---|---|
| 3.1 | A anatomia do promotor bacteriano e a força que ele carrega | `slide-33` pegada da RNAP e do repressor no DNA — 75% |
| 3.2 | CAP-cAMP: o ativador que compensa um promotor fraco de propósito | `slide-36` sítio CAP e αCTD — 62% · `slide-37` CAP só liga com cAMP — 55% |
| 3.3 | Glicose × lactose: quatro ambientes, uma porta lógica | `slide-35` regulação integrada em três estados — 65% |

**Conclusão integradora** (`#conclusao-box`, 4 camadas) + **Resumindo** (8 seções).

**Figuras descartadas pelo filtro de utilidade (regra 15):** `slide-16` (fotos do Nobel — retrato não carrega mecanismo), `slide-25` (placa com colônias azuis/brancas — bonita, mas o mecanismo do X-Gal está na prosa e a foto não distingue os genótipos), `slide-31` (sequência do operador — a palindromia é dita em uma frase e a figura exigiria leitura de bases), `slide-18` (curva de inducibilidade — redundante com `slide-21`, que traz a mesma curva **e** os dois mutantes), `slide-06` (bullets de cis/trans — texto puro, coberto por `slide-07`).

## Seção B.bis — Registro de abertura por subtópico

Pergunta âncora/retórica banida. Nenhum par vizinho compartilha registro.

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | integração-anterior |
| 2.1 | analogia concreta |
| 2.2 | enquadramento |
| 2.3 | ponto-de-quebra |
| 3.1 | integração-posterior |
| 3.2 | integração-anterior |
| 3.3 | analogia concreta |

## Seção C — Profundidade, termo-notas e distribuição da E2

**Termo-notas obrigatórias (alvo 6–10):** operon · mRNA policistrônico · alolactose · IPTG · X-Gal · diploide parcial (merozigoto) · palíndromo · sequência consenso · repressão por catabólito · diauxia.

**Siglas com `#sigla` na 1ª aparição:** RNAP · mRNA · cAMP · CAP · HTH · pb · PTS · DNA.

**Distribuição E2 (PADRÃO):** Q01–Q10 Consolidação (decoreba) · Q11–Q25 Integração · Q26–Q30 Aplicação.
**Formatos:** 10 itens Certo/Errado com 4 assertivas cada, distribuídos pelas três categorias; 3 itens "assinale a incorreta"; o restante múltipla escolha A–E.

**Fronteira UC03 declarada.** Conteúdo de `biomol-04` (transcrição em detalhe), `biomol-07`/`biomol-08` (eucariotos) e `micro-06` (genética bacteriana, conjugação) entra apenas como retomada de 1–2 frases quando o mecanismo desta aula depende — a conjugação, por exemplo, aparece só como o meio de construir o merozigoto.

## Seção D — Mapa de Confusões inicial

Gravado integralmente em `mapa-confusoes/biomol-05-operon-procariotos.md` (4+ confusões por subtópico). Eixos principais:

- Indutor **não** liga o operon: ele desliga o repressor. Regulação negativa induzível continua sendo negativa.
- Lactose não é o indutor — **alolactose** é, e ela é produto da própria β-galactosidase.
- Operador é elemento **cis**; repressor é produto **trans**. O^c é dominante e cis; I⁻ é recessivo e trans.
- CAP-cAMP não responde à lactose; responde à **falta de glicose**.
- Promotor lac fraco não é defeito de sequência: é o que dá espaço para a ativação.
- Expressão basal não é vazamento inútil — é o que permite a lactose entrar e virar indutor.

## Seção E — Exemplares-âncora

- **Categoria 1 (universal) — explicação mecanística parágrafo a parágrafo.** Acerta em dar a cada parágrafo uma função discreta, encadeada na anterior. Uso em 2.2 (indutor liga no core → HTH se desalinha → afinidade pelo operador cai ~1000× → RNAP escapa) e em 3.2 (glicose entra pelo PTS → EIIA^Glc fica desfosforilada → adenilato-ciclase não é estimulada → cAMP cai → CAP não liga).
- **Categoria 8 (universal) — `#atencao-box`.** Acerta em reservar o vermelho para a inversão que destrói o raciocínio. Reservo dois: (a) indutor age **sobre o repressor**, não sobre o DNA; (b) O^c e I⁻ têm comportamentos genéticos opostos no diploide parcial.
- **Categoria 14 (universal) — siglas em footnote.** `#sigla` na 1ª aparição de RNAP, mRNA, cAMP, CAP, HTH, pb, PTS.
- **Categoria 5 — refinamento histórico de teoria.** Acerta em mostrar como um modelo nasceu de fenótipos antes de haver bioquímica. Uso em 2.3: Jacob e Monod deduziram uma proteína difusível sem nunca terem visto o repressor.
- **Categoria 6 — organização terminológica.** Acerta em arrumar nomenclatura ramificada sem virar lista. Uso em 1.2 para as quatro combinações, com tabela (gatilho de cruzamento de duas dimensões).
- **Categoria 7 — analogia construtiva.** Uso em 2.1 (o operon como uma linha de produção com um único interruptor) e em 3.3 (porta lógica AND) — analogias que carregam o mecanismo, não a aparência.
- **Categoria 9 — `#clinica-box`.** Uso em 2.3 (X-Gal e o rastreio azul/branco no diagnóstico molecular e na produção de proteína recombinante) e em 3.3 (a mesma lógica de indução governando genes de virulência e de resistência a antibióticos em patógenos).
- **Categoria 18 — quando quebrar a prosa.** Gatilho de tabela duas vezes: as quatro lógicas de regulação (1.2) e os quatro ambientes glicose × lactose (3.3). Todo o resto é prosa corrida.
