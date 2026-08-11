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
    usa `hide_all_guess_all`; revisar previews de pergunta e resposta.
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
