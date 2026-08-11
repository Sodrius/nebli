# Visual e Image Occlusion

## Fontes

1. imagem do card AnKing selecionado;
2. card irmão pertinente do AnKing;
3. deck externo privado;
4. fonte médica institucional aprovada;
5. slide, somente em último caso.

Wikimedia e OpenStax não são fontes padrão. Imagem de mesmo tema não basta: o
ativo precisa ensinar o alvo do card.

Essa ordem também vale para cards autorais: primeiro procurar uma imagem útil
nos cards AnKing locais e reutilizar a referência de mídia sem duplicar o
arquivo. Slide ou fonte externa só entram com busca visual AnKing concluída,
motivo concreto de rejeição e crédito. Toda imagem declara a operação cognitiva
que sustenta e `didactic_value_reviewed=true`; imagem decorativa é bloqueada.

## Decisão por objetivo

- reconhecer/localizar: Image Occlusion ou prompt visual na frente;
- mecanismo/fluxo/comparação explicativa: imagem no Extra;
- estritamente verbal: sem imagem por decisão explícita.

IO só entra quando existe uma resposta espacial mascarável e sua montagem pode
ser comprovada no preview. Em diagrama rotulado, a máscara cobre o **rótulo da
resposta**, nunca a estrutura que o aluno precisa reconhecer. Em imagem não
rotulada, adicionar seta/contorno e rótulo e ocultar esse rótulo; em histologia,
preferir prompt com marcador quando mascarar o tecido destruiria a pista.

IO usa `hide_two_guess_two`: em geral duas respostas relacionadas ficam ocultas
e são recuperadas juntas, reduzindo o número de cards sem criar listas longas.
Um alvo isolado é permitido; mais de dois é bloqueado. O par precisa formar uma
unidade cognitiva coerente e declarar `pair_rationale`.

Anatomia macro combina, quando possível, esquema e peça real. Histologia combina
identificação visual e card conceitual quando ambos são objetivos da aula.

## Gate

Todo visual declara necessidade, papel, tarefa, modo, fonte, crédito, hash,
valor didático, preview e vazamento. IO declara rótulos, coordenadas, comportamento e se cada
máscara cobre o rótulo-resposta. São obrigatórios preview de pergunta e de
resposta, ambos revisados. Bloquear crop ruim, baixa resolução, resposta visível,
máscara sobre a pista anatômica/morfológica, rótulo duplicado exposto, imagem
genérica ou preview ausente. O recibo de instalação compara as referências de
mídia esperadas com pergunta e resposta realmente renderizadas no AnkiDroid.
