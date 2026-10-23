# Especificação curada — 61 Patologia da infecção viral (UC03 P3, Patologia; Prof. Luiz Fernando Ferraz da Silva; 29 lâminas). Pipeline v7
# (23/10): o deck nasce de compreensao-aula.json (aprender por bloco) e segue as lâminas. O deck antigo (14/10) não existe mais no Anki.
# História: o vírus lesa a célula diretamente (lise → inflamação aguda; transformação → neoplasia; o resto é o efeito citopático que o
# patologista vê: inclusões, sincícios, coilócitos) e lesa pelo que provoca na resposta (inata no agudo, com IFN-I e NK; adaptativa no
# crônico, porque o vírus está dentro da célula). Na hepatite B crônica tudo se junta: vidro fosco, antígenos no tecido e no sangue,
# inflamação periportal, apoptose e necrose, interface, perda da reticulina e cirrose.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 7
SECOES_MOTIVO = ("Aula de princípio geral (morfologia da infecção viral): nenhuma seção de recurso do AnKing é do seu assunto; as de NK, "
                 "interferon, HBV, zonas do fígado e cirrose foram lidas e delas entra só o card que responde a um item aprender")
SECOES_DA_AULA = []
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt61-20261023a"
SHORT = "pt61"
LESSON = "2026-uc03-patologia-61-patologia-infeccao-viral"
DECK = "NEBLI::UC03::P3::Patologia::Patologia da infecção viral"
CRITERIOS = "MEMORY.md + pipeline v7 (EXECUCAO-DECK-AULA) + FEEDBACKS até F-20261023-CLAUDE-03 + GUIA_CARDS.md de 23/10"
_IMGS = ("raiva", "sarampo", "sincicio", "coilocito", "curva", "vidro-fosco", "ihq-hbsag", "ihq-hbcag", "infiltrado", "zonas", "necrose",
         "apoptose", "interface", "linf-b", "septos", "masson")
MEDIA = {f"pt61-{n}.png": f"img/pt61-{n}.png" for n in _IMGS}
IMG = lambda n, w=420: f'<img src="pt61-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (23/10): seções de recurso do AnKing (NK, interferons, HBV, zonas do fígado, cirrose; busca/secoes); palavra-chave em "
         "AnKing e Referências Externas (busca/anking.txt); significado em AnKing, nos acervos externos e no NEBLI vivo, uma consulta por item "
         "do mapa (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


EXCLUIDOS = [
 (1502152318872, "Cowdry/herpes: efeito citopático de outra versão da aula (monitoria), fora das lâminas de 2026"),
 (1503861947945, "CMV olho de coruja: outra versão da aula, fora das lâminas"),
 (1506299172244, "Warthin-Finkeldey: célula gigante do sarampo em linfonodo; a lâmina 6 mostra inclusão nuclear em neurônio"),
 (1516474771301, "locais das inclusões de Negri (hipocampo, Purkinje): detalhe de raiva, fora do ponto da lâmina 5"),
 (1516475620459, "repete 1516474665512 (Negri citoplasmático eosinofílico)"),
 (1463094113348, "repete 1385335604751 (coilócito)"),
 (1506459892639, "repete 1506457588894 (proteína F → células gigantes)"),
 (1461794607480, "IFN-α no tratamento das hepatites: farmacologia, fora (a lâmina 25 só cita que já foi o tratamento)"),
 (1489970516941, "IFN-γ e MHC II: o contraste fica no verso de ak1520301453074"),
 (1506628692802, "corpúsculos de Councilman em HAV e febre amarela: detalhe clínico; a lâmina 24 entra pelo card de apoptose"),
 (1584230461040, "caso de sorologia (hepatite crônica ativa): clínica"),
 (1495743863878, "interpretação de painel sorológico: clínica"),
 (1486522654540, "células de Ito e TGF-β: aula de reparo (65)"),
]
FORA_DO_RECORTE = [
 "Efeitos citopáticos vírus a vírus da monitoria e da apostila (herpes, CMV, Cowdry A/B, EBV, adenovírus, zika, influenza): outra versão da aula; as lâminas de 2026 mostram raiva, sarampo, VSR e HPV.",
 "Clínica, sorologia completa e tratamento das hepatites: aula de clínica e UC08; aqui só os antígenos e anticorpos que a fala usa para ler a lesão.",
 "Imunologia antiviral em detalhe (sensores, ISGs, CTL): 63 Resposta imune aos vírus; aqui como causa e forma da lesão.",
 "Fibrose como processo geral (células estreladas, TGF-β): 65 Reparo tecidual.",
]
A_, B_, C_, D_, E_ = "A-efeitos", "B-citopatico", "C-resposta", "D-hepatite-virus", "E-hepatite-resposta"

CARDS = [
 # ---------- Dois efeitos (lâmina 2) ----------
 au("au-dois-efeitos", "Viral injury comes from the virus and from host {{c1::immune response}}, which causes most liver damage in <b>hepatitis B</b>",
    "V-pilar", A_, "Lesão viral = efeito do vírus + efeito da resposta", 2, "lâmina 2; transcrição; Robbins cap. 8 (lesão do HBV/HCV pela resposta, não pelo efeito citopático)",
    sem_imagem="princípio da aula (lâmina 2 só tem texto)", extra="How the virus replicates (nucleus or cytoplasm) decides what the lesion looks like.<br>The response is what weighs most in chronic infections."),
 # ---------- Efeitos diretos (lâminas 3–4) ----------
 au("au-efeitos", ORG("<b>Viral effects on the cell</b>:<br>- lysis: {{c1::acute inflammation}}<br>- transformation: {{c1::neoplasia}}<br>- blocked synthesis, syncytia, cytoskeleton, arrested cycle: {{c1::cytopathic}} effect"),
    "V-pilar", A_, "Lise → inflamação aguda; transformação → neoplasia; o resto → efeito citopático", 4, "lâminas 3–4; transcrição",
    sem_imagem="lista das lâminas 3–4, sem figura", extra="Lysis releases DAMPs, which set off acute inflammation.<br>Viral DNA next to a cell-cycle gene can drive uncontrolled proliferation."),
 au("au-sequestro", "Because the virus takes over the <b>synthesis machinery</b> for its own proteins, an infected cell usually {{c1::stops dividing}}",
    "A-aula", A_, "Síntese sequestrada para. o ciclo", 4, "lâmina 4; transcrição ('não está a fim de replicar o material genético dela')",
    sem_imagem="mecanismo, lâmina sem figura", extra="Synthesis is not switched off: it is redirected to viral proteins.<br>Unprocessed proteins can pile up in the cell."),
 # ---------- Efeito citopático (lâminas 5–8) ----------
 au("au-inclusao", "Viral <b>inclusions</b> form when assembly stops at the {{c1::scarcest}} component and the excess components pile up",
    "V-prova", B_, "Inclusão = acúmulo desproporcional", 5, "lâmina 5; transcrição (linha de produção desregulada); prova 2024 P3 1.2",
    sem_imagem="princípio; as figuras de inclusão estão em au-raiva-sarampo", extra="Viral parts are made out of proportion, like an unbalanced production line.<br>Lots of protein without genome cannot become virions.<br>The excess stays where it is made, in the cytoplasm or in the nucleus."),
 sh(1792695054492, "azul", B_, "Inclusão no local da montagem", 5, "A-aula: card da 58; a lâmina 5 é a mesma ideia vista ao microscópio"),
 au("au-raiva-sarampo", "<b>Rabies</b> inclusions are {{c1::cytoplasmic::nuclear/cytoplasmic}}, whereas measles inclusions in neurons are {{c1::nuclear::nuclear/cytoplasmic}}",
    "A-aula", B_, "Inclusão citoplasmática (raiva) × nuclear (sarampo)", 6, "lâminas 5–6; transcrição",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="Both are eosinophilic accumulations of viral components.<br>" + IMG("raiva", 300) + IMG("sarampo", 300)),
 K(1516474665512, "A-aula", B_, "Negri: replicação em inclusões citoplasmáticas", 5, "lâmina 5 (inclusão citoplasmática eosinofílica da raiva)"),
 K(1506457588894, "A-aula", B_, "VSR: proteína F → células gigantes", 7, "lâmina 7 (sincícios no pulmão pelo vírus sincicial respiratório)",
   slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra_add="- Infected type II pneumocytes and macrophages fuse; adenovirus and H1N1 can do the same<br>" + IMG("sincicio", 260)),
 au("au-sincicio-granuloma", ORG("<b>Viral syncytium × granuloma giant cell</b>: the syncytium has no<br>- rim of {{c1::lymphocytes::l…}}<br>- {{c1::epithelioid::e…}} macrophages<br>- central {{c1::necrosis::n…}}"),
    "V-pilar", B_, "Sincício × célula gigante de granuloma", 7, "lâmina 7; transcrição ('isso não tem a ver com a formação de um granuloma'); prova 2017 P3 1.3",
    sem_imagem="a figura do sincício está no card da proteína F (lâmina 7)", extra="The syncytium is infected cells fused together, sitting directly in the alveolar septa.<br>A granuloma giant cell is fused macrophages inside an organized granuloma."),
 K(1385335604751, "V-prova", B_, "Coilócito: halo perinuclear do HPV", 8, "lâmina 8; transcrição; prova 2016 P3 1.2",
   slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra_add="- On a Pap smear it signals HPV; since some types are oncogenic (16, 18), the patient is followed more closely<br>" + IMG("coilocito", 260)),
 # ---------- Resposta (lâminas 9–13) ----------
 sh(1792753615215, "azul", C_, "Agudo: inata; crônico: adaptativa", 9, "A-aula: card da 59; a lâmina 9 é este quadro"),
 au("au-intracelular", "<b>Innate immunity</b> rarely clears viruses alone because they hide {{c1::inside cells}}, so T cells and antibodies are needed",
    "V-pilar", C_, "A inata não basta: vírus intracelular", 10, "lâmina 10; transcrição ('a imunidade inata gosta de enxergar coisas fora da célula')",
    sem_imagem="princípio; a curva está em au-curva", extra="T cells kill infected cells; antibodies neutralize virus released when they burst.<br>Unlike most bacteria, which neutrophils and macrophages can handle."),
 au("au-complemento", "Besides neutralizing enveloped viruses, <b>complement</b> can kill infected cells showing viral proteins through the {{c1::membrane attack complex}}",
    "A-aula", C_, "Complemento: neutraliza e lisa a célula infectada", 9, "lâmina 9; transcrição",
    sem_imagem="mecanismo sem figura na aula", extra="It helps, but the main killer of infected cells is the cytotoxic T cell."),
 au("au-curva", "<b>IFN-I</b> and NK cells peak early in a viral infection, while {{c1::T cells}} and then {{c2::antibodies}} dominate later",
    "A-aula", C_, "Curva da resposta antiviral", 10, "lâmina 10 (curva: vírus, IFN-I, NK, linfócitos T, anticorpos)",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="The innate wave holds the exponential rise; the adaptive one clears the virus and leaves memory.<br>" + IMG("curva", 380)),
 K(1489970693302, "V-pilar", C_, "IFN-I age nas células vizinhas", 11, "lâmina 11; transcrição (efeito parácrino; proteína antiviral)", sem_imagem="mecanismo imunológico sem morfologia; a curva da resposta está em au-curva"),
 K(1520301328706, "A-aula", C_, "IFN-I reduz a síntese proteica: estado antiviral", 12, "lâmina 12 (estado de resistência antiviral: inibição da síntese proteica)", sem_imagem="mecanismo molecular, sem figura útil"),
 au("au-ifn-tempo", "Type I <b>interferon</b> slows replication in neighboring cells without blocking entry, buying {{c1::time}} for adaptive immunity",
    "A-aula", C_, "IFN-I ganha tempo", 11, "lâmina 11; transcrição ('ele ganha tempo')",
    sem_imagem="lâminas 11–12 são esquemas de livro; o card cobra o para quê", extra="Meanwhile antigen is processed and presented to lymphocytes.<br>This is IFN-α/β from infected cells, not the IFN-γ of the granuloma."),
 K(1520301453074, "V-pilar", C_, "IFN-I sobe MHC I", 12, "lâmina 12 (aumento da expressão do MHC I)",
   extra_add="- IFN-γ, by contrast, raises MHC II", sem_imagem="mecanismo molecular, sem figura útil"),
 K(1487117310594, "A-aula", C_, "IFN-α/β ativam NK", 12, "lâmina 12 (ativação de NK e macrófagos)", sem_imagem="mecanismo imunológico, sem figura útil"),
 K(1487117314403, "V-pilar", C_, "NK mata a célula sem MHC I", 13, "lâmina 13; transcrição",
   extra_add="- A virus that hides MHC I escapes CTLs but becomes an NK target"),
 K(1487117308213, "A-aula", C_, "NK: perforina e granzima", 13, "lâmina 13 (perforina e granzima)", sem_imagem="mecanismo imunológico, sem figura útil"),
 K(1518053116398, "R-detalhe", C_, "NK e tumor sem MHC I", 13, "transcrição (vigilância antitumoral da NK)"),
 # ---------- Hepatite: o vírus (lâminas 14–18) ----------
 au("au-hbv-antigenos", ORG("<b>Hepatitis B antigens</b>:<br>- envelope: surface antigen ({{c1::HBsAg}})<br>- core: core antigen ({{c1::HBcAg}})<br>- rises during replication: {{c1::HBeAg}}"),
    "V-pilar", D_, "HBsAg, HBcAg, HBeAg", 14, "lâmina 14; transcrição",
    sem_imagem="o esquema do vírus (lâmina 14) é de banco de imagens comercial com marca d'água", extra="These proteins are what immunohistochemistry stains in the liver and what antibodies are made against."),
 au("au-hav", "<b>Hepatitis A</b> kills hepatocytes acutely but spares the {{c1::reticulin}} framework, so the liver regenerates fully",
    "A-aula", D_, "HAV aguda preserva a reticulina e regenera", 14, "lâmina 14; transcrição",
    sem_imagem="a aula não mostra figura da hepatite A", extra="Chronic hepatitis B and C, driven by adaptive immunity, eventually destroy that framework."),
 K(1715273523479, "V-pilar", D_, "Vidro fosco: HBsAg no hepatócito", 16, "lâmina 16 (efeito citopático do hepatócito)",
   slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra_add=IMG("vidro-fosco", 300)),
 au("au-vidro-fosco", "<b>Ground-glass</b> hepatocytes have a homogeneous cytoplasm packed with {{c1::HBsAg}}, which takes over their synthetic machinery",
    "A-aula", D_, "Vidro fosco = HBsAg acumulado", 16, "lâminas 16–17; transcrição; Robbins cap. 18 (esferas e túbulos de HBsAg)",
    sem_imagem="a figura do vidro fosco está no card AnKing ao lado", extra="So the hepatocyte makes less albumin and clotting factors and conjugates bilirubin less well."),
 au("au-ihq", "On immunohistochemistry, <b>HBsAg</b> stains the hepatocyte {{c1::cytoplasm::nucleus/cytoplasm}}, whereas HBcAg stains the {{c1::nucleus::nucleus/cytoplasm}}",
    "A-aula", D_, "IHQ: HBsAg no citoplasma, HBcAg no núcleo", 18, "lâminas 17–18; transcrição",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="The core antigen goes to the nucleus, where the viral genome is and new cores start.<br>" + IMG("ihq-hbsag", 260) + IMG("ihq-hbcag", 260)),
 au("au-hcv-esteatose", "<b>Hepatitis C</b> causes steatosis by occupying the hepatocyte's lipid {{c1::conjugation}} machinery, unlike alcohol, which causes fat overload",
    "R-detalhe", D_, "HCV → esteatose", 18, "lâmina 18 (fala); Robbins cap. 18 (esteatose no HCV)",
    sem_imagem="a aula não mostra figura de esteatose do HCV", extra="Fat that cannot be packaged and exported stays in the hepatocyte."),
 K(1502066053913, "A-aula", D_, "Vacina do HBV: HBsAg recombinante", 18, "transcrição (vacina com fragmento: só o HBsAg)"),
 K(1521044225681, "V-prova", D_, "Só anti-HBs = vacina", 18, "transcrição (anti-HBs pode ser vacina ou infecção)"),
 au("au-anti-hbc", "<b>Anti-HBc</b> proves contact with the virus, because the hepatitis B vaccine contains only {{c1::HBsAg}}",
    "A-aula", D_, "Anti-HBc = contato com o vírus", 18, "lâmina 18 (fala: 'faz sentido ter uma vacina que usa a proteína do core? Não')",
    sem_imagem="sorologia, sem figura", extra="Anti-HBs alone cannot tell vaccine from infection."),
 K(1521044306629, "A-aula", D_, "HBeAg: replicação e infectividade", 18, "transcrição (HBeAg é marcador de replicação viral)",
   extra_add="- Low when the virus is quiet, high when it is transcribing and making new virions"),
 # ---------- Hepatite: a resposta (lâminas 19–29) ----------
 K(1486522630094, "A-aula", E_, "Inflamação crônica expande o espaço porta", 19, "lâmina 19 (espaço porta expandido por linfócitos)",
   slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra_add=IMG("infiltrado", 300)),
 K(1486776378880, "A-aula", E_, "Lesão viral do fígado começa na zona I", 20, "lâmina 20; transcrição (inflamação periportal)"),
 au("au-periportal", "<b>Viral hepatitis</b> begins periportally because both the virus and the {{c1::inflammatory cells}} arrive through the portal tract blood",
    "A-aula", E_, "Por que periportal", 20, "lâmina 20; transcrição",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="Metabolic and ischemic injury instead favor zone 3, the one with least oxygen.<br>" + IMG("zonas", 260)),
 K(1487117293576, "V-pilar", E_, "CTL mata célula infectada por apoptose", 21, "lâminas 21–24, 27; transcrição (citotoxicidade, apoptose)"),
 K(1521424037362, "A-aula", E_, "Necrose e apoptose de hepatócitos com infiltrado mononuclear", 21, "lâminas 21–24",
   slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra_add=IMG("apoptose", 220)),
 au("au-apoptose-necrose", "When lymphocytes kill hepatocytes, <b>apoptosis</b> spares the surrounding tissue, whereas {{c1::necrosis}} spills cell contents into it",
    "A-aula", E_, "Apoptose (dirigida) × necrose (suja)", 22, "lâminas 21–24; transcrição",
    sem_imagem="as figuras de apoptose e necrose estão nos cards vizinhos", extra="Lymphocyte killing is targeted, so apoptosis causes little collateral damage."),
 au("au-necrose-matriz", "Hepatocyte <b>necrosis</b> recruits {{c1::neutrophils}}, whose proteases destroy the reticulin framework, so regenerating hepatocytes cannot form trabeculae",
    "V-pilar", E_, "Necrose → neutrófilo → matriz destruída → sem regeneração ordenada", 22, "lâmina 22; transcrição",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="Elastase and collagenase digest the matrix along with the cells.<br>" + IMG("necrose", 260)),
 au("au-interface", "Portal inflammation breaking through the {{c1::limiting plate}} is <b>interface hepatitis</b>, a biopsy sign that the disease is active",
    "V-pilar", E_, "Atividade de interface = doença ativa", 25, "lâmina 25; transcrição ('isso é critério de atividade')",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="Also called piecemeal necrosis; on biopsy it means treatment is needed.<br>" + IMG("interface", 260)),
 au("au-linf-b", "In chronic hepatitis B, portal <b>B cells</b> make {{c1::antibodies}} that neutralize virus released from killed hepatocytes",
    "A-aula", E_, "Linfócitos B no infiltrado", 26, "lâmina 26; transcrição",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="CD8 T cells in the same infiltrate kill infected hepatocytes.<br>" + IMG("linf-b", 220)),
 K(1468250259504, "A-aula", E_, "Reticulina é colágeno III", 28, "lâmina 28; transcrição (reticulina, 'um colágeno muito fininho')",
   extra_add="- In cirrhosis this fine framework is replaced by thick collagen", sem_imagem="conceito; a reticulina em prata está no card compartilhado vizinho (lâmina 28)"),
 au("au-colageno", "When hepatocyte loss outpaces regeneration, the collapsed <b>reticulin</b> is replaced by thick {{c1::collagen}} that forms septa",
    "A-aula", E_, "Reticulina → colágeno → septos", 28, "lâmina 28; transcrição",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="The septa join and isolate regenerative nodules: cirrhosis.<br>" + IMG("septos", 260)),
 sh(1791022173275, "azul", E_, "Prata: reticulina contorna os nódulos", 28, "A-aula: card da correlação pato-radio 2; a lâmina 28 é a reticulina em prata com septos"),
 K(1486522637384, "V-pilar", E_, "Cirrose: fibrose e nódulos regenerativos", 29, "lâmina 29"),
 au("au-masson", "On <b>Masson trichrome</b>, liver fibrosis stains {{c1::blue}} while hepatocytes stain red",
    "R-detalhe", E_, "Masson: fibrose azul", 29, "lâmina 29; transcrição",
    slide_sem_alternativa="a figura é a lâmina que o professor comenta (microscopia da aula); não há equivalente no AnKing", extra="Blue septa of collagen surround red nodules of regenerating hepatocytes: established cirrhosis.<br>" + IMG("masson", 300)),
]

# F-20261022-CLAUDE-04: a resposta do cloze autoral vai em negrito, como no AnKing
for c in CARDS:
    if c["kind"] == "autoral":
        c["text"] = _re.sub(r"\{\{c(\d+)::(.*?)((?:::[^}]*)?)\}\}", lambda m: "{{c%s::<b>%s</b>%s}}" % (m.group(1), m.group(2), m.group(3)), c["text"])

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1516474665512": "The inclusion is where the virus is being made: eosinophilic, in the neuron cytoplasm.",
 "ak1520301328706": "Neighbouring cells enter an antiviral state: they can still be infected but make few new virions.",
 "ak1487117310594": "Activated NK cells and macrophages patrol for infected cells.",
 "ak1487117308213": "The same weapons CTLs use.",
 "ak1518053116398": "Same rule as for virus-infected cells: no MHC I, no inhibitory signal.",
 "ak1502066053913": "So a vaccinated person makes anti-HBs but never anti-HBc.",
 "ak1521044225681": "The vaccine has no core protein.",
 "ak1486776378880": "The virus and the lymphocytes come in with portal blood.",
 "ak1487117293576": "In hepatitis B this is what kills most hepatocytes.",
 "ak1486522637384": "After repeated necrosis destroys the reticulin framework.",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "au-vidro-fosco": "ganho: o AnKing nomeia o vidro fosco; aqui o porquê (HBsAg acumulado) e a consequência para a função do hepatócito",
 "au-anti-hbc": "ganho: o AnKing dá 'só anti-HBs = vacina' e 'vacina de HBsAg'; aqui a dedução que a fala ensina (anti-HBc prova contato)",
 "au-ifn-tempo": "ganho: o AnKing dá onde o IFN-I age; aqui para que serve (ganhar tempo para a adaptativa)",
 "au-hbv-antigenos": "ganho: organizador das três proteínas do vírus; a resposta HBsAg repete-se em outros cards porque é a mesma proteína vista no tecido e na vacina",
 "au-periportal": "ganho: o AnKing dá a zona I; aqui o porquê (vírus e células chegam pelo sangue portal)",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "pt61-raiva.png": "lâmina 5: neurônio com inclusão citoplasmática eosinofílica (raiva), seta",
 "pt61-sarampo.png": "lâmina 6: neurônio com inclusão nuclear (sarampo)",
 "pt61-sincicio.png": "lâmina 7: pulmão com sincícios do vírus sincicial respiratório nos septos",
 "pt61-coilocito.png": "lâmina 8: Papanicolau com coilócitos (halo claro perinuclear)",
 "pt61-curva.png": "lâmina 10: curva de vírus, IFN-I, NK, linfócitos T e anticorpos por dia",
 "pt61-vidro-fosco.png": "lâmina 16: hepatócitos em vidro fosco (seta)",
 "pt61-ihq-hbsag.png": "lâmina 17: imuno-histoquímica de HBsAg no citoplasma",
 "pt61-ihq-hbcag.png": "lâmina 18: imuno-histoquímica de HBcAg nos núcleos",
 "pt61-infiltrado.png": "lâmina 19: espaço porta expandido por infiltrado linfocitário",
 "pt61-zonas.png": "lâmina 20: fígado normal com zonas 1, 2 e 3",
 "pt61-necrose.png": "lâmina 22: necrose de hepatócitos com infiltrado perto do espaço porta",
 "pt61-apoptose.png": "lâmina 24: hepatócito apoptótico eosinofílico",
 "pt61-interface.png": "lâmina 25: inflamação portal invadindo o lóbulo (interface)",
 "pt61-linf-b.png": "lâmina 26: imuno-histoquímica de linfócitos B no infiltrado portal",
 "pt61-septos.png": "lâmina 28: reticulina com septos isolando nódulos",
 "pt61-masson.png": "lâmina 29: tricrômico de Masson, fibrose azul e nódulos vermelhos (cirrose)",
}
REVISAO = {}
ESCOPO = {"objetivo": "Entender como a infecção viral aparece no tecido: efeito direto do vírus (e o efeito citopático que se reconhece) e efeito da resposta, integrados na hepatite B crônica até a cirrose.",
          "centrais": [
           ["dois efeitos", "au-dois-efeitos"],
           ["efeitos diretos e efeito citopático", "au-efeitos", "au-inclusao", "au-sincicio-granuloma"],
           ["resposta inata × adaptativa; vírus intracelular", "au-intracelular", "ak1489970693302", "ak1487117314403"],
           ["IFN-I e MHC I", "ak1520301453074"],
           ["antígenos do HBV e vidro fosco", "au-hbv-antigenos", "ak1715273523479"],
           ["necrose destrói a matriz", "au-necrose-matriz"],
           ["interface = atividade", "au-interface"],
           ["cirrose", "sh-1791022172624"],
           ["sorologia: anti-HBs × anti-HBc", "ak1521044225681"],
           ["coilócito e HPV", "ak1385335604751"]],
          "exemplos": ["au-hcv-esteatose", "au-masson", "ak1518053116398"],
          "outras_aulas": ["59 Patogênese da infecção viral", "47 Inflamação granulomatosa", "62 Inflamação crônica", "63 Resposta imune aos vírus", "65 Reparo tecidual"]}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
