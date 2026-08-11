# Pipeline canônico E1 + Deck-Aula — v7

## Definição de pronto

O pipeline só termina quando o **deck inteiro** foi planejado, validado e
instalável pelo Nebli Companion no AnkiDroid. O artefato canônico de entrega é o
manifesto completo `nebli-ankidroid-deck-v3`; APKG não faz parte do fluxo normal.

## Fluxo

1. Validar slug, nome curto, UC/prova/componente e fontes.
2. Criar checkpoint e contrato inicial a partir de slides/objetivos.
3. Escrever E1 rascunho; não gerar E2/E3.
4. Atomizar a E1 em conceitos nucleares, de apoio e opcionais.
5. Definir porte e congelar `card_budget.hard_max` antes da seleção.
6. Para cada conceito, definir a **recuperação específica** que justificaria um
   card e sua âncora literal na E1.
7. Planejar fonte na ordem AnKing → deck externo → autoral.
8. Para cada recuperação, concluir a busca AnKing antes de autorar. Registrar
   consultas independentes, resposta esperada, contexto obrigatório/proibido,
   candidatos aceitos/rejeitados e um fallback validado.
9. Julgar Step 1 pelo teste de mesmo tema. O AnKing regula a profundidade, não o
   escopo: conteúdo aceito entra na E1 antes do card e somente então a E1 é
   congelada.
10. Definir plano visual antes de fechar cada card:
    - reconhecimento/localização → IO/prompt visual;
    - mecanismo → imagem no Extra quando agrega;
    - verbal → `none`.
11. Autorais só para lacunas reais. Seguir integralmente
    `docs/canon/CARD-QUALITY.md`.
12. IO precisa de fonte real, máscara correta, geometria, preview de pergunta e
    resposta, ausência de vazamento e QA visual.
13. Produzir `arquivos-trabalho/<slug>/deck-data.json` com **todos os cards
    finais**. Cada card tem `card_key`, `concept_id`, `source`, `tier`,
    `atomic=true`, `relevant=true` e os campos específicos da fonte.
14. Rodar o gate card a card no total real. Uma falha impede empacotamento.
15. Gerar o manifesto completo:

    `python flashcards/scripts/gerar_manifesto_ankidroid.py --slug <slug> --deck-data arquivos-trabalho/<slug>/deck-data.json`

16. O gerador:
    - exige os quatro metadados e deriva exclusivamente
      `NEBLI::<UC>::<Prova>::<Componente>::<Nome curto>`;
    - rejeita `target_deck` manual divergente;
    - valida novamente autorais/IO;
    - exige fallback para cada seleção AnKing;
    - embute mídia nova por SHA-256/base64;
    - rejeita identidades duplicadas;
    - fixa `expected_card_count` no número real do deck.
17. No tablet, abrir o manifesto no Nebli Companion.
18. O Companion:
    - busca a nota AnKing pelo contexto e escolhe o sibling pela resposta
      esperada, sem misturar os dois scores;
    - trata o nome local do deck AnKing como dica e rebusca por marcador quando
      necessário;
    - copia literal quando confiável;
    - usa fallback validado quando a busca é ausente/ambígua;
    - instala autorais e IO diretamente;
    - separa `::Optional`;
    - verifica fonte, siblings, render e contagem;
    - faz rollback das notas novas se houver falha parcial;
    - seleciona o deck correto e abre o AnkiDroid.
19. O recibo final precisa provar:
    - `installed_card_count == expected_card_count`;
    - nenhuma falha;
    - nenhuma fonte alterada;
    - deck correto selecionado.
20. Entregar E1, manifesto completo e relatório/recibo. Atualizar checkpoint e
    memória canônica do projeto.

## Bloqueios

Bloqueiam a conclusão:

- lacuna nuclear ignorada;
- card sem âncora E1;
- card não atômico ou irrelevante;
- teto excedido;
- AnKing escolhido apenas por tema semelhante;
- autoral direto sem busca AnKing completa e motivo real de rejeição;
- AnKing previamente validado que caiu silenciosamente em fallback;
- AnKing sem fallback no plano final;
- autoral com mais de uma recuperação/cloze ou cloze longo;
- IO incorreto ou visual obrigatório ausente;
- mídia quebrada;
- total validado diferente do esperado;
- total instalado diferente do esperado;
- fonte AnKing modificada;
- qualquer write fora de `NEBLI::*`.
