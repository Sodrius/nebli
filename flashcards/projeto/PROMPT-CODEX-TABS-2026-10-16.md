# Prompt para o Codex — Tabs das aulas entregues em 15–16/10 (pipeline AnKing-primeiro)

Gere os Tabs (explicação por card) de TODOS os cards destas duas aulas, que hoje estão sem Tab:

| Aula | Busca | Cards sem Tab |
|---|---|---|
| UC03 P1 · 09 Lesão celular, necrose e apoptose | `"tag:NEBLI::2026-uc03-patologia-09-lesao-celular"` | 127 (125 faltando + 2 em estilo antigo) |
| UC03 P1 · 02 Diagnóstico radiológico | `"tag:NEBLI::2026-uc03-radiologia-02-diagnostico-radiologico"` | 52 faltando |

Regras (MEMORY §9 e `config/explicacao-tab.md`):
1. Entrada: `ESTADO-ATUAL.md` › Retomar aqui e MEMORY §9. Não altere cards, cores, ordem nem suspensão; só os Tabs.
2. Gere pela tag da aula, nunca pelo nome do deck:
   `python3 -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc03-patologia-09-lesao-celular"'`
   `python3 -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc03-radiologia-02-diagnostico-radiologico"'`
   (se a geração cair, rode de novo; ela pula o que já está atual).
3. Tab em português, texto corrido de 2–4 parágrafos, do princípio ao card, sem rótulos nem listas. Na 02, respeite a fronteira da radiologia: física, Hounsfield, janelas e T1/T2 só como uma frase de ponte para as aulas 04, 05 e 12.
4. Aceite só com `python3 -m nebli.explicacoes resumo '"tag:…"'` = faltando 0, desatualizada 0, revisar 0, formato_incompleto 0 nas duas tags, e leia uma amostra em sequência (um organizador, um card de imagem da 02, um AnKing, um externo MCAT/Ankisthesia/AnatoKing).
5. Depois: `NEBLI_SEM_TAB=0 python3 -m nebli.gates arquivos-trabalho/deck-aula-uc03-pt09-lesao-celular-v2-2026-10-15` e o mesmo para `deck-aula-uc03-rd02-diagnostico-radiologico-v2-2026-10-16` (gate de Tab deve passar), atualize o ESTADO-ATUAL e faça commit.

Fora deste pedido (decisão de Davi, 16/10): decks P2/P3 antigos têm cards sem Tab ou em estilo antigo, mas serão refeitos pelo pipeline novo; não gerar Tab neles agora.
