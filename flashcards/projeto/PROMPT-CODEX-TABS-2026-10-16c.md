# Prompt para o Codex — Tabs da 43 Biologia geral dos fungos (16/10 noite, refação v2 da Micro P3)

Gere os Tabs (explicação por card) dos cards desta aula que estão sem Tab ou com Tab desatualizado:

| Aula | Busca | Cards sem Tab |
|---|---|---|
| UC03 P3 · 43 Biologia geral dos fungos | `"tag:NEBLI::2026-uc03-microbiologia-43-biologia-fungos"` | 37 (28 faltando + 6 desatualizados + 3 a revisar) |

(09, 02, 03 e 51 já estão completas: faltando 0, desatualizada 0, revisar 0.)

Regras (MEMORY §9 e `config/explicacao-tab.md`):
1. Entrada: `ESTADO-ATUAL.md` › Retomar aqui e MEMORY §9. Não altere cards, cores, ordem nem suspensão; só os Tabs. Não toque nas notas com `NEBLI::retirado::refacao-v2` (aula antiga retirada).
2. Gere pela tag da aula, nunca pelo nome do deck:
   `python3 -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc03-microbiologia-43-biologia-fungos"'`
   (se cair, rode de novo; ele pula o que já está atual).
3. Tab em português, texto corrido de 2–4 parágrafos, do princípio ao card, sem rótulos nem listas. Aula guarda-chuva da micologia: o que é um fungo
   (eucarionte heterotrófico; parede de quitina e glucanas; ergosterol), formas (levedura, bolor, dimórfico), reprodução, fatores de crescimento, e como os
   antifúngicos exploram parede e ergosterol. Os temas sem card desta aula (pleomorfismo, melanina, nutrição por absorção, cristas achatadas, micélio
   vegetativo × aéreo, esporos sexuais por filo) podem aparecer no Tab do card vizinho, sem virar capítulo. Espécies em detalhe ficam para as aulas 44/50.
4. Aceite só com `python3 -m nebli.explicacoes resumo '"tag:NEBLI::2026-uc03-microbiologia-43-biologia-fungos"'` = faltando 0, desatualizada 0, revisar 0,
   formato_incompleto 0, e leia uma amostra em sequência (o organizador de antifúngicos, um AnKing de dimorfismo, o organizador do ciclo sexual).
5. Depois: `NEBLI_SEM_TAB=0 python3 -m nebli.gates arquivos-trabalho/deck-aula-uc03-mb43-biologia-fungos-v2-2026-10-16` (gate de Tab deve passar),
   atualize o ESTADO-ATUAL e faça commit.
