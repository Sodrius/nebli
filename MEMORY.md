# MEMORY.md — estado vivo do NEBLI

Atualizado em 2026-08-09. Este arquivo contém apenas estado atual; histórico e
regras antigas estão em `docs/legacy/` e no Git.

## Projeto ativo

- Reformar o pipeline padrão para produzir E1 + deck-aula `.apkg` de qualidade.
- E2 e E3 suspensas por não participarem da rotina atual de estudo.
- Retenção longitudinal: 25 novos/dia; cram pré-prova separado.
- A pasta privada `Anking` está visível no Google Drive, mas ainda não expõe um
  arquivo concluído. Quando o APKG aparecer, rodar ingestão, índice e integridade.
- Primeiro ensaio integral após a reforma: aula de Digestório, do zero, sem
  reutilizar decks antigos.

## Decisões vigentes

- Sessão principal produz tudo; agentes apenas revisam e devolvem achados.
- Aula define o escopo; Step 1 aprofunda o mesmo mecanismo/estrutura.
- Ordem de fontes: AnKing → decks externos → autoral.
- Frente e terminologia autoral em inglês; Extra curto em português.
- Imagens: AnKing primeiro, depois decks privados; slide somente em último caso.
- Anatomia e histologia usam IO/identificação visual quando a habilidade é
  reconhecer ou localizar.
- Entrega offline em APKG; AnkiConnect pode existir como utilitário legado, mas
  não é dependência do pipeline canônico.

## Pendências bloqueantes

- Aguardar o APKG concluído aparecer na pasta privada do Drive.
- Indexar o pacote e confirmar mídia/note types.
- Rodar a primeira aula completa e importar o APKG resultante no AnkiDroid.
