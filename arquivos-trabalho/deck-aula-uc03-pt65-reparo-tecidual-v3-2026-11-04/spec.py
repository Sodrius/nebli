# Especificação curada — 65 Reparo tecidual e cicatrização de feridas (UC03 P3, Patologia; Luiz Fernando Ferraz da Silva; 45 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral SÓ para lacuna provada em busca/cobertura.tsv (gate duro), último do último caso.
# Modelo vivo: arquivos-trabalho/deck-aula-uc03-im64-hipersensibilidade-v3-2026-11-04/spec.py (04/11, exemplar de deck).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 15
from nebli.spec_lib import acervo
SECOES_MOTIVO = ""
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ("O AnKing traz a cicatrização como fatos soltos do Pathoma e do First Aid (fases, tipos de colágeno, intenções, cicatrizes), mas não os fios que o professor ensina: "
                   "o arcabouço que decide entre regenerar e cicatrizar, os quatro destinos da lesão, o crescimento compensatório do fígado, os nichos de células-tronco, as fases com seus tempos, "
                   "o ponto cirúrgico que só aproxima, M1 × M2 na ferida, a angiogênese com vasos imaturos, a reepitelização, a segunda intenção, a imunossupressão que bloqueia a fase inflamatória, "
                   "os papéis do macrófago e a fibrose pelo mesmo mecanismo. Cobertura da aula vem antes do teto (F-20261029-CLAUDE-02); todo autoral está num item do mapa e numa motivação.")
MODO = "aula"
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt65-20261104a"
SHORT = "pt65"
LESSON = "2026-uc03-patologia-65-reparo-tecidual"
DECK = "NEBLI::UC03::P3::Patologia::Reparo tecidual e cicatrização"
CRITERIOS = "MEMORY.md + pipeline v15 + FEEDBACKS até F-20261104-CLAUDE-03 + GUIA-1 a GUIA-4 relidos em 04/11/2026"
_IMGS = ("destinos", "arcabouco", "crescimento", "nichos", "integrinas", "fases", "intencoes", "m1m2", "angiogenese", "macrofago", "fibrose", "granulacao-histo", "forca")
MEDIA = {f"im65-{n}.png": f"img/im65-{n}.png" for n in _IMGS}
IMG = lambda n: f'<br><br><img src="im65-{n}.png" style="width:100%;max-width:850px;height:auto">'
BUSCA = ("Três caminhos (04/11): seções de recurso do AnKing de cicatrização (FirstAid Wound healing e Scar formation, Pathoma, OME, Physeo, B&B, Bootcamp colágeno e cicatrização; busca/secoes); "
         "palavra-chave com sinônimos em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e no NEBLI vivo, uma consulta por card planejado (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


_FORA = "outra aula ou UC: ver FORA_DO_RECORTE"
EXCLUIDOS = [
 # granuloma e inflamação aguda: outras aulas
 (1487642936903, "granuloma: aula 47 Inflamação granulomatosa"), (1487643760880, "granuloma: aula 47"), (1487643766184, "granuloma: aula 47"), (1487643775029, "granuloma: aula 47"),
 (1487643778956, "granuloma: aula 47"), (1487643789145, "granuloma: aula 47"), (1487643792482, "granuloma: aula 47"), (1487643795892, "granuloma: aula 47"), (1520715899772, "talcose e granuloma: aula 47"),
 (1487727429546, "PECAM-1 na extravasão: aula 38 Inflamação aguda"),
 # infecções e microbiologia
 (1510260312665, "Vibrio e frutos do mar: Microbiologia"), (1510260413494, "Vibrio vulnificus em feridas: Microbiologia"), (1522347475309, "Vibrio e acloridria: Microbiologia"), (1522201141426, "anaeróbios em tecido necrótico: Microbiologia"),
 # colágeno e vitamina C como bioquímica/nutrição (UC02)
 (1468250287632, "estrutura Gly-X-Y do colágeno: Bioquímica (UC02)"), (1468250319201, "repete 1476583833764 (vitamina C hidroxila prolina e lisina)"),
 (1468250327871, "síntese do colágeno em etapas: Bioquímica (UC02); a lâmina 28 só ilustra"), (1468250335702, "síntese do colágeno em etapas: Bioquímica (UC02)"),
 (1468250383192, "síntese do colágeno em etapas: Bioquímica (UC02)"), (1468250390306, "cobre e lisil oxidase: Bioquímica (UC02)"),
 (1476583840567, "vitamina C em frutas: Nutrição, trivia"), (1476583846055, "quadro clínico do escorbuto: Nutrição; aqui só a ligação com a cicatrização"), (1476583848657, "quadro clínico do escorbuto: Nutrição"),
 (1476583854343, "repete 1487981589146 (vitamina C e cicatrização retardada)"), (1487981591003, "repete 1476584079267 (zinco e cicatrização retardada)"),
 # farmacologia e tumores
 (1489968326925, "bevacizumabe: farmacologia (UC19) e aulas de tumores"), (1489968613360, "ranibizumabe e bevacizumabe: farmacologia (UC19)"),
 (1487981562504, "PDGF e remodelamento vascular: repete o papel de PDGF já em outros cards"), (1487981570164, "EGF e tirosina quinase: coberto pelo organizador de fatores e pelo Extra"),
 # trivia de cicatriz
 (1487981606867, "hipertrófica e herança: trivia"), (1487981609857, "hipertrófica e recidiva: repete o contraste com o queloide"), (1487981624737, "queloide e predisposição étnica: trivia"),
 (1487981634878, "queloide na orelha: localização, trivia"), (1568496019520, "repete 1487981545623 (colágeno I na cicatriz)"),
 (1468101717082, "mesma resposta de 1468101709109 (tecido estável); os exemplos vão no Extra dele"),
 (1487981602812, "mesma resposta de 1487981599441 (cicatriz hipertrófica); o colágeno paralelo vai no Extra dele"),
 (1487981616609, "mesma resposta de 1487981612881 (queloide); o colágeno desorganizado vai no Extra dele"),
 (1487981620664, "mesma resposta de 1487981545623 (colágeno I e III); a síntese aumentada vai no Extra do queloide"),
 (1468101697168, "repete 1487981520428 (tecido permanente); o verso dele já traz os exemplos"),
 (1474059949481, "grânulos densos (Ca e ADP): hemostasia da aula 69; a serotonina e a histamina da plaqueta vão no Extra do plug primário"),
 (1487981552881, "repete a resposta (zinco) de 1476584079267; a colagenase vai no Extra de 1487981550712"),
 (1482374264661, "estenose macroscópica do Crohn: aula de Patologia do trato digestivo; a fibrose que retrai a parede vai no Extra de c-fibrose-mec"),
 (1487981629888, "recidiva do queloide: sim ou não; já no Extra de 1487981612881"),
 (1487981541929, "repete c-angiogenese e 1487981537242 (capilares nutrem a granulação)"),
 (1487981353937, "definição de regeneração: repete c-org-destinos e c-arcabouco"),
 (1487981526005, "definição de reparo: repete c-org-destinos e c-arcabouco"),
 (1468250215718, "colágeno organiza a matriz: tautológico e repete c-mec-funcoes"),
 (1496163125083, "fatores angiogênicos do tumor: aulas de tumores (74 a 82)"),
 (1487981589146, "repete 1476583833764 (vitamina C na síntese do colágeno e na cicatrização)"),
 (1473982141617, "resposta ambígua (weak, temporary, unstable); o plug primário frágil vai no Extra de 1473985984856"),
 (1487981568284, "VEGF e angiogênese: repete c-angiogenese e a linha de angiogênese de c-macrofago-reparo"),
 (1487981566131, "FGF-2 e angiogênese: a linha de angiogênese de c-macrofago-reparo traz VEGF e FGF-2"),
 (1524169597395, "contratura por MMP e miofibroblasto: detalhe sem HY que repete 1487981543711"),
 (1487981560574, "resposta ambígua (TGF-β e VEGF também vêm de plaquetas e macrófagos); o PDGF entra por sh-1791983683760"),
 (1476584079267, "resposta ambígua (vitamina C, cobre e proteína também atrasam); o zinco vai no Extra do card de vitamina C"),
 (1463884007824, "alvos secundários (colágeno, cicatrização) e uma só ideia lateral; o corticoide que atrasa a cicatrização vai no Tab"),


 (1487981550712, "repete parte do verso de 1487981545623 (remodelamento do colágeno)"),
 (1487981576976, "contraste espelho de 1487981574852; a cicatriz mínima vai no Extra dele"),
 (1487981581148, "contraste espelho de 1487981578907; a cicatriz maior vai no Extra dele"),
 (1487460268378, "tecido permanente só hipertrofia: aula 11 Acúmulos e adaptação"), (1479425811082, "neurônios permanentes: repete os exemplos de tecido permanente"),
 # NEBLI vivo de outras aulas
 (1793301697517, "proteases de neutrófilos destroem o arcabouço na hepatite: detalhe da aula 61; o princípio entra pelos dois cards da 61 e por c-arcabouco"),
 (1791625434457, "M2 por Th2 na inflamação crônica: repete sh-1791983682407 e sh-1791983681904 (aula 62)"),
 (1791910086149, "fatores de macrófago e fibroblasto no granuloma: repete PDGF e TGF-β da 62"),
 (1791780349490, "transcitose por VEGF: detalhe da inflamação aguda (38)"),
 (1791743342606, "monócitos depois dos neutrófilos: repete 1487642786172"),
 (1793301695344, "autoral da aula 61 reprovado pelo revisor independente na versão atual (alvo amplo sem o órgão na frente); o princípio entra por c-arcabouco"),
 (1793301698344, "autoral da aula 61 reprovado pelo revisor independente na versão atual (alvo previsível); a fibrose da perda de arcabouço entra por c-org-destinos"),
 (1791780363131, "autoral da aula 38 (suspenso por Davi) reprovado pelo revisor independente: negrito na lacuna e alvo previsível; o conteúdo entra por ak1487981520428 e c-org-destinos"),
 (1791780353997, "autoral da aula 38 (suspenso por Davi) reprovado pelo revisor independente: negrito na lacuna e alvo ambíguo; entra por ak1474059949481"),
 (1791983681904, "autoral da aula 62 reprovado pelo revisor independente: negrito na lacuna; os indutores vão no Extra de c-m1-m2"),
 (1791983682407, "autoral da aula 62 reprovado pelo revisor independente: vários fatores cabem e repete c-m1-m2; o TGF-β do M2 está em c-m1-m2"),
 (1791780360877, "autoral da aula 38 (suspenso por Davi) reprovado pelo revisor independente: alvo previsível e Extra repete; TNF e IL-1 passam para a frente de c-m1-m2"),
 (1791780363380, "autoral da aula 38 (suspenso por Davi) reprovado pelo revisor independente: alvo genérico e Extra vazio; a fibrose crônica entra por c-fibrose-mec"),
 (1520717070355, "M2 por Th2 na inflamação crônica (cópia suspensa na aula 37): repete sh-1791983682407 e sh-1791983681904 da aula 62"),
 (1792117377748, "necrose liquefativa do cérebro: aula 09; o arcabouço do cérebro vai no Extra de c-arcabouco"), (1792117378246, "necrose liquefativa do cérebro: aula 09"),
 (1792117377497, "necrose liquefativa: aula 09"), (1792117376722, "necrose coagulativa: aula 09"), (1792117361820, "hepatite viral aguda: aula 09"),
 (1791022173275, "reticulina na cirrose: Correlação patológica-radiológica 2"), (1791022173097, "célula estrelada: outra aula"),
 (1792240569417, "metaplasia: aula 11"), (1791780338996, "inflamação aguda e homeostase: aula 38"), (1792240994116, "hallmark do câncer: aula 13"),
 (1791631347767, "iPSC por quatro fatores: aula 52 Biomol"), (1790980911781, "Lgr5: aula UC08"), (1790980916280, "cólon sem Paneth: aula UC08"), (1790980911405, "células da cripta migram: aula UC08"),
 (1791762411098, "receptor tirosina quinase: Bioquímica, ação hormonal"), (1791054018897, "diabetes e infecção: GR2"), (1791054020671, "osteomielite no pé diabético: GR2"), (1791054019022, "gangrena no pé diabético: GR2"),
 (1791054015070, "AGEs: GR2"), (1791054015697, "glicação na membrana basal glomerular: GR2"), (1791054015573, "diabetes e aterosclerose: GR2"),
 (1791743342910, "P-selectina e histamina: aula 37"), (1791023366868, "células enterocromafins: UC08"), (1791780351076, "fontes de histamina: aula 38"),
 (1791780360131, "sequência de edema, neutrófilo e monócito: aula 38"), (1791780359481, "neutrófilos em 6 a 24 horas: aula 38"), (1791743346434, "glicocorticoide e fosfolipase A2: aula 37"),
 (1791729316911, "glicocorticoide e catabolismo proteico: Bioquímica"), (1791780360756, "efeitos sistêmicos de TNF e IL-1: aula 38"),
 (1791780364433, "exsudato fibrinoso: aula 38"), (1791780363632, "fibrina compartimentaliza: aula 38"), (1791780364057, "úlcera: aula 38"), (1791780364806, "flegmão: aula 38"), (1791780363756, "úlcera: aula 38"),
 (1791743340457, "DAMPs na organização do SI: aula 07"), (1792240575392, "vitamina A e metaplasia: aula 11"), (1792240575643, "vitamina A e epitélio: aula 11"),
 (1792240996768, "rugas do envelhecimento: aula 13"), (1791000314427, "vitamina D: UC08"), (1791000312303, "vitamina C e ferro: UC08"),
 (1791746129301, "colagenase bacteriana: Microbiologia"), (1791626776427, "colagenase de dermatófitos: Microbiologia"), (1791746124259, "MSCRAMMs: Microbiologia"), (1791746122043, "invasina e integrinas: Microbiologia"),
 (1791780358556, "integrinas na adesão leucocitária: aula 38"), (1791780359356, "colagenases na transmigração: aula 38"), (1791780355567, "adesão após rolamento: aula 38"), (1791780355920, "transmigração: aula 38"),
 (1791983682682, "proteases do macrófago destroem matriz: aula 62"), (1792081074669, "fibronectina ativa macrófagos: aula 62"), (1791983684357, "macrófagos por MIF: aula 62"), (1791983677979, "DAMPs na inflamação crônica: aula 62"),
 (1791983686733, "remodelamento na asma: aula 64"), (1791716416026, "TGF-β no granuloma: aula 47"), (1791716413152, "proliferação local no granuloma: aula 47"),
 (1791628676621, "doença de Jorge Lobo: Microbiologia"), (1790974694280, "Crohn skip lesions: Anatomia UC08"),
 (1792239823571, "resolução da pneumonia lobar: Correlação 1"), (1792239823071, "consolidação: Correlação 1"), (1791023362943, "renovação do epitélio gástrico: UC08"),
 (1791023294649, "capilares fenestrados da vilosidade: UC08"), (1790980910230, "vilosidades: UC08"), (1791023299118, "contração da vilosidade: UC08"), (1791023355944, "células mioepiteliais: UC08"),
 (1792695028263, "HPV e estrato basal: Micro 58"), (1791629596922, "transcitose de IgA: Imuno"), (1791780352317, "congestão capilar: aula 38"),
]
FORA_DO_RECORTE = [
 "Capa e encerramento (lâminas 1 e 45).",
 "Cascata da coagulação e fatores de coagulação: aula 69 Hemostasia, trombose, embolia e infarto; aqui só os plugs primário e secundário (lâminas 18 a 20).",
 "Cicatrização por terceira intenção e tipos de fio de sutura: só no vídeo e na analogia do professor; sem princípio de ciclo básico.",
 "Tip cells e stalk cells, Notch e DLL4: só na apostila; sem card de acervo, vai no Tab da angiogênese.",
 "Síntese do colágeno em etapas e outros tipos de colágeno: Bioquímica (UC02); a lâmina 28 é ilustração.",
 "HER2, anti-TNF e bloqueio de fatores como tratamento: farmacologia (UC19) e aulas de tumores.",
 "Escorbuto e quadro clínico da deficiência de vitamina C: Nutrição; aqui só a vitamina C na hidroxilação do colágeno e na cicatrização.",
 "Fatores de crescimento EGF, TGF-α, HB-EGF além de HGF e KGF: tabela da lâmina 8 sem fala nem prova; no Tab.",
 "Reparo do DNA e telômeros: outra aula (Biomol 85); aqui 'reparo' é tecidual.",
 "Reepitelização por células basais, epiderme mais fina e cor da cicatriz pelo melanócito (lâmina 35), anexos cutâneos e queratina: Tab.",
]
A_, B_, C_, D_, E_, F_, G_, H_ = "A-arcabouco-regeneracao", "B-tecidos-celulas-tronco", "C-fatores-matriz", "D-fases-hemostasia", "E-inflamatoria", "F-proliferativa", "G-maturacao-intencao", "H-reparo-inflamacao-cronica"

CARDS = [
 # ---------- Lâminas 2–3: regeneração × reparo e o arcabouço (princípio) ----------
 au("c-org-destinos", ORG("<b>Outcome of tissue injury</b> by tissue and lesion:<br>- renewing tissue (skin, gut): {{c1::regeneration}}<br>- stable tissue after resection (liver): compensatory growth<br>- deep wound: {{c1::scar}}<br>- chronic inflammation: {{c1::fibrosis}}"),
    "V-pilar", A_, "Quatro destinos da lesão", 2, "lâmina 2; transcrição p.4; Robbins cap.3", motivacao="m2", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Eu tenho de um lado os tecidos que estão se renovando constantemente",
    fontes=F("transcrição p.4", "Eu tenho de um lado os tecidos que estão se renovando constantemente"),
    extra="Regeneration and compensatory growth need replicating cells and a surviving scaffold.<br>Scar and fibrosis are what remains when the scaffold is lost or the injury persists." + IMG("destinos")),
 au("c-arcabouco", "After cell loss, the surviving cells can rebuild the original tissue only if its <b>scaffold</b>, the {{c1::extracellular matrix}}, survives",
    "V-pilar", A_, "O arcabouço decide regeneração ou cicatriz", 3, "lâminas 3; transcrição p.6; apostila cap.2; prova 2016 P2 1.7", motivacao="m1",
    fontes=F("transcrição p.6", "Mas eu dependo também do arcabouço"),
    imagem="im65-arcabouco.png",
    extra="Surviving cells rebuild the original pattern on the scaffold.<br>Without it they replicate but disorganize, and matrix is deposited as scar.<br>The brain scaffold is made of neuronal and glial processes, so brain infarcts liquefy." + IMG("arcabouco")),
 # ---------- Lâmina 4: tecidos lábeis, estáveis e permanentes ----------
 K(1487981487576, "A-aula", B_, "Tecido lábil", 4, "lâmina 4: lábeis ciclam sempre"),
 K(1487981494590, "A-aula", B_, "Tecido estável", 4, "lâmina 4: estáveis voltam ao ciclo quando necessário"),
 K(1487981520428, "A-aula", B_, "Tecido permanente sem regeneração", 4, "lâmina 4: permanentes cicatrizam"),
 # ---------- Lâminas 5–6: células-tronco ----------
 au("c-org-nichos", ORG("<b>Somatic stem cells</b> give only the cells of their own tissue:<br>- intestinal crypt: {{c1::Paneth}}, goblet and absorptive cells<br>- hair follicle bulge: {{c1::keratinocytes}}<br>- eye limbus: corneal or conjunctival epithelium<br>- liver: hepatocytes or {{c1::bile duct}} cells"),
    "A-aula", B_, "O que cada nicho de célula-tronco somática origina", 6, "lâmina 6; transcrição p.12; apostila cap.2", motivacao="m6", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Elas são comprometidas por linhagens específicas",
    fontes=F("transcrição p.12", "ela só dá queratinócito, ela não dá célula de Paneth") + F("transcrição p.12", "Na córnea, ela pode estar no limbo ali do olho") + F("transcrição p.12", "células que vão fazer o revestimento da córnea ou células que vão compor a conjuntiva") + F("transcrição p.12", "eu posso ter alguma célula que podem dar ou ducto biliar ou hepatócito"),
    imagem="im65-nichos.png",
    extra="The restriction comes from genetic programming plus the local microenvironment.<br>A crypt stem cell never makes keratinocytes, and a follicle stem cell never makes Paneth cells." + IMG("nichos")),
 K(1486608763486, "A-aula", B_, "Células-tronco do intestino na cripta", 6, "lâmina 6: cripta intestinal; HY 1"),
 # ---------- Lâmina 7: ciclo celular ----------
 K(1468101709109, "A-aula", B_, "Célula estável entra em G1 quando estimulada", 7, "lâmina 7: G0 → G1 por fator de crescimento"),
 K(1468101721156, "A-aula", B_, "Célula lábil nunca entra em G0", 7, "lâmina 7: lábeis ciclam sempre"),
 # ---------- Lâminas 8–9: fatores de crescimento ----------
 K(1487981558376, "V-pilar", C_, "TGF-β medeia fibrose e angiogênese", 8, "lâminas 8 e 9: TGF-β promove fibrose"),
 K(1487981564266, "A-aula", C_, "PDGF estimula o fibroblasto", 8, "lâmina 8: PDGF e síntese de colágeno"),
 # ---------- Lâmina 10: regeneração × reparo, crescimento compensatório ----------
 au("c-crescimento-comp", "After <b>partial hepatectomy</b> the remaining liver regrows to near its original size, but not its shape, by {{c1::compensatory growth::process}}",
    "V-pilar", A_, "Crescimento compensatório do fígado", 10, "lâmina 10; transcrição p.20; prova 2015 P2 3.4", motivacao="m3",
    fontes=F("transcrição p.20", "crescimento compensatório"),
    imagem="im65-crescimento.png",
    extra="Also called compensatory hyperplasia: stable hepatocytes leave G0 under growth factors and replicate on the remaining architecture.<br>The lost lobes do not return, so this is not true regeneration.<br>It makes living donor liver transplant possible." + IMG("crescimento")),
 # ---------- Lâminas 11–12: matriz extracelular ----------
 au("c-mec-funcoes", "Matrix <b>proteoglycans</b> bind and store {{c1::growth factors}}, giving the tissue its signaling microenvironment",
    "A-aula", C_, "A matriz guarda fatores de crescimento", 11, "lâmina 11; transcrição p.22", motivacao="m9",
    fontes=F("transcrição p.22", "reter líquidos e alguns mediadores como fatores de crescimento") + F("transcrição p.22", "que retém líquido, que criam a possibilidade de eu guardar ali por mais tempo mediadores"),
    sem_imagem="função da matriz em texto na lâmina 11; a figura da lâmina 12 está em c-integrinas",
    extra="When injury remodels the matrix, the stored factors are released and stimulate repair.<br>Fibrillar components such as collagen and elastin give structure, while proteoglycans hold fluid and keep mediators near for paracrine action."),
 au("c-integrinas", "Cells anchor to the <b>matrix</b> through {{c1::integrins}}, which signal through the cytoskeleton to the nucleus",
    "A-aula", C_, "Integrinas sinalizam célula-matriz", 12, "lâmina 12; transcrição p.24", motivacao="m10",
    fontes=F("transcrição p.24", "Moléculas de adesão vão ancorar nesses componentes ﬁbrilares"),
    imagem="im65-integrinas.png",
    extra="This signaling sets cell polarity and tells the cell whether it has room to grow.<br>Contact inhibition works through cell to matrix contact, not only cell to cell." + IMG("integrinas")),
 # ---------- Lâminas 13–17: etapas e fases ----------
 K(1487981574852, "A-aula", D_, "Primeira intenção: bordas aproximadas", 14, "lâmina 14: ferida fina", text="<div><b>Cutaneous healing</b> by {{c1::primary}}<u> intention</u> is when the <b>wound edges are brought together</b> (e.g., suturing a surgical incision)</div>"),
 au("c-org-fases", ORG("<b>Wound healing</b> phases by time and event:<br>- first day, platelet plug and fibrin: {{c1::hemostasis}}<br>- next days, neutrophils then macrophages: {{c1::inflammatory}}<br>- first 3 weeks, fibroblasts, collagen and new capillaries: {{c1::proliferative}}<br>- 3 weeks to 2 years, collagen remodeling: {{c1::maturation}}"),
    "V-pilar", D_, "Fases da cicatrização e seus tempos", 13, "lâminas 13 e 15 a 17 (o gráfico das fases está nas lâminas 13 e 16); transcrição p.26 e p.30; prova 2025 P3 4.2", motivacao="m11", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Inﬂamatória, proliferativa e a de maturação",
    fontes=F("transcrição p.30", "Inﬂamatória, proliferativa e a de maturação dessa ferida"),
    extra="The phases overlap, and timing varies with wound size, location and infection.<br>The text slides give days 2 to 4 for inflammation and days 4 to 21 for proliferation, and the graph gives 4 to 6 and 4 to 24." + IMG("fases")),
 # ---------- Lâminas 18–20: hemostasia ----------
 K(1473985984856, "A-aula", D_, "Hemostasia secundária estabiliza com fibrina", 19, "lâmina 19: plug secundário", text="<div><b>Secondary hemostasis</b> stabilizes the <b>platelet plug</b> with {{c1::fibrin}}</div>"),
 # ---------- Lâminas 21–25: fase inflamatória ----------
 K(1487642786172, "A-aula", E_, "Macrófagos depois dos neutrófilos", 21, "lâmina 21: neutrófilo no 2º a 4º dia, depois macrófago; HY 1"),
 au("c-m1-m2", ORG("<b>Wound macrophages</b> by function:<br>- {{c1::M1}}: kills microbes, clears debris, makes TNF and IL-1<br>- {{c1::M2}}: clears apoptotic cells, makes IL-10 and TGF-β"),
    "V-pilar", E_, "M1 depois M2 na ferida", 22, "lâmina 22; transcrição p.26 e p.42", motivacao="m15", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="No começo, M1, porque tem um monte de destruição tecidual",
    fontes=F("transcrição p.26", "No começo, M1"),
    extra="M1 comes first and M2 later, once damage signals fade, induced by IFN-γ and by IL-4 and IL-13.<br>M2 TGF-β stimulates fibroblasts and new vessels, which starts the proliferative phase." + IMG("m1m2")),
 K(1520715124462, "A-aula", E_, "IL-10 e TGF-β mediam a resolução", 23, "lâmina 23: IL-10 e TGF-β; HY 3"),
 au("c-neutrofilo-dano", "In the first days <b>neutrophils</b> enter the <b>wound</b>, drawn by bacterial products and by signals from injured host cells, the {{c1::DAMPs}}",
    "V-pilar", D_, "Neutrófilo migra por produtos bacterianos e DAMPs", 21, "lâmina 21: polimorfonucleares", motivacao="m14",
    fontes=F("slides p.21", "Migração conforme demanda"),
    sem_imagem="fato de uma fase da cicatrização, sem figura própria; a sequência das fases está em c-org-fases",
    extra="DAMPs (damage-associated molecular patterns) are signals released by damaged cells, so tissue damage itself calls the neutrophils even without infection.<br>Macrophages replace them on days 2 to 4."),
 # ---------- Lâminas 26–35: fase proliferativa ----------
 K(1487981531796, "V-pilar", F_, "Fase proliferativa é o tecido de granulação", 26, "lâmina 26: proliferativa; HY 1"),
 K(1487981539804, "A-aula", F_, "Fibroblasto deposita colágeno III", 27, "lâmina 27: fibroblasto e colágeno"),
 K(1476583833764, "A-aula", F_, "Vitamina C hidroxila prolina e lisina no colágeno", 28, "lâmina 28: síntese do colágeno; HY 1"),
 K(1487981545623, "V-pilar", F_, "Colágeno III vira I no remodelamento", 29, "lâmina 29: III → I; HY 1"),
 au("c-angiogenese", "In the wound bed, <b>hypoxia</b> and VEGF make endothelial cells sprout new capillaries that are {{c1::immature and leaky}}",
    "A-aula", F_, "Angiogênese com vasos imaturos e permeáveis", 31, "lâmina 31; transcrição p.60; apostila cap.4", motivacao="m18",
    fontes=F("transcrição p.60", "Esses vasos são menores, são imaturos"),
    imagem="im65-angiogenese.png",
    extra="Leaky vessels let nutrients and cells reach the granulation tissue.<br>Later, as collagen builds and inflammation fades, the vessels mature and many regress." + IMG("angiogenese")),
 K(1487981537242, "V-pilar", F_, "Tecido de granulação: colágeno III, capilares e miofibroblastos", 33, "lâminas 32 a 34: componentes; HY 1; prova 2016 P2 2.4", text="<div><b>Granulation tissue</b> consists of type III collagen, {{c1::capillaries}}, and myofibroblasts</div>"),
 au("c-maturacao", "In the <b>maturation phase</b> the <b>granulation tissue</b> becomes scar as surplus vessels {{c1::regress}} and collagen is remodeled",
    "V-pilar", D_, "Maturação regride vasos e remodela colágeno", 36, "lâmina 36: 21º dia até 2 anos", motivacao="m21",
    fontes=F("slides p.36", "Regressão dos vasos"),
    sem_imagem="fato da fase de maturação, sem figura própria; os tempos das fases estão em c-org-fases",
    extra="It runs from day 21 to 2 years. Once inflammation fades the new capillaries are no longer needed, and remodeling reduces edema.<br>Tensile strength reaches at most 70 to 80% of normal."),
 K(1487981594443, "V-prova", G_, "70 a 80% da força em 3 meses", 38, "lâmina 38: força tênsil; transcrição p.74 e p.78"),
 K(1487981592613, "A-aula", G_, "Deiscência após cirurgia abdominal", 38, "lâmina 38: cicatriz é ponto de fragilidade (hérnia incisional)"),
 # ---------- Lâminas 39–41: segunda intenção e fatores que atrasam ----------
 K(1487981578907, "A-aula", G_, "Segunda intenção: bordas não aproximadas", 39, "lâminas 39 e 41: úlcera"),
 K(1487981543711, "A-aula", G_, "Miofibroblasto contrai a ferida", 40, "lâmina 40: contração; Robbins"),
 K(1487981587235, "A-aula", G_, "Infecção atrasa a cicatrização", 41, "lâmina 41: infecção é a causa local mais importante; transcrição p.30"),
 au("c-imunossupressao", "In an <b>immunosuppressed</b> patient the wound heals slowly because the {{c1::inflammatory}} phase is not properly triggered",
    "V-prova", D_, "Imunossupressão bloqueia a fase inflamatória", 15, "lâmina 15 (fases); transcrição p.30; prova 2025 P3 4.2", motivacao="m24",
    fontes=F("provas 2025 P3 4.2", "A principal fase comprometida neste caso é a fase inflamatória"),
    sem_imagem="raciocínio de prova sobre a ordem das fases, sem figura; as fases estão em c-org-fases",
    extra="Without it the later phases receive no stimulus.<br>Its macrophages and cytokines are what activate fibroblasts and angiogenesis in the proliferative phase."),
 # ---------- Lâminas 42–44: reparo na inflamação crônica ----------
 au("c-macrofago-reparo", ORG("<b>Macrophage mediators</b> by role in wound repair:<br>- debridement: phagocytosis, collagenase and elastase<br>- antimicrobial defense: {{c1::nitric oxide}} and ROS<br>- angiogenesis: {{c1::VEGF}} and FGF-2"),
    "A-aula", H_, "Mediadores do macrófago por papel no reparo", 42, "lâmina 42; transcrição p.86", motivacao="m25", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="E, de novo, o macrófago é importante",
    fontes=F("transcrição p.86", "E, de novo, o macrófago é importante") + F("lâmina 42", "Reparo na Inflamação"),
    extra="Macrophages also drive fibroblast growth with PDGF and TGF-β and remodel the matrix." + IMG("macrofago")),
 au("c-fibrose-mec", "<b>Persistent injury</b> keeps macrophages and lymphocytes active, which raise collagen synthesis and lower the activity of {{c1::metalloproteinases}}, causing fibrosis",
    "V-prova", H_, "Fibrose: mais síntese e menos degradação", 43, "lâmina 43; transcrição p.88; prova 2018 P3 4.2 e 2015 P2sub 3.2", motivacao="m25",
    fontes=F("transcrição p.88", "esses macrófagos são ativados"),
    imagem="im65-fibrose.png",
    extra="They release PDGF, FGF and TGF-β and cytokines such as TNF, IL-1, IL-4 and IL-13, which drive the fibroblasts, while less collagen is degraded.<br>It is the scar mechanism spread through the organ, and in Crohn disease it retracts the wall and can obstruct it." + IMG("fibrose")),
 # ---------- Lâmina 44: destinos finais e cicatrizes patológicas ----------
 K(1487981599441, "A-aula", H_, "Cicatriz hipertrófica respeita a borda", 44, "transcrição p.18; palavras-cruzadas e Robbins: excesso de colágeno"),
 K(1487981612881, "A-aula", H_, "Queloide ultrapassa a borda", 44, "palavras-cruzadas: queloide; Robbins"),
]

finalizar(CARDS, HERE, BUSCA)


# v12 (forma_das_lacunas): negrito, itálico e sublinhado ficam fora da lacuna; o resto do formato do AnKing é preservado
from nebli.spec_lib import _call as _chamada
_ids = [c["src"] for c in CARDS if c["kind"] == "text" and "text" not in c]
_vivas = {n["noteId"]: n["fields"].get("Text", {}).get("value", "") for n in (_chamada("notesInfo", notes=_ids) if _ids else [])}
_CZ = _re.compile(r"\{\{c(\d+)::(.*?)\}\}", _re.S)
def _limpa(m):
    corpo = _re.sub(r"</?(?:b|i|u|strong|em)>", "", m.group(2))
    return "{{c" + m.group(1) + "::" + corpo + "}}"
for _c in CARDS:
    if _c["kind"] == "text" and "text" not in _c:
        _novo = _CZ.sub(_limpa, _vivas.get(_c["src"], ""))
        if _novo and _novo != _vivas.get(_c["src"], ""):
            _c["text"] = _novo

_V = {"ak1476583833764": "Vitamin C deficiency, or scurvy, weakens the collagen and so delays wound healing.<br>Zinc deficiency also delays healing, since collagenase needs zinc to swap type III for type I collagen.",
 "ak1468101709109": "Stable tissues include the liver, lymphocytes, renal tubule cells and periosteum.<br>They sit in G0 until a growth factor pushes them into G1.",
 "ak1468250215718": "Collagen is the fibrillar component that gives the scaffold its structure and strength.",
 "ak1487981574852": "Closer edges leave a smaller matrix gap to fill, so less disorganized scar forms.<br>Sutures only bring the edges together and give no strength, so a tight stitch makes a bigger scar and skin sutures come out at 7 to 10 days.",

 "ak1487981539804": "Fibroblasts are stimulated by TGF-β, PDGF, EGF and IL-1 and lay down loose type III collagen first.",
 "ak1487981537242": "These three components give the red, moist bed of a healing wound, with capillaries, fibroblasts and a few inflammatory cells.",
 "ak1487981541929": "New capillaries are immature and leaky, which brings oxygen and nutrients to the busy fibroblasts.",
 "ak1487981592613": "A scar never regains full strength, so a sudden rise in abdominal pressure can reopen it.",
 "ak1487981578907": "A large or infected gap cannot be closed with stitches, so granulation tissue fills it from the base.<br>It has more inflammation and wound contraction than primary intention, a bigger scar, and it is slower.",

 "ak1487981543711": "Myofibroblasts pull the margins together, which shrinks the wound area.",
 "ak1473985984856": "Primary hemostasis makes a weak platelet plug first, and activated platelets also release serotonin, histamine and PDGF, which cause vasodilation and permeability and start the inflammation.",
 "ak1487981587235": "Infection keeps inflammation going, so the wound cannot move on to the proliferative phase.<br>Poor nutrition, poor perfusion and hyperglycemia, which glycates new collagen, also delay healing.",
 "ak1487981599441": "A hypertrophic scar has excess collagen but stays inside the original wound margins.<br>Its collagen is laid out in parallel bundles, unlike the disorganized bundles of a keloid.",
 "ak1487981612881": "A keloid has disorganized collagen with markedly increased type I and III synthesis.<br>It tends to recur after excision, unlike a hypertrophic scar."}
for _c in CARDS:
    if _c["key"] in _V and _c["kind"] != "autoral":
        _c["extra_add"] = _V[_c["key"]] + ("<br>" + _c["extra_add"] if _c.get("extra_add") else "")
for _c in CARDS:
    if _c["key"] == "ak1487981537242":
        _c["extra_add"] = _c.get("extra_add", "") + IMG("granulacao-histo")
    elif _c["key"] == "ak1487981594443":
        _c["extra_add"] = _c.get("extra_add", "") + IMG("forca")
    elif _c["kind"] == "text":
        _c["sem_imagem"] = "fato de texto do AnKing sem figura focal na aula; a figura do bloco está no card autoral ou no card de acervo vizinho"
    if _c["kind"] == "autoral" and _c.get("imagem"):
        _c["slide_sem_alternativa"] = "a figura é do Robbins reproduzida na lâmina da aula, que é a referência do deck; o livro da corrida só tem o texto extraído, sem a figura em resolução utilizável; recorte em 2,4x a 3x"

VERSO = {}  # chave: "- linha curta" para nota de acervo sem Extra (gate de verso)
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"c-org-destinos": "ganho: junta os quatro destinos por tipo de tecido e lesão (lâmina 2), enquanto c-arcabouco explica por que o arcabouço decide",
 "c-arcabouco": "ganho: o princípio causal do arcabouço; c-org-destinos mapeia os destinos por tecido",
 "c-macrofago-reparo": "ganho: mediadores de cada papel do macrófago, enquanto c-m1-m2 trata dos fenótipos e sh-1791983682407 do TGF-β do M2"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "im65-destinos.png": "lâmina 2: esquema de Robbins com os quatro destinos da lesão (renovação, estável, ferida, inflamação crônica) e seus desfechos; no verso do organizador, não na frente",
 "im65-arcabouco.png": "lâmina 3: lóbulo hepático com lesão só das células (regeneração) e das células e da matriz (reparo por cicatriz); mostra os dois polos do card",
 "im65-crescimento.png": "lâmina 10: fígado antes e depois da ressecção, lobo remanescente crescendo, TC das duas fases e ciclo celular com priming; sem título que dê a resposta",
 "im65-nichos.png": "lâmina 6: pele (bulge do folículo), intestino (cripta), fígado e córnea (limbo) com os nichos marcados; os quatro painéis do organizador",
 "im65-integrinas.png": "lâmina 12: matriz, integrinas, adesões focais, citoesqueleto e núcleo com os caminhos de sinalização; legível em 2,6x",
 "im65-fases.png": "lâmina 16: curva das três fases sobrepostas com inflamação 4 a 6 dias, proliferação 4 a 24 dias e remodelação 21 dias a 2 anos",
 "im65-intencoes.png": "lâmina 14: ferida fina (A) e ferida com cicatriz e contração (B) em 24 horas, 3 a 7 dias e semanas",
 "im65-m1m2.png": "lâmina 22: macrófago M2 resolutivo e M1 inflamatório com indutores, produtos e funções de cada lado",
 "im65-angiogenese.png": "lâmina 31: vaso que brota em rede de capilares em quatro etapas, sem fatores de crescimento rotulados",
 "im65-macrofago.png": "lâmina 42: macrófago com os cinco papéis no reparo e os mediadores de cada um",
 "im65-fibrose.png": "lâmina 43: fluxo de estímulo persistente a fibrose com fatores de crescimento, citocinas e redução de metaloproteinases",
 "im65-granulacao-histo.png": "lâmina 33: histologia do tecido de granulação com vasos, fibroblastos e células inflamatórias em colágeno frouxo; legível em 2,6x",
 "im65-forca.png": "lâmina 38: duas curvas de força tênsil no tempo, uma em semanas (até cerca de 80%) e outra comparando tecido ferido e íntegro",
}
REVISAO = {}
ESCOPO = {"objetivo": "Explicar por que um tecido regenera e outro cicatriza (arcabouço, tecidos lábeis, estáveis e permanentes, células-tronco, fatores de crescimento e matriz) e o reparo da ferida em fases até a fibrose da inflamação crônica; clínica só como exemplo do mecanismo.",
          "centrais": [["Neutrófilo e DAMPs", "c-neutrofilo-dano"], ["Maturação", "c-maturacao"], ["Destinos da lesão", "c-org-destinos"], ["Arcabouço", "c-arcabouco"], ["Crescimento compensatório", "c-crescimento-comp"], ["Fases", "c-org-fases"],
                       ["M1 e M2", "c-m1-m2"], ["Primeira e segunda intenção", "ak1487981578907"], ["Imunossupressão", "c-imunossupressao"], ["Fibrose", "c-fibrose-mec"], ["Tecido de granulação", "ak1487981531796", "ak1487981537242"],
                       ["Colágeno III e I", "ak1487981545623"], ["Vitamina C", "ak1476583833764"], ["Força tênsil", "ak1487981594443"]],
          "exemplos": ["ak1487981599441", "ak1487981612881", "ak1487981587235"],
          "outras_aulas": ["sh-1791983683185", "sh-1791983683760", "sh-1792242119048"]}
_slide = lambda c: int(_re.search(r"\d+", c["evid"]).group())
CARDS.sort(key=_slide)
