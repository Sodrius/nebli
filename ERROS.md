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
8. Autoral: português médico natural, alvo único, **uma ocorrência de c1**, Extra
   curto em português e sem voz de apostila.
9. Nunca misturar `nucleo` e `optional` no mesmo card; opcionais vão para
   `::Optional`.
10. Um card testa uma recuperação independente. Cloze: 1 palavra por padrão,
    2 quando necessário e 3 só com justificativa; 4+ bloqueia.
11. Nunca ultrapassar `card_budget.hard_max`; contar cards reais, não notas ou
    conceitos.
12. Não aceitar card por semelhança temática. `relevant=true` significa que a
    recuperação específica pertence à aula e possui âncora E1.
13. Não aceitar card que peça duas ou mais recuperações independentes, listas ou
    enumerações disfarçadas. Atomicidade é hard gate.

## Visual

16. Imagem do mesmo tema não basta: precisa cumprir a tarefa daquele card.
17. Identificação/localização pede IO ou prompt visual; mecanismo pede imagem no
    Extra. Não esconder a pista morfológica que deveria ser reconhecida.
18. Em IO rotulado, mascarar o rótulo-resposta. Mapa coerente com várias partes
    usa `hide_two_guess_two`, no máximo duas máscaras e justificativa do par; revisar previews de pergunta e resposta.
19. Anatomia macro e histologia não fecham apenas com cards verbais quando a
    aula exige reconhecimento.
20. Bloquear imagem ilegível, genérica, decorativa, sem proveniência, quebrada ou
    que revele a resposta.
21. IO multi-rótulo exige conjunto coerente. Máscaras precisam estar dentro da
    imagem e o runtime deve comprovar máscara na pergunta + imagem/solução na
    resposta.

## AnkiDroid / artefato

22. O fluxo canônico termina no AnkiDroid. Não declarar pronto enquanto o recibo
    não confirmar `installed_card_count == expected_card_count`.
23. O deck final deve ter nome canônico `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
    opcionais ficam em `<Deck>::Optional`.
24. O manifesto canônico é `nebli-ankidroid-deck-v3`: contém o plano completo e
    a mídia nova necessária. O Companion resolve AnKing localmente e instala
    autorais/IO diretamente.
25. Falha parcial não deixa lote parcial novo: reverter as notas NEBLI criadas
    naquela tentativa. Nunca apagar ou modificar fonte AnKing.
26. Reexecutar o mesmo deck é idempotente: conteúdo igual é reutilizado;
    conteúdo NEBLI alterado é substituído pela versão nova sem duplicar.
27. O gate final é 100% card a card, sem amostragem. Uma falha bloqueia o deck.
28. Não depender de Drive, Colab, AnkiConnect ou APKG no fluxo normal.
29. Não versionar AnKing, decks privados, índices privados ou mídia protegida.
30. E2, E3 e RemNote não podem reaparecer no comando padrão.
31. Uma consulta local incompatível com a versão do Content Provider não pode
    abortar a aula inteira: a busca vira `unresolved` e usa o fallback validado
    daquele card. O planejamento é somente leitura e precisa terminar antes da
    criação do deck, para nenhuma falha deixar deck vazio.
32. Nunca consultar campos completos da coleção inteira para buscar AnKing. A
    busca deve incluir o deck-fonte, obter IDs primeiro e hidratar somente o
    pool limitado; coleções de vários GB podem derrubar o processo Android.
33. Regex executada no Android precisa escapar chaves literais dos dois lados e
    não deve ser compilada em inicializador estático crítico. OpenJDK e Android
    podem divergir; um padrão aceito apenas no teste JVM não pode inutilizar o
    Companion com `ExceptionInInitializerError`.
34. Ao corrigir incompatibilidade de regex Android/JVM, auditar todas as
    ocorrências de `Pattern.compile`, `replaceAll`, `split` e `matches` no app;
    não encerrar a correção após encontrar somente o primeiro padrão inválido.
35. Teste JVM e compilação do APK não bastam para liberar o Companion. O gate
    precisa executar no runtime Android com AnkiDroid oficial instalado, criar
    fonte local, resolver/copy AnKing, instalar autoral e confirmar a contagem
    real de cards pelo Content Provider antes de publicar o artefato.
## Qualidade funcional da recuperação

36. Passar nos gates formais não significa ser um bom card. A revisão final
    precisa julgar a recuperação produzida: pergunta inequívoca, resposta útil,
    dificuldade adequada e relação direta com a âncora da E1.
37. Bloquear cloze de palavra genérica ou previsível pela gramática quando ele
    não recupera conhecimento médico específico. Termos como “contexto”,
    “resposta”, “migração”, “adaptação” ou “plasticidade” exigem uma pista que
    determine precisamente o conceito e exclua sinônimos plausíveis.
38. Não mostrar metade de um par para esconder apenas a outra (`X e {{c1::Y}}`)
    quando o objetivo é aprender a associação completa. Tratar o par canônico
    como uma unidade justificável ou criar recuperações independentes.
39. O conteúdo efetivamente cobrado pelo cloze deve coincidir com o conceito e
    com a consulta AnKing. Se a busca pede duas moléculas, uma via ou uma
    relação completa, não aceitar um card que teste somente um fragmento fácil.
40. Informação presente apenas no Extra não conta como cobertura. Toda afirmação
    nuclear precisa ser recuperada no Front/cloze de pelo menos um card; o Extra
    serve para explicar, contextualizar ou corrigir confusões.
41. Cards de mecanismo devem cobrar o elo causal ou funcional relevante, não
    somente o nome da etapa. Saber o rótulo “priming”, por exemplo, não substitui
    recuperar o que ele produz e como difere da montagem/ativação posterior.
42. Sequências, mapas topológicos e vias devem ser decompostos em recuperações
    atômicas suficientes. Um card abstrato sobre “localização” não cobre as
    associações concretas entre compartimento, sensor e ligante.
43. Bloquear respostas com várias alternativas semanticamente defensáveis. Se
    “destruição”, “eliminação”, “inflamação” ou “morte” cabem na mesma lacuna, a
    formulação precisa ser reescrita até existir uma resposta claramente melhor.
44. Atomicidade funcional é diferente de ter uma única marca `c1`. Uma frase
    com um cloze pode continuar exigindo uma lista, esconder múltiplas relações
    ou revelar a própria resposta por pistas vizinhas.
45. Quantidade correta de cards não comprova cobertura. Conferir a distribuição
    por objetivos e mecanismos da E1, substituindo cards fracos antes de usar a
    margem do orçamento para simplesmente adicionar mais cards.
47. Imagem no Extra precisa acrescentar compreensão mecanística ou espacial ao
    card. Não criar IO quando não há tarefa visual de reconhecimento, mas também
    não aceitar um deck inteiramente verbal quando a E1 exige interpretar uma
    estrutura, lâmina, mapa ou relação espacial.

## Identidade do deck

51. O nome do deck não é campo livre. Gerador e Companion derivam e conferem
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
