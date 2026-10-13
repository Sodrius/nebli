# O que orientar nos próximos decks — releitura de 28/09/2026

**Histórico desta rodada, superado pelos esclarecimentos posteriores:** 40 é apenas referência de calibração, sem meta de média/cota; cerca de 400 respostas totais/dia, cramming à parte, é referência flexível. Story teller ensina e relembra, sem exigir caso/narrativa. Tradução preserva tudo e fica para próximas aulas. Ver [respostas](RESPOSTAS-2026-09-28.md), README/CONTRATO/BANDEIRAS/TRADUCAO/ESTILO e F-C35–39; não executar interpretações antigas deste registro.

Registro desta revisão, não outra política. Critérios ativos em `flashcards/projeto/README.md`, `BANDEIRAS-E-PROGRESSAO.md`, `CONTRATO-DE-QUALIDADE.md` e `TRADUCAO-DOS-CARDS.md`. Feedback novo registrado uma vez, F-C28–30.

## Fontes recuperadas

- [Documento indicado por Davi](https://docs.google.com/document/d/1gHGICvzQMe_B5CJFPAKwo6SvtIjcqEwBPCV5v-dBhD0/edit?tab=t.0), título atual **pipeline criação de cards**, aba t.0, lido pelo conector. O conteúdo atual é uma lista de ajustes/feedbacks; não contém sozinho toda a arquitetura inicial.
- `arquivos-trabalho/arquitetura-nebli-decisoes-2026-09-22.md`: 37 decisões/respostas da construção inicial, com o mesmo documento como origem.
- `arquivos-trabalho/calibracao-escala-2026-09-23/RESPOSTAS-ORIGINAIS.md`: 30 perguntas e respostas literais, incluindo os “não entendi” e as condições para escalar.
- Documentação atual, FEEDBACKS e recibos da manutenção de 28/09; planos históricos usados como evidência, não comandos de execução.
- Histórico local disponível das sessões deste workspace consultado de forma delimitada. Não foi recuperado todo o histórico de outros computadores; preferências não foram inventadas para preencher ausências.

## Entendimento que precisa sobreviver a esta conversa

Você quer aprender o conteúdo da aula com profundidade e construir base médica durável, com pouca fricção para estudar. Seleção ruim e cards ruins eram os problemas centrais desde 22/09. A direção atual está funcionando; o pedido é aperfeiçoar decisões e acabamento, preservando o que já está bom.

“É melhor ter o card” expressa disponibilidade de conteúdo pertinente. Não obriga revisar tudo por anos. A bandeira verde precisa ser uma recomendação confiável de assumir esse compromisso; azul conserva aprendizagem/prática válida. O núcleo pode ser grande quando a aula realmente concentra fundamentos, ou muito pequeno quando há pouco ganho longitudinal. Contagem de slides, tamanho do deck e uma média entre aulas não decidem isso.

Um bom card permite recuperar um alvo claro, com contexto suficiente, e o verso ajuda a compreender/lembrar. Uma explicação completa pode estar na E1 ou no verso; isso não exige uma frente para cada frase. Uma pergunta de identificação pode ser excelente sem cobrar um mecanismo. Em anatomia, reconhecer a estrutura certa na imagem certa já é uma habilidade importante.

| Tema | Entendimento vigente e origem |
|---|---|
| Escopo | Aula delimita os alvos; fontes aprofundam esses alvos. Exemplo clínico não vira uma aula sobre a doença. F-C01/F-C15 e reprovação do piloto de Edema continuam centrais. |
| Tamanho | Deck do tamanho necessário para ser bom. Nada de orçamento por dias até prova ou número fixo de cards. Núcleo e seleção completa têm tamanhos próprios. F-C18/F-C21/F-C28. |
| Importância | Steps, residência e formação geral orientam; anatomia/fisiologia têm valor especial como base. Importância precisa ser atribuída ao que o card recupera. Pedido atual, BANDEIRAS. |
| Busca | Reutilizar a identidade NEBLI; depois AnKing, outros acervos adequados, autoria excepcional. Muitos autorais pedem revisar busca/recorte. Q10/Q11, README. |
| Anatomia | AnKing → outros de anatomia → AnatoKing; várias práticas permitidas, um representante verde por estrutura do núcleo; imagem legível e alvo correto. F-C23/F-C24. |
| Autoria e verso | Frente focal e fluida; explicação curta visível, apoio maior pertinente recolhível. Não aumentar o verso como forma de compensar uma pergunta ruim. Q17/F-C22. |
| Idioma | EN + apoio PT era a decisão anterior. O pedido novo é arquitetar PT-BR de qualidade. Mantém-se a escolha de não duplicar revisão por idioma. F-C29; decisão 8 de 22/09 e Q19/Q20. |
| Identidade e compartilhados | Um card, um histórico, várias associações por aula. Q18/Q22 tiveram “não entendi”: não são aprovação de uma interface específica. A seleção acessível de compartilhados ainda precisa de validação. |
| Pós-prova | Cor não suspende automaticamente. Pausa automática do plano inicial foi substituída por decisão pessoal. Q25 não fechou a interface futura. |
| Rotina | 400 respostas totais/dia, cramming à parte. Não 400 novos nem regressão silenciosa aos 35/150 novos de decisões antigas. Macros ABNT2 adiadas. F-C25. |
| E1 | Continua junto dos cards, mesmo que a leitura seja opcional para Davi. Ajuste do tamanho da E1 está em outra conversa; esta rodada não modifica didatica/E1 nem seu verificador. |
| Autonomia | Executor procura fontes, corrige e verifica; Davi refina preferências, não faz fiscalização card a card. Perguntar somente ambiguidades novas relevantes. F-C17, Q29/Q30. |
| Escala | Pequenos lotes, origens/tipos variados e experiência real de estudo. Transferir contexto para Claude é parte do sucesso, não basta funcionar nesta conversa. Q28/Q30. |

## O que esta rodada tornou concreto

- Substituiu a referência ~50 verdes por núcleo derivado de alvos. Incluiu conferência de cobertura essencial, excesso de verdes e ganho de recuperação própria. Não definiu novas cotas ou pontuação automática.
- Tornou explícito o limite da manutenção anterior: `bandeiras.py` usava motivos amplos por grupo para parte dos verdes. As 144 mudanças anteriores não provam que cada aula já tem o núcleo delimitado pelo critério atual. Recibos antigos preservados; nenhuma migração geral executada para maquiar essa diferença.
- Especificou tradução por versão da cópia NEBLI, preservação de identidade, terminologia, clozes, irmãos, imagens e edições pessoais. Separou tradução, correção científica e edição didática.
- Preparou `amostra.json` e `amostra.html`: seis notas vivas, nove cards, incluindo mecanismo, contraste, sinal clínico, c2, quatro irmãos e AnatoKing. Inglês atual e proposta PT comparáveis, com estados/limites. Dados de cards ficam em artefatos ignorados pelo Git.
- Atualizou a rota de leitura, contrato, execução e handoff; retirou a referência concorrente de volume da fila. Corrigiu referência operacional obsoleta de 150 novos como se ainda fosse o valor atual. Preservou as respostas antigas e backups.

## Limites e próximo uso

Somente leitura no Anki e no Google Doc nesta rodada; sem tradução/recoloração aplicada, suspensão, mudança de agendamento ou publicação. A amostra confere marcadores simples e mantém a mídia, mas não prova geração de cards no Anki nem funcionamento no tablet. A página comparativa não é template de estudo.

Na próxima aula atribuída, delimitar objetivos com as fontes; justificar seu núcleo; selecionar os melhores cards; conferir imagem e fluidez. Para tradução, começar com o piloto delimitado e os critérios da arquitetura, não usar `amostra.py` como tradutor universal. Não iniciar uma aula nova por causa deste registro. Manter pendências de sanguessugas, opções, progressão e tutor em suas frentes próprias.
