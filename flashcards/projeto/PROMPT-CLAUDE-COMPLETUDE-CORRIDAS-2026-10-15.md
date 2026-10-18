# Prompt para o Claude — recuperar a completude das corridas de 13–15/10

Trabalhe no repo `~/NEBLI`, com o Anki aberto, seguindo `AGENTS.md`, `MEMORY.md`, `flashcards/projeto/EXECUCAO-DECK-AULA.md`, `flashcards/projeto/ANTI-EXEMPLARES-CARDS.md` e `flashcards/projeto/PLANO-CARDS-TABS.md`.

O nível dos decks recentes caiu. O principal problema não é a quantidade final de cards: faltou planejar **tudo o que cada aula precisava cobrir** antes de selecionar notas, e algumas informações ficaram sem card. Leia primeiro `arquivos-trabalho/auditoria-cobertura-corridas-13-15-10-2026/AUDITORIA.md`. Ele contém lacunas concretas e pontos que precisam de confirmação nas fontes e no Anki vivo.

## Regra central

Não faça uma correção pontual guiada apenas pela lista da auditoria. Para cada corrida, reconstrua primeiro a cobertura completa da aula, na ordem das fontes:

1. Releia todas as lâminas e os materiais já declarados em `fontes-decl.json`, inclusive transcrição, exercícios, provas e a seção pertinente do livro.
2. Refaça `inventario.py`/`cobertura.json` em granularidade de **informação ou relação**, não de lâmina. Itens como “Tabela”, “Fluxo”, “Contexto”, “Resumo” ou “Exemplo” são insuficientes: enumere o que aquela tabela/fluxo ensina.
3. Para cada informação, decida explicitamente: **card**, **Tab/Extra** ou **exclusão com motivo específico**. Toda informação que o aluno precisa lembrar, explicar, distinguir, organizar ou reconhecer exige card. Tab não substitui recuperação.
4. Só então confronte o inventário com os cards vivos. Preserve notas, histórico, comentários, bandeiras e compartilhados. Reutilize `sh()` antes de criar autoral.
5. Acrescente os cards ausentes e os organizadores de mapa mental. Não infle: fatos já recuperáveis continuam onde estão; exemplos puramente ilustrativos podem ficar no Tab/Extra; detalhe de outra aula continua fora com destino nomeado.
6. Autorais seguem o AnKing: atômicos, nucleares, não ambíguos, cloze exatamente no que se decora; organizadores em tópicos, uma linha por item. O percurso deve avançar princípio → mecanismo/distinção → organização → aplicação, na ordem dos slides.

## Escopo obrigatório

Audite estas 15 corridas, na ordem, usando a seção “Aula por aula” da auditoria como mínimo, não como teto:

- `deck-aula-uc03-pt09-lesao-celular-2026-10-13`
- `deck-aula-uc03-pt11-acumulos-adaptacao-2026-10-14`
- `deck-aula-uc03-pt13-envelhecimento-2026-10-14`
- `deck-aula-uc03-pt14-declaracao-obito-2026-10-14`
- `deck-aula-uc03-bq10-acao-hormonal-2026-10-14`
- `deck-aula-uc03-rd12-rm-2026-10-14`
- `deck-aula-uc03-bq16-regulacao-hormonal-2026-10-14`
- `deck-aula-uc03-gr15-grand-round-1-2026-10-14`
- `deck-aula-uc03-bm18-recombinacao-2026-10-14`
- `deck-aula-uc03-im08-reconhecimento-inato-2026-10-14`
- `deck-aula-uc03-im17-reconhecimento-adaptativo-2026-10-14`
- `deck-aula-uc03-im20-mhc-2026-10-14`
- `deck-aula-uc03-im22-mecanismos-efetores-2026-10-15`
- `deck-aula-uc03-mb40-pratica3-2026-10-15`
- `deck-aula-uc21-dic05-insuf-metabolica-2026-10-15`

Prioridade inicial pelas lacunas já demonstradas: 10 Ação hormonal → 14 Declaração de óbito → 08 Reconhecimento inato → 20 MHC → 22 Mecanismos efetores → 40 Prática 3 → 18 Recombinação → 15 GR1 → 11 Acúmulos. Depois confirme 13 e 16. Nas aulas 09, 12, 17 e UC21, não aumente o deck sem lacuna nova demonstrada; faça as correções de conteúdo descritas na auditoria.

## Convivência e segurança

Antes de cada corrida, releia `ESTADO-ATUAL.md`, reivindique-a e não toque em aula que outro executor estiver alterando. Davi pode estar estudando: nunca toque a nota em tela nem irmãs; escrita só por `nebli.decks.escrita()`, com backup e readback. Não apague nota sem autorização explícita. Não gere E1.

## Validação por aula

- Conferir inventário × plano × cards vivos item por item.
- Ler `revisao-despejo.txt` inteiro na ordem viva e provar que nenhum bloco ficou sem recuperação.
- Rodar ordem, inventário, revisão e gates; gate aprovado não substitui julgamento.
- Só depois regenerar Tabs alterados e exigir faltando 0, desatualizada 0, revisar 0 e formato incompleto 0.
- Atualizar `REVISAO-DE-QUALIDADE.md` com lacunas encontradas, cards adicionados/associados/reescritos, itens que continuaram fora e motivo.

No fim, repita a análise da UC03 P1 e da P2 para conferir progressão entre aulas, atualize `ESTADO-ATUAL.md`, republique o pacote da UC03 em pasta nova e sincronize apenas se Davi estiver ocioso. Relate por aula o que faltava e como ficou recuperável. Não diga apenas “gates 100%”.
