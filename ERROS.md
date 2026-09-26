# Armadilhas atuais — índice técnico
Feedbacks e regressões: `flashcards/projeto/FEEDBACKS.md`. Conteúdo integral anterior preservado em `backups/contexto-2026-09-25/ERROS.md`. E2/E3/RemNote estão apenas no histórico.

## E1/PDF
- Sem slide não significa sem figura; não ignorar necessidade de representação espacial/mecanística.
- Evitar truncamento, Unicode corrompido, YAML sem acentos e sintaxe Markdown vazando para Typst. Editar com apply_patch.
- Não duplicar etapa-header/set-etapa dentro de etapa1/resumindo: causa páginas vazias.
- Conferir sigla/termo-nota na primeira aparição, referências e caminhos /figuras; preservar definição sem duplicar footnote.
- E1: checar forma/volume com verificadores, revisão visual e contagem real. Não medir E1 pela primeira ocorrência de “em uma frase”.
- Teto de referência e exceção declarada em didatica/E1.md; cortar verbosidade, nunca mecanismo para caber.
- Fonte correta embarcada; font-path e raiz explícitos na compilação. Conferir tamanho da capa, numeração, sumário, conclusão e Resumindo sem cortes.
- Formatos/listas do Resumindo seguem tupla dupla; figuras e suas legendas precisam função distinta do corpo.
- Builder legado inclui questões e pode usar pasta errada: usar modo somente-E1 e saída explícita isolada. Não executar limpeza destrutiva do workspace compartilhado.

## Anki/curadoria
- Descoberta de acervos não pode depender de caixa do nome AnKing nem de pasta-pai fixa.
- cardsInfo pode omitir flags: ler por findCards flag:N; tag HY não é recomendação de retenção.
- Uma nota pode gerar vários irmãos; tag não é associação por card. Deletar nota pode excluir irmãos úteis.
- Identidade/texto sem duplicação não exclui redundância semântica.
- Verificar origem pelo corpus real, não só tag copiada.
- Lock exclusivo, backup antes de exclusão, diário e readback; após timeout, procurar identidade.
- Pacote sem flags deve ser produzido isoladamente; nunca zerar coleção viva para exportar.
- Contagem, keyword gate, mídia presente e sync aceito não provam qualidade, renderização ou chegada aos dispositivos.

Quando retomar ferramenta com falha antiga específica, consultar seu item técnico no arquivo preservado; este índice não substitui documentação do template/scripts.
