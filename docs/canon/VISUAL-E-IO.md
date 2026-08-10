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

## Construção da máscara

Em prancha rotulada, a máscara cobre o **nome da estrutura e todo texto que a define ou a
localiza** — inclusive as legendas entre parênteses. "Espaço entre as colunas", "porção
superior das colunas" e "6-10 cm, tecido linfoide" não citam o nome, mas entregam a
identidade: deixá-las à vista troca reconhecimento visual por leitura de definição e ainda
repete o que um cloze já cobra. Só fica visível o que não nomeia nem define — crédito da
fonte, título de orientação da prancha, qualificador neutro.

Antes de aprovar, varrer a figura atrás de **rótulo rasterizado**: atlas costumam trazer
nomes impressos dentro da própria imagem, sem texto no PDF. Rótulo rasterizado que repete um
nome já mascarado precisa virar máscara também, ou ser apagado do recorte junto com a
figura secundária que o exibe. O preview de pergunta é onde isso se confere.

O note type de IO precisa mostrar a **imagem mascarada na frente**. Note type de revelação
incremental não serve a `hide_all_guess_all`, em que o mapa inteiro é uma recuperação só.

## Gate

Todo visual declara necessidade, papel, tarefa, modo, fonte, crédito, hash,
preview e vazamento. IO declara rótulos, coordenadas, comportamento e se cada
máscara cobre o rótulo-resposta. São obrigatórios preview de pergunta e de
resposta, ambos revisados. Bloquear crop ruim, baixa resolução, resposta visível,
máscara sobre a pista anatômica/morfológica, rótulo duplicado exposto, imagem
genérica ou preview ausente.
