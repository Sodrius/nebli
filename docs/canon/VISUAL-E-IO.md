# Visual e Image Occlusion

## Fontes

1. imagem do card AnKing selecionado;
2. card irmão pertinente do AnKing;
3. deck externo privado;
4. fonte médica institucional aprovada;
5. slide, somente em último caso.

Wikimedia e OpenStax não são fontes padrão. Imagem de mesmo tema não basta: o
ativo precisa ensinar o alvo do card.

## Decisão por objetivo

- reconhecer/localizar: Image Occlusion ou prompt visual na frente;
- mecanismo/fluxo/comparação explicativa: imagem no Extra;
- estritamente verbal: sem imagem por decisão explícita.

IO só entra quando existe uma resposta espacial mascarável e sua montagem pode
ser comprovada no preview. Em diagrama rotulado, a máscara cobre o **rótulo da
resposta**, nunca a estrutura que o aluno precisa reconhecer. Em imagem não
rotulada, adicionar seta/contorno e rótulo e ocultar esse rótulo; em histologia,
preferir prompt com marcador quando mascarar o tecido destruiria a pista.

Mapas com várias partes coerentes — por exemplo, identificar as partes de um
órgão no mesmo esquema — usam `hide_all_guess_all`: todas as respostas ficam
ocultas e o conjunto inteiro é recuperado. Isso é a única exceção multi-alvo e
precisa declarar `coherent_visual_map` e justificar por que o mapa é uma unidade.

Anatomia macro combina, quando possível, esquema e peça real. Histologia combina
identificação visual e card conceitual quando ambos são objetivos da aula.

## Gate

Todo visual declara necessidade, papel, tarefa, modo, fonte, crédito, hash,
preview e vazamento. IO declara rótulos, coordenadas, comportamento e se cada
máscara cobre o rótulo-resposta. São obrigatórios preview de pergunta e de
resposta, ambos revisados. Bloquear crop ruim, baixa resolução, resposta visível,
máscara sobre a pista anatômica/morfológica, rótulo duplicado exposto, imagem
genérica ou preview ausente.
