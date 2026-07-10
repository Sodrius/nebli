#import "../typst-template/nebli_v2_apostila.typ": *

// =====================================================
// Bloco 1 — CONSOLIDAÇÃO (Q01-Q10)
// =====================================================

#questao-mc("01", badge-consolidacao,
  [Em um organismo multicelular saudável, qual o estado-padrão de uma célula isolada do contato com seus sinais extracelulares de sobrevivência?],
  (
    ("A", [Permanece viva indefinidamente desde que haja nutrientes e oxigênio suficientes no meio extracelular para o metabolismo basal.]),
    ("B", [Entra em senescência replicativa, com metabolismo preservado mas incapaz de dividir, mantendo-se viável por meses.]),
    ("C", [Ativa o programa interno de apoptose por liberação das proteínas pró-apoptóticas constitutivas e morre por morte celular regulada.]),
    ("D", [Sofre necrose acidental por falta de coordenação iônica entre o meio interno e o externo, com ruptura de membrana.]),
    ("E", [Diferencia-se em outro tipo celular mais autônomo para se adaptar ao isolamento, perdendo dependência de sinais externos.]),
  ),
)

#questao-mc("02", badge-consolidacao,
  [Qual das alternativas distingue corretamente mitógenos, fatores de crescimento e fatores de sobrevivência?],
  (
    ("A", [Mitógenos disparam a transição G1→S por liberação de freios como Rb; fatores de crescimento aumentam síntese e diminuem degradação proteica, gerando massa celular; fatores de sobrevivência bloqueiam ativamente apoptose.]),
    ("B", [Mitógenos aumentam massa proteica via mTOR; fatores de crescimento disparam mitose por hiperfosforilação direta de Cdks; fatores de sobrevivência ativam transcrição de Bax e induzem apoptose seletiva.]),
    ("C", [Os três termos são sinônimos do ponto de vista funcional — variam apenas a nomenclatura histórica entre autores europeus e norte-americanos sem distinção mecanística real.]),
    ("D", [Mitógenos atuam exclusivamente em organelas citoplasmáticas; fatores de crescimento exclusivamente em receptores transmembrana; fatores de sobrevivência exclusivamente em alvos nucleares de transcrição.]),
    ("E", [Mitógenos são pequenos peptídeos lipossolúveis; fatores de crescimento são proteínas solúveis em água; fatores de sobrevivência são gases voláteis com ação parácrina rápida.]),
  ),
)

#questao-ce("03", badge-consolidacao,
  [Julgue os itens sobre as três categorias de morte celular pela nomenclatura moderna (Comitê de Nomenclatura sobre Morte Celular, 2018):],
  (
    ("I", [ACD (_accidental cell death_) corresponde à morte por trauma físico ou químico extremo, sem via molecular dedicada.]),
    ("II", [Toda morte com morfologia de necrose (célula incha, membrana rompe, conteúdo extravasa) é, por definição, ACD.]),
    ("III", [RCD (_regulated cell death_) inclui apoptose, necroptose, autosis, piroptose e ferroptose, entre outras.]),
    ("IV", [PCD (_programmed cell death_) é o subset estritamente fisiológico da RCD, como a apoptose que esculpe os dedos no embrião.]),
  ),
)

#questao-mc("04", badge-consolidacao,
  [Sobre a morfologia comparativa entre apoptose e necrose, é correto afirmar:],
  (
    ("A", [Na apoptose a célula encolhe e a membrana plasmática permanece íntegra até a fagocitose; na necrose a célula incha, a membrana rompe e o conteúdo extravasa, disparando inflamação local intensa.]),
    ("B", [Na apoptose a célula incha por entrada de água e a membrana rompe cedo, liberando conteúdo; na necrose a célula encolhe e fragmenta-se ordenadamente em corpos discretos sem extravasamento.]),
    ("C", [Ambas apresentam ruptura imediata da membrana plasmática nas primeiras horas e ambas culminam na formação de corpos apoptóticos arredondados que são fagocitados em silêncio imunológico.]),
    ("D", [Apoptose ocorre apenas em células do sistema imune adaptativo (linfócitos B e T); necrose ocorre apenas em células epiteliais expostas ao ambiente externo, como pele e mucosa.]),
    ("E", [Apoptose e necrose são indistinguíveis morfologicamente — apenas a presença de marcadores moleculares específicos como caspase-3 ativada permite separá-las em laboratório.]),
  ),
)

#questao-mc("05", badge-consolidacao,
  [A externalização de fosfatidilserina na superfície da célula apoptótica resulta de:],
  (
    ("A", [Síntese aumentada de fosfatidilserina no folheto externo pelo retículo endoplasmático rugoso, com transporte direto via vesículas até a membrana plasmática.]),
    ("B", [Endocitose massiva da face externa da membrana, que internaliza colina e expõe os grupos serina dos fosfolipídios remanescentes como subproduto.]),
    ("C", [Inativação da flipase ATP-dependente e ativação simultânea da scramblase pelas caspases, permitindo que a fosfatidilserina passe livremente entre os folhetos.]),
    ("D", [Hiperativação da flipase pelas caspases efetoras, que passa a transportar fosfatidilserina para o folheto externo contra o gradiente termodinâmico.]),
    ("E", [Glicosilação enzimática da fosfatidilserina pelo aparelho de Golgi, tornando-a quimicamente estável apenas na face externa por afinidade aos receptores.]),
  ),
)

#questao-mc("06", badge-consolidacao,
  [Caspases são uma família de proteases caracterizadas por:],
  (
    ("A", [Serina no sítio ativo e clivagem após resíduos básicos como arginina e lisina, em padrão similar à tripsina pancreática.]),
    ("B", [Cisteína no sítio ativo e clivagem específica logo após resíduos de aspartato nas proteínas-substrato, daí o nome "casp-ase".]),
    ("C", [Cisteína no sítio ativo e clivagem aleatória de qualquer ligação peptídica acessível, sem preferência por sequência específica.]),
    ("D", [Zinco metálico no sítio ativo e ação restrita à membrana mitocondrial externa, em proximidade com a cadeia respiratória.]),
    ("E", [Aspartato no sítio ativo e clivagem após resíduos de cisteína, em padrão inverso ao implícito na nomenclatura da família.]),
  ),
)

#questao-ce("07", badge-consolidacao,
  [Julgue os itens sobre caspases iniciadoras e executoras:],
  (
    ("I", [Iniciadoras (caspase-2, -8, -9, -10) ativam-se por proximidade induzida em plataformas como DISC ou apoptossomo.]),
    ("II", [Executoras (caspase-3, -6, -7) ativam-se por proximidade induzida; iniciadoras ativam-se por clivagem.]),
    ("III", [A caspase-3 é uma executora típica e seu substrato inclui lâminas nucleares, citoesqueleto e ICAD (inibidor de uma DNAse).]),
    ("IV", [A diferença entre iniciadoras e executoras é apenas a ordem temporal na cascata, sem distinção estrutural.]),
  ),
)

#questao-mc("08", badge-consolidacao,
  [O DISC (_death-inducing signaling complex_) é uma plataforma de ativação característica de qual via apoptótica e formada por quais componentes principais?],
  (
    ("A", [Via intrínseca mitocondrial, formada por Apaf-1, citocromo c citosólico, dATP e pró-caspase-9 conectadas via domínios CARD.]),
    ("B", [Via extrínseca de receptores de morte, formada por receptor agrupado (Fas ou TNFR1), adaptador FADD via DD-DD e pró-caspase-8/10 via DED-DED.]),
    ("C", [Via mitocondrial direta, formada por BAX e BAK oligomerizados na membrana mitocondrial externa formando o poro de saída do citocromo c.]),
    ("D", [Via autofágica clássica, formada por LC3-II ligada à fosfatidiletanolamina na membrana do autofagossomo em maturação após fusão com lisossomo.]),
    ("E", [Via necroptótica clássica, formada por RIPK1 e RIPK3 fosforiladas reciprocamente que recrutam e fosforilam MLKL para abertura da membrana plasmática.]),
  ),
)

#questao-mc("09", badge-consolidacao,
  [O apoptossomo é montado a partir de:],
  (
    ("A", [BAX, BAK e Bcl-2 antiapoptótica oligomerizados em equilíbrio na membrana mitocondrial externa para regular o limiar de morte celular.]),
    ("B", [Sete moléculas de Apaf-1 ativadas pela ligação a citocromo c citosólico na presença de dATP, formando uma roda heptamérica que recruta pró-caspase-9 via CARD.]),
    ("C", [FasL exógeno, receptor Fas e adaptador FADD agrupados na membrana plasmática para recrutamento e ativação direta da pró-caspase-8 do citosol.]),
    ("D", [Necrossomo intracelular com RIPK1 fosforilando RIPK3 que por sua vez fosforila a pseudoquinase MLKL para abrir poros na membrana plasmática.]),
    ("E", [Maquinaria autofágica com LC3 e Atg5 conjugados à fosfatidiletanolamina na membrana do autofagossomo em maturação intracelular.]),
  ),
)

#questao-mc("10", badge-consolidacao,
  [A família Bcl-2 controla a via intrínseca da apoptose. Sobre suas classes funcionais, é correto afirmar:],
  (
    ("A", [Bcl-2, Bcl-X#sub[L] e Mcl-1 são as efetoras pró-apoptóticas que oligomerizam na membrana mitocondrial externa e formam o poro do MOMP responsável pela liberação de citocromo c.]),
    ("B", [As proteínas BH3-only (Bid, Bim, Bad, Puma, Noxa) formam diretamente o poro do MOMP na membrana mitocondrial externa, dispensando BAX e BAK como efetores estruturais terminais.]),
    ("C", [BAX e BAK são efetoras pró-morte que oligomerizam na membrana mitocondrial externa formando o poro do MOMP; antiapoptóticas (Bcl-2, Bcl-X#sub[L], Mcl-1) sequestram-nas; BH3-only sinalizam ativando BAX/BAK ou ocupando antiapoptóticas.]),
    ("D", [Todas as proteínas da família têm exatamente a mesma função: induzir apoptose por sinergia conformacional na membrana mitocondrial externa, com redundância completa funcional entre todos os membros descritos.]),
    ("E", [A família Bcl-2 atua exclusivamente na via extrínseca de apoptose, regulando a montagem do DISC e a clivagem da pró-caspase-8 pela proximidade induzida no complexo de receptores de morte.]),
  ),
)

// =====================================================
// Bloco 2 — INTEGRAÇÃO (Q11-Q25)
// =====================================================

#questao-mc("11", badge-integracao,
  [Durante o desenvolvimento do sistema nervoso, os neurônios são produzidos em excesso e apenas aqueles que recebem fator de sobrevivência adequado das células-alvo permanecem vivos. Esse mecanismo:],
  (
    ("A", [Garante que o número final de neurônios sobreviventes seja proporcional ao número de células-alvo disponíveis, ajustando o sistema nervoso ao corpo.]),
    ("B", [Resulta em sobrevivência indiscriminada de todos os neurônios produzidos no desenvolvimento, expandindo continuamente o sistema nervoso ao longo da maturação.]),
    ("C", [Depende de mitógenos secretados pelos alvos que dividem ativamente os neurônios maduros até atingir o número correto por hiperplasia compensatória.]),
    ("D", [Ocorre apenas no embrião precoce e não guarda relação com qualquer fenômeno de plasticidade neural posterior do organismo adulto.]),
    ("E", [Independe da via apoptótica clássica e usa exclusivamente autofagia para remover os neurônios excedentes que não recebem fator de sobrevivência.]),
  ),
)

#questao-mc("12", badge-integracao,
  [Em uma célula epitelial saudável, a fosfatidilserina permanece confinada à face citoplasmática da membrana. Caso a célula seja exposta a um estímulo apoptótico, a sequência mecanística que leva à externalização da fosfatidilserina é:],
  (
    ("A", [Síntese de novo de fosfatidilserina especificamente no lado externo pelo retículo endoplasmático, com glicosilação subsequente que a fixa na face externa.]),
    ("B", [Endocitose maciça que internaliza o folheto externo da membrana plasmática e expõe o folheto interno como nova face externa em todo o perímetro celular.]),
    ("C", [Caspases ativas inativam a flipase ATP-dependente e ativam a scramblase, permitindo que a fosfatidilserina equilibre-se entre os folhetos sem gasto de ATP.]),
    ("D", [Fagocitose direta pela própria célula apoptótica, que digere internamente o folheto interno da membrana, expondo a serina à face externa.]),
    ("E", [Aumento súbito de Ca²⁺ intracelular ativa diretamente a flipase, que passa a transportar fosfatidilserina para o folheto externo contra o gradiente.]),
  ),
)

#questao-mc("13", badge-integracao,
  [Em ensaio de citometria de fluxo com marcação dupla por anexina V (afinidade a fosfatidilserina) e iodeto de propídio (entra em células com membrana rompida), uma célula anexina V positiva e PI negativa é classificada como:],
  (
    ("A", [Viva — fosfatidilserina e membrana íntegra, sem qualquer sinal de morte iniciada nem morfologia compatível com programa apoptótico em andamento.]),
    ("B", [Apoptose tardia ou necrose secundária — membrana já rompida com fosfatidilserina previamente externalizada antes do colapso final da bicamada.]),
    ("C", [Apoptose inicial — fosfatidilserina exposta na face externa, mas membrana plasmática ainda íntegra (PI não entra), portanto antes da lise secundária.]),
    ("D", [Necrose pura — membrana plasmática rompida cedo, antes que o programa de inversão de fosfatidilserina pelo eixo scramblase-flipase pudesse operar.]),
    ("E", [Não há classificação possível com esses dois marcadores combinados — seria necessária imunomarcação adicional para caspase-3 clivada para definir.]),
  ),
)

#questao-ce("14", badge-integracao,
  [Sobre a via intrínseca (mitocondrial) da apoptose, julgue:],
  (
    ("I", [O evento de não-retorno é a permeabilização da membrana mitocondrial externa (MOMP), realizada por BAX/BAK oligomerizados.]),
    ("II", [O citocromo c que escapa para o citosol é uma proteína distinta do citocromo c que participa da cadeia respiratória.]),
    ("III", [Além de citocromo c, escapa do espaço intermembranar Smac/Diablo, que neutraliza IAPs e libera as caspases.]),
    ("IV", [Apaf-1 reside permanentemente na membrana mitocondrial externa e só é liberada após MOMP.]),
  ),
)

#questao-mc("15", badge-integracao,
  [Sobre o cross-talk entre as vias extrínseca e intrínseca da apoptose, é correto afirmar:],
  (
    ("A", [A via intrínseca cliva diretamente a caspase-8 ativa do DISC e ativa a via extrínseca como amplificador secundário do sinal mitocondrial em células do tipo II, com retroalimentação positiva contínua.]),
    ("B", [As duas vias são totalmente independentes molecularmente e nunca interagem dentro da mesma célula durante um único evento apoptótico fisiológico, mantendo-se em compartimentos celulares separados durante todo o programa.]),
    ("C", [Em células tipo II (hepatócitos, células beta), a caspase-8 do DISC cliva Bid em tBid, que migra à mitocôndria, ativa BAX/BAK e dispara MOMP, amplificando o sinal extrínseco pela via intrínseca.]),
    ("D", [O cross-talk só ocorre em células neoplásicas devido a rearranjos cromossômicos típicos de câncer, sendo ausente em qualquer célula somática normal por restrição de expressão das proteínas adaptadoras envolvidas.]),
    ("E", [tBid é gerado especificamente pela caspase-9 ativa no apoptossomo e tem função inibitória sobre a via extrínseca, freando a montagem do DISC e bloqueando a ativação da caspase-8 inicial.]),
  ),
)

#questao-mc("16", badge-integracao,
  [Sobre as classes de proteínas BH3-only e seus mecanismos de ativação da via intrínseca, é correto afirmar:],
  (
    ("A", [Todas as BH3-only formam diretamente o poro do MOMP na membrana mitocondrial externa, dispensando completamente BAX e BAK como efetores estruturais finais.]),
    ("B", [BH3-only e antiapoptóticas são sinônimos funcionais — Bcl-2 e Bim são a mesma proteína em estados de fosforilação distintos que alternam função entre as classes.]),
    ("C", [BH3-only são proteínas antiapoptóticas que sequestram BAX e BAK na membrana mitocondrial externa, mantendo a célula viva por bloqueio da oligomerização efetora.]),
    ("D", [BH3-only ativadoras (Bid, Bim, Puma) ligam diretamente BAX/BAK e os ativam; BH3-only sensibilizadoras (Bad, Noxa) ocupam apenas antiapoptóticas, liberando BAX/BAK indiretamente.]),
    ("E", [BH3-only atuam exclusivamente na via extrínseca regulando estabilidade do DISC e estequiometria de pró-caspase-8 versus FLIP no agrupamento de receptores de morte.]),
  ),
)

#questao-mc("17", badge-integracao,
  [As proteínas IAPs (XIAP, cIAP1, cIAP2) atuam na regulação da apoptose:],
  (
    ("A", [Sintetizando ativamente Bcl-2 e Bcl-X#sub[L] no retículo endoplasmático para sequestrar BAX e BAK na membrana mitocondrial externa antes da MOMP.]),
    ("B", [Formando o poro do MOMP em substituição funcional a BAX/BAK quando estes estão ausentes ou inativados por modificações pós-traducionais específicas.]),
    ("C", [Clivando Bid em tBid no citosol e disparando assim a via intrínseca via BAX/BAK como amplificador secundário do sinal extrínseco em células tipo II.]),
    ("D", [Externalizando fosfatidilserina para sinalizar fagocitose silenciosa pelos macrófagos, ligando-se aos fosfolipídios e induzindo recrutamento de receptores TIM4.]),
    ("E", [Ligando-se diretamente a caspases ativas e bloqueando seu sítio catalítico, constituindo uma segunda camada de freio após a família Bcl-2.]),
  ),
)

#questao-mc("18", badge-integracao,
  [Smac/Diablo é uma proteína do espaço intermembranar mitocondrial que, após MOMP, escapa para o citosol. Sua função no programa apoptótico é:],
  (
    ("A", [Clivar caspase-3 diretamente, ativando-a sem necessidade de caspase-9 ou apoptossomo, em rota paralela à formação da plataforma de ativação.]),
    ("B", [Atuar como BH3-only ativadora citosólica de BAX e BAK na membrana mitocondrial externa, em retroalimentação positiva após o início do MOMP.]),
    ("C", [Ligar-se a IAPs com alta afinidade, deslocando-as das caspases ativas e liberando a cascata executora previamente freada por bloqueio do sítio catalítico.]),
    ("D", [Inibir a flipase de fosfatidilserina diretamente, contribuindo para a externalização da fosfatidilserina como sinal "coma-me" para os macrófagos teciduais.]),
    ("E", [Ativar diretamente o inflamassoma NLRP3 no citosol e disparar piroptose dependente de caspase-1 como alternativa à apoptose silenciosa convencional.]),
  ),
)

#questao-ce("19", badge-integracao,
  [Sobre os mecanismos pelos quais fatores de sobrevivência extracelulares bloqueiam apoptose, julgue:],
  (
    ("I", [Aumentam a transcrição de proteínas antiapoptóticas (Bcl-2, Bcl-X#sub[L]) via fatores como NF-κB ou CREB.]),
    ("II", [A via PI3K/Akt fosforila Bad em resíduo específico, e Bad fosforilada é sequestrada por proteínas 14-3-3 no citosol, perdendo a capacidade de promover apoptose.]),
    ("III", [Os efeitos da sinalização de sobrevivência ocorrem exclusivamente em escala de horas via transcrição, sem componentes pós-traducionais rápidos.]),
    ("IV", [Sinais de sobrevivência também atuam mantendo IAPs funcionais, somando uma terceira camada de proteção.]),
  ),
)

#questao-mc("20", badge-integracao,
  [Macrófagos que fagocitam corpos apoptóticos via reconhecimento de fosfatidilserina exposta produzem:],
  (
    ("A", [Quantidades massivas de IL-1β e TNF-α maduros via caspase-1 do inflamassoma, intensificando inflamação local e recrutando neutrófilos para o sítio da apoptose.]),
    ("B", [Espécies reativas de oxigênio em explosão respiratória (_oxidative burst_) que destroem o tecido vizinho sadio em padrão similar ao combate a infecções bacterianas.]),
    ("C", [Histamina e leucotrienos em granulação rápida, recrutando neutrófilos circulantes e aumentando permeabilidade vascular ao redor do tecido em apoptose.]),
    ("D", [Citocinas anti-inflamatórias IL-10 e TGF-β e suprimem ativamente as pró-inflamatórias IL-12 — fagocitose imunologicamente silenciosa que evita inflamação local.]),
    ("E", [Anticorpos específicos anti-fosfatidilserina apresentados em complexo MHC-II, gerando memória imunológica adaptativa contra futuros eventos apoptóticos.]),
  ),
)

#questao-mc("21", badge-integracao,
  [Em um camundongo geneticamente modificado com deleção da caspase-8 nos hepatócitos, esperar-se-ia que a sensibilidade dessas células à apoptose mediada por Fas/FasL fosse:],
  (
    ("A", [Aumentada por compensação, pois sem caspase-8 a via intrínseca passaria a operar em hiperatividade constitutiva via BAX/BAK ativados espontaneamente.]),
    ("B", [Inalterada, pois a apoptose mediada por Fas independe de caspase-8 e usa caspase-2 e caspase-9 como iniciadoras alternativas em qualquer tipo celular.]),
    ("C", [Drasticamente reduzida, pois hepatócitos são células tipo II que dependem da clivagem de Bid pela caspase-8 para amplificar pela via intrínseca.]),
    ("D", [Aumentada apenas no fígado e reduzida em outros órgãos, em padrão tecido-específico que reflete diferenças regionais na maquinaria apoptótica padrão.]),
    ("E", [Os hepatócitos passariam a usar exclusivamente necroptose por RIPK3/MLKL, com sensibilidade ao FasL similar à apoptose normal mas com inflamação local.]),
  ),
)

#questao-mc("22", badge-integracao,
  [Sobre a autofagia como processo celular, é correto afirmar:],
  (
    ("A", [É um processo exclusivamente patológico, restrito a células doentes com estresse metabólico crônico e ausente em fisiologia celular normal de eucariotos.]),
    ("B", [Forma uma vesícula de membrana única (fagossomo) que engloba conteúdo citoplasmático aleatório e funde-se com lisossomo para digestão final.]),
    ("C", [É uma via secretória especializada que exporta proteínas mal-dobradas e organelas envelhecidas para o meio extracelular via exocitose mediada por SNAREs.]),
    ("D", [Forma uma vesícula de membrana dupla (autofagossomo) que engloba conteúdo citoplasmático, funde com lisossomo e gera reciclagem de monômeros — citoprotetora em jejum.]),
    ("E", [Substitui completamente a apoptose como mecanismo de morte em qualquer contexto celular adulto, sendo a única via responsável por morte programada em mamíferos.]),
  ),
)

#questao-mc("23", badge-integracao,
  [Sobre a necroptose, é correto afirmar:],
  (
    ("A", [Depende de RIPK1, RIPK3 e MLKL, ocorre tipicamente quando caspase-8 está bloqueada (por patógeno ou inibidor), tem morfologia de necrose e dispara inflamação.]),
    ("B", [Depende de caspase-1 e gasdermina D em montagem inflamassoma, com formação de poros transmembrana e liberação de IL-1β madura nos tecidos circundantes.]),
    ("C", [É indistinguível morfologicamente da necrose acidental e bioquimicamente também — não há proteínas-chave identificáveis, sendo morte verdadeiramente passiva.]),
    ("D", [É a mesma via molecular da apoptose intrínseca, apenas com nomenclatura distinta na literatura mais recente para distinguir contextos clínicos específicos.]),
    ("E", [Ocorre exclusivamente em neutrófilos durante a NETose, com extrusão de cromatina decorada com elastase e mieloperoxidase ao meio extracelular.]),
  ),
)

#questao-ce("24", badge-integracao,
  [Sobre receptores de morte da família TNF e seus inibidores, julgue:],
  (
    ("I", [Fas, TNFR1 e TRAIL-R são membros da superfamília TNF e possuem domínio de morte (DD) intracelular.]),
    ("II", [Receptores armadilha (DcR1, DcR2) ligam o ligante FasL como se fossem Fas, mas não têm DD funcional e por isso não disparam sinalização.]),
    ("III", [FLIP é uma cópia funcional de caspase-8 com sítio ativo proteolítico — ao entrar no DISC, ela cliva substratos adicionais e amplifica a apoptose.]),
    ("IV", [O mesmo TNFR1 pode disparar NF-κB (sobrevivência), apoptose (via caspase-8) ou necroptose (via RIPK3/MLKL), dependendo do contexto intracelular.]),
  ),
)

#questao-mc("25", badge-integracao,
  [Em uma célula com dano massivo ao DNA, a proteína p53 acumulada pode disparar dois desfechos distintos. Esses desfechos são:],
  (
    ("A", [Apoptose imediata sempre ou senescência permanente sempre — a decisão é binária e aleatória sem participação de fatores transcricionais celulares específicos.]),
    ("B", [Necroptose obrigatória sempre ou autofagia obrigatória sempre, conforme o tipo celular previamente programado e independente da extensão real do dano de DNA.]),
    ("C", [Parada do ciclo em G1 via transcrição de p21 (para reparo) ou apoptose via transcrição de Puma/Noxa/Bax (se dano irrecuperável) — dois braços transcricionais.]),
    ("D", [Aumento intenso da degradação de p53 por hiperatividade da MDM2, eliminando o sinal apoptótico em todos os contextos por retroalimentação negativa rápida.]),
    ("E", [Indução de mitose imediata para diluir o dano de DNA entre as células-filhas e estratégia de "lavar mutações" por replicação acelerada do genoma comprometido.]),
  ),
)

// =====================================================
// Bloco 3 — APLICAÇÃO (Q26-Q30)
// =====================================================

#questao-mc("26", badge-aplicacao,
  [Um paciente de 67 anos com leucemia linfocítica crônica (LLC) refratária a quimioterapia inicia tratamento com venetoclax, droga oral de uso recente em hemato-oncologia. Após poucas semanas, observa-se queda acentuada da contagem linfocitária e melhora clínica. Considerando que as células dessa LLC superexpressam Bcl-2 (típico de LLC), o mecanismo molecular pelo qual o venetoclax induziu apoptose nessas células foi:],
  (
    ("A", [O venetoclax fosforilou diretamente BAX e BAK no citosol, ativando-os e induzindo abertura de poros na membrana mitocondrial externa sem necessidade de mudança no equilíbrio com proteínas antiapoptóticas da família Bcl-2.]),
    ("B", [O venetoclax atravessou a membrana plasmática e clivou a pró-caspase-8 dentro do citosol, montando um DISC funcional sem necessidade de ligante extracelular Fas-L ou TNF, e disparando a via extrínseca diretamente.]),
    ("C", [O venetoclax é um BH3-mimético que se liga ao sulco de Bcl-2 superexpressa nas células leucêmicas e desloca dali as proteínas pró-apoptóticas BAX e BAK previamente sequestradas, liberando-as para oligomerizar na membrana mitocondrial externa.]),
    ("D", [O venetoclax bloqueou a via PI3K/Akt nas células leucêmicas, impedindo a fosforilação inibitória de Bad e permitindo que Bad ativa fosse à mitocôndria induzir morte por uma via independente da família Bcl-2 clássica.]),
    ("E", [O venetoclax aumentou diretamente a transcrição do gene da gasdermina D nas células leucêmicas, formando poros na membrana plasmática que extravasaram conteúdo citosólico e induziram morte por mecanismo similar à piroptose.]),
  ),
)

#questao-mc("27", badge-aplicacao,
  [Em um modelo experimental de infarto agudo do miocárdio em camundongos, a administração de necrostatina-1 imediatamente após a reperfusão reduz significativamente a área de lesão final, sem alterar a área isquêmica inicial. A necrostatina-1 é um inibidor seletivo de RIPK1. A explicação mecanística mais coerente para esse efeito protetor é:],
  (
    ("A", [A necrostatina-1 estimula a fosforilação de Bad pela via PI3K/Akt nos cardiomiócitos da zona de penumbra, fazendo com que Bad fosforilada seja sequestrada por proteínas 14-3-3 e perca capacidade pró-apoptótica.]),
    ("B", [A necrostatina-1 bloqueia a montagem do complexo DISC nos cardiomiócitos via Fas/FasL ativado pelo estresse de reperfusão, impedindo a clivagem da pró-caspase-8 e abortando completamente a via extrínseca da apoptose.]),
    ("C", [A necrostatina-1 inibe a peroxidação de lipídios de membrana dependente de ferro nos cardiomiócitos, prevenindo a ferroptose desencadeada pelo acúmulo de ROS durante o restabelecimento do fluxo coronariano após o evento isquêmico.]),
    ("D", [Inibindo RIPK1, a necrostatina-1 impede a formação do necrossomo (RIPK1-RIPK3-MLKL) nos cardiomiócitos da zona de penumbra, abortando a necroptose que expandiria a lesão por DAMPs liberados e inflamação local após a reperfusão.]),
    ("E", [A necrostatina-1 estimula a produção de citocinas anti-inflamatórias IL-10 e TGF-β pelos macrófagos teciduais que fagocitam cardiomiócitos apoptóticos, suprimindo a resposta imune inata e limitando a extensão da inflamação no miocárdio.]),
  ),
)

#questao-mc("28", badge-aplicacao,
  [Um vírus citomegálico (CMV) expressa uma proteína viral chamada vICA, que se liga e inibe a caspase-8 da célula hospedeira. Apesar dessa inibição, células infectadas por CMV podem ainda morrer em resposta ao TNF — só que com morfologia de necrose, não de apoptose, e disparando inflamação intensa. A interpretação correta desse fenômeno é:],
  (
    ("A", [Sem caspase-8 ativa, a via intrínseca da apoptose passa a operar independentemente e mata a célula por MOMP, com extravasamento de citocromo c que neste contexto causa inflamação local intensa em vez de fagocitose silenciosa.]),
    ("B", [A inibição da caspase-8 pelo vICA causa acúmulo direto de fosfatidilserina na face externa da membrana plasmática, e os macrófagos teciduais fagocitam essas células com resposta pró-inflamatória maciça por reconhecimento aberrante.]),
    ("C", [Sem caspase-8 funcional, RIPK1 e RIPK3 não são clivadas e permanecem disponíveis para se associar no necrossomo; RIPK3 fosforila MLKL, que oligomeriza e fura a membrana plasmática — necroptose, com liberação de DAMPs e inflamação que alerta o sistema imune contra o vírus.]),
    ("D", [O CMV ativa autofagia massiva nas células infectadas, e o excesso prolongado dessa autofagia leva à autosis, morte autofágica dependente da Na⁺/K⁺-ATPase que neste cenário promove extravasamento secundário de DAMPs e inflamação.]),
    ("E", [O TNF, na ausência de caspase-8, ativa diretamente o inflamassoma com caspase-1 e gasdermina D, e a clivagem da gasdermina D forma poros na membrana plasmática causando piroptose, com liberação de IL-1β madura e inflamação dependente de citocinas.]),
  ),
)

#questao-mc("29", badge-aplicacao,
  [Em um cultivo de células beta pancreáticas humanas expostas a citocinas inflamatórias (IL-1β + IFN-γ, mimetizando o ambiente de pâncreas em diabetes tipo 1 inicial), observa-se: aumento transcricional de Puma e Noxa; translocação de BAX do citosol para a mitocôndria; clivagem de caspase-3; e externalização de fosfatidilserina nas células ainda íntegras. A sequência mecanística que melhor explica esse conjunto de achados é:],
  (
    ("A", [As citocinas ativam diretamente RIPK1 no citosol das células beta, e o necrossomo RIPK1-RIPK3-MLKL fosforila MLKL, que migra à mitocôndria e abre os poros responsáveis pela translocação observada de BAX, processo independente da família Bcl-2.]),
    ("B", [As citocinas ativam estresse celular que dispara p53 e outros fatores, com transcrição de BH3-only sensibilizadoras (Puma, Noxa) que se ligam às antiapoptóticas Bcl-2/Bcl-X#sub[L], liberando BAX/BAK; BAX migra à mitocôndria, ocorre MOMP, citocromo c forma apoptossomo com Apaf-1 e ativa caspase-9, que cliva caspase-3 — executora que ativa a scramblase responsável pela externalização de fosfatidilserina.]),
    ("C", [As citocinas ativam o inflamassoma NLRP3 nas células beta, e caspase-1 ativada cliva gasdermina D que forma poros na membrana plasmática causando piroptose; a clivagem secundária da caspase-3 observada decorre da ativação cruzada por caspase-1, e a externalização de fosfatidilserina é consequência tardia da despolarização da membrana plasmática piroptótica.]),
    ("D", [As citocinas ativam autofagia nas células beta, e o acúmulo de autofagossomos esgota a fosfatidiletanolamina disponível para a flipase; sem fosfatidiletanolamina suficiente, a flipase deixa de operar e a fosfatidilserina migra passivamente à face externa, enquanto BAX é recrutado para autofagossomos como cargo molecular.]),
    ("E", [As citocinas ativam diretamente o receptor Fas na superfície das células beta sem necessidade de ligante FasL, montando um DISC funcional autônomo; a caspase-8 ativada cliva diretamente caspase-3 sem amplificação pela via intrínseca, e a translocação de BAX observada é epifenômeno do colapso geral do citoesqueleto durante a apoptose extrínseca.]),
  ),
)

#questao-mc("30", badge-aplicacao,
  [Um paciente com câncer colorretal metastático recebe quimioterapia com 5-fluorouracil, que causa dano massivo ao DNA das células tumorais. A análise molecular do tumor mostra que o gene TP53 está mutado em ambos os alelos (perda completa de p53 funcional). Apesar do tratamento, o tumor progride rapidamente. A explicação molecular mais coerente é:],
  (
    ("A", [Sem p53 funcional, as células tumorais respondem ao dano de DNA com hiperativação de PARP-1 que consome NAD⁺ e ATP em escala catastrófica; essa exaustão metabólica deveria induzir parthanatos eficiente, mas a quimioterapia bloqueia paradoxalmente essa via colateral.]),
    ("B", [A ausência de p53 ativa transcrição compensatória massiva de IAPs e Smac/Diablo simultaneamente, e o balanço resultante é neutro, mantendo as células tumorais em estado de equilíbrio entre apoptose e sobrevivência durante o tratamento citotóxico.]),
    ("C", [Sem p53 funcional, as células tumorais com DNA danificado pelo 5-FU não param em G1 (não há transcrição de p21) nem disparam apoptose via Puma/Noxa/Bax pela via intrínseca; continuam ciclando, acumulam mais mutações e selecionam clones resistentes, levando à progressão tumoral.]),
    ("D", [As células tumorais sem p53 substituem a apoptose por necroptose como resposta padrão ao dano de DNA, e a necroptose causada pelo 5-FU promove inflamação local que paradoxalmente recruta células-tronco tumorais residentes, expandindo o tumor.]),
    ("E", [A ausência de p53 leva ao acúmulo intracelular de ferro livre por desregulação de ferritina, e as células tumorais entram em ferroptose maciça que, ao liberar DAMPs no microambiente tumoral, promove vascularização compensatória e progressão da doença.]),
  ),
)

// =====================================================
// Gabarito consolidado
// =====================================================

#gabarito-page((
  (
    "Consolidação (Q01-Q10)",
    (
      ("01", "C"),
      ("02", "A"),
      ("03", "CECC"),
      ("04", "A"),
      ("05", "C"),
      ("06", "B"),
      ("07", "CECE"),
      ("08", "B"),
      ("09", "B"),
      ("10", "C"),
    ),
  ),
  (
    "Integração (Q11-Q25)",
    (
      ("11", "A"),
      ("12", "C"),
      ("13", "C"),
      ("14", "CECE"),
      ("15", "C"),
      ("16", "D"),
      ("17", "E"),
      ("18", "C"),
      ("19", "CCEC"),
      ("20", "D"),
      ("21", "C"),
      ("22", "D"),
      ("23", "A"),
      ("24", "CCEC"),
      ("25", "C"),
    ),
  ),
  (
    "Aplicação (Q26-Q30)",
    (
      ("26", "C"),
      ("27", "D"),
      ("28", "C"),
      ("29", "B"),
      ("30", "C"),
    ),
  ),
))
