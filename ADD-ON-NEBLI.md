# add-on NEBLI

Pedido de Davi em 08/10/2026: ao final da campanha, reunir os add-ons próprios em **um único add-on NEBLI**, instalável e compartilhável com os amigos. Este documento reúne o escopo e o estado; o pacote único ainda não foi criado.

Preferências canônicas: [MEMORY.md](MEMORY.md). Fila: [ESTADO-ATUAL.md](ESTADO-ATUAL.md). Não antecipar esta consolidação às correções dos decks.

## O que será reunido

| Módulo próprio atual | Funções a preservar |
|---|---|
| `nebli_atalhos` | Atalhos de revisão, bandeiras, comentário, desfazer e enterrar; regras vigentes de suspensão no Reviewer |
| `nebli_decks` + `nebli/anki_addon.py` | Contagem de cards nos nomes, ferramentas de decks já existentes e ajustes do Browse |
| `nebli_explicacoes` | Explicação única por card ao apertar Tab no verso, com estado de atualização |

Inventário instalado conferido em 08/10: **Review Heatmap (Glutanimate), Anki GoalBar (moritzvitt), Advanced Browser, VS Code For Anki e AnkiConnect são add-ons de terceiros e ficam separados**. Não renomeá-los nem empacotá-los como autoria NEBLI. Ajustes próprios de integração podem entrar como módulos NEBLI; dependências externas devem ser identificadas separadamente.

## Browse — já aplicado no Anki

- **J** alterna a suspensão dos cards selecionados, substituindo Ctrl+J. Atua na tabela; a busca e o editor continuam recebendo texto normalmente. A ação e o desfazer são os nativos do Anki.
- Coluna **Suspenso** mostra **Sim/Não**, independente da bandeira. Em modo Notas, mostra quantos irmãos estão suspensos sobre o total. Enterrado e suspenso são estados distintos.
- Coluna **Ordem da aula** mostra **somente números**: `01`, `02`, `03`… sem `bt03`, `an07` ou nome do bloco.
- Card compartilhado mantém uma posição por aula e uma única identidade/histórico. Na consulta de uma aula, mostra sua posição no contexto dessa aula. Quando não há um contexto de aula resolvido, exibe as posições numéricas distintas separadas por ` | `.
- Os identificadores internos de aula continuam necessários para não misturar posições de aulas diferentes; não aparecem na coluna. Salvar a posição por associação card–aula é obrigatório em toda geração/atualização.
- A ordenação padrão é numérica pela aula, com o cabeçalho correspondente. Uma escolha manual de outra coluna é respeitada durante a consulta. Não alterar vencimentos/histórico para simular essa ordem.

Implementação atual: [ordem.py](nebli/ordem.py), [anki_addon.py](nebli/anki_addon.py). Os três módulos continuam instalados separadamente até a consolidação final.

## Preparação necessária para compartilhar

1. Empacotar a lógica hoje carregada do repositório local. O amigo não pode precisar do caminho `/Users/davisousa/NEBLI` nem do projeto de produção.
2. Configuração única, com funções identificáveis e ativáveis. Preservar preferências existentes na migração e não impor a rotina pessoal de Davi a novos usuários.
3. Migrar com backup a base de explicações e configurações dos três módulos; evitar hooks/atalhos duplicados e permitir retorno à instalação anterior.
4. Separar o **leitor de Tabs** do processo de geração. Hoje as explicações ficam em SQLite local por card; instalar o add-on sozinho não transfere nem gera as explicações dos decks dos amigos. Definir exportação/importação com identidade verificada antes de prometer compartilhamento dos Tabs.
5. Não incluir coleção, comentários, histórico, credenciais, logs ou caminhos pessoais no pacote público. Recursos de deck e programa são entregas distintas.
6. Gerar um `.ankiaddon` versionado, instruções de instalação/atualização e inventário do que está incluído.
7. Testar instalação limpa, atualização, migração, colisão com os módulos antigos, Browse, edição de texto, desfazer, suspensão com bandeira, irmãos e cards compartilhados. Validar nos sistemas suportados; teste no Mac não comprova Windows nem AnkiDroid.

## Estado e aceitação

- [x] Inventário dos três add-ons próprios e dos terceiros.
- [x] J e coluna de suspensão aplicados e verificados na interface real.
- [x] Rótulo da ordem alterado para números; testes de posição por aula compartilhada.
- [ ] Unificação dos módulos e configurações.
- [ ] Migração da base de Tabs e distribuição independente do repositório.
- [ ] Pacote `.ankiaddon` e teste em perfil limpo.
- [ ] Entrega para compartilhar com amigos, ao final da campanha.

Evidências do Browse e limites dos testes: `arquivos-trabalho/auditoria-browse-2026-10-08/` e `arquivos-trabalho/auditoria-uc08-provas-2026-10-08/`. Não marcar pacote pronto com base neste documento.


## Estudo de um deck com um clique (11/10/2026)
Na tela de baralhos, engrenagem do deck → **NEBLI: estudar tudo deste deck (prova)**: cria (ou reconstrói) o filtrado `NEBLI · <deck>: estudo para prova`, fora da árvore NEBLI, com todos os cards **não suspensos** do ramo, **reagendando pelo FSRS** (o estado de memória dos cards se atualiza a cada resposta). Sem mexer em configuração; para encerrar, Excluir o filtrado (os cards voltam às aulas). **NEBLI: recalcular memória FSRS deste deck** recalcula estabilidade e dificuldade dos cards já revisados a partir do histórico. Testado em 11/10 pelo gatilho `arquivos-trabalho/anki-acao-pedido.json` ({"acao": "estudar"|"memoria", "deck": "<nome canônico>"}); o item de menu precisa de **reiniciar o Anki uma vez** (o carregador `__init__.py` mudou).

## Tela de baralhos e Browser (11/10/2026, F-20261011-CLAUDE-04/05)
- **Nome da aula em negrito** e os números `(total|ativos|novos)` sem negrito; **deck todo suspenso** (ativos = 0) aparece em **vermelho**. Feito no HTML da tela de baralhos (`deck_browser_will_render_content`), sem renomear nada.
- **Apagar no Browser renumera a ordem**: ao apagar notas, as posições `NEBLI::ordem::<curto>-NN` seguintes da mesma aula descem para fechar o buraco (`notes_will_be_deleted` + `operation_did_execute`). Agendamento, bandeiras e conteúdo não mudam.
- Os ganchos novos estão no carregador `anki-addon/nebli_decks/__init__.py`: **reiniciar o Anki uma vez**; a lógica (`nebli/anki_addon.py`) se recarrega sozinha.
