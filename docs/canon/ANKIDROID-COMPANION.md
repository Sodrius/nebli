# AnkiDroid Companion — arquitetura canônica

Status: backend preferido do pipeline `e1-deck-v5`. Desktop/AnkiConnect permanece apenas como fallback.

## Objetivo

O AnkiDroid instalado no tablet é simultaneamente:

1. fonte local do AnKing;
2. motor de busca/seleção dos cards-fonte;
3. destino do deck-aula;
4. dono da mídia já existente na coleção.

O fluxo normal não exige Drive, Colab, índice externo de 6 GB, `.apkg` nem importação manual de cards AnKing.

## Regra de segurança

- READ permitido em qualquer deck fonte, inclusive AnKing.
- WRITE permitido somente em decks cujo nome comece por `NEBLI::`.
- UPDATE/DELETE de notas fonte são proibidos.
- Toda cópia relê a origem depois da escrita e verifica `mid + flds + tags` inalterados.
- Instalação é idempotente por `lesson_slug + source_note_id`.
- Falha parcial nunca autoriza apagar ou alterar a fonte.
- Resultado ambíguo não é auto-selecionado: fica `unresolved`.

## Semântica da cópia

Para cards provenientes do AnKing/deck externo:

- preservar o `mid`/note type;
- preservar `flds` literalmente, incluindo HTML, clozes e referências de mídia;
- preservar tags de origem e acrescentar apenas proveniência NEBLI;
- criar nota nova no deck-aula;
- não carregar scheduling/history da fonte;
- inferir o ordinal relevante em notas cloze quando houver evidência suficiente;
- suspender siblings não selecionados;
- se o sibling correto não puder ser inferido com segurança, bloquear a cópia daquele conceito.

É proibido prefixar ou modificar `Text` em cópias AnKing.

## Manifesto preferido — v2

O core produz `flashcards/manifests/<slug>.ankidroid.json`. Ele não precisa conhecer IDs locais do AnkiDroid.

```json
{
  "schema": "nebli-ankidroid-lesson-v2",
  "lesson_slug": "anato-10-intestino-grosso",
  "target_deck": "NEBLI::UC02::P3::Anatomia::Intestino grosso",
  "mutate_source": false,
  "search": {
    "min_score": 0.82,
    "min_margin": 0.06,
    "max_candidates": 80,
    "prefer_anking": true,
    "require_anking_marker": false
  },
  "concepts": [
    {
      "id": "c001",
      "query": "marginal artery of Drummond",
      "aliases": ["marginal artery of the colon"],
      "required": true
    }
  ]
}
```

O Companion recebe os conceitos atômicos, busca na coleção local, ranqueia candidatos e copia somente os casos que passam os gates.

O schema `nebli-ankidroid-v1`, baseado em IDs/query já curados, permanece como compatibilidade legada.

## Busca e ranking local

O caminho preferido usa a própria busca do AnkiDroid; não duplica os 6 GB do AnKing.

Para cada conceito:

1. buscar a query principal e aliases;
2. ampliar de forma limitada por tokens longos se a busca vier estreita demais;
3. remover cópias `NEBLI::source::copy` do pool;
4. preferir candidatos com marcadores típicos do AnKing quando existirem;
5. calcular cobertura lexical + bônus de frase exata + bônus pequeno de proveniência AnKing;
6. exigir `min_score` e margem sobre o segundo colocado;
7. bloquear em vez de adivinhar quando a margem for insuficiente.

Ranking local é um **pré-curador conservador**, não uma licença para selecionar qualquer resultado textual. O core continua responsável por atomizar bem os conceitos e por tratar lacunas reais.

## Cloze siblings

Uma note do AnKing pode gerar vários cards. Ao selecionar uma note:

- se há apenas um número de cloze, ele é ativado;
- se há vários, o Companion compara o texto de cada resposta cloze com o conceito;
- somente um ordinal claramente compatível é ativado;
- siblings não selecionados são suspensos;
- ausência de evidência suficiente gera `ambiguous_cloze_sibling` e nenhuma cópia automática para aquele conceito.

## Pipeline canônico

1. Extrair learning objectives e conceitos atômicos da aula.
2. Gerar E1 e garantir que cada conceito candidato esteja ancorado.
3. Gerar o manifesto v2 com conceitos/aliases.
4. Abrir o manifesto no Companion.
5. Companion busca no AnKing local e ranqueia candidatos.
6. Candidatos confiáveis são copiados fielmente para `NEBLI::*`.
7. Casos ambíguos/lacunas ficam `unresolved` no recibo.
8. O core cria autorais/IO apenas para lacunas comprovadas e mantém as regras de atomicidade/cloze/visual do pipeline.
9. Gate final compara conceitos previstos, resolvidos e pendentes.

## Recibo

Após cada corrida o Companion grava recibo JSON contendo:

- `concepts_total`;
- `resolved_count`;
- `unresolved_count`;
- notas criadas e reaproveitadas idempotentemente;
- fontes verificadas intactas;
- siblings suspensos;
- `resolved[]` com `source_note_id`, `copy_note_id`, score e ordinais;
- `unresolved[]` com motivo (`no_candidate`, `low_confidence`, `ambiguous_cloze_sibling`, etc.);
- timestamp.

`unresolved_count > 0` não autoriza seleção forçada. Esses itens voltam ao pipeline para refino/autorais.

## Compatibilidade

`montar_deck_aula.py --backend desktop` mantém AnkiConnect/APKG como fallback. O backend canônico é `ankidroid`, manifest v2, resolução local por conceitos.
