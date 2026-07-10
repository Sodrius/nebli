# Revisão profunda Tier 3 — UC01-BC-03-compartimentos-intracelulares-i

**Tema (ancoragem):** Compartimentos intracelulares I — por que compartimentar, três vias de transporte, núcleo, mitocôndria, peroxissomo.
**Autor:** Patrícia Coltri (atribuído); PDF renderizado no template NEBLI v2 — análise trata o conteúdo como apostila histórica reaproveitada no formato.
**Personagem:** aluno FMUSP turma 114, 1º ano, dificuldade real com biologia celular molecular.
**Avaliador:** Opus via general-purpose simulando revisor-pdf-profundo.
**Data:** 2026-05-25

**Ancoragem:**
- 3 conceitos centrais que o aluno-alvo quer aprender: (1) por que a célula gasta energia construindo membrana, (2) como uma proteína sintetizada no citosol sabe ir pra mitocôndria e não pro núcleo, (3) por que duas membranas no núcleo e na mitocôndria têm origens diferentes.
- 2 temas vizinhos que NÃO são esse: tráfego vesicular RE→Golgi (é Compartimentos II); fosforilação oxidativa em detalhe (é Bioenergética).

---

## 1. Pontos de parada (simulação leitura linha a linha)

| Seção | Status | Pág | Razão mecanística |
|---|---|---|---|
| Abertura (compartimento = ambiente químico) | passa | 3 | Excelente — desfaz a imagem ingênua de "sala" antes de oferecer a definição técnica. Aluno engaja. |
| 1.1 "regulação" — RNA revisado antes da tradução | [STOP] | 4 | Aluno: "o que é 'revisar o mRNA'? splicing? edição? capping? cai do nada." Frase usa termo guarda-chuva sem retomada de 1ª. |
| Footnotes DNA/RNA/mRNA/rRNA na pág 4 | passa | 4 | Bom — define em rodapé na 1ª aparição. |
| 1.3 "α-hélice anfipática" do sinal mitocondrial | [STOP] | 14 | Aluno não sabe o que é hélice anfipática. Apenas "um lado polar/positivo, outro hidrofóbico" — passa, mas a expressão técnica fica sem nome explicado em footnote. |
| 2.1 "20–40 nm" do espaço perinuclear | passa | 7 | Número concreto sem desviar — boa âncora visual. |
| 2.2 "gradiente Ran-GTP/GDP" | [STOP] | 8 | Aluno: "ok, importina puxa, mas POR QUE Ran-GTP no núcleo e Ran-GDP no citosol? quem mantém esse gradiente?" Texto cita o fato, não o mecanismo (RCC1 nuclear / RanGAP citosólico). |
| 2.3 H3K9me3, H3K27me3, H3K4me3 | parcial-STOP | 9-10 | Quatro marcas de histona despejadas sem `#sigla()` nem footnote. Aluno não sabe o que é "tri-metilação de lisina 9 na histona H3". |
| 3.1 "ψ negativo dentro" da matriz | [STOP] | 12 | Símbolo Δψ aparece como "ψ" (cai a maiúscula delta em encoding) — confuso, vira mojibake conceitual. |
| 3.3 importação mitocondrial passo a passo | passa | 14 | Sequência limpa: sinal → TOM20 → TOM/TIM23 alinhados → MPP cliva → Hsp60 enovela. Boa cadeia multi-passo. |
| 3.4 plasmalogênio = mielina = Zellweger | passa | 16-17 | Excelente conexão clínica concreta. Liga organela a sintoma neurológico. |
| Conclusão integradora pág 18 | passa | 18 | Faz callback à abertura ("volte ao começo") — fechamento técnico forte. |

Total: 5 [STOP] em 19 páginas de E1 — taxa 26%. Aceitável, mas resolvíveis.

---

## 2. T3.1 — Comparação com EXEMPLARES.md

**Categoria relevante:** abertura por desfazer imagem ingênua + cadeia multi-passo enzimática.

**Apostila histórica (pág 3, abertura):**
> "Antes de qualquer coisa, é preciso desfazer uma confusão fundamental. Quando ouvimos 'compartimento intracelular', quase todo mundo imagina uma sala fechada dentro da célula — um quarto onde a célula guarda alguma coisa. Isso é parcialmente verdade, mas só parcialmente, e aceitar essa imagem como definição esconde o que realmente importa."

**Padrão EXEMPLARES "abertura ingênua → desmonte":** começa pela imagem que o aluno provavelmente carrega, nomeia o erro, oferece a definição correta. Esta abertura executa esse padrão **com precisão cirúrgica** — aluno se reconhece na "imagem de quarto" e fica curioso pelo desmonte. NEBLI deveria copiar esse molde.

**Apostila histórica (pág 14, importação mitocondrial):**
> "A sequência-sinal N-terminal liga-se ao receptor TOM20 na superfície da mitocôndria. (...) Nos sítios de contato (...) o canal TOM se alinha com o canal TIM23 (...) Aqui entram duas fontes de energia. Primeiro, o gradiente eletroquímico (...) Segundo, Hsp70 da matriz liga-se ao N-terminal (...) Quando a proteína está toda na matriz, a MPP cliva a sequência-sinal (...) Hsp60 ajuda a proteína a enovelar-se."

Cadeia 5 passos, cada um com sujeito+verbo+complemento concreto, energia explicitada em dois momentos distintos. **Acima do padrão NEBLI médio** (que tende a juntar 2 passos numa frase só).

---

## 3. T3.2 — 3 parágrafos mais fracos (triangulação)

### Parágrafo 1 — pág 4, "revisão do mRNA"

**Citação literal:** "O núcleo, por exemplo, isola o DNA do citoplasma e cria uma chance de revisar o RNA mensageiro antes que ele seja traduzido — o que é impossível em bactérias, onde a tradução começa antes mesmo de a transcrição terminar (o ribossomo 'monta' no mRNA enquanto a RNA-polimerase ainda está produzindo o transcrito)."

**Diagnóstico mecanístico:** "revisar" é abstração que o aluno em dificuldade traduz como "checar erros de digitação". Os processos reais (splicing, capping 5', poly-A, edição de RNA) nunca são nomeados. Aluno fecha o PDF para procurar "revisão do mRNA" e não acha nada com esse nome.

**Reescrita pronta:** "O núcleo, por exemplo, isola o DNA do citoplasma e cria espaço para PROCESSAR o RNA mensageiro antes que ele seja traduzido — colocar um cap protetor na ponta 5', cortar os íntrons (splicing) e adicionar a cauda poli-A. Em bactérias isso é impossível: o ribossomo já monta no mRNA enquanto a RNA-polimerase ainda está produzindo o transcrito, não dá tempo de processar nada."

### Parágrafo 2 — pág 8, direcionalidade Ran-GTP/GDP

**Citação literal:** "A energia desse transporte vem do GTP hidrolisado pela proteína Ran. No núcleo, Ran-GTP é abundante; no citosol, é Ran-GDP. Quando a importina-α + cargo entram no núcleo, Ran-GTP se liga à importina e força o desligamento do cargo."

**Diagnóstico mecanístico:** o texto declara o gradiente Ran-GTP/Ran-GDP como dado, sem explicar QUEM mantém esse gradiente. O aluno em dificuldade fica perguntando "mas por que cargo chega só no citosol e desliga só no núcleo?". A resposta é: RCC1 nuclear (GEF que carrega Ran com GTP) + RanGAP citosólico (que hidrolisa Ran-GTP a Ran-GDP). Sem isso, o "gradiente" parece arbitrário.

**Reescrita pronta:** "Quem mantém esse gradiente? Duas enzimas em lados opostos. No núcleo, a RCC1 (ancorada na cromatina) recarrega Ran com GTP — então tudo que está no núcleo encontra Ran-GTP. No citosol, a RanGAP hidrolisa Ran-GTP a Ran-GDP em milissegundos — então tudo que sai do poro encontra Ran-GDP. É essa assimetria espacial entre as duas enzimas que dá direção ao transporte: a importina só solta o cargo onde encontra Ran-GTP (núcleo), e a exportina só solta o cargo onde encontra Ran-GDP (citosol)."

### Parágrafo 3 — pág 9-10, marcas de histona despejadas

**Citação literal:** "Heterocromatina (...) carrega marcas de histona que silenciam a transcrição (H3K9me3, H3K27me3). (...) A eucromatina (...) carrega marcas de ativação (H3K4me3, acetilação de H3K27)."

**Diagnóstico mecanístico:** quatro códigos crípticos sem decodificação. "H3K9me3" significa "histona H3, lisina na posição 9, tri-metilada" — o aluno não tem como saber isso. Como decora? Vira ruído. NEBLI tem `#sigla()` justamente para isso.

**Reescrita pronta:** "Heterocromatina carrega marcas químicas específicas nas caudas das histonas que silenciam a transcrição. As duas mais importantes são H3K9me3#footnote[histona H3, com a lisina na posição 9 recebendo três grupos metil — trimetilação que recruta proteínas repressoras] e H3K27me3#footnote[mesma histona H3, lisina 27 trimetilada — marca depositada pelo complexo Polycomb durante o desenvolvimento, mantém genes desligados de forma estável]. Eucromatina, por contraste, carrega marcas de ativação: H3K4me3#footnote[lisina 4 da H3 trimetilada — marca de promotor ativo, recruta a maquinaria de transcrição] e acetilação de H3K27#footnote[acetil-grupo no lugar do metil na lisina 27 — anula a repressão Polycomb e abre o nucleossomo]."

---

## 4. T3.3 — 3 seções mais densas

### Seção 1 — 2.2 Poros nucleares (pág 8)

**Densidade:** 125 MDa, 30 nucleoporinas, 3-5 mil poros, malha FG, cutoff 20-40 kDa, NLS, importina, Ran-GTP/GDP, mesmo NPC bidirecional — 8 conceitos em ~280 palavras. **Mitigação:** quebrar em duas sub-seções — "anatomia do poro" e "como funciona o tráfego" — com um mini-resumo entre elas.

### Seção 2 — 3.3 Importação mitocondrial (pág 13-15)

**Densidade:** TOM20, TOM, TIM23, sítios de contato, gradiente eletroquímico, Hsp70 citosólica, Hsp70 matriz, Hsp90, MPP, Hsp60, ATP em dois momentos — 11 elementos. **Mitigação:** já tem boa cadeia narrativa, mas falta uma **figura-fluxograma** numerada (1→2→3→4→5) que o aluno possa olhar enquanto lê. Pág 14 tem só uma figura genérica.

### Seção 3 — 3.4 Peroxissomos (pág 15-17)

**Densidade:** membrana única, PTS1/PTS2, PEX5/PEX7/PEX19, β-oxidação >C22, H2O2, catalase, urato-oxidase, plasmalogênios, mielina, Zellweger, 22 genes PEX — 12 elementos numa seção curta. **Mitigação:** separar "anatomia/importação" de "função bioquímica" — hoje vêm misturados em 3 páginas.

---

## 5. T3.4 — Voz fora do padrão

Voz autoral muito consistente. Dois lapsos:

- Pág 5, "Confundir as vias é um erro caro de prova." — bom, mas "erro caro" repete em pág 6 ("Quem confunde isso, perde questão.") e pág 19 ("Confundir vias é erro grave de prova"). Três vezes vira maneirismo.
- Pág 12, callout "DNA mitocondrial é uma fração ínfima do total" usa "Aluno tende a superestimar..." — voz didática-distanciada que destoa do "vamos seguir" / "repare" coloquial do corpo.

---

## 6. T3.7 — Carga cognitiva pico

**Seção-pivô:** pág 8 (Poros nucleares). Aluno chega aqui depois de 5 páginas, recebe 8 conceitos novos em 280 palavras, e logo em seguida (pág 9) entra cromatina + marcas de histona. **Pico real** = páginas 8-10.

**3 mitigações:**
1. Inserir página de respiro entre 2.2 e 2.3 — micro-mini-resumo do poro antes de mergulhar em cromatina.
2. Adicionar figura-fluxograma do ciclo Ran-GTP/Ran-GDP (importina entra cheia, sai vazia; exportina o contrário) — explicar visual o que o texto explica verbal.
3. Mover marcas de histona (H3K9me3 etc) para um **box de aprofundamento**, deixando o corpo principal só com "marcas químicas que silenciam vs ativam".

**Qual escolher:** mitigação 2 (figura do ciclo Ran). Custo baixo, ganho cognitivo alto, resolve um [STOP] confirmado.

---

## 7. T3.8 — ANÁLISE VISUAL

- **Hierarquia tipográfica:** consistente — header navy "NEBLI · ETAPA 1 — TEXTO DIDÁTICO" em todas as páginas; títulos de PARTE em maior; sub-seções (1.1, 2.2) em médio. Funciona.
- **Valor pedagógico das figuras:** 13 imagens em 19 páginas de E1 (proporção boa). Legendas curtas e explicativas ("Repare como a membrana externa se conecta com o RE..."). **Problema:** páginas 19-43 (Resumindo + E2 + E3 + Gabarito) ZERO figuras — todo aprofundamento conceitual textual sem suporte visual. Aluno revisando questões não tem âncora visual.
- **Densidade visual:** página 19 (Resumindo em 2 colunas) parece muros densos — 484 palavras sem respiro. Demais páginas ~270-340 palavras, dentro do aceitável.
- **Uso de cor:** badges por categoria (Consolidação verde / Integração azul / Aplicação violeta) cumprem papel, mas o gabarito final (pág 43, 82 palavras) está numa diagramação confusa — Q11 D Q12 A na mesma linha que Q13 CCEE Q14 C Q15 E. Layout em grade mista que dificulta conferência.
- **Cortes/overflow:** pág 11 termina abruptamente em "rede mitocondrial — não centenas" e pág 13 retoma — quebra mid-paragraph aceitável. Não vi mojibake, mas o Δψ vira "ψ" no extract (pode ser problema do extract, ou problema real da renderização).

---

## 8. T3.9 — O QUE O AUTOR FAZ BEM (3 técnicas, ALIMENTA Phase F)

### Técnica 1 — "Abertura por desmonte de imagem ingênua"
**Citação:** "Quando ouvimos 'compartimento intracelular', quase todo mundo imagina uma sala fechada dentro da célula — um quarto onde a célula guarda alguma coisa. Isso é parcialmente verdade, mas só parcialmente..."
**Quando NEBLI deveria usar:** SEMPRE que o tema tem um nome que carrega metáfora popular falsa. REDATOR-E1 deve abrir a PARTE I nomeando a imagem ingênua antes de oferecer a definição técnica. Exemplos imediatos: "membrana plasmática = parede" (na verdade fluida), "DNA = projeto da célula" (na verdade catálogo passivo), "enzima = chave que abre" (na verdade catalisa estado de transição).

### Técnica 2 — "Mini-resumo em caixa cinza a cada 2-3 páginas"
**Citação:** "Resumindo até aqui: Compartimento existe para manter condições químicas incompatíveis funcionando ao mesmo tempo. Sem membrana, sem gradiente. Sem gradiente, sem especialização química." (pág 3, e mais 6 vezes ao longo da E1)
**Quando NEBLI deveria usar:** já é regra canônica, mas a apostila histórica executa MELHOR — frases concretas com sujeito+verbo, encadeamento "sem X, sem Y" que é mnemônico. REDATOR-E1 deve copiar a fórmula sintática "Sem A, sem B. Sem B, sem C." onde funcionar.

### Técnica 3 — "Callout clínico paradigmático ao final de cada organela"
**Citação:** "Síndrome de Zellweger e doenças peroxissomais (...) ácidos graxos de cadeia muito longa, deficiência de plasmalogênios, e — pela falência de mielinização — encefalopatia neonatal grave (...) É o exemplo paradigmático de como a falha de uma organela 'secundária' pode ser letal."
**Quando NEBLI deveria usar:** todo resumo NEBLI que cobre organela/enzima/via deve fechar com **1 doença paradigmática** que torna a função tangível. Não é "factoide clínico" decorativo — é prova de que o mecanismo importa. Para gliconeogênese, é von Gierke; para cadeia respiratória, são LHON / encefalomiopatias mitocondriais; para compartimentos, é Zellweger. REDATOR-E1 deve identificar a doença paradigmática no Tema Card Seção C e amarrar a Conclusão Integradora a ela.

---

## 9. T3.10 — 7 erros NEBLI (calibração)

| # | Erro | Status no PDF | Evidência |
|---|---|---|---|
| 1 | Paridade distratoras E2 Aplicação | PRESENTE leve | Q26-Q30: corretas têm 60-80 palavras com mecanismo completo, distratoras têm 35-55 palavras — ratio aceitável (~1.3-1.5), mas no limite. Q30 distratora A é 5 palavras a menos do que deveria. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | PRESENTE forte | H3K9me3, H3K27me3, H3K4me3 (pág 9-10) aparecem sem footnote nem `#sigla()`. CDK1 (pág 7) idem. Δψ (pág 12) idem. ATP/ADP/GTP aparecem mas só ATP tem footnote (pág 12). NLS, NPC, TOM, TIM, MPP, PEX, PTS1, PTS2 — todas têm footnote, boa. |
| 3 | Subagentes Opus falhando | N/A | Apostila histórica, não pipeline. |
| 4 | Heredoc ENAMETOOLONG | N/A | Apostila histórica. |
| 5 | `questao-ce` tupla | AUSENTE | Q13, Q16, Q18, Q22 usam CE — compilaram, formato OK. |
| 6 | Termo-notas abaixo do alvo | AUSENTE | Conta-se ~9 footnotes técnicos (DNA, RNA, mRNA, rRNA, lâmina nuclear, NPCs, cromatina, ATP, PEX) — dentro do alvo 6-8 ampliado. |
| 7 | Teto E1 22 páginas | PRESENTE leve | E1 cobre páginas 3-18 = 16 páginas. Dentro do teto. Aceitável. |

---

## 10. Recomendações por hierarquia

### ESTRUTURAL (max 3)
1. **Reordenar 2.2 → 2.3:** inserir mini-página de respiro com fluxograma do ciclo Ran entre poros e cromatina. Pico cognitivo páginas 8-10 é o maior risco do resumo.
2. **Adicionar figura-fluxograma numerada (1→5) da importação mitocondrial em 3.3** (pág 14) — hoje tem só uma figura ilustrativa genérica, não um diagrama de processo.
3. **Reformatar gabarito da pág 43** — grade mista atual mistura objetivas A-E com itens CE de 4 letras na mesma linha. Separar em 3 blocos claros (Consolidação / Integração / Aplicação) em colunas únicas.

### MECANÍSTICO (max 3)
1. **Explicar quem mantém o gradiente Ran-GTP/Ran-GDP** (pág 8) — adicionar RCC1 nuclear + RanGAP citosólico em uma frase de 2 linhas. Sem isso, o gradiente é mágica.
2. **Decodificar as 4 marcas de histona** (pág 9-10) — H3K9me3, H3K27me3, H3K4me3, acetilação H3K27 precisam de `#sigla()` ou footnote.
3. **Nomear processamento do mRNA explicitamente** (pág 4) — splicing/capping/poli-A em vez do guarda-chuva "revisar".

### DIDÁTICO (max 3)
1. **Variar fórmula "erro caro de prova"** — três usos vira maneirismo. Trocar 2 das 3 por construções concretas ("a banca testa exatamente isso" / "questão clássica monta a casca em cima dessa confusão").
2. **Adicionar 1-2 figuras em E2/E3** — 25 páginas de questão sem nenhuma figura é deserto visual. Pelo menos um esquema de revisão antes do gabarito.
3. **Box "DNA mitocondrial fração ínfima"** — reescrever em voz coloquial coerente com o corpo (em vez de "Aluno tende a superestimar...").

### ESTÉTICO (max 3)
1. **Resumindo página 19** está em muros — 484 palavras em 2 colunas sem respiro entre seções. Separar com micro-linha horizontal navy ou pequeno espaço vertical.
2. **Pág 11 quebra mid-parágrafo** — aceitável mas poderia ter `#pagebreak(weak: true)` antes de "rede mitocondrial".
3. **Δψ aparece como ψ** no encoding extraído — verificar se renderiza correto no PDF (pode ser só artefato do .txt; se for real, pacote `unicode-math` ou fallback Δ).

---

## 11. Veredito acionável

1. **APROVAR como referência positiva?** SIM. Três técnicas (abertura por desmonte, mini-resumo "sem X sem Y", callout clínico paradigmático) merecem virar regra no REDATOR-E1.
2. **≥1 ESTRUTURAL/MECANÍSTICO?** SIM — 3 mecanísticas e 3 estruturais identificadas, todas com fix prescrito.
3. **Seção para refazer?** Nenhuma seção precisa refazer do zero. 2.2 (Poros nucleares) precisa de injeção de mecanismo Ran-GTP.
4. **Parágrafos para reescrever?** 3 — (a) pág 4 "revisar mRNA"; (b) pág 8 "gradiente Ran sem origem"; (c) pág 9-10 "marcas de histona despejadas".

---

[APROVAR COM RESERVAS]

FIM-DA-REVISAO-PROFUNDA
