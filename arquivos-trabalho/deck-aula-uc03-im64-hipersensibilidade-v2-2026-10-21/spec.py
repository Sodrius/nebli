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
    "Fotografias clínicas (pele, glomérulo, pulmão, esclerose múltipla, artrite), figuras de livro e imunofluorescência (lâminas 4–8, 16, 19–26, 32–38, 50, 63–81): ilustram, não ensinam alvo.",
    "Diagnóstico (teste de Coombs, prick test, IgE específica, patch test), tratamento (adrenalina, Rhogan, corticoide) e fármacos que causam reações: clínica e farmacologia.",
    "Lúpus, artrite reumatoide, esclerose múltipla, Graves, miastenia e outros exemplos em detalhe: são das aulas de autoimunidade (51) e de patologia; aqui só a classificação por tipo.",
    "Heredabilidade da atopia e níveis de IgE em atópicos (lâminas 50–52): ilustração sem cobrança.",
]

CARDS = [
    au("au-gell", ORG("<b>Hypersensitivity types</b>:<br>- I: {{c1::IgE}}<br>- II: antibodies against {{c2::cell-surface}} or matrix antigens<br>- III: {{c3::immune complexes}}<br>- IV: {{c4::T cells}}"),
       "V-pilar", G_, "Gell e Coombs: os quatro tipos", 2, "lâminas 2 e 3; transcrição (distinção pelo processo imunológico); monitoria P3 de Imuno",
       extra="- Hypersensitivity = tissue damage mediated by the immune system<br>- Types I, II and III are antibody-mediated; type IV is cell-mediated"),
    K(1487207248593, "V-pilar", G_, "Antes de IV: tipos mediados por anticorpo são I, II e III", 2, "lâmina 2; seção FirstAid de hipersensibilidade"),
    K(1487207102783, "V-pilar", T2_, "Tipo II: anticorpos contra antígenos de superfície celular", 3, "lâmina 3; seção FirstAid"),
    K(1487207122541, "A-aula", T2_, "Tipo II: mediado por IgM e IgG", 3, "lâmina 3; seção FirstAid"),
    K(1487207105743, "V-pilar", T2_, "Tipo II destrói a célula por opsonização", 3, "lâmina 3 (anticorpos sobre a célula-alvo); seção FirstAid"),
    K(1487207112553, "V-pilar", T2_, "Tipo II causa disfunção: bloqueio ou ativação de receptor", 3, "lâmina 3 (afeta a fisiologia celular); seção FirstAid"),
    K(1487207119666, "A-aula", T2_, "Tipo II causa inflamação por complemento e fagócitos", 3, "lâmina 3; seção FirstAid"),
    K(1487117328797, "A-aula", T2_, "ADCC: IgG liga a NK por CD16", 3, "lâmina 3 (célula com receptor para Fc); seção Bootcamp"),
    K(1487207142388, "A-aula", T2_, "Trombocitopenia imune e anemia hemolítica autoimune: tipo II", 9, "lâminas 9–10 (anticorpos anti-plaqueta e anti-hemácia); seção FirstAid"),
    K(1487207145930, "A-aula", T2_, "Doença hemolítica do RN e reações transfusionais: tipo II", 9, "lâminas 9–13; seção FirstAid"),
    K(1516061921946, "A-aula", T2_, "Doença hemolítica Rh: mãe Rh− e feto Rh+", 13, "lâmina 13 (grupo Rh: eritroblastose fetal); seção Bootcamp"),
    K(1475376572176, "A-aula", T2_, "Goodpasture: tipo II (membrana basal)", 10, "lâminas 10 e 26; seção Bootcamp"),
    K(1487207160372, "A-aula", T2_, "Pênfigo: tipo II (desmossomos)", 6, "lâminas 7 e 10 (anti-desmogleína); seção FirstAid"),
    K(1487207158134, "A-aula", T2_, "Graves e miastenia gravis: tipo II com disfunção celular", 10, "lâmina 10 (receptor de TSH e de acetilcolina); seção FirstAid"),
    K(1503089762191, "R-detalhe", T2_, "Febre reumática: tipo II", 10, "lâmina 10 (Streptococcus cruza com antígenos do coração); seção FirstAid"),
    K(1501511684746, "R-detalhe", T2_, "Anemia perniciosa: tipo II", 10, "lâmina 10 (fator intrínseco); seção FirstAid"),
    K(1487207162179, "V-pilar", T3_, "Tipo III: imunocomplexos circulantes", 14, "lâmina 14; seção FirstAid"),
    K(1487207167794, "V-pilar", T3_, "Tipo III: imunocomplexos ativam o complemento e atraem neutrófilos", 17, "lâmina 17 (ação local de imunocomplexos); seção FirstAid"),
    K(1487207184256, "A-aula", T3_, "Hapteno: molécula pequena que se liga a proteína e induz resposta", 15, "lâmina 15 (doença do soro, antígenos solúveis); seção FirstAid"),
    K(1487207175248, "A-aula", T3_, "Doença do soro: anticorpos contra proteínas séricas estranhas", 19, "lâminas 15 e 19 (soro de cavalo); seção FirstAid"),
    K(1487207192567, "V-pilar", T3_, "Doença do soro: tipo III", 19, "lâmina 19; seção FirstAid"),
    K(1487207194698, "A-aula", T3_, "Reação de Arthus: tipo III local", 17, "lâminas 15, 17 e 41; seção FirstAid"),
    K(1487207216546, "A-aula", T3_, "Glomerulonefrite pós-estreptocócica: tipo III", 15, "lâmina 15; seção FirstAid"),
    K(1487815313912, "A-aula", T3_, "Lúpus: tipo III (imunocomplexos)", 22, "lâminas 22–26; seção B&B de hipersensibilidade"),
    K(1583964087768, "R-detalhe", T3_, "Artrite reumatoide: componente tipo III", 15, "lâmina 15 (componente tipo III)"),
    K(1474132602716, "R-detalhe", T3_, "Poliarterite nodosa: tipo III", 15, "lâmina 15 (hepatite B e outras viroses)"),
    K(1487207218837, "V-pilar", T4_, "Tipo IV: mediado por células T", 27, "lâmina 27; seção FirstAid"),
    K(1487207220752, "A-aula", T4_, "Tipo IV por citotoxicidade direta: CD8", 27, "lâmina 43 (mediada por CD8, hepatite); seção FirstAid"),
    K(1487207229813, "A-aula", T4_, "Tipo IV tardio: CD4 (DTH)", 27, "lâmina 27; seção FirstAid"),
    K(1487207238825, "A-aula", T4_, "Dermatite de contato alérgica: tipo IV", 28, "lâminas 28–32; seção FirstAid"),
    K(1487207242473, "A-aula", T4_, "Teste do PPD: tipo IV mediado por Th1", 41, "lâmina 43 (reação tuberculínica); seção FirstAid"),
    K(1462326990404, "A-aula", T4_, "Diabetes tipo 1: tipo IV por citotoxicidade", 28, "lâmina 28 (IDDM); seção FirstAid"),
    K(1487115889320, "A-aula", T4_, "MHC I apresenta antígenos endógenos ao CD8", 43, "lâmina 43 (CD8 citotóxico)"),
    K(1487116831797, "A-aula", T4_, "MHC II apresenta antígenos exógenos ao CD4", 27, "lâmina 27 (CD4 e dermatite de contato)"),
    K(1487206917325, "V-pilar", T1_, "Tipo I: IgE ligada a mastócitos e basófilos", 43, "lâmina 44; seção FirstAid"),
    K(1487207079363, "V-pilar", T1_, "Tipo I: ligação cruzada de IgE por antígeno", 44, "lâmina 54; seção FirstAid"),
    K(1487117263860, "A-aula", T1_, "IgE faz ligação cruzada ao alérgeno", 44, "lâmina 54; seção Bootcamp"),
    K(1487207084334, "V-pilar", T1_, "Resposta imediata: histamina e triptase pré-formadas", 62, "lâmina 62 (reação imediata); seção FirstAid"),
    K(1487207091819, "V-pilar", T1_, "Resposta tardia: quimiocinas e citocinas", 71, "lâmina 71 (fase tardia); seção FirstAid"),
    au("au-sensibil", "At the <b>first contact</b> with an allergen, IgE only {{c1::sensitizes}} the mast cells, with {{c2::no}} clinical reaction",
       "A-aula", T1_, "Primeiro contato: sensibilização sem clínica", 53, "lâminas 53–54; transcrição (a clínica do primeiro contato é zero)",
       extra="- Th2 and IL-4 drive B cells to make IgE, which arms the mast cell Fc receptors<br>- The reaction appears at later contacts"),
    au("au-mediadores", ORG("<b>Mast cell mediators</b>:<br>- {{c1::histamine}}: vasodilation and permeability<br>- {{c2::prostaglandins and leukotrienes}}: smooth muscle contraction"),
       "A-aula", T1_, "Mediadores do mastócito e seus efeitos", 70, "lâminas 70 e 73; transcrição (histamina, prostaglandinas e leucotrienos)",
       extra="- In the airway: bronchoconstriction; in the gut: hypermotility<br>- Cytokines come later and promote inflammation"),
    K(1474571583341, "A-aula", T1_, "Inflamação alérgica: histamina no receptor H1", 70, "lâmina 70; seção Bootcamp"),
    au("au-th2-alergia", "In allergy, Th2 IL-4 makes {{c1::IgE}}, IL-5 recruits {{c2::eosinophils}} and IL-13 makes {{c3::mucus}}",
       "A-aula", T1_, "Th2: IL-4, IL-5 e IL-13", 87, "lâmina 87 (pacote funcional Th2); transcrição",
       extra="- The same Th2 package defends against helminths: IgE, mucus, eosinophils and smooth muscle contraction"),
    K(1473628085810, "R-detalhe", T1_, "Asma: em geral tipo I", 50, "lâminas 50 e 82–86 (asma brônquica); seção Bootcamp"),
    K(1487207094725, "A-aula", T1_, "Anafilaxia: tipo I", 50, "lâmina 50 (choque anafilático); seção FirstAid"),
    K(1500404728172, "A-aula", T2_, "IgG opsonina: fagocitose por receptor de Fc ou complemento", 3, "lâmina 3 e apostila (opsonização por Fc e complemento); seção de imunologia"),
    K(1487640151914, "A-aula", T2_, "Via clássica do complemento começa em C1, ativado por IgM ou IgG", 3, "lâmina 3 e apostila (ativação do complemento por anticorpo ligado)"),
    K(1488418525490, "A-aula", T2_, "Miastenia: autoanticorpo contra receptor de acetilcolina", 10, "lâmina 10 (disfunção por bloqueio de receptor); seção Bootcamp"),
    K(1487640222923, "A-aula", T3_, "C3b ajuda a limpar imunocomplexos", 17, "lâmina 17 e apostila (complemento e remoção de imunocomplexos)"),
    K(1487207200447, "A-aula", T3_, "Arthus: imunocomplexos na pele com edema, necrose e complemento", 17, "lâmina 17 (ação local de imunocomplexos); seção FirstAid"),
    K(1503091131993, "A-aula", T3_, "Imunocomplexos circulantes depositam no glomérulo na GNPE", 15, "lâmina 15 (glomerulonefrite pós-estreptocócica); seção B&B"),
    K(1487207190223, "A-aula", T3_, "Doença do soro: sintomas 1–2 semanas depois do antígeno", 19, "lâmina 19 (tempo para formar anticorpo e imunocomplexo); seção FirstAid"),
    K(1481335976660, "A-aula", T4_, "Células de Langerhans apresentam antígeno ao T virgem", 28, "lâminas 28–31 (sensibilização na dermatite de contato)"),
    K(1487116928027, "V-pilar", T4_, "Th1 ativa macrófagos e T citotóxicos", 29, "lâminas 29–31 (hipersensibilidade tardia); seção Bootcamp"),
    K(1489970364081, "A-aula", T4_, "IFN-γ é o sinal que ativa o macrófago", 29, "lâminas 29–31 (macrófago ativado causa a lesão tardia)"),
    K(1487117293576, "A-aula", T4_, "CD8 citotóxico mata por apoptose", 43, "lâmina 43 (citotoxicidade direta do tipo IV)"),
    K(1487117300306, "R-detalhe", T4_, "CD8 induz apoptose por Fas ligante e Fas", 43, "lâmina 43 (mecanismo da morte celular pelo T citotóxico)"),
    K(1487643795892, "A-aula", T4_, "Granuloma: Th1 e IFN-γ transformam macrófagos em epitelioides", 36, "lâminas 36–38 (granuloma da hipersensibilidade tardia crônica); seção Bootcamp"),
    K(1487116878738, "V-pilar", T1_, "Th2 promove a produção de IgE", 55, "lâmina 55 (como a IgE é produzida); seção Bootcamp"),
    K(1487117161213, "V-pilar", T1_, "IL-4 e IL-13 promovem a troca de classe para IgE", 55, "lâmina 55 e transcrição (troca de classe do B pela IL-4)"),
    K(1474580620228, "V-pilar", T1_, "IgE se liga ao receptor de alta afinidade FcεRI do mastócito", 60, "lâmina 60 (FcεRI); seção Bootcamp"),
    K(1487640136892, "V-pilar", T1_, "Ligação cruzada de IgE agrega FcεRI e inicia a degranulação", 62, "lâmina 62 (desencadeamento da reação); seção B&B"),
    K(1473628107938, "A-aula", T1_, "Resposta imediata: mastócito libera histamina pré-formada", 66, "lâmina 66 (reação imediata); seção Bootcamp"),
    K(1473628116213, "A-aula", T1_, "Mastócito gera os leucotrienos C4, D4 e E4", 68, "lâmina 68 (mediadores lipídicos); seção Bootcamp"),
    K(1474571630796, "A-aula", T1_, "Histamina aumenta a permeabilidade vascular", 70, "lâmina 70 (vasodilatação e aumento de permeabilidade); seção Bootcamp"),
    K(1474571606722, "A-aula", T1_, "Histamina aumenta o muco nasal e brônquico", 70, "lâmina 70 e 85 (muco); seção Bootcamp"),
    K(1474571636173, "A-aula", T1_, "Histamina contrai o músculo liso brônquico", 70, "lâminas 70 e 86 (broncoconstrição); seção Bootcamp"),
    K(1473628097990, "A-aula", T1_, "Th2 secreta IL-4, que leva à troca para IgE", 87, "lâmina 87 (Th2 e IgE)"),
    K(1473628101206, "A-aula", T1_, "Th2 secreta IL-5, que atrai eosinófilos", 87, "lâminas 80 e 87 (eosinófilos na fase tardia); seção Bootcamp"),
    K(1479267436105, "A-aula", T1_, "Eosinófilo produz proteína básica maior", 80, "lâminas 80–81 (eosinófilo e lesão epitelial); seção FirstAid"),
    K(1473628119069, "A-aula", T1_, "Fase tardia: proteína básica maior perpetua o dano", 78, "lâmina 78 (fase tardia da resposta); seção Bootcamp"),
    au("au-dth-fases", ORG("<b>Delayed hypersensitivity</b>:<br>- sensitization: dendritic cells prime {{c1::naive T}} cells<br>- re-exposure: {{c2::Th1}} cells release IFN-γ<br>- IFN-γ activates {{c3::macrophages}}, which damage tissue"),
       "A-aula", T4_, "Hipersensibilidade tardia: da sensibilização ao dano", 29, "lâminas 29–31; transcrição (Th1, IFN-γ e macrófago)",
       extra="- The reaction takes about 48 h to peak because T cells and macrophages must be recruited<br>- CD8 T cells can instead kill the target directly"),
    au("au-tempo", ORG("<b>Skin reaction time</b>:<br>- type I: {{c1::minutes}}<br>- type III: {{c2::hours}}<br>- type IV: about {{c3::48 h}}"),
       "A-aula", G_, "Tempo da reação cutânea por tipo", 41, "lâminas 41–42 (aspecto das três reações); transcrição (imediata, 5–12 h e 48 h)",
       extra="- Type I uses pre-formed IgE on mast cells<br>- Type III needs immune complexes and complement to recruit neutrophils<br>- Type IV needs T cells and macrophages to arrive"),
    au("au-liga-ii-iii", "Type II targets antigen on the {{c1::cell}}, while type III forms complexes with {{c2::soluble}} antigen",
       "A-aula", T3_, "Conexão: tipo II (antígeno fixo) e tipo III (antígeno solúvel)", 14, "lâmina 14 e transcrição (diferença entre II e III pelo antígeno)",
       extra="- Both use IgG or IgM and complement<br>- That is why the damage in III depends on where the complexes deposit"),
    au("au-liga-iv", "Types I to III need {{c1::antibodies}}, but type IV is mediated by {{c2::T cells}}",
       "A-aula", T4_, "Conexão: do anticorpo ao linfócito T", 27, "lâmina 27 e transcrição (tipo IV não depende de anticorpo)",
       extra="- That is why the reaction is delayed: T cells and macrophages must arrive and be activated"),
    au("au-liga-i", "In type I, {{c1::IgE}} arms the {{c2::mast cell}} at first contact, so the reaction starts at the second",
       "A-aula", T1_, "Conexão: o tipo I fecha a história (IgE no mastócito)", 43, "lâmina 43 e transcrição (primeiro contato só sensibiliza)",
       extra="- Unlike II and III, no antibody has to be made after the second contact<br>- That explains the speed of minutes"),
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
 "ak1487207200447": "- Preformed IgG meets the injected antigen in the skin; the complexes fix complement and neutrophils cause the necrosis",
 "ak1473628107938": "- Histamine acts within minutes: vasodilation, permeability and bronchoconstriction",
 "ak1473628116213": "- Leukotrienes are made from arachidonic acid after activation, so they follow the preformed histamine",
 "ak1474571606722": "- Mucus and vascular leak add to the airway obstruction in asthma and the runny nose in rhinitis",
 "ak1474571636173": "- Smooth muscle contraction narrows the airway within minutes",
 "ak1473628119069": "- Eosinophils arrive hours later, so the late phase keeps the inflammation going after histamine is gone",
 "ak1487207122541": "- IgE is type I; IgM and IgG act in types II and III",
 "ak1487207160372": "- The antibodies block desmoglein, which holds epidermal cells together",
 "ak1487207142388": "- Antibodies against platelets or red cells mark them for removal",
 "ak1487207145930": "- Antibodies against Rh or ABO antigens destroy the red cells",
 "ak1487207158134": "- The antibodies bind the TSH receptor or the acetylcholine receptor and change its function",
 "ak1474132602716": "- Immune complexes deposit in medium-sized vessel walls and cause vasculitis",
 "ak1487207220752": "- CD8 T cells kill the target cell directly",
 "ak1462326990404": "- CD8 T cells destroy the insulin-producing beta cells",
 "ak1487206917325": "- Presensitized means IgE already sits on the mast cell receptors",
 "ak1473628085810": "- Allergic asthma shows an early bronchoconstriction and a late inflammatory phase",
 "ak1474571583341": "- Histamine causes vasodilation, more permeability and smooth muscle contraction",
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
DUPLICACAO = {"au-liga-i": "au-sensibil diz que o primeiro contato não dá clínica; este fecha a história da classificação ligando IgE, mastócito e segundo contato", "au-mediadores": "histamina, leucotrienos e proteína básica têm cards próprios; aqui o organizador junta os três mediadores com o efeito de cada um", "au-th2-alergia": "IL-4 e IL-5 têm cards próprios; aqui o organizador junta IL-4, IL-5 e IL-13 (muco), que o AnKing traz separadas", "au-gell": "IgE, imunocomplexos e células T aparecem nos cards de cada tipo; aqui é o quadro dos quatro tipos pelo mecanismo"}
for _k, _v in DUPLICACAO.items():
    _c = next((c for c in CARDS if c["key"] == _k), None)
    if _c:
        _c["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
    "objetivo": "Distinguir os quatro tipos de hipersensibilidade de Gell e Coombs pelo mecanismo imunológico e reconhecer os exemplos que a aula nomeia.",
    "centrais": [("tipos", "au-gell"), ("tipo I", "au-sensibil", "au-mediadores", "au-th2-alergia")],
    "exemplos": ["fotografias clínicas", "heredabilidade da atopia", "lúpus e artrite em detalhe"],
    "outras_aulas": [("autoimunidade e imunodeficiências", "51 Distúrbios do sistema imune"), ("granuloma", "47 Inflamação granulomatosa"), ("transplantes", "66 Bases imunológicas dos transplantes")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
