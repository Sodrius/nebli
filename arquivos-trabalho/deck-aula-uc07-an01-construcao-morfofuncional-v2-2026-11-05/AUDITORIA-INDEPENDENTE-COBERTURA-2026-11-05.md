# Auditoria independente de cobertura — AN01 v2

O deck entregue não demonstra cobertura integral das relações básicas das 24 lâminas mais a bibliografia de introdução. Isso não implica que todo IO regional deva entrar na AN01. Há recuperação de muitos conceitos celulares, mas faltam estruturas explícitas e relações; algumas foram substituídas por nomes de regiões, rótulos no verso ou explicações no Extra. Há Kenhubs pertinentes já exportados que não foram selecionados. Portanto, não sustento o fechamento anterior como cobertura completa.

## Orientação vigente de Davi e disposição dos achados

Durante esta auditoria, Davi esclareceu: **“o básico entra agora, io mt aprofundado entra no deck próprio de cada aula, mas no fim temos que garantir que cobrimos tudo com qualidade”**. Esta orientação prevalece sobre uma leitura de que todo rótulo das lâminas é obrigatório na AN01.

A tabela abaixo é inventário de diferenças **da versão entregue contra as fontes**, e não uma ordem para inserir todos os IOs agora. Disposição vigente:

- **Básico para AN01:** composição geral e grandes estruturas; identidade/direção das raízes e ramos; cinzenta/branca/cornos; núcleo craniano como agregado central motor ou sensitivo; reconhecimento global de bulbo/ponte/mesencéfalo nos cortes; grandes relações estruturais e funcionais; mecanismos introdutórios da bibliografia e interpretação elementar dos métodos.
- **Destino regional, sem cobrança de IO profundo agora:** localização individual dos núcleos III/VI/XII e demais cranianos, tegmento/pedúnculos/oliva e detalhes de cada corte, colículos e comparação precisa de seus níveis, caudado/putâmen/pálido isoladamente. Registrar destino para aula03/04 e confirmar sua cobertura lá. Estes itens **não** são bloqueadores próprios da AN01 sob a última orientação.
- **L11 parcialmente regional:** cápsula interna, corpo caloso, ventrículo lateral e grandes regiões são básicos; individualizar todos os núcleos profundos não é exigido agora. A categoria “núcleos profundos” já tem recuperação geral.
- **L12 parcialmente resolúvel por conceito:** não exijo os três IOs cranianos de exemplo. O déficit atual é o eixo motor/sensitivo e a distinção núcleo central/nervo/gânglio; a localização fina fica no destino regional.
- **L13 regional em sua maior parte:** os três cortes globais atuais são recuperação básica válida. Seus marcos específicos e o segundo nível mesencefálico devem ser rastreados para a aula própria, sem serem considerados já entregues pelo nome global.
- **L20:** não exige IO de toda região da rede agora nem catálogo funcional hipocampo/amígdala/núcleos da base. O exemplo básico dos quatro papéis é proporcional; a cobertura regional futura deve receber os demais rótulos relevantes.
- **L24:** o princípio reflexo/integração/consciência é introdutório; a classificação formal segmentar/suprassegmentar pode ter destino posterior se o mapa do curso explicitar onde será cobrada. Não converter o livro inteiro em obrigação automática desta primeira aula.

Assim, “adiado com destino” não significa “coberto” nem “excluído do curso”. O fechamento precisa de duas conferências: qualidade/completude do básico agora e cobertura efetiva dos conteúdos destinados às aulas seguintes ao fim do curso.

## Escopo e evidência

Revisão somente de leitura de `plan.json` (60 entradas mais 26 compartilhados), `curadoria.json`, `visuais-reuso.json`, `inventario-aula.json`, `busca/cobertura.tsv`, exclusões do plano, `candidatos-vivos.json`, resultados de `busca/anking.txt`, e fontes abaixo. Não consultei nem escrevi o Anki. Não gerei cards.

- As 24 lâminas foram vistas nas quatro folhas `visual/folha-01.png` a `folha-04.png`; ampliei também as páginas 15 e 16 do PDF original em `/tmp/nebli-an01-audit-slide-15.png` e `...16.png`.
- Li `fontes/veteranos-introducao.txt`, PDF13–19, integralmente. Confrontei trechos pertinentes de `livros/machado-cap1-3.txt`: filogênese/reflexos, formação do tubo e suas cavidades, migração/diferenciação, divisões do SN, classificação neuronal, fluxo axoplasmático, sinapses, glia e nervos. Consultei também `machado-recortes-figuras.txt`, `machado-cortex-conferencia.txt` e `fontes/limites-e-divergencias.md`.
- Inspecionei as imagens-base Kenhub de cápsula interna, corpo caloso, tálamo, diencéfalo, ponte, bulbo, mesencéfalo e ventrículo lateral, presentes em collection.media. São alvos destacados reais; não apenas nomes de notas.
- A lista nova `auditoria-2026-11-05/selecao-kenhub.json` contém 41 propostas. Distingui essa proposta da versão entregue: ela ainda não prova aplicação nem cobertura das relações. Não auditei visualmente todos os 41 overlays.

Critério: uma frente precisa induzir a estrutura/relação em questão, ou uma figura efetivamente ocultar/pedir o alvo. Campo `alvo`, rótulo legível em figura do verso e texto do Extra não contam, sozinhos, como recuperação.

## Lacunas concretas da versão entregue

| ID | Fonte e localizador | Relação/estrutura faltante | O que o plano realmente recupera |
|---|---|---|---|
| L01 | Lâmina3; veteranos PDF13 cap2; Machado cap2 §2.2.3, PDF21, linhas626–643 | Mapa cavidade embrionária→canal central/aqueduto/III/IV/ventrículos laterais, incluindo continuidade aqueduto III↔IV e revestimento ependimário | Vesículas e derivados adultos, sem cavidades nas frentes. Exclusões1479351805802/1479351825915/1479353800465 adiam explicitamente para líquor; isso deixa a bibliografia descoberta agora. |
| L02 | Veteranos PDF13–14 cap2; Machado cap2 §3.1–3.3, PDF21–22 | Glia radial como suporte à migração cortical; cone de crescimento guiando axônio ao alvo; eliminação de neurônios/sinapses em excesso e refinamento funcional | Nenhuma frente de migração, orientação axonal ou refinamento. Origem SNC/SNP não recupera esses processos. |
| L03 | Lâminas4–5; Machado cap3 §1.2 e §1.7.2.4, PDF30/38 | Recepção e integração de entradas múltiplas, com disparo condicionado ao limiar; diferença entre potencial pós-sináptico e potencial de ação | Dendritos=receber, soma=metabolismo, axônio=saída. Integração e condição de disparo aparecem em Extras, sem serem cobradas. |
| L04 | Lâminas7–8; veteranos PDF16 cap4; Machado cap3 §1.7.2.4, PDF37–38 | Cadeia completa: entrada de Ca²⁺→fusão/exocitose→receptor pós-sináptico→resposta graduável excitatória ou inibitória | `liberacao-sinaptica` termina em liberar neurotransmissor. A resposta pós-sináptica, receptor e influxo/fusão só estão no Extra. Não significa que cada passo precise de nota isolada. |
| L05 | Lâmina8; Machado cap3 §3.2, PDF42 | Condução contínua na fibra amielínica versus regeneração nodal na mielínica; ausência de mielina não significa ausência de Schwann no SNP | Saltatória e C=amielínica são cobrados; o modo contínuo e suporte de Schwann amielinizante são somente explicações. |
| L06 | Lâmina9, título e tabela | Relação maior diâmetro/maior mielinização→maior velocidade e ordem relativa I/Aα > II/Aβ > III/Aδ > IV/C | Modalidades e correspondências de nomes são cobradas; C=fina/amielínica é um extremo. Não há recuperação do eixo causal ou da ordem completa de velocidades. Não proponho mecanicamente transformar cada faixa numérica em lacuna. |
| L07 | Lâmina10; veteranos PDF15 cap3; Machado cap3 §1.5, PDF33 | Exemplos situados: bipolar na retina/gânglio espiral, pseudounipolar em gânglio sensitivo; ambos os ramos pseudounipolares são axonais | `morfologias` cobra contagem/disposição; `pseudounipolar-trajeto` cobra soma fora do percurso. Nenhum liga tipo à localização nem exige identidade axonal dos dois ramos. |
| L08 | Lâmina11; veteranos PDF17–18 cap5; Machado cap2 §1.2, PDF26 | SNA como componente **eferente** do visceral, distinto da aferência visceral; efetores liso/cardíaco/glândulas | Um organizador de via pré/pós-ganglionar e outro de nomes simpático/parassimpático/entérico não cobram a definição SNA=eferência visceral. O Extra contém a distinção. Somático→esquelético está coberto. |
| L09 | Lâmina12 | Localizar raiz posterior/anterior, ramos anterior/posterior e sua continuidade com nervo e gânglio | Há raiz anterior/posterior em texto e gânglio/nervo em IO. Não há identificação visual das raízes/ramos. Nervo misto não substitui a topografia de cada estrutura. |
| L10 | Lâmina13; veteranos PDF18 cap6 | Ponte, bulbo, mesencéfalo e diencéfalo nas vistas; orientação anterior/posterior/medial; lobos e sulco central | IOs de encéfalo, cérebro, cerebelo e medula nomeiam regiões maiores. O organizador do tronco enumera três nomes, sem exigir encontrá-los em vista anatômica. |
| L11 | Lâmina14, título e cortes; lâmina22 | Cápsula interna, corpo caloso, ventrículo lateral, caudado/putâmen/pálido, tálamo e ínsula; localizar cinzenta/branca na figura | `branca-composicao`, `cinzenta-composicao`, `cortex-nucleos` cobram composição/categoria. Os nomes específicos e suas posições permanecem rótulos nas figuras. |
| L12 | Lâmina15, título, desenho e legenda de cores | Núcleos de nervos cranianos no tronco: localizar exemplos e distinguir núcleo motor/eferente de núcleo sensitivo/aferente; separar núcleo de nervo/fibra e de gânglio | Inventário renomeia a lâmina como `nucleo-ganglio` e aponta apenas o organizador central/periférico. Isso não recupera a organização mostrada na lâmina15. Ver mínimo proporcional abaixo. |
| L13 | Lâmina16, seis cortes e frase final | Marcos nos próprios cortes: cavidade dorsal versus constituintes ventrais; oliva/pirâmide no bulbo, base pontina, aqueduto/teto-colículos/pedúnculo no mesencéfalo; distinguir cortes no colículo inferior/superior | Os três compartilhados só perguntam nível: mesencéfalo rostral, ponte rostral e bulbo aberto. Marcos são listados no Extra. Não existe o outro nível mesencefálico mostrado na lâmina. |
| L14 | Lâminas17–18; veteranos PDF18 cap6 | Identificar cornos e canal no corte, explicar expansão da cinzenta nas intumescências, e função sensitiva do corno posterior | Cinzenta central/branca periférica, proporção rostral e anterior=motoneurônio estão cobrados. Corno posterior sensitivo e explicação causal das intumescências ficam no Extra; não são recuperados por simplesmente nomear cervical/lombossacral. |
| L15 | Lâmina18, título SOMATOTOPIA; veteranos PDF19 cap6 | Definição geral de somatotopia e polo medial=axial/proximal, além de lateral=distal | Distal/lateral, flexor/dorsal e extensor/ventral cobrem partes do mapa. Definição e polo medial só constam de contexto/Extra. |
| L16 | Lâmina19, texto sobre lesão na cápsula interna e degeneração ao longo da via | Degeneração distal à lesão como método de seguir axônios; porção cranial ipsilateral à lesão antes do cruzamento e via espinal contralateral depois; déficit contralateral acima e ipsilateral abaixo da decussação | `sh-1792329760618` cobra trato=corticoespinal e membro=contralateral no encéfalo. Não cobra degeneração/Walleriana nem raciocínio abaixo do cruzamento. O campo alvo promete mais que a frente. |
| L17 | Lâmina20; Machado córtex cap26 e figura de Broca | Localização da área de produção da fala no frontal dominante e inferência lesão→função | `broca-fala` cobra somente não fluente; localização está no Extra e na fotografia sem pergunta de identificação. |
| L18 | Lâmina21; Machado cap3 §1.6, PDF34 | Inferir destinos da projeção por marcador anterógrado e neurônios de origem por marcador retrógrado após uma injeção | `tracadores` cobra apenas nomes de sentidos soma↔terminal. `transporte-axonal` cobra trilho=microtúbulo. Não existe problema inferencial de conectividade; a imagem da lâmina21 nem é a imagem principal de `tracadores` no plano (usa motores/microtúbulos). |
| L19 | Lâmina22 | Correspondência real entre desenho e RM das estruturas medianas: corpo caloso, diencéfalo, ponte, bulbo, mesencéfalo, cerebelo e medula | `imagem-estrutural` cobra exclusivamente Sagital. Conseguir responder o plano não exige localizar nenhuma das estruturas na RM. |
| L20 | Lâmina23 | Rede inclui interação entre regiões; na figura há ainda córtex parietal posterior, núcleos da base, hipocampo, amígdala/hipotálamo e tronco/medula | `redes` recupera quatro papéis (visual/pré-motor/motor/cerebelo), o que é bom, mas não esgota as estruturas rotuladas na figura. A ausência é visual/anatômica; não atribuo automaticamente a cada rótulo uma função específica que a lâmina não escreveu. |
| L21 | Lâmina24, quatro condições A–D | Comparar recrutamento diferente ao ver/ouvir/falar/pensar palavras e concluir coexistência de especialização e rede distribuída | `ressonancia-funcional` só cobra nome da técnica e hemodinâmica. A figura inteira fica no verso; a tarefa e o padrão de recrutamento não são recuperados. |
| L22 | Machado cap3 §2.1.4/2.2, PDF40–41 | Glia ependimária reveste cavidades; glia satélite envolve somas em gânglios versus Schwann nos axônios | Só quatro tipos clássicos foram efetivamente contemplados. Ependimária foi expressamente adiada na exclusão1479430560753; satélite não tem frente. |
| L23 | Veteranos PDF18 cap6; Machado cap2 §3 e cap7 recorte | Cinco lobos incluindo ínsula; sulcos delimitam giros e permitem maior área cortical dentro do crânio | Sem frente de lobos/ínsula/sulco/giro na versão entregue. A seleção nova dos quatro lobos de superfície não cobre por si só ínsula nem a relação de dobramento. |
| L24 | Machado cap2 §1.3/§2.0, PDF26–27; veteranos PDF19 | Segmentar versus suprassegmentar; arco reflexo pode integrar sem percepção cortical consciente, com vias ascendentes informando encéfalo; mono/polissináptico | `interneuronios` explica a exceção monossináptica só no Extra; nomes aferente/eferente não cobram o papel do centro nem independência do reflexo em relação à consciência. É lacuna bibliográfica; não exige nova lista de espécies/história. |

## Lâminas15/16: básico atual e destino regional

Não considero necessário transformar todo rótulo do Netter em uma ficha regional/clínica nem exigir todos os núcleos, síndromes vasculares, funções farmacológicas ou circuitos de cada nervo. Também não considero suficiente dizer apenas que detalhes ficam para aula03, pois a aula01 mostra essas estruturas para ensinar sua organização.

**Lâmina15, básico agora:** núcleo craniano é agregado de corpos neuronais dentro do tronco, que recebe aferências ou origina eferências — eixo explícito da legenda vermelho/azul. Distingui-lo da fibra/nervo e do gânglio sensitivo periférico mostrado no desenho. O organizador atual núcleo/gânglio cobre só central/periférico, sem aplicar motor/sensitivo aos núcleos cranianos. A nota AnKing1480389622314 pode ajudar na ligação corno motor↔núcleos motores cranianos sem trazer síndrome regional.

**Lâmina15, destino regional:** exemplos como III no mesencéfalo, VI na ponte e XII no bulbo, núcleos nomeados e organização medial/lateral. Não exijo estes IOs individuais agora. Ao ensiná-los depois, não universalizar “todo núcleo motor é medial”: a regra simples se refere aos motores somáticos, não a todo grupo branquial/autonômico.

**Lâmina16, básico agora:** os três compartilhados que reconhecem globalmente mesencéfalo, ponte e bulbo são pertinentes. Nenhuma razão para substituí-los apenas por atlas Kenhub: a modalidade histológica tem ganho próprio. Grandes regiões do atlas precisam também de reconhecimento, conforme a seleção básica proposta.

**Lâmina16, destino regional:** (a) bulbo aberto, IV dorsal e complexo olivar inferior/pirâmide ventral; (b) ponte, base ventral/fibras transversais versus tegmento; (c) mesencéfalo, aqueduto central, teto/colículos dorsais e pedúnculos ventrais. A figura mostra dois níveis mesencefálicos, superior e inferior: o card global rostral não os cobre especificamente, mas a distinção de detalhe pode entrar na aula regional. Aqueduto/IV como grandes cavidades e suas relações são básicos bibliográficos; seus IOs microtopográficos não são obrigatórios aqui. Não registrar os constituintes como recuperados só porque o Extra da identificação global os enumera.

## Evidência concreta da prioridade Kenhub não cumprida

Os seguintes candidatos constavam de `candidatos-vivos.json` e não estão entre as entradas/compartilhados da versão entregue. Os oito primeiros grupos tiveram imagem-base inspecionada nesta auditoria; todos mostram alvo destacado real. A boa qualidade das três imagens AnKing de corte não elimina o ganho de identificação macroscópica Kenhub: são modalidades diferentes, a preservar conforme o objetivo.

| Alvo | ID já exportado | Mídia/localizador | Defeito de cobertura na versão entregue |
|---|---:|---|---|
| Cápsula interna | 1792572870678 | kh-capsula-interna.jpg; lâmina14 | Não é cobrada por axônios da branca; posição entre massas profundas ausente. |
| Corpo caloso | 1792572870701 | kh-corpus-callosum.jpg; lâminas3/22 | Não há cloze/oclusão sobre a comissura; rótulo na frente de Sagital não conta. |
| Tálamo | 1792572870651 | kh-thalamus.jpg; lâminas3/14 | Figura presente não exige identificá-lo. |
| Diencéfalo | 1792572870657 | kh-interbrain.jpg; lâminas3/13/22 | Só nome embrionário não exige reconhecer a região adulta. |
| Ponte | 1792572870632 | kh-pons.jpg; lâminas13/16/22 | Nome na lista do tronco e reconhecimento do corte não equivalem à vista medial. |
| Bulbo | 1792696993352 | kh-medulla-oblongata.jpg; lâminas13/16/22 | Mesmo déficit de modalidade. |
| Mesencéfalo | 1792572870663 | kh-mesencephalon-2.jpg; lâminas13/16/22 | Mesmo déficit, além da distinção de dois níveis na lâmina16. |
| Ventrículo lateral | 1792572870704 | kh-lateral-ventricle.jpg; lâmina14/bibliografia | Cavidade não é recuperada pelo reconhecimento geral do cérebro. |
| Pedúnculo cerebral | 1792572870634; também1792244857819 | candidato exportado; lâminas13/16 | Marco ventral apenas no Extra de corte. Imagem/overlay ainda precisam conferência para adoção. |
| Oliva/núcleo olivar | 1792572870655 | candidato exportado; lâmina16 | Principal pista do bulbo aberto só no Extra. Imagem/overlay a conferir. |
| Aqueduto cerebral | 1792696997556 | candidato exportado; lâmina16/Machado2§2.2.3 | Excluir derivação por futura aula de líquor deixa um marco desta aula sem alvo. |
| Colículos superior/inferior | 1792572870648 /1792572870644 | candidatos exportados; lâmina16 | Nenhuma identificação própria; o plano tem só rostral. |
| Corno posterior/anterior | 1792697130129 /1792697129929 | candidatos exportados; lâminas14/18 | Função textual anterior não ensina reconhecer ambos os cornos. |

A falha não é uma porcentagem insuficiente de Kenhub. Para os alvos básicos, há candidatos disponíveis sem recuperação correspondente, enquanto o mapa registra a seção como coberta por uma categoria mais ampla. Para os regionais, disponibilidade no acervo não obriga inserção agora: é preciso registrar o destino e conferir depois.

## Candidatos AnKing já encontrados nos registros locais

Estes IDs foram **lidos em exportações da própria corrida**, sem novas buscas no Anki. Linhas de `busca/anking.txt` podem estar truncadas: onde não há ficha em `candidatos-vivos.json`, é preciso obter e ler a nota inteira antes de selecionar. São pistas de acervo, não aprovação automática.

- **1479430645161**, AnKing, `busca/anking.txt`: “Distal ... site of CNS or PNS axon injury ... Wallerian degeneration”. Lacuna L16; confirma que existe um alvo de acervo direto, não exige autoria nova para nome/direção de degeneração.
- **1480389648940**, AnKing: “Most (80–90%) ... corticospinal ... caudal medulla ... pyramidal decussation”. L16: local de cruzamento; conferir integralmente e não supor que o card de contralateral já o cobra.
- **1480389622314**, AnKing: “Lower motor neurons ... ventral horn ... cranial nerve nuclei in brainstem”. L12/L14: ponte conceitual entre núcleos motores espinais e cranianos; útil sem ficha clínica regional.
- **1479351825915**, AnKing em candidatos e exclusão: cavidade mesencefálica→aqueduto. **1479351805802** e **1479353800465** estão nas exclusões por ventrículos: reabrir o julgamento bibliográfico, não tratá-los como inexistentes.
- **1479430560753**, AnKing nas exclusões: ependimária. O adiamento explícito a líquor não demonstra cobertura do revestimento no Machado desta introdução.
- **1555082140623**, MCAT, `busca/anking.txt`: neurotransmissores em vesículas liberados com entrada de Ca²⁺ no terminal após PA. L04: é mais direto para o elo de influxo que a adaptação atual que o empurrou ao Extra.
- **1701724039712**, Lightyear, `busca/anking.txt`: mapa de nervos do tronco por níveis e posição; há potencial para L12, mas a linha está truncada e o mapa simplificado precisa julgamento dos complexos que se estendem por vários níveis. Não o recomendo integral sem conferência.
- **1561043470778**, MCAT, `busca/anking.txt`: trato corticobulbar liga córtex a núcleos motores cranianos. Serve como pista de acervo para relação núcleo/saída; a via detalhada pode exceder o mínimo necessário de AN01.
- **1480612594042**, AnKing, `busca/anking.txt`: identificação de colículo superior. **1481048556126**: cinzenta periaquedutal em torno do aqueduto. Modalidades de corte/figura a inspecionar; não basta encontrar o nome.

## Confronto com a proposta nova de 41 Kenhubs

A proposta resolve grande parte das omissões visuais de macrorregiões, raízes/ramos, lobos superficiais, núcleos profundos, medula e exemplos de núcleos cranianos **se cada alvo for realmente ocultado e conferido**. Não a declaro concluída sem integração e readback.

Na lista de41 lida antes do último ajuste ainda não aparecem raiz **posterior**, hipotálamo e ínsula, a conferir como grandes alvos básicos. Oliva/pedúnculo e os núcleos/colículos individuais podem ser retirados para destino regional conforme a orientação final. A lista de imagens não resolve automaticamente as relações L02/L03/L04/L06/L07/L08/L15/L16/L17/L18/L19/L21/L22/L23 e o princípio reflexo de L24. Há diferentes níveis de prioridade dentro desses grupos; não são pedidos de um card por frase do livro.

Defeito pontual no material de seleção: o `fields_source` do núcleo do hipoglosso, src1792338706934, inclui o sinônimo **“Núcleo do nervo craniano X”**. O correto é **XII**. Não propagar esse sinônimo.

## Por que o gate anterior não bastou

Há falha rastreável no inventário e na passagem alvo→frente:

1. A lâmina15 foi reduzida a núcleo versus gânglio, omitindo justamente núcleos cranianos e sua organização mostrada na figura.
2. A lâmina16 promete relação cavidade/estruturas ventrais, mas aponta para frentes que só nomeiam o nível.
3. A lâmina19 promete degeneração e cruzamento, mas aponta para corticoespinal/contralateral.
4. A lâmina21 promete inferência origem/destino, mas aponta para nome do sentido de transporte.
5. A lâmina22 permite acertar Sagital sem localizar as estruturas que ela pretende correlacionar.
6. A lâmina24 permite acertar técnica/hemodinâmica sem interpretar qualquer diferença entre as quatro condições.
7. Exclusões por “futura aula regional/líquor” precisam distinguir princípio básico atual de IO profundo posterior. O esclarecimento de Davi autoriza o segundo adiamento, desde que haja destino explícito e conferência futura; não autoriza marcar o conteúdo futuro como já recuperável na AN01.

O parecer anterior por exemplares julgou cards presentes, não certificou o conteúdo ausente. Minha frase anterior de ausência de elos novos faltantes foi forte demais: este confronto direto das fontes a revoga. A aprovação de um prompt individual não valida a completude do inventário que escolheu quais prompts mostrar ao revisor.

## Limites e fechamento

Não usei cada detalhe do capítulo para inflar automaticamente o deck. Detalhes de receptores específicos, farmacologia, doenças regionais, todos os núcleos e síndromes não foram promovidos a obrigatórios apenas por aparecerem no acervo. Não reproduzir também erros conhecidos da apostila/edição antiga: “sulco pulposo”, origem meníngea simplificada, micróglia como reposição contínua de monócitos, ou regra de que todo potencial pós-sináptico dispara outro PA.

A correção necessária é refazer o mapa de recuperação por estrutura/relação nas fontes, separando básico atual de regional com destino, e depois conferir o conjunto final. Acrescentar imagens ao Extra, trocar `origin` ou aumentar o total de cards, isoladamente, não fecha as lacunas listadas.
