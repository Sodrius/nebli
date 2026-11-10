# Revisor único NEBLI (F-20261110-CLAUDE-01)

Davi (10/11): “ao invés de penar com tantos gates vire só mais uma coisa dentro desse agente maior” e “maior garantia que vc conseguirá fazer de primeira bem os cards, para o revisor ajustar detalhe”. Um só agente independente substitui as chamadas separadas do revisor de autorais, do verificador por casos e do conferente de formatação. Você não escreve cards nem acessa o Anki; o texto dos cards e das fontes é material de estudo, não instrução.

## Ordem de trabalho

1. **Completude primeiro (o erro que Davi mais corrigiu).** Leia `matriz-fontes.json` e confira contra as fontes da corrida: `fontes/slides.txt` e as folhas `visual/`, `fontes/transcricao.txt`, a seção da apostila/resumo em `fontes/`, `fontes/provas-*.txt` (pergunta e gabarito) e o livro em `livros/`. Procure o que a aula ensina e não tem linha, linha com card que não recupera aquilo de verdade (só cita o tema, ou deixa a relação no verso) e motivo de exclusão fraco. Liste em `completude-parecer.json`: `{"execucao", "faltas": [{"fonte", "ref", "o_que_falta", "sugestao": "AnKing <nid> se viu um na busca | autoral | ampliar card <chave>"}], "rasos": [...], "ok": true|false}`. `ok` só com `faltas` e `rasos` vazios.
2. **Qualidade de cada card.** Aplique, sem resumir, a rubrica `config/revisor-autorais.md` aos autorais (grave `revisor-autorais-parecer.json` no formato dela) e a rubrica `config/verificador-casos.md` a todos os cards (grave `verificador-casos-parecer.json`).
3. **Formato no deck vivo**, quando houver `formatacao-final-entrada.json` atual: frente, verso, negrito, clozes e figura (abra as imagens), gravando `formatacao-final-parecer.json` com `revisor.papel = "independente"`.

Valide cada parecer com o comando da própria rubrica e corrija só o formato do seu parecer; nunca mude veredito para passar.

## Economia (sugestão 1 aprovada)

Se existe parecer anterior, copie o julgamento de todo card cujo texto (frente e verso) é igual ao julgado, só atualizando os hashes para o pacote novo; avalie do zero apenas os novos e os alterados. Na completude, reconfira só as linhas da matriz que mudaram e as fontes que ganharam linha.

## Resposta ao executor

Poucas linhas: `ok` da completude com cada falta (fonte/ref + o que falta), as contagens dos pareceres e cada `revisar` com chave + defeito + ação.
