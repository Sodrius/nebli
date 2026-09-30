# Histórico — versões integrais, sem políticas paralelas

## Consolidação de 29/09/2026

Davi pediu juntar memórias, incorporar suas respostas e excluir arquivos repetidos. Foram retirados **26 documentos de flashcards/projeto e o handoff da raiz**, deixando 7 arquivos no projeto. MEMORY é a memória normativa única; execução, estado, fontes e feedback têm funções distintas. Não criar stubs nos caminhos apagados nem restaurar instruções antigas como políticas atuais.

[Arquivo único de preservação](../../backups/contexto-2026-09-29-consolidacao.zip): 41 documentos originais + `manifest.json` com caminho, tamanho e SHA-256. Inclui documentos removidos, entradas/memória e teste antes da consolidação. A cópia respondida salva depois do snapshot também está preservada byte a byte em `respostas-salvas/CALIBRACAO-DECK-100-PERGUNTAS.md`, com seu próprio `respostas-salvas/manifest.json`. O questionário ativo mantém respostas e acrescenta os três esclarecimentos posteriores; Q093 permanece vazia.

Além do snapshot inicial, `rotas-legadas/manifest.json` preserva 15 entradas/guias anteriores byte a byte. `flashcards/README.md` e entradas especializadas Claude foram redirecionadas; guias e exemplos de julho/agosto continuam em seus caminhos, explicitamente históricos, pois também documentam código/dados legados. Não são leitura obrigatória de uma nova aula.

A remoção só ocorreu após conferir cada arquivo contra seus bytes no ZIP. Testes verificam os hashes dos dois manifestos e o encaminhamento da documentação. Esses testes provam integridade/contexto, **não qualidade científica ou pedagógica do deck**. Não houve escrita Anki/Drive nesta consolidação; código de produção e artefatos privados de decks não foram limpos.

### Destino dos documentos retirados

O caminho da primeira coluna existe **dentro do ZIP**, com a versão integral anterior. Links de relatórios antigos que mencionam esses caminhos são referências históricas: consultar o ZIP, sem restaurar outro conjunto de regras ativas.

| Caminho original preservado | Onde consultar hoje |
|---|---|
| `flashcards/projeto/AJUSTES-ANKI-2026-09-28.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-ANTIBIOTICOS.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-FISIOLOGIA-BACTERIANA.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-GENETICA-BACTERIANA.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-INFLAMACAO-V2.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-INSUFICIENCIA-METABOLICA.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-INTESTINOS.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-SISTEMA-COMPLEMENTO.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/APRENDIZADOS-VASCULARIZACAO-VISCERAS.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/ARQUITETURA.md` | EXECUCAO-DECK-AULA + limites técnicos no MEMORY |
| `flashcards/projeto/AUDITORIA-2026-09-25.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/BANDEIRAS-E-PROGRESSAO.md` | MEMORY (preferências) + EXECUCAO-DECK-AULA (procedimento) |
| `flashcards/projeto/CALIBRACAO-2026-09-25.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/CALIBRACAO-DECK-AULA-V3.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/CALIBRACAO-ESCALA-V4.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/CALIBRACAO-INFLAMACAO.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/CONTABILIDADE-INFLAMACAO-V2.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/CONTRATO-DE-QUALIDADE.md` | MEMORY (preferências) + EXECUCAO-DECK-AULA (procedimento) |
| `flashcards/projeto/ESTILO-ANKING.md` | MEMORY (preferências) + EXECUCAO-DECK-AULA (procedimento) |
| `flashcards/projeto/FILA-UC03-P2-UC08-P1.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/HANDOFF-CLAUDE.md` | CLAUDE/AGENTS → README → MEMORY; estado em RECONSTRUCAO-UC08 |
| `flashcards/projeto/IMPLEMENTACAO.md` | EXECUCAO-DECK-AULA + limites técnicos no MEMORY |
| `flashcards/projeto/OPERACAO-CODEX-CLAUDE.md` | EXECUCAO-DECK-AULA + limites técnicos no MEMORY |
| `flashcards/projeto/PUBLICACAO-POR-UC.md` | EXECUCAO-DECK-AULA + limites técnicos no MEMORY |
| `flashcards/projeto/RELATORIO-CONSOLIDACAO-2026-09-25.md` | MEMORY + FEEDBACKS (aprendizados); detalhes/estado antigos no ZIP |
| `flashcards/projeto/TRADUCAO-DOS-CARDS.md` | MEMORY (preferências) + EXECUCAO-DECK-AULA (procedimento) |
| `HANDOFF-CLAUDE.md` | CLAUDE/AGENTS → README → MEMORY; estado em RECONSTRUCAO-UC08 |

## Preservação de 25/09/2026

[Manifesto anterior](../../backups/contexto-2026-09-25/manifest.json): 17 arquivos originais preservados com SHA-256, sem alteração nesta consolidação. O teste correspondente continua verificando cada byte. MEMORY/ROLES/CLAUDE integrais desse backup conservam backlog de outros projetos, instruções editoriais extensas, papéis aposentados e contexto anterior; consultar a seção específica antes de retomar um tema. Ausência na entrada curta não significa tarefa resolvida.

E1 continua em `didatica/E1.md`, com EXEMPLARES/ANTI-EXEMPLARES/ajustes didáticos preservados. Cadernista segue ROLES/banco; E2/E3/RemNote permanecem históricos. Arquivos de fontes, scripts de corridas e recibos privados não foram excluídos para reduzir a documentação.

## Como interpretar o passado

Pedido posterior de Davi prevalece. As respostas de 29/09 mudam idioma para inglês nas próximas entregas, fazem melhorias prospectivas, flexibilizam revisão por amostra, condicionam instalação às fontes importantes, registram suspensão pós-prova desejada e deixam papéis/ritmo pelo pedido. Q024/Q074/Q100 têm esclarecimentos no questionário e FEEDBACKS. Não reativar tradução, quotas, monitor ou gates antigos porque estavam em um contrato/handoff arquivado.

Backup conserva links relativos como eram: interpretar pelo caminho original. Exemplos UC03 ensinam forma/recorte, não quotas de cards/verdes nem aprovação automática de versões posteriores. Registros técnicos podem estar desatualizados; confirmar estado vivo na execução. Preferências portáveis estão no MEMORY; snapshots/recibos privados não são necessários para lembrar o que Davi quer, mas podem ser necessários para verificar uma aula específica.
