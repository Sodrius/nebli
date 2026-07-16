# VEREDITO — anti-indução (`lint_neblicard.py`)

## Decisão

Implementar um linter determinístico antes do card-mirror. O linter não tenta substituir o julgamento LLM; ele barra vazamentos óbvios e manda zona cinza para o card-mirror.

## Gate hard inicial

- Nome da resposta já aparece no stem, principalmente como head-word.
- Sigla no cloze com expansão visível no stem.
- Parêntese/aposto que entrega a resposta por overlap ou prefixo numérico.
- Negrito no stem que casa a raiz da resposta.

## Zona cinza

- Cloze longo.
- Marcadores causais demais no stem antes de um cloze curto.
- Score composto intermediário.

Esses casos viram `MIRROR`, não reprovação automática, porque há AnKing real com linguagem causal, frases longas e padrões conversacionais.

## Implementado

Script: `flashcards/scripts/lint_neblicard.py`.

Uso:

```bash
python flashcards/scripts/lint_neblicard.py flashcards/cards-nebli/<slug>.json
python flashcards/scripts/lint_neblicard.py flashcards/cards-nebli/<slug>.json --json
```

Política de exit:

- `0`: passou.
- `1`: há `REJECT`.
- `2`: não há reject, mas há `MIRROR`.

## Dissidência vencida

O Propositor queria usar comprimento de cloze e “mecanismo no stem” como reprovação forte. Isso foi rebaixado: comprimento e causalidade sozinhos dão falso positivo em cards AnKing reais. Entram como score/zona cinza.
