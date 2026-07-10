# cards-nebli/ — cards autorais NEBLI (fonte versionada)

Cards **gerados pelo NEBLI** para cobrir lacunas de processo que o AnKing não drilla (EMT, dobramentos, membranas, organizadores...). Um arquivo por aula: `<slug>.json`.

**Princípio:** o Anki é o alvo renderizado; **o git é a fonte-verdade**. Se o deck do Anki morrer, os cards autorais se reconstroem daqui via AnkiConnect. Cada card carrega um `nebli_id` estável (campo escondido) para permitir re-sync quando a E1 muda, sem duplicar.

## Schema por aula (`<slug>.json`)
```json
{
  "slug": "embrio-gastrulacao-neurulacao",
  "deck": "NEBLI::UC02::03_Embriologia::P3-06_gastrulacao-neurulacao",
  "cards": [
    {
      "nebli_id": "embrio-gn-emt-01",
      "subtopico": "1.2",
      "modelo": "Cloze",
      "texto": "To ingress through the primitive streak, an epiblast cell undergoes {{c1::epithelial–mesenchymal transition (EMT)}}.",
      "extra": "Same machinery is re-used by neural crest and, pathologically, in cancer metastasis.",
      "imagem": "figuras/embrio-gastrulacao-neurulacao/slide-14.png",
      "fonte_e1": "1.3 — A ingressão: ...frase da E1...",
      "tags": ["NEBLI::embrio-gastrulacao-neurulacao", "NEBLI::autoral"]
    }
  ]
}
```

## Regras
- **Formato R9:** cloze deletion, **um único cloze** (`{{c1::...}}`) por card, `extra` sucinto sempre, `imagem` quando viável (slide ou figura de card AnKing).
- Só gerar após a lacuna estar confirmada (subtópico RASO/LACUNA na rubrica R6) **e** a fonte estar na E1 (`fonte_e1` obrigatório — honra R1).
- Formato e voz seguem `../EXEMPLARES-CARDS.md`; evitar os padrões de `../ANTI-EXEMPLARES-CARDS.md`.
- Tag dupla: `NEBLI::<slug>` (aula) + `NEBLI::autoral` (para distinguir de card AnKing curado).
- Aplicar via AnkiConnect `addNotes` (dedupe pelo primeiro campo); nunca inserir na árvore AnKing compartilhada — só no deck NEBLI.

Nenhum card autoral gerado ainda (pendência: calibrar padrão com cards reais antes — ver `FLASHCARDS.md` § Pendências).
