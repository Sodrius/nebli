# Especificação curada — BC10 Embriologia do digestório, fígado e pâncreas (UC08 P2, Biologia Celular e do Desenvolvimento; Profa. Patrícia Gama; 92 lâminas: embriologia 1–57, pâncreas 58–67, fígado 68–92). Sem transcrição.
# Ciclo básico: desenvolvimento do tubo digestório, rotações e posição dos órgãos, e histologia funcional do pâncreas e do fígado (processo, não doença).
# História do deck: o endoderma dobra e fecha o tubo → o tubo ganha mesentérios → o estômago gira e leva o fígado para a direita → a alça do intestino médio herniá e gira → os brotos do fígado e do pâncreas saem do endoderma → o acino produz enzimas e o lóbulo produz bile.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("A aula é de processo (dobramento, mesentérios, rotação do estômago, herniação do intestino, brotos hepático e pancreático, ácino e lóbulo) "
                   "e o AnKing traz só fatos soltos de embriologia e de patologia; Langman, Junqueira e Ninja Nerd trazem o processo; busca nos três caminhos não achou esses cards.")
PIPELINE = "anking-primeiro"
RUN_ID = "uc08-bc10-20261022a"
SHORT = "bc10"
LESSON = "2026-uc08-biocel-10-embriologia-digestorio-figado-pancreas"
DECK = "NEBLI::UC08::P2::Biologia Celular::Embriologia do digestório, fígado e pâncreas"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261022-CLAUDE-02 + ANTI-EXEMPLARES §1–16, 22/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (22/10): seções de recurso do AnKing (embriologia do GI, microarquitetura hepática, pâncreas exócrino; busca/secoes); palavra-chave e significado "
         "em AnKing, Referências Externas e NEBLI vivo (busca/semantica.jsonl, uma consulta por conceito). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


A_, B_, C_, D_, E_, F_ = "A-tubo", "B-estomago", "C-intestinos", "D-brotos-figado-pancreas", "E-pancreas-histologia", "F-figado-histologia"
EXCLUIDOS = []
FORA_DO_RECORTE = [
    "Clínica além do mecanismo mostrado em aula (regra dos 2 do Meckel, cintilografia, associações e conduta de onfalocele e gastroschisis, estenose do piloro, pancreatite, cirrose, hepatites): fica para patologia e clínica.",
    "Inervação autonômica do digestório e ligamentos e recessos do peritônio (esplenorrenal, gastrocólico, SAID PUCKER): são das aulas de Anatomia de inervação e peritônio.",
    "Fisiologia da secreção pancreática e biliar (fluxo, íons, CFTR, regulação hormonal em detalhe): aula de Fisiologia do fígado e pâncreas de 29/10; aqui só entram o ácino, o ducto e os dois hormônios da lâmina 67.",
    "Mucosa gástrica fetal de rato (lâmina 32), tese de lisossomos tubulares, referências e vídeos: ilustram, não ensinam alvo.",
]

CARDS = [
    # Bloco A — o tubo se forma (lâminas 1–24)
    K(1405189607684, "A-aula", A_, "Gastrulação na terceira semana", 6, "lâmina 6 (gastrulação e três folhetos)"),
    K(1489112981171, "V-pilar", A_, "O epitélio do tubo e dos órgãos vem do endoderma", 6, "lâmina 6 e 15 (endoderma forma o revestimento do tubo e das glândulas)"),
    au("au-dobramento", "Cephalocaudal and lateral folding pull the endoderm inside the embryo and close it into the {{c1::primitive gut}} tube",
       "V-pilar", A_, "O dobramento do embrião fecha o intestino primitivo", 11, "lâminas 9–13 (dobramento lateral e céfalo-caudal)",
       extra="- The yolk sac stays outside, connected by the vitelline duct<br>- The tube ends blind at both ends, in the foregut and hindgut"),
    au("au-origem-parede", ORG("<b>Layers of the gut wall</b>:<br>- epithelium and gland cells: {{c1::endoderm}}<br>- muscle, connective tissue, serosa: {{c1::splanchnic mesoderm}}"),
       "V-pilar", A_, "Origem das camadas do tubo", 16, "lâminas 10, 16 e 41 (endoderma, mesoderma esplâncnico e crista neural)",
       extra="- Splanchnic mesoderm lines the gut and the somatic mesoderm lines the body wall"),
    K(1489112968862, "A-aula", A_, "O peritônio vem do mesoderma", 17, "lâminas 16–17 (mesoderma esplâncnico e cavidade peritoneal)"),
    K(1486767243259, "V-pilar", A_, "Intestino anterior: do esôfago inferior ao duodeno proximal", 15, "lâmina 15 (derivados do intestino anterior)"),
    K(1486767250072, "V-pilar", A_, "Intestino médio: do duodeno distal aos 2/3 proximais do colo transverso", 15, "lâmina 15 (derivados do intestino médio)"),
    K(1486767254523, "V-pilar", A_, "Intestino posterior: do terço distal do colo transverso ao canal anal", 15, "lâmina 15 (derivados do intestino posterior)"),
    K(1486771325323, "A-aula", A_, "Linha pectínea: endoderma encontra ectoderma", 15, "lâmina 15 (reto do intestino posterior)"),
    K(1486596671662, "V-pilar", A_, "O fígado e a vesícula vêm do intestino anterior", 15, "lâmina 15 (fígado e pâncreas do intestino anterior)"),
    K(1482965424718, "V-pilar", A_, "O pâncreas vem do intestino anterior", 15, "lâmina 15"),
    K(1486767159823, "A-aula", A_, "O intestino anterior é irrigado pelo tronco celíaco", 34, "lâmina 34 (artéria celíaca)"),
    K(1486767163689, "A-aula", A_, "O intestino médio é irrigado pela mesentérica superior", 34, "lâmina 34 (artéria mesentérica superior)"),
    K(1486767179344, "A-aula", A_, "O intestino posterior é irrigado pela mesentérica inferior", 34, "lâmina 34 (artéria mesentérica inferior)"),
    au("au-septo", "The septum transversum is splanchnic mesoderm that forms the central tendon of the {{c1::diaphragm}} and receives the {{c1::liver}}",
       "V-pilar", A_, "Septo transverso: tendão central do diafragma e leito do fígado", 18, "lâmina 18 (septo transverso separa tórax e saco vitelino; origina o tendão central)",
       extra="- It lies between the heart and the yolk-sac stalk<br>- The hepatic bud grows into it"),
    # Bloco B — o estômago gira (lâminas 25–32)
    au("au-vago", "The 90° turn of the stomach brings the left vagus to its {{c1::anterior}} wall and the right to the {{c1::posterior}}",
       "V-pilar", B_, "A rotação de 90° leva o vago esquerdo para a frente", 29, "lâminas 28–29 (rotação de 90° no eixo craniocaudal e nervos vagos)",
       extra="- The stomach turns clockwise around its long axis<br>- This is why the anterior vagal trunk is the left one"),
    au("au-curv-maior", "The posterior wall of the stomach grows faster than the anterior one and forms the {{c1::greater curvature}}",
       "V-pilar", B_, "A parede posterior cresce mais e forma a curvatura maior", 29, "lâminas 28–29 (parede posterior cresce mais rápido)",
       extra="- The slower anterior wall forms the lesser curvature"),
    au("au-mesogastrio", ORG("<b>Mesentery of the stomach</b>:<br>- ventral mesogastrium gives the {{c1::lesser omentum}}<br>- dorsal mesogastrium gives the {{c1::greater omentum}}"),
       "V-pilar", B_, "Mesogástrio ventral e dorsal", 30, "lâmina 30 (pequeno omento A e grande omento B)",
       extra="- The ventral one also gives the falciform ligament<br>- The dorsal one stretches like an apron over the intestines"),
    au("au-bolsa", "The rotation of the stomach pulls the dorsal mesogastrium to the left and opens the {{c1::omental bursa}} behind it",
       "A-aula", B_, "A rotação cria a bolsa omental", 30, "lâminas 29–31 (rotação, mesogástrio dorsal para a esquerda); Langman cap. 15",
       extra="- The bursa opens to the rest of the peritoneal cavity through the epiploic foramen"),
    K(1486605759797, "A-aula", B_, "O omento menor: ligamentos gastro-hepático e hepatoduodenal", 30, "lâmina 30 (pequeno omento)"),
    K(1486605785335, "A-aula", B_, "O omento maior: ligamentos gastrocólico e gastroesplênico", 30, "lâmina 30 (grande omento)"),
    K(1486605738754, "A-aula", B_, "Ligamento gastro-hepático liga o fígado à curvatura menor", 30, "lâmina 30 (ligamentos do pequeno omento)"),
    K(1482971264299, "R-detalhe", B_, "O baço vem do mesoderma", 30, "lâminas 30 e 50 (baço no mesogástrio dorsal)"),
    K(1482971271910, "A-aula", B_, "O baço do intestino anterior é irrigado pela celíaca", 30, "lâmina 30 e Ninja Nerd (baço no mesogástrio dorsal)"),
    # Bloco C — os intestinos (lâminas 34–44)
    au("au-limbos", ORG("<b>Primary loop of the midgut</b>:<br>- cephalic limb forms {{c1::jejunum}} and ileum<br>- caudal limb forms {{c1::cecum}} and ascending colon"),
       "A-aula", C_, "Ramos cefálico e caudal da alça intestinal", 37, "lâminas 36–37 (porção cefálica e caudal do intestino médio)",
       extra="- The superior mesenteric artery runs along the axis of the loop"),
    au("au-hernia-porque", "The midgut herniates into the umbilical cord because the abdomen is too small for the fast-growing loop and the {{c1::liver}}",
       "V-pilar", C_, "Por que a alça herniá", 36, "lâmina 36 (herniação na 6ª ou 7ª semana); Langman cap. 15",
       extra="- The liver is large at this stage because it is a hematopoietic organ"),
    K(1486596675590, "A-aula", C_, "A alça herniá pelo anel umbilical na sexta semana", 36, "lâmina 36 (herniação 6ª ou 7ª semana)"),
    au("au-4etapas", ORG("<b>Midgut loop in four steps</b>:<br>- growth<br>- {{c1::herniation}}<br>- 90° rotation<br>- return with {{c2::180°}} rotation"),
       "V-pilar", C_, "Quatro etapas da formação dos intestinos", 36, "lâmina 36 (crescimento, herniação, rotação de 90°, retração com 180°)",
       extra="- The two rotations sum to 270° counterclockwise"),
    K(1486596678532, "V-pilar", C_, "Na décima semana a alça volta e completa 270° anti-horários", 36, "lâmina 36 (retração com rotação de 180° na 10ª semana)"),
    au("au-fixacao", "After the return, the ascending and descending colon fuse to the posterior wall and become {{c1::secondarily retroperitoneal}}",
       "A-aula", C_, "Fixação dos intestinos", 39, "lâmina 39 (fixação dos intestinos delgado e grosso); Langman cap. 15",
       extra="- The mesentery proper of the small intestine stays free"),
    K(1489112951090, "V-pilar", C_, "O plexo mioentérico vem da crista neural", 41, "lâmina 41 (plexos submucoso e mioentérico, crista neural, Pax-3)"),
    K(1482289554846, "A-aula", C_, "O ducto vitelino liga o saco vitelino ao intestino médio", 43, "lâminas 10 e 43 (remanescente do ducto vitelino)"),
    K(1463526273142, "A-aula", C_, "Fechamento parcial do ducto vitelino dá o Meckel", 43, "lâmina 43 (remanescente proximal do ducto vitelino)"),
    K(1463526266052, "A-aula", C_, "Falha total do fechamento do ducto vitelino dá a fístula vitelina", 43, "lâmina 43 (ducto vitelino)"),
    K(1482289502594, "V-pilar", C_, "O divertículo de Meckel é a persistência do ducto vitelino", 43, "lâmina 43 (remanescente proximal do ducto vitelino)"),
    K(1482289491610, "A-aula", C_, "O Meckel é um divertículo verdadeiro", 43, "lâmina 43"),
    K(1482289539018, "A-aula", C_, "O Meckel pode conter mucosa gástrica ou tecido pancreático", 43, "lâmina 43 (pode conter tecido gástrico ou pancreático)"),
    K(1482289549128, "R-detalhe", C_, "O Meckel costuma ser assintomático", 43, "lâmina 43 (assintomático)"),
    K(1482274965376, "A-aula", C_, "Onfalocele: a alça persiste no cordão umbilical", 42, "lâmina 42 (onfalocele)"),
    K(1482274971453, "A-aula", C_, "Onfalocele: falha do retorno da alça herniada", 42, "lâminas 36 e 42"),
    K(1486596683598, "A-aula", C_, "Hérnia umbilical: o anel umbilical não fecha", 42, "lâmina 42 (hérnia umbilical congênita)"),
    K(1482959873096, "A-aula", C_, "Má rotação intestinal: falha da rotação da alça", 42, "lâmina 42 (rotação anormal do intestino)"),
    K(1482886567135, "V-pilar", C_, "Hirschsprung: gânglios não chegam aos plexos", 44, "lâmina 44 (agangliose por falha de migração)"),
    K(1482886572434, "A-aula", C_, "Os gânglios vêm da crista neural", 44, "lâmina 44 (migração das células da crista neural)"),
    K(1482886576526, "A-aula", C_, "Hirschsprung: mutação do gene RET", 44, "lâmina 44 (proto-oncogene RET)"),
    K(1482878964408, "A-aula", C_, "Hirschsprung: reto e sigmoide distal sem relaxamento", 44, "lâmina 44 (megacólon congênito)"),
    # Bloco D — brotos do fígado e do pâncreas (lâminas 46–55)
    au("au-conx-endoderma", "The endoderm that was folded into the gut tube now buds out the liver and the {{c1::pancreas}}",
       "A-aula", D_, "Do tubo aos brotos", 46, "lâmina 46 (brotamento das glândulas); conexão com o bloco anterior",
       extra="- The buds grow into the mesoderm around the foregut"),
    au("au-broto-hepatico", "The liver starts as the {{c1::hepatic bud}}, an outgrowth of the caudal foregut endoderm that invades the septum transversum",
       "V-pilar", D_, "Broto hepático invade o septo transverso", 49, "lâminas 48–49 (evaginação do endoderma ventral e proliferação no septo transverso)",
       extra="- It appears in the third week<br>- Its connection with the gut narrows into the bile duct"),
    au("au-parenquima", ORG("<b>Origins of the liver</b>:<br>- hepatocytes and bile ducts: {{c1::endoderm}}<br>- stroma, Kupffer and blood cells: {{c1::mesoderm}}"),
       "V-pilar", D_, "Origem dos componentes do fígado", 48, "lâmina 48 (endoderma forma parênquima e ductos; mesênquima forma estroma e hematopoiese)",
       extra="- The mesenchyme comes from the septum transversum"),
    au("au-conx-omento", "The liver grew inside the ventral mesentery, so the lesser omentum and the falciform ligament are the {{c1::remnants}} around it",
       "A-aula", D_, "Omento menor e ligamento falciforme vêm do mesentério ventral", 49, "lâminas 30, 49 e 50 (conexão entre fígado e mesentério ventral); Langman cap. 15",
       extra="- The free edge of the falciform ligament carries the umbilical vein<br>- The free edge of the lesser omentum carries the portal triad"),
    K(1486605712112, "A-aula", D_, "O ligamento falciforme é derivado do mesentério ventral", 49, "lâminas 30 e 49 (mesentério ventral e fígado)"),
    K(1486605702844, "A-aula", D_, "O ligamento falciforme liga o fígado à parede anterior", 49, "lâmina 49 (mesentério ventral)"),
    K(1472319992978, "A-aula", D_, "O ligamento redondo é a veia umbilical obliterada", 49, "Langman cap. 15 (margem livre do ligamento falciforme)"),
    au("au-conx-sinusoide", "The hepatic cords mix with the vitelline and umbilical veins, and these vessels become the {{c1::sinusoids}}",
       "A-aula", D_, "As veias vitelinas e umbilicais formam os sinusoides", 49, "Langman cap. 15 (cordões hepáticos e sinusoides)",
       extra="- This is how the portal circulation ends up inside the liver"),
    au("au-rotacao-orgaos", "The rotation of the stomach and duodenum places the liver on the {{c1::right}} and the spleen on the {{c1::left}}",
       "A-aula", D_, "Posição do fígado e do baço", 50, "lâmina 50 (rotação e posicionamento do fígado à direita e do estômago à esquerda)",
       extra="- The liver was at first on the midline"),
    au("au-brotos-pancreas", "The pancreas forms from a {{c1::dorsal}} and a ventral bud of the duodenal endoderm",
       "V-pilar", D_, "Dois brotos pancreáticos", 52, "lâmina 52 (precursor dorsal e ventral aos 30, 32 e 35 dias)",
       extra="- The dorsal bud appears first<br>- The ventral bud is close to the hepatic bud"),
    au("au-conx-duodeno", "The duodenum swings right and carries the {{c1::ventral}} pancreatic bud behind it to meet the dorsal bud",
       "V-pilar", D_, "A rotação do duodeno leva o broto ventral até o dorsal", 53, "lâmina 53 (fusão pancreática); Langman cap. 15",
       extra="- The two buds and their ducts then fuse"),
    K(1482971236131, "A-aula", D_, "A cabeça do pâncreas vem dos dois brotos", 53, "lâmina 53 (fusão dos brotos dorsal e ventral)"),
    K(1482971220318, "A-aula", D_, "O processo uncinado vem do broto ventral", 53, "lâmina 53"),
    K(1482971225208, "A-aula", D_, "Corpo, cauda e istmo vêm do broto dorsal", 53, "lâmina 53"),
    K(1482971213105, "A-aula", D_, "O ducto pancreático principal vem dos dois brotos", 53, "lâmina 53 (fusão dos ductos)"),
    K(1482971231424, "A-aula", D_, "O ducto acessório vem do broto dorsal", 53, "lâmina 53"),
    K(1482971243363, "R-detalhe", D_, "Pâncreas anular: o broto ventral rodeia o duodeno", 53, "lâmina 53 (falha da rotação do broto ventral)"),
    K(1482971258399, "R-detalhe", D_, "Pâncreas divisum: os brotos não se fundem", 53, "lâmina 53 (fusão dos brotos)"),
    au("au-retroperitoneal", "The pancreas ends up {{c1::retroperitoneal}} because the duodenum and its mesentery fuse with the posterior abdominal wall",
       "A-aula", D_, "Posição retroperitoneal do pâncreas", 53, "lâmina 53; Langman cap. 15 (posição do pâncreas)",
       extra="- The dorsal mesentery of the duodenum disappears, so the gland lies against the posterior wall"),
    K(1486777651171, "A-aula", D_, "Colédoco e ducto pancreático desembocam na ampola de Vater", 53, "lâminas 49 e 53 (ducto biliar e ductos pancreáticos)"),
    # Bloco E — o pâncreas por dentro (lâminas 58–67)
    au("au-acino-zimogenio", "Pancreatic acinar cells store enzymes in apical {{c1::zymogen}} granules",
       "V-pilar", E_, "Grânulos de zimogênio das células acinares", 65, "lâmina 65 (grânulos de tripsinogênio, quimotripsinogênio, carboxipeptidases, amilase e lipase)",
       extra="- The granules are released by exocytosis into the lumen of the acinus<br>- The cell has abundant rough ER"),
    K(1462120796565, "A-aula", E_, "As ilhotas de Langerhans são a porção endócrina do pâncreas", 61, "lâmina 61 (ilhotas pancreáticas e porção exócrina)"),
    K(1482115296382, "V-pilar", E_, "As células acinares secretam as enzimas pancreáticas", 65, "lâmina 65 (grânulos de secreção)"),
    K(1482115500165, "V-pilar", E_, "As proteases pancreáticas são secretadas inativas", 65, "lâmina 65 (tripsinogênio e quimotripsinogênio)"),
    K(1482115492876, "A-aula", E_, "A enteropeptidase ativa o tripsinogênio", 65, "lâmina 65 (tripsinogênio)"),
    K(1482115504921, "A-aula", E_, "A tripsina ativa todas as pró-enzimas", 65, "lâmina 65 (tripsinogênio, quimotripsinogênio, carboxipeptidases)"),
    K(1482115420919, "A-aula", E_, "A amilase pancreática hidrolisa o amido", 65, "lâmina 65 (amilase)"),
    K(1482115541696, "A-aula", E_, "A lipase pancreática digere gordura no intestino", 65, "lâmina 65 (lipase, colesterol esterase, fosfolipase)"),
    K(1482115305907, "V-pilar", E_, "As células dos ductos secretam a parte aquosa", 66, "lâmina 66 (bicarbonato e água)"),
    K(1482115316095, "A-aula", E_, "As células dos ductos secretam bicarbonato", 66, "lâmina 66 (bicarbonato e água)"),
    K(1482021827543, "A-aula", E_, "A CCK vem das células I do duodeno", 67, "lâmina 67 (células enteroendócrinas e colecistoquinina)"),
    K(1482021831523, "A-aula", E_, "A CCK aumenta a secreção das enzimas pancreáticas", 67, "lâmina 67 (colecistoquinina)"),
    K(1482021883479, "A-aula", E_, "A secretina vem das células S do duodeno", 67, "lâmina 67 (secretina)"),
    K(1482021886990, "A-aula", E_, "A secretina aumenta o bicarbonato pancreático", 67, "lâmina 67 (secretina)"),
    # Bloco F — o fígado por dentro (lâminas 68–90)
    au("au-porta-duas", "The liver gets nutrient-rich blood from the {{c1::portal vein}} and oxygen-rich blood from the {{c1::hepatic artery}}",
       "V-pilar", F_, "Duplo suprimento do fígado", 71, "lâminas 69–71 (veia porta e artéria hepática chegam ao fígado)",
       extra="- The portal vein drains the gut, so the absorbed nutrients reach the hepatocytes first"),
    au("au-porco", "In pig liver the lobules are clearly separated by connective tissue, whereas the human liver shows {{c1::no visible lobulation}}",
       "A-aula", F_, "Lóbulo do fígado de porco e do humano", 75, "lâminas 74–75 (fígado de porco e fígado humano); roteiro de aulas práticas da Profa. Patrícia Gama",
       extra="- The portal spaces mark the corners of each pig lobule<br>- In the human slide look for the cords of hepatocytes and the sinusoids"),
    K(1486775502282, "V-pilar", F_, "Tríade portal: ducto biliar, artéria hepática e veia porta", 77, "lâminas 77–78 (espaço porta com veia, artéria e ducto)"),
    K(1486605719941, "A-aula", F_, "O ligamento hepatoduodenal contém a tríade portal", 77, "lâmina 77 (espaço porta)"),
    K(1486776257809, "V-pilar", F_, "Os cantos do hexágono são os espaços porta", 76, "lâminas 75–78 (lóbulo clássico e espaço porta)"),
    K(1486776254440, "V-pilar", F_, "O centro do hexágono é a veia central", 76, "lâminas 74–76 (veia centrolobular)"),
    K(1486776235726, "A-aula", F_, "Ramos portais terminais abrem para os sinusoides", 77, "lâminas 77–78 (sangue chega aos vértices dos lóbulos)"),
    K(1486776242882, "V-pilar", F_, "O sangue flui do espaço porta à veia central", 78, "lâmina 78 (o sangue chega aos vértices e vai à veia central)"),
    K(1486776248771, "V-pilar", F_, "A bile flui da veia central ao espaço porta", 82, "lâmina 82 (a bile corre em sentido contrário ao da circulação)"),
    au("au-canaliculo", "Bile canaliculi are grooves between neighboring {{c1::hepatocytes}} and get their own wall only in the portal space",
       "V-pilar", F_, "Canalículos biliares", 82, "lâminas 81–82 (canalículos entre hepatócitos, parede própria no espaço porta)",
       extra="- The canaliculi drain into the bile ducts of the portal space"),
    au("au-sinusoide", "Hepatic sinusoids are {{c1::fenestrated}} capillaries without a continuous basement membrane",
       "A-aula", F_, "Sinusoide hepático", 79, "lâminas 76–79 (sinusoides); Junqueira cap. 16",
       extra="- This lets plasma reach the hepatocytes in the space of Disse"),
    K(1486776332176, "V-pilar", F_, "As células de Kupffer são macrófagos do sinusoide", 80, "lâmina 80 (células de Kupffer)"),
    K(1486776339459, "A-aula", F_, "O espaço de Disse fica entre hepatócito e sinusoide", 80, "lâminas 80–81; Junqueira cap. 16"),
    K(1486776347708, "R-detalhe", F_, "As células estreladas guardam vitamina A", 80, "Junqueira cap. 16 (células de Ito no espaço de Disse)"),
    K(1486776353051, "R-detalhe", F_, "As células estreladas ativadas produzem matriz", 80, "Junqueira cap. 16 (células de Ito)"),
    K(1486776314995, "A-aula", F_, "A face basolateral do hepatócito encara o sinusoide", 81, "lâmina 81 (hepatócito)"),
    K(1486776304662, "A-aula", F_, "A face apical do hepatócito forma o canalículo biliar", 81, "lâmina 81 (canalículo bilífero)"),
    au("au-organelas", "In the hepatocyte the rough ER makes plasma proteins like {{c1::albumin}} and the smooth ER {{c2::detoxifies}} drugs",
       "V-pilar", F_, "Organelas do hepatócito", 87, "lâmina 87 (REG: albumina, protrombina, fibrinogênio; REL: detoxificação)",
       extra="- The smooth ER also makes the lipids of lipoproteins and relates to glycogen"),
    au("au-acino", "The hepatic acinus is the smallest unit supplied by a terminal {{c1::portal vein}} branch and drained by a {{c1::bile duct}}",
       "V-pilar", F_, "Ácino hepático", 90, "lâmina 90 (menor porção irrigada pelo último ramo da veia porta e drenada por um duto biliar)",
       extra="- It is centered on the portal space"),
    K(1486776364876, "V-pilar", F_, "A zona 1 do ácino é a periportal", 90, "lâmina 90 (zonas 1, 2 e 3)"),
    K(1486776370260, "A-aula", F_, "A zona 2 é a intermediária", 90, "lâmina 90 (zonas)"),
    K(1486776374938, "V-pilar", F_, "A zona 3 é a pericentral", 90, "lâmina 90 (zonas)"),
    au("au-zona-o2", "Acinus zone 1 receives the most oxygen and zone 3, near the central vein, the {{c1::least}}",
       "V-pilar", F_, "Oxigenação das zonas do ácino", 90, "lâmina 90 (zonas que recebem quantidades diferentes de O2)",
       extra="- Blood loses oxygen as it crosses the sinusoids"),
    K(1486776394241, "A-aula", F_, "A zona 3 contém o citocromo P450", 90, "lâmina 90 e 87 (REL e detoxificação)"),
    K(1482115360476, "A-aula", F_, "O fígado sintetiza a bile", 81, "lâminas 81–82 (hepatócito produz a bile)"),
]


_CZ = _re.compile(r"\{\{c(\d+)::((?:(?!\}\}).)*?)(::(?:(?!\}\}).)*?)?\}\}", _re.S)
def _bold_cloze(t):
    def sub(m):
        corpo = m.group(2)
        if "<b>" not in corpo and "<strong>" not in corpo:
            corpo = f"<b>{corpo}</b>"
        return "{{c%s::%s%s}}" % (m.group(1), corpo, m.group(3) or "")
    return _CZ.sub(sub, t)
for _c in CARDS:
    if _c["kind"] == "autoral":
        _c["text"] = _bold_cloze(_c["text"])

exec((HERE / "exclusoes.py").read_text(encoding="utf-8")) if (HERE / "exclusoes.py").exists() else None
_CENTRAIS = [("pilares", *[c["key"] for c in CARDS if c.get("cod") == "V-pilar"])]
finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1482021831523": "- Parasympathetic acetylcholine also makes the acinar cells release their enzymes",
 "ak1489112981171": "- So the gut lining and the glands of the liver and pancreas share the same germ layer",
 "ak1486767250072": "- The midgut is supplied by the superior mesenteric artery",
 "ak1486767254523": "- The anal canal below the pectinate line comes from ectoderm",
 "ak1486596671662": "- The liver and gallbladder bud from the caudal foregut",
 "ak1482965424718": "- The pancreas buds from the duodenum, which is part of the foregut",
 "ak1482971264299": "- It forms between the two layers of the dorsal mesogastrium, so it moves with the stomach rotation",
 "ak1463526273142": "- The part of the duct that stays open next to the ileum becomes the Meckel diverticulum",
 "ak1463526266052": "- The open duct connects the ileum to the umbilicus, so intestinal content leaks out",
 "ak1489112968862": "- The gut wall muscle and the peritoneum both come from the mesoderm",
 "ak1489112951090": "- The enteric plexuses are made by neural crest cells that migrate into the gut wall",
 "ak1482274965376": "- The herniated loop stays covered by a sac of peritoneum",
 "ak1482289491610": "- The wall has mucosa, submucosa and muscularis, like the ileum it hangs from",
 "ak1482886572434": "- The neural crest cells fail to finish their migration to the distal gut",
 "ak1486605702844": "- It comes from the ventral mesentery that the liver grew into",
 "ak1472319992978": "- The umbilical vein closes after birth and leaves this ligament",
 "ak1462120796565": "- They are scattered among the exocrine acini of the gland",
 "ak1482115316095": "- This makes the juice alkaline, which protects the duodenum from the stomach acid",
 "ak1486776257809": "- Each corner of the lobule holds a portal space with the triad",
 "ak1486776254440": "- Blood from the sinusoids drains into this vein",
 "ak1486605719941": "- The triad runs in the free edge of the lesser omentum",
 "ak1486776339459": "- Plasma bathes the microvilli of the hepatocytes here",
 "ak1486776314995": "- Blood plasma reaches this face through the space of Disse",
 "ak1486776304662": "- The bile canaliculus is the groove between two hepatocyte apical faces",
 "ak1482115360476": "- Hepatocytes secrete it into the canaliculi",
 "ak1486776248771": "- Bile runs in the opposite direction to the blood, toward the bile ducts of the portal space",
 "ak1486776394241": "- Detoxification is strongest where the oxygen supply is lowest",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "au-septo": "os cards do AnKing dão o fígado como derivado do intestino anterior; este dá o septo transverso, que é o leito do broto e origina o tendão central do diafragma",
 "au-hernia-porque": "o card do AnKing dá a época da herniação; este dá a causa, a cavidade pequena e o fígado grande",
 "au-4etapas": "os cards do AnKing dão a herniação e a rotação de 270° em datas; este ordena as quatro etapas do processo",
 "au-conx-duodeno": "o card do AnKing dá o pâncreas anular; este explica o giro do duodeno que junta os dois brotos",
 "au-porta-duas": "o card do AnKing dá a tríade portal; este dá o que cada vaso traz ao fígado",
 "au-acino": "o card do AnKing dá a zona 1 como periportal; este define o ácino pela veia porta e pelo ducto biliar",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
STRIP_IMG = {"ak1482971264299": ["4d312dd26072007eca47af22e43d3a3a.webp"],
 "ak1486596675590": ["c6e6376c0c4b294e1e2950ea92ac7c10.webp"], "ak1486596678532": ["c6e6376c0c4b294e1e2950ea92ac7c10.webp"],
 "ak1482959873096": ["c12fa413454141f4cec64779b0663e9b.webp"], "ak1482886572434": ["18aa74c7e1e6c6c3f8273e48ab17455c.webp"],
 "ak1482878964408": ["18aa74c7e1e6c6c3f8273e48ab17455c.webp"], "ak1482971243363": ["83a418e20afde833d7f4efeae3ddaa2b.jpg"]}  # figuras que não batem com o cloze do card
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {"objetivo": "Acompanhar a aula: do dobramento do embrião ao tubo digestório, à rotação do estômago, à herniação do intestino, aos brotos do fígado e do pâncreas e à histologia funcional do ácino e do lóbulo.",
          "centrais": _CENTRAIS, "exemplos": [], "outras_aulas": []}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
