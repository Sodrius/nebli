# Operação compartilhada
Rota atual em README.md; conteúdo/aceite em CONTRATO-DE-QUALIDADE.md. **E1 + cards**, sem API paga adicional obrigatória. Ambos os executores usam os mesmos artefatos e critérios.

## Diagnóstico
Abrir na raiz. Confirmar perfil vivo, AnkiConnect e ferramentas Drive disponíveis; não copiar nome de ferramenta/caminho do outro computador.
`python -m nebli.preflight --catalog --output arquivos-trabalho/deck-aula-<slug>-<data>/catalogo.json`
Somente leitura no Anki. Catálogo descobre raízes externas/modelos, mas não aprova conteúdo. Resolver errors/partial antes de escrita insegura. Comentários em cards vivos são pendências; apagados não ressuscitam.

## Execução segura
Seguir EXECUCAO-DECK-AULA.md e fila. Criar lock exclusivo `arquivos-trabalho/ANKI-ESCRITA.lock` com executor/aula/horário; só remover seu próprio lock após readback. Não atropelar lock existente. Curadoria em leitura pode continuar.
Um run_id/pasta por execução, plano de IDs/clozes/fields/cor/origem, snapshot antes, backup para remoções, journal e recibo. Após timeout, procurar identidade antes de repetir.
Não rodar `nebli/anki_apply.py` nem scripts antigos de corridas como gerador universal. Existem decisões específicas e operações por nota que podem mover/expor irmãos indevidos.

## E1
Ler didatica/E1.md e exemplares. Mesmas fontes/objetivos para E1 e cards, sem reciprocidade artificial de cada frase. Usar modo somente-E1 dos scripts e build isolado; não limpar arquivos de outra sessão. Verificar PDF textual/visual, fonte, figuras e cópia leve. Não declarar capítulo consultado por causa de figura no slide.

## Compartilhados
Uma identidade/histórico; seleção deve registrar card_id e cloze/template pertinente. Tag vive na nota e pode selecionar irmãos fora do recorte. Deck físico não exibe automaticamente associações de outras aulas.
Até a interface completa, entregar consulta explícita pelos IDs **vivos e validados**, conferindo conjunto retornado. Não duplicar/mover cards para simular duas aulas. Consulta do navegador não é botão de estudo calibrado; declarar essa diferença.
Empacotador atual cobre conjunto físico da UC. Compartilhados fisicamente em outra UC exigem união lógica isolada ainda não implementada; não anunciar pacote completo se faltam.

## Mexer em decks a pedido de Davi
Ação num deck vale para ele e todos os subdecks; trecho do nome sem acento basta. Só NEBLI:: e NEBLI-deck::, nunca AnKing/Referências.
`python -m nebli.decks status [trecho]` · `dessuspender|suspender <trecho> [--simular]` · `desfazer <registro>` · `liberar <trecho> [--encerrar]` · `instalar-addon`
Suspender grava os card IDs em `arquivos-trabalho/deck-ops/` antes de mudar, confere por ID e sincroniza. Suspender/dessuspender só por pedido dele (Manutenção no README).

**Total no nome (Davi, 25/09):** o add-on `nebli_decks` (Windows; lógica em `nebli/anki_addon.py`, recarregada sem reiniciar o Anki; log em `addons21/nebli_decks/user_files/log.txt`) põe o total de cards no nome de todo deck NEBLI, ex.: `Antibióticos e resistência (112)`. A identidade é o nome canônico sem o número (`nebli.rotulos.canonical`); leitura compara por ele. **Toda escrita no Anki passa por `with nebli.decks.escrita(Anki(), "<aula>"):`**, que cria ANKI-ESCRITA.lock, espera o add-on devolver os nomes canônicos, libera, espera os totais voltarem e sincroniza. Script que cria o lock à mão espera `deckNames` sem nenhum " (N)" antes do primeiro findCards/createDeck: sem isso, createDeck("NEBLI::...") cria árvore paralela e addNotes falha com "deck was not found". Em outro computador sem o add-on, os nomes chegam rotulados pelo sync e `escrita` recusa escrever.

**Opções do baralho:** um preset único para todo NEBLI (150 novos/dia). Status acusa deck fora dele ou dois presets com o mesmo nome (armadilha do menu de Opções); conserto `flashcards/scripts/nebli_novos.py --alinhar`, que também renomeia o preset largado. **O teto diário do NEBLI vale também ao clicar numa aula ou num filtrado dentro da árvore** (medido 25/09, Anki 26.9: limite "Este baralho" e "Somente hoje" num ramo não liberam nada). Para liberar todos os novos de um ramo sem mexer no resto: `liberar <trecho>` grava `config/anki-decks.json` e o add-on mantém no nível de cima o filtrado `NEBLI · <ramo>: todos os novos`, reconstruído quando entram novos no ramo; `--encerrar` devolve os cards às aulas. Conferência "ao clicar": pedido em `arquivos-trabalho/anki-contagem-pedido.json`, resposta do add-on em `anki-contagem-resposta.json` (`nebli.decks.count_on_click`).

## Entregas e escala
E1/guia por aula na pasta privada; APKG local UC inteira:
`python -m nebli.package_uc --uc UC03 --output <corrida>/NEBLI-UC03.apkg`
PUBLICACAO-POR-UC.md descreve compressão/validação sem flags no arquivo. **Upload APKG pausado**; não atualizar Drive por inferência. Se reautorizado, manter file_id/destino em config/publicacoes-uc.json, readback e permissões; não sobrescrever IDs antigos inadvertidamente.

Sincronizar após escrita autorizada e readback; aceitação de sync não confirma dispositivo remoto. Não mudar o limite de novos/dia (150 desde 25/09) nem o agendador sem pedido de Davi. Validar pequena amostra/lote e uso real antes de escala. Documentos e testes estruturais não garantem julgamento de conteúdo pelo modelo.
