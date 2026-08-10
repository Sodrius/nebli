# Contrato APKG offline

AnkiConnect não é dependência canônica. O pacote final precisa ser montado e
auditado offline.

## Montagem

- cópias de fontes recebem GUID novo e mantêm `source_guid`;
- note types, templates, campos, tags e mídia são preservados;
- mídia idêntica é deduplicada por hash;
- colisão de nome com conteúdo diferente é renomeada e o HTML é atualizado;
- opcionais ficam em subdeck próprio;
- nenhum arquivo privado é versionado.

## Auditoria do arquivo real

Abrir o ZIP/APKG e a coleção; conferir notas, cards, decks, GUIDs, note types,
campos, clozes, tags, mapa de mídia e referências HTML. Renderizar todos os
autorais e IO, toda mídia alterada e uma amostra das cópias. Um relatório JSON
sem inspeção do pacote não aprova a aula.

O AnKing completo, índices e shards de mídia ficam em armazenamento privado.
O GitHub contém apenas código, schemas e manifestos sem conteúdo protegido.
