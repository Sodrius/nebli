# Auditoria de cobertura — corridas de 13–15/10/2026

Pedido de Davi em 15/10: “olha todas as aulas que tá faltando coisa, anota o que é e me dá um prompt pra mandar pro claude ajeitar e deixar a aula completa, como já deixamos outras; o nível tem caído”.

## Diagnóstico transversal

O problema principal é anterior à escrita dos cards: vários inventários foram feitos em granularidade de lâmina, com itens genéricos como “Tabela”, “Fluxo”, “Contexto”, “Exemplo” ou “Resumo”. Isso permite decidir uma lâmina inteira como “Tab” ou “ilustração” sem listar as informações e relações que ela ensina. Em outros casos, uma chave de card foi usada como cobertura de três a oito itens distintos; o gate comprova que há uma referência, mas não que cada alvo recuperável esteja realmente coberto.

A correção precisa reconstruir primeiro o inventário em granularidade de **informação/relação**, na ordem das fontes. Para cada item: card, Tab/Extra ou exclusão com motivo específico. Só depois selecionar ou escrever cards. Conferir novamente no Anki vivo; não aceitar `cobertura.json`, contagem ou gate como prova autônoma.

## Aula por aula

### Lacunas claras ou blocos sem recuperação suficiente

1. **10 Ação hormonal** — `deck-aula-uc03-bq10-acao-hormonal-2026-10-14`
   - Falta recuperar o mapa dos pontos em que uma resposta hormonal pode ser regulada: biossíntese → estocagem → secreção → transporte → reconhecimento → resposta → degradação. Hoje está apenas como Tab, embora seja o organizador da aula.
   - Falta o processamento geral de hormônio peptídico: pré-pró-hormônio/peptídeo sinal → pró-hormônio → clivagem no Golgi/grânulo → hormônio maduro; a insulina aparece como exemplo, mas o princípio não tem recuperação própria.
   - Falta a distinção GLUT-1/3 independentes de insulina × GLUT-4 regulado por insulina no próprio percurso da aula; hoje GLUT-1/3 foi relegado ao Tab. Pode ser compartilhado com o organizador já existente na UC21, sem duplicar nota.
   - Reavaliar RIA: se a aula exige reconhecer o princípio competitivo do método, precisa de card; se só nomeia a técnica, exclusão específica é aceitável.

2. **14 Declaração de óbito** — `deck-aula-uc03-pt14-declaracao-obito-2026-10-14`
   - A regra abstrata da Parte I existe, mas seis casos das lâminas 9–15 foram descartados como “ilustração”. Falta recuperação aplicada: ao menos dois casos sem resposta vazada para montar imediata → intermediária(s) → básica e separar condição contribuinte na Parte II.
   - O deck deve provar que o aluno consegue preencher a cadeia, não apenas recitar os nomes das linhas.

3. **08 Reconhecimento imune inato** — `deck-aula-uc03-im08-reconhecimento-inato-2026-10-14`
   - MyD88 e TRIF existem isoladamente, mas falta um organizador que integre receptor/adaptador → fator de transcrição → produto → função: MyD88 → NF-κB/AP-1 → citocinas inflamatórias; TRIF → IRF3/7 → IFN tipo I; inflamassoma → caspase-1 → IL-1β/IL-18 e piroptose.
   - O “resumo/produtos liberados” da lâmina 22 foi enviado ao Tab por receio de cloze em verbo; deve virar um card bem escrito, com cloze nos produtos/conjuntos, não ser excluído.

4. **20 MHC e apresentação de antígenos** — `deck-aula-uc03-im20-mhc-2026-10-14`
   - Há muitos cards pontuais, mas falta o mapa que liga localização do antígeno → via de processamento → classe de MHC → linfócito → resposta: citosólico/proteassomo/TAP/MHC I/CD8; vesicular/endossomo-Ii-CLIP-DM/MHC II/CD4.
   - As lâminas 9–27 foram quase todas classificadas genericamente como “contexto/Tab”. Reabrir esse bloco e discriminar quais relações são pré-requisito real para captura, apresentação e escolha do efetor; não aceitar “contexto” como motivo para um bloco inteiro.

5. **22 Mecanismos efetores imunes** — `deck-aula-uc03-im22-mecanismos-efetores-2026-10-15`
   - As etapas da fagocitose da lâmina 25 ficaram apenas no Tab. É mecanismo central e precisa de recuperação organizada: reconhecimento/adesão → englobamento/fagossomo → fusão com lisossomo → morte/digestão.
   - Integrar opsonização, explosão respiratória, MPO/ROS e NO ao fluxo, sem criar cards repetidos; hoje os componentes existem, mas a cadeia não é recuperada.

6. **40 Prática 3 — identificação bacteriana** — `deck-aula-uc03-mb40-pratica3-2026-10-15`
   - A árvore e a tabela de bancada (lâminas 18 e 20) foram mandadas ao Tab, embora a função da prática seja decidir o próximo teste. Faltam organizadores/algoritmos recuperáveis.
   - Criar mapa de escolha de coloração e meio a partir da amostra/hipótese; mapa dos cocos Gram-positivos (catalase → O/F/coagulase/novobiocina; hemólise → bacitracina/optoquina/CAMP conforme a aula); e mapa de quando usar cultura/bioquímica, sorologia, PCR/sequenciamento, MALDI-TOF e antibiograma/MIC.
   - Preservar os cards pontuais existentes e acrescentar somente os organizadores que dão sentido a eles.

7. **18 Recombinação V(D)J** — `deck-aula-uc03-bm18-recombinacao-2026-10-14`
   - A lâmina 25 sobre geração de clones autorreativos foi excluída como “tolerância é da imunologia”. Falta a consequência lógica do mecanismo: recombinação aleatória gera receptores potencialmente autorreativos, exigindo seleção/tolerância. Deve haver um card de conexão curto, sem transformar a aula em revisão de tolerância.

8. **15 Grand Round 1 — esquizofrenia** — `deck-aula-uc03-gr15-grand-round-1-2026-10-14`
   - O bloco 49–54 sobre estigma ficou inteiro sem recuperação. Se o professor o apresentou como objetivo, precisa ao menos de um card nuclear sobre como estigma prejudica procura de cuidado/adesão/participação social; se era encerramento ilustrativo, registrar evidência específica.
   - Rever as lâminas 37–46 para garantir um card integrador da sequência patologia sináptica → microglia/neuroinflamação → alteração de espinhas/sinapses; hoje há peças (`d-espinhas`, `d-il1`, privilégio/linfáticos), mas não está demonstrado que a relação inteira é recuperável.

### Cobertura quase completa, mas com organizadores ou relações a verificar

9. **11 Acúmulos e adaptação** — `deck-aula-uc03-pt11-acumulos-adaptacao-2026-10-14`
   - Reavaliar o mecanismo geral da atrofia: menor síntese proteica + maior degradação por ubiquitina-proteassomo/autofagia, antes dos mediadores e exemplos. As peças existem, mas o encadeamento pode não ter recuperação própria.
   - A classificação final dos pigmentos foi excluída porque cada pigmento tem card. Pelo feedback atual, isso não basta: criar organizador de mapa mental para exógenos/endógenos e situar antracose, lipofuscina, melanina, hemossiderina e bilirrubina.

10. **13 Envelhecimento celular e tecidual** — `deck-aula-uc03-pt13-envelhecimento-2026-10-14`
    - A lacuna de sarcopenia → creatinina baixa foi corrigida na revisão de 15/10. Confirmar no Anki vivo.
    - Reavaliar a tabela-resumo da lâmina 21 e a lista sistêmica da 12: se forem objetivos de comparação, um organizador por sistemas é necessário; não usar “itens principais têm card” sem conferir item a item.

11. **16 Regulação hormonal e massa corpórea** — `deck-aula-uc03-bq16-regulacao-hormonal-2026-10-14`
    - Leptina, resistência à leptina, AMPK e núcleo arqueado foram corrigidos e estão cobertos pontualmente.
    - Confirmar se há recuperação integrada de sinal periférico → neurônio do arqueado → mediador → fome/saciedade: leptina/insulina → POMC/CART → α-MSH/MC4R; grelina → NPY/AgRP. Se `d-arqueado` e `d-msh` não permitirem reconstruir a cadeia completa, acrescentar um organizador único.

### Sem lacuna de cobertura clara nesta passada; não inflar

12. **09 Lesão celular, necrose e apoptose** — cobertura longitudinal forte. Não acrescentar cards por quantidade. Corrigir, porém, dois problemas de conteúdo detectados pelo gerador de Tabs: Extra de Fas–FasL atribui seleção negativa tímica ao eixo errado; Extra de catalase/glutationa peroxidase mostra produtos químicos incorretos.

13. **12 Ressonância magnética** — fundamentos, T1/T2, gadolínio, segurança e técnicas estão cobertos; manter vigilância contra excesso de física. Não acrescentar sem lacuna demonstrada.

14. **17 Reconhecimento adaptativo** — estrutura, funções e classes de imunoglobulina estão cobertas após a associação do transporte de IgA. Confirmar card vivo, sem inflar.

15. **UC21 Caso 5 — insuficiência metabólica** — as 12 perguntas oficiais têm destino em card. Não há lacuna clara, mas há formulações vivas incorretas/gerais que precisam ser corrigidas: K sérico “tipicamente aumentado em qualquer DM1”; K intracelular “diminuído em qualquer DM1”; cortisol/glucagon/epinefrina tratados como se induzissem resistência por uma única fosforilação em Ser/Thr; “urina diluída” na diurese osmótica. Contextualizar em CAD e corrigir mecanismos antes de regenerar Tabs.

## Critério de encerramento

Para cada aula: inventário refeito em granularidade atômica; cada informação marcada para recuperação resolve para um card vivo; organizadores preservam o mapa mental; exemplos só ficam sem card quando realmente não acrescentam decisão/aplicação; ordem viva lida; cards compartilhados preservados; Tabs regenerados apenas depois; gates 100%. Registrar no relatório o que entrou e o que continuou fora, com motivo específico.
