# ERROS.md — bloqueios ativos

Consultar antes de fechar E1 ou deck-aula. O contrato detalhado de cards está em
`docs/canon/CARD-QUALITY.md` e é hard gate.

## Conteúdo e cobertura

1. Não declarar cobertura por impressão. Todo conceito nuclear aparece no
   contrato, tem âncora literal na E1 e card adequado.
2. Card não ensina conteúdo novo. Aprofundamento entra primeiro na E1.
3. Step 1 aprofunda o mesmo tema; não admite vizinhos high-yield, Step 2,
   conduta, dose, guideline ou tópico que exija uma nova aula.
4. Subtópicos recebem cards proporcionalmente ao peso, sem cota uniforme.

## Cards

5. Buscar AnKing e decks externos antes de autorar; guardar a rejeição real.
6. Preservar campos, HTML, note type, tags, mídia e créditos do card-fonte.
7. A cópia NEBLI usa nota independente e nunca altera o original.
8. Autoral: inglês médico natural, alvo único, **uma ocorrência de c1**, Extra
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
14. Resultado AnKing ambíguo nunca é escolhido à força. Rebuscar com aliases e,
    permanecendo ambíguo, usar fallback autoral/IO já validado.
15. Todo card AnKing planejado no manifesto final precisa ter fallback válido;
    assim uma diferença na coleção local não deixa o Deck-Aula incompleto.

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
46. Para card AnKing, validar o card realmente selecionado — nota, ordinal e
    pergunta/resposta renderizadas — e não apenas a semelhança temática da nota.
    Resultado clínico vizinho, cloze irrelevante ou card excessivamente guiado
    deve ser rejeitado e substituído pelo próximo candidato ou pelo fallback.
47. Imagem no Extra precisa acrescentar compreensão mecanística ou espacial ao
    card. Não criar IO quando não há tarefa visual de reconhecimento, mas também
    não aceitar um deck inteiramente verbal quando a E1 exige interpretar uma
    estrutura, lâmina, mapa ou relação espacial.

## Gate que mede declaração em vez de conteúdo

52. O relatório card-a-card não pode ser escrito à mão em paralelo ao deck.
    Gerar sempre com `flashcards/scripts/derivar_validacao_cards.py`: números
    mensuráveis (cloze, frente, Extra, máscaras) saem do card real e a âncora é
    conferida contra a E1 fonte. Dois arquivos independentes fazem o gate medir
    o relatório, não o deck.
53. Exigir prova de uma busca AnKing que a sessão não pode ter feito produz
    declaração falsa, não bloqueio. Usar `anking_search_mode`: `session_local`
    só quando a coleção esteve ao alcance; `device_deferred` quando o Companion
    resolve no aparelho; `unavailable` quando não há coleção alguma, sempre com
    `anking_deferral_reason` concreto. Fonte local com `unavailable` bloqueia.
54. Não validar no plano o que só existe depois da instalação. Score, note type,
    sibling e `resolved_without_fallback` são propriedades do resultado da busca;
    em `device_deferred` o gate valida consulta, resposta esperada e o fallback
    que será instalado.
55. Passar no lint funcional é obrigatório e não substituível por justificativa
    genérica. Os escapes (`generic_answer_reason`, `pair_is_unit_reason`,
    `duplicate_answer_reason`) exigem texto que explique por que aquela
    formulação é a recuperação correta — se não houver o que escrever, o card
    está errado e deve ser reescrito.

## Contrato entre manifesto e Companion instalado

56. **Renomear um token do manifesto é mudança quebrante.** Quem lê o manifesto
    é o Companion **já instalado no aparelho**, não o código do repo. Em
    2026-08-12 o token de IO virou `hide_two_guess_two` nos dois lados do repo,
    mas o APK do tablet era do #18: a instalação morreu no primeiro card IO,
    `IO gate: [io_mode_must_be_hide_all_guess_all]`, com rollback do lote
    inteiro depois de 23 cards criados.
    Regra: nome novo **soma-se** ao antigo como alias no Companion; o antigo só
    sai depois que o APK do aparelho for reinstalado e um recibo real confirmar.
57. O vocabulário emitido no manifesto vive em
    `config/pipeline.json → ankidroid.installed_companion.io_mode_token` e
    descreve o **aparelho**, não o repo. Só trocar esse valor depois de
    reinstalar o Companion e confirmar por recibo. `io_mode_contract` continua
    registrando a regra canônica contra a qual o card foi validado.
58. Gerador Python e gate Java precisam ser comparados por teste
    (`flashcards/tests/test_contrato_companion.py`), que lê `IO_MODES` do
    `CardRules.java`. Sem isso, os dois lados podem divergir e a falha só
    aparece na hora da instalação, no aparelho, com o lote perdido.

## Resolução AnKing e identidade do deck

48. `prefer_anking=true` sem efeito mecânico não é prioridade. A nota deve ser
    buscada por contexto e o sibling pela resposta esperada; usar a consulta
    longa para pontuar um cloze curto produz falso `unresolved` e fallback.
49. O nome local `AnKing Step Deck` não é identidade confiável. Para AnKing,
    `source_filter` é dica; se falhar, rebuscar sem escopo e exigir marcador.
50. Fallback autoral não pode ocultar falha técnica quando um AnKing adequado já
    foi validado. `anking_required=true` bloqueia o lote e o recibo registra o
    motivo, consultas tentadas e contagem de candidatos.
51. O nome do deck não é campo livre. Gerador e Companion derivam e conferem
    `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>` a partir dos quatro
    metadados; override divergente ou segmento ausente bloqueia a instalação.
