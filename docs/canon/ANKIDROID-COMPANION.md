# AnkiDroid Companion — arquitetura canônica

Status: backend preferido do pipeline. Desktop permanece como fallback para casos ainda não suportados nativamente.

## Objetivo

O AnkiDroid instalado no tablet passa a ser simultaneamente:

1. fonte local do AnKing;
2. destino do deck-aula;
3. dono da mídia já existente na coleção.

O fluxo normal não deve exigir Drive, Colab, `.apkg` nem importação manual para cards AnKing.

## Regra de segurança

- READ permitido em qualquer deck fonte, inclusive AnKing.
- WRITE permitido somente em decks cujo nome comece por `NEBLI::`.
- UPDATE/DELETE de notas fonte são proibidos.
- Uma instalação é idempotente por aula + note fonte + ordinal selecionado.
- Falha parcial não autoriza apagar ou alterar a fonte.
- Resultado de busca ambíguo fica `unresolved`; nunca é escolhido à força.

## Semântica da cópia

Para cards provenientes do AnKing/deck externo:

- preservar note type/model;
- preservar todos os campos sem reescrita;
- preservar HTML, clozes e referências de mídia;
- preservar tags de origem e acrescentar apenas tags de proveniência NEBLI;
- criar uma nota nova no deck-aula;
- não carregar scheduling/history da fonte;
- irmãos não selecionados devem nascer suspensos quando o manifesto selecionar apenas um ordinal;
- reler a origem após a cópia e comprovar que `mid/flds/tags` permaneceram intactos.

É proibido prefixar ou modificar `Text` em cópias AnKing. A fidelidade do conteúdo é literal.

## Manifesto v2

O `nebli-core` produz `flashcards/manifests/<slug>.ankidroid.json` no schema
`nebli-ankidroid-lesson-v2`. O manifesto carrega conceitos atômicos e aliases,
não IDs locais obrigatórios e não contém a mídia pesada do AnKing.

O Companion resolve cada conceito diretamente contra a coleção local do
AnkiDroid, aplica ranking conservador e copia somente candidatos confiáveis.

## Ranking

Parâmetros canônicos atuais:

- `min_score = 0.82`;
- `min_margin = 0.06` quando não há frase exata forte;
- no máximo 80 candidatos por conceito;
- preferência por marcadores AnKing;
- ambiguidade => `unresolved`.

Um match lexical parcial nunca deve ser tratado como lacuna comprovada nem como
seleção automática só por aparecer em primeiro lugar.

## Pipeline

1. Extrair conceitos da aula.
2. Gerar queries/aliases médicos em PT/EN quando úteis.
3. Enviar manifesto v2 ao Companion.
4. Companion consulta o AnKing local e ranqueia candidatos.
5. Candidatos confiáveis são copiados literalmente para `NEBLI::*`.
6. Ambíguos ficam `unresolved`.
7. Autorais/IO só cobrem lacunas reais após nova busca.
8. Rodar gates de atomicidade, cloze, visual e cobertura.
9. Gerar um registro de validação para **cada card real do deck**.
10. Rodar `flashcards/scripts/validar_deck_card_a_card.py`.
11. Instalar/fechar somente se 100% dos cards passarem.
12. Conferir recibo e exigir total instalado = total validado.

## Gate card a card

A validação final nunca usa amostragem. `expected_card_count` é o número real do
deck daquela aula e precisa ser igual a `validated_card_count` e
`passed_card_count`. `failed_card_count` deve ser zero.

O registro por card inclui, conforme a fonte:

- identidade (`card_key`, `concept_id`, `source`);
- atomicidade e relevância;
- segurança da fonte;
- score/margem da seleção AnKing;
- preservação de note type e campos;
- mídia;
- política de siblings;
- tamanho do cloze autoral;
- QA visual quando aplicável.

Qualquer falha individual bloqueia o deck inteiro até correção e nova execução do
gate.

O CI mantém um teste de regressão de **40 cards**, distribuídos como um deck-aula
realista (30 AnKing, 6 autorais e 4 IO). Esse 40 não é limite do produto: numa
aula real validam-se todos os cards existentes, sejam 20, 37, 52 ou outro total
dentro do contrato da aula.

## Recibo

Após instalar, o Companion produz/expõe um recibo com:

- conceitos resolvidos/pendentes;
- notas previstas/criadas/puladas;
- cards previstos/criados/suspensos;
- verificações de fonte;
- erros;
- timestamp.

O total confirmado no recibo deve ser igual ao total que passou no gate card a
card. Divergência é falha de pipeline.

## Compatibilidade

Enquanto autorais/IO ainda exigirem recursos não disponíveis no Companion, apenas
essas lacunas podem usar o backend desktop/APKG como fallback. O AnKing não volta
a depender do índice privado/Drive/Colab.
