# Prompt para o Codex — Tabs das aulas instaladas em 17/10 (UC03 P1 v2 04→22 e P3 53, 55, 56, 57)

Gere os Tabs (explicação por card) dos cards destas aulas que estão sem Tab ou desatualizados (revisar = 0 em todas):

| Aula | Busca | Faltando | Desatualizados |
|---|---|---|---|
| UC03 P1 · 04 Radiografia e ultrassom | `"tag:NEBLI::2026-uc03-radiologia-04-radiografia-ultrassom"` | 42 | 0 |
| UC03 P1 · 05 Tomografia | `"tag:NEBLI::2026-uc03-radiologia-05-tomografia"` | 27 | 3 |
| UC03 P1 · 06 Correlação 1 | `"tag:NEBLI::2026-uc03-patologia-radiologia-06-correlacao-1"` | 69 | 7 |
| UC03 P1 · 07 Organização do SI | `"tag:NEBLI::2026-uc03-imunologia-07-organizacao-sistema-imune"` | 44 | 3 |
| UC03 P1 · 08 Reconhecimento inato | `"tag:NEBLI::2026-uc03-imunologia-08-reconhecimento-inato"` | 28 | 0 |
| UC03 P1 · 10 Ação hormonal | `"tag:NEBLI::2026-uc03-bioquimica-10-acao-hormonal"` | 84 | 8 |
| UC03 P1 · 11 Acúmulos e adaptação | `"tag:NEBLI::2026-uc03-patologia-11-acumulos-adaptacao"` | 72 | 6 |
| UC03 P1 · 12 Ressonância magnética | `"tag:NEBLI::2026-uc03-radiologia-12-ressonancia-magnetica"` | 16 | 2 |
| UC03 P1 · 13 Envelhecimento | `"tag:NEBLI::2026-uc03-patologia-13-envelhecimento"` | 55 | 0 |
| UC03 P1 · 14 Declaração de óbito | `"tag:NEBLI::2026-uc03-patologia-14-declaracao-obito"` | 18 | 7 |
| UC03 P1 · 15 GR1 Esquizofrenia | `"tag:NEBLI::2026-uc03-grand-round-01-esquizofrenia"` | 78 | 0 |
| UC03 P1 · 16 Regulação hormonal | `"tag:NEBLI::2026-uc03-bioquimica-16-regulacao-hormonal-massa-corporea"` | 43 | 8 |
| UC03 P1 · 17 Reconhecimento adaptativo | `"tag:NEBLI::2026-uc03-imunologia-17-reconhecimento-adaptativo"` | 42 | 0 |
| UC03 P1 · 18 Recombinação | `"tag:NEBLI::2026-uc03-biologia-molecular-18-recombinacao"` | 24 | 1 |
| UC03 P1 · 20 MHC e apresentação | `"tag:NEBLI::2026-uc03-imunologia-20-mhc-apresentacao"` | 24 | 0 |
| UC03 P1 · 22 Mecanismos efetores | `"tag:NEBLI::2026-uc03-imunologia-22-mecanismos-efetores"` | 24 | 2 |
| UC03 P3 · 53 GR4 Paracoccidioidomicose | `"tag:NEBLI::2026-uc03-grand-round-04-paracoccidioidomicose"` | 8 | 1 |
| UC03 P3 · 55 Prática de micologia | `"tag:NEBLI::2026-uc03-microbiologia-55-pratica-micologia"` | 16 | 5 |
| UC03 P3 · 56 Contrastes radiológicos | `"tag:NEBLI::2026-uc03-radiologia-56-contrastes"` | 34 | 0 |
| UC03 P3 · 57 Princípios gerais dos vírus | `"tag:NEBLI::2026-uc03-microbiologia-57-principios-gerais-virus"` | 64 | 3 |

Total: 812 faltando, 56 desatualizados.

Pontos de conteúdo para o Tab:
- 08 · ak-nod2-crohn: o Extra original do AnKing diz que o NOD2 reconhece LPS; o ligante do NOD2 é o muramil-dipeptídeo do peptidoglicano. O Tab deve dizer o certo (sem editar o Extra original).
- 53 · lâmina 65 atribui ao itraconazol a inibição da glucana-sintase; o alvo dos azóis é a 14α-desmetilase (glucana-sintase é das equinocandinas). O Tab dos cards de antifúngico pode lembrar a diferença.
- 57 · a tabela da lâmina 25 dá à Rickettsia metabolismo gerador de ATP (só a Chlamydia não tem); não repetir no Tab que a Rickettsia não gera ATP.
- 56 · limites da aula: clearance < 30 contraindica iodo e gadolínio (exceto se houver diálise logo depois); 30–45 pondera; a apostila de veteranos diz "gadolínio sempre contraindicado na IRC" — vale a aula.

Regras (MEMORY §9 e `config/explicacao-tab.md`):
1. Entrada: `ESTADO-ATUAL.md` › Retomar aqui e MEMORY §9. Não altere cards, cores, ordem nem suspensão; só os Tabs.
2. Gere pela tag de cada aula: `python3 -m nebli.explicacoes gerar '"tag:NEBLI::<lesson>"'` (rode de novo se cair; ele pula o que já está atual).
   Respeite o lock `arquivos-trabalho/ANKI-ESCRITA.lock` e nunca toque a nota em tela de Davi.
3. Tab em português, texto corrido de 2–4 parágrafos, do princípio ao card, sem rótulos nem listas; nota compartilhada entre aulas: Tab que sirva a todas.
4. Aceite só com `python3 -m nebli.explicacoes resumo '"tag:NEBLI::<lesson>"'` = faltando 0, desatualizada 0, revisar 0, formato_incompleto 0 em cada aula,
   e leia uma amostra em sequência por aula (um autoral, um AnKing, uma nota compartilhada).
5. Depois: `NEBLI_SEM_TAB=0 python3 -m nebli.gates arquivos-trabalho/deck-aula-uc03-<corrida>` em cada corrida da tabela (as pastas são as da coluna 1 do
   ESTADO-ATUAL › Retomar aqui), atualize o ESTADO-ATUAL e faça commit.

Corridas: `deck-aula-uc03-rd04-radiografia-ultrassom-v2-2026-10-16`, `deck-aula-uc03-rd05-tomografia-v2-2026-10-16`, `deck-aula-uc03-pr06-correlacao-1-v2-2026-10-16`, `deck-aula-uc03-im07-organizacao-sistema-imune-v2-2026-10-16`, `deck-aula-uc03-im08-reconhecimento-inato-v2-2026-10-16`, `deck-aula-uc03-bq10-acao-hormonal-v2-2026-10-16`, `deck-aula-uc03-pt11-acumulos-adaptacao-v2-2026-10-17`, `deck-aula-uc03-rd12-rm-v2-2026-10-17`, `deck-aula-uc03-pt13-envelhecimento-v2-2026-10-17`, `deck-aula-uc03-pt14-declaracao-obito-v2-2026-10-17`, `deck-aula-uc03-gr15-grand-round-1-v2-2026-10-17`, `deck-aula-uc03-bq16-regulacao-hormonal-v2-2026-10-17`, `deck-aula-uc03-im17-reconhecimento-adaptativo-v2-2026-10-17`, `deck-aula-uc03-bm18-recombinacao-v2-2026-10-17`, `deck-aula-uc03-im20-mhc-v2-2026-10-17`, `deck-aula-uc03-im22-mecanismos-efetores-v2-2026-10-17`, `deck-aula-uc03-gr53-grand-round-4-v2-2026-10-17`, `deck-aula-uc03-mb55-micologia-pratica-v2-2026-10-17`, `deck-aula-uc03-rd56-contrastes-v2-2026-10-17`, `deck-aula-uc03-mb57-principios-virus-v2-2026-10-17`
