# Pipeline canônico E1 + Deck-Aula — v10

## Definição de pronto

O pipeline só termina quando o **deck inteiro** foi planejado, validado e
instalável pelo Nebli Companion no AnkiDroid. O artefato canônico de entrega é o
manifesto completo `nebli-ankidroid-deck-v3`; APKG não faz parte do fluxo normal.

## Fluxo

1. Validar slug, nome curto, UC/prova/componente e fontes.
2. Criar checkpoint e contrato inicial a partir de slides/objetivos.
3. Escrever E1 rascunho; não gerar E2/E3.
4. Revisar semanticamente a E1 contra o inventário dos slides. O gate exige
   objetivos, conteúdo visível, mecanismos, relações, informação visual e notas
   do professor cobertos ou explicitamente indisponíveis. A E1 precisa permitir
   estudar o core sem reabrir os slides na maior parte dos casos.
5. Montar a E1 exclusivamente com `nebli_v2_apostila.typ`: `main.typ` aplica
   `pagina-padrao` e reúne capa, sumário, cabeçalho, `etapa1.typ` e
   `resumindo.typ`. O texto usa os helpers canônicos e não redefine página,
   parágrafo ou hierarquia visual localmente.
6. Compilar, renderizar todas as páginas e fazer revisão visual independente.
   Registrar `e1_format_review` com template, hierarquia, figuras, clipping e
   overflow aprovados; defeito visual pendente bloqueia a entrega.
7. Classificar conceitos como `must_recall`, `derivable`, `e1_only` ou
   `optional`, seguindo `docs/canon/NUCLEO-DE-RETENCAO.md`.
8. Definir porte, congelar `card_budget.hard_max` e fixar os slots de recuperação
   antes da busca AnKing.
9. Para cada slot, definir a **recuperação específica** que justifica o card e
   sua âncora literal na E1. Todo card deve caber em até 10 segundos.
10. Planejar fonte na ordem AnKing → deck externo → autoral.
11. Para cada recuperação, concluir a busca AnKing antes de autorar. Registrar
   consultas independentes, resposta esperada, contexto obrigatório/proibido,
   candidatos aceitos/rejeitados e um fallback validado.
12. Julgar Step 1 pelo teste de mesmo tema. O AnKing regula a profundidade, não o
   escopo: conteúdo aceito entra na E1 antes do card e somente então a E1 é
   congelada.
13. Definir plano visual antes de fechar cada card:
    - card autoral procura primeiro mídia AnKing local;
    - reconhecimento/localização → IO/prompt visual;
    - mecanismo → imagem no Extra quando agrega;
    - verbal → `none`.
    Slide/fonte externa só entra após busca visual AnKing documentada; toda
    imagem precisa de propósito cognitivo e revisão didática.
14. Autorais só para lacunas reais. Seguir integralmente
    `docs/canon/CARD-QUALITY.md`.
15. IO usa `hide_two_guess_two`, com alvo de duas respostas coerentes (uma é
    permitida, mais de duas não), fonte real, máscara correta, geometria,
    `pair_rationale`, preview de pergunta/resposta, ausência de vazamento e QA.
16. Todo card entregue tem frente, Extra, prompt e resposta visual em português. Fonte AnKing/deck
    externo em inglês informa conteúdo, profundidade e mídia, mas não é copiada;
    a recuperação final é autoral em PT-BR.
17. Todo autoral passa pelo gate anti-indução: exige conhecimento médico,
    revisão cega, zero alternativas plausíveis não resolvidas e ausência de
    pistas gramaticais, lexicais ou da própria resposta na frente.
18. Produzir `arquivos-trabalho/<slug>/deck-data.json` com **todos os cards
    finais**. Cada card tem `card_key`, `concept_id`, `source`, `tier`,
    `atomic=true`, `relevant=true` e os campos específicos da fonte.
19. Registrar `release_gate=nebli-e1-deck-release-v1` no `deck-data.json`, com
    hashes da E1 fonte/PDF, revisão semântica, teto e matriz conceito → âncora →
    qualidade → cards. Todo nuclear exige cobertura 2–3 e toda omissão ou
    ambiguidade nuclear precisa estar resolvida. Incluir
    `retention_kernel_review`: slots prévios à busca, compressão, ablação e teto
    de 10 segundos aprovados.
20. Rodar o gate card a card no total real. Uma falha impede empacotamento.
21. Fechar a entrega pelo comando único:

    `python flashcards/scripts/finalizar_entrega_canonica.py --slug <slug> --deck-data arquivos-trabalho/<slug>/deck-data.json --validation-report arquivos-trabalho/<slug>/validacao-cards.json --out-dir entregas/<slug>`

22. O gerador:
    - recusa `deck-data.json` sem `release_gate` aprovado;
    - prova por SHA-256 que E1 fonte e PDF são os artefatos revisados;
    - prova que todo nuclear está coberto e todo card tem conceito/âncora;
    - exige os quatro metadados e deriva exclusivamente
      `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
    - rejeita `target_deck` manual divergente;
    - valida novamente autorais/IO;
    - exige fallback para cada seleção AnKing;
    - embute mídia nova por SHA-256/base64;
    - rejeita identidades duplicadas;
    - fixa `expected_card_count` no número real do deck.
23. No tablet, tocar no manifesto; o Android abre o Nebli Companion.
24. O Companion inicia a instalação automaticamente:
    - busca a nota AnKing pelo contexto e escolhe o sibling pela resposta
      esperada, sem misturar os dois scores;
    - trata o nome local do deck AnKing como dica e rebusca por marcador quando
      necessário;
    - copia literal quando confiável;
    - usa fallback validado quando a busca é ausente/ambígua;
    - instala autorais e IO diretamente, reutilizando mídia AnKing quando
      selecionada;
    - separa `::Optional`;
    - compara referências de mídia esperadas com o render real, além de fonte,
      siblings e contagem;
    - faz rollback das notas novas se houver falha parcial;
    - seleciona o deck correto e abre o AnkiDroid.
25. O recibo final precisa provar:
    - `installed_card_count == expected_card_count`;
    - nenhuma falha;
    - nenhuma fonte alterada;
    - deck correto selecionado.
26. Entregar ao usuário somente E1/PDF e manifesto. `deck-data`, validações e
    relatórios continuam como artefatos internos. Atualizar checkpoint e memória
    canônica do projeto.

## Bloqueios

Bloqueiam a conclusão:

- lacuna nuclear ignorada;
- E1 sem revisão independente ou que ainda dependa dos slides para o core;
- E1 que contorna o template oficial, redefine página/parágrafo ou omite a
  estrutura `main.typ` + `etapa1.typ` + `resumindo.typ`;
- página não renderizada, clipping, overflow ou defeito visual não resolvido;
- objetivo, mecanismo ou informação visual da aula sem decisão de cobertura;
- card sem âncora E1;
- card não atômico ou irrelevante;
- teto excedido;
- card removível sem perda relevante no teste de ablação;
- conceito `derivable` sem caminho curto e explícito a partir de cards reais;
- AnKing escolhido apenas por tema semelhante;
- autoral direto sem busca AnKing completa e motivo real de rejeição;
- card não-AnKing sem três buscas independentes, expansão de escopo, revisão de
  siblings e registro dos candidatos/rejeições;
- AnKing previamente validado que caiu silenciosamente em fallback;
- AnKing sem fallback no plano final;
- autoral com mais de uma recuperação/cloze ou cloze longo;
- IO incorreto ou visual obrigatório ausente;
- mídia quebrada, não renderizada, decorativa ou sem valor didático;
- total validado diferente do esperado;
- total instalado diferente do esperado;
- fonte AnKing modificada;
- qualquer write fora de `NEBLI::*`.
