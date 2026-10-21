# Prompt para o Codex — Tabs da aula 58 instalada em 21/10 (UC03 P3 Microbiologia)

Gere os Tabs (explicação por card) desta aula, instalada suspensa em 21/10 (Claude):

| Aula | Busca | Faltando | Desatualizados |
|---|---|---|---|
| UC03 P3 · 58 Multiplicação viral e antivirais | `"tag:NEBLI::2026-uc03-microbiologia-58-multiplicacao-viral-antivirais"` | 258 | 0 |

Pontos de conteúdo para o Tab:
- Foscarnet: a apostila guia de Micro diz que “se parece com um aminoácido”; o certo (AnKing e Jawetz) é análogo do pirofosfato que liga o sítio do pirofosfato da polimerase, sem fosforilação. O Tab deve dizer o certo.
- A aula 58 é a base mecanística dos antivirais; efeitos adversos, doses e indicações são da UC19 e não entram nos cards (não detalhar no Tab).
- A seção de efeito citopático da Transcrição Ib é da aula 60 (Prática de virologia); aqui só entram o conceito (cópia da 61) e a lise do poliovírus.
- Cards compartilhados com 57, 61 e 51 (polaridade do RNA, sincícios, inclusões): o Tab serve às duas aulas.

Regras (MEMORY §9 e `config/explicacao-tab.md`):
1. Não altere cards, cores, ordem nem suspensão; só os Tabs. Respeite `arquivos-trabalho/ANKI-ESCRITA.lock` e nunca toque a nota em tela de Davi.
2. `python3 -m nebli.explicacoes gerar '"tag:NEBLI::2026-uc03-microbiologia-58-multiplicacao-viral-antivirais"'` (roda de novo se cair; pula o que está atual).
3. Tab em português, texto corrido de 2–4 parágrafos, do princípio ao card, sem rótulos nem listas.
4. Aceite só com `python3 -m nebli.explicacoes resumo '"tag:NEBLI::2026-uc03-microbiologia-58-multiplicacao-viral-antivirais"'` = faltando 0, desatualizada 0, revisar 0, formato_incompleto 0, e uma amostra lida (um autoral, um AnKing, uma nota compartilhada).
5. Depois: `NEBLI_SEM_TAB=0 python3 -m nebli.gates arquivos-trabalho/deck-aula-uc03-mb58-multiplicacao-viral-v2-2026-10-21`, atualize o ESTADO-ATUAL e faça commit.
