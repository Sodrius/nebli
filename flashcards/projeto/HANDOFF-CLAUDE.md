# Próxima sessão no Claude — qualidade dentro do recorte

24/09/2026. Preferência declarada: Opus 5.5, esforço alto, selecionado pelo usuário na interface. Não trocar modelo nem contratar API automaticamente. Modelo forte não substitui ler fontes, conferir imagens e executar verificações; não prometer perfeição ou cobertura integral sem evidência.

## Pedido suficiente

```text
/deck-aula <link do slide/pasta no Drive>
```

Abrir Claude Code na raiz NEBLI. Ler a ordem do README e executar a aula indicada, sem escolher outra automaticamente. Slash command é instrução de orquestração, não programa autônomo nem garantia de resultado.

## Sucesso para Davi

- Receber material confiável para estudar, sem ter de procurar cards faltantes e organizar arquivos.
- Aula delimita o assunto; bibliografia/vídeos/AnKing aprofundam o mesmo assunto para faculdade, Step pertinente e compreensão durável. Exemplo não vira objetivo; não antecipar outra aula.
- Bons AnKing encontrados do assunto ficam disponíveis, tolerando alguma repetição pré-prova. Outros acervos vêm antes de autoria rara, curta, AnKing-like e com imagem útil. Nenhuma cota justifica cards fracos.
- Teoria e identificação visual auditadas separadamente. Verso conta para aprender, mas não comprova recuperação ativa/reconhecimento.
- Manter é padrão. Rosa desde a criação para candidatos pós-prova; Davi decide suspender. Verde só HY literal, sem comentários meta nos cards.
- E1 explicativa + guia/vídeos/bibliografia + Anki verificado + APKG único da UC inteira comprimido/sem flags, atualizado no mesmo arquivo privado. Flags permanecem na coleção viva.
- Respeitar limpeza manual, identidade e histórico. Não ressuscitar removidos nem duplicar para simular compartilhamento.

## Antes de produzir

1. Ler README, CALIBRACAO-ESCALA-V4, CONTRATO-DE-QUALIDADE, OPERACAO-CODEX-CLAUDE, EXECUCAO-DECK-AULA, ACERVOS-REFERENCIA e PUBLICACAO-POR-UC.
2. Rodar `python -m unittest discover -s nebli/tests -v` e diagnóstico vivo `python -m nebli.preflight --catalog --output <pasta-da-execucao>/catalogo.json`.
3. Confirmar perfil, fontes e destino privado no Drive. O GitHub contém instruções/código, não AnKing, mídia, slides, credenciais ou coleção pessoal. Clone novo sozinho não fornece esses acessos.
4. Criar `config/publicacoes-uc.json` do exemplo somente se ausente; nunca sobrescrever IDs locais. Descobrir/testar as ferramentas de upload do executor atual.
5. Exemplos históricos calibram julgamento, não contagens atuais. Se uma evidência local não está no clone, não alegar que foi conferida.

## Fechamento

Revisar escopo, cobertura, excesso, todos os autorais e imagens adaptadas. Salvar REVISAO-DE-QUALIDADE conforme contrato. Rodar empacotador e confirmar upload por metadados. Relatar aula/UC, origens, autoria, cores locais, zero flags no arquivo, fontes ausentes e links. Não transferir ao aluno a auditoria que cabe ao executor.

Uma amostra da primeira aula precisa ser aprovada pelo usuário. Compartilhados entre UCs, importação Mac/Android e uma aula inteira pelo Claude ainda não têm validação ponta a ponta registrada. Se algo falhar, informar estado parcial e causa, sem chamar concluído.

## Hook antigo — não reativar automaticamente

`.claude/settings.json` contém um Stop hook apontando para `C:\AI use\nebli`, caminho inexistente na vistoria. O script faz git add/commit/push de tudo. Não corrigir o caminho e reativar sem autorização específica: o push manual solicitado nesta sessão não autoriza publicação automática futura. O hook pode gerar erro ao encerrar o turno; não faz parte da execução de decks e não deve ser usado para publicar o pipeline. O pedido para desativá-lo ainda não foi respondido.
