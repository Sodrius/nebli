# Publicação: um APKG atual por UC

> **Suspenso por Davi em 23/09/2026 (noite): não subir APKG ao Drive.** O empacotador segue útil para backup local; as seções de upload abaixo ficam como histórico até nova decisão.

Decisão explícita posterior ao questionário, 23/09/2026. Substitui o upload padrão de APKG por aula. E1, guia, fontes e relatórios continuam por aula.

## Contrato

- Publicar **um arquivo `NEBLI-UC03.apkg`, `NEBLI-UC08.apkg` etc.** na pasta pessoal da respectiva UC. A cada aula nova/alterada, exportar novamente a UC inteira existente e atualizar o mesmo file_id. Não somar arquivos históricos, não publicar só o incremento, não exportar AnKing/Referências/Etimologia.
- Conservar hierarquia `NEBLI::UCxx::Px::Componente::Aula` conforme calendário/material; não inventar prova ausente nem mover deck antigo silenciosamente para padronizar. Hierarquia física e associações por card são coisas diferentes.
- Pacote **comprimido internamente e ainda terminado em `.apkg`**, pronto para importar; sem `.zip` externo obrigatório. Mídia não recebe compressão com perda, redução de resolução ou recompressão de imagem.
- **Zero bandeiras visíveis no arquivo publicado.** Rosa, verde, vermelho e laranja permanecem na coleção viva. Nunca limpar a coleção e tentar restaurar as bandeiras depois.
- O normal no Anki é manter cards ativos. Candidatos à suspensão pós-prova já recebem rosa no plano de curadoria; Davi decide a cada prova se suspende ou mantém. Nenhuma suspensão automática por data, falta de HY ou rosa.
- Sem pedido contrário, o empacotador conserva agendamento/histórico exportado. “Sem flags” não significa resetar progresso. O APKG não substitui AnkiWeb/sincronização; reimportação sobre uma coleção estudada precisa de cautela.

## Implementação disponível

Depois de instalar e verificar a aula e reconciliar a seleção viva da UC:

```text
python -m nebli.package_uc --uc UC03 --output arquivos-trabalho/deck-aula-<slug>-<data>/NEBLI-UC03.apkg
```

O comando exporta via AnkiConnect, com mídia/agendamento, e trabalha em cópia temporária do pacote. Remove apenas os bits de bandeira, preserva IDs/GUIDs, campos, modelos, histórico e mídia; aplica ZIP DEFLATE nível 9 e compara conteúdo lógico antes/depois. Confere todos os IDs da UC, escopo dos decks, integridade do ZIP/SQLite, mapa de mídia e bytes dos arquivos não alterados. Faz readback dos IDs/bandeiras vivos. Gera `.publication-ready.json`; **não faz upload**.

O formato tratado é o APKG SQLite legado que o exportPackage atual produz (`collection.anki21`/`collection.anki2`). `.anki21b` é recusado explicitamente: não fingir que o formato moderno é SQLite simples. Não afirmar compressão máxima possível; o formato nativo moderno pode comprimir melhor, mas sua limpeza de bandeiras exige implementação/teste próprio. Referência: [manual de exportação](https://docs.ankiweb.net/exporting.html).

O comando recusa saída existente, UC vazia, divergência de IDs e conteúdo fora da UC. Perfil precisa ser identificado. Se o pai UC não existir, só aceita outro ancestral existente quando ele contém **exatamente todo o conjunto** de cards da UC; nunca publica subconjunto como completo. Em caso de falha, resolver a causa em vez de executar restauração de pacotes antigos.

**Limite:** exportação física da UC. Se houver card compartilhado associado à UC mas fisicamente em outra UC, comparar associações antes de publicar. A união lógica exige coleção temporária isolada/seleção por IDs, ainda não implementada neste utilitário; não duplicar ou mover cards vivos para contornar nem declarar cobertura do pacote completa. No teste atual não havia compartilhados entre UCs identificados.

## Upload e identidade do arquivo

1. Ler `config/publicacoes-uc.json`; se ausente, inicializar do `.example.json`, nunca sobrescrever estado existente. O arquivo real é local e ignorado no Git. Resolver a pasta privada da UC por metadados e hierarquia, nunca por adivinhação. Não reutilizar IDs dos APKGs antigos por aula como se fossem arquivo da UC.
2. Se já existe file_id, atualizar o conteúdo desse arquivo. Se não, listar a pasta por nome exato antes de criar; resolver colisões sem sobrescrever arquivo incerto.
3. Fazer upload apenas de pacote verificado da execução atual. Após timeout, readback antes de repetir. Conferir nome, bytes, pasta, link e permissões.
4. Persistir entrada da UC com file_id, parent_folder_id, nome, link, hash local, bytes, IDs/contagens das aulas incluídas, run_id e horário da confirmação. Não gravar publicado antes da confirmação.
5. Entregar o link estável da UC, E1/guia da aula, onde estudar e contabilidade **da aula + total único da UC**, incluindo diferenças entre flags locais e arquivo sem flags.

Uploads antigos por aula continuam históricos: não apagar/mover/reimportar sem pedido. Após a limpeza de 23/09, jamais usar esses APKGs para repor conteúdo ausente ou montar a UC.

## Teste realizado nesta rodada

UC03 viva: 89 cards, 74 notas, duas aulas restantes. Exportação local verificada em `arquivos-trabalho/reinicio-uc-2026-09-23/teste-local-2/`: 8.421.490 → 7.713.658 bytes, 67 mídias, 15 bandeiras retiradas só da cópia. IDs e bandeiras vivos inalterados. Não publicado nem reimportado; importação Mac/Android e execução pelo Claude ainda não testadas. O teste não certifica a curadoria desses 89 cards.
