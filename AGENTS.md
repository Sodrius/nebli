# NEBLI — entrada universal

Este arquivo é a entrada obrigatória para qualquer agente, inclusive ChatGPT e Claude. Não use histórico de conversa para completar regras do pipeline.

1. Leia `config/pipeline.json` — autoridade mecânica.
2. Leia `docs/canon/EXECUCAO.md` — ordem operacional e definição de pronto.
3. Leia `docs/canon/E1.md` — contrato pedagógico e visual da E1.
4. Leia `docs/canon/CARD-QUALITY.md`, `docs/canon/CARDS.md`, `docs/canon/VISUAL-E-IO.md` e `docs/canon/ANKIDROID-COMPANION.md`.
5. Leia somente os exemplares UC02 apontados por `docs/canon/E1.md`.

`docs/legacy/`, scripts históricos e arquivos de memória não participam de uma corrida normal. O modo ativo é `authored_only`: AnKing e decks externos permanecem preservados no código, suspensos por configuração e nunca são consultados ou copiados.

Quando o usuário fornecer materiais de uma aula, execute todo o fluxo sem pedir escolhas resolvíveis pelo repositório: materiais → matriz fonte/E1 → E1 → núcleo de retenção → autorais/IO → validação com hashes → manifesto → Companion → AnkiDroid.
