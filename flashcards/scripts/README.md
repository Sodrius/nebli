# Scripts do pipeline

## Caminho canônico v3

- `index_private_apkg.py`: cria índice local do AnKing/decks privados;
- `search_private_index.py`: recupera candidatos reais por conceito;
- `validate_lesson_contract.py`: gate de cobertura E1/Step 1/cards/visual;
- `io_manual_from_image.py`: manifesto e preview de IO sem AnkiConnect;
- `audit_apkg.py`: abre e audita o pacote exportado real;
- `gate_deck_aula_completo.py`: combina contrato congelado e APKG auditado.

Os demais scripts são operações históricas ou utilitários específicos. Eles não
são chamados por `/resumo` e não definem o contrato atual. Migre um utilitário
antes de recolocá-lo no caminho canônico; em particular, não use montagem ou
validação baseada em AnkiConnect para aprovar uma entrega.
