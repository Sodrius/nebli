# UC07 — rodadas de geração: o que aprendemos e o que melhorar

Uma linha por unidade, escrita **depois** da revisão card a card + deck inteiro (`./kenhub-deck --revisado`). Serve para a próxima unidade sair melhor
e para toda sessão nova saber de onde partir. Regra do que vira gate: MEMORY §15.

## Como cada rodada roda (ordem do cronograma, uma unidade por vez, sem fazer em massa)

1. `coleta` (estruturas + imagens) e `coleta_texto` (objetivos, parágrafos, legendas, tabela-resumo) — ritmo humano.
2. `./kenhub-deck <slug> "<Módulo>" "<Submódulo>"` → rascunho com candidatos (AnKing/AnatoKing) **para as estruturas e para os fatos do texto**; `--resumo` para ler.
3. Curadoria: cor por estrutura; Netter/AnKing-IO só se o Kenhub não tem figura; AnKing traduzido (lacunas originais); cards `texto` para o que o AnKing não cobre; `cobre_texto` em tudo.
4. `--dry-run` até os gates PRÉ passarem (cobertura de estruturas, cobertura do quiz, tradução oficial, uma figura, direcionamento…).
5. Instalar (Anki sem janela de edição) → gates PÓS + renderização do deck inteiro (PC e celular) → **olhar as folhas** → `revisao.md` (card a card; deck todo: cobre o quiz? falta algo da aula?) → `--revisado`.
6. Anotar aqui o que melhorar; todo defeito novo vira gate + caso ruim em `teste_gates.py`.

## Rodada 0 (17–18/10/2026) — tronco encefálico, unidades 1–4

- **Aprendido:** o quiz do Kenhub não é só estrutura: tem questões de texto. Cobrir só as estruturas deixa o deck incompleto (comentário de Davi no plexo braquial) → `coleta_texto` + gate `[cobertura-quiz]`.
- **Aprendido:** nome em PT inventado/calcado do inglês (“lâmina quadrigêmea”, “gânglios da raiz posterior”) → `glossario.py` (Kenhub PT + Machado + aceitos com fonte); usar a grafia do Machado (“bulbo-pontino”, “teto”).
- **Aprendido:** AnatoKing com duas figuras no card → só uma (G20).
- **Melhorar na próxima:** buscar AnKing também para os fatos do texto (feito no rascunho); cards `texto` curtos (cloze ≤ 4 palavras), um fato por card, no mesmo tom do AnKing; conferir se cada trecho do `revisao.md` tem card que de fato pergunta aquele fato.

## Rodada 1 (18/10/2026) — unidades 1–10, feedback F-01..05 do dia

- **Aprendido (Davi):** sem IO nas estruturas (o Kenhub já destaca em verde: basta a seta); um só tipo de card de texto (AnKing de verdade); mesma estrutura junta e só uma verde; termo técnico explicado no Extra; cloze no termo central (não no complemento); figura do Extra cabendo na tela; AnatoKing só com seta evidente.
- **Aprendido (código):** o template do AnKing repete o Text escondido e tem botões escondidos → render ajustado; `sync` do Anki ocupado derrubava o pipeline → sem sync (pendente); ids de cards de texto precisam ser únicos entre unidades (prefixo da unidade); `texto` pode cobrir estrutura sem figura (`cobre`) e ancorar numa estrutura (`estrutura`).
- **Melhorar na próxima:** curar já com cloze no termo central e negrito no sujeito; usar `img`/`estrutura` quando a figura automática não serve; conferir G18 com Moore; revisar as folhas das 3 unidades novas card a card.

