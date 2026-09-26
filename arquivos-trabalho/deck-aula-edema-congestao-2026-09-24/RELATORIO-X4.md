# X4 — Edema e congestão (UC03)

24/09/2026. Lote apenas deck; não foram criados E1 ou guia.

## Recorte e fontes

- **Prova:** `referencias-externas/uc03/consultar.py --slug pat-05-edema-congestao --completo`; questões úteis incluem edema pulmonar hidrostático após falência cardíaca (2024 P2) e edema inflamatório com exsudato (2019 P1). Menções incidentais a edema no gabarito não ampliaram o escopo.
- **Slide docente:** [Edema e congestão](https://drive.google.com/file/d/1akEbdwSRKaGC3-6rj2e7XZEsyYHK2yss/view). Usei somente o início, até a divisória “Patologia Ambiental”: definições, coleções, forças, mecanismos e morfologia.
- **E1 antiga:** [Edema e congestão — etapas 1 a 3](https://drive.google.com/file/d/1VKwKWVk11boLAp5lfQcWApHIHYYme7Nl/view). Complementou exemplos e a descrição de pulmão/fígado. Não transpus a simplificação de reabsorção venosa ampla nem limiares diagnósticos soltos.
- **Livro:** Robbins & Cotran, 10ª ed., cap. 4 é a bibliografia indicada, mas o exemplar integral não estava acessível nesta corrida. Substitutos efetivamente consultados: [Clinical Methods, Edema](https://www.ncbi.nlm.nih.gov/books/NBK348/) para forças/retensão e [StatPearls, Cardiac Cirrhosis](https://www.ncbi.nlm.nih.gov/books/NBK431053/) para congestão hepática.
- **Vídeo do assunto:** [Osmosis, Pulmonary Edema](https://www.youtube.com/watch?v=oRDOUv6dEpE). Legendas consultadas em `video-pulmonary-edema.en.vtt`; confirmam hidrostática, oncótica, permeabilidade, linfa e falência esquerda. Não atribuí achados visuais ao vídeo.
- **Step 1:** notas originais do AnKing no deck vivo `Referências::Anking Step Deck`, inspecionadas antes da cópia. Acervos externos redescobertos no preflight (`catalogo.json`) e confrontados com o [mapa X2](../deck-aula-inflamacao-aguda-2026-09-24/MAPA-ACERVOS-EXTERNOS.md); nenhum candidato externo acrescentou teste melhor ao recorte.

## Resultado vivo

- Deck: `NEBLI::UC03::P2::Patologia::Edema e congestão`.
- **30 notas/36 cartões novos**: 21 AnKing, 15 autorais. **1 nota da X2 já existente, com 2 cartões**, recebeu a tag X4 sem duplicação física (nota `1790253536913`, exsudato versus transudato). Portanto a aula tem 38 cartões acessíveis por deck + tag.
- **3 rosas**: hidrotórax, hidropericárdio e anasarca, nomes ensinados no objetivo, de menor valor duradouro. **8 verdes** do AnKing. Nenhum suspenso.
- Revisão final retirou a cópia recém-instalada sobre Budd–Chiari, pois a entidade específica extrapolava o recorte documentado. O original AnKing permanece intacto; a exclusão está em `prune.json`.
- `verification.json`: 36 IDs previstos = 36 no deck, frente/verso/mídia presentes, fontes originais inalteradas, flag 5 em 3, flag 3 em 8, tag compartilhada presente, histórico da nota compartilhada intacto.
- Preset NEBLI alinhado (35 novos/dia), sincronização concluída após instalar e novamente após a correção.
- [NEBLI-UC03.apkg](NEBLI-UC03.apkg) é o pacote **da UC03 inteira**, exportado da coleção viva: 789 cartões, 190 arquivos de mídia, 45.976.588 bytes, SHA-256 `dee6eb240b541997a71b3dafa23ee92312467d08c86bba9a2781125fe784e303`. ZIP e SQLite íntegros, compressão DEFLATE, zero bandeiras visíveis no APKG; IDs e bandeiras da coleção preservados. Recibo em `NEBLI-UC03.publication-ready.json`. Não houve teste de importação em perfil separado nem upload.

## Repetições e lacunas

- Antes da criação, a busca viva achou a nota X2 de exsudato/transudato e a associou por tag. A tabela de limiares da X2 não foi copiada: além de ser repetição, limiares de E1 e critérios de derrame pleural não são intercambiáveis. Os cartões externos Ankisthesia de critérios de Light também ficaram fora.
- Nenhuma identidade de fonte selecionada já existia em outro deck NEBLI. A auditoria X2 (`DUPLICIDADES-ENTRE-DECKS.md`) registrara zero cópias de fonte entre decks naquela data; a busca X4 foi feita de novo no estado vivo.
- Lacunas de fonte: Robbins integral não acessível; texto extraído do PDF docente omite detalhes de várias figuras. Por isso a morfologia foi triangulada com E1 e substituto, sem criar identificação de imagem não verificada.
