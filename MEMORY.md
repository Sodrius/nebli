# MEMORY — estado e pendências, não outra política
Atualizado em 25/09/2026. Política: `flashcards/projeto/README.md`. Feedback: `flashcards/projeto/FEEDBACKS.md`. Histórico integral anterior preservado em `backups/contexto-2026-09-25/MEMORY.md`; inventário e destinos em HISTORICO.md. Números abaixo têm data, não substituem consulta viva.

## Situação
- Davi está no 1º ano/2º semestre em 2026, Turma B. UC03, UC08, UC16 e demais UCs descritas nos cronogramas. Calendário individual: planilha, aba Mês prevalece.
- Lote UC03 P2/UC08 P1: propriedade e andamento em FILA-UC03-P2-UC08-P1.md. Não assumir aula de outro executor.
- Auditoria de 25/09: snapshot inicial 1.453 cards médicos; após correções limitadas e adição concorrente, 1.523 no recibo. Origem de 38 cards corrigida, quatro notas ajustadas, uma nota rejeitada excluída com backup, 161 rosas antigos migrados a azul com autorização daquela rodada. Não repetir essa migração.
- Auditoria: `flashcards/projeto/AUDITORIA-2026-09-25.md`; evidência privada em `arquivos-trabalho/auditoria-lote-2026-09-25/`. Não foi auditoria científica completa nem demonstração de aprendizagem; snapshot inicial tinha reps=0.
- Atualização atual: pipeline E1 + cards; sem repetição semântica sem ganho; novas cores por retenção, não HY literal. A exceção “só deck” acabou prospectivamente. Upload APKG continua pausado.
- Mac principal declarado e Android; Windows perfil Davi consultado. Não assumir sincronização remota sem teste.

## Próximas ações delimitadas
00. **26/09 (Davi):** passa a trabalhar no **Mac**; tudo no GitHub `Sodrius/nebli` (público — dados de deck ficam fora, ver `.gitignore`). Instalação: `SETUP-MAC.md`. Pendência do deck de Edema (10 lacunas propostas, decisão de Davi sobre itens e idioma): `arquivos-trabalho/deck-aula-edema-congestao-2026-09-25/LACUNAS-PROPOSTAS.md`. Robbins (501 MB, Drive) ainda não lido.
0. **25/09 (Davi):** piloto E1 + cards de Edema e congestão pelo Claude, "realmente com qualidade" — entregue e **reprovado por Davi no mesmo dia** ("excessivamente clínico... o outro caminho era bem melhor", F-C20). Deck de Edema **restaurado** ao estado anterior (36 cards; `restore-receipt.json`; piloto em `backup-piloto-antes-de-restaurar.apkg`). E1 do piloto só local, não publicada. Próximo passo: ajustes pequenos e aprovados sobre o deck existente, não reconstrução. Depois de calibrado, Davi apaga os decks do lote UC03 P2/UC08 P1 e todos são refeitos pela rota nova (fila). Snapshot vivo 25/09: 1.537 cards, **0 estudados**. Calibração do tamanho da E1 pela importância da aula está em outra conversa de Davi: não alterar didatica/E1.md nem a trava do precompile-check até ele avisar.
1. Amostra concluída: 9 cards de Edema, 5 brancos → verdes; resultado 7 verdes/2 azuis. Notas/agendamento e flags externas à amostra preservados. Recibo observou 1.537 cards médicos (produção concorrente); não auditoria geral. Conferir `flashcards/projeto/RELATORIO-CONSOLIDACAO-2026-09-25.md`. Não recolorir toda a coleção; calibrar próximas aulas gradualmente.
2. Compartilhados: identidade única pode existir sem seleção acessível na segunda aula. Falta validar interface de estudo por IDs/cloze e união lógica entre UCs no pacote. Consulta no navegador não é agendador novo.
3. Redundância/autoria do lote antigo: triagem dirigida pendente (inclui PRR/PAMP e autorais de Edema); não prometer que documentação resolveu toda a coleção.
4. Validar nova execução E1 + cards pelo Claude, fontes/precisão/visual/identidade e cores, depois pequeno lote e uso real. Modo somente-E1 dos scripts precisa teste de uma apostila real além dos testes estruturais.
5. Carga **150 novos/dia** num preset único para todo NEBLI (Davi, 25/09; antes 35) e média ~50 verdes/aula: observar tempo/revisões reais e união de compartilhados. Davi ajusta o ritmo; o deck não é reduzido para caber (F-C18). 25/09 ~11:30: Microbiologia inteira dessuspensa a pedido (65 cards; registro `arquivos-trabalho/deck-ops/20260925-113128-dessuspender.json`); nenhum suspenso em NEBLI::UC*. O Anki do Windows fechou durante um sync às 11:34 (causa não identificada, sem crash.log); reaberto, WAL recuperado, readback e sync ok. Desde ~12:00: total de cards no nome dos decks (add-on `nebli_decks`, só no Windows) e filtrado `NEBLI · Microbiologia: todos os novos` (476 novos, prova UC03 P2 em 02/10); encerrar com `python -m nebli.decks liberar microbiologia --encerrar` quando Davi pedir.
6. Progressão futura: estudo institucional inicial em BANDEIRAS-E-PROGRESSAO; confirmar currículos/cronogramas da turma quando publicados. Step 1 pensado para fim do quarto ano, ainda sem data marcada.
7. Respostas antigas Q18/Q22: a solução técnica/interface dos compartilhados continua aberta, não pedir novamente preferências já compreendidas. Retenção pós-prova é pessoal.

## Outras frentes preservadas
- Cadernos: pipeline_caderno.py; banco/CLAUDE.md e ROLES.md.
- Banco e cronogramas: gerar slim quando banco for atualizado; nenhuma faxina agendada em execução comprovada.
- Site NEBLI e Liga Clínica: dormentes; gatilhos, caminhos dos planos e escopo no MEMORY arquivado, § Active Projects. Ler o plano integral antes de retomar. Não iniciar como parte desta limpeza.
- Geração 20 encerrada; arquivos de resumos/modelos/figuras e EXEMPLARES preservados.
- Backlog antigo completo (inclusive detalhes de Typst, projetos e decisões não revogadas) em MEMORY arquivado, § Pendências abertas. Ao retomar tema específico, consultar essa seção: não foi dado como resolvido nem descartado.
