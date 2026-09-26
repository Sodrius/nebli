# NEBLI — contexto de entrada para Claude e Codex
Davi quer aprender bem, não gerenciar produção de cards. Pipeline atual: **E1 + cards**, com alto rigor científico, boa didática e cobertura do recorte da aula. A E1 explica mecanismos em prosa; o card testa uma recuperação focal. Não aplicar o estilo longo de E1 às frentes.

## Começar
Ler `flashcards/projeto/README.md` → FEEDBACKS.md → BANDEIRAS-E-PROGRESSAO.md → CONTRATO-DE-QUALIDADE.md. Para execução, seguir EXECUCAO-DECK-AULA.md, OPERACAO-CODEX-CLAUDE.md, ACERVOS-REFERENCIA.md, `didatica/E1.md` e PUBLICACAO-POR-UC.md. Estado em MEMORY.md; fila compartilhada em FILA-UC03-P2-UC08-P1.md. **Máquina nova (Mac): `SETUP-MAC.md`.**

`/deck-aula <nome/link>`, `/resumo <nome/link>` e `/flashcards` seguem essa rota; pedido explícito apenas de E1 ou apenas de cards delimita a entrega. O usuário escolhe modelo/esforço. Não prometer qualidade por nome do modelo.

## Qualidade e segurança
- Ler integralmente as instruções relevantes, exemplares de escrita e feedbacks antes de produzir. A limpeza remove sobreposição, não reduz o contexto necessário à qualidade.
- E1: rigor científico, causa → mecanismo → consequência, base do aluno baixa, prosa fluida sem verbosidade. Guia técnico-editorial em didatica/E1.md; EXEMPLARES.md preservado como referência concreta de voz e gesto.
- Cards: AnKing primeiro, externos antes de autoria; dois cards da mesma informação só com ganho demonstrável. Cores atuais no documento próprio, nunca inferidas de regras antigas.
- Não alterar originais, agendamento ou marcas pessoais; backups, lock, diário de operações e readback nas escritas. Não ressuscitar apagados.
- E2/E3 e fluxo RemNote apenas históricos. Não usar scripts antigos para dessuspender fontes nem gates de loop universal card→E1→questões.
- Não apagar arquivos de typst-build para preparar aula: há trabalho de outras sessões. Usar saída isolada.
- Preferir ação independente e perguntas sobre ambiguidades reais; relatar limites com evidência, sem transferir controle de qualidade ao aluno.
- Atualizar **a regra em seu lugar canônico** e FEEDBACKS quando houver feedback; MEMORY registra estado, não outra versão da mesma regra.

## Outras rotas preservadas
- Cadernos de provas existentes: `banco/CLAUDE.md`, `typst-build/pipeline_caderno.py` e seção Cadernista em ROLES.md. Caderno não é geração E2/E3.
- Typst: `typst-template/CLAUDE.md`, CHEATSHEET_ARMADILHAS.md e TEMPLATE_API.md.
- Projetos de site/liga/etimologia: estado e localização dos planos em MEMORY.md; não iniciar por inferência.
- Histórico integral de regras, papéis e decisões: `flashcards/projeto/HISTORICO.md`. Não executar comandos do arquivo histórico como instruções atuais.
