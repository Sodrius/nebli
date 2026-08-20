# Tema Card — Reconhecimento inato no sistema imune

## Seção A — Escopo

- **Tema:** Reconhecimento inato
- **Slug:** `imuno-02-reconhecimento-inato`
- **Disciplina:** Imunologia
- **Fonte:** transcrição integral da aula "Reconhecimento inato no Sistema Imune" (22 slides extraídos em `figuras/imuno-02-reconhecimento-inato/`)
- **Onde estudar:** Abbas cap. 4 · Janeway cap. 3 · Takeuchi & Akira, *Cell* 140:805–820 (2010) · Schroder & Tschopp, *Cell* 140:821–832 (2010) — as duas últimas são as referências que o próprio professor projetou
- **Alvo de páginas E1:** piso 2, **teto 22** — alvo 15–19
- **`profundidade:`** `padrao` (o novo default já elevado, CANON 2026-07-12)
- **Recorte slide × tema:** o slide cobre exatamente o tema pedido. Duas ressalvas declaradas: (a) os slides 3–7 são recapitulação da aula anterior (repertório clonal, tolerância × resposta, apresentação de antígenos) — entram na PARTE I como **pré-requisito retomado**, não como conteúdo novo, porque a lógica hierárquica do reconhecimento não se sustenta sem eles; (b) a aula não tem banco FMUSP associado (Imunologia não está em `aulas_uc01.yml`/`aulas_uc02.yml` com este recorte) — a calibração vem do slide + bibliografia projetada pelo professor, sem régua de banco.
- **Sem Anki vivo nesta corrida:** sessão remota, sem AnkiConnect em localhost. O passe de aprofundamento nasce do slide + bibliografia projetada (Takeuchi & Akira; Schroder & Tschopp) + Abbas/Janeway, não de card curado. Declarado no relatório.

### Prioridades desta corrida (do § Diário de revisões)

| Entrada | Peso | O que isso obriga aqui |
|---|---|---|
| 2026-05-29 · biocel-07 — "sem slide ≠ sem figura", cadeia ≥4 setas sem figura | **alto** | Há slide farto (22 imagens). A cadeia TLR→MyD88→NF-κB→citocinas e a cadeia NLRP3→caspase-1→pró-IL-1β→IL-1β são multi-passo: **figura adjacente obrigatória** (slides 18/19 e 20/21). Nenhum parágrafo de cascata sem figura ao lado. |

Demais gates herdados sem entrada de diário: paridade banda dupla 0.80–1.25 em Q01–Q30; C/E sempre 4 itens; conclusão integradora em 4 camadas; cota de 1–2 caixas vermelhas/gold por PARTE; sem pergunta retórica.

## Seção B — Esqueleto das 3 PARTES

### PARTE I — Quem detecta a perda de homeostasia
- **1.1 Receptor pronto e receptor sorteado** — os dois modos de reconhecer; repertório clonal gerado aleatoriamente + selecionado nos órgãos linfoides primários; PRR já codificado na linhagem germinativa.
- **1.2 O que decide entre tolerar e responder** — o mesmo antígeno gera resposta ou tolerância; o fator de decisão é o **estado homeostático do tecido** de onde ele veio; ambos os desfechos geram memória; transplante e tumor como os dois lados da moeda.
- **1.3 A ponte da apresentação de antígenos** — APC captura moléculas *e* mede a homeostasia do tecido; leva as duas informações ao órgão linfoide secundário; sem o sinal da inata, o antígeno chega "desacompanhado".
- **1.4 DAMP, PAMP e as famílias de PRR** — o que os PRR leem; história do "danger" de Matzinger; as seis famílias e onde cada uma mora (membrana externa, endolisossomo, citoplasma, núcleo).

**Figuras planejadas:** slide-03 (repertório completo + seleção), slide-05 (tolerância × resposta com o estado homeostático no meio), slide-06 (mapa do reconhecimento hierárquico), slide-07 (ponte APC), slide-08 (tabela das famílias de PRR + DAMP/PAMP).

### PARTE II — O que a célula faz depois de detectar
- **2.1 Salvar o vizinho: interferons do tipo I** — a célula infectada avisa antes de morrer; bloqueio da replicação na vizinha; efeitos sistêmicos (os sintomas da gripe são do IFN, não do vírus).
- **2.2 Eliminar a célula doente: citotoxicidade** — morte induzida, não destruição; reconhecimento por receptor clonal *ou* inato; FasL–Fas e desgranulação; a efetora sai inteira para procurar o próximo alvo.
- **2.3 Limpar a área: a fagocitose em etapas** — quimiotaxia; complemento como PRR **solúvel**; opsonização e adesão; zíper; fagossomo + lisossomo; explosão respiratória.
- **2.4 Chamar socorro: citocinas e febre** — citocina como nome genérico e pleiotrópico; interleucinas, fatores de crescimento/CSF, interferons, quimiocinas; mediadores lipídicos do araquidônico; exossomos; a febre como mecanismo de defesa (experimento do lagarto).

**Figuras planejadas:** slide-09 (as quatro estratégias — mapa da PARTE), slide-10 (ação protetora do IFN), slide-11 (citotoxicidade em 3 tempos), slide-12 (etapas da fagocitose), slide-13 (mediadores da comunicação).

### PARTE III — Como o sinal entra na célula
- **3.1 Os toll-like receptors e onde eles moram** — origem do nome (Toll da drosófila); TLR1–11 e a lógica da localização (membrana plasmática lê superfície microbiana, endolisossomo lê ácido nucleico); a tabela não é uma lista fechada de ligantes.
- **3.2 Do ligante ao núcleo: MyD88 e TRIF** — dimerização ou mudança conformacional de dímero pré-formado; MyD88 → NF-κB/AP-1 → citocinas inflamatórias; TRIF → IRFs → interferon do tipo I.
- **3.3 Por que a mesma via dá saídas diferentes** — cruzamento entre as vias; sobrevivência (AKT) × apoptose (caspase-8); "anatomia do citoplasma" — a localização física das moléculas decide o desfecho.
- **3.4 O inflamassoma e a maturação da IL-1β** — NLR; NODs vão por NF-κB, NLRPs/AIM2 montam plataforma; caspase-1 cliva pró-IL-1β e pró-IL-18; exigência dos dois sinais; doenças inflamatórias hereditárias.

**Figuras planejadas:** slide-16 (ligantes dos TLR), slide-17 (ligantes dos demais PRR), slide-18 (esquema limpo das vias), slide-19 (figura densa do artigo — carrega o *cruzamento*), slide-20 (definição + famílias do inflamassoma), slide-21 (montagem do NLRP3).

**Cadeia multi-passo ≥5 etapas → figura obrigatória:** (a) fagocitose (2.3, slide-12); (b) TLR → adaptador → fator de transcrição → gene → citocina (3.2, slides 18/19); (c) sinal → montagem → caspase-1 → clivagem → liberação (3.4, slide-21).

## Seção B.bis — Registro de abertura por subtópico

| Subtópico | Registro |
|---|---|
| 1.1 | enquadramento |
| 1.2 | ponto-de-quebra |
| 1.3 | integração-posterior |
| 1.4 | analogia concreta |
| 2.1 | integração-anterior |
| 2.2 | ponto-de-quebra |
| 2.3 | analogia concreta |
| 2.4 | enquadramento |
| 3.1 | integração-anterior |
| 3.2 | ponto-de-quebra |
| 3.3 | enquadramento |
| 3.4 | integração-posterior |

Nenhum par vizinho compartilha registro. Sem pergunta âncora/retórica em nenhuma abertura (canônico 2026-05-29).

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta)

| Pré-requisito | Frase pronta (≤25 palavras) |
|---|---|
| Homeostasia | "Homeostasia é o tecido operando dentro da faixa em que suas células vivem bem — mesma temperatura, mesmo pH, mesmas moléculas nos lugares de sempre." |
| Apoptose | "Apoptose é morte programada: a célula desmonta o próprio conteúdo em pacotes de membrana intacta, sem derramar nada no tecido." |
| Fator de transcrição | "Fator de transcrição é a proteína que entra no núcleo, senta no promotor de um gene e autoriza a RNA-polimerase a transcrevê-lo." |
| Órgão linfoide primário × secundário | "Nos primários (medula e timo) o linfócito nasce e é filtrado; nos secundários (linfonodo, baço) ele encontra o antígeno já trazido de fora." |
| Lisossomo | "Lisossomo é a vesícula ácida cheia de enzimas digestivas que a célula usa para desmontar o que engoliu." |

## Seção C — Distribuição da E2

Profundidade **PADRÃO** → **10 Consolidação · 15 Integração · 5 Aplicação**.

- **Formatos:** 20 múltipla escolha · **10 Certo/Errado com 4 itens I–IV** (Q03, Q06, Q09, Q12, Q15, Q18, Q21, Q24, Q28, Q30) · **3 "assinale a incorreta"** (Q05, Q14, Q22, com `*incorreta*` sinalizado no stem).
- **Gabarito:** sorteado de verdade (script com guarda anti-degeneração). Distribuição MC: A=6, B=4, C=3, D=4, E=3 (máx 30%); nenhuma corrida ≥4; nenhuma string C/E degenerada (sem CECE/ECEC/CCCC/EEEE) e nenhum bloco de 5 C ou 5 E ao longo das 10 strings. Bloco `gabarito:` já preenchido no `.yml`.

### Termos-nota nominalmente obrigatórios (6–10)
`homeostasia` · `opsonização` · `quimiotaxia` · `explosão respiratória` · `desgranulação` · `pleiotrópico` · `plataforma molecular` · `priming`

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** tratar PRR e receptor clonal como dois nomes para a mesma coisa.
  **Correção:** o PRR já vem escrito no genoma e é idêntico em todas as células que o expressam; o receptor clonal é montado por recombinação aleatória e é único de cada clone. Um lê *categoria de molécula*, o outro lê *uma molécula específica*.
- **Quebra:** achar que "não-próprio" é o gatilho da resposta imune.
  **Correção:** o gatilho é a **perda de homeostasia** lida pelos PRR. Comida é não-própria e é tolerada; uma proteína própria liberada por célula que morreu mal é DAMP e desencadeia resposta.
- **Quebra:** ler DAMP como "molécula de bactéria danificada".
  **Correção:** DAMP é molécula **do próprio hospedeiro** que só aparece fora do lugar quando há dano — ATP no meio extracelular, DNA mitocondrial no citoplasma. PAMP é que é de micro-organismo.
- **Quebra:** imaginar a citotoxicidade como a célula efetora furando a célula-alvo.
  **Correção:** a efetora entrega um sinal (FasL–Fas ou grânulos) que **liga o programa de apoptose dentro do alvo**. Quem executa a morte é a célula-alvo; a efetora sai íntegra e vai buscar outra.
- **Quebra:** supor que o interferon salva a célula que o produziu.
  **Correção:** a célula infectada já está perdida. O IFN age nas vizinhas ainda sadias, deixando-as em estado antiviral antes de o vírus chegar. É gesto de vizinhança, não de autossalvamento.
- **Quebra:** achar que o inflamassoma transcreve IL-1β.
  **Correção:** o inflamassoma não liga gene nenhum. A transcrição da pró-IL-1β vem antes, por NF-κB. O inflamassoma ativa caspase-1, que **corta** a pró-forma já sintetizada. Sem os dois sinais não sai IL-1β madura.
- **Quebra:** ler a tabela de ligantes dos TLR como lista fechada.
  **Correção:** cada linha traz o ligante *típico* daquele receptor, não o único. O TLR4 é o exemplo do professor: canônico para LPS, mas reconhece também proteína viral e ligante próprio.
- **Quebra:** tratar febre como efeito colateral a ser suprimido.
  **Correção:** a febre é resposta efetora induzida pelos mediadores da inata. O lagarto impedido de se aquecer morre mais da infecção — o aumento de temperatura faz parte da defesa.

*(Voz de mecanismo em todos os itens; sem vocabulário de avaliação.)*

## Seção E — Exemplares-âncora

- **Exemplar 1.1 (universal)** — acerta o encadeamento parágrafo-a-parágrafo com cadeia mecanística completa ("ligante liga → canal abre → íon entra → despolariza"). Vou usar isso em **3.2** e **3.4**, escrevendo TLR→MyD88→NF-κB→citocina e sinal→plataforma→caspase-1→IL-1β como cadeias faladas inteiras, nunca como enfileiramento de siglas.
- **Exemplar 8.1/8.2 (universal, `atencao-box`)** — acerta o movimento de dois tempos: nomear a derrapada e depois entregar a fronteira memorizável. Vou usar isso em **1.4** (DAMP é do hospedeiro, não do micróbio) e em **3.4** (inflamassoma corta, não transcreve) — as duas inversões que derrubam o resto do capítulo se ficarem erradas.
- **Exemplar 14.1 (universal, siglas)** — acerta o uso inline do helper sem repetir o termo na prosa. Tema com carga de sigla altíssima (PRR, PAMP, DAMP, TLR, NLR, RLR, CLR, MyD88, TRIF, NF-κB, AP-1, IRF, IFN, IL, CSF, LPS, APC, ROS): cada uma entra dentro de frase com sujeito e verbo, nunca em rajada (3ª regra editorial).
- **Exemplar 3.1 (`#imuno`, abertura por desfazer confusão)** — acerta ao separar duas coisas que se misturam na cabeça do aluno *antes* de qualquer fórmula. Vou usar isso em **1.1**, separando "receptor pronto" de "receptor sorteado" antes de nomear PRR e TCR/BCR.
- **Exemplar 6.1 (`#receptores`, organização terminológica)** — acerta ao construir hierarquia explícita antes de definir termo por termo. Vou usar isso em **2.4**, montando citocina como guarda-chuva e interleucina/CSF/interferon/quimiocina como rótulos históricos por baixo dela — que é exatamente a queixa do professor sobre a nomenclatura.
- **Exemplar 16.1 (catálogo de família)** — acerta ao dar o princípio organizador antes da tabela. Vou usar isso em **1.4** (famílias de PRR pela **localização celular** como eixo) e em **3.1** (TLR pela lógica membrana-plasmática × endolisossomo).
- **Exemplar 17 (cadência dialogal)** — passada de olho para não deixar as PARTES II e III abrirem sempre em "O/A [substantivo]"; a PARTE II tem quatro estratégias paralelas e é onde o risco de quatro parágrafos gêmeos é maior.
- **Exemplares 11.x + 13.1 (Questionador)** — distratora com peça roubada da correta e motivador experimental curto. Aplicação natural aqui: trocar MyD88 por TRIF na mesma frase, trocar a direção do IFN (produtora × vizinha), trocar transcrição por clivagem no inflamassoma.

---

## Reprodutibilidade das figuras

Os PNGs em `figuras/imuno-02-reconhecimento-inato/` são gitignored (convenção do repo — só `MAPA_CONTEUDO.txt` é versionado). A fonte não é um slide solto, e sim a **transcrição da aula em PDF** (`Transcrição de Aula — IM: Reconhecimento inato no Sistema Imune`), em que cada página ímpar traz a imagem do slide e a página par seguinte traz a narração correspondente. Para regerar:

```python
import pymupdf
d = pymupdf.open("<transcricao>.pdf")
n = 0
for i, p in enumerate(d):
    imgs = p.get_images(full=True)
    if not imgs: continue
    n += 1
    pix = pymupdf.Pixmap(d, imgs[0][0])
    pix.save(f"figuras/imuno-02-reconhecimento-inato/slide-{n:02d}.png")
    # narração do slide n = texto de d[i+1]
```

`extrair_slides.py` não serve aqui: ele rasteriza páginas inteiras, e neste PDF a página é um documento de texto com o slide embutido.
