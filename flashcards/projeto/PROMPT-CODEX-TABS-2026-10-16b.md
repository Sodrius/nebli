# Prompt para o Codex — Tabs da 51 Distúrbios do sistema imune (16/10, pipeline AnKing-primeiro v4)

Gere os Tabs (explicação por card) de TODOS os cards desta aula, que hoje estão sem Tab:

| Aula | Busca | Cards sem Tab |
|---|---|---|
| UC03 P3 · 51 Distúrbios do sistema imune | `"tag:NEBLI::2026-uc03-imunologia-51-disturbios-sistema-imune"` | 161 (124 faltando + 37 desatualizados das notas associadas de outras aulas) |

(09, 02 e 03 já estão completas: faltando 0, desatualizada 0.)

Regras (MEMORY §9 e `config/explicacao-tab.md`):
1. Entrada: `ESTADO-ATUAL.md` › Retomar aqui e MEMORY §9. Não altere cards, cores, ordem nem suspensão; só os Tabs.
2. Gere pela tag da aula, nunca pelo nome do deck:
   `python3 -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc03-imunologia-51-disturbios-sistema-imune"'`
   (se cair, rode de novo; ele pula o que já está atual).
3. Tab em português, texto corrido de 2–4 parágrafos, do princípio ao card, sem rótulos nem listas. Aula sem lâminas: a lógica está em `arquivos-trabalho/deck-aula-uc03-im51-disturbios-si-v2-2026-10-16/fontes/roteiro-aula.md` (classificar pelo mecanismo que falhou: imunodeficiência, autoimunidade, autoinflamação). Síndromes por cima, foco no mecanismo molecular e celular; hipersensibilidade só como ponte para a aula 64; HIV só entrada pelo CD4 e critério de AIDS. Antígeno sequestrado (oftalmia simpática) pode aparecer no Tab da tolerância.
4. Aceite só com `python3 -m nebli.explicacoes resumo '"tag:NEBLI::2026-uc03-imunologia-51-disturbios-sistema-imune"'` = faltando 0, desatualizada 0, revisar 0, formato_incompleto 0, e leia uma amostra em sequência (um organizador, um AnKing de síndrome, uma nota associada da aula 45).
5. Depois: `NEBLI_SEM_TAB=0 python3 -m nebli.gates arquivos-trabalho/deck-aula-uc03-im51-disturbios-si-v2-2026-10-16` (gate de Tab deve passar), atualize o ESTADO-ATUAL e faça commit.
