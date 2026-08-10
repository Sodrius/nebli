# NEBLI — entrada canônica

O NEBLI transforma o material de uma aula em dois produtos: **E1 para aprender** e
**deck-aula Anki para reter**. O comando normal `/resumo` já executa esse fluxo.
E2, E3 e RemNote estão suspensos e não pertencem ao pipeline padrão.

## Leitura obrigatória

Leia, nesta ordem, antes de produzir qualquer aula:

1. `MEMORY.md` — estado e pendências atuais;
2. `ERROS.md` — bloqueios recorrentes ativos;
3. `docs/canon/PRODUTO-DECK-AULA.md`;
4. `docs/canon/COBERTURA-E-STEP1.md`;
5. `docs/canon/PIPELINE-E1-DECK.md`;
6. `docs/canon/CARDS.md`;
7. `docs/canon/EXEMPLOS-CARDS.md`;
8. `docs/canon/VISUAL-E-IO.md`;
9. `docs/canon/APKG.md`;
10. `docs/canon/ANKING-PRIVADO.md`;
11. `docs/canon/REVISAO.md`.

Os documentos em `docs/legacy/` são históricos. Não os carregue nem aplique, a
menos que Davi peça explicitamente uma recuperação histórica.

## Autoridade e execução

- A **sessão principal** lê fontes, define cobertura, escreve e corrige a E1,
  seleciona cards, admite aprofundamentos Step 1, escolhe imagens, gera IO,
  cria cards autorais, monta o APKG e aplica correções.
- Agentes são **somente revisores**. Eles não redigem partes do produto e não
  alteram arquivos silenciosamente.
- O slide e os objetivos da aula definem o escopo. AnKing e bibliografia Step 1
  aprofundam o mesmo tema. Todo conteúdo de card precisa estar explicado na E1.
- AnKing e decks externos são fontes privadas, somente leitura e nunca entram no
  GitHub. Cópias NEBLI recebem GUID novo e preservam conteúdo, mídia e crédito.

## Entrega

Ao fim de toda aula, mande **no chat** o PDF da E1 e o `.apkg` como arquivos anexados,
sempre — não basta dizer onde eles estão no repositório.

## Gates de fechamento

Uma aula não fecha se houver conceito nuclear sem card adequado, card sem âncora
literal na E1, aprofundamento que escapou do tema, necessidade visual obrigatória
não atendida, autoral sem rejeição documentada das fontes reais, mídia quebrada
ou APKG não auditado. Também bloqueiam: exceder o teto de cards congelado no
contrato, card com mais de uma recuperação independente, cloze acima de três
palavras e IO cuja máscara não cubra o rótulo-resposta. Relatórios declaratórios
não substituem a inspeção do arquivo `.apkg` entregue.

## Configuração ativa

`config/pipeline.json` é a configuração mecânica. O padrão atual é E1 + deck,
25 novos/dia, revisão sem teto prático, APKG offline e E2/E3/RemNote desligados.
