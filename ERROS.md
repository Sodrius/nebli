# ERROS.md — bloqueios ativos

Consultar antes de fechar E1 ou deck-aula. O contrato detalhado de cards está em
`docs/canon/CARD-QUALITY.md` e é hard gate.

## Conteúdo e cobertura

- E1 nunca é documento Typst autônomo: importa `nebli_v2_apostila.typ`, usa
  `main.typ`/`resumindo.typ` e não redefine página, parágrafo, capa ou
  hierarquia visual localmente.
- PDF compilado ainda não está aprovado. Todas as páginas precisam ser
  renderizadas e revisadas; clipping, overflow ou defeito visual pendente
  bloqueiam a entrega.

1. Não declarar cobertura por impressão. Todo conceito nuclear aparece no
   contrato, tem âncora literal na E1 e card adequado.
2. Card não ensina conteúdo novo. Aprofundamento entra primeiro na E1.
3. Step 1 aprofunda o mesmo tema; não admite vizinhos high-yield, Step 2,
   conduta, dose, guideline ou tópico que exija uma nova aula.
4. Subtópicos recebem cards proporcionalmente ao peso, sem cota uniforme.

## Cards

5. Autorar direto: `card_source_mode=authored_only` dispensa busca externa.
6. Idioma é medido **só na frente**. Extra em português não compensa frente
   inglesa: foi assim que uma prova inteira saiu em inglês com o gate aprovando.
7. Declaração não é evidência. Booleano que o próprio agente escreve não fecha
   card: idioma, papel do cloze, ablação, teto e vazamento visual são medidos.
8. Autoral: português médico natural, alvo único, **uma ocorrência de c1**, Extra
   curto em português e sem voz de apostila.
9. Nunca misturar `nucleo` e `optional` no mesmo card; opcionais vão para
   `::Optional`.
10. Um card testa uma recuperação independente. Cloze: 1 palavra por padrão,
    2 quando necessário e 3 só com justificativa; 4+ bloqueia.
11. Nunca ultrapassar `card_budget.hard_max`; contar cards reais, não notas ou
    conceitos. Teto **ausente bloqueia**: ele nunca é derivado da quantidade de
    cards produzidos, senão a comparação é sempre verdadeira.
12. Resposta abstrata que serve a qualquer frase (`tempo`, `tamanho`,
    `arquitetura`) não é recuperação. Nem resposta que oferece alternativas
    (`x ou y`, `x/y`) sem `compound_answer_reason` declarado.
13. O termo cobrado precisa existir na âncora da E1. Card não estreia conteúdo:
    se o aluno não teve como aprender, a recuperação não é possível.
14. A informação que decide a resposta mora na frente. Card cujo discriminador só
    aparece no Extra cobra o que só é lido depois de responder.
15. Duas recuperações do mesmo alvo custam duas revisões por dia. Mesma resposta
    ou mesmo `retrieval_target` no lote exige `derivation_rationale`.
16. Card sem perda concreta na ablação sai. `ablation_loss` que apenas reformula
    o enunciado não é perda: precisa citar outro conceito do contrato.
17. Defeito já apontado pelo usuário não pode reaparecer. Todo comentário vira
    entrada em `flashcards/tests/feedback_regressions.json`, com exemplo
    reprovado rodado contra o gate real.
18. Não aceitar card por semelhança temática. `relevant=true` significa que a
    recuperação específica pertence à aula e possui âncora E1.
19. Não aceitar card que peça duas ou mais recuperações independentes, listas ou
    enumerações disfarçadas. Atomicidade é hard gate.

## Visual

20. Imagem do mesmo tema não basta: precisa cumprir a tarefa daquele card.
21. Identificação/localização pede IO ou prompt visual; mecanismo pede imagem no
    Extra. Não esconder a pista morfológica que deveria ser reconhecida.
22. Em IO rotulado, mascarar o rótulo-resposta. Mapa coerente com várias partes
    usa `hide_two_guess_two`, no máximo duas máscaras e justificativa do par; revisar previews de pergunta e resposta.
23. IO exige `visual_evidence`: previews de pergunta e resposta com hash,
    `crop_ratio` (recorte quase igual ao slide inteiro bloqueia), varredura de
    texto e termos proibidos cobrindo todas as respostas. `no_leak: true`
    declarado não substitui a varredura.
24. Anatomia macro e histologia não fecham apenas com cards verbais quando a
    aula exige reconhecimento.
25. Bloquear imagem ilegível, genérica, decorativa, sem proveniência, quebrada ou
    que revele a resposta.
26. IO multi-rótulo exige conjunto coerente. Máscaras precisam estar dentro da
    imagem e o runtime deve comprovar máscara na pergunta + imagem/solução na
    resposta.

## AnkiDroid / artefato

27. O fluxo canônico termina no AnkiDroid. Não declarar pronto enquanto o recibo
    não confirmar `installed_card_count == expected_card_count`.
28. O deck final deve ter nome canônico `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
    opcionais ficam em `<Deck>::Optional`.
29. O manifesto canônico é `nebli-ankidroid-deck-v3`: contém o plano completo e
    a mídia nova necessária. O Companion resolve AnKing localmente e instala
    autorais/IO diretamente.
30. Falha parcial não deixa lote parcial novo: reverter as notas NEBLI criadas
    naquela tentativa. Nunca apagar ou modificar fonte AnKing.
31. Reexecutar o mesmo deck é idempotente: conteúdo igual é reutilizado;
    conteúdo NEBLI alterado é substituído pela versão nova sem duplicar.
32. O gate final é 100% card a card, sem amostragem. Uma falha bloqueia o deck.
33. Não depender de Drive, Colab, AnkiConnect ou APKG no fluxo normal.
34. Não versionar AnKing, decks privados, índices privados ou mídia protegida.
35. E2, E3 e RemNote não podem reaparecer no comando padrão.
36. Uma consulta local incompatível com a versão do Content Provider não pode
    abortar a aula inteira: a busca vira `unresolved` e usa o fallback validado
    daquele card. O planejamento é somente leitura e precisa terminar antes da
    criação do deck, para nenhuma falha deixar deck vazio.
37. Nunca consultar campos completos da coleção inteira para buscar AnKing. A
    busca deve incluir o deck-fonte, obter IDs primeiro e hidratar somente o
    pool limitado; coleções de vários GB podem derrubar o processo Android.
38. Regex executada no Android precisa escapar chaves literais dos dois lados e
    não deve ser compilada em inicializador estático crítico. OpenJDK e Android
    podem divergir; um padrão aceito apenas no teste JVM não pode inutilizar o
    Companion com `ExceptionInInitializerError`.
39. Ao corrigir incompatibilidade de regex Android/JVM, auditar todas as
    ocorrências de `Pattern.compile`, `replaceAll`, `split` e `matches` no app;
    não encerrar a correção após encontrar somente o primeiro padrão inválido.
40. Teste JVM e compilação do APK não bastam para liberar o Companion. O gate
    precisa executar no runtime Android com AnkiDroid oficial instalado, criar
    fonte local, resolver/copy AnKing, instalar autoral e confirmar a contagem
    real de cards pelo Content Provider antes de publicar o artefato.
## Qualidade funcional da recuperação

41. Passar nos gates formais não significa ser um bom card. A revisão final
    precisa julgar a recuperação produzida: pergunta inequívoca, resposta útil,
    dificuldade adequada e relação direta com a âncora da E1.
42. Bloquear cloze de palavra genérica ou previsível pela gramática quando ele
    não recupera conhecimento médico específico. Termos como “contexto”,
    “resposta”, “migração”, “adaptação” ou “plasticidade” exigem uma pista que
    determine precisamente o conceito e exclua sinônimos plausíveis.
43. Não mostrar metade de um par para esconder apenas a outra (`X e {{c1::Y}}`)
    quando o objetivo é aprender a associação completa. Tratar o par canônico
    como uma unidade justificável ou criar recuperações independentes.
44. O conteúdo efetivamente cobrado pelo cloze deve coincidir com o conceito e
    com a consulta AnKing. Se a busca pede duas moléculas, uma via ou uma
    relação completa, não aceitar um card que teste somente um fragmento fácil.
45. Informação presente apenas no Extra não conta como cobertura. Toda afirmação
    nuclear precisa ser recuperada no Front/cloze de pelo menos um card; o Extra
    serve para explicar, contextualizar ou corrigir confusões.
46. Cards de mecanismo devem cobrar o elo causal ou funcional relevante, não
    somente o nome da etapa. Saber o rótulo “priming”, por exemplo, não substitui
    recuperar o que ele produz e como difere da montagem/ativação posterior.
47. Sequências, mapas topológicos e vias devem ser decompostos em recuperações
    atômicas suficientes. Um card abstrato sobre “localização” não cobre as
    associações concretas entre compartimento, sensor e ligante.
48. Bloquear respostas com várias alternativas semanticamente defensáveis. Se
    “destruição”, “eliminação”, “inflamação” ou “morte” cabem na mesma lacuna, a
    formulação precisa ser reescrita até existir uma resposta claramente melhor.
49. Atomicidade funcional é diferente de ter uma única marca `c1`. Uma frase
    com um cloze pode continuar exigindo uma lista, esconder múltiplas relações
    ou revelar a própria resposta por pistas vizinhas.
50. Quantidade correta de cards não comprova cobertura. Conferir a distribuição
    por objetivos e mecanismos da E1, substituindo cards fracos antes de usar a
    margem do orçamento para simplesmente adicionar mais cards.
51. Imagem no Extra precisa acrescentar compreensão mecanística ou espacial ao
    card. Não criar IO quando não há tarefa visual de reconhecimento, mas também
    não aceitar um deck inteiramente verbal quando a E1 exige interpretar uma
    estrutura, lâmina, mapa ou relação espacial.

## Identidade do deck

52. O nome do deck não é campo livre. Gerador e Companion derivam e conferem
    `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>` a partir dos quatro
    metadados; override divergente ou segmento ausente bloqueia a instalação.

## Suspenso — vale somente com `anking.status = active`

As regras abaixo governam a cópia de AnKing e de decks externos. O modo ativo é
`authored_only`, então **nenhuma delas se aplica hoje**. Ficam registradas porque
descrevem trabalho já validado, não porque estejam em vigor: enquanto o canônico
disser uma coisa e `config/pipeline.json` disser outra, o agente escolhe.

- Buscar AnKing e decks externos antes de autorar; guardar a rejeição real.
- Preservar campos, HTML, note type, tags, mídia e créditos do card-fonte.
- A cópia NEBLI usa nota independente e nunca altera o original.
- Resultado AnKing ambíguo nunca é escolhido à força. Rebuscar com aliases e,
  permanecendo ambíguo, usar fallback autoral/IO já validado.
- Todo card AnKing planejado no manifesto final precisa ter fallback válido.
- Para card AnKing, validar o card realmente selecionado — nota, ordinal e
  pergunta/resposta renderizadas — e não apenas a semelhança temática da nota.
- `prefer_anking=true` sem efeito mecânico não é prioridade: buscar a nota por
  contexto e o sibling pela resposta esperada.
- O nome local `AnKing Step Deck` não é identidade confiável; `source_filter` é
  dica, e falhando, rebuscar sem escopo e exigir marcador.
- Fallback autoral não pode ocultar falha técnica quando um AnKing adequado já
  foi validado.
