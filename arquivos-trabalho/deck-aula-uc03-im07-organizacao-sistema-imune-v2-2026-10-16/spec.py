# Especificação curada — Organização e funcionamento do sistema imune (UC03 P1, Imunologia; Barbuto; 26 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → cópias NEBLI vivas das aulas 45, 49, 38, 08, 51, 20 e UC08 por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
# Nunca associar 1791667093238 (nota aberta no navegador de Davi em 16/10; ver MEMORY: não tocar a nota em tela).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06: todo AnKing do conteúdo entra (só notas do baralho AnKing; cópias NEBLI por sh)
    "_FirstAid_02_Immunology_01_Lymphoid_01_Immune_system_organs.txt",
    "_FirstAid_02_Immunology_01_Lymphoid_02_Lymph_node.txt",
    "_FirstAid_02_Immunology_01_Lymphoid_04_Spleen_White_Pulp.txt",
    "_FirstAid_02_Immunology_01_Lymphoid_04_Spleen_Marginal_Zone.txt",
    "_FirstAid_02_Immunology_01_Lymphoid_04_Spleen_Red_Pulp.txt",
    "_FirstAid_02_Immunology_01_Lymphoid_05_Thymus_Histology.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"  # F-20261015-CLAUDE-06: liga os gates duros (cobertura_anking, cores_rubrica, inducao_clozes); não remover
RUN_ID = "uc03-im07-20261016a"
SHORT = "im07n"
LESSON = "2026-uc03-imunologia-07-organizacao-sistema-imune"
DECK = "NEBLI::UC03::P1::Imunologia::Organização do sistema imune"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 16/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (FirstAid estruturas linfoides: órgãos, linfonodo, baço, timo; busca/secoes); "
         "palavra-chave em AnKing e Referências Externas (busca/anking.txt: primários, secundários, seleção, HEV, linfonodo, baço, células M, "
         "dendríticas, adesão, quimiocinas, inata, plasmócitos, asplenia, janela); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1486945128758, "seção órgãos: timo matura T — entra a cópia NEBLI viva da aula 45 (sh-1791625422783)"),
 (1540066474869, "seção órgãos: B naive vai ao secundário — entra a cópia NEBLI da aula 49 (sh-1791629588022)"),
 (1519267270847, "seção órgãos: anel de Waldeyer e linfoma não Hodgkin — linfomas são de outra UC"),
 (1486945164044, "seção linfonodo: folículo secundário com centro germinativo — entra a cópia NEBLI (sh-1791625425757)"),
 (1486945178237, "seção linfonodo: HEV no paracórtex — entra a cópia NEBLI (sh-1791625425583)"),
 (1486945186009, "seção linfonodo: paracórtex na DiGeorge — entra a cópia NEBLI da aula 51 (sh-1792166984740)"),
 (1700925803760, "seção linfonodo: centro germinativo na resposta humoral — entra a cópia NEBLI da aula 49 (sh-1791629593848)"),
 (1481335266202, "seção linfonodo: histiócitos sinusais drenando câncer — patologia de linfonodo, fora do recorte"),
 (1486952739648, "seleção negativa na medula — entra a cópia NEBLI (sh-1791625423808)"),
 (1486952720521, "seleção positiva no córtex — entra a cópia NEBLI (sh-1791625423407)"),
 (1479267468509, "DC como elo inato-adaptativo — entra a cópia NEBLI (sh-1791625422291)"),
 (1486831448616, "células M na placa de Peyer — entra a cópia NEBLI da UC08 (sh-1790980915172)"),
 (1487642586907, "selectinas e sialil-Lewis X — entra a cópia NEBLI da aula 38 (sh-1791780357418)"),
 (1487642625895, "LAD1 por CD18 — entra a cópia NEBLI (sh-1791743343209)"),
 (1487642652400, "quimiotáticos de neutrófilo — entra a cópia NEBLI da aula 38 (sh-1791780359733)"),
 (1486867495023, "macrófagos e monócitos são inatos: classificação de células é da aula 08"),
 (1486867499358, "neutrófilos e DC são inatos: aula 08"),
 (1486867503989, "NK é inata: aula 08"),
 (1486867644687, "barreiras fisiológicas (temperatura, pH): aula 08 (barreiras); aqui basta a barreira física"),
 (1486867649389, "barreiras químicas (lisozima, defensinas): aula 08"),
 (1486952361607, "anatomia do timo no mediastino: anatomia, fora da aula"),
 (1486952585000, "timoma e miastenia: patologia do timo, fora da aula"),
 (1486952730716, "AIRE no timo — entra a cópia NEBLI da aula 45 (sh-1791625423932)"),
 (1486831451445, "Peyer → plasmócitos de IgA — entra a cópia NEBLI da UC08 (sh-1790980915277)"),
 (1481335802501, "mieloma múltiplo: patologia hematológica; a aula só o cita como exemplo, que fica no verso de ak-plasmocito-mo"),
]
FORA_DO_RECORTE = [
 "Fagocitose e citotoxicidade (lâminas 7–8): ilustração; aulas 08, 22 e 38.",
 "Apresentação de antígeno por MHC I e II em detalhe: aula 20.",
 "Cadeias de linfonodos por região (seção FirstAid): anatomia.",
 "Esplenectomia (corpúsculos de Howell-Jolly, plaquetas) e anatomia do baço: fora; ficam só encapsulados e IgM (baço filtra o sangue).",
 "Nomes das quimiocinas e receptores em detalhe (CXCR5, CCR7): o professor pede só a ideia nesta aula (objetivos em cinza).",
]
A_, B_, C_, D_, E_, F_, G_ = ("A-inata-adaptativa", "B-primarios-selecao", "C-recirculacao", "D-apc", "E-linfonodo", "F-baco-malt", "G-adesao-quimiocinas")
_CHAVE_TABELA = "- Innate: fast, nonspecific, no memory · Adaptive: slow (days), specific, diverse, with memory"

CARDS = [
 # ---------- A. Inata × adaptativa (lâminas 4–9) ----------
 ak("ak-inata-barreiras", 1486867633025, "A-step", A_, "Barreiras físicas são inatas", 4, "lâminas 4 e 6 (barreiras anatômicas, funcionais, biológicas)"),
 ak("ak-adaptativa-especifica", 1486867612235, "V-prova", A_, "Adaptativa é altamente específica", 5, "lâmina 5 (repertório clonal); prova 2024 P1 2.11 (diferença inata × adquirida)", extra_add=_CHAVE_TABELA),
 ak("ak-adaptativa-diversa", 1486867628723, "A-step", A_, "Adaptativa tem diversidade extensa", 5, "lâmina 5 (repertório completo)"),
 ak("ak-inata-inespecifica", 1486867513384, "A-step", A_, "Inata é inespecífica", 5, "par de ak-adaptativa-especifica"),
 ak("ak-inata-diversidade", 1486867606359, "R-detalhe", A_, "Inata tem diversidade limitada", 5, "par de ak-adaptativa-diversa"),
 sh(1791780352647, "azul", A_, "Macrófagos e mastócitos são sentinelas", 6, "lâmina 6 (células residentes que dão o alarme); card da 38"),
 sh(1791743342260, "rosa", A_, "Mastócito ativado por trauma", 6, "lâmina 6 e transcrição (mastócito explode e alarma); card da 08"),
 sh(1791743340457, "azul", A_, "Tecido necrótico libera DAMPs", 6, "lâmina 6 (células do tecido → DAMPs); card da 08"),
 sh(1791780358855, "rosa", A_, "ICAM-1 e VCAM-1 induzidas por TNF e IL-1", 6, "lâmina 6 (endotélio → moléculas de adesão); card da 38"),
 ak("ak-inata-rapida", 1486867532110, "A-step", A_, "Inata age em minutos a horas", 9, "lâmina 9 e transcrição (inata primeiro; adquirida em paralelo)"),
 ak("ak-adaptativa-lenta", 1486867623104, "A-step", A_, "Adaptativa demora mais", 9, "transcrição (expansão clonal leva cerca de 2 semanas)"),
 ak("ak-inata-memoria", 1486867518070, "V-prova", A_, "Inata não tem memória", 9, "prova 2024 P1 2.11"),
 ak("ak-adaptativa-memoria", 1486867618953, "V-prova", A_, "Adaptativa tem memória", 9, "prova 2024 P1 2.11; transcrição (ideia da vacina)"),
 # ---------- B. Primários e seleção (lâminas 10–11) ----------
 sh(1791625423407, "verde", B_, "Seleção positiva no córtex do timo", 10, "lâmina 10 (1º interação com APC); prova 2015 P2sub 6.1; card da 45"),
 sh(1791625423808, "verde", B_, "Seleção negativa na medula do timo", 10, "lâmina 10 (2º autorreatividade → deleção clonal); prova 2015 P2sub 6.1; card da 45"),
 sh(1791625423683, "azul", B_, "Seleção negativa: alta afinidade pelo próprio", 10, "lâmina 10; card da 20"),
 sh(1791625423932, "azul", B_, "AIRE expressa autoantígenos de tecidos no timo", 10, "lâmina 10 (deleção clonal); palavras-cruzadas da turma (19: AIRE); card da 45"),
 sh(1792166970267, "azul", B_, "Tolerância central × periférica", 10, "lâmina 10 (desvio para Treg); prova 2025 P3 4.1; card da 51"),
 ak("ak-timo-cortex", 1486952572343, "A-step", B_, "Córtex do timo: denso, T imaturos", 10, "seção FirstAid timo; lâmina 10"),
 ak("ak-timo-medula", 1486952576797, "A-step", B_, "Medula do timo: clara, T maduros e Hassall", 10, "seção FirstAid timo"),
 ak("ak-hassall", 1486952580934, "R-detalhe", B_, "Corpúsculos de Hassall", 10, "seção FirstAid timo"),
 ak("ak-mo-producao", 1486945122632, "V-pilar", B_, "Medula óssea produz as células imunes", 11, "lâmina 11 (primários); seção FirstAid órgãos"),
 ak("ak-mo-b", 1486945125504, "V-pilar", B_, "Medula óssea matura o linfócito B", 11, "lâmina 11 (medula óssea → B); palavras-cruzadas (13)"),
 sh(1791625422783, "verde", B_, "Timo matura o linfócito T", 11, "lâmina 11 (timo → T); card da 45"),
 ak("ak-secundarios", 1486945131833, "V-pilar", B_, "Secundários: onde o linfócito encontra o antígeno", 11, "lâminas 11, 17 e 25; seção FirstAid órgãos",
    extra_add="- Lymph nodes, spleen and mucosal tissue (Peyer patches, appendix, tonsils of Waldeyer's ring)"),
 sh(1791629588022, "azul", B_, "B naive vai aos secundários", 11, "lâmina 11; card da 49"),
 sh(1791023357519, "azul", B_, "MALT", 11, "lâmina 11 (Peyer, apêndice, Waldeyer = MALT); palavras-cruzadas (BALT); card da UC08"),
 sh(1790980914855, "rosa", B_, "Placas de Peyer no íleo", 11, "lâmina 11; card da UC08"),
 # ---------- C. Recirculação e tolerância (lâminas 12–16) ----------
 sh(1791716419826, "azul", C_, "T naive é ativado no linfonodo drenante", 12, "lâmina 12; card da 47"),
 sh(1791625425583, "verde", C_, "HEV no paracórtex", 13, "lâmina 13 e transcrição (vênulas de endotélio alto); card da 07 antiga/45"),
 sh(1791577165815, "rosa", C_, "Linfa volta ao sangue pelo ducto torácico", 13, "lâmina 13 (linfa → sangue); card da 23"),
 sh(1791625425207, "verde", C_, "Naive recircula; efetor vai ao tecido", 13, "lâminas 13–14 e transcrição (ativado muda moléculas de adesão e não volta); card da 45"),
 au("au-tolerancia", "Antigen carried from an uninjured <b>tissue</b> to lymphoid organs tends to induce {{c1::tolerance}} rather than an effector response",
    "V-pilar", C_, "Sem lesão, tolerância", 16, "lâminas 16 e 24 (resposta × tolerância); objetivo 3; transcrição (sem lesão, a informação tende a gerar tolerância)",
    extra="- With tissue damage, the molecular landscape (DAMPs, cytokines) pushes toward an effector response<br>- Both happen together; the balance decides what we see"),
 sh(1791629597796, "azul", C_, "Resposta secundária: latência menor, pico maior", 16, "transcrição (vacina: produtos da resposta adquirida já presentes no alarme); card da 49"),
 # ---------- D. APC (lâminas 17–18) ----------
 sh(1791625426408, "verde", D_, "DC: a APC que ativa o T naive", 18, "lâmina 18 (capacidade única de ativar T naive); card da 45"),
 sh(1791625422291, "azul", D_, "DC: elo entre inata e adaptativa", 18, "lâmina 18 (direcionamento da resposta); card da 45"),
 sh(1791625427531, "verde", D_, "Apresentação cruzada", 18, "lâmina 18; transcrição (exemplo do HBV); prova 2018 P1 1.11; card da 20"),
 au("au-b-apc", "B cells capture scarce antigen through surface {{c1::immunoglobulin}}, then present it to <b>helper T cells</b> that see the same antigen",
    "A-aula", D_, "Linfócito B como APC seletiva", 18, "lâmina 18 (apresentação seletiva → resposta humoral); transcrição (afinidade 10 mil vezes maior)",
    extra="- Unlike dendritic cells and macrophages, B cells do not phagocytose<br>- This coupling makes antibody production depend on T cells"),
 sh(1791629593971, "azul", D_, "T auxiliar e B se encontram na borda do folículo", 18, "lâmina 18 (conversa B–T); card da 49"),
 # ---------- E. Aferência e linfonodo (lâminas 19–21) ----------
 ak("ak-aferente", 1486945137995, "A-aula", E_, "Antígeno chega ao linfonodo pela linfa aferente", 19, "lâmina 19 (drenagem linfática traz a informação)"),
 ak("ak-foliculos", 1486945149721, "A-step", E_, "Folículos no córtex externo", 20, "lâmina 20; seção FirstAid linfonodo"),
 ak("ak-foliculo-b", 1486945155220, "V-pilar", E_, "B ficam e proliferam nos folículos", 20, "lâmina 20 (áreas timo-independentes)"),
 ak("ak-foliculo-primario", 1486945159596, "A-step", E_, "Folículo primário: denso e quiescente", 20, "seção FirstAid linfonodo"),
 sh(1791625425757, "azul", E_, "Folículo secundário com centro germinativo", 20, "lâmina 20 (centro germinativo = expansão de B); card da 07 antiga"),
 ak("ak-paracortex", 1486945168998, "V-pilar", E_, "Paracórtex entre folículos e medula", 20, "lâmina 20 (área timo-dependente do linfonodo)"),
 ak("ak-paracortex-viral", 1486945189088, "V-prova", E_, "Paracórtex cresce na resposta celular (vírus)", 20, "lâmina 20 (predomínio T × B); provas 2023 P2 2.3 e 2019 P1 3.3"),
 sh(1791629593848, "verde", E_, "Centro germinativo cresce na resposta humoral", 20, "lâmina 20; card da 49"),
 sh(1792166984740, "rosa", E_, "Paracórtex pouco desenvolvido na DiGeorge", 20, "lâmina 20 (área timo-dependente esvazia sem timo); card da 51"),
 ak("ak-hiperplasia-folicular", 1481335246915, "A-step", E_, "Hiperplasia folicular (B)", 20, "transcrição (predomínio de expansão B); seção FirstAid linfonodo"),
 ak("ak-hiperplasia-paracortical", 1481335256235, "A-step", E_, "Hiperplasia paracortical (T)", 20, "transcrição (predomínio de expansão T); prova 2023 P2 2.3"),
 sh(1791629594223, "azul", E_, "FDC guarda antígeno intacto e sustenta memória", 20, "lâmina 20 e transcrição (FDC não apresenta a T; depósito de liberação lenta); card da 49"),
 ak("ak-medula-ln", 1486945192340, "A-step", E_, "Medula do linfonodo: cordões e seios", 21, "lâmina 21; seção FirstAid linfonodo"),
 ak("ak-seios-eferente", 1486945196492, "A-aula", E_, "Seios medulares → linfa eferente", 21, "transcrição (o linfócito sai do linfonodo pela linfa)"),
 ak("ak-seios-macrofagos", 1486945200481, "R-detalhe", E_, "Seios medulares têm macrófagos", 21, "seção FirstAid linfonodo"),
 ak("ak-cordoes", 1486945204408, "A-aula", E_, "Cordões medulares têm plasmócitos", 21, "lâmina 21 (plasmócitos nos cordões medulares)"),
 # ---------- F. Baço, MALT e eferência (lâminas 19–21) ----------
 ak("ak-zona-marginal", 1486945335969, "A-step", F_, "Zona marginal do baço", 19, "lâmina 19 (baço recebe informação do sangue); seção FirstAid baço"),
 ak("ak-zona-marginal-captura", 1486945340214, "A-aula", F_, "Zona marginal capta antígenos do sangue", 19, "lâmina 19 e transcrição (resposta no baço = sinais do sangue)"),
 sh(1792083501161, "rosa", F_, "B da zona marginal: IgM T-independente", 19, "card da 49"),
 ak("ak-esplenectomia-vacina", 1486945363228, "R-detalhe", F_, "Esplenectomia: vacinar contra encapsulados", 19, "baço filtra o sangue; leitura complementar (Kruetzmann)"),
 ak("ak-baco-igm", 1486945368306, "R-detalhe", F_, "Disfunção esplênica reduz IgM", 19, "leitura complementar da lâmina 26 (memória B IgM contra pneumococo gerada no baço)"),
 sh(1790980915172, "verde", F_, "Células M na placa de Peyer", 19, "lâmina 19 (células M, transcitose); prova 2018 P3 5.6; card da UC08"),
 sh(1791780605649, "azul", F_, "DC recebe antígeno amostrado pela célula M", 19, "lâmina 19 e transcrição (DC estende prolongamentos até a luz); card da UC08"),
 sh(1790980915277, "azul", F_, "Peyer: B viram plasmócitos de IgA", 19, "prova 2018 P3 5.6 (imunidade da mucosa); card da UC08"),
 ak("ak-pals", 1486945314023, "A-step", F_, "PALS em volta das arteríolas centrais", 20, "lâmina 20 (bainha periarteriolar = área T do baço); seção FirstAid"),
 ak("ak-polpa-branca", 1486945318448, "A-step", F_, "PALS + folículos = polpa branca", 20, "seção FirstAid baço"),
 ak("ak-baco-t", 1486945322037, "V-pilar", F_, "T do baço na PALS", 20, "lâmina 20"),
 ak("ak-baco-b", 1486945327076, "A-step", F_, "B do baço nos folículos e zona marginal", 20, "lâmina 20"),
 ak("ak-polpa-vermelha", 1486945331281, "A-step", F_, "Polpa vermelha: sinusoides", 21, "lâmina 21 (plasmócitos vão à polpa vermelha); seção FirstAid"),
 ak("ak-plasmocito-mo", 1479267527440, "A-aula", F_, "Plasmócitos moram na medula óssea", 21, "lâmina 21 e transcrição (medula óssea também é secundária)",
    extra_add="- That is why plasma-cell tumors (multiple myeloma) appear in the bone marrow at many sites"),
 sh(1791625428033, "azul", F_, "T específicos atingem o pico em 1–2 semanas", 21, "transcrição (expansão clonal leva cerca de duas semanas); card da 45"),
 ak("ak-janela-hiv", 1552864862676, "R-detalhe", F_, "Antes da soroconversão, NAT do HIV", 21, "transcrição (janela imunológica e transfusão no início da AIDS)",
    extra_add="- Antibodies take weeks to reach detectable levels: the immunological window"),
 # ---------- G. Adesão e quimiocinas (lâminas 22–23) ----------
 au("au-adesao", ORG("<b>Leukocyte adhesion molecule families</b>:<br>1. {{c1::Selectins::S…}} (bind carbohydrates)<br>2. {{c1::Integrins::I…}} (β2 = CD18, e.g., LFA-1)<br>"
                      "3. {{c1::Immunoglobulin superfamily::I…}} (ICAM, VCAM, MAdCAM)<br>4. {{c1::Mucin-like::M…}} (CD34, GlyCAM-1)"),
    "R-org", G_, "Famílias de moléculas de adesão", 22, "lâmina 22 (objetivo 4, em cinza: só a ideia); transcrição (selectinas primeiro, depois integrinas)",
    extra="- Selectins slow (rolling); integrins binding ICAM/VCAM stop the cell (firm adhesion); then transmigration"),
 sh(1791780357418, "azul", G_, "Selectinas e sialil-Lewis X: rolamento", 22, "lâmina 22; card da 38"),
 sh(1791743343209, "rosa", G_, "LAD1: defeito de CD18", 22, "lâmina 22 (β2-integrinas = CD18); palavras-cruzadas (LFA-1); card da 08"),
 au("au-quimiocinas", "<b>Chemokine</b> families (CXC, CC, CX3C, XC) are named by the spacing of their N-terminal {{c1::cysteines}}",
    "R-detalhe", G_, "Famílias de quimiocinas", 23, "lâmina 23 (objetivo 5, em cinza); transcrição (as letras C são cisteínas)",
    extra="- An L marks the chemokine (CXCL8 = IL-8) and an R its receptor (CCR7)<br>- They guide cell migration toward the highest concentration"),
 sh(1791780359733, "azul", G_, "Quimiotáticos de neutrófilo: IL-8, C5a, LTB4", 23, "lâmina 23 (IL-8, C5a, leucotrienos); card da 38"),
 sh(1791780360378, "rosa", G_, "Macrófagos secretam IL-8", 23, "lâmina 23; card da 38"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "conceito de organização e fluxo sem estrutura a reconhecer em imagem; os esquemas das lâminas são desenhos do professor, não figuras reais"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM

VERSO = {  # chave: "- linha curta" para nota de acervo sem Extra útil
 "ak-aferente": "- Lymph brings dendritic cells, free antigen and tissue mediators: the molecular landscape",
 "ak-seios-eferente": "- Lymphocytes leave the node through efferent lymph, not through blood",
 "ak-inata-barreiras": "- Anatomical, functional and biological barriers are the first innate defense; injury to them triggers the alarm",
 "ak-adaptativa-diversa": "- Receptor genes are assembled somatically in each lymphocyte, so the repertoire recognizes almost anything",
 "ak-inata-inespecifica": "- Innate receptors see shared patterns (PAMPs, DAMPs), not one particular antigen",
 "ak-inata-diversidade": "- A few germline-encoded receptor types, the same in every cell of a lineage",
 "ak-inata-rapida": "- Its cells are already in the tissue and respond within minutes",
 "ak-adaptativa-lenta": "- Clonal expansion in the lymphoid organ takes about two weeks before the response is measurable",
 "ak-inata-memoria": "- A second encounter gets the same innate response",
 "ak-adaptativa-memoria": "- Memory lymphocytes make the second response faster and stronger: the basis of vaccines",
 "ak-hassall": "- They sit in the thymic medulla, where mature T cells are",
 "ak-mo-b": "- B cells finish maturing in the marrow; T precursors leave it for the thymus",
 "ak-zona-marginal-captura": "- The spleen samples blood, so it responds to blood-borne invaders",
 "ak-foliculos": "- Follicles are the B-cell, thymus-independent areas",
 "ak-foliculo-b": "- Follicular dendritic cells there hold antigen for B cells",
 "ak-paracortex": "- Thymus-dependent area: T cells and dendritic cells, with the high endothelial venules",
 "ak-paracortex-viral": "- Viral infections expand T cells, so the paracortex grows (paracortical hyperplasia)",
 "ak-baco-t": "- The PALS is the spleen's thymus-dependent area",
 "ak-medula-ln": "- Plasma cells settle in the cords; lymph leaves through the sinuses",
 "ak-polpa-vermelha": "- Plasma cells made in the white pulp migrate to the red pulp",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
IMAGENS_VISTAS = {}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (42 notas novas, 44 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Descrever órgãos linfoides primários (geração e seleção do repertório) e secundários (encontro com o antígeno), a recirculação "
             "de linfócitos naive e ativados, as APC, as áreas T e B, a eferência de plasmócitos e anticorpos, e a ideia de resposta × tolerância; "
             "conhecer as famílias de adesão e quimiocinas só em linhas gerais.",
 "centrais": [
   ("inata × adaptativa", "ak-adaptativa-especifica", "ak-inata-memoria", "ak-adaptativa-memoria"),
   ("primários e seleção", "sh-1791625423407", "sh-1791625423808", "ak-mo-producao", "ak-mo-b", "sh-1791625422783"),
   ("secundários e recirculação", "ak-secundarios", "sh-1791625425583", "sh-1791625425207", "au-tolerancia"),
   ("áreas T e B", "sh-1791625426408", "ak-foliculo-b", "ak-paracortex", "ak-baco-t"),
 ],
 "exemplos": ["DiGeorge", "mononucleose (paracórtex)", "mieloma", "HBV e apresentação cruzada", "vacina", "janela do HIV"],
 "outras_aulas": [("reconhecimento inato, DAMPs, barreiras", "08 (sh)"), ("MHC e apresentação", "20"), ("ativação T e B", "45 e 49 (sh)"),
                  ("adesão e quimiotaxia na inflamação", "37/38 (sh)")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
