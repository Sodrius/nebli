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
_IMGS = ("destinos", "arcabouco", "crescimento", "potencia", "nichos", "integrinas", "fases", "intencoes", "m1m2", "angiogenese", "reepit", "macrofago", "fibrose", "granulacao-histo", "forca")
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
 (1487460268378, "tecido permanente só hipertrofia: aula 11 Acúmulos e adaptação"), (1479425811082, "neurônios permanentes: repete os exemplos de tecido permanente"),
 # NEBLI vivo de outras aulas
 (1793301697517, "proteases de neutrófilos destroem o arcabouço na hepatite: detalhe da aula 61; o princípio entra pelos dois cards da 61 e por c-arcabouco"),
 (1791625434457, "M2 por Th2 na inflamação crônica: repete sh-1791983682407 e sh-1791983681904 (aula 62)"),
 (1791910086149, "fatores de macrófago e fibroblasto no granuloma: repete PDGF e TGF-β da 62"),
 (1791780349490, "transcitose por VEGF: detalhe da inflamação aguda (38)"),
 (1791743342606, "monócitos depois dos neutrófilos: repete 1487642786172"),
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
 "Cor e pigmentação da cicatriz em detalhe, anexos cutâneos e queratina: só uma frase no Extra da reepitelização.",
]
A_, B_, C_, D_, E_, F_, G_, H_ = "A-arcabouco-regeneracao", "B-tecidos-celulas-tronco", "C-fatores-matriz", "D-fases-hemostasia", "E-inflamatoria", "F-proliferativa", "G-maturacao-intencao", "H-reparo-inflamacao-cronica"

CARDS = [
 # ---------- Lâminas 2–3: regeneração × reparo e o arcabouço (princípio) ----------
 au("c-org-destinos", ORG("<b>Outcome of tissue injury</b> by tissue and lesion:<br>- renewing tissue (skin, gut): {{c1::regeneration}}<br>- stable tissue after resection (liver): {{c1::compensatory growth}}<br>- deep wound: {{c2::scar}}<br>- chronic inflammation: {{c2::fibrosis}}"),
    "V-pilar", A_, "Quatro destinos da lesão", 2, "lâmina 2; transcrição p.4; Robbins cap.3", motivacao="m2", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="crescimento compensatório",
    fontes=F("transcrição p.4", "Eu tenho de um lado os tecidos que estão se renovando constantemente"),
    extra="Regeneration and compensatory growth need replicating cells and a surviving scaffold.<br>Scar and fibrosis are what remains when the scaffold is lost or the injury persists." + IMG("destinos")),
 K(1487981353937, "A-aula", A_, "Regeneração é reposição com tecido nativo", 2, "lâmina 2: definição de regeneração; Pathoma e First Aid"),
 K(1487981526005, "A-aula", A_, "Reparo é reposição por cicatriz", 2, "lâmina 2: definição de reparo; par da regeneração"),
 au("c-arcabouco", "Cell loss with the <b>matrix scaffold intact</b> ends in {{c1::regeneration}}, but loss of the <b>scaffold</b> ends in {{c1::scar}}",
    "V-pilar", A_, "O arcabouço decide regeneração ou cicatriz", 3, "lâminas 3; transcrição p.6; apostila cap.2; prova 2016 P2 1.7", motivacao="m1",
    fontes=F("transcrição p.6", "Mas eu dependo também do arcabouço"),
    imagem="im65-arcabouco.png",
    extra="Surviving cells rebuild the original pattern on the scaffold.<br>Without it they replicate but disorganize, and matrix is deposited as scar.<br>The brain scaffold is made of neuronal and glial processes, so brain infarcts liquefy." + IMG("arcabouco")),
 sh(1793301695344, "azul", A_, "Infecção aguda poupa a reticulina e regenera", 3, "A-aula: lâmina 3, hepatite A destrói hepatócitos e mantém as trabéculas; card da aula 61 associado"),
 sh(1793301698344, "azul", A_, "Perda maior que a regeneração colapsa a reticulina e vira septo de colágeno", 3, "A-aula: lâmina 3, hepatite B e crônicas destroem o arcabouço; card da aula 61 associado"),
 # ---------- Lâmina 4: tecidos lábeis, estáveis e permanentes ----------
 K(1487981487576, "A-aula", B_, "Tecido lábil", 4, "lâmina 4: lábeis ciclam sempre"),
 K(1487981494590, "A-aula", B_, "Tecido estável", 4, "lâmina 4: estáveis voltam ao ciclo quando necessário"),
 K(1487981520428, "A-aula", B_, "Tecido permanente sem regeneração", 4, "lâmina 4: permanentes cicatrizam"),
 K(1468101717082, "A-aula", B_, "Exemplos de tecido estável", 4, "lâmina 4 e transcrição p.4: fígado como estável"),
 K(1468101697168, "A-aula", B_, "Exemplos de tecido permanente", 4, "lâmina 4: neurônios, miocárdio e músculo esquelético"),
 sh(1791780363131, "azul", B_, "Cura por fibrose quando o tecido não regenera", 4, "A-aula: lâmina 4, tecido que não regenera repara por cicatriz; cópia suspensa por Davi na aula 38, volta para reavaliar"),
 # ---------- Lâminas 5–6: células-tronco ----------
 au("c-tronco-niveis", "<b>Embryonic</b> stem cells can give rise to any cell lineage, so they are {{c1::pluripotent}}",
    "R-detalhe", B_, "Pluripotente × comprometida × somática", 5, "lâmina 5; transcrição p.10", motivacao="m5",
    fontes=F("transcrição p.10", "células-tronco embrionárias, que são pluripotentes"),
    imagem="im65-potencia.png",
    extra="Lineage committed stem cells make only one germ layer's cells.<br>Adult somatic stem cells are narrower still, giving only the cell types of their own tissue." + IMG("potencia")),
 au("c-org-nichos", ORG("<b>Somatic stem cell niches</b> by tissue:<br>- small intestine: {{c1::crypt}} base<br>- skin: hair follicle {{c1::bulge}}<br>- cornea: {{c1::limbus}}"),
    "A-aula", B_, "Nichos de células-tronco somáticas", 6, "lâmina 6; transcrição p.12; apostila cap.2", motivacao="m6", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Isso acontece em todos os lugares",
    fontes=F("lâmina 6", "Células Tronco Somáticas"),
    imagem="im65-nichos.png",
    extra="Each niche gives only the cell types of its own tissue.<br>Crypt stem cells make absorptive, goblet and Paneth cells, but never keratinocytes." + IMG("nichos")),
 K(1486608763486, "A-aula", B_, "Células-tronco do intestino na cripta", 6, "lâmina 6: cripta intestinal; HY 1"),
 # ---------- Lâmina 7: ciclo celular ----------
 K(1468101709109, "A-aula", B_, "Célula estável entra em G1 quando estimulada", 7, "lâmina 7: G0 → G1 por fator de crescimento"),
 K(1468101721156, "A-aula", B_, "Célula lábil nunca entra em G0", 7, "lâmina 7: lábeis ciclam sempre"),
 # ---------- Lâminas 8–9: fatores de crescimento ----------
 au("c-org-fatores", ORG("<b>Growth factors</b> and their main target cell in repair:<br>- keratinocyte: {{c1::KGF}}<br>- hepatocyte: {{c1::HGF}}<br>- endothelial cell: {{c2::VEGF}}"),
    "R-org", C_, "Fator de crescimento e a célula-alvo", 8, "lâmina 8; transcrição p.16", motivacao="m7", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="fator de crescimento de endotélio vascular",
    fontes=F("transcrição p.16", "fator de crescimento de endotélio vascular"),
    sem_imagem="tabela de texto da lâmina 8, sem figura focal",
    extra="KGF is also called FGF-7 and comes from fibroblasts.<br>HGF comes from mesenchymal cells and also stimulates epithelial and endothelial cells.<br>VEGF also raises vascular permeability."),
 K(1487981558376, "V-pilar", C_, "TGF-β medeia fibrose e angiogênese", 8, "lâminas 8 e 9: TGF-β promove fibrose"),
 K(1487981560574, "A-aula", C_, "PDGF vem de plaquetas e macrófagos", 8, "lâmina 8: fonte do PDGF"),
 K(1487981564266, "A-aula", C_, "PDGF estimula o fibroblasto", 8, "lâmina 8: PDGF e síntese de colágeno"),
 K(1487981566131, "R-detalhe", C_, "FGF-2 e angiogênese", 8, "lâmina 8: FGF"),
 K(1487981568284, "A-aula", C_, "VEGF e angiogênese", 8, "lâmina 8: VEGF"),
 K(1496163125083, "A-aula", C_, "Tumor produz fatores angiogênicos", 9, "lâmina 9: VEGF e nutrição tumoral; liga a aula às de tumores"),
 # ---------- Lâmina 10: regeneração × reparo, crescimento compensatório ----------
 au("c-crescimento-comp", "After <b>partial hepatectomy</b> the remaining liver regrows to near its original size by {{c1::compensatory growth}}",
    "V-pilar", A_, "Crescimento compensatório do fígado", 10, "lâmina 10; transcrição p.20; prova 2015 P2 3.4", motivacao="m3",
    fontes=F("transcrição p.20", "crescimento compensatório"),
    imagem="im65-crescimento.png",
    extra="Stable hepatocytes leave G0 under growth factors and replicate on the remaining architecture.<br>The lost lobes do not return, so this is not true regeneration.<br>It makes living donor liver transplant possible." + IMG("crescimento")),
 # ---------- Lâminas 11–12: matriz extracelular ----------
 au("c-mec-funcoes", "Matrix <b>proteoglycans</b> bind and store {{c1::growth factors}}, giving the tissue its signaling microenvironment",
    "A-aula", C_, "A matriz guarda fatores de crescimento", 11, "lâmina 11; transcrição p.22", motivacao="m9",
    fontes=F("transcrição p.22", "a matriz extracelular é importante para prover suporte mecânico"),
    sem_imagem="função da matriz em texto na lâmina 11; a figura da lâmina 12 está em c-integrinas",
    extra="Fibrillar components such as collagen and elastin give structure.<br>Non fibrillar ones such as fibronectin and proteoglycans hold fluid and keep mediators near for paracrine action."),
 K(1468250215718, "A-aula", C_, "Colágeno organiza e fortalece a matriz", 11, "lâmina 11: componente fibrilar da matriz"),
 au("c-integrinas", "Cells anchor to the <b>matrix</b> through {{c1::integrins}}, which signal through the cytoskeleton to the nucleus",
    "A-aula", C_, "Integrinas sinalizam célula-matriz", 12, "lâmina 12; transcrição p.24", motivacao="m10",
    fontes=F("transcrição p.24", "Moléculas de adesão vão ancorar nesses componentes ﬁbrilares"),
    imagem="im65-integrinas.png",
    extra="This signaling sets cell polarity and tells the cell whether it has room to grow.<br>Contact inhibition works through cell to matrix contact, not only cell to cell." + IMG("integrinas")),
 # ---------- Lâminas 13–17: etapas e fases ----------
 au("c-ponto", "Skin sutures come out after about {{c1::7 to 10}} days, since they only bring the edges together and do not give the wound strength",
    "V-prova", D_, "O ponto aproxima e não dá resistência", 14, "lâmina 14; transcrição p.28; prova 2015 P2sub 3.1", motivacao="m12",
    fontes=F("transcrição p.28", "Eu dou ponto só pra aproximar a borda"),
    sem_imagem="decisão cirúrgica explicada na fala, sem figura própria; a ferida fina e a com cicatriz estão em c-intencoes",
    extra="Closer edges leave less matrix gap to fill with imperfect scar.<br>A tight stitch for strength pulls the edges apart and makes a bigger scar.<br>Full strength returns only after weeks of remodeling."),
 K(1487981574852, "A-aula", D_, "Primeira intenção: bordas aproximadas", 14, "lâmina 14: ferida fina"),
 K(1487981576976, "A-aula", D_, "Primeira intenção deixa cicatriz mínima", 14, "lâmina 14: ferida fina, cicatriz mínima"),
 au("c-org-fases", ORG("<b>Wound healing</b> phases by time and event:<br>- day 1, platelet plug and fibrin: {{c1::hemostasis}}<br>- days 2 to 4, neutrophils then macrophages: {{c1::inflammatory}}<br>- days 4 to 21, granulation tissue: {{c2::proliferative}}<br>- day 21 to 2 years, collagen remodeling: {{c2::maturation}}"),
    "V-pilar", D_, "Fases da cicatrização e seus tempos", 16, "lâminas 15 a 17; transcrição p.26 e p.30; prova 2025 P3 4.2", motivacao="m11", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Inﬂamatória, proliferativa e a de maturação",
    fontes=F("transcrição p.30", "Inﬂamatória, proliferativa e a de maturação dessa ferida"),
    extra="The phases overlap, and their duration depends on wound size, location and infection.<br>Each phase prepares the next." + IMG("fases")),
 # ---------- Lâminas 18–20: hemostasia ----------
 K(1473982141617, "A-aula", D_, "Hemostasia primária forma plug plaquetário frágil", 18, "lâmina 18: plug primário"),
 K(1473985984856, "A-aula", D_, "Hemostasia secundária estabiliza com fibrina", 19, "lâmina 19: plug secundário"),
 sh(1791780353997, "azul", D_, "Plaqueta libera serotonina e histamina e aumenta a permeabilidade", 20, "A-aula: lâmina 20, a plaqueta ativada inicia a inflamação; cópia suspensa por Davi na aula 38, volta para reavaliar"),
 # ---------- Lâminas 21–25: fase inflamatória ----------
 K(1487642786172, "A-aula", E_, "Macrófagos depois dos neutrófilos", 21, "lâmina 21: neutrófilo no 2º a 4º dia, depois macrófago; HY 1"),
 K(1463884007824, "V-prova", E_, "Corticoide inibe fibroblasto e atrasa a cicatrização", 21, "lâmina 21: corticoide diminui o macrófago; HY 2"),
 au("c-m1-m2", ORG("<b>Wound macrophages</b> by phase:<br>- early: {{c1::M1}}, kill microbes and clear debris<br>- later: {{c1::M2}}, clear apoptotic cells and secrete IL-10 and TGF-β"),
    "V-pilar", E_, "M1 depois M2 na ferida", 22, "lâmina 22; transcrição p.26 e p.42", motivacao="m15", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="No começo, M1",
    fontes=F("transcrição p.26", "No começo, M1"),
    extra="The switch happens once damage signals fade.<br>M2 TGF-β drives fibroblast, epithelial and endothelial proliferation, which starts the proliferative phase." + IMG("m1m2")),
 sh(1791983681904, "azul", E_, "M1 por micróbios e IFN-γ; M2 por IL-4 e IL-13", 22, "A-aula: lâmina 22, indutores do M1 e do M2; card da aula 62 associado"),
 sh(1791983682407, "verde", E_, "M2 impulsiona o reparo com TGF-β", 23, "V-pilar: lâmina 23, o TGF-β do M2 inicia a proliferação; card da aula 62 associado"),
 K(1520715124462, "A-aula", E_, "IL-10 e TGF-β mediam a resolução", 23, "lâmina 23: IL-10 e TGF-β; HY 3"),
 sh(1791780360877, "azul", E_, "TNF e IL-1 ligam inflamação ao reparo", 23, "A-aula: lâmina 23, TNF e IL-1 na fase inicial; cópia suspensa por Davi na aula 38, volta para reavaliar"),
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
 K(1487981537242, "V-pilar", F_, "Tecido de granulação: colágeno III, capilares e miofibroblastos", 33, "lâminas 32 a 34: componentes; HY 1; prova 2016 P2 2.4"),
 K(1487981541929, "A-aula", F_, "Capilares nutrem o tecido de granulação", 33, "lâmina 33: capilares"),
 au("c-reepitelizacao", "<b>Basal cells</b> of the epidermis proliferate to re-epithelialize the wound, and the new epidermis has fewer layers and less {{c1::keratin}}",
    "R-detalhe", F_, "Reepitelização por células basais", 35, "lâmina 35; transcrição p.66 e p.70", motivacao="m20",
    fontes=F("transcrição p.66", "comecem a proliferar e reepitelizar esse tecido"),
    imagem="im65-reepit.png",
    extra="The thinner epithelium shows the vessels below it, so the area looks red.<br>Scars lose skin appendages, and melanocytes repopulate poorly, so color can change." + IMG("reepit")),
 # ---------- Lâminas 36–38: maturação ----------
 K(1487981550712, "A-aula", G_, "Colagenase remove o colágeno III", 36, "lâmina 36: remodelação do colágeno"),
 K(1487981552881, "R-detalhe", G_, "Colagenase precisa de zinco", 36, "lâmina 36: metaloproteinase"),
 K(1487981594443, "V-prova", G_, "70 a 80% da força em 3 meses", 38, "lâmina 38: força tênsil; transcrição p.74 e p.78"),
 K(1487981592613, "A-aula", G_, "Deiscência após cirurgia abdominal", 38, "lâmina 38: cicatriz é ponto de fragilidade (hérnia incisional)"),
 # ---------- Lâminas 39–41: segunda intenção e fatores que atrasam ----------
 K(1487981578907, "A-aula", G_, "Segunda intenção: bordas não aproximadas", 39, "lâminas 39 e 41: úlcera"),
 K(1487981581148, "A-aula", G_, "Segunda intenção deixa cicatriz maior", 39, "lâmina 39: úlcera, cicatriz maior"),
 au("c-intencoes", "Compared with primary intention, <b>secondary intention</b> has more inflammation and granulation tissue, and wound {{c1::contraction}} closes the gap",
    "V-prova", G_, "Segunda intenção: mais granulação e contração", 40, "lâminas 14, 39 a 41; transcrição p.30 e p.82; prova 2025 P3 4.3", motivacao="m23",
    fontes=F("transcrição p.30", "Aliás, só pra continuar, se eu não tiver um corte bonitinho como esse"),
    imagem="im65-intencoes.png",
    extra="Edges that cannot be approximated, as in large ulcers, infected wounds and dehiscence, are left open.<br>The scar is bigger and slower, but safer than closing an infected wound over an abscess." + IMG("intencoes")),
 K(1487981543711, "A-aula", G_, "Miofibroblasto contrai a ferida", 40, "lâmina 40: contração; Robbins"),
 K(1524169597395, "R-detalhe", G_, "Contratura por MMP e miofibroblastos", 40, "lâmina 40: contração exagerada"),
 K(1487981589146, "V-prova", G_, "Vitamina C e cicatrização retardada", 41, "lâmina 41: o que atrasa; HY 3"),
 K(1476584079267, "A-aula", G_, "Zinco e cicatrização retardada", 41, "lâmina 41: o que atrasa; HY 2"),
 K(1487981587235, "A-aula", G_, "Infecção atrasa a cicatrização", 41, "lâmina 41: infecção é a causa local mais importante; transcrição p.30"),
 au("c-imunossupressao", "In an <b>immunosuppressed</b> patient the wound heals slowly because the {{c1::inflammatory}} phase is not properly triggered",
    "V-prova", G_, "Imunossupressão bloqueia a fase inflamatória", 41, "lâmina 41; prova 2025 P3 4.2", motivacao="m24",
    fontes=F("provas 2025 P3 4.2", "A principal fase comprometida neste caso é a fase inflamatória"),
    sem_imagem="raciocínio de prova sobre a ordem das fases, sem figura; as fases estão em c-org-fases",
    extra="Without that first phase the later ones receive no stimulus.<br>The inflammatory phase triggers the proliferative and maturation phases."),
 # ---------- Lâminas 42–44: reparo na inflamação crônica ----------
 au("c-macrofago-reparo", ORG("<b>Macrophage roles in wound repair</b> and their mediators:<br>- angiogenesis: {{c1::VEGF}} and FGF-2<br>- fibroblast and keratinocyte proliferation: {{c1::PDGF}}, TGF-β, KGF<br>- debridement: {{c2::collagenase}} and elastase<br>- antimicrobial defense: {{c2::nitric oxide}} and ROS"),
    "A-aula", H_, "Papéis do macrófago no reparo", 42, "lâmina 42; transcrição p.86", motivacao="m16", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="o macrófago é importante",
    fontes=F("transcrição p.86", "E, de novo, o macrófago é importante"),
    extra="Macrophages clean the wound and then recruit and stimulate the cells that rebuild it.<br>The same cell drives the fibrosis of chronic inflammation." + IMG("macrofago")),
 au("c-fibrose-mec", "Persistent injury keeps macrophages and lymphocytes active, raising collagen synthesis and lowering its degradation by {{c1::metalloproteinases}}, which causes fibrosis",
    "V-prova", H_, "Fibrose: mais síntese e menos degradação", 43, "lâmina 43; transcrição p.88; prova 2018 P3 4.2 e 2015 P2sub 3.2", motivacao="m25",
    fontes=F("transcrição p.88", "esses macrófagos são ativados"),
    imagem="im65-fibrose.png",
    extra="Growth factors PDGF, FGF and TGF-β and cytokines such as TNF, IL-1, IL-4 and IL-13 drive the fibroblasts.<br>The mechanism is the same as in a scar, but spread through the organ." + IMG("fibrose")),
 sh(1791780363380, "azul", H_, "Inflamação crônica mostra infiltrado mononuclear, angiogênese e fibrose", 43, "A-aula: lâmina 43; cópia suspensa por Davi na aula 38, volta para reavaliar"),
 K(1482374264661, "R-detalhe", H_, "Crohn: estenose e espessamento", 43, "transcrição p.88: a fibrose retrai a parede e obstrui, como no Crohn"),
 # ---------- Lâmina 44: destinos finais e cicatrizes patológicas ----------
 K(1487981599441, "A-aula", H_, "Cicatriz hipertrófica respeita a borda", 44, "transcrição p.18; palavras-cruzadas e Robbins: excesso de colágeno"),
 K(1487981602812, "R-detalhe", H_, "Hipertrófica: colágeno paralelo", 44, "Robbins: excesso de colágeno"),
 K(1487981612881, "A-aula", H_, "Queloide ultrapassa a borda", 44, "palavras-cruzadas: queloide; Robbins"),
 K(1487981616609, "R-detalhe", H_, "Queloide: colágeno desorganizado", 44, "Robbins: queloide"),
 K(1487981620664, "R-detalhe", H_, "Queloide: síntese de colágeno I e III muito aumentada", 44, "Robbins: queloide"),
 K(1487981629888, "R-detalhe", H_, "Queloide recidiva", 44, "Robbins: o queloide recidiva após a excisão"),
]

finalizar(CARDS, HERE, BUSCA)

VERSO = {}  # chave: "- linha curta" para nota de acervo sem Extra (gate de verso)
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {"objetivo": "", "centrais": [], "exemplos": [], "outras_aulas": []}
_slide = lambda c: int(_re.search(r"\d+", c["evid"]).group())
CARDS.sort(key=_slide)
