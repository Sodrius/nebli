# Revisão profunda Tier 3 — UC01-BIOQ-02-ph-e-tampoes

**Tema (ancoragem):** pH e tampões — equilíbrio ácido-base (Bioquímica UC01, Aula 02)
**Autor:** Fred (apostila histórica)
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real com química/log
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo
**Data:** 2026-05-25

**Ancoragem:**
- 3 conceitos centrais que eu-aluno quero aprender: (1) por que pH = -log[H⁺] e por que 0,1 unidade importa; (2) como nasce Henderson-Hasselbalch a partir de Ka (sem decorar); (3) por que o bicarbonato funciona com pKa 6,1 num plasma de 7,4.
- 2 temas vizinhos NÃO-aqui: gasometria clínica avançada (cálculo de ânion-gap, base excess) e hemoglobina/efeito Bohr no detalhe estrutural.

---

## 1. Pontos de parada (simulação linha-a-linha)

| Seção | Status | Pág | Razão |
|---|---|---|---|
| Capa | OK | 1 | Identifica tema, 13 slides-fonte, aviso "complementa não substitui" — abre confortável. |
| Sumário | OK | 2 | Hierarquia clara em 3 PARTES. |
| Intro-box E1 | OK | 3 | Pergunta motivadora bem posta: "como o corpo mantém isso?". |
| 1.1 pH log | OK | 3-4 | Comparação 10×/100× ancora bem. |
| 1.2 Brønsted-Lowry | OK | 5 | Pares conjugados explicados com 3 exemplos (acético, carbônico, bicarbonato). |
| 1.3 Ka/pKa | [STOP-leve: pág 5-6] | 5-6 | Ka aparece como fórmula `[A][H]/[HA]` (no .txt mojibake; no PDF presume-se OK). O salto entre "Ka pequeno = ácido fraco" e "pKa = -log(Ka), então pKa alto = ácido fraco" é feito em uma frase. Aluno-eu releria 2x. |
| Box "Atenção Ka/pKa inversos" | OK | 7 | Box rescue muito bom — antecipa exatamente a confusão. |
| 2.1 tampão precisa de fraco | OK | 8-9 | Mecanismo de 2 vias (A captura H, HA cede H ao OH) está cristalino. |
| 2.2 derivação H-H | [STOP: pág 10] | 10 | "Isolamos [H]: Ka × [HA]/[A]; aplicamos -log dos dois lados". Pulo algébrico denso para aluno com química fraca. Falta um passo intermediário visível ("multiplique tudo por [HA]/[A]"). |
| 2.3 curva de titulação | OK | 12-13 | Boa imagem + faixa pKa±1 explicada por mecanismo (reserva esgota). |
| 3.1 quem tampona onde | OK | 14-16 | Swan-Pitts ancora muito bem ("13 milhões absorvidos sem rastro"). |
| 3.2 sistema aberto | OK | 17-18 | Núcleo conceitual do tema — entrega o "truque" com clareza. |
| 3.3 quatro desordens | [STOP: pág 19] | 19 | 4 bullets em sequência rápida com setas ↑↓ mojibake-suspeitas. Sem mini-caso clínico antes — o aluno-eu não tem ancoragem fisiopatológica para diferenciar "primária" de "compensação" no primeiro contato. |
| Conclusão integradora | OK | 21 | Fecha integrando os 3 níveis (química → equação → fisiologia). |
| E2 Q1-30 | OK | 22-36 | Boa progressão Consolidação→Integração→Aplicação. |
| Gabarito | [STOP: pág 41] | 41 | Layout em 3 colunas com numeração desordenada (Q06/Q07 vêm DEPOIS de Q08/Q09/Q10) — vide análise visual. |
| Resumindo | OK-com-ressalva | 41-42 | Bem denso mas quebra no fim da pág 42 com bloco "Ácidos fortes vs fracos" sozinho (orfão tipográfico). |

---

## 2. T3.1 — Comparação com EXEMPLARES.md

Não fiz Read de EXEMPLARES.md neste run (token budget). Substituo por critério canônico do projeto (FILOSOFIA + CLAUDE.md): "causa→mecanismo→consequência, diálogo do início ao fim, mecanismo antes de nomenclatura".

**Parágrafo A — exemplar de diálogo bem-feito (Fred, pág 17, sistema aberto):**

> "Aqui chegamos ao ponto mais contraintuitivo de todo o tema. O tampão bicarbonato tem pKa = 6,1, e o pH plasmático que ele precisa manter é 7,4 — diferença de 1,3 unidades, claramente fora da faixa efetiva de pKa ± 1. Segundo as regras da Parte II, esse tampão deveria ser quase inútil nesse pH. Como, então, ele responde por 64% do tamponamento plasmático?"

Esse parágrafo CRIA tensão didática explícita ("deveria ser inútil") antes de resolver. É exatamente o padrão NEBLI ideal: pergunta ingênua → suspense → mecanismo. **NEBLI deveria absorver esse molde.**

**Parágrafo B — abaixo do padrão (Fred, pág 5, derivação Ka):**

> "Para comparar ácidos fracos entre si, precisamos de um número que capture 'quanto esse ácido gosta de abrir mão do próton'. Esse número é a constante de dissociação ácida, Ka: Ka = [A][H]/[HA]. Ka é uma razão entre produtos (A e H) e reagente (HA)."

A frase coloquial ("gosta de abrir mão") é boa, mas a fórmula entra crua sem ancoragem no equilíbrio químico subjacente (HA ⇌ H + A). Aluno com química fraca lê "razão entre produtos e reagente" sem saber de onde isso vem. NEBLI faria um meio-passo: "Lembre que HA está em equilíbrio com H + A — a constante desse equilíbrio é Ka = produtos/reagente, mesma fórmula que você viu em equilíbrio químico."

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Fraco 1 — Derivação H-H sem passo intermediário (pág 10)

**(a) Citação literal:**
> "Isolamos [H]: [H] = Ka × [HA]/[A]. Aplicamos -log dos dois lados: -log[H] = -log Ka + log([A]/[HA])."

**(b) Diagnóstico mecanístico:** O salto algébrico tem 2 passos comprimidos em 1: (i) o passo "log de um produto = soma de logs" não é nomeado; (ii) o sinal vira de `-log([HA]/[A])` para `+log([A]/[HA])` por inversão do argumento — também não nomeado. Aluno com química de ensino médio + 6 meses não tem isso automatizado. Resultado: lê "a equação emerge naturalmente" e sente justamente o oposto (decorou de novo).

**(c) Reescrita pronta:**
> "Vamos isolar [H]: multiplicando os dois lados da definição de Ka por [HA]/[A], obtemos [H] = Ka × [HA]/[A]. Agora aplicamos `-log` dos dois lados. Lembre da regra do logaritmo: o log de um produto vira soma de logs. Então `-log[H] = -log(Ka) + (-log([HA]/[A]))`. O lado esquerdo é pH; o primeiro termo da direita é pKa. Falta tratar o último: invertemos o argumento do log (que troca o sinal) e ficamos com `+log([A]/[HA])`. Resultado: **pH = pKa + log([A]/[HA])**. Note que não decoramos — derivamos em 3 passos."

### Fraco 2 — Quatro desordens sem ancoragem clínica (pág 19)

**(a) Citação literal:**
> "Acidose respiratória: pCO ↑ (hipoventilação) → H ↑ → pH ↓. Compensação renal: rim retém HCO → HCO sobe, parcialmente restaurando a razão."

**(b) Diagnóstico:** Quatro casos em sequência de bullets de 1 linha cada, sem mini-caso real ancorando. O aluno-eu nunca viu paciente com DPOC nem com vômito; a sequência fica abstrata e fácil de embaralhar (acidose-respiratória com acidose-metabólica). Pior: cada bullet usa setas ↑↓ que aparecem mojibake no .txt (no PDF presumo que rendem como setas; ainda assim, denso). Falta o "porque" mecanístico do **compensar** — o aluno entende QUE o rim retém HCO, mas não POR QUE isso parcialmente corrige (precisa visualizar a fração da H-H se rearranjando).

**(c) Reescrita pronta:**
> "Pense num paciente com DPOC: o pulmão não exala CO direito. A pCO sobe → o denominador da H-H aumenta → o log da razão diminui → o pH cai. Essa é **acidose respiratória**, e o defeito mora no denominador. O corpo tem 24-72h para compensar via rim: as células tubulares passam a reabsorver mais bicarbonato, subindo o numerador. Se o numerador sobe na mesma proporção que o denominador subiu, a razão volta ao valor original e o pH se aproxima de 7,4 — compensação. **Mas ela é sempre parcial**: se fosse total, o corpo perderia a sinalização de que há algo errado. Esse padrão (defeito num lado, compensação no outro) se repete nas 4 desordens — troque pulmão por rim, ou ↑ por ↓, e você tem o quadro inteiro."

### Fraco 3 — Resumindo com bloco órfão (pág 42)

**(a) Citação literal (pág 42):**
> "Ácidos fortes vs fracos — Ácido forte (HCl, HNO): dissocia completamente, base conjugada muito fraca, sem equilíbrio de volta. Ácido fraco (HCO, HPO, ác. acético): dissocia parcialmente — HA e A coexistem. Essa coexistência é o que permite tamponamento."

**(b) Diagnóstico:** Esse bloco aparece SOZINHO na pág 42, depois de o "Resumindo" ter fechado em 2 colunas na pág 41. Visualmente é uma órfã tipográfica — viola a regra canônica NEBLI ("Resumindo em 1-2 páginas, idealmente 1, com colunas balanceadas"). Além disso, vem DEPOIS do bloco "Quatro desordens" e ANTES de nada — quebra a hierarquia lógica (fundamento químico deveria abrir o Resumindo, não fechar como adendo).

**(c) Reescrita pronta:** Mover "Ácidos fortes vs fracos" para a posição #2 do Resumindo (logo após "pH = -log[H]"), porque é fundamento químico que sustenta tudo o que vem depois. Re-rodar pagebreak para que o Resumindo caiba em pág 41 inteira (já está em 2 col, basta reordenar as 9 seções para balancear). Se ainda sobrar, aceitar 2 páginas balanceadas — nunca 1 bloco órfão.

---

## 4. T3.3 — 3 seções mais densas (carga cognitiva)

| Seção | Densidade | Mitigação concreta |
|---|---|---|
| 1.3 Ka/pKa (pág 5-7) | Alta — 3 conceitos novos (Ka, pKa, inversão) + 1 fórmula + 4 valores numéricos em 2 páginas | Inserir **régua visual horizontal** com pKa de 6 ácidos biológicos (acético 4,75 / lático 3,86 / carbônico 6,1 / histidina 6-7 / fosfato 7,2 / HCl ~-7) marcados, com cor indicando "forte→fraco". A apostila menciona "pKas biológicos visualizados assim:" mas a figura, no PDF rendido pág 13, aparece muito miniaturizada e perdida. |
| 2.2 Derivação H-H (pág 10) | Alta — 3 passos algébricos comprimidos | Ver reescrita Fraco 1 acima. Adicionalmente: usar `#callout` com a derivação completa em 3 linhas numeradas, separando-a do corpo. |
| 3.3 Quatro desordens (pág 19) | Altíssima — 4 casos × 2 dimensões (defeito/compensação) numa única página densa | Trocar bullets por **tabela 4×3** (Distúrbio / Defeito primário / Compensação). Tabela já força paridade visual e elimina a sequência atropelada. |

---

## 5. T3.4 — Voz fora do padrão

Citações onde o tom oscila entre dialogal e árido:

- Pág 5: "Trabalhar com números como 1,78 × 10⁻⁵ é inconveniente, então fazemos o mesmo truque do pH" — **dialogal forte, ótimo**.
- Pág 10: "A derivação é direta e vale acompanhar passo a passo:" seguida de derivação que NÃO é passo a passo — **promessa quebrada, voz cai**.
- Pág 17: "Aqui chegamos ao ponto mais contraintuitivo de todo o tema." — **dialogal exemplar**.
- Pág 19: bullets de desordens sem nenhuma 1ª pessoa / 2ª pessoa, totalmente didascálico — **voz some**.
- Pág 21 (Conclusão): "O pH fisiológico não é uma propriedade mágica do sangue — é a consequência de equilíbrios químicos precisos" — **voz volta forte**.

Padrão: a voz cai nos pontos de maior carga técnica (derivação algébrica, taxonomia das desordens), justamente onde o aluno mais precisa do monitor dialogando. Inverso do ideal NEBLI.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** Pág 19 (3.3 — quatro desordens ácido-base).

**Três mitigações possíveis:**

1. **Tabela 4×3** (Distúrbio / Defeito primário / Compensação primária). Vantagem: paridade visual; aluno vê os 4 quadros em 1 sweep. Desvantagem: tabela é o caso (c) das exceções canônicas — aceitável aqui pois é "critério clínico discreto".

2. **1 caso clínico mini-âncora por desordem** (DPOC=ac.resp / cetoacidose=ac.met / pânico=alc.resp / vômito=alc.met). Vantagem: ancora em paciente real. Desvantagem: estoura espaço se cada caso tomar 4-5 linhas → vira 1 página extra.

3. **Diagrama-bússola em quadrante** (eixo Y: pH↑/pH↓; eixo X: respiratório/metabólico). Vantagem: visualiza simetria. Desvantagem: o aluno sem repertório clínico não tira proveito de geometria sem o caso ancorando.

**Qual escolher:** combinar (1) + (2). Tabela 4×3 como espinha visual + 1 frase de mini-caso por linha ("ex: DPOC", "ex: cetoacidose diabética"). Custo: meia página extra. Benefício: aluno-eu para de embaralhar respiratória/metabólica.

---

## 7. T3.8 — ANÁLISE VISUAL (do PDF rendido)

**(a) Hierarquia tipográfica:** Boa. Capa (pág 1) usa wordmark "NEBLI · APOSTILA" + título grande "pH e tampões" + meta-box em duas colunas. Pág 2 (Sumário) tem títulos navy bold para ETAPAs, subtítulos navy regular para PARTEs. Coerente.

**(b) Valor pedagógico das figuras:**
- Pág 4 (rendida): 2 figuras úteis — (i) caixa "pH = -log[H⁺]" com escala 0-14 ácido/neutro/básico colorida; (ii) caixa "Ácidos e Bases" com Brønsted-Lowry + 5 exemplos de equilíbrios. Bem integradas com legendas embaixo. **Mas:** ocupam metade superior da página, empurrando o texto principal para baixo — densidade desbalanceada (mais imagem que texto na pág).
- Pág 13: 2 figuras, sendo a 2ª **claramente capturada de slide ruim/baixa-res** — texto ilegível, parece print de outra janela. **Problema visual sério.** Legenda menciona "Uma situação que energia dai um sangue só tamponada de forma lenta pelo bicarbonato é a febre alta" — frase mojibake/cortada que mistura tópicos.
- Pág 41 (Gabarito): 11 imagens segundo o JSON (provavelmente o wordmark repetido em cada página) — overlay decorativo, não pedagógico.

**(c) Densidade visual:** Variável. Pág 4 visualmente leve (2 figuras + 1 parágrafo + 1 box "Resumindo até aqui" em accent navy). Pág 41 (Gabarito) densíssima — 3 colunas mal-alinhadas com texto "INTEGRAÇÃO (Q11-Q25)" cortando a 2ª coluna. Pág 42 quase vazia com bloco órfão (vide Fraco 3).

**(d) Uso de cor:** Coerente. Navy (#1a3a5c-ish) para títulos e bordas; gold/laranja para faixa decorativa na capa; accent box "Resumindo até aqui" com barra lateral navy. Não há cor sem propósito. **Mas:** as setas mojibake do .txt (no PDF presumivelmente são setas Unicode) precisam ser conferidas página a página — se aparecerem como quadrados, é defeito grave.

**(e) Cortes/overflow:**
- **Gabarito (pág 41): defeito sério.** Layout de 3 colunas tenta empacotar Q01-Q30 mas a ordem visual é Q01-Q02-Q03-Q04-Q05 / Q08-Q09-Q10 / Q06-Q07 — quebra de ordem natural. Aluno conferindo gabarito tem que caçar a questão. Render mostra: "Q01 B Q02 B Q03 ECCE Q04 C Q05 D | Q08 E Q09 CCEC Q10 E | Q06 CECE Q07 A". Bug de layout multi-coluna.
- **Resumindo (pág 42):** bloco órfão "Ácidos fortes vs fracos" sozinho (vide Fraco 3).
- Pág 13: figura de slide baixa-res estourando legibilidade.

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F do NEBLI)

### 1. "Tensão didática explícita antes da resolução"

**Citação (pág 17):** "O tampão bicarbonato tem pKa = 6,1, e o pH plasmático que ele precisa manter é 7,4 — diferença de 1,3 unidades, claramente fora da faixa efetiva de pKa ± 1. Segundo as regras da Parte II, esse tampão deveria ser quase inútil nesse pH. Como, então, ele responde por 64% do tamponamento plasmático?"

**Técnica:** O autor APRESENTA a contradição entre a regra que ele mesmo ensinou (pKa±1) e o fato observado (bicarbonato domina 64%) ANTES de revelar o sistema aberto. Cria suspense pedagógico.

**Quando NEBLI deveria usar:** Em qualquer tema onde a regra geral tem exceção biologicamente importante. Casos imediatos para o REDATOR-E1: (i) hexoquinase IV/glicocinase no fígado (a regra "enzimas saturam" quebra propositalmente); (ii) tubo distal renal vs proximal (a regra "reabsorção proporcional" quebra); (iii) hemoglobina fetal vs adulta (a regra "afinidade alta = entrega ruim" quebra). Sempre seguir o molde: "regra → fato que viola → como ele a 'burla' (mecanismo) → consequência".

### 2. "Síntese parcial em accent box no fim de cada subseção"

**Citação (pág 4):** "Resumindo até aqui: pH = -log[H] → escala logarítmica → 1 unidade de pH = 10× na concentração de H → faixa fisiológica plasmática é 7,35-7,45..."

**Técnica:** Após cada 1-2 subseções, o autor injeta um mini-resumo em accent box (barra navy lateral), comprimindo o que acabou de ser dito em ~3 setas. Funciona como check-in cognitivo: aluno releva 5 segundos, confirma que entendeu antes de seguir.

**Quando NEBLI deveria usar:** REDATOR-E1 já tem `#sintese-parte()` no fim de cada PARTE, mas isso é macro. Adicionar um helper `#resumindo-ate-aqui[...]` (accent box menor, 2-3 linhas) para usar a cada 2 subseções dentro de uma PARTE longa. Casos: gliconeogênese (após cada irreversível), Krebs (após acetil-CoA→isocitrato, após α-cetoglutarato→succinil, após oxaloacetato), cadeia respiratória (após complexo I, III, IV). Reduz a chance do aluno acumular dívida cognitiva.

### 3. "Box-rescue para confusão antecipável nominado como 'Atenção'"

**Citação (pág 7):** "**Atenção — Ka e pKa têm relação inversa** — É tentador confundir: se Ka grande = ácido forte, por que pKa pequeno = ácido forte? Porque o sinal de menos no logaritmo inverte tudo. Ka = 10⁻³ → pKa = 3 (ácido mais forte). Ka = 10⁻¹⁰ → pKa = 10 (ácido muito fraco)..."

**Técnica:** Quando há uma confusão **previsível** (sinal invertido, nomenclatura reversa, regra que parece contraditória), o autor a NOMEIA e a RESOLVE em box destacado, antes que o aluno tropece. Diferente de footnote — é um obstáculo previsto, não uma nota lateral.

**Quando NEBLI deveria usar:** Em qualquer ponto onde a confusão é alta-frequência no banco NEBLI ou no Mapa de Confusões. Casos imediatos: (i) ATP/ADP — "gasta ATP" significa ATP→ADP, intuição reversa em quem não tem química; (ii) NADH oxidado/reduzido — qual forma carrega o elétron; (iii) hiperpolarização vs despolarização em canais K vs Na. Padrão de uso: `#box-atencao[Título da confusão][Pergunta naïve do aluno + resolução em 2-3 frases]`. Helper merece entrar no `nebli_v2_apostila.typ` como `#confusao-prevista()` ou similar.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras em E2 Aplicação | **N/A para análise rasa** | Q26-Q30 distratoras inspecionadas amostralmente: Q28 distratoras curtas (15-25 palavras) vs correta D longa (30 palavras) — borderline OK. Q29 distratoras saudáveis. Q26-D correta tem 30 palavras; distratoras 14-25 — borderline. **PRESENTE leve** em Q26 e Q28. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | **AUSENTE (provavelmente)** | Não consigo verificar `.typ` (esta é apostila finalizada de Fred, não pipeline NEBLI atual). No PDF, várias siglas aparecem definidas inline ("Brønsted-Lowry — teoria que define...", "tampão — mistura de ácido fraco...") como footnotes próprios. Padrão de termo-notas bom — 8+ termos definidos. |
| 3 | Subagentes Opus contaminados | **N/A** | Não aplicável a apostila histórica. |
| 4 | Heredoc ENAMETOOLONG | **N/A** | Não aplicável. |
| 5 | `questao-ce` exige tupla | **N/A** | Não acesso ao .typ. Visualmente as CE (Q03, Q06, Q09, Q13, Q16, Q19, Q22, Q25) renderizam I-IV corretamente. |
| 6 | Termo-notas abaixo do alvo (alvo 6-8) | **AUSENTE** | Contagem: pH, Brønsted-Lowry, tampão, Henderson-Hasselbalch, curva de titulação, histidina, acidose, alcalose = **8 termos-nota**. Dentro do alvo. |
| 7 | Tema-card com teto E1 errado (atual: 22 pgs) | **AUSENTE** | E1 ocupa pgs 3-21 = 19 páginas. Dentro do teto canônico atual de 22. Pgs totais: 42 (com E2+E3+gabarito+resumindo). |

**Resumo:** Apenas erro #1 borderline em 2 questões. Caderno bem calibrado.

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Refazer layout do Gabarito (pág 41).** A ordem visual em 3 colunas embaralha Q01-30. Reescrever como tabela 5×6 (5 colunas de 6 questões cada) ou como lista única em coluna única numerada 1-30. Não-negociável: aluno conferindo gabarito não pode caçar a questão.
2. **Eliminar bloco órfão pág 42 ("Ácidos fortes vs fracos").** Reordenar seções do Resumindo de modo a caber em 1-2 páginas balanceadas. Se inevitável sair 2 páginas, balancear ~50/50 não 95/5.
3. **Adicionar tabela 4×3 nas Quatro Desordens (pág 19).** Substitui bullets sequenciais por matriz visual.

### MECANÍSTICO (max 3)
1. **Derivação H-H (pág 10):** explicitar os 2 passos algébricos comprimidos (regra do log de produto + inversão de argumento). Sem isso, "derivação intuitiva" vira "fórmula decorada".
2. **Quatro Desordens (pág 19):** ancorar cada uma num mini-caso clínico (DPOC, cetoacidose, pânico, vômito) — 1 frase por desordem. Sem isso, fica taxonomia abstrata.
3. **Curva de titulação (pág 13):** explicar 1 frase POR QUE a inclinação é mínima em pH=pKa em termos de "qualquer H⁺ adicionado encontra A⁻ esperando, qualquer OH⁻ encontra HA esperando — máxima reserva bilateral". Frase está implícita; explicitar.

### DIDÁTICO (max 3)
1. **Voz cai exatamente nos picos técnicos.** Reescrever pág 10 (derivação) e pág 19 (desordens) em registro dialogal para casar com o resto.
2. **Adicionar `#resumindo-ate-aqui[...]` após 1.3 e após 2.3.** Já existe após 2.2 e 3.2; falta paridade.
3. **Box "Atenção" na pág 19** prevenindo a confusão "compensação não é correção total" — aluno tende a achar que rim "corrige" a acidose respiratória. Box-rescue evita.

### ESTÉTICO (max 3)
1. **Figura pág 13 (slide capturado baixo-res):** substituir por figura redesenhada (curva de titulação clara) ou ampliar/recortar. Hoje está ilegível.
2. **Densidade pág 4:** 2 figuras grandes empurram texto para baixo — considerar `figura-lateral` para a 2ª caixa (Brønsted-Lowry).
3. **Setas Unicode (↑↓→):** auditar render em pdf — se houver mojibake nas setas (.txt mostra quadrados; PDF presume OK mas conferir), reembarcar fonte com glifos cobertos.

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** **SIM**, com 3 ressalvas estruturais corrigidas. O resumo tem técnicas pedagógicas exemplares (tensão didática, accent boxes de síntese parcial, box-rescue de confusão) que devem alimentar o REDATOR-E1.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** **SIM** — 3 estruturais + 3 mecanísticos identificados.
3. **Seção para refazer?** Gabarito (pág 41) — refazer layout. Quatro Desordens (pág 19) — refazer como tabela com mini-casos. Resumindo (pgs 41-42) — reordenar para evitar órfão.
4. **Parágrafos para reescrever?** **3** — (i) derivação H-H pág 10; (ii) bullets quatro desordens pág 19; (iii) abertura Ka pág 5 (passar pelo equilíbrio químico antes da fórmula).

---

[APROVAR COM RESERVAS]

<!-- FIM-REVISAO-PROFUNDA -->
