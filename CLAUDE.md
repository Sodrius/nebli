# NEBLI — entrada de toda sessão

1. [ESTADO-ATUAL.md](ESTADO-ATUAL.md) › **Retomar aqui** e **Quem está com o quê**: o que fazer agora e o que outro executor já pegou.
2. [MEMORY.md](MEMORY.md): **a regra única e vigente** do que Davi quer (reorganizada em 13/10; versões antigas em `arquivo/` não são norma). Das [FEEDBACKS](flashcards/projeto/FEEDBACKS.md), ler só as entradas novas desde a última sessão.
3. Para fazer um deck: **[PIPELINE DE GERAÇÃO DE DECK v5](flashcards/projeto/EXECUCAO-DECK-AULA.md)** — pipeline único e fixo (E0 abrir → E1 ler todo o material → E2 compreender a aula → E3 planejar → E4 buscar nos acervos → E5 montar → E6 instalar e ler o vivo → E7 fidelidade ao slide → E8 entregar), sem pular etapa. Mudança no jeito de fazer deck = mudar a etapa certa desse pipeline (seção “Como mudar o pipeline”), nunca criar processo paralelo.

## Pedido curto

“Faz a aula X”, “continua”, `/deck-aula X` ou só o nome da aula = executar o roteiro inteiro até o deck entregue (instalado **sem Tab**, gates duros 100%, pacote da UC, sync) e relatar no formato do MEMORY §11. Sem agente, sem plano para aprovar, sem pedir permissão, sem parar no meio. **Desde 16/10 noite (F-20261016-CLAUDE-11): rodar as aulas em sequência, cada uma pelo pipeline inteiro, até Davi pedir para parar**; feedback que chegar é aplicado antes do deck seguinte. Plano vigente: [PLANO-ANKING-PRIMEIRO](flashcards/projeto/PLANO-ANKING-PRIMEIRO-2026-10-15.md).

- **O deck segue o slide (F-20261022-CLAUDE-06, gate duro):** depois de ler todo o material e antes de buscar, responder em `compreensao-aula.json` o que a aula ensina, onde se encaixa, o que lembrar e o que o professor ensina em cada bloco de lâminas; o deck nasce disso, o exemplo clínico vem depois do princípio e nunca vira carro-chefe, e a revisão final confere bloco a bloco a fidelidade ao slide.

## Limites que não mudam

- Davi estuda no Anki enquanto o executor trabalha: nunca tocar a nota em tela nem irmãos; escrita só por `nebli.decks.escrita()`; sync quando ele estiver ocioso.
- Outro executor (Codex) trabalha em paralelo: reivindicar a aula no ESTADO-ATUAL antes; não mexer no que ele reivindicou; reler antes de gravar.
- Preservar originais AnKing, IDs/histórico, comentários, marcas e suspensões pessoais. Não apagar notas sem autorização de Davi e backup. Arquivar documentos superados em `arquivo/` com hash.
- Feedback novo: literal em FEEDBACKS → regra **reescrita no lugar** no MEMORY (sem acrescentar camada) → check no lint/gate quando mecanizável.
- Não fabricar leitura, busca, teste ou revisão. Gate aprovado não prova julgamento.
- **AnKing-primeiro com gates duros** (MEMORY §5): busca nos três caminhos em todos os acervos, `busca/cobertura.tsv`, autoral só para lacuna provada depois de buscar em AnKing e todas as Referências Externas (sem teto desde 22/10), **todo AnKing do conteúdo da aula entra, sem teto de cards** (`PIPELINE_VERSAO = 5`, `SECOES_DA_AULA`) e relido contra os ANTI-EXEMPLARES. O `apply` recusa instalar sem isso.

## UC07 / Kenhub (neuroanatomia)

**Toda sessão da UC07 começa por `./kenhub-deck --painel`** (gera `flashcards/projeto/UC07-PAINEL.md`: feedbacks de Davi → gates conferidos + onde estamos + próximo passo). `./kenhub-deck <slug-da-unidade> "<Módulo>" "<Submódulo>"` gera o deck final da unidade com **todos os gates duros** (cobertura 100% das estruturas, deck já instalado e dessuspenso, renderização do deck inteiro em PC e celular). Plano e tabela das unidades: [PLANO-UC07-NEUROANATOMIA-COMPLETA](flashcards/projeto/PLANO-UC07-NEUROANATOMIA-COMPLETA-2026-10-17.md); regras no MEMORY §15. Davi está sempre no Anki (MEMORY §1): nada de janela na tela dele. Depois de rodar, **olhar as folhas de contato** antes de entregar.

## Outras rotas (só sob pedido)

Índice do projeto: [README.md](README.md). Pedido explícito de “E1 + cards” (E1 + deck) inclui a E1: `didatica/E1.md`. Cadernos: `banco/CLAUDE.md` e `ROLES.md`. Typst: `typst-template/CLAUDE.md`. Site, liga e Etimologia: preservar.
