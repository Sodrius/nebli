# FLASHCARDS.md — política canônica do deck-aula

Este arquivo é a **única fonte normativa sobre seleção, conteúdo e qualidade dos flashcards NEBLI**.

- `EXEMPLARES-CARDS.md` mostra exemplos e anti-exemplos desta política.
- `CLAUDE.md` descreve como executar o pipeline e produzir os artefatos.
- Scripts e schemas tornam regras verificáveis, mas não criam política pedagógica paralela.
- Documentos históricos, `MEMORY.md`, planos antigos, AnKing, Companion e decks anteriores não são autoridade para decidir o que vira card.

## 1. Função do deck-aula

O deck não é uma miniatura da E1 nem um inventário de tudo que apareceu nos slides.

**O deck registra o ganho marginal de conhecimento produzido pela aula.**

Um conceito não vira card porque foi mencionado. Ele vira card quando a aula acrescenta conhecimento que merece ser recuperado depois.

A pergunta de seleção é:

> Depois desta aula, qual conhecimento específico o aluno deve conseguir recuperar que esta aula efetivamente ensinou?

A mera presença de um termo, estrutura, doença, via, célula ou mecanismo no material **não autoriza card**.

## 2. Limite epistemológico do pipeline

Para selecionar cards, o agente pode usar somente:

1. os materiais da aula atual — slides, roteiro, PDF, notas fornecidas e a E1 construída a partir deles;
2. a planilha mestra — para localizar a aula no currículo, identificar aulas anteriores e inferir o que pode ser conhecimento já pressuposto.

Não consultar decks anteriores para decidir novidade. Não presumir que existe ou não existe card prévio. Não usar memória pessoal do usuário.

A planilha mestra fornece **prior curricular presumido**, não histórico de cards.

## 3. Análise global obrigatória antes da autoria

Nenhum card deve ser escrito durante a primeira leitura do material.

A ordem obrigatória é:

1. ler todos os materiais da aula;
2. identificar título, objetivos e estrutura global;
3. localizar a aula na planilha mestra e ler as aulas anteriores relevantes;
4. dividir a aula em blocos pedagógicos;
5. identificar as afirmações ou relações que cada bloco realmente ensina;
6. classificar cada candidato pelo papel pedagógico definido abaixo;
7. formar o ganho da aula e o núcleo de retenção;
8. somente então autorar cards.

Uma informação que parece central num slide isolado pode revelar-se apenas contexto quando a aula inteira é compreendida.

## 4. Classificação obrigatória dos candidatos

Cada conceito/claim da matriz de cobertura recebe exatamente um `learning_role`.

### `foco_novo`

Conhecimento explicitamente introduzido, definido, explicado ou desenvolvido nesta aula.

**Pode gerar card.**

### `relacao_nova`

Os componentes podem ser prévios, mas a aula ensina agora uma nova relação causal, funcional, espacial, comparativa ou mecanística entre eles.

**Pode gerar card.** O alvo do card deve ser a relação nova, não a redefinição das peças antigas.

### `aprofundamento_novo`

Aprofundamento Step 1 diretamente ligado a um ganho novo da aula, dentro do mesmo ramo conceitual e explicado primeiro na E1.

**Pode gerar card.**

### `pre_requisito`

Conhecimento usado para compreender a aula, mas pressuposto em vez de ensinado.

**Não gera card.** Pode ser explicado na E1 para manter a E1 autocontida.

### `revisao`

Conteúdo que o material relembra, repete ou retoma.

**Não gera card.**

### `contexto`

Informação usada para situar o tema, motivar uma discussão ou conectar partes da aula sem ser alvo de ensino próprio.

**Não gera card.**

### `exemplo`

Caso, entidade ou situação usada para demonstrar uma regra mais geral.

**Não gera card sobre o exemplo**, salvo se a própria aula transformar aquele exemplo em objeto explícito de aprendizagem. Preferir card sobre a regra ensinada.

### `mencao`

Termo ou fato incidental, inclusive em legenda, frase lateral, lista ou comentário sem desenvolvimento.

**Nunca gera card.**

Somente `foco_novo`, `relacao_nova` e `aprofundamento_novo` são elegíveis a `card_keys`.

## 5. Evidência positiva de ensino

O default é **não cardificar**.

Antes de admitir um candidato, deve existir evidência positiva de que a aula o ensina.

Sinais fortes de ensino:

- seção ou slide dedicado ao assunto;
- definição ou introdução explícita;
- explicação de como ou por que ocorre;
- sequência causal ou mecanismo;
- comparação construída para distinguir entidades;
- figura/tabela cujo objetivo é explicar aquela relação;
- consequências desenvolvidas;
- objetivo da aula retomado e desenvolvido no corpo do material;
- várias informações convergindo para construir o mesmo conceito.

Sinais de conhecimento pressuposto ou de suporte:

- o termo apenas aparece dentro da explicação de outra coisa;
- o material usa o conceito sem defini-lo ou desenvolvê-lo;
- é ponto de partida para a verdadeira novidade;
- aparece só em exemplo, legenda, título auxiliar ou enumeração;
- a planilha mestra mostra uma aula anterior especificamente dedicada ao tema;
- expressões como “lembrando”, “como já vimos”, “sabemos que”, “já discutido”;
- a explicação continua funcionando se o conceito for tratado apenas como pré-requisito.

**Ausência de explicação é evidência de pressuposição, não de ensino.**

## 6. Matriz do ganho da aula

A classificação fica registrada em `release_gate.concepts[]` antes da autoria.

Cada conceito declara, no mínimo:

- `concept_id`;
- `learning_role`;
- `e1_anchor`;
- `retention_class`;
- `card_keys`;
- `teaching_evidence[]` com `source`, `locator` e `rationale`;
- `curriculum_ref`, quando a planilha mestra for relevante.

Conceitos elegíveis a card também declaram `lesson_gain`: uma frase concreta descrevendo **o que esta aula acrescenta**.

Conceitos não elegíveis declaram `exclusion_reason` e não podem possuir `card_keys`.

`teaching_evidence.source` usa apenas:

- `slide` — evidência nos materiais da aula;
- `e1` — evidência na E1 derivada dos materiais;
- `master_sheet` — evidência de posição curricular na planilha mestra.

Uma declaração genérica como “é importante” não é evidência de ensino.

## 7. Uso da planilha mestra

A planilha mestra serve para construir `curriculum_context`:

- `current_lesson` identifica a aula atual;
- `prior_lessons` lista aulas anteriores relevantes para interpretar pressupostos.

Se um tema foi objeto explícito de aula anterior e reaparece sem novo desenvolvimento, o default é `pre_requisito` ou `revisao`.

Se a aula atual usa conhecimentos antigos para ensinar uma relação nova, classificar a relação como `relacao_nova`.

A unidade de novidade não é o nome do conceito; é **a afirmação recuperável**.

## 8. Teste contrafactual de admissão

Para cada card candidato:

> Se este card for removido, perde-se alguma informação específica que esta aula pretendeu ensinar?

Se a perda for apenas “o aluno revisará menos um pré-requisito”, o card deve sair.

Outro teste:

> O que neste card só consigo justificar apontando para esta aula?

Se não houver resposta concreta, o candidato provavelmente é pré-requisito, revisão, contexto ou menção.

## 9. E1 não implica card

A E1 deve ser didática e pode conter:

- pré-requisitos;
- revisão necessária;
- contexto;
- explicações básicas;
- conteúdo novo;
- aprofundamentos diretamente relacionados.

O deck é mais seletivo.

**Estar na E1 não é critério suficiente para receber card.**

A E1 ensina; o deck decide o que precisa ser recuperado longitudinalmente.

Todo card deve possuir `e1_anchor` literal e sua resposta precisa ter sido ensinada antes de ser cobrada.

## 10. Aprofundamento Step 1

Step 1 aprofunda o **mesmo ganho novo da aula**. Não abre um tópico adjacente só porque é high-yield.

Admitir quando:

- pertence diretamente ao mecanismo/estrutura novo da aula;
- encaixa numa seção existente da E1;
- é durável;
- aumenta capacidade de reconstruir o mesmo processo;
- não exige abrir uma nova aula de pré-requisitos.

Bons aprofundamentos: mecanismo molecular do mesmo processo, relação estrutura-função, fisiopatologia imediata, genética relevante, previsão laboratorial, morfologia ou correlação clínica estável.

Excluir: manejo, doses, guideline, estadiamento, técnica, Step 2 ou tópico adjacente autônomo.

O aprofundamento entra na E1 antes de poder virar `aprofundamento_novo`.

## 11. Núcleo de retenção

A seleção vem antes do orçamento.

Cada slot do núcleo deve corresponder a uma decisão recuperável independente. Não criar cards para preencher quota.

Classes de retenção:

- `must_recall` — precisa de recuperação própria;
- `derivable` — pode ser reconstruído a partir de outra recuperação; não duplica card;
- `e1_only` — útil para compreensão, mas não merece card;
- `optional` — aprofundamento de menor prioridade, em subdeck Optional.

Conteúdo com `learning_role` não elegível deve ser `e1_only` ou, excepcionalmente, `derivable`.

## 12. Volume

Faixas servem como sanity check, não meta:

- aula pequena: aproximadamente 8–12 cards;
- média: 12–18;
- grande: 18–22.

Tetos padrão podem ser 15, 20 e 25, mas o `card_budget_hard_max` deve ser definido antes da autoria.

Se há cards demais, primeiro:

1. remover suporte que não é ganho;
2. eliminar recuperações redundantes;
3. converter fatos deriváveis em `derivable`;
4. procurar relações geradoras melhores;
5. só então considerar exceção de volume.

## 13. Atomicidade

Um card testa **uma recuperação independente**.

Uma única marca `c1` não garante atomicidade. Bloquear frases que escondem lista, duas relações, uma definição inteira ou vários fatos sob um único cloze.

Tempo-alvo de resposta: cerca de 10 segundos.

## 14. Retrieval target

Todo card autoral declara `retrieval_target` específico.

O alvo deve coincidir com:

- o ganho da aula do conceito;
- a frente do card;
- a resposta escondida;
- a âncora na E1.

Em `relacao_nova`, o alvo deve ser a **relação acrescentada**. Não gastar o card redefinindo os componentes prévios.

## 15. Cloze

Padrão:

- uma ocorrência de `c1`;
- nunca `c2` em card autoral verbal;
- uma palavra por padrão;
- duas palavras quando formam unidade semântica que perderia sentido ao ser dividida;
- três palavras somente em expressão médica indivisível, com justificativa explícita;
- quatro ou mais bloqueia.

Não esconder uma oração inteira, enumeração ou definição.

O cloze deve esconder o conhecimento que merece recuperação, não a palavra mais fácil de prever gramaticalmente.

## 16. Indução, ambiguidade e vazamento

A frente deve permitir uma resposta claramente melhor sem depender do Extra.

Bloquear:

- resposta previsível apenas pela gramática;
- resposta visível em outra parte da frente;
- sigla ou definição que entrega o cloze;
- palavra abstrata que aceita muitos sinônimos;
- várias respostas semanticamente defensáveis;
- discriminador presente somente no Extra;
- metade de um par mostrada enquanto a outra metade é escondida quando o objetivo é aprender a associação completa.

O Extra é lido depois da tentativa; ele não pode tornar a pergunta respondível retroativamente.

## 17. Extra

O Extra explica, conecta mecanismo, corrige confusão ou oferece imagem útil.

Não deve:

- carregar a informação necessária para descobrir a resposta;
- transformar o card em miniapostila;
- introduzir conteúdo não ensinado;
- compensar uma frente ruim.

Manter curto; máximo canônico de 100 palavras.

## 18. Idioma

Cards são em português médico natural.

Termos técnicos em inglês podem permanecer quando forem nomenclatura médica legítima, mas a prosa da frente e do Extra deve ser portuguesa.

## 19. Imagens e Image Occlusion

Imagem só entra quando cumpre tarefa cognitiva concreta.

- mecanismo: imagem no Extra quando melhora reconstrução;
- identificação/localização: preferir tarefa visual/IO;
- não criar IO decorativo;
- não esconder a estrutura que deveria ser reconhecida; mascarar o rótulo-resposta;
- recortar mantendo marcos necessários à orientação;
- toda mídia nova exige proveniência.

IO canônico:

- `hide_two_guess_two`;
- uma ou duas máscaras;
- duas máscaras somente se formam conjunto coerente, com `pair_rationale`;
- prompt e respostas em português;
- pergunta mostra rótulos mascarados;
- resposta revela a imagem original;
- nenhum rótulo-resposta pode permanecer visível fora das máscaras;
- previews de pergunta e resposta e evidência de vazamento são obrigatórios no contrato de revisão.

## 20. Redundância dentro da aula

Não criar duas recuperações equivalentes só porque a formulação muda.

Mesma resposta ou mesmo `retrieval_target` exige revisão de redundância. Se duas recuperações realmente diferentes usam a mesma resposta, justificar a derivação explicitamente; caso contrário, manter apenas uma.

O pipeline **não depende de consultar decks anteriores**. A prevenção de recapitulação longitudinal vem do gate de ganho da aula + planilha mestra.

## 21. Revisão independente

Autoria e revisão são etapas distintas.

O autor não libera o próprio lote apenas escrevendo `passed=true`.

A revisão deve procurar, em especial:

- card que cobre suporte em vez de ganho;
- ambiguidade;
- indução;
- recuperação duplicada;
- resposta genérica;
- Step 1 lateral;
- vazamento visual;
- excesso de cards;
- relação nova reduzida a uma definição antiga.

Relatórios devem ficar ligados por hash ao conjunto exato de cards revisado. Se o conteúdo muda, a revisão anterior deixa de valer.

## 22. Feedback e regressões

Erro corrigido uma vez não pode depender de memória do agente.

Todo padrão de defeito recorrente deve virar:

1. regra neste arquivo, quando for política geral;
2. exemplar/anti-exemplar em `EXEMPLARES-CARDS.md`, quando o contraste ajudar;
3. teste executável quando houver forma mecânica de bloqueá-lo.

A suíte de regressões faz parte obrigatória da CI. Não manter regressão bloqueadora somente como nota manual.

## 23. Definição de card/deck aprovado

Um deck só está pronto quando:

- a aula foi lida globalmente antes da autoria;
- o contexto curricular da planilha mestra foi registrado;
- todos os conceitos foram classificados por `learning_role`;
- nenhum `pre_requisito`, `revisao`, `contexto`, `exemplo` ou `mencao` recebeu card;
- cada card representa ganho específico da aula;
- todos os cards estão ancorados na E1;
- atomicidade, idioma, cue quality, volume, mídia e IO passaram nos gates;
- regressões obrigatórias passaram;
- o conjunto final foi revisado depois da última alteração;
- o artefato final passou por auditoria do pacote gerado.

A regra-mãe é simples:

> **O card não deve existir porque o assunto apareceu. Ele deve existir porque a aula ensinou algo novo que vale a pena recuperar.**
