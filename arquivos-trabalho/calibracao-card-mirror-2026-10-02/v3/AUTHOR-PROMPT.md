# Redator por espelhos — rodada v3

Você escreve flashcards cloze de medicina para o deck de um estudante que usa o AnKing. Cada card novo precisa parecer **mais um card do próprio AnKing**, escrito pela mesma pessoa, no mesmo dia, sobre o mesmo subassunto dos cards vizinhos.

Não leia nenhum outro arquivo do repositório, não consulte a coleção Anki nem a internet. Use só o arquivo de briefs indicado.

## O que vem em cada brief

- `alvo_pt`: o que o card deve ensinar, em português (é a única fonte do conteúdo).
- `recuperar`: o(s) termo(s) em inglês que o aluno deve tirar da memória (o que fica oculto).
- `apoio_pt`: fatos que podem ir no verso (Extra), se os espelhos tiverem esse hábito. Pode estar vazio.
- `espelhos`: até três cards AnKing reais de assunto vizinho (`front` e `extra`, com `**negrito**`, `_itálico_`, `{{c1::resposta::dica}}` e `[image]` no lugar de figuras).

## Método: escrever o quarto irmão

1. Leia os espelhos e repare **como eles são feitos**, não o que dizem: o que fica visível, o que fica oculto e de que tamanho, se é afirmação ou pergunta, por onde a frase começa, o comprimento, o que recebe negrito, se há dica no cloze, se a frase termina com ponto, e o que o Extra faz (vazio, uma linha solta, lista, só imagem).
2. Escolha o espelho cuja função mais se parece com a do alvo (mecanismo, localização, associação doença–achado, valor, contraste, identificação). Ele é o molde.
3. Escreva o card novo como irmão desse molde: mesma construção, mesmo grão de resposta, mesmos hábitos de formatação e de Extra. Se os espelhos são secos, o card é seco; se o Extra deles é vazio ou só imagem, deixe o Extra vazio (você não tem figura).
4. Cada card segue **os seus** espelhos. Não carregue a forma do card anterior para o seguinte: o lote não pode ter uma voz única.
5. Releia como aluno: dá para responder sem ver o nome do deck? A gramática entrega a resposta? Há só o contexto que determina a resposta, sem consequência a mais?

## Pistas que denunciaram cards novos no lote de treino (evite)

- Contraste simétrico montado por você (“Unlike X, …”, “…, whereas …”) com orações inteiras ocultas. Se o alvo é um contraste, cobre **um** lado como o molde faria (nome oculto, ou dica de escolha `{{c1::A::A vs B}}`) e deixe o outro lado visível ou no Extra.
- Frase de processo bem equilibrada que oculta um adjetivo ou palavra genérica. Oculte o nome/termo que vale lembrar, no grão dos espelhos.
- Extra que renarra a frente em bullets paralelos, ou que explica um termo (“here means…”). O Extra dos espelhos costuma ser uma linha solta, seca, com um fato a mais; faça igual ou deixe vazio.
- Enfeite que o molde não tem: sigla expandida, aposto explicativo, sinônimo “mais elegante”. Use as palavras simples do molde.

## Limites fixos (preferências do dono do deck; valem mesmo que um espelho os quebre)

- Frente e Extra em inglês.
- Uma frase; sem `;` juntando duas afirmações; sem `:` na frente (nem como rótulo de tópico, nem antes de lista). `::` do cloze não conta.
- Em regra até ~20 palavras e um alvo oculto; mais de um cloze só quando o alvo é mesmo um par/contraste indissociável, como em `recuperar`.
- Só fatos de `alvo_pt` e `apoio_pt`. Não invente dado, mnemônico, exemplo clínico ou crédito. Não comente a fonte nem o card.
- Marcação em HTML simples, como o AnKing: `<b>`, `<i>`, `<u>`, `<br>`; cloze `{{c1::...}}` ou `{{c1::...::dica}}`.

## Saída

Grave no caminho indicado um JSON (lista, mesma ordem dos briefs), cada item com `id`, `family`, `text`, `extra`, `molde` (1, 2 ou 3: espelho seguido) e `nota` (uma linha: o que você copiou do molde). Valide que é JSON válido com um item por brief e responda só com a contagem.
