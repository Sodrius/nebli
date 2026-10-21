# Especificação curada — 64 Reações de hipersensibilidade (UC03 P3, Imunologia; 90 lâminas). Ordem da aula: tipo II, III, IV e I.
# Ciclo básico: os quatro tipos de Gell e Coombs pelo mecanismo e os exemplos que a aula nomeia, sem diagnóstico, tratamento nem fármacos.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = "Mecanismo causa→efeito da aula (sensibilização ao efetor de cada tipo e tempos), que o AnKing traz como classificação; exigido pela linha lógica de F-20261021-CLAUDE-02."
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-im64-20261021a"
SHORT = "im64"
LESSON = "2026-uc03-imunologia-64-hipersensibilidade"
DECK = "NEBLI::UC03::P3::Imunologia::Reações de hipersensibilidade"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261021-CLAUDE-01 + ANTI-EXEMPLARES §1–16, 21/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (21/10): seções de recurso do AnKing (tipos de hipersensibilidade, FirstAid e Bootcamp; busca/secoes); palavra-chave e significado "
         "em AnKing, Referências Externas e NEBLI vivo (busca/semantica.jsonl, uma consulta por conceito). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


G_, T2_, T3_, T4_, T1_ = "A-tipos", "B-tipo-II", "C-tipo-III", "D-tipo-IV", "E-tipo-I"
EXCLUIDOS = []
FORA_DO_RECORTE = [
    "Fotografias clínicas (pele, glomérulo, pulmão, esclerose múltipla, artrite), figuras de livro e imunofluorescência (lâminas 4–8, 16, 19–26, 32–38, 63–81): ilustram, não ensinam alvo.",
    "Diagnóstico (Coombs, prick test, IgE específica, patch test), tratamento (adrenalina, Rhogan, corticoide) e fármacos: clínica e farmacologia.",
    "Doenças por tipo (pênfigo, Goodpasture, púrpura, poliarterite, lúpus, artrite reumatoide, esclerose múltipla, diabetes, filariose): a aula é de mecanismo geral, não de doenças (F-20261021-CLAUDE-04); só entram exemplos que ilustram um mecanismo.",
    "Dados epidemiológicos e hereditariedade da atopia, níveis de IgE em atópicos (lâminas 36–40, 45–47): ilustração sem cobrança.",
]

CARDS = [
    # Intro (lâminas 1–2): o que é hipersensibilidade e os quatro tipos
    au("au-gell", ORG("<b>Hypersensitivity types</b>:<br>- I: {{c1::IgE}}<br>- II: antibodies against {{c2::cell-surface}} or matrix antigens<br>- III: {{c3::immune complexes}}<br>- IV: {{c4::T cells}}"),
       "V-pilar", G_, "Gell e Coombs: os quatro tipos", 2, "lâminas 2 e 3; transcrição (a aula abre com os quatro tipos pelo processo imunológico)",
       extra="- Hypersensitivity = tissue damage mediated by the immune system<br>- Types I, II and III are antibody-mediated; type IV is cell-mediated"),
    K(1487207248593, "V-pilar", G_, "Mediados por anticorpo: I, II e III", 2, "lâmina 2; seção FirstAid de hipersensibilidade"),
    # Tipo I (lâminas 43–90), na ordem em que a aula explica
    K(1487206917325, "V-pilar", T1_, "Tipo I: ligação cruzada de IgE em mastócitos pré-sensibilizados", 44, "lâmina 44; seção Bootcamp"),
    K(1487116878738, "V-pilar", T1_, "Th2 promove a produção de IgE", 48, "lâmina 48 (elementos-chave: IgE, Th2, mastócito, eosinófilo, FcεRI); seção Bootcamp"),
    au("au-sensib-cadeia", ORG("<b>Type I sensitization</b>:<br>- allergen activates {{c1::Th2}} cells<br>- IL-4 makes B cells secrete {{c2::IgE}}<br>- IgE arms the {{c3::mast cell}}"),
       "V-pilar", T1_, "Sensibilização: do alérgeno à IgE no mastócito", 54, "lâminas 53–55; transcrição (o primeiro contato só sensibiliza, a clínica é zero)",
       extra="- The reaction appears only at the next contact with the allergen<br>- IgE binds to the Fc receptors of the mast cell"),
    K(1487117161213, "V-pilar", T1_, "IL-4 e IL-13 promovem a troca de classe para IgE", 55, "lâmina 55 e transcrição (IL-4 ajuda na mudança de classe para IgE); seção Bootcamp"),
    K(1474580620228, "V-pilar", T1_, "IgE se liga ao receptor de alta afinidade FcεRI do mastócito", 60, "lâminas 58–61 (FcεRI); seção Bootcamp"),
    K(1487640139590, "A-aula", T1_, "Anafilatoxinas do complemento ativam mastócitos", 59, "lâmina 59 (trauma, neuropeptídeos, C3a e C5a também degranulam); seção de imunologia"),
    K(1487640136892, "V-pilar", T1_, "Ligação cruzada de IgE agrega FcεRI e inicia a degranulação", 62, "lâmina 62 (desencadeamento); seção B&B"),
    K(1487207084334, "V-pilar", T1_, "Resposta imediata: histamina e triptase pré-formadas", 66, "lâmina 66 (reação imediata); seção FirstAid"),
    K(1474571583341, "A-aula", T1_, "Histamina age no receptor H1", 70, "lâmina 70 (histamina: vasodilatação e permeabilidade); seção Bootcamp"),
    K(1474571630796, "A-aula", T1_, "Histamina aumenta a permeabilidade vascular", 70, "lâminas 70 e 73 (edema); seção Bootcamp"),
    K(1473628116213, "A-aula", T1_, "Mastócito gera os leucotrienos C4, D4 e E4", 73, "lâmina 73 (prostaglandinas e leucotrienos); seção Bootcamp"),
    K(1474571636173, "A-aula", T1_, "Histamina contrai o músculo liso brônquico", 73, "lâmina 73 (broncoconstrição); seção Bootcamp"),
    K(1487207091819, "V-pilar", T1_, "Resposta tardia: quimiocinas e citocinas", 73, "lâminas 71–73 (fase tardia, horas); seção FirstAid"),
    K(1473628119069, "A-aula", T1_, "Fase tardia: proteína básica maior perpetua o dano", 78, "lâmina 78 (fase tardia da resposta); seção Bootcamp"),
    K(1479267436105, "A-aula", T1_, "Eosinófilo produz proteína básica maior", 80, "lâminas 80–81 (eosinófilo: lesivo ao helminto e ao tecido); seção FirstAid"),
    K(1474571606722, "A-aula", T1_, "Histamina aumenta o muco nasal e brônquico", 85, "lâmina 85 (muco); seção Bootcamp"),
    K(1473628137176, "R-detalhe", T1_, "Asma crônica: hipertrofia do músculo liso brônquico", 86, "lâmina 86 (muco, membrana basal e músculo liso); seção Bootcamp"),
    K(1473628097990, "A-aula", T1_, "Th2 secreta IL-4, que leva à troca para IgE", 87, "lâmina 87 (Th2: IL-4 e IgE)"),
    K(1473628101206, "A-aula", T1_, "Th2 secreta IL-5, que atrai eosinófilos", 87, "lâmina 87 (IL-5 e eosinófilo); seção Bootcamp"),
    K(1487117266817, "A-aula", T1_, "IgE ajuda a imunidade a vermes ativando eosinófilos", 89, "lâminas 88–89 (pacote Th2 contra helmintos)"),
    # Tipo II (lâminas 3–13)
    K(1487207102783, "V-pilar", T2_, "Tipo II: anticorpos contra antígenos de superfície celular", 3, "lâmina 3; seção FirstAid"),
    K(1487207122541, "A-aula", T2_, "Tipo II: mediado por IgM e IgG", 3, "lâmina 3; seção FirstAid"),
    K(1487207105743, "V-pilar", T2_, "Tipo II destrói a célula por opsonização", 3, "lâmina 3 (célula-alvo marcada por anticorpo); seção FirstAid"),
    K(1487117328797, "A-aula", T2_, "ADCC: IgG liga a NK por CD16", 3, "lâmina 3 (célula com receptor para Fc); seção Bootcamp"),
    K(1487207119666, "A-aula", T2_, "Tipo II causa inflamação por complemento", 3, "lâmina 3 (ativação do complemento); seção FirstAid"),
    K(1487207112553, "V-pilar", T2_, "Tipo II causa disfunção: bloqueio ou ativação de receptor", 3, "lâminas 3 e 10 (bloqueio da molécula e doença de Graves); seção FirstAid"),
    K(1462038209306, "A-aula", T2_, "Graves: anticorpo estimula o receptor de TSH", 10, "lâmina 10 (o anticorpo mimetiza o TSH em vez de bloquear)"),
    K(1489972384117, "A-aula", T2_, "Reação transfusional aguda: anticorpo do receptor contra ABO do doador", 12, "lâmina 12 (grupos ABO e reações transfusionais)"),
    K(1516062859864, "A-aula", T2_, "Doença hemolítica Rh não ocorre na primeira gravidez", 13, "lâmina 13 (eritroblastose: o contato ocorre no parto)"),
    K(1516062099732, "A-aula", T2_, "Primeiro parto Rh+ em mãe Rh−: ela forma anticorpos anti-Rh", 13, "lâmina 13 (sensibilização da mãe no parto)"),
    # Tipo III (lâminas 14–26)
    K(1487207162179, "V-pilar", T3_, "Tipo III: imunocomplexos circulantes", 14, "lâmina 14; seção FirstAid"),
    au("au-liga-ii-iii", "Type II targets antigen on the {{c1::cell}}, while type III forms complexes with {{c2::soluble}} antigen",
       "A-aula", T3_, "Conexão: tipo II (antígeno fixo) e tipo III (antígeno solúvel)", 14, "lâmina 14 e transcrição (II: estrutura da célula; III: antígeno solúvel em grande quantidade)",
       extra="- Both use IgG or IgM<br>- That is why in III the damage depends on where the complexes deposit"),
    K(1487207167794, "V-pilar", T3_, "Tipo III: imunocomplexos ativam o complemento e atraem neutrófilos", 17, "lâminas 17–18 (ação local e sistêmica de imunocomplexos); seção FirstAid"),
    K(1487207194698, "A-aula", T3_, "Reação de Arthus: tipo III local", 17, "lâmina 17 (ação local de imunocomplexos); seção FirstAid"),
    au("au-soro", ORG("<b>Serum sickness</b>:<br>- antibodies against {{c1::horse}} serum proteins<br>- complexes peak at {{c2::equivalence}}<br>- complexes deposit in {{c3::vessel}} walls"),
       "A-aula", T3_, "Doença do soro: do soro heterólogo ao depósito de imunocomplexos", 19, "lâminas 19–21; transcrição (soro antiveneno de cavalo, ponto de equivalência)",
       extra="- The foreign serum protein is slowly cleared while antibodies rise<br>- At equivalence the soluble complexes are largest and deposit"),
    # Tipo IV (lâminas 27–43)
    K(1487207218837, "V-pilar", T4_, "Tipo IV: mediado por células T", 27, "lâmina 27; seção FirstAid"),
    au("au-liga-iv", "Types I to III need {{c1::antibodies}}, but type IV is mediated by {{c2::T cells}}",
       "A-aula", T4_, "Conexão: do anticorpo ao linfócito T", 27, "lâmina 27 e transcrição (o tipo IV não é mediado por anticorpo)",
       extra="- CD4 or CD8 T cells are involved<br>- That is why the reaction is delayed"),
    K(1487207229813, "A-aula", T4_, "Tipo IV tardio: CD4 (DTH)", 27, "lâmina 27 (CD4); seção FirstAid"),
    K(1487207238825, "A-aula", T4_, "Dermatite de contato alérgica: tipo IV, não tipo I", 28, "lâminas 28–32 (muita gente chama de alergia, mas é mediada por T); seção FirstAid"),
    au("au-dth-fases", ORG("<b>Delayed hypersensitivity</b>:<br>- sensitization: dendritic cells prime {{c1::naive T}} cells<br>- re-exposure: {{c2::Th1}} cells release IFN-γ<br>- IFN-γ activates {{c3::macrophages}}, which damage tissue"),
       "A-aula", T4_, "Hipersensibilidade tardia: da sensibilização ao dano", 29, "lâminas 29–31; transcrição (T produz citocinas que ativam macrófago: eixo T-macrófago)",
       extra="- The reaction takes about 48 h to peak because T cells and macrophages must be recruited<br>- CD8 T cells can instead kill the target directly"),
    K(1487116928027, "V-pilar", T4_, "Th1 ativa macrófagos e T citotóxicos", 29, "lâminas 29–31 (eixo T-macrófago); seção Bootcamp"),
    K(1489970364081, "A-aula", T4_, "IFN-γ é o sinal que ativa o macrófago", 29, "lâminas 29–31 (macrófago ativado causa a lesão)"),
    K(1487643795892, "A-aula", T4_, "Granuloma: Th1 e IFN-γ transformam macrófagos em epitelioides", 37, "lâminas 36–38 (granuloma quando o T não elimina a micobactéria); seção Bootcamp"),
    au("au-tempo", ORG("<b>Skin reaction time</b>:<br>- type I: {{c1::minutes}}<br>- type III: {{c2::hours}}<br>- type IV: about {{c3::48 h}}"),
       "A-aula", T4_, "Tempo da reação cutânea por tipo", 41, "lâminas 41–42 (aspecto das três reações); transcrição (imediata, 5–12 h e 48 h)",
       extra="- Type I uses pre-formed IgE on mast cells<br>- Type III needs immune complexes and complement to recruit neutrophils<br>- Type IV needs T cells and macrophages to arrive"),
    K(1487207242473, "A-aula", T4_, "Teste do PPD: tipo IV mediado por Th1", 42, "lâmina 42 (reação ao PPD em 48 h, infiltração de T e macrófagos); seção FirstAid"),
    K(1487117293576, "A-aula", T4_, "CD8 citotóxico mata por apoptose", 43, "lâmina 43 (tipo IV por CD8, ex.: vírus da hepatite)"),
    K(1487207220752, "A-aula", T4_, "Tipo IV por citotoxicidade direta: CD8", 43, "lâmina 43; seção FirstAid"),
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

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1487207122541": "- IgE is type I; IgM and IgG act in types II and III",
 "ak1487117328797": "- The NK cell recognizes the Fc of IgG bound to the target cell",
 "ak1487207119666": "- Complement and Fc receptors bring neutrophils and macrophages, which release enzymes and oxygen radicals",
 "ak1462038209306": "- Instead of blocking the receptor, the antibody mimics TSH, so the thyroid is stimulated",
 "ak1489972384117": "- Natural anti-A and anti-B antibodies are IgM: type A people have anti-B, type B have anti-A, type O have both and type AB none",
 "ak1516062099732": "- At delivery fetal blood reaches the mother, who makes anti-Rh antibodies and memory cells",
 "ak1516062859864": "- In the second Rh+ pregnancy, maternal IgG anti-Rh crosses the placenta and attacks fetal red cells",
 "ak1487207194698": "- Preformed IgG meets the injected antigen in the skin; the complexes fix complement and neutrophils cause the damage",
 "ak1474580620228": "- IgE lasts 2-3 days in serum but weeks on the mast cell, which keeps it ready to degranulate",
 "ak1487640139590": "- Trauma and neuropeptides also degranulate mast cells, without IgE",
 "ak1473628116213": "- Leukotrienes are made from arachidonic acid after activation, so they follow the preformed histamine",
 "ak1474571636173": "- Prostaglandins and leukotrienes also contract smooth muscle: bronchoconstriction in the lung, hypermotility in the gut",
 "ak1474571606722": "- Mucus and vascular leak add to the airway obstruction",
 "ak1473628119069": "- Eosinophils arrive hours later, so the late phase keeps the inflammation going after histamine is gone",
 "ak1473628137176": "- Chronic inflammation also thickens the basement membrane and plugs the bronchi with mucus",
 "ak1487207220752": "- CD8 T cells kill the target cell directly",
 "ak1487206917325": "- Presensitized means IgE already sits on the mast cell receptors",
 "ak1474571583341": "- Histamine causes vasodilation, more permeability and smooth muscle contraction",
 "ak1487117266817": "- The Th2 package (IgE, mucus, eosinophils, smooth muscle contraction) evolved against intestinal worms",
 "ak1487207238825": "- Contact dermatitis is delayed and T-cell mediated, so it is not type I even though it is called allergy",
 "ak1487207242473": "- The lesion is hard because T cells and macrophages infiltrate; there is no increase in permeability",
 "ak1487117293576": "- In hepatitis B/C the CD8 T cells kill infected hepatocytes, which is also a type IV injury",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
exec((HERE / "exclusoes.py").read_text(encoding="utf-8")) if (HERE / "exclusoes.py").exists() else None

SEM_IMAGEM = "fato ou conjunto sem estrutura a reconhecer; as figuras da aula são fotografias clínicas e esquemas de livro"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
DUPLICACAO = {"au-gell": "IgE, imunocomplexos e células T aparecem nos cards de cada tipo; aqui é o quadro dos quatro tipos pelo mecanismo", "au-liga-ii-iii": "conexão entre os tipos II e III pelo antígeno fixo ou solúvel; os cards de cada tipo não fazem essa ponte", "au-liga-iv": "conexão do anticorpo (I a III) ao linfócito T (IV); os cards de cada tipo não fazem essa ponte", "au-tempo": "compara os tempos das três reações cutâneas, que os cards de cada tipo citam separados"}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Distinguir os quatro tipos de hipersensibilidade de Gell e Coombs pelo mecanismo imunológico e reconhecer os exemplos que a aula nomeia.",
    "centrais": [("tipos", "au-gell"), ("tipo I", "au-sensib-cadeia")],
    "exemplos": ["Graves", "doença hemolítica Rh", "asma", "dermatite de contato", "lúpus e artrite em detalhe"],
    "outras_aulas": [("autoimunidade e imunodeficiências", "51 Distúrbios do sistema imune"), ("granuloma", "47 Inflamação granulomatosa"), ("transplantes", "66 Bases imunológicas dos transplantes")],
}
FAIXAS = [[1, 2], [44, 90], [3, 13], [14, 26], [27, 43]]  # ordem em que o professor falou (transcrição): intro, tipo I, II, III, IV
_slide = lambda c: int(_re.search(r"\d+", c["evid"]).group())
CARDS.sort(key=lambda c: next((i for i, f in enumerate(FAIXAS) if f[0] <= _slide(c) <= f[1]), len(FAIXAS)) * 1000 + _slide(c))
