# UC19 P1 — estado da refação em 06/10/2026

Pedido: primeira aula completa, AnKing-first, história mínima, mecanismos gerais e exemplos clínicos proporcionais; slides + Ninja Nerd + Outros + Rang & Dale; Tabs e Anki; sem E1.

**Instalado no Anki:** deck `NEBLI::UC19::P1::Farmacologia::Introdução à farmacologia e mecanismos de ação`, tag `NEBLI::UC19::P1::FA01`. A refação contém 110 notas/142 cards, 120 cards AnKing Step, 1 Referências Externas, 21 autorais (14,8%), 72 verdes, 68 azuis, 2 rosas. `receipt.json` confirma readback sem divergência. A versão antiga foi preservada como `plan-v1-reprovado.json` e `receipt-v1-reprovado.json`. O deck antigo já não estava no Anki antes desta instalação, então não houve exclusão.

**Não concluído:** 142/142 Tabs faltam. O gerador da assinatura retornou limite semanal, reset previsto para 08/10 às 12h (São Paulo). NÃO reaproveitar `tabs_local.py`: é fallback genérico rejeitado pelo usuário. O gate `python3 -m nebli.gates . --sem-drive` passou 40/49 e NÃO aprova entrega. Pendências: cobertura.json item a item, revisão-inventario, revisão-final card a card, duplicações autorais `drug_medication` e `adme`, campo `motivo` das cores, REVISAO-DE-QUALIDADE.md, Tabs, pacote Drive. Não afirmar conclusão até passar gate.

Fontes e objetivos: `fontes.json` e `planejamento.json` foram registrados; `--fontes` passou. `inventario-aula.json`: 69 slides, 195 itens de conteúdo + 10 itens de objetivos/exercícios. Plano atual `plan.json`, especificação `refacao_spec.py`, gerador `refacao_build.py`. `busca-externos.md` e o lint autoral documentam busca e forma AnKing. O cap. 2 de Rang foi extraído em `fontes/rang-cap2.txt`; provas pertinentes em `fontes/prova-farmacodinamica.txt`; DeNucci introdutório em `fontes/denucci-introducao.txt`.

Ao continuar, respeitar o pedido de economia de tokens: priorizar finalizar Tabs e auditoria sem recomeçar seleção, a menos que uma falha semântica concreta exija correção. Revisar exemplos clínicos e a integridade de cada cópia antes de declarar pronto.
