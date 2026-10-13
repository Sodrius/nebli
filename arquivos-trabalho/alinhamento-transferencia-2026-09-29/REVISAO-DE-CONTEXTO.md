# Revisão da transferência de preferências — 29/09/2026

Pedido: recuperar o entendimento construído com Davi e fazer cada sessão aplicar o padrão dele, sem exigir que reensine. Esta rodada revisa contexto e artefatos locais; não altera Anki nem certifica cientificamente os decks.

## Evidências relidas

- Decisões de 22/09: objetivo de aprender com bons decks, cobertura sem teto, separação entre disponibilidade e manutenção.
- Respostas literais de 23/09: Q3/Q6 (teoria, reconhecimento e conteúdo da aula), Q10/Q11 (alternativos antes de autoria), Q12–17 (visual, AnKing e verso), Q29/Q30 (correções conservadoras, qualidade transferível ao Claude).
- Respostas literais de 28/09: story teller corrigido pelo usuário; aprender com AnKing real; preservar boa frente, atomicidade/contexto, imagens, tradução integral e núcleo sem quota.
- FEEDBACKS até F-C44, README, contrato, bandeiras, estilo, tradução, entradas e handoffs. F-C45/46 acrescentam as mensagens desta conversa, não novas escolhas presumidas.
- Caso Vascularização aprovado e Intestinos não aprovado; relatórios e campos locais de FI08/BT03, com cuidado para distinguir versões.

## Falhas encontradas e correção

| Falha de transferência | Evidência | Correção documental |
|---|---|---|
| Intenção substituída por minimalismo | Pilotos registram irmãos retirados como triviais, cobertura contestada e frentes extensas | README explica cobertura completa relevante, disponibilidade versus núcleo e comparação por ganho; entrada exige decisão concreta |
| Propostas viraram preferências | F-C44 misturava fala literal com “verde generoso”, “redundância só literal” e forma universal | Manter fala, diagnosticar regressão e identificar interpretações; não usar essas expressões como política nova |
| Instalação/ritmo contraditórios | Plano exigia revisão Codex antes de instalar e também registrava F-C43 de revisão após instalação; continuava sem feedback apesar de pausa por pares | Consolidado F-C43: revisão própria, instalação, revisão Codex, retorno de Davi por par |
| Estado inicial aparecia como atual | “Primeira atribuição FI08”, “reset não confirmado” e “nenhum deck instalado” junto dos recibos novos | Entradas encaminham ao estado atual; primeira atribuição vira histórico, prioridade é corrigir o par |
| Duas cópias de handoff | Raiz repetia o documento inteiro, com links relativos inadequados e regras antigas | Raiz só encaminha; handoff canônico reúne início, critérios essenciais e estado |
| Exemplar aprovado continha regra de cor revogada | Vascularização ainda mandava verde só por HY | Mantido caso positivo e história; regra marcada como superada |
| Leitura declarada não provava aplicação | Existência dos documentos não impediu F-C44 | Toda sessão relaciona escolhas reais aos critérios/exemplares no relatório já exigido; não criar outro formulário para o usuário |

## Tradução: o que foi e não foi conferido

Lidos Text/Extra EN/PT dos registros iniciais de 19 notas BT03 e 22 FI08. Isso permite localizar alterações e avaliar a redação disponível, mas não comprova os campos vivos ou a apresentação da versão atual. Não houve revisão científica integral, renderização independente ou readback do Anki nesta rodada.

Achados concretos dos registros iniciais:

- BT03 `adventicia`: desaparecem destaques do contexto original e o negrito passa para a resposta; largura da imagem também muda. O registro didático só descreve o acréscimo de exemplos. É necessário distinguir a decisão visual da tradução e verificá-la.
- BT03 `mucosa-camadas`/`parietal-hcl` e FI08 `calmodulina`/`mlck`/`mlcp`: clozes removidos em curadoria e resultado PT apresentados juntos. As remoções não provam erro linguístico, mas comparar o original externo diretamente com PT não demonstra preservação de uma base curada intermediária.
- Há notas com `state: reviewed`, `visual: pendente de render após aplicação` e `independente: aguarda revisão Codex`, enquanto o relatório afirma renderização concluída. Reconciliar estado e versão; nenhuma dessas declarações isoladas é certificado de qualidade extrema.
- FI08 `reflexo-curto` e `varicosidades`, BT03 `mucosas-colo` e `parietal-canaliculo` são casos para conferir extensão/forma contra ESTILO e F-C44. Alterar estilo é etapa editorial identificada, não uma “tradução” que apaga conteúdo silenciosamente.
- Fontes: FI08 relatava Margarida inacessível; BT03 relatava não ter visto figuras do slide nem o PDF do Junqueira. Não substituir essas pendências por alegação genérica de bibliografia conferida.

Durante a leitura, os planos foram alterados por outra execução: os registros mais recentes observados já contêm 37 notas em cada `translation-plan.json`. FI08 `plan.selection_hash=1e3c86162ce68358`; BT03 `b978f7080b018d7c`. Nessa observação, ambos ainda tinham `visual: pendente` nas 37 entradas e nenhuma base curada intermediária explícita nos campos inspecionados. **A leitura textual anterior não aprova essas novas versões.** Não interferi nos scripts, planos ou aplicação do trabalhador.

Próxima revisão: fixar os arquivos/versão efetivamente entregues; reconciliar fonte original → base curada → PT; conferir semântica, estrutura/destaques e renderização, incluindo todos os irmãos afetados; comparar com o estado vivo e recibo. Preservar comentários, histórico e alterações concorrentes. Critérios e esta limitação estão no contrato de tradução/handoff; não há confirmação independente de “extrema qualidade” ainda.

## Entendimento que a próxima sessão deve demonstrar

O deck pode ser grande, mas cada inclusão precisa ensinar/recuperar algo relevante da aula. Não fazer cards para tudo que um livro ou figura menciona, nem reduzir o que precisa estar disponível por confundir seleção com núcleo. Buscar AnKing e alternativos, consultar bibliografia, usar autoria somente onde importa e falta candidato adequado. O autoral deve parecer e funcionar como bom AnKing: foco, contexto, fluidez e imagem útil; story teller ensina e relembra, não exige história.

Calibração de Davi não é validação técnica delegada ao aluno. Ele define a preferência e refina casos reais; executor busca, confere e corrige. Não aumentar volume, verdes ou clínica mecanicamente para responder a uma crítica local. Quando um tradeoff novo não estiver resolvido pelas respostas anteriores, apresentar exemplos e recomendação antes de transformá-lo em regra.

## Preservação e limite

Documentos anteriores e artefatos disponíveis na captura foram preservados em `antes/`, com hashes em `before-hashes.json`. Textos de cards ficam em arquivos privados ignorados pelo Git. Preferências históricas não foram apagadas; a operação corrente foi separada delas. Mudanças locais de outros trabalhos e dos decks em correção foram preservadas.

Conferência desta rodada: entradas apontam à mesma intenção; raiz não duplica handoff; fila não ordena reinício FI08/reset nem contém regras concorrentes de revisão/pausa. Isso verifica a passagem documental. A prova de transferência será uma execução que mantenha esses critérios no deck entregue, sem Davi repeti-los. Não chamar isso de resolvido apenas por editar instruções.

## Complemento — UC03, brainstorming e 100 perguntas

Pedido posterior de Davi: usar UC03 como base que já funcionava e aperfeiçoá-la; consolidar no MEMORY intenção/uso, registrar todo feedback de ambos e preparar 100 perguntas A/B/C/D sobre o projeto inteiro. Pedido repetido após interrupções, tratado uma vez.

Lido o brainstorming atual pelo conector Drive (`modified_time=2026-09-29T13:51:03.575Z`); literal privado em BRAINSTORMING-DRIVE-29.txt. Recuperados decisões de 22/09, respostas de 23/28, relatórios UC03 e registros antigos do monitor em MEMORY arquivado/INFRA-REMOTO. Não executados scripts históricos nem e-mails/macros/tarefas. Relatórios UC03 de 24/09 descrevem versões e limitações antigas; o mapa inicial de Antibióticos não equivale à v3 aprovada.

O Claude acrescentou F-C45 “calibração é do executor” enquanto este trabalho estava em curso. Preservado como **F-20260929-CLAUDE-01**, resolvendo colisão com F-C45 “reforço de fontes, autoria e limite”. Fala explicitamente impede pedir a Davi julgamento de total/cobertura/verdes. Registros v3/v3c FI08/BT03 relatam correções e revisão por agente; esta consolidação não as desfaz nem certifica. Consulta pontual read-only de deckNames viu UC03 1.173 e UC08 96 (FI08 47/BT03 49). A captura ampliada subsequente falhou na conexão; não foi concluída comparação de campos vivos nesta rodada. Com o pedido ampliado para memória/questionário, essa leitura não era necessária para concluir a preparação.

Entregue `flashcards/projeto/CALIBRACAO-DECK-100-PERGUNTAS.md`: dez blocos, Q001–Q100, 400 alternativas, histórico/leitura atual e resposta em branco por item. Abrange objetivo, cobertura, fontes, escrita, clínica/Step, imagens/tradução, bandeiras, uso, monitor/tutor/macros e memória/feedback. Nenhuma resposta presumida. Uma conferência programática confirmou sequência exata, A/B/C/D em cada item, títulos distintos, 100 espaços de resposta e ausência de links locais quebrados nos nove documentos principais. `git diff --check` sem erros.

MEMORY agora consolida o que Davi quer e por quê, além do estado. Entradas AGENTS/CLAUDE/comando/handoff recuperam essa memória para mensagem comum. FEEDBACKS exige captura de todo feedback pelo receptor na mesma sessão, releitura antes da entrega e atualização de critérios/estado com evidência. Registros novos do Codex têm IDs por data/executor para reduzir colisão concorrente. Cobertura exige varredura de toda a fonte, não só validar uma lista curta de objetivos escolhidos pelo próprio executor.

Documentação pronta para a próxima sessão neste workspace; respostas ainda pendentes e qualidade de próxima execução ainda por demonstrar. Sem garantia absoluta de comportamento de qualquer IA, coletor automático de chats, commit/push, sincronização entre computadores ou implementação das ferramentas futuras. Alterações de código/artefatos do Claude e outras mudanças locais foram preservadas. Snapshot documental anterior a esta rodada em `antes-calibracao-100/`.
