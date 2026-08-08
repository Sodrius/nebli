# FLASHCARDS.md — política canônica do deck NEBLI

> Este arquivo define **o que o deck tenta assegurar** e as decisões editoriais que valem hoje. O passo a passo operacional vive em `flashcards/DECK-AULA-PIPELINE.md`. Histórico de tentativas antigas não é regra.

## Objetivo

O deck-aula existe para duas coisas com os **mesmos cards e o mesmo histórico de revisão**:

1. **Retenção longitudinal:** estudar o topo `NEBLI` com **25 novos/dia** + revisões do FSRS, construindo uma base que sobreviva ao semestre e seja útil nas matérias seguintes.
2. **Cram pré-prova:** abrir o subdeck da prova (`NEBLI::<UC>::<Prova>`) e acelerar temporariamente os novos/reviews que ainda faltam para aquela prova. Depois, voltar a 25 novos/dia. Não criar um segundo deck nem duplicar cards para cram.

O deck não substitui a E1. A E1 ensina; o card força recuperação. Todo card precisa ser respondível a partir da E1 daquela aula.

## Escopo de conteúdo

**FMUSP define o que entra.** O slide, os objetivos da aula, perguntas orientadoras e a E1 definem o núcleo. AnKing, bons decks e bibliografia podem elevar a profundidade **do mesmo mecanismo** um pouco acima da aula.

Um aprofundamento entra quando é imediatamente adjacente ao conteúdo da aula, tem pouco custo de pré-requisito e melhora entendimento/transferência entre matérias. Mecanismo, contraste útil, predição, correlação clínico-fisiopatológica curta e reconhecimento visual costumam ser bons. Conduta, dose, guideline, staging, Step 2 e rabbit holes de outra aula ficam fora.

O aprofundamento nunca estreia no Anki: bom card sugere algo útil → a E1 recebe e explica esse conteúdo → só então o card pode entrar.

## Primeiro decidir o que merece card

Antes de buscar qualquer card, cada conceito da E1 recebe uma decisão explícita:

- `nuclear` — precisa ser recuperado ativamente meses depois. É obrigatório haver card aprovado.
- `supporting` — é útil, mas só vira card se acrescentar um alvo de recuperação realmente distinto.
- `no_card` — continua na E1, mas não merece custo de spaced repetition.

Um conceito tende a merecer card quando pelo menos uma destas perguntas tem resposta forte:

- a FMUSP pode exigir recuperação sem pista?
- é mecanismo, relação causal, sequência ou discriminação que se esquece facilmente?
- reaparece em outras matérias/sistemas e vale carregar longitudinalmente?
- é base direta para Step 1 ou para entender fisiopatologia posterior sem abrir outro currículo?
- reconhecimento/localização visual é parte real da competência?

Não criar card só porque algo está em negrito, tem nome técnico, apareceu numa questão da E2 ou é pesquisável no AnKing. E2 **audita** a cobertura; não cria automaticamente novos alvos de card.

## Ordem obrigatória de fontes

Para cada conceito selecionado, a ordem é:

1. **AnKing** — procurar e ler candidatos card a card.
2. **Outros decks de referência** — BlueLink/Dope para anatomia, Histology/LLU para histologia e outros mapeados em `referencias-externas/`.
3. **NEBLIcard autoral** — somente se as duas buscas anteriores forem ausentes ou inadequadas, com a rejeição registrada.

A prioridade vale também depois: se um autoral provisório existe e depois aparece um AnKing/external melhor para o mesmo alvo, o melhor **substitui** o autoral; não é somado a ele.

`curar_anking_v2.py` é um **localizador/rankeador de candidatos**, não um juiz semântico. Palavra em comum, número de imagens, tamanho do Extra ou score heurístico não bastam para aprovar um card.

## Como aprovar um card

Um card só entra se passar pelos seguintes critérios:

- testa exatamente o conceito selecionado, não apenas um vizinho semântico;
- tem um alvo inequívoco e pequeno; idealmente um retrieval target por card;
- não duplica outro card já aprovado para o mesmo alvo;
- pode ser entendido com a E1, sem pré-requisitos laterais escondidos;
- o cloze/pergunta não entrega a resposta por gramática ou contexto;
- o Extra ajuda a reconstruir o porquê sem virar uma miniapostila;
- se o conceito é visual, a imagem treina exatamente a habilidade visual necessária.

Para NEBLIcards autorais: frente/cloze em **inglês médico natural**, Extra em **português**, cloze único por card por padrão, lint + card-mirror + contrato E1 antes de aplicar.

## Imagens

Fonte real é a preferência absoluta, principalmente quando a competência é visual. Para identificar/localizar uma estrutura, preferir **Image Occlusion** sobre peça, atlas ou micrografia real. Para mecanismo/comparação, preferir uma imagem explicativa pertinente no Extra.

Imagem genérica do tema não conta como qualidade. `visual_need=required` sem ativo pertinente, legível e com proveniência não fecha. Regras técnicas ficam em `flashcards/GUIA-IMAGENS-CARDS-NEBLI.md`.

## Volume: consequência do conteúdo, não meta

Não há quota de cards por subtópico e não se mira o topo de uma faixa. Regra prática: **um alvo de recuperação independente ≈ um card**. Um mecanismo complexo pode justificar dois; reconhecimento visual pode justificar um IO adicional. Três ou mais cards sobre o mesmo conceito exigem motivo concreto.

Guardrails para revisão editorial, não metas de produção:

| Porte da aula | Faixa usual |
|---|---:|
| pequena | ~15–25 cards |
| média | ~25–40 cards |
| grande/densa | ~35–55 cards |

Acima da faixa não significa automaticamente erro, mas exige poda de redundância. **Acima de 60 cards numa aula exige revisão explícita de volume e justificativa.** O que importa é o número de cards reais que aparecerão para o Davi, não o número de notes/linhas do manifesto.

Esses guardrails existem para manter 25 novos/dia viável: uma aula não deve consumir vários dias de fila só porque o pipeline encontrou muitos candidatos.

## Deck e ordem de estudo

Árvore única:

`NEBLI::<UC>::<Prova>::<Matéria>::<Aula>`

Uma aula que cai em várias provas mora apenas na primeira prova. Cards AnKing e de decks externos entram por **cópia**; a fonte original fica intocada. `nuclear` deve aparecer antes de `supporting` na fila de novos da aula.

No dia normal: topo `NEBLI`, 25 novos/dia. No cram: subdeck da prova, aumento temporário apenas ali. Detalhes em `flashcards/estrutura-deck-mestre.md`.

## Hard gate de fechamento

Uma aula só fecha quando:

1. todos os conceitos `nuclear` têm card aprovado;
2. `no_card` não foi transformado em card sem reclassificação justificada;
3. todo card está ancorado literalmente na E1;
4. a busca obedeceu `AnKing → outros decks → autoral` e todo autoral tem rejeição das fontes preferidas;
5. não há retrieval targets duplicados;
6. cards visuais obrigatórios têm imagem/IO pertinente aprovado;
7. o volume está dentro do guardrail ou passou revisão explícita de redundância;
8. o deck real no Anki contém as referências aprovadas no manifesto.

O manifesto é a lista de admissão. `montar_deck_aula.py` não pode copiar todo card simplesmente por possuir `NEBLI::<slug>`: tags antigas não são autorização para entrar no deck atual.

## Fonte de verdade

- `FLASHCARDS.md` — objetivos e política editorial.
- `flashcards/DECK-AULA-PIPELINE.md` — sequência operacional e gates.
- `flashcards/CURADORIA-ANKING.md` — como procurar e registrar candidatos AnKing.
- `flashcards/EXEMPLARES-CARDS.md` / `ANTI-EXEMPLARES-CARDS.md` — craft.
- `flashcards/GUIA-IMAGENS-CARDS-NEBLI.md` — visual/IO.
- `MEMORY.md` — apenas estado vivo e preferências atuais; não replica histórico.

Se um documento antigo divergir destes arquivos, este documento e `DECK-AULA-PIPELINE.md` vencem.
