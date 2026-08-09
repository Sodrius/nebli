# Reforma do pipeline E1 + deck-aula

Estado em 2026-08-09. Este documento acompanha a implantação; as regras de
produto vivem em `docs/canon/`.

## Concluído nesta reforma

- [x] tornar `/resumo` a entrada padrão de E1 + deck;
- [x] desligar E2, E3 e RemNote na configuração;
- [x] separar regras atuais de documentação histórica;
- [x] concentrar produção na sessão principal e restringir agentes à revisão;
- [x] formalizar cobertura atomizada, âncora E1 e aprofundamento Step 1;
- [x] formalizar AnKing → deck externo → autoria comprovada;
- [x] definir visual/IO por tarefa cognitiva e proveniência;
- [x] indexar APKG privado moderno/legado sem AnkiConnect;
- [x] auditar o APKG real offline;
- [x] criar hard gate do contrato v3 + APKG;
- [x] fixar 25 novos/dia e opcionais em subdeck;
- [x] preservar regras antigas em `docs/legacy/`.

## Dependências ainda externas

- [ ] aguardar o APKG concluído aparecer na pasta privada `Anking` do Drive;
- [ ] gerar e validar o índice privado, sem versioná-lo;
- [ ] adaptar/fechar o montador offline com os note types e mídia observados no
  AnKing real;
- [ ] executar a aula Digestório do zero;
- [ ] importar o APKG no Anki Desktop e AnkiDroid;
- [ ] ajustar critérios com base no primeiro uso longitudinal.

## Riscos e resposta

| Risco | Detecção | Resposta |
|---|---|---|
| upload incompleto/corrompido | tamanho, SHA-256, ZIP e SQLite | bloquear índice e deck |
| formato Anki moderno | membro `anki21b`/zstd | descompactação e schema moderno suportados |
| busca literal perde card bom | pouca cobertura e sinônimos | consultas PT/EN, mecanismo, tags e cards irmãos |
| Step 1 abre assunto vizinho | nova árvore de pré-requisitos | rejeitar ou criar aula separada |
| autoria encobre busca ruim | ausência de candidatos/rejeição | hard gate de contagens e justificativa |
| imagem bonita mas inútil | tarefa visual não demonstrada | reprovar no contrato/preview |
| IO esconde a própria pista | target ilegível sem rótulo | usar marcador/prompt visual, sobretudo em histologia |
| mídia colide ou quebra | hash, mapa ZIP e referência HTML | deduplicar/renomear e auditar APKG |
| JSON diz “ok”, pacote não | divergência do arquivo exportado | gate abre o APKG real |
| scripts antigos voltam ao fluxo | comando/configuração canônica | `/resumo` chama apenas v3; legado não aprova release |

O montador offline só será considerado concluído depois de receber o AnKing real:
implementar às cegas contra um note type suposto recriaria exatamente o problema
que esta reforma busca eliminar.
