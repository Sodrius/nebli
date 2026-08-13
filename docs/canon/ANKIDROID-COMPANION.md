# Companion e AnkiDroid

O manifesto ativo é `nebli-ankidroid-deck-v3`, `pipeline_version=e1-deck-v11` e exige Companion 0.8.0 (`versionCode 13`). Ele declara capacidades, hashes individuais, hash do conjunto ordenado, E1 e mídia.

O Companion verifica compatibilidade antes de criar o deck, instala autorais e IO, valida mídia/renderização, usa subdeck `::Optional`, atualiza card cujo hash mudou, evita duplicação quando o hash é igual e remove todas as notas novas se uma instalação falhar. O recibo precisa confirmar `installed_card_count == expected_card_count` e o deck canônico selecionado.

AnKing e decks externos permanecem implementados para reativação futura, mas `authored_only` proíbe busca e cópia no fluxo atual.
