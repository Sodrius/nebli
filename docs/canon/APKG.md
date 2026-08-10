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

A montagem é feita por `flashcards/scripts/build_apkg_offline.py`, que escreve a coleção
diretamente em SQLite a partir do `contrato-cobertura.json`. Os cards moram no contrato; o
montador não guarda uma segunda cópia e aborta se o total real divergir do previsto ou
ultrapassar o teto congelado.

## Auditoria do arquivo real

Abrir o ZIP/APKG e a coleção; conferir notas, cards, decks, GUIDs, note types,
campos, clozes, tags, mapa de mídia e referências HTML. Renderizar todos os
autorais e IO, toda mídia alterada e uma amostra das cópias. Um relatório JSON
sem inspeção do pacote não aprova a aula.

A renderização é em **navegador de verdade**, por
`flashcards/scripts/render_apkg_previews.py`: ele aplica o template do note type às notas do
pacote e fotografa pergunta e resposta de cada card. Relatório JSON não vê tela — foi assim
que passou despercebido um note type de IO cuja frente não exibia imagem nenhuma. Os PNGs
precisam ser olhados, não apenas gerados. O renderizador reproduz o DOM do Anki (`<div class="card">`, sem contêiner extra); rodar em largura de tablet (`--width 1500`) e em modo noturno (`--night`) faz parte do gate, porque é onde aparecem desalinhamento de coluna e contraste ruim.

O AnKing completo, índices e shards de mídia ficam em armazenamento privado.
O GitHub contém apenas código, schemas e manifestos sem conteúdo protegido.
