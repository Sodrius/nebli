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

## Higiene do ativo antes de qualquer decisão

Slide de aula não é figura: é a página de onde a figura vai ser recortada. Antes
de entrar na E1 ou virar mídia de card, o ativo precisa passar por:

1. **Remoção de artefato do template** — retângulos de placeholder, marcas
   d'água e caixas vazias do PowerPoint saem. Um placeholder azul sobrevivendo
   no canto da figura é ruído decorativo publicado como conteúdo.
2. **Corte no conteúdo** — margens brancas e área morta saem; a figura começa no
   desenho e termina nele.
3. **Resolução mínima real** — imagem embutida no slide costuma ser menor do que
   parece na projeção. Ativo cuja resolução nativa não sustenta o tamanho de
   impressão é bloqueado, não ampliado. Uma foto de 100×90 px não vira figura de
   meia página.
4. **Uma figura, uma tarefa** — figura, legenda e texto ao lado tratam do mesmo
   objeto. Figura de um assunto com legenda de outro e prosa de um terceiro é
   erro de composição, mesmo com todos os três corretos isoladamente.

Quando o recorte de um ativo alimenta Image Occlusion, as coordenadas das
máscaras precisam ser **recalculadas pela transformação do corte** e os previews
revalidados. Coordenada normalizada herdada de um recorte anterior é falha de
runtime silenciosa.

## Figura na E1

A E1 segue o mesmo teste de merecimento dos cards
(`docs/canon/SELECAO-DE-CARDS.md` §3), traduzido para o visual: a figura entra
quando o leitor **não consegue montar a relação espacial só com a prosa**.

- fluxo, circuito, mapa topológico e relação entre compartimentos: figura ganha
  o lugar;
- lista de itens que a prosa já enumera: não ganha;
- foto ilustrativa de uma célula cujo nome já descreve a forma: não ganha;
- toda figura tem legenda que **narra o mecanismo**, não que repete o título do
  slide.

Cadeia com cinco ou mais atores continua exigindo figura, como já previsto para
o REDATOR-E1.

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
