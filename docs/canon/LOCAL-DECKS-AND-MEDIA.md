# Decks locais e mídia nova — complemento canônico v6

Este arquivo complementa `CARD-QUALITY.md` e `ANKIDROID-COMPANION.md`.

## Deck externo local

`source=external_deck` segue a mesma exigência pedagógica de uma cópia AnKing:

- só usar quando o card testa a recuperação específica da aula;
- preservar literalmente note type, campos, HTML, clozes, tags, mídia e créditos;
- nunca modificar a fonte;
- inferir/ativar somente o sibling relevante;
- exigir `query` + aliases úteis;
- usar `source_filter` quando o deck/note type/tags de origem forem conhecidos,
  para reduzir falsos positivos;
- exigir fallback autoral ou IO já validado no plano final;
- se busca/ranking/sibling forem ambíguos, usar o fallback em vez de escolher à
  força.

O marcador AnKing é obrigatório apenas para `source=anking`; um deck externo usa
seu próprio `source_filter` quando disponível.

## Imagem nova no Extra de autoral

Uma imagem no Extra precisa ter função cognitiva real, tipicamente mecanismo,
relação espacial ou comparação que agrega mais que decoração.

No `deck-data.json`, registrar em `extra_images` como objeto:

```json
{
  "path": "imagem.png",
  "source_credit": "fonte real",
  "alt": "descrição curta"
}
```

Regras:

- `source_credit` é obrigatório;
- preferência absoluta por fonte real e adequada;
- imagem genérica/decorativa não entra;
- o gerador calcula SHA-256, embute a mídia no manifesto e remove o caminho local;
- o Companion entrega a mídia ao AnkiDroid e substitui o placeholder pelo nome
  final retornado pela coleção;
- placeholder não resolvido é falha de runtime e bloqueia o lote.

## IO

Toda mídia IO nova também exige `source_credit`. O fato de a imagem estar no
slide não elimina a necessidade de registrar sua proveniência no plano quando
ela for empacotada como mídia nova.

## Definição de completo

O Deck-Aula v6 não tem exceção escondida para mídia ou deck externo. AnKing,
deck externo, autorais com ou sem imagem e IO devem chegar ao mesmo
`NEBLI::<...>` no AnkiDroid, respeitando os gates card a card e a contagem final.
