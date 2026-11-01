# NEBLI — entrada de toda sessão

1. [ESTADO-ATUAL.md](ESTADO-ATUAL.md) › **Retomar aqui** e **Quem está com o quê**: o que fazer agora e o que outro executor já pegou.
2. [MEMORY.md](MEMORY.md): **a regra única e vigente** do que Davi quer (reorganizada em 13/10; versões antigas em `arquivo/` não são norma). Das [FEEDBACKS](flashcards/projeto/FEEDBACKS.md), ler só as entradas novas desde a última sessão.
3. Para fazer um deck: **[PIPELINE DE GERAÇÃO DE DECK v11](flashcards/projeto/EXECUCAO-DECK-AULA.md)** — pipeline único e fixo (deck-prova independente das aulas = mesmo pipeline no **modo prova**, v11) (E0 abrir → E1 ler todo o material → E2 compreender a aula → E3 planejar → E4 buscar nos acervos → E5 montar → E6 instalar e ler o vivo → E7 fidelidade ao slide → E8 entregar), sem pular etapa. Mudança no jeito de fazer deck = mudar a etapa certa desse pipeline (seção “Como mudar o pipeline”), nunca criar processo paralelo.

**v7 (23/10, F-20261023-CLAUDE-01/02/03) — os dois erros a não repetir:** deck que não entende a aula (passo a passo não seguido) e autoral fraco. Cada etapa é registrada com `python3 -m nebli.etapa <corrida> En "…"`; a busca recusa rodar sem compreensão (`aprender` por bloco, conferido lâmina a lâmina) e mapa; **leitura obrigatória inteira antes de abrir a corrida (v10, F-20261029-CLAUDE-03; `nebli.etapa E0` recusa sem ela)** — [regras](flashcards/projeto/GUIA-1-REGRAS.md), [exemplares](flashcards/projeto/GUIA-2-EXEMPLARES.md), [anti-exemplares](flashcards/projeto/GUIA-3-ANTI.md), [a aula: exemplares e anti-exemplares de deck](flashcards/projeto/GUIA-4-AULA.md), MEMORY, pipeline, `config/revisor-autorais.md`, CALIBRACAO-QUALIDADE e FEEDBACKS até a mais recente (lista em `gates.LEITURA_OBRIGATORIA`; o `GUIA_CARDS.md` é histórico de consulta); **exemplo do professor é exemplo** (lâmina “o exemplo de…” nunca vira princípio; o começo da aula pesa mais; deck completo DA AULA, sem trocar de conteúdo); cada autoral moldado num exemplar real; referência da aula consultada (**se não souber qual é, perguntar antes de rodar o deck**).

## Pedido curto

“Faz a aula X”, “continua”, `/deck-aula X` ou só o nome da aula = executar o roteiro inteiro até o deck entregue (instalado **sem Tab**, gates duros 100%, pacote da UC, sync) e relatar no formato do MEMORY §11. Com revisor independente de autorais autorizado em 25/10, sem plano para aprovar, sem pedir permissão, sem parar no meio. **Desde 16/10 noite (F-20261016-CLAUDE-11): rodar as aulas em sequência, cada uma pelo pipeline inteiro, até Davi pedir para parar**; feedback que chegar é aplicado antes do deck seguinte. Plano vigente: [PLANO-ANKING-PRIMEIRO](flashcards/projeto/PLANO-ANKING-PRIMEIRO-2026-10-15.md).

- **O deck segue o slide (F-20261022-CLAUDE-06, gate duro):** depois de ler todo o material e antes de buscar, responder em `compreensao-aula.json` o que a aula ensina, onde se encaixa, o que lembrar e o que o professor ensina em cada bloco de lâminas; o deck nasce disso, o exemplo clínico vem depois do princípio e nunca vira carro-chefe, e a revisão final confere bloco a bloco a fidelidade ao slide.

**Comentários de Davi (F-20261101-CLAUDE-04):** sempre em sete passos com gate — `python3 -m nebli.rodada_comentarios abrir <pasta>` … `verificar <pasta>` (ver MEMORY › Rodada de comentários).

## Limites que não mudam

- Davi estuda no Anki enquanto o executor trabalha: nunca tocar a nota em tela nem irmãos; escrita só por `nebli.decks.escrita()`; sync quando ele estiver ocioso.
- Outro executor (Codex) trabalha em paralelo: reivindicar a aula no ESTADO-ATUAL antes; não mexer no que ele reivindicou; reler antes de gravar.
- Preservar originais AnKing, IDs/histórico, comentários, marcas e suspensões pessoais. Não apagar notas sem autorização de Davi e backup. Arquivar documentos superados em `arquivo/` com hash.
- Feedback novo: literal em FEEDBACKS → regra **reescrita no lugar** no MEMORY (sem acrescentar camada) → check no lint/gate quando mecanizável.
- Não fabricar leitura, busca, teste ou revisão. Gate aprovado não prova julgamento.
- **AnKing-primeiro com gates duros** (MEMORY §5): busca nos três caminhos em todos os acervos, `busca/cobertura.tsv`, autoral só para lacuna provada depois de buscar em AnKing e todas as Referências Externas (sem teto desde 22/10), **todo AnKing das seções da aula é decidido: entra se ensina o princípio da aula, senão fica em EXCLUIDOS com motivo** (v12, F-20261101-CLAUDE-01; `SECOES_DA_AULA`) e relido contra os ANTI-EXEMPLARES. O `apply` recusa instalar sem isso.

## UC07 / Kenhub (neuroanatomia)

**Toda sessão da UC07 começa por `./kenhub-deck --painel`** (gera `flashcards/projeto/UC07-PAINEL.md`: feedbacks de Davi → gates conferidos + onde estamos + próximo passo). `./kenhub-deck <slug-da-unidade> "<Módulo>" "<Submódulo>"` gera o deck final da unidade com **todos os gates duros** (cobertura 100% das estruturas, deck já instalado e dessuspenso, renderização do deck inteiro em PC e celular). Plano e tabela das unidades: [PLANO-UC07-NEUROANATOMIA-COMPLETA](flashcards/projeto/PLANO-UC07-NEUROANATOMIA-COMPLETA-2026-10-17.md); regras no MEMORY §15. Davi está sempre no Anki (MEMORY §1): nada de janela na tela dele. Depois de rodar, **olhar as folhas de contato** antes de entregar.

## Outras rotas (só sob pedido)

Índice do projeto: [README.md](README.md). Pedido explícito de “E1 + cards” (E1 + deck) inclui a E1: `didatica/E1.md`. Cadernos: `banco/CLAUDE.md` e `ROLES.md`. Typst: `typst-template/CLAUDE.md`. Site, liga e Etimologia: preservar.
