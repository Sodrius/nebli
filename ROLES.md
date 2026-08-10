# ROLES.md — produção central, revisão independente

## Sessão principal

É a única produtora. Mantém o contexto completo e executa o fluxo inteiro:
fontes → cobertura → E1 → aprofundamento Step 1 → curadoria → visual/IO →
autoria de lacunas → APKG → correções → entrega.

Mantém `CHECKPOINT-<slug>.md` com fase, decisões, pendências e próximo passo.

## Revisores

Revisores recebem artefatos já produzidos, trabalham em modo somente leitura e
retornam achados. Não redigem E1, cards ou manifestos e não aplicam patches.

### Revisor de cobertura

Compara slides/objetivos, E1, contrato e deck. Procura omissões, assunto
adjacente, profundidade Step 1 inadequada, card órfão e lacuna nuclear.

### Revisor de cards e visual

Procura falta de atomicidade, indução, Extra ruim, autoral desnecessário,
imagem irrelevante, vazamento, máscara incorreta e escolha errada entre IO,
prompt visual e imagem explicativa.

### Auditor do APKG

Confere estrutura, GUIDs, note types, mídia, referências, renderização e IO do
arquivo final. O veredito técnico não substitui a decisão da sessão principal.

Detalhes: `docs/canon/REVISAO.md`.
