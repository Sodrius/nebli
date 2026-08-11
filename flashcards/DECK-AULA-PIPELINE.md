# Pipeline canônico de deck-aula v9

O contrato autoritativo está em `docs/canon/PIPELINE-E1-DECK.md`. Este resumo
existe para impedir que comandos antigos reintroduzam E2, APKG ou cobertura por
amostragem.

## Ordem obrigatória

1. Inventariar slides, objetivos, notas e informação visual.
2. Escrever a E1-base e revisá-la slide a slide.
3. Atomizar o core em conceitos com âncora literal na E1.
4. Buscar cada recuperação no AnKing; usar deck externo e autoria apenas depois
   de busca ampla documentada.
5. Incorporar na E1 o aprofundamento Step 1 do mesmo tema antes de congelá-la.
6. Fechar a matriz conceito → âncora → qualidade → cards e o teto real.
7. Validar 100% dos cards e rodar `finalizar_entrega_canonica.py`, que produz
   somente E1/PDF + manifesto completo para o Companion.
8. Tocar no manifesto no tablet; o Companion instala, valida, seleciona o deck e
   abre o AnkiDroid.

## Gates

- `pipeline_version=e1-deck-v9`;
- `release_gate.schema=nebli-e1-deck-release-v1`;
- E1 fonte/PDF congeladas por SHA-256;
- revisão independente da formulação, core, mecanismos e informação visual;
- todo nuclear com cobertura 2–3 e ao menos um card adequado;
- AnKing selecionado sempre `anking_required=true`;
- qualquer rota não-AnKing com três buscas independentes, expansão de escopo,
  revisão de siblings e rejeições registradas;
- todo autoral com recuperação única e revisão de qualidade explícita;
- `failed_card_count=0` e total instalado igual ao previsto.

Para o usuário, a saída é somente E1/PDF + manifesto `.ankidroid.json`. Os
artefatos de trabalho e auditoria permanecem internos.
