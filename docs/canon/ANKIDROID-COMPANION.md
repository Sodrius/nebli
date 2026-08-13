# AnkiDroid Companion — arquitetura canônica

Status: backend canônico do Deck-Aula. O fluxo normal é integralmente AnkiDroid.
Desktop/APKG só pode ser usado como contingência se for solicitado explicitamente.

## Objetivo

O AnkiDroid no tablet é simultaneamente:

1. fonte local do AnKing;
2. destino do Deck-Aula;
3. dono da mídia já existente na coleção;
4. destino direto de cards autorais e Image Occlusion.

Fluxo esperado:

`aula → E1/contrato → plano final de cards → manifesto v3 → Companion → AnkiDroid`

O fluxo normal não exige Drive, Colab, AnkiConnect, `.apkg` ou importação manual
de deck.

## Manifesto canônico v3

O pipeline produz um único arquivo:

`flashcards/manifests/<slug>.ankidroid.json`

Schema: `nebli-ankidroid-deck-v3`.

Ele contém:

- `lesson_slug`;
- `deck_identity` com UC, prova, componente e nome curto;
- `target_deck` canônico;
- `expected_card_count` real;
- resumo do `release_gate=nebli-e1-deck-release-v1`, provando que a E1 revisada,
  o core e a matriz de cobertura foram aprovados antes do empacotamento;
- plano de **todos os cards**;
- consultas de contexto, respostas esperadas, restrições e fallback validado dos
  cards preferencialmente AnKing;
- cards autorais completos;
- IO completos, incluindo máscaras e QA;
- mídia nova necessária embutida por hash/base64;
- contrato de ranking e segurança.

A mídia pesada já existente no AnKing não é duplicada no manifesto: a cópia
mantém as referências originais da coleção local.

O runtime também impõe o contrato linguístico e cognitivo: frente e Extra
autorais, prompt e respostas de IO em português, cópia local somente quando
pergunta e resposta renderizadas estão em português e metadados de revisão
anti-indução completos. O valor de `front_language` sozinho não basta; prosa
inglesa marcada como PT-BR é bloqueada. Em IO derivado de imagem rotulada em
outro idioma, a resposta mantém o rótulo original coberto e coloca no mesmo
local um rótulo textual revisado em português.

## Nome e localização

O nome é derivado exclusivamente de `deck_identity`:

`NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`

Cards `optional` vão para:

`<Deck-Aula>::Optional`

No fim de uma instalação bem-sucedida, o Companion seleciona o deck raiz e abre
o AnkiDroid.

Gerador e Companion rejeitam segmentos ausentes, UC/prova inválidas e qualquer
`target_deck` divergente dos quatro metadados.

## AnKing local

Para cada card com `source=anking`:

1. pesquisar `search_queries` independentes na coleção local;
   a busca AnKing é limitada por padrão a `deck:\"AnKing Step Deck\"` e lê
   primeiro apenas IDs, hidratando no máximo o pool de candidatos necessário;
2. tratar esse filtro como dica; se o nome local for diferente, repetir a busca
   sem escopo e exigir marcador AnKing;
3. excluir cópias NEBLI do pool;
4. aplicar `must_contain` e `must_not_contain`;
5. ranquear a nota pelo contexto/frase e margem;
6. inferir o sibling/ordinal por `expected_answers`, separadamente do contexto;
7. quando o conceito é visual, exigir que o candidato realmente tenha visual na
   pergunta;
8. se o resultado for confiável e a pergunta renderizada estiver em português,
   copiar literalmente a nota; se estiver em inglês, usar o fallback autoral em
   português e preservar a fonte apenas como referência de conteúdo/mídia;
9. se for ambíguo, ausente ou visualmente insuficiente, usar o `fallback`
   validado do próprio manifesto — nunca escolher à força.

No v9, todo `source=anking` já representa card curado e usa
`anking_required=true`. Falhar em resolvê-lo bloqueia o lote, sem fallback
silencioso. O recibo registra
consultas tentadas, candidatos, motivo da decisão e fonte realmente instalada.

Parâmetros canônicos:

- `min_score = 0.82`;
- `min_margin = 0.06`;
- até 80 candidatos por card;
- `require_anking_marker = true`;
- ambiguidade = `use_validated_fallback`.

## Fidelidade e segurança da cópia

Cópia AnKing/deck externo:

- mesmo note type (`mid`);
- mesmos campos (`flds`) byte a byte;
- mesmo HTML, clozes e referências de mídia;
- tags originais preservadas, adicionando apenas proveniência NEBLI;
- scheduling/history novo;
- somente sibling selecionado ativo; irmãos não selecionados suspensos;
- fonte relida depois da cópia e comprovadamente intacta.

WRITE só é permitido em `NEBLI::*`. UPDATE/DELETE de fonte são proibidos.

## Autorais diretos

O Companion instala autorais sem desktop/APKG.

Preferência: reutilizar um note type cloze já existente na coleção. Se a coleção
não possuir cloze compatível, usar `NEBLI Basic v1` com renderização equivalente
de uma lacuna.

Antes da instalação, o card precisa cumprir `docs/canon/CARD-QUALITY.md`, incluindo:

- inglês na frente, Extra em português;
- uma recuperação;
- exatamente uma ocorrência de `c1`;
- 1 palavra no cloze por padrão, 2 quando necessário, 3 excepcionalmente com
  justificativa, 4+ bloqueado;
- atomicidade e relevância explícitas.

## Image Occlusion direto

IO não depende de note type nativo de Image Occlusion. O Companion usa
`NEBLI Image Occlusion v1`, mídia da coleção e overlay HTML determinístico.

Hard gates:

- `hide_two_guess_two`, com uma ou duas máscaras e alvo de duas por card;
- máscara cobre o rótulo-resposta, não a estrutura visual;
- duas máscaras exigem conjunto coerente e `pair_rationale`;
- geometria dentro da imagem;
- fonte real;
- previews de pergunta e resposta validados;
- sem vazamento de resposta;
- runtime deve renderizar máscara + imagem na pergunta e imagem/solução na
  resposta.

Cards autorais podem declarar `anking_images`: o Companion resolve o card
AnKing, seleciona a referência local indicada por `media_index` e a reutiliza no
Extra. Imagens de slide/externas só são aceitas com evidência por arquivo de
busca visual AnKing, rejeição concreta, crédito, propósito cognitivo e revisão
didática. O gate compara as referências esperadas às renderizadas, inclusive em
instalações idempotentes.

## Mídia nova

Mídia autoral/IO nova é empacotada no manifesto com:

- key;
- filename;
- SHA-256;
- base64;
- crédito/fonte quando aplicável.

No tablet, o Companion:

1. verifica SHA-256;
2. escreve temporariamente no cache privado;
3. expõe um `content://` temporário por FileProvider;
4. entrega a mídia ao ContentProvider do AnkiDroid;
5. grava no card apenas o nome final retornado pelo AnkiDroid.

## Idempotência e atualização

Cada card tem identidade estável por `lesson_slug + card_key` e hash de conteúdo.

- mesmo hash → reutilizar, sem duplicar;
- hash novo de um card NEBLI → substituir apenas a cópia NEBLI;
- nunca modificar/apagar fonte AnKing.

## Rollback

A instalação é um lote lógico. Se um card novo falhar no runtime:

- o deck não é declarado pronto;
- todas as notas NEBLI criadas naquela tentativa são removidas;
- nenhuma nota-fonte é tocada;
- o recibo registra a falha.

Mídia já copiada pode permanecer deduplicada na coleção, mas não existe lote
parcial de notas novas aprovado.

## Gate card a card

Antes do manifesto, o pipeline valida **todos os cards reais**. Sem amostragem.

Depois da instalação, o Companion também valida o runtime aplicável.

Obrigatório:

- `expected_card_count == validated_card_count`;
- `passed_card_count == expected_card_count`;
- `installed_card_count == expected_card_count`;
- zero falhas;
- card keys únicas;
- fonte AnKing intacta;
- mídia/IO funcionais.

O CI mantém uma regressão de 40 cards como tamanho realista, mas 40 não é cota.
Uma aula real valida o próprio total.

## Experiência final

Depois do setup inicial do Companion:

1. o pipeline gera `<slug>.ankidroid.json`;
2. o usuário abre esse arquivo no tablet;
3. o Companion resolve AnKing, usa fallbacks quando necessário, instala
   autorais/IO, valida a contagem e seleciona o deck;
4. o AnkiDroid abre no final.

Nenhuma seleção card a card ou montagem manual é parte do fluxo normal.
