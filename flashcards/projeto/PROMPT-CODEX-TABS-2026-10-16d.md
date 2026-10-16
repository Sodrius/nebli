# Prompt para o Codex — Tabs da Micro P3 refeita (43, 44, 48, 50), 16/10 noite

Gere os Tabs (explicação por card) dos cards destas aulas que estão sem Tab, desatualizados ou a revisar:

| Aula | Busca | Faltando | Desatualizados | Revisar |
|---|---|---|---|---|
| UC03 P3 · 43 Biologia geral dos fungos | `"tag:NEBLI::2026-uc03-microbiologia-43-biologia-fungos"` | 37 | 6 | 3 |
| UC03 P3 · 44 Micoses superficiais e cutâneas | `"tag:NEBLI::2026-uc03-microbiologia-44-micoses-cutaneas"` | 73 | 6 | 2 |
| UC03 P3 · 48 Micoses subcutâneas | `"tag:NEBLI::2026-uc03-microbiologia-48-micoses-subcutaneas"` | 19 | 9 | 1 |
| UC03 P3 · 50 Micoses sistêmicas | `"tag:NEBLI::2026-uc03-microbiologia-50-micoses-sistemicas"` | 92 | 10 | 2 |

(09, 02, 03 e 51 já estão completas. Este prompt substitui o PROMPT-CODEX-TABS-2026-10-16c, que só tinha a 43.)

Refazer também (Davi criticou o Tab nos comentários de 16/10; regenere com `python3 -m nebli.explicacoes gerar 'nid:1791625427358 OR nid:1791629595872' --refazer` levando estas instruções):
- `nid:1791625427358` — “tab não fala o que é invariant chain”: o Tab tem de dizer o que é a cadeia invariante (ocupa a fenda do MHC II no RE e guia ao endossomo; sobra o CLIP, trocado pelo peptídeo via HLA-DM).
- `nid:1791629595872` — “TAB RUIM”: explicar o porquê (C1q precisa de duas Fc próximas; IgM pentamérica oferece isso com uma molécula, IgG precisa de várias).

Regras (MEMORY §9 e `config/explicacao-tab.md`):
1. Entrada: `ESTADO-ATUAL.md` › Retomar aqui e MEMORY §9. Não altere cards, cores, ordem nem suspensão; só os Tabs.
2. Gere pela tag de cada aula, nunca pelo nome do deck: `python3 -m nebli.explicacoes gerar '"tag:NEBLI::<lesson>"'` (rode de novo se cair; ele pula o que já está atual).
3. Tab em português, texto corrido de 2–4 parágrafos, do princípio ao card, sem rótulos nem listas. Muitas notas são compartilhadas entre 43/44/48/50:
   o Tab deve servir à nota em qualquer das aulas (sem citar a aula). Temas sem card próprio podem aparecer no Tab do card vizinho (43: pleomorfismo,
   melanina, nutrição por absorção; 44: tinha imbricata/manuum, técnica do carpete; 48: Lacazia não cultivável, golfinhos; 50: histórico da PCM, gp43).
   Micoses de cobertura mínima (tinha negra, piedras, feo-hifomicose, cocci, blasto, aspergilose, mucormicose, pneumocistose): Tab curto, sem virar capítulo.
4. Aceite só com `python3 -m nebli.explicacoes resumo '"tag:NEBLI::<lesson>"'` = faltando 0, desatualizada 0, revisar 0, formato_incompleto 0 em cada aula,
   e leia uma amostra em sequência por aula (um organizador, um AnKing, uma nota compartilhada).
5. Depois: `NEBLI_SEM_TAB=0 python3 -m nebli.gates arquivos-trabalho/<corrida>` nas quatro corridas (`…-mb43-biologia-fungos-v2-2026-10-16`,
   `…-mb44-micoses-cutaneas-v2-2026-10-16`, `…-mb48-micoses-subcutaneas-v2-2026-10-16`, `…-mb50-micoses-sistemicas-v2-2026-10-16`), atualize o ESTADO-ATUAL e faça commit.
