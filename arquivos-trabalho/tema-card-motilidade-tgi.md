# TEMA CARD — Motilidade do TGI

## Seção A — Identidade e réguas da corrida

- **Tema:** Motilidade do trato gastrointestinal — bases neuromusculares
- **Slug:** `motilidade-tgi`
- **Aula curta (Drive/deck/PDF):** `Motilidade do TGI`
- **Disciplina:** Fisiologia do sistema digestório
- **Docente:** Fran Goulart da Silva (ICB/USP) — sigla `FGS`
- **Onde estudar:** Berne & Levy, *Fisiologia* — capítulo de motilidade do trato gastrointestinal (a figura 9-17 do slide sai daí) · Guyton & Hall, *Tratado de Fisiologia Médica* — princípios gerais da função gastrointestinal · Boron & Boulpaep, *Fisiologia Médica* — músculo liso e organização do sistema nervoso entérico
- **Alvo de páginas E1:** piso 2 · **teto 15** (canônico 2026-09-03)
- **Formato:** 3 PARTES × 3 subtópicos = **9 subtópicos**, 450–550 palavras cada → miolo-alvo ~5.000 palavras

### Recorte slide × tema

O slide cobre os **fundamentos neuromusculares da motilidade**, não a motilidade órgão a órgão. Ele abre em cinco frentes: (1) que músculo move o tubo e em que proporção; (2) inervação intrínseca (SNE) versus extrínseca (SNA); (3) integração dos reflexos curto e longo; (4) os cinco esfíncteres e a regra da distensão; (5) o acoplamento excitação-contração do músculo liso, da junção neuroefetora até a via RhoA/ROCK.

**Não entram nesta corrida** (são de aula posterior): deglutição em fases, complexo motor migratório, peristalse e segmentação intestinais, reflexo gastrocólico, defecação, absorção. O resumo entrega o **aparato**; a aula seguinte entrega o **repertório de padrões motores**.

### Teto histórico e degrau

- **Teto histórico do conteúdo.** A UC-8 não tem acervo de provas indexado no banco NEBLI (`banco/aulas_uc08.yml` não existe; o acervo de calibração em `referencias-externas/uc03/` é escopado à UC03 e foi ignorado, como manda o canônico). O teto foi calibrado pelo próprio slide + bibliografia: nomear os dois plexos e sua divisão de trabalho, separar reflexo curto de longo, listar os esfíncteres e o sinal da distensão, e percorrer a cadeia Ca²⁺ → calmodulina → MLCK → contração com o relaxamento por extrusão e miosina fosfatase.
- **Degrau que a E1 acrescenta (um por subtópico, diretriz 17).** 1.1 células intersticiais de Cajal como marcapasso da onda lenta · 1.2 estado *latch* (por que o tônus é barato em ATP) · 1.3 aganglionose de Hirschsprung como o experimento natural do SNE · 2.1 lei do intestino (polarização oral-excitatória / aboral-inibitória do reflexo peristáltico) · 2.2 íleo paralítico pós-operatório pelo reflexo inibitório simpático · 2.3 relaxamento transitório do EEI e a acalásia como perda do ramo inibitório · 3.1 por que a junção neuroefetora é lenta e difusa (fenda ampla, sem placa motora) · 3.2 miosina fosfatase como alvo regulável, e não apenas como "desligar" · 3.3 nitrato → GMPc → PKG → ativação da MLCP, o ramo farmacológico da mesma alavanca.

### Prioridades desta corrida (do § Diário de revisões do MEMORY.md)

1. **Registro científico (2026-09-03, peso alto).** Jargão exato na mesma frase da definição — `MLCK`, `miosina fosfatase`, `varicosidade`, `sincício funcional` entram nomeados, não parafraseados. Filtro das três funções aplicado subtópico a subtópico antes de fechar.
2. **Teto de 15 páginas / 8–10 subtópicos / miolo ≤ 6.000 palavras** (gates do `precompile-check` e do `pos_pipeline_check`). Orçamento prévio: 9 subtópicos × ~500 palavras.
3. **Consolidação decoreba** com alternativas de 10–20 palavras (gate `check_consolidacao_decoreba`).
4. **Figura mesmo quando o slide é econômico** (`biocel-07`, peso alto): o slide tem 6 páginas, então as figuras vêm de **recortes por unidade de mecanismo** — os slides 4 e 5 carregam dois e três mecanismos distintos cada, e foram fatiados em vez de reproduzidos inteiros.

---

## Seção B — Esqueleto das 3 PARTES

### PARTE I — O músculo e a rede nervosa que o comanda
- **1.1** Músculo liso visceral: sincício elétrico e o marcapasso das ondas lentas
- **1.2** Contração fásica e contração tônica: dois modos de ocupar o tempo
- **1.3** Sistema nervoso entérico: o plexo mioentérico move, o submucoso secreta

Figuras: `fig-tubo` (mapa do tubo, lateral 34%) · `fig-fasico-tonico` (Berne & Levy, 60%) · `fig-inervacao` (SNE × SNA, 66%)

### PARTE II — Reflexos: o tubo que decide sozinho e o tubo que consulta o encéfalo
- **2.1** Reflexo curto intramural: mecanorreceptor, acetilcolina e VIP/NO
- **2.2** Reflexo longo vago-vagal e o comando extrínseco do SNA
- **2.3** Esfíncteres: tônus de repouso e o relaxamento comandado pela distensão

Figuras: `fig-reflexos` (integração curto × longo, 74%) · `fig-esfincteres` (os cinco esfíncteres + piloro, 58%)

### PARTE III — Da membrana à força: acoplamento excitação-contração
- **3.1** Junção neuroefetora e as varicosidades: a sinapse sem endereço fixo
- **3.2** Ca²⁺/calmodulina → MLCK → cadeia leve fosforilada, e o caminho de volta
- **3.3** GPCR: Gq/PLCβ/IP₃ e a sensibilização ao Ca²⁺ pela via RhoA/ROCK

Figuras: `fig-juncao` (varicosidades, lateral 38%) · `fig-calmodulina` (Ca²⁺→CaM→MLCK→miosina ativada, 62%) · `fig-cascata-ca` (contração × relaxamento, 68%) · `fig-gpcr` (Gq e G12/13, 72%)

**Cadeia multi-passo ≥5 etapas → figura obrigatória:** satisfeita em 3.2 (`fig-calmodulina` + `fig-cascata-ca`) e em 3.3 (`fig-gpcr`).

---

## Seção B.bis — Registro de abertura por subtópico

| Subtópico | Registro | Nenhum vizinho repete |
|---|---|---|
| 1.1 | enquadramento | — |
| 1.2 | ponto-de-quebra | ✓ |
| 1.3 | analogia concreta | ✓ |
| 2.1 | integração-anterior | ✓ |
| 2.2 | enquadramento | ✓ |
| 2.3 | ponto-de-quebra | ✓ |
| 3.1 | analogia concreta | ✓ |
| 3.2 | integração-anterior | ✓ |
| 3.3 | integração-posterior | ✓ |

Pergunta âncora / retórica / ingênua: **banidas** (canônico 2026-05-29).

---

## Seção B.ter — Pré-requisitos cruzados (frase-âncora pronta, ≤25 palavras)

| Pré-requisito | Frase pronta para colar na 1ª aparição |
|---|---|
| Canal de Ca²⁺ voltagem-dependente | "Canais de cálcio tipo L abrem quando a membrana despolariza e deixam entrar cálcio a favor de um gradiente de dez mil vezes." |
| Junção neuromuscular esquelética | "No esquelético, a acetilcolina cai numa placa motora de 50 nm e cada axônio comanda suas fibras e mais nenhuma." |
| Receptor acoplado à proteína G | "Um receptor acoplado à proteína G atravessa sete vezes a membrana e, ao ligar o agonista, troca GDP por GTP na subunidade α." |
| Troponina C do músculo estriado | "No estriado, o cálcio liga-se à troponina C e o alvo é o filamento fino; no liso não existe troponina, e o alvo é a miosina." |
| Segundos mensageiros IP₃ e DAG | "A fosfolipase C parte o PIP₂ da membrana em dois: IP₃ solúvel, que libera cálcio estocado, e DAG, que fica na membrana e ativa a PKC." |

---

## Seção C — Distribuição da E2

**PADRÃO — 10 Consolidação · 15 Integração · 5 Aplicação.** Escolha justificada: a aula tem alta densidade de nomenclatura decorável (dois plexos, cinco esfíncteres, dois neurotransmissores do ramo inibitório, duas proteínas-alvo da fosforilação) que pede Consolidação cheia, e uma cadeia mecanística longa que sustenta 15 Integrações sem forçar.

- **Formato:** ~10 itens Certo/Errado (4 assertivas I–IV cada, gate hard) distribuídos pelas três categorias; 2–3 "assinale a incorreta"; o resto múltipla escolha A–E.
- **Gabarito:** sorteado de verdade. Para C/E, a sequência é **lida das assertivas depois de escritas** (`ERROS.md` #23) e só então gravada no YAML — nunca sorteada antes.
- **Paridade:** banda dupla 0.80–1.25 em Q01–Q30; alternativas de Consolidação em 10–20 palavras.

---

## Seção D — Pontos de quebra do raciocínio

- **Quebra:** tratar o plexo mioentérico e o submucoso como sinônimos de "sistema nervoso entérico" com funções intercambiáveis.
  **Correção:** o mioentérico fica entre as camadas musculares circular e longitudinal e governa contração e relaxamento; o submucoso fica sob a mucosa e governa secreção e fluxo sanguíneo local. A posição anatômica prediz a função.

- **Quebra:** localizar o corpo do neurônio do reflexo curto fora da parede do tubo.
  **Correção:** o arco inteiro — mecanorreceptor sensitivo, interneurônio e motoneurônio — está dentro da parede. É por isso que um segmento de intestino desnervado e isolado ainda propaga conteúdo.

- **Quebra:** supor que o parassimpático "manda" no tubo e o sistema entérico apenas executa.
  **Correção:** o entérico gera o programa motor completo sozinho; o vago modula ganho. A fibra pré-ganglionar vagal faz sinapse em neurônio entérico, e não diretamente no músculo.

- **Quebra:** ler o esfíncter como um anel que se contrai quando o alimento chega.
  **Correção:** o esfíncter está contraído em repouso, por tônus; o evento fisiológico é o **relaxamento** disparado pela distensão a montante. Contração é o estado basal, não a resposta.

- **Quebra:** transferir a troponina C do músculo estriado para o liso.
  **Correção:** o liso não tem troponina. O cálcio liga-se à calmodulina, e o complexo ativa a quinase da cadeia leve da miosina — a regulação é sobre o filamento **grosso**, não sobre o fino.

- **Quebra:** concluir que a queda do cálcio citosólico basta para relaxar.
  **Correção:** enquanto a cadeia leve permanecer fosforilada, a ponte cruzada continua ciclando. O relaxamento exige a **miosina fosfatase** removendo o fosfato; a queda do cálcio apenas interrompe a fosforilação nova.

- **Quebra:** achar que mais força exige obrigatoriamente mais cálcio.
  **Correção:** a via RhoA/Rho-quinase inibe a miosina fosfatase, e a mesma concentração de cálcio passa a render mais fosforilação e mais força. É sensibilização ao cálcio, e sustenta o tônus prolongado do esfíncter.

- **Quebra:** esperar que a contração fásica e a tônica venham de mecanismos moleculares diferentes.
  **Correção:** o maquinário é o mesmo; o que muda é a duração do estímulo e o balanço entre quinase e fosfatase. A tônica mantém força com pouca fosforilação nova por meio de pontes cruzadas de ciclagem lenta.

---

## Seção E — Exemplares-âncora (`EXEMPLARES.md`)

- **Categoria 1 — explicação mecanística parágrafo-a-parágrafo** (universal). Gesto: cada parágrafo com uma função discreta, cadeia causal completa sem salto. Onde aplicar: 3.2 e 3.3, que são as cadeias mais longas do resumo.
- **Categoria 8 — `atencao-box`** (universal). Gesto: dois movimentos no mesmo box, quebra e correção. Onde aplicar: uma por PARTE, no máximo — o esfíncter contraído em repouso (II) e a fosfatase que falta para relaxar (III).
- **Categoria 14 — siglas em footnote** (universal). Onde aplicar: SNE, SNA, VIP, NO, MLCK, GPCR, IP₃, DAG, EEI, EES.
- **Categoria 7 — analogia construtiva.** Gesto: analogia que carrega mecanismo, não decoração. Onde aplicar: 3.1, a varicosidade como "regador" contra a "seringa" da placa motora.
- **Categoria 17 — cadência dialogal** (leitura leve). Onde aplicar: PARTE II, para não deixar a sequência de reflexos virar catálogo.
- **Ressalva 2026-09-03 aplicada:** os exemplares foram lidos pelo **gesto**; a superfície da frase segue o § Registro científico (jargão na mesma frase da definição, zero pergunta retórica, zero moldura).
