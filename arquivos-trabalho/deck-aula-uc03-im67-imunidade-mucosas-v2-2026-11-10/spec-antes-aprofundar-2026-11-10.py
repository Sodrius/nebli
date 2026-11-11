# Especificação curada — 67 Imunidade de mucosas (UC03 P4, Imunologia; aula assíncrona; 29 lâminas + transcrição).
# Ordem = slides. AnKing (seções First Aid de Peyer, IgA e Th17, decididas nota a nota) → NEBLI vivo (sh) → externos → autoral SÓ para lacuna provada.
# Aula de princípio geral (regulação tecido-específica): nenhum bloco é exemplo; o começo (GALT e inflamação fisiológica) e os quatro mecanismos de tolerância são o núcleo.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
_sys.path.insert(0, str(HERE))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 16
SECOES_MOTIVO = ""
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("A aula ensina mecanismos próprios da mucosa que o AnKing não tem (dendrítica tolerogênica por ácido retinoico com IL-10/IDO, "
                   "PRR só basolateral, inflamação fisiológica, retorno dos linfócitos à mucosa, Th3/Tr1, IL-6 decidindo Treg × Th17, olho imunoprivilegiado); "
                   "buscados nos três caminhos em todos os acervos (busca/cobertura.tsv). Tudo o que o acervo tem (Peyer, células M, IgA, pIgR, componente "
                   "secretor, Th17) entrou por AnKing ou por associação a cópias NEBLI vivas; cortar os autorais deixaria blocos inteiros da aula sem card.")
MODO = "aula"
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-im67-20261110a"
SHORT = "im67"
LESSON = "2026-uc03-imunologia-67-imunidade-mucosas"
DECK = "NEBLI::UC03::P4::Imunologia::67 Imunidade de mucosas"
CRITERIOS = "MEMORY.md + pipeline v16 + FEEDBACKS até F-20261109-CODEX-01 + GUIA-1 a GUIA-4 relidos em 10/11/2026"
_IMGS = ("tonsila", "peyer-ileo", "peyer-centro", "iel", "nodulo-colon", "galt-esquema", "vias-inducao", "prr", "iga-plasmocitos", "th3-th17")
MEDIA = {f"im67-{n}.png": f"img/im67-{n}.png" for n in _IMGS}
IMG = lambda n: f'<br><br><img src="im67-{n}.png" style="width:100%;max-width:850px;height:auto">'
BUSCA = ("Três caminhos (10/11): seções First Aid de placas de Peyer, IgA e diferenciação Th17, Physeo/Pixorize de IgA e Th17 (busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e no NEBLI vivo, uma consulta por card "
         "(busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


A_, B_, C_, D_, E_, F_, G_, H_, I_ = ("A-malt", "B-histologia", "C-fisiologica", "D-inducao", "E-dc-tolerancia", "F-prr", "G-iga", "H-treg-th17", "I-olho")
FORA_DO_RECORTE = []
EXCLUIDOS = [
 (1487117247126, "IgA não cruza a placenta: propriedade de isotipo sem relação com a mucosa (aula 17, reconhecimento adaptativo)"),
 (1487117272282, "isotipos que um plasmócito secreta: genérico da aula 49, não ensina a mucosa"),
 (1487116982311, "Th17 no dano autoimune: autoimunidade é das aulas 51 e 72"),
 (1520300403523, "inibição da via Th17 por IFN-γ e IL-4: regulação cruzada dos subsets é da aula 45"),
 (1520300435789, "deficiência de Th17 na síndrome de Job: imunodeficiência, aula 51"),
 (1791023297666, "mucinas das caliciformes (UC08 BT04, suspenso por Davi): detalhe histológico; esta aula cobra a barreira de muco em k-caliciforme"),
 (1791023302370, "lâmina própria do cólon rica em nódulos (UC08, suspenso): contradiz a ênfase da aula (nódulos escassos no cólon); k-nodulo-colon cobre"),
 (1791743343033, "integrinas por C5a e LTB4 (aula 37, suspenso): extravasamento da inflamação aguda, não homing de mucosa"),
 (1791780360378, "macrófago secreta IL-8 (aula 07, suspenso): quimiocina geral, fora desta aula"),
 (1792240074220, "B cells nos folículos do linfonodo (aula 07, suspenso): anatomia do linfonodo, fora desta aula"),
 (1792240074544, "folículo primário denso e dormente (aula 07, suspenso): o centro germinativo da placa de Peyer já entra pelo card do folículo secundário"),
 (1791983685881, "MALT constitutivo × folículo terciário (aula 62, suspenso por Davi): revisor apontou negrito no cloze e sobreposição com k-malt; não volta"),
 (1791780608272, "macrófagos matam o que penetra (aula 39, suspenso por Davi): cloze em verbo com sinônimos; k-prr-basolateral cobre o princípio"),
 (1791780602055, "microbiota estimula tolerância (aula 39, suspenso por Davi): alvo vago (tolerance/maturation); k-tres-tarefas cobre a tolerância aos comensais"),
 (1791625433083, "Treg induzida por TGF-β + ácido retinoico (aula 45): revisor apontou IL-2 como resposta alternativa; k-ac-retinoico e k-dc-il10-ido cobrem"),
 (1791780605649, "dendrítica recebe o antígeno da célula M (aula 07): 'such as' admite macrófago ou B; a célula M HY e k-dc-mesenterico cobrem"),
 (1791780613803, "hipótese da higiene (aula 39, suspenso por Davi): negrito no cloze e Extra sem a cadeia causal (revisor 10/11); a ideia fica no verso de k-tres-tarefas"),
 (1791780601643, "comensais competem e fazem antimicrobianos (aula 39, suspenso por Davi): cloze genérico 'antimicrobial'; k-microbiota cobre com o nome do fenômeno"),
 (1516218740374, "poliovírus em placas de Peyer: ficha de patógeno, virologia é da 58/59"),
 (1510105605930, "Shigella invade por células M: ficha de patógeno (micro); a célula M já entra pelo card HY"),
 (1500056732694, "Giardia e IgA: parasita específico, outra aula"),
 (1497204171184, "natalizumab no Crohn: fármaco e doença, fora do ciclo básico"),
]

CARDS = [
 # ---------- Lâmina 2: MALT, GALT e BALT ----------
 au("k-malt", ORG("Mucosal lymphoid tissue by site:<br><br>- <b>Peyer patches</b> and lamina propria lymphocytes: {{c1::GALT}}<br>- lymphoid tissue of the <b>airways</b>: {{c1::BALT}}"),
    "A-aula", A_, "MALT, GALT e BALT", 2, "lâmina 2; transcrição p.4", motivacao="m1", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="nos brônquios, existe um tecido linfático",
    fontes=F("transcrição p.4", "nos brônquios, existe um tecido linfático"),
    sem_imagem="lâmina 2 é um mapa do corpo inteiro sem MALT destacado; a histologia vem nos cards seguintes",
    extra="Both are parts of the mucosa-associated lymphoid tissue (MALT): gut-associated and bronchus-associated.<br>The gut has its own lymphoid system because it must tolerate food and commensals and still fight pathogens."),
 K(1473289461901, "V-hy", A_, "Escalador mucociliar na mucosa respiratória", 2, "apostila Aula 11: muco e cílios são a defesa inata da mucosa respiratória (BALT)"),
 sh(1791023357519, "azul", A_, "MALT: nódulos e células livres da mucosa", 2, "lâmina 2: definição de MALT (card da aula 07)"),
 # ---------- Lâmina 3: tonsila ----------
 ak("ex1701979294684", 1701979294684, "A-aula", B_, "Tonsilas: tecido linfoide da faringe", 3, "lâmina 3: tonsila", origin="Histology",
    extra_add="Tonsils and adenoids guard the entrance shared by the airway and the gut, with B- and T-cell follicles under the epithelium." + IMG("tonsila")),
 # ---------- Lâminas 4–6: placas de Peyer ----------
 K(1486831445995, "V-hy", B_, "Placas de Peyer no íleo", 4, "lâminas 4–5: placas de Peyer no íleo",
   extra_add="The ileum concentrates the Peyer patches, seen as dark follicles along one side of the cross section." + IMG("peyer-ileo")),
 K(1486608789738, "A-step", B_, "Peyer distingue o íleo", 4, "lâmina 4: placas de Peyer no íleo"),
 K(1486945164044, "V-hy", B_, "Centro germinativo claro", 6, "lâmina 6: áreas claras de proliferação na placa de Peyer",
   extra_add="In a Peyer patch the pale center is the same germinal center, where B cells proliferate and switch to IgA." + IMG("peyer-centro")),
 # ---------- Lâmina 7: IEL e lâmina própria ----------
 au("k-iel-cd8", "<b>Intraepithelial lymphocytes</b> of the <b>small intestine</b> are mostly {{c1::CD8}} T cells",
    "A-aula", B_, "IEL são principalmente CD8", 7, "lâminas 7 e 9; transcrição p.14; apostila", motivacao="m7",
    fontes=F("transcrição p.14", "que são predominantemente CD8 e podem ser do tipo alfa-beta"),
    extra="Many of them carry a γδ T-cell receptor, which recognizes stress molecules of the epithelium without classic antigen presentation.<br>Below the epithelium, the lamina propria holds CD4 and CD8 T cells, plasma cells and macrophages." + IMG("iel")),
 # ---------- Lâmina 8: nódulo solitário do cólon ----------
 au("k-nodulo-colon", ORG("<b>Organized lymphoid tissue</b> along the bowel:<br><br>- <b>ileum</b>, many and large: {{c1::Peyer patches}}<br>- <b>colon</b>, few and scattered: {{c1::solitary lymphoid nodules}}"),
    "R-detalhe", B_, "Nódulo solitário do intestino grosso × Peyer do íleo", 8, "lâmina 8; transcrição p.22–24", motivacao="m6", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="São relativamente poucos, e sua maior concentração ocorre no íleo",
    fontes=F("transcrição p.24", "São relativamente poucos, e sua maior concentração ocorre no íleo"),
    extra="Top figure: ileum cross section with Peyer patches along one side.<br>Bottom figure: colon, the arrow marks a solitary lymphoid nodule." + IMG("peyer-ileo") + IMG("nodulo-colon")),
 au("k-infl-fisiologica", ORG("<b>Physiological inflammation</b> of the gut lamina propria:<br><br>- <b>healthy gut</b>: lymphocytes and {{c1::plasma cells}}, no damage<br>- <b>pathogen invasion</b>: rapid influx of {{c1::neutrophils}}"),
    "V-pilar", C_, "Inflamação fisiológica × invasão com neutrófilos", 9, "lâminas 9–10; transcrição p.28–30", motivacao="m8", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Assim, há uma grande quantidade de células, mas não se trata de",
    fontes=F("lâmina 10", "aparecem rapidamente PMNs"),
    sem_imagem="lâminas 9–10 são texto; a histologia da lâmina própria cheia está no card dos linfócitos intraepiteliais",
    extra="The healthy infiltrate faces food and commensals.<br>It looks like chronic inflammation but causes no damage, so digestion and absorption go on.<br>Neutrophils mark that a pathogen crossed the barrier and the response switched to defense."),
 au("k-homing", "Lymphocytes activated in <b>gut lymphoid tissue</b> <b>home back</b> as effectors to the intestinal {{c1::lamina propria}}",
    "V-pilar", D_, "Linfócitos ativados na mucosa voltam à mucosa", 11, "lâmina 11; transcrição p.36; Janeway 12.6", motivacao="m14",
    fontes=F("transcrição p.36", "células efetoras. Isso é fundamental por dois"),
    sem_imagem="lâmina 11 é uma pergunta em texto; o percurso aparece no esquema das vias de indução",
    extra="Gut dendritic cells imprint gut-homing receptors (integrin α4β7, CCR9) through retinoic acid.<br>So the effectors return to the site of the antigen, already tuned to the regulated mucosal pattern."),
 # ---------- Lâmina 12: barreiras e célula M ----------
 K(1486608768857, "A-aula", D_, "Paneth secreta defensinas", 12, "lâmina 12: células de Paneth e peptídeos antimicrobianos",
   extra_add="Defensins add to the antimicrobials made by commensals and keep bacteria away from the crypt."),
 au("k-caliciforme", "In the <b>intestine</b>, {{c1::goblet}} cells secrete the <b>mucus layer</b> that keeps luminal bacteria away from the epithelium",
    "A-aula", D_, "Caliciformes fazem a barreira de muco", 12, "lâmina 12; transcrição p.26 e 32", motivacao="m10",
    fontes=F("transcrição p.26", "caliciformes forma uma barreira gelatinosa"),
    extra="A bacterium must cross this gel to touch the epithelium.<br>Paneth-cell defensins act inside the mucus." + IMG("galt-esquema")),
 au("k-microbiota", "Gut <b>commensal bacteria</b> keep pathogens from settling by competing for space and nutrients, a protection called {{c1::colonization resistance}}",
    "A-aula", D_, "Microbiota protege por competição", 12, "transcrição p.6", motivacao="m11",
    fontes=F("transcrição p.6", "ocupam espaço no tubo digestivo, competindo com outras bactérias"),
    sem_imagem="dado da fala, sem figura própria na aula",
    extra="Commensals also secrete antimicrobial peptides that inhibit pathogens.<br>So tolerating them is protective, not just harmless."),
 K(1486831448616, "V-hy", D_, "Células M amostram antígeno", 12, "lâminas 12–13: célula M sobre a placa de Peyer"),
 # ---------- Lâmina 13: dendrítica e linfonodo mesentérico ----------
 au("k-dc-mesenterico", "<b>Gut dendritic cells</b> sample the lumen and carry antigen through lymphatics to the {{c1::mesenteric}} lymph node",
    "V-pilar", D_, "Dendrítica leva o antígeno ao linfonodo mesentérico", 13, "lâmina 13; transcrição p.34; prova UC03 (DC intestinal)", motivacao="m13",
    fontes=F("transcrição p.34", "linfonodo mesentérico"),
    extra="This is the second route of induction, beside M cells over Peyer patches.<br>In the node the dendritic cell presents to T cells, and B cells meet the antigen directly." + IMG("vias-inducao")),
 # ---------- Lâmina 14: as três tarefas ----------
 au("k-tres-tarefas", "The <b>gut immune system</b> stays <b>tolerant</b> to {{c1::food}} antigens and {{c1::commensal bacteria}} while still responding to pathogens",
    "V-pilar", E_, "Tolerância à comida e aos comensais, resposta a patógeno", 14, "lâmina 14; transcrição p.38", motivacao="m15",
    fontes=F("lâmina 14", "Tolerância à comida"),
    sem_imagem="lâmina 14 é texto; o card fecha o que os mecanismos seguintes explicam",
    extra="Food is the most essential symbiosis and commensals protect the gut, so attacking either would harm the host.<br>Tolerance here is active: tolerogenic dendritic cells, IgA and regulatory T cells, as the next cards show."),
 # ---------- Lâminas 15–17: dendrítica soft ----------
 au("k-ac-retinoico", "<b>Gut dendritic cells</b> become <b>tolerogenic</b> under {{c1::retinoic acid}}, a vitamin A derivative made by epithelium and dendritic cells",
    "V-pilar", E_, "Ácido retinoico torna a dendrítica tolerogênica", 16, "lâminas 15–16; transcrição p.40–42; Janeway 12.8", motivacao="m16",
    fontes=F("lâmina 16", "ácido retinoico, um derivado da"),
    sem_imagem="lâminas 15–16 são texto; não há figura real do condicionamento da dendrítica na aula",
    extra="The local microenvironment, not the antigen, sets this soft behavior.<br>Retinoic acid also imprints gut homing and helps naive CD4 cells become Tregs."),
 au("k-dc-il10-ido", "<b>Tolerogenic gut dendritic cells</b> secrete IL-10 and the <b>tryptophan-degrading</b> enzyme {{c1::IDO}}, which favor regulatory T cells",
    "A-aula", E_, "Dendrítica produz IL-10 e IDO", 16, "lâmina 16; transcrição p.42", motivacao="m17",
    fontes=F("lâmina 16", "Produzem IL-10 e IDO"),
    sem_imagem="lâmina 16 é texto",
    extra="IDO is indoleamine 2,3-dioxygenase: it starves nearby T cells of tryptophan.<br>IL-10 dampens antigen presentation, so antigen shown in this context induces tolerance."),
 au("k-dc-proinfl", ORG("<b>Gut dendritic cells</b> by behavior:<br><br>- the {{c1::majority}}: <b>tolerogenic</b>, induce regulatory T cells<br>- a {{c1::minority}}: <b>pro-inflammatory</b>, start defense"),
    "A-aula", E_, "Algumas dendríticas são pró-inflamatórias", 17, "lâmina 17; transcrição p.44", motivacao="m18", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Portanto, o comportamento predominante das células dendríticas",
    fontes=F("lâmina 17", "algumas DCs pró-"),
    sem_imagem="lâmina 17 é texto",
    extra="The minority is the backup plan that lets the mucosa switch from tolerance to defense.<br>In a viral infection they make IL-12 and type I interferon and help B cells become IgA plasma cells."),
 au("k-prr-basolateral", ORG("<b>Gut epithelial cells</b> keep pattern recognition receptors where only <b>invading</b> bacteria meet them:<br><br>- <b>Toll-like</b> receptors: {{c1::basolateral}} membrane<br>- <b>NOD-like</b> receptors: {{c1::cytosol}}"),
    "V-pilar", F_, "PRR só basolateral e citosólico", 19, "lâminas 18–19; transcrição p.46–48; apostila", motivacao="m19", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Em vez disso, esses receptores estão presentes no citosol, como",
    fontes=F("lâmina 18", "Não ha PRRs na superfície apical"),
    extra="There are none on the apical, lumenal surface, so bacteria that only touch it are ignored.<br>A microbe that enters the cell or crosses to the lamina propria triggers inflammation." + IMG("prr")),
 K(1487117227757, "V-hy", G_, "IgA protege o trato gastrointestinal", 20, "lâmina 20: resposta humoral da mucosa por IgA"),
 K(1487117209824, "V-hy", G_, "IgA é o anticorpo mais produzido", 20, "apostila: IgA é a maior parte dos anticorpos produzidos"),
 au("k-iga-neutraliza", "<b>Secretory IgA</b> protects mucosae mainly by {{c1::neutralization}}, blocking microbial adhesion and toxins without complement or inflammation",
    "V-prova", G_, "IgA só neutraliza, sem inflamar", 20, "lâmina 20; transcrição p.50 e 58; apostila; prova UC03 (sIgA)", motivacao="m20",
    fontes=F("transcrição p.58", "neutralização. Imagine, por exemplo, uma ba"),
    sem_imagem="lâmina 20 é texto; a figura de plasmócitos de IgA está no card da lâmina 21",
    extra="Its Fc does not fix complement, opsonize or degranulate mast cells, so it protects without damaging the mucosa.<br>It binds the bacterial molecules used to attach, so the microbe never reaches the epithelium."),
 au("k-iga-aglutina", "Besides blocking adhesion, <b>secretory IgA</b> traps microbes in the <b>mucus</b> by {{c1::agglutination}}, and they leave with the feces",
    "A-aula", G_, "IgA aglutina e elimina pelas fezes", 20, "prova UC03 (gabarito: aglutinar partículas virais e eliminar pelas fezes); transcrição p.58", motivacao="m20",
    fontes=F("prova UC03 2025 P3 2.2", "aglutinar partículas virais e favorece"),
    sem_imagem="gabarito de prova em texto",
    extra="Being dimeric, IgA has four binding sites and cross-links microbes.<br>Clumped microbes stay trapped in the mucus and cannot reach the epithelium."),
 K(1487117240890, "V-hy", G_, "IgA não fixa complemento", 20, "transcrição p.50: Fc da IgA não ativa complemento"),
 K(1487117238120, "V-hy", G_, "IgA nas secreções", 20, "lâmina 20: IgA das mucosas"),
 K(1487117234083, "V-hy", G_, "IgA no leite", 20, "transcrição p.74: o leite materno traz IgA"),
 K(1487117156031, "A-aula", G_, "TGF-β favorece a troca para IgA", 20, "transcrição p.52: produção de IgA incentivada por TGF-β"),
 K(1487117216624, "V-hy", G_, "IgA monomérica no sangue", 20, "transcrição p.50: IgA monomérica ou dimérica"),
 K(1487117219869, "V-hy", G_, "IgA dimérica com cadeia J", 20, "transcrição p.54: a forma dimérica tem função especial"),
 K(1487117251418, "V-hy", G_, "IgA liga o receptor poli-Ig", 20, "transcrição p.54: receptor poli-Ig"),
 K(1487117223955, "A-step", G_, "Transcitose da IgA", 20, "transcrição p.54: transporte através da célula epitelial"),
 K(1487117255825, "V-hy", G_, "Componente secretor protege das proteases", 20, "transcrição p.54: peça secretória resistente às enzimas"),
 K(1486831451445, "A-step", G_, "Plasmócitos de IgA na lâmina própria", 21, "lâmina 21: plasmócitos de IgA predominam na lâmina própria",
   extra_add="In the colon mucosa IgA plasma cells (green) far outnumber IgG plasma cells (red)." + IMG("iga-plasmocitos")),
 # ---------- Lâminas 22–27: células reguladoras e Treg × Th17 ----------
 au("k-reguladoras", ORG("<b>Regulatory</b> CD4 cells induced in the gut mucosa, by cytokine:<br><br>- make <b>TGF-β</b>: {{c1::Th3}} cells<br>- make <b>IL-10</b>: {{c1::Tr1}} cells"),
    "V-pilar", H_, "Treg induzida, Th3 e Tr1", 22, "lâmina 22; transcrição p.58–60", motivacao="m25", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="favorece a indução de células reguladoras",
    fontes=F("lâmina 22", "TRs produtoras de IL-10"),
    sem_imagem="lâmina 22 é uma lista em texto",
    extra="They join the FoxP3+ Tregs induced locally by TGF-β, which outnumber thymic Tregs in the gut.<br>Together they keep the many effector cells of the lamina propria from causing inflammation."),
 au("k-il10-colite", "Without {{c1::IL-10}} from regulatory cells, the gut response to commensals is unchecked and severe <b>colitis</b> develops",
    "A-aula", H_, "Sem IL-10 há inflamação intestinal grave", 22, "transcrição p.60", motivacao="m26",
    fontes=F("transcrição p.60", "células reguladoras produtoras de IL-10"),
    sem_imagem="dado experimental em texto na fala do professor",
    extra="Mice that cannot make IL-10 develop intestinal inflammation severe enough to kill many of them.<br>Gut tolerance is an active process, not ignorance."),
 K(1487116967325, "A-step", H_, "Treg: CD25 e FoxP3", 22, "lâmina 22: Treg induzidas FoxP3+"),
 K(1487116971703, "A-aula", H_, "Treg secreta IL-10 e TGF-β", 22, "lâmina 22: Th3 (TGF-β) e Tr1 (IL-10)"),
 K(1489970615786, "V-hy", H_, "IL-10 atenua a inflamação", 22, "transcrição p.60: importância da IL-10"),
 K(1487981558376, "V-hy", H_, "TGF-β inibe a inflamação", 22, "lâmina 25: TGF-β no ambiente da mucosa"),
 au("k-treg-th17", ORG("Naive CD4 T cells in gut <b>TGF-β</b>:<br><br>- <b>TGF-β alone</b>, no IL-12: {{c1::Th3}} and other Tregs<br>- <b>plus IL-6</b>: {{c1::Th17}}"),
    "V-pilar", H_, "IL-6 decide entre Treg e Th17", 25, "lâminas 23–26; transcrição p.62–66", motivacao="m27", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="mediada por uma única citocina, a IL-6",
    fontes=F("lâmina 23", "A transição TREG/TH17 depende de"),
    extra="A single cytokine, IL-6, flips the same TGF-β environment from tolerance to defense.<br>IL-6 comes from macrophages and dendritic cells activated by an invading pathogen." + IMG("th3-th17")),
 K(1487116955601, "A-aula", H_, "Treg: TGF-β e IL-2, inibida por IL-6", 25, "lâminas 23 e 25: TGF-β induz Treg, IL-6 desvia"),
 K(1487116975048, "A-aula", H_, "Th17: IL-6 com TGF-β", 26, "lâmina 26: TGF-β com IL-6 leva a Th17"),
 K(1489970054827, "V-hy", H_, "IL-6 vem de macrófagos", 26, "transcrição p.62: IL-6 é o sinal que troca Treg por Th17"),
 K(1520300013308, "A-aula", H_, "Th17 secreta IL-17, IL-21 e IL-22", 26, "lâmina 26: IL-17, IL-21 e IL-22"),
 K(1520300296240, "A-step", H_, "Th17 recruta neutrófilos", 26, "transcrição p.68: citocinas que recrutam polimorfonucleares"),
 au("k-balanco-treg", ORG("Effector response the gut MALT induces when <b>invaded</b>:<br><br>- <b>intracellular</b> microbes: {{c1::Th1}}<br>- <b>helminths</b>: {{c1::Th2}}"),
    "A-aula", H_, "Na invasão: Th1 ou Th2 contra helmintos", 27, "lâmina 27; transcrição p.70", motivacao="m29", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="balanceadas pelo ambiente rico em TREGs",
    fontes=F("lâmina 27", "balanceadas pelo ambiente rico em TREGs"),
    sem_imagem="lâmina 27 é texto",
    extra="In the healthy gut, Th1, Th2, Th17 and CD8 effectors cause no inflammation because Tregs balance them.<br>Invasion shifts the balance toward the effector type the microbe calls for."),
 K(1479267424779, "V-hy", H_, "Eosinófilos contra helmintos", 27, "transcrição p.26 e 30: eosinófilos aumentam na infecção por helmintos"),
 au("k-higiene", "The idea that <b>little microbial exposure</b> early in life leaves immune regulation untrained and raises <b>allergies</b> is the {{c1::hygiene hypothesis}}",
    "R-detalhe", H_, "Hipótese da higiene", 27, "transcrição p.72–74", motivacao="m30",
    fontes=F("transcrição p.72", "o organismo. Isso foi formulado na hipótese da higiene, que sugere"),
    sem_imagem="fala do professor sem lâmina",
    extra="Constant contact with gut microbes trains Tregs and IL-10, which restrain Th2 and IgE responses.<br>Cleaner environments and food weaken this training, and asthma and allergies become more common."),
 K(1487116873670, "V-hy", H_, "Th2 contra helmintos", 27, "lâmina 27: Th2 nas infecções por helmintos"),
 # ---------- Lâminas 28–29: olho imunoprivilegiado ----------
 au("k-olho", ORG("Anterior chamber of the eye, an immune-privileged site:<br><br>- <b>cornea</b>: no {{c1::blood vessels}}<br>- <b>aqueous humor</b>: {{c1::TGF-β}}<br>- <b>epithelium</b>: {{c1::Fas ligand}} and PD-L1"),
    "A-aula", I_, "Olho imunoprivilegiado", 29, "lâmina 29; transcrição p.78", motivacao="m31", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Além disso, o líquido ocular contém TGF-beta e",
    fontes=F("lâmina 29", "constitutivamente FasL e PD-L1"),
    sem_imagem="lâmina 29 é texto; não há figura real do olho na aula",
    extra="Inflammation would cloud the anterior chamber and cost vision, so few cells reach it.<br>Fas ligand makes arriving lymphocytes die by apoptosis, and PD-L1 switches T cells off."),
 K(1487117300306, "V-hy", I_, "FasL induz apoptose", 29, "lâmina 29: epitélio expressa FasL"),
]

from nebli.hx_cortes import recortar
from hx_cortes import CORTES
CARDS = recortar(CARDS, CORTES)
for _c in CARDS:
    if _c.get('recorte_de'):
        _c['extra'] = _c.pop('extra_add', '') or ''

finalizar(CARDS, HERE, BUSCA)
for _c in CARDS:
    if _c.get('recorte_de'):
        _c['flags'] = {1: 5 if _c['key'].endswith('-tipos') else 4}

VERSO = {
 "ak1486608789738": "Peyer patches are the inductive sites of the gut, where antigen sampled by M cells meets naive lymphocytes.",
 "ak1487117227757": "IgA protects without inflammation, which suits a surface in constant contact with food and microbes.",
 "ak1487117209824": "Most of it goes to the mucosae, where plasma cells of the lamina propria make it every day.",
 "ak1487117240890": "Its Fc does not trigger complement or inflammation, so it protects the mucosa without damage.",
 "ak1487117238120": "Plasma cells of each mucosa make dimeric IgA that is carried into the secretion.",
 "ak1487117234083": "Milk IgA protects the newborn gut before the infant makes its own.",
 "ak1487117156031": "TGF-β is abundant in the gut, which is why mucosal B cells switch mostly to IgA.",
 "ak1487117216624": "Mucosal plasma cells make dimers, while bone marrow plasma cells release monomers into the blood.",
 "ak1487117219869": "Only the dimer binds the polymeric Ig receptor, so only it reaches the lumen.",
 "ak1487117251418": "The receptor sits on the basolateral side of the epithelium and carries IgA to the lumen.",
 "ak1487117223955": "IgA crosses inside a vesicle from the basolateral to the apical side.",
 "ak1487117255825": "Proteases from the host and from bacteria would otherwise digest the antibody in the lumen.",
 "ak1486831448616": "M cells transfer antigen to dendritic cells in the follicle below, so the response starts without breaking the barrier.",
 "ak1486608768857": "",
 "ak1487116955601": "IL-6, made during infection, is what tips the same TGF-β toward Th17.",
 "ak1487116975048": "Without IL-6, the same TGF-β would induce regulatory T cells instead.",
 "ak1520300013308": "These cytokines recruit neutrophils and strengthen the epithelial barrier.",
 "ak1520300296240": "IL-17 drives neutrophil recruitment, which is why neutrophils appear quickly when the gut is invaded.",
 "ak1487116873670": "In the gut this is the response induced against helminths, with eosinophils and IgE.",
 "ak1486831445995": "",
 "ak1486945164044": "",
 "ak1486831451445": "Their B cells switched to IgA in the Peyer patch germinal centers and homed back to the lamina propria.",
}
for c in CARDS:
    v = VERSO.get(c["key"]) or VERSO.get(c["key"].replace("sh-", "ak"))
    if v and c["kind"] != "autoral":
        c["extra_add"] = v + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "k-nodulo-colon": "ganho: contrasta íleo × cólon pela quantidade de tecido linfoide; os AnKing de Peyer não falam do cólon",
 "k-ac-retinoico": "ganho: o ácido retinoico como condicionador da dendrítica (lâmina 16); sh-1791625433083 cobra a indução de Treg",
 "k-reguladoras": "ganho: organiza os três tipos de célula reguladora da mucosa; os AnKing de Treg cobram as citocinas da Treg geral",
 "k-treg-th17": "ganho: contrasta Th3 × Th17 pela IL-6, como as lâminas 25–26; os AnKing cobram cada indução solta",
 "k-balanco-treg": "ganho: as Treg mantêm os efetores da lâmina própria sem inflamação (lâmina 27); os outros cards de Treg não falam da mucosa",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "im67-tonsila.png": "lâmina 3: corte de tonsila com epitélio estratificado em cima e folículos linfoides abaixo",
 "im67-peyer-ileo.png": "lâmina 4: corte transversal do íleo com as placas de Peyer escuras de um lado",
 "im67-peyer-centro.png": "lâmina 6: placa de Peyer em aumento maior, centro claro de proliferação e vilosidades",
 "im67-iel.png": "lâmina 7: vilosidade com linfócitos entre as células epiteliais e lâmina própria cheia de células (setas)",
 "im67-nodulo-colon.png": "lâmina 8: nódulo linfoide solitário na mucosa do intestino grosso (seta)",
 "im67-galt-esquema.png": "lâmina 12: esquema do GALT com célula caliciforme, Paneth, célula M, placa de Peyer e linfonodo mesentérico",
 "im67-vias-inducao.png": "lâmina 13: o mesmo esquema com as duas vias de indução destacadas (placa de Peyer e dendrítica até o linfonodo mesentérico)",
 "im67-prr.png": "lâmina 19 (Abbas fig. 13-2) sem a legenda: NLR no citosol, TLR basolateral e na dendrítica, nenhum no lado luminal",
 "im67-iga-plasmocitos.png": "lâmina 21 (Abbas fig. 13-6) sem a legenda: imunofluorescência do cólon com plasmócitos de IgA verdes e de IgG vermelhos",
 "im67-th3-th17.png": "lâminas 25 e 26 lado a lado: CD4 com TGF-β sem IL-12 vira Th3; com TGF-β e IL-6 vira Th17",
}
EXTRA_VIVO = {1790980914855: "peyer-ileo", 1791625425757: "peyer-centro", 1790980915277: "iga-plasmocitos"}  # figuras das lâminas 4, 6 e 21 no verso das cópias NEBLI
REVISAO = {}
ESCOPO = {"objetivo": "Entender a regulação imune tecido-específica da mucosa intestinal: GALT e inflamação fisiológica, indução por célula M e dendrítica com retorno dos linfócitos, os quatro mecanismos de tolerância (dendrítica tolerogênica, PRR basolateral, IgA secretora, células reguladoras), a IL-6 trocando Treg por Th17, e o olho imunoprivilegiado.",
          "centrais": [["Inflamação fisiológica", "k-infl-fisiologica"], ["Retorno à mucosa", "k-homing"], ["Três tarefas", "k-tres-tarefas"],
                       ["Ácido retinoico", "k-ac-retinoico"], ["PRR basolateral", "k-prr-basolateral"], ["Células reguladoras", "k-reguladoras"],
                       ["IL-6: Treg × Th17", "k-treg-th17"], ["IgA neutraliza", "k-iga-neutraliza"], ["Dendrítica ao linfonodo mesentérico", "k-dc-mesenterico"]],
          "exemplos": [], "outras_aulas": []}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
