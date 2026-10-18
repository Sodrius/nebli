# Prompt para o Codex — Tabs pendentes (15/10/2026)

Cole o texto abaixo no Codex.

---

Você vai gerar os Tabs (explicações) de todos os decks que o Claude instalou entre 13 e 15/10/2026 sem Tab. Trabalhe no repo `~/NEBLI`, com o Anki aberto (AnkiConnect), seguindo `CLAUDE.md`, `MEMORY.md`, `config/explicacao-tab.md`, `flashcards/projeto/PLANO-CARDS-TABS.md` e `GUIA-EXPLICACOES-TAB.md`.

**Convivência com a revisão por prova do Claude (15/10):** o Claude está revisando os decks da UC03 por prova (começando pelas aulas novas da P1, depois P3 e P2) e pode mudar cards destas aulas (reescrever, retirar, acrescentar card-ponte ou de conexão). Antes de cada aula, olhe no `ESTADO-ATUAL.md` se ela está “Com Claude: revisão por prova”; se estiver, pule e volte a ela depois. (Em 15/10 à tarde, todas as aulas desta tabela e a micro da P3 — 43, 44, 48, 50 — foram refeitas por completude; as da P3 também precisam de Tab nos cards novos.) Você não muda cards. No fim, rode `gerar` de novo em todas as tags da tabela: só os cards alterados depois do seu Tab saem como desatualizados e são refeitos.

**Antes de começar:** registre no `ESTADO-ATUAL.md` (“Com Codex: Tabs das corridas Claude 13–15/10”), releia o arquivo antes de gravar e não mexa em corrida que outro executor tenha reivindicado. Davi pode estar estudando: nunca toque a nota em tela nem as irmãs (o próprio `nebli.explicacoes` respeita isso), e o Tab fica fora da coleção.

**Estilo novo (pedido de Davi):** cada Tab em português, em texto corrido, indo do básico ao muito aprofundado naquele ponto. Começa pelo princípio que o estudante do 1º ano precisa para entender a resposta, desce para o mecanismo e termina no detalhe que o card cobra e no porquê dele. O tamanho acompanha a necessidade: 200–300 palavras para um princípio difícil, menos para uma distinção simples. Nunca fale do card, da pergunta, do Extra, da lacuna nem do slide. Explique o assunto como num livro e sem mnemônico inventado. Em organizadores (tríades e classificações), explique o que une os itens e o significado de cada nome.

**Use o percurso de cada aula:** antes de gerar, leia `arquivos-trabalho/<corrida>/percurso-aula.md` (capacidades C1 e blocos), o `spec.py` (bloco, alvo e motivo de cada card) e as fontes em `fontes/` (transcrição, provas). O Tab de cada card deve servir à função dele no bloco e ligar-se ao card vizinho na ordem da aula. Os compartilhados já podem ter Tab de outra aula: não refaça, a menos que esteja ausente.

**Aulas (tag da aula → corrida):**

| Tag (`tag:NEBLI::…`) | Corrida em `arquivos-trabalho/` |
|---|---|
| `2026-uc03-imunologia-07-organizacao-sistema-imune` | `deck-aula-uc03-im07-organizacao-sistema-imune-2026-10-15` |
| `2026-uc03-patologia-09-lesao-celular` | `deck-aula-uc03-pt09-lesao-celular-2026-10-13` |
| `2026-uc03-patologia-11-acumulos-adaptacao` | `deck-aula-uc03-pt11-acumulos-adaptacao-2026-10-14` |
| `2026-uc03-patologia-13-envelhecimento` | `deck-aula-uc03-pt13-envelhecimento-2026-10-14` |
| `2026-uc03-patologia-14-declaracao-obito` | `deck-aula-uc03-pt14-declaracao-obito-2026-10-14` |
| `2026-uc03-bioquimica-10-acao-hormonal` | `deck-aula-uc03-bq10-acao-hormonal-2026-10-14` |
| `2026-uc03-radiologia-12-ressonancia-magnetica` | `deck-aula-uc03-rd12-rm-2026-10-14` |
| `2026-uc03-bioquimica-16-regulacao-hormonal-massa-corporea` | `deck-aula-uc03-bq16-regulacao-hormonal-2026-10-14` |
| `2026-uc03-grand-round-01-esquizofrenia` | `deck-aula-uc03-gr15-grand-round-1-2026-10-14` |
| `2026-uc03-biologia-molecular-18-recombinacao` | `deck-aula-uc03-bm18-recombinacao-2026-10-14` |
| `2026-uc03-imunologia-08-reconhecimento-inato` | `deck-aula-uc03-im08-reconhecimento-inato-2026-10-14` |
| `2026-uc03-imunologia-17-reconhecimento-adaptativo` | `deck-aula-uc03-im17-reconhecimento-adaptativo-2026-10-14` |
| `2026-uc03-imunologia-20-mhc-apresentacao` | `deck-aula-uc03-im20-mhc-2026-10-14` |
| `2026-uc03-imunologia-22-mecanismos-efetores` | `deck-aula-uc03-im22-mecanismos-efetores-2026-10-15` |
| `2026-uc03-microbiologia-40-pratica-3` | `deck-aula-uc03-mb40-pratica3-2026-10-15` |
| `2026-uc21-dic-05-insuficiencia-metabolica` | `deck-aula-uc21-dic05-insuf-metabolica-2026-10-15` |
| `2026-uc03-microbiologia-43-biologia-fungos` | `deck-aula-uc03-mb12-fungos-2026-10-09` |
| `2026-uc03-microbiologia-44-micoses-cutaneas` | `deck-aula-uc03-mb44-micoses-cutaneas-2026-10-10` |
| `2026-uc03-microbiologia-48-micoses-subcutaneas` | `deck-aula-uc03-mb48-micoses-subcutaneas-2026-10-10` |
| `2026-uc03-microbiologia-50-micoses-sistemicas` | `deck-aula-uc03-mb50-micoses-sistemicas-2026-10-10` |

A 09 tem 1 Tab atual e 3 desatualizados: regenere os desatualizados (`--refazer` só neles).

**Para cada aula, na ordem da tabela:**
1. `python3 -m nebli.explicacoes gerar '"tag:NEBLI::<tag>"'` (com `--backend codex` se for o seu caminho).
2. `python3 -m nebli.explicacoes resumo '"tag:NEBLI::<tag>"'` deve sair 0, com cobertura de 100%.
3. Leia os pares card + Tab **na ordem viva da aula** (o despejo `revisao-despejo.txt` dá a ordem). Refaça com `--refazer` os Tabs que falem do card, repitam o Extra, fujam do bloco ou não deixem alguém que não sabia o princípio reconstruir a resposta.
4. `python3 -m nebli.artefatos pos arquivos-trabalho/<corrida> --li-despejo` deve passar em todos os passos (hoje o único que falta é o Tab).
5. Anote em `REVISAO-DE-QUALIDADE.md` da corrida: Tabs N/N, os refeitos e o porquê.

**No fim:** atualize as linhas dessas aulas no `ESTADO-ATUAL.md` (“Tabs N/N”). Republique o pacote da UC03 numa pasta nova (`arquivos-trabalho/pacote-uc03-<data>`): `python3 -m nebli.package_uc --uc UC03 --output "<pasta>/NEBLI - UC03.apkg"` e depois `python3 -m nebli.entrega "UC03/Microbiologia/40 - Prática 3 — identificação bacteriana" --nome "Prática 3 — identificação bacteriana" --uc-apkg "<pasta>/NEBLI - UC03.apkg"`. Sincronize só com Davi ocioso. Não gere E1 e não mude cards: problema de card vai para o relato a Davi.
