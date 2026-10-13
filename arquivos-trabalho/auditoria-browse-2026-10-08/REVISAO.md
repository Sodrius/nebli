# Auditoria do plano e Browse — 08/10/2026

## Conclusão e alcance

A execução trouxe correções reais, mas os decks ainda não podem ser declarados completos ou integralmente revisados. A leva 1 permanece aberta. A reconstrução UC03 P3 → UC03 P2 → UC08 P2 ainda consta pendente. Auditoria pelo Codex, sem atribuir nova revisão ao Claude.

Consulta viva de 1.179 cards médicos / 15 decks físicos UC03 e UC08, via AnkiConnect no perfil User 1. Campos e IDs em `vivo.json`; base de Tabs lida somente para consulta. Contagens incluem cards preservados como substituídos/retirados; não são contagens de conteúdo aprovado. Revisão editorial dirigida aos achados abaixo, não revisão científica individual dos 1.179 cards. Slides locais de Morfologia consultados em texto; páginas 10 e 37 renderizadas e vistas. Browser real Anki 26.09.3 inspecionado por captura da própria janela.

## Avanços comprovados

12 recibos da leva 1: **137 notas únicas corrigidas, 20 cards dessuspensos**, sem divergências registradas nos readbacks. Isso comprova aplicação e conferência de campos na ocasião, não qualidade científica universal.

O card `nid:1791023364492` (canalículo intracelular) contém agora uma frente contextualizada e Extra específico, conforme a revisão mais recente de feedback2; não repeti a crítica antiga como se a correção não existisse. A inspeção de ordem ignorou como defeitos os seis cards sem tag de posição que estavam explicitamente substituídos/retirados.

## Defeitos reais

1. **Edema: 30/67 cards sem Tab salvo.** Os outros 37 existem em estilo anterior. Falta de Tab é distinta de estilo antigo: este último não comprova conteúdo médico errado. Evidência: `resumo.json` e coleção viva; `tab-gerar3.log` da leva registra interrupção por limite da sessão Claude.
2. **Ambiental: Extra genérico em 27 notas / 36 de 41 cards.** Repete “Connect the fact to inhaled pollutants and the tissue response described in this lesson”, sem explicar o alvo. Exemplo `nid:1791147086686` (afinidade do CO pela Hb). É defeito pedagógico/editorial, sem necessidade de alegar erro médico.
3. **Ambiental: duplicação literal.** `nid:1791147114714` e `nid:1791147095424`, ambos com um card, cobram exatamente a mesma exposição ao pó de carvão na pneumoconiose; Text e Extra idênticos. São notas distintas, não irmãos que cobram lacunas diferentes. Não removidos nesta auditoria.
4. **Morfologia: cobertura incompleta de recuperação.** Os slides 10 e 37 apresentam espirilos/espiroquetas/vibriões e distribuições de flagelos. Li as frentes dos 36 cards atuais: nenhum pergunta essas distinções/identificações. Os dois cards de flagelos perguntam corpo basal e motilidade; não substituem reconhecer a distribuição flagelar. Os slides foram renderizados em `morfologia-slide-10.png` e `morfologia-slide-37.png`. Presença eventual como figura/Extra não equivale a pergunta. A auditoria não certificou os demais blocos da aula.
5. **Browse efetivamente fora da ordem antes do ajuste.** AN01 estava ordenada por Deck; começava com posições 07, 30, 41... (`ui-before-order.json/png`). A implementação também podia ordenar por aula sem atualizar o cabeçalho, dependendo de “nebli” no texto da busca. Corrigido nesta sessão.
6. **Ordem de Fungos: posição 10 duplicada entre notas distintas**, `1791163035648` e `1791069773210`, em `ordem-tags.json`. Não escolhi uma posição pedagógica arbitrária; resolver na revisão de Fungos contra fontes/plano. Uma UI em ordem numérica não certifica a sequência pedagógica inteira.
7. **Fechamento/pipeline pendente.** `nebli.gates leva01` falha por ausência de fontes.json/plan.json nesse agregador de correções (0/2; não significa que todas as aulas careçam desses arquivos). O gate da corrida antiga de Ambiental aborta porque trata uma lista como dicionário em fontes. Registros em `gates-*.txt`; não há gate verde de entrega desta leva. Reconciliar esquema das corridas e critérios atuais, sem inventar evidências para passar.

## Browse implementado e verificado

- `J` substitui Ctrl+J na ação nativa de alternar suspensão, com foco na tabela. Seleção e desfazer continuam nativos.
- Coluna **Suspenso**, Sim/Não, independente da bandeira; em modo Notas, contagem de suspensos/total de irmãos. Enterrado não é confundido com suspenso.
- Ordem da aula passa a ser a coluna de ordenação padrão nas ordenações anteriores usuais. Cabeçalho e resultado concordam; clicar noutra coluna é respeitado.
- Ordem e suspensão ficam visíveis à esquerda. Captura final `ui.png`: linha com bandeira azul e “Sim”; bandeiras preservadas.
- Todos os **123 IDs de AN01** retornaram na ordem das tags, incluindo irmãos e compartilhados (`ui.json`). Isso comprova ordenação da interface, não revisão integral da sequência dos slides.
- **7 testes unitários passaram**. Teste Qt no Anki: J acionou a ação na tabela e digitou normalmente na busca. Sinais da ação bloqueados durante o teste para não suspender/dessuspender nenhum card; estado do botão e texto restaurados. Resultado `shortcut-test.json`. Código diagnóstico temporário removido; fontes usadas preservadas nesta pasta.
- Nenhum conteúdo, bandeira, suspensão ou agendamento de card foi alterado por esta auditoria. Ajustes carregados pelo add-on existente sem reiniciar o Anki.

## Melhorias prioritárias

Fechar os Tabs pendentes e revisar os alterados; substituir versos genéricos e retirar duplicação com preservação de histórico; voltar aos slides para conferir cada alvo e habilidade visual antes da reconstrução. Separar na entrega “aplicado”, “cobertura conferida”, “revisão visual”, “Tab atual” e “gate aprovado”. Não expandir alegação de qualidade com base só em recibo, número de cards ou coluna ordenada. Manter fila aprovada; auditoria não iniciou reconstrução pelo Codex nem mudou a prioridade do executor Claude.
