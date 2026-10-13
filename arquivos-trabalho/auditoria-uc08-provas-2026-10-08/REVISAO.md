# UC08: decks vivos × provas TA/TB e pipeline

Auditoria paralela à execução do Claude; nenhum card foi escrito, suspenso, dessuspenso ou reordenado nesta análise. Os PDFs TA (17 páginas) e TB (19 páginas) foram copiados do Drive com origem e SHA-256 em `fontes.json`; as 36 páginas foram examinadas visualmente e OCR guardado ao lado. São provas P1, sem ano confirmado no documento; portanto servem para medir correspondência com o conteúdo cobrado, não para estimar nota ou certificar a P2.

## Veredito

Os decks UC08 vivos cobrem bem os alvos centrais de anatomia e histologia que aparecem nas duas provas. A cobrança coincide de modo concreto em esôfago, estômago, papila duodenal, vasos retos, tênias, válvula ileocecal, linha pectínea, troncos arteriais, túnicas e células gástricas/criptas. Não dá para concluir que os decks “garantem a prova”: as questões pedem identificação em figuras e justificativas integradas, e não renderizei todos os cards correspondentes. A fisiologia tem três lacunas claras quando comparada às perguntas e aos slides da aula.

## Cobertura observada

TA e TB repetem grande parte dos temas anatômicos com variação de segmento/estrutura. Em cada uma há 10 questões de anatomia com subitens de identificação e caracterização, 8 de histologia e 2 de fisiologia. As linhas abaixo tratam os subitens como parte da questão, sem inflar a contagem.

| Bloco cobrado | Deck vivo correspondente | Avaliação |
|---|---|---|
| Esôfago torácico (TA) / abdominal (TB), caracterização e posição | 1790972064584; 1790972064705; 1790972064784 | Alvos presentes. |
| Cárdia (TA) / piloro (TB), identificação e anatomia funcional | 1790973213781; 1790972066759; 1790972067059; 1790972067160 | Alvos presentes. |
| Papila duodenal maior e abertura dos ductos | 1790972069112; 1790972069210; 1790973220806 | Alvo presente. |
| Vasa recta curtos no íleo (TA) / longos no jejuno (TB) | 1790973222133; 1790973222856; 1790972067059 | Comparação está nos cards/Extra. A identificação em imagem merece inspeção visual própria. |
| Tênia livre e camada longitudinal | 1790974690979; 1790974693656; 1791023303592 | Alvos presentes; há também relação cirúrgica com apêndice. |
| Lábio ileocecal inferior (TA) / superior (TB) | 1790974692455; 1790974692579 | Ambos presentes. |
| Linha pectínea e significado anatômico | 1790974696505; 1790974697280; 1790974697531; 1790974697657; 1790974698156 | Alvo presente, incluindo origem embrionária e territórios acima/abaixo. Não usar a resposta marcada na prova como fonte do conteúdo. |
| Artéria gastroduodenal e irrigação (TA) / tronco celíaco e ramos (TB) | 1790981514577; 1790981516405; 1790981517780; 1790981513225; 1790981513853 | Alvos presentes. |
| AMS, órgãos/território e ramos; AMI, órgãos/território e ramos | 1790981513351; 1790981520801; 1790981521328; 1790981522203; 1790981513476; 1790981523653; 1790981524153 | Alvos presentes. |
| Fundo/corpo versus antro/piloro: fossetas, glândulas e epitélio | 1790979865684; 1790979866060; 1791023360920; 1790979866562; 1790979867432 | Correspondência boa; há cards de imagem e distinções morfológicas. |
| Células parietais/principais, HCl e pepsinogênio | 1790979867432; 1790979867685; 1790979867810; 1790979869285; 1790979869685 | Correspondência direta. |
| Intestino delgado versus cólon: vilosidades, criptas, epitélio e lâmina própria | 1790980916154; 1790980916029; 1791023301992; 1790980915404; 1791023294400 | Correspondência boa. |
| Componentes segmentares (células caliciformes, absortivas, Paneth, glândulas de Brunner, placas de Peyer) | 1791023297542; 1791023296668; 1790980912277; 1790980913728; 1790980914730 | Componentes distribuídos em cards, não numa lista única. Isso é adequado; a prova é uma matriz de identificação. |
| Muscular circular, plexo mioentérico e serosa em lâmina | 1790979864907; 1790979863784; 1790979863660; 1790979865684 | Conceitos presentes; conferir se a figura/campo do card permite localizar a mesma estrutura da prova. |
| Esôfago: epitélio, submucosa e adventícia | 1790979863287; 1791023357791; 1790979863784 | Correspondência direta. |
| Criptas: células-tronco e descendentes secretoras/absortivas | 1790980910905; 1790980911405; 1790980911781; 1790980912277 | Conceitos presentes; a relação completa entre as duas linhagens está distribuída, não cobrada num único prompt. |
| Deglutição: eventos motores coordenados, fase faríngea, esfíncter esofágico superior | 1790999834254; 1790999834379; 1790999834629; 1790999834753; 1790999835129; 1790999835252 | **Parcial.** Os elementos estão espalhados, mas não há prompt que recupere a sequência completa exigida pela questão TA. O slide FI09 p. 6 lista relaxamento do EES, passagem do bolo e contração/reconstituição do esfíncter. |
| Motilidade gástrica/pilórica, mistura e feedback duodenal | 1790999835379; 1790999271207; 1790999835629; 1790999835754; 1790999836003; 1790999836779 | Núcleo presente. **Integração parcial:** a pergunta TB exige correlacionar padrão motor, processamento do quimo e controle neural/hormonal; os mecanismos estão em cards separados e o GIP é cobrado pela fonte, sem prompt focal de sua relação com esvaziamento. |
| Ondas lentas, limiar elétrico/contrátil, potencial em espícula e força | 1790999832404; 1790999832528; 1790999833029; 1790999833204; 1790999833329 | **Parcial e prioritário.** Há onda lenta, limiar elétrico, espículas e força; falta explicitar a distinção entre limiar elétrico e contrátil que aparece no slide FI09 p. 3 e na questão-modelo fotografada na TB. O Extra do 1790999833029 (“slow waves alone do not cause contraction”) precisa ser reconciliado com a formulação da aula para não ensinar uma simplificação conflitante. |
| Motilidade colônica e defecação, TA | 1790999838053; 1791052303773; 1790999838304; 1790974694881; 1791052036733 | **Parcial.** Movimentos de massa, distensão retal, reflexo pélvico e esfíncteres estão cobertos; slide FI09 p. 13 também inclui contração de músculos abdominais e respiratórios na evacuação voluntária, sem card focal identificado. |

A comparação não usa as alternativas assinaladas pelos alunos como gabarito. Na TB, as páginas 18–19 incluem imagens de uma explicação do professor (2020) sobre ondas lentas; elas sustentam somente aquele ponto específico. A TA/TB tem divergências em respostas manuscritas/anotadas para as quais não encontrei gabarito oficial.

## Ajustes recomendados nos decks UC08

1. Criar/associar cards de recuperação para a sequência motora completa da deglutição, com foco no EES e na coordenação da fase faríngea (slide FI09 p. 6).
2. Tornar explícitos limiar elétrico versus limiar contrátil e relacionar espículas/entrada de Ca²⁺ à força, conforme FI09 p. 3 e a questão-modelo da TB. Revisar a frase do Extra do 1790999833029 contra a aula antes de alterá-la.
3. Completar defecação voluntária com musculatura abdominal/respiratória, respeitando o recorte do slide FI09 p. 13.
4. Rever a explicação integrada do esvaziamento gástrico para que o aluno consiga encadear retropulsão, piloro e feedback duodenal. Só criar card hormonal se a aula cobrar mecanismo específico ausente; o alvo imediato é integração, não decorar lista maior.
5. Na revisão visual por Claude, exigir teste dos cards de anatomia/histo com a pergunta “consigo localizar a estrutura na imagem sem depender da legenda já impressa?”. Este relatório mapeou IDs/textos e examinou imagens das provas, mas não renderizou os 695 cards elegíveis um a um.

## Problemas de pipeline demonstrados no código/testes

A suíte local executada nesta auditoria teve 94 testes: 90 passaram, 3 falharam e 1 deu erro. São avisos de regressão/expectativas, não prova de defeito nos cards vivos:

- `test_e1_mode`: diferença entre caminhos `/private/Users/...` e `/Users/...` no macOS. Ajuste: normalizar caminhos reais no teste.
- `test_entrega`: o teste espera comportamento antigo de exportação; a implementação atual copia entregas. Atualizar o teste para o contrato aprovado, sem reverter o código por causa do teste.
- `test_handoff`: espera “E1 + cards” no texto de entrada, embora a entrega padrão agora seja só deck. Atualizar fixture/expectativa.
- `test_explicacoes`: mock da API não cobre `notesInfo`; completar o mock e manter teste de integração isolado.

Achados de desenho/código que merecem correção antes de declarar o pipeline robusto:

- `nebli.gates.drive_checks()` (linha 517) só verifica existência dos arquivos do Drive; um deck ou slide velho/vazio passa. Acrescentar hash/versão esperada e checagem mínima de conteúdo/metadados.
- `nebli.gates.MAX_IDENT_HISTO = 0.25` (linha 30), aplicado no gate de plano, conflita com a regra vigente em MEMORY para UC02, que não tem teto de 25% para identificação. Parametrizar o critério por plano/UC e deixar clara a evidência da aula, sem relaxar automaticamente outros gates.
- `nebli.reconcilia` preserva divergências de campos, mas não reconcilia mudanças de tags de retirada/suspensão. `nebli.delta` suspende retiradas e altera tags de ordem. Antes de rebuilds, incluir um diff explícito de tags/estado e exigir decisão idempotente para que remoções e correções vivas não sejam ressuscitadas.
- `nebli.decks.escrita()` adia sync se `guiCurrentCard` existe, mas o bloco não impede a escrita. `nebli.corrige` exclui a nota visível no início; `nebli.delta` não consulta a nota visível e entra na escrita com sync padrão. Uniformizar a proteção por lote: ler card visível imediatamente antes de aplicar e adiar nota/irmãos, mantendo `sync=False` enquanto Davi revisa.
- Gate aprovado mede itens codificados, não prova completude semântica, qualidade de figuras ou se o card pede a habilidade da prova. Fazer a entrega manter uma tabela de alvo→card→fonte e uma amostra visual por objetivo; não reportar apenas percentuais agregados.

Este relatório é diagnóstico. As lacunas indicadas ainda não foram aplicadas no Anki nem incorporadas às specs enquanto Claude executa o plano.
