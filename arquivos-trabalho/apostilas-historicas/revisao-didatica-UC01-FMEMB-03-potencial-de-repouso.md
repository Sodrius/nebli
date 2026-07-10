# Revisão didática Tier 2 — UC01-FMEMB-03-potencial-de-repouso

**Tema (ancoragem):** Potencial de repouso — propriedades elétricas passivas da membrana neuronal em equilíbrio (−70 mV)
**Recorte real do PDF:** Cobre integralmente: membrana como capacitor, gradientes iônicos canônicos, equação de Nernst (K⁺, Na⁺, Cl⁻), equação de GHK por condutâncias, circuito equivalente, driving force, bomba Na/K-ATPase (curto vs longo prazo), aplicações clínicas (digoxina, hipercalemia)
**Autor:** Italiano (conforme instrução — apostila histórica NEBLI)
**Avaliador:** Claude Sonnet 4.6 via general-purpose simulando revisor-pdf-didatico
**Data:** 2026-05-25
**Total páginas:** 64 | **Média palavras/pág:** 293,8 | **Total imagens:** 1344 (dado do JSON — provavelmente metadado cumulativo, não imagens únicas)

---

## Sumário executivo

- Score médio: **4,5 / 5**
- CRÍTICOS falhando (≤2): **0**
- IMPORTANTES falhando: **1** (T2.9 — conclusão integradora tem leve deficiência em camada de integração clínica prospectiva)
- Veredito: **[APROVAR]**

Esta apostila é um exemplar de alta qualidade didática pelo padrão NEBLI. A voz é dialógica e mecanística do início ao fim; o aluno de baixo conhecimento é conduzido por construção cumulativa explícita. O único ponto de atenção é a conclusão integradora (T2.9), que excelente mas poderia integrar mais explicitamente a ponte para o potencial de ação como consequência. T2.7 (variação de registro) e T2.12 (antropomorfismo) têm ocorrências pontuais aceitáveis dentro da política.

---

## Detalhamento por critério

| # | Critério | Sev | Score | Justificativa | Citação literal (p) | Sugestão |
|---|---|---|---|---|---|---|
| T2.1 | Pergunta ingênua abrindo subtópicos | CRÍTICO | 5 | Cada seção abre com a pergunta que o aluno em dificuldade faria. Exemplos: "O que acontece com o Vm?" (2.1), "Por que -70 mV não é igual a nenhum dos três?" (2.4), "Por que a bomba é necessária?" (3.4). Padrão consistente em todas as partes. | "Para construir a equação de Nernst de forma intuitiva, vamos fazer um experimento de pensamento. Imagine uma célula com as concentrações reais [...] mas com apenas um tipo de canal aberto: canal para K⁺. O que acontece com o Vm?" (p.9) | Manter. Modelo a ser seguido. |
| T2.2 | Mecanismo antes do nome técnico | CRÍTICO | 5 | "Gradiente eletroquímico" é definido ANTES de receber o nome. "Driving force" é explicada conceitualmente ("a força motriz") antes da fórmula. Capacitor explicado pela física antes de nomear. "GHK" introduzida como "a pergunta deixada pendente: qual é exatamente o Vm com vários canais abertos" antes do nome. | "A soma das duas forças é chamada de gradiente eletroquímico. Quando o gradiente eletroquímico é zero [...] o íon está em equilíbrio eletroquímico" (p.7) | Manter. Sem regressões ao longo do texto. |
| T2.3 | Pré-requisitos retomados em 1–2 frases | IMP | 4 | Gradiente de concentração é retomado em 1 frase antes de Nernst ("Esta força existe pela mesma razão que qualquer difusão acontece: a entropia aumenta"). Concentrações canônicas são tabeladas antes dos cálculos. Leve ponto fraco: "valência z" aparece na fórmula de Nernst sem retomada breve de "o que é valência" para o aluno que não lembra de química. | "A energia elétrica associada ao Vm sobre um íon de valência z é elétrica = zF × Vm — onde F é a constante de Faraday" (p.11) | Adicionar 1 frase antes da equação de Nernst: "z é a carga elétrica do íon em unidades de carga elementar (+1 para K⁺, +1 para Na⁺, −1 para Cl⁻)." |
| T2.4 | Aprofundamento em camadas (porquê cru → nuance → exceção → clínica) | IMP | 5 | Estrutura exemplar: (1) intuição física (capacitor, força química vs elétrica); (2) equação de Nernst com derivação; (3) GHK como generalização necessária; (4) circuito equivalente como terceira perspectiva da mesma física; (5) boxe "Em Vm ≠ Eíon não viola Nernst" como exceção aparente resolvida; (6) digoxina e hipercalemia como clínica. Cada camada nomeia explicitamente o que veio antes. | "Existem duas formas dela, equivalentes em casos simples. A que vamos usar aqui é a forma por condutâncias, mais intuitiva para o caso de canais separados (não-acoplados)" (p.18) | Manter. |
| T2.5 | Diálogo > livro-texto (3 parágrafos aleatórios) | CRÍTICO | 5 | Parágrafo 1 (p.3 — intro): "Não vem da bomba sódio-potássio diretamente (essa é a confusão clássica), nem de uma 'carga elétrica acumulada' misteriosa." — voz de monitor antecipando confusão. Parágrafo 2 (p.9 — célula só K⁺): "Mas espere: cada K⁺ que sai leva consigo uma carga positiva." — ruptura narrativa para envolver leitor. Parágrafo 3 (p.25 — bomba): "Bloquear a bomba é como cortar a manutenção de uma represa: o lago não esvazia na hora, mas vai esvaziando até virar terreno seco." — metáfora concreta. | "Não vem da bomba sódio-potássio diretamente (essa é a confusão clássica), nem de uma 'carga elétrica acumulada' misteriosa." (p.3) | Manter. Voz dialógica consistente. |
| T2.6 | Boxes/avisos em voz mecanística (sem vocab de prova) | CRÍTICO | 5 | Todos os boxes (5 identificados) usam linguagem mecanística: "Despolarizar não é virar positivo" explica via "a direção da mudança, não o sinal absoluto"; "Nernst não é o Vm real" explica via "depende de todos os íons ponderados por suas condutâncias"; "Vm ≠ Eíon não viola Nernst" explica via estado estacionário vs equilíbrio; "Bomba bloqueada NÃO zera o Vm na hora" explica via duas camadas de causalidade. Zero ocorrências de "cai na prova", "importante para P1", "memorize". | "Aluno tende a achar: 'se a bomba mantém o Vm, então bloquear a bomba zera o Vm imediatamente'. Errado em duas camadas. (1) A bomba não mantém o Vm diretamente — ela mantém os gradientes a partir dos quais os canais fazem o Vm." (p.25-26) | Manter. Modelo perfeito de box mecanístico. |
| T2.7 | Variação de registro entre subtópicos vizinhos | IMP | 4 | PARTE I usa metáforas físicas ("condensador", "reservatório"). PARTE II muda para derivação matemática com passos explícitos. PARTE III alterna entre três perspectivas (GHK, circuito, corrente líquida). Pequena inconsistência: o registro matemático da seção 3.1 é muito similar ao da 2.2; faltou diferenciação maior na textura narrativa entre as duas. | "Vamos calcular EK com os números da nossa célula. R = 8,314 J/(mol×K). T = 310,15 K [...] Fator de Nernst" (p.11 — registro matemático) vs "vamos montar o circuito completo" (p.22 — registro de "engenharia") | Diferenciação 2.2 → 3.1: na entrada de 3.1, poderia ativar o aluno com frase de transição explícita de registro: "Agora trocamos o chapéu de termodinâmica pelo de engenheiro de circuitos." |
| T2.8 | Mini-resumos em parágrafos longos | IMP | 5 | Cada seção termina com bloco "Resumindo até aqui:" formatado em itálico/recuo. 12 ocorrências identificadas. Os mini-resumos são sintéticos sem introduzir conceito novo, e começa com sujeito+verbo (não lista de siglas). | "Resumindo até aqui: Célula só com canal de K: K⁺ sai por gradiente químico → interior fica negativo → aparece força elétrica que puxa K⁺ de volta → no equilíbrio, as duas forças se cancelam, fluxo líquido é zero." (p.10) | Manter. Quantidade e qualidade exemplares. |
| T2.9 | Conclusão integradora em 3+ camadas | IMP | 4 | Conclusão (p.27-28) tem claramente 3 camadas: (1) síntese mecânica dos três componentes; (2) cálculo confirmatório (GHK dá −71,65 mV); (3) ponte prospectiva para potencial de ação. Ponto fraco: a camada clínica está nos boxes anteriores (digoxina, hipercalemia) mas não é relembrada na conclusão integradora. O aluno que só leu a conclusão não vê a síntese clínica. | "Por que tudo isso importa? Porque o repouso é a reserva de energia a partir da qual o neurônio dispara. Quando canais de Na⁺ voltagem-dependentes abrirem [...] gNa vai subir 1000× em poucos milissegundos, e pelo princípio de GHK o Vm vai se aproximar de ENa = +62 mV" (p.27-28) | Adicionar 1–2 frases finais na conclusão conectando à clínica: "É por isso que alterar os gradientes — hipercalemia mudando EK, digoxina mudando [Na⁺]int — perturba o repouso com consequências imediatas na excitabilidade." |
| T2.11 | Figuras integradas ao texto (análise visual) | IMP | n/a — PDF não pôde ser lido por ausência de pdftoppm no ambiente Windows. Avaliação baseada em referências no .txt. | O .txt cita extensivamente legendas descritivas que precedem e seguem cada figura (ex.: "A membrana em repouso (esquerda) tem cargas positivas se acumulando do lado externo [...] A direita, durante excitação e propagação, esse arranjo se inverte localmente" — p.3; "Cálculo numérico de EK a 37 °C [...] Este é o número-chave do potencial de repouso" — p.12). Todas as figuras têm legenda mecanística integrada ao argumento, não decorativa. | "Cálculo da driving force para Na⁺ no repouso: Vm − ENa = −70 − (+62) = −132 mV. Negativa → Na⁺ entra pelo canal — e com magnitude enorme em comparação com a do K⁺ (132 vs 10 mV)." (p.21) | Pelo texto, parecem bem integradas. Verificação visual recomendada pelo COMPILADOR antes de aprovação final. |
| T2.12 | Cota de antropomorfismo (≤3x por capítulo) | DES | 4 | Expressões antropomórficas identificadas: "K⁺ sai" (aceitável — padrão fisiológico), "o íon quer sair" (p.9 — antropomorfismo leve), "cada íon vota proporcional ao seu peso" (p.17 — metáfora pedagógica intencional), "o íon não 'vê' só o Vm da célula" (p.19 — marcado com aspas, uso consciente). Total: ~3 ocorrências explícitas em toda a E1. Dentro do limite. | "cada K⁺ que sai leva consigo uma carga positiva. A célula, que era neutra, começa a ficar negativa por dentro (perdeu cátion)" (p.9) | Manter. Uso deliberado e marcado graficamente nas metáforas mais fortes. |
| T2.13 | Densidade visual e legibilidade (análise visual) | IMP | n/a — PDF não lido. Baseado em estrutura do .txt: ~293 palavras/página é densidade moderada adequada para apostila de estudo. Formatação do .txt revela boxes destacados, mini-resumos recuados, tabela de concentrações iônicas. | "K⁺: 100 mM dentro, 5 mM fora (20× maior dentro). Na⁺: 15 mM dentro, 150 mM fora (10× maior fora). Cl⁻: 13 mM dentro, 150 mM fora." (p.5 — tabela) | Verificação visual do PDF recomendada para confirmar espaçamento e hierarquia tipográfica. |

---

## Incidência dos 7 erros NEBLI

| # | Erro | Presente? | Evidência |
|---|---|---|---|
| 1 | Paridade de distratoras em E2 Aplicação (Q26–Q30) | AUSENTE | Q26–Q30 verificadas no .txt: todas as distratoras têm extensão comparável à alternativa correta (25–55 palavras cada). Q29 (hipercalemia) tem distratoras ricas com mecanismo errado plausível. Ratio correta/maior-distratora estimado ≤1,2 em todas. |
| 2 | Siglas sem `#sigla()` na 1ª aparição | N/A | Apostila histórica — não usa sistema Typst/`#sigla()`. Avaliado pelo critério equivalente: siglas são expandidas na primeira aparição via footnote no rodapé da página (ex.: "Vm — potencial de membrana — diferença de voltagem entre o lado intracelular e o lado extracelular", p.3; "mV — milivolt — milésima parte do Volt", p.3; "GHK — equação de Goldman-Hodgkin-Katz", p.18; "driving force", p.20). Sistema funcional, equivalente em resultado ao `#sigla()`. |
| 3 | Subagentes Opus customizados falhando | N/A | Erro de pipeline de geração, não aplicável a apostila histórica. |
| 4 | Heredoc atômico ENAMETOOLONG no Windows | N/A | Erro de compilação, não aplicável a apostila histórica. |
| 5 | `questao-ce` exige tupla não lista | N/A | Erro de Typst, não aplicável a apostila histórica. |
| 6 | Termo-notas abaixo do alvo | N/A | Sistema de footnotes equivalente ao `#termo-nota`. Apostila tem ≥12 footnotes de glossário identificadas no .txt. Não há déficit. |
| 7 | Tema-card com teto E1 errado | N/A | Apostila histórica — não gerada via pipeline Tema Card. |

---

## Top 3 recomendações priorizadas

1. **[T2.9 — Conclusão integradora]** Adicionar 1–2 frases no final da Conclusão integradora retomando as aplicações clínicas (hipercalemia e digoxina) que estão nos boxes da E1 mas não aparecem na conclusão. O aluno que usa a conclusão como revisão rápida não vê a síntese clínica. Custo: 40–50 palavras adicionais.

2. **[T2.3 — Pré-requisitos]** Inserir 1 frase antes da equação de Nernst explicitando "z é a valência do íon, sua carga elétrica em múltiplos da carga elementar: +1 para K⁺ e Na⁺, −1 para Cl⁻." O aluno de 1º semestre pode não trazer esse conceito de química com segurança suficiente para aplicar o sinal corretamente.

3. **[T2.7 — Variação de registro]** Sinalizar a transição de registro entre PARTE II (termodinâmica/Nernst) e PARTE III (circuito equivalente/GHK) com uma frase de ponte que ative o aluno: a física é a mesma, mas a lente é diferente. Não é uma falha grave, mas ajuda o aluno a saber que está mudando de ferramenta conceitual, não de tema.

---

[APROVAR]
