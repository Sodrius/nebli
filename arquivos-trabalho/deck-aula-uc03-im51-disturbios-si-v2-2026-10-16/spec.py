# Especificação curada — 51 Distúrbios do sistema imune (UC03 P3, Imunologia; aula SEM lâminas: roteiro em fontes/roteiro-aula.md).
# Ordem = roteiro (princípio → critério → grupos → mecanismos → síndromes por cima). AnKing → externos → autoral só para lacuna provada.
# F-20261016-CLAUDE-05 (classificar, não colecionar doenças) + F-20261016-CLAUDE-06 (todo AnKing do conteúdo entra, sem limite).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4  # 3 = teto de autoral (20%; 35% com AUTORAL_EXCECAO); 4 = todo AnKing das SECOES_DA_AULA entra ou é excluído com motivo
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-im51-20261016a"
SHORT = "im51"
LESSON = "2026-uc03-imunologia-51-disturbios-sistema-imune"
DECK = "NEBLI::UC03::P3::Imunologia::Distúrbios do sistema imune"
CRITERIOS = "EXECUCAO-DECK-AULA (passos 0–7) + MEMORY §2–§8 + ANTI-EXEMPLARES + F-20261016-CLAUDE-04/05/06, 16/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (16/10): seções de recurso do AnKing (busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); "
         "significado em todos os acervos e nos decks NEBLI vivos (busca/semantica.jsonl). ")
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]

FORA_CONT = "fora do recorte da aula"
EXCLUIDOS = [
 # Maturação tímica e marcadores: aula 45 (ativação de LT) / 07; aqui só a seleção negativa (tolerância central)
 (1486952695243, "maturação de LT (CD na medula óssea): aula 45/07; aqui só a seleção negativa"),
 (1486952700865, "maturação de LT (córtex duplo-positivo): aula 45/07"),
 (1486952708867, "maturação de LT (medula simples-positiva): aula 45/07"),
 (1486952713234, "maturação de LT (diferenciação CD4/CD8): aula 45/07"),
 (1486952717741, "seleção positiva: aula 45/07 (não é mecanismo de tolerância)"),
 (1486952720521, "seleção positiva: aula 45/07"),
 (1523570028468, "clonalidade por rearranjo de TCR: diagnóstico de linfoma, outra aula"),
 (1487983941570, "HLA da rinite alérgica: alergia, aula 64"),
 # Síndromes por cima (F-20261016-CLAUDE-05): tratamento, vacina, detalhe de teste e achado clínico ficam fora
 (1487815289189, "achado clínico do IPEX (diabetes em lactente): síndrome por cima"),
 (1517365356878, "achados dermatológicos do IPEX: síndrome por cima"),
 (1487727594138, "vacina na XLA: conduta, fora do recorte"),
 (1577803381607, "teste cutâneo com Candida: diagnóstico, fora do recorte"),
 (1487727486402, "CATCH-22: achados embriológicos e clínicos da deleção 22q11, síndrome por cima"),
 (1487727486403, "mnemônico CATCH-22: achados clínicos, síndrome por cima"),
 (1487727491234, "tetania na DiGeorge: achado clínico (paratireoide)"),
 (1487727517131, "PTH baixo na DiGeorge: achado endócrino, não imune"),
 (1487727520922, "cálcio baixo na DiGeorge: achado endócrino, não imune"),
 (1527342711798, "tetralogia de Fallot: cardiologia"),
 (1487727546252, "apresentação clínica da SCID (deficit de crescimento, diarreia, monilíase): síndrome por cima"),
 (1487727549762, "tratamento da SCID: conduta"),
 (1487727555893, "vacina na SCID: conduta"),
 (1497306261171, "pegademase: tratamento"),
 (1487642687838, "albinismo no Chédiak-Higashi: achado clínico"),
 (1487642699807, "hemostasia no Chédiak-Higashi: achado clínico"),
 (1487642712472, "neuropatia no Chédiak-Higashi: achado clínico"),
 (1520301719601, "linfo-histiocitose no Chédiak-Higashi: achado clínico raro"),
 (1461794791535, "IFN-γ no tratamento da DGC: conduta"),
 (1487642751066, "DHR/NBT: teste diagnóstico da DGC"),
 (1587828670445, "leitura do teste de DHR: diagnóstico"),
 (1506190688913, "bastonetes gram-positivos catalase-positivos: microbiologia"),
 (1487642598269, "etapas do extravasamento leucocitário: aula 37/38 (inflamação)"),
 (1487642602159, "ICAM-1/VCAM-1: aula 37/38 (inflamação)"),
 (1487642614060, "CAMs e integrinas: aula 37/38 (inflamação)"),
 (1487642630321, "queda tardia do coto umbilical na LAD: achado clínico"),
 (1581895688197, "perda de dentes na LAD: achado clínico"),
]
FORA_DO_RECORTE = [
 "Hipersensibilidade tipos I–IV como classificação: aula 64 (Reações de hipersensibilidade); aqui só o mecanismo efetor das doenças autoimunes, por cima.",
 "Autoanticorpos por doença (seção FirstAid Autoantibodies) e doenças autoimunes uma a uma (artrite reumatoide, esclerodermia, Sjögren, vasculites): Davi pediu síndromes por cima.",
 "Job (STAT3), Wiskott-Aldrich, ataxia-telangiectasia, deficiência de IL-12R e candidíase mucocutânea crônica: estão no Abbas/Janeway, mas ficaram fora para não colecionar síndromes (caso de fronteira, perguntar a Davi).",
 "HIV além da entrada pelo CD4 e do critério de AIDS (ciclo, estágios, antirretrovirais, oportunistas): aulas de virologia.",
 "Tratamentos, vacinas e testes diagnósticos das imunodeficiências.",
]
A_, B_, C_, D_ = "A-tres-falhas", "B-autoimunidade", "C-imunodeficiencias", "D-autoinflamatorias"

# AnKing em lote: (nid, código, bloco, lâmina do roteiro, alvo, motivo)
AK = [
 # B. Autoimunidade
 (1486952612312, "V-pilar", B_, 6, "Tolerância central B: deleção", "Abbas pp. 180–181"),
 (1486952615115, "V-pilar", B_, 8, "Tolerância periférica T: anergia", "Abbas pp. 175–177"),
 (1487117363961, "V-pilar", B_, 8, "Anergia: definição", "Abbas p. 175"),
 (1495599255138, "A-aula", B_, 8, "PD-1 na tolerância periférica", "Abbas p. 176; prova 2024 P4"),
 (1489970994844, "A-aula", B_, 9, "Treg: CD4 e CD25", "Abbas p. 178"),
 (1520300460306, "R-detalhe", B_, 9, "Treg: citocinas", "Abbas p. 178"),
 (1487812660177, "R-detalhe", B_, 11, "CD25 polimórfico na EM e DM1", "Abbas p. 184 (polimorfismos não HLA)"),
 (1487983926461, "V-pilar", B_, 11, "HLA-B27", "Abbas Fig. 9-11"),
 (1487983915856, "R-detalhe", B_, 11, "HLA na doença de Addison", "Abbas Fig. 9-11"),
 (1487983933302, "R-detalhe", B_, 11, "HLA na doença celíaca", "Janeway 15.19"),
 (1487983947972, "R-detalhe", B_, 11, "HLA no LES", "Abbas Fig. 9-11"),
 (1487983954783, "R-detalhe", B_, 11, "HLA na síndrome de Goodpasture", "Abbas Fig. 9-11"),
 (1487983968953, "R-detalhe", B_, 11, "HLA na anemia perniciosa", "Abbas Fig. 9-11"),
 (1582315762546, "R-detalhe", B_, 11, "HLA na miastenia", "Abbas Fig. 9-11"),
 (1487815300280, "R-detalhe", B_, 11, "PTPN22", "Abbas p. 184"),
 (1487815294185, "R-detalhe", B_, 12, "Sexo feminino e autoimunidade", "Abbas p. 186"),
 (1503089543399, "V-pilar", B_, 12, "Mimetismo molecular: febre reumática", "Abbas p. 185; prova 2018 P1"),
 (1487815285101, "R-detalhe", B_, 13, "IPEX ligado ao X", "Abbas p. 178; prova 2015 P2"),
 (1487470217383, "V-prova", B_, 13, "ALPS: Fas–FasL", "Abbas p. 179; prova 2015 P2 (falhas de tolerância)"),
 (1495629799342, "V-prova", B_, 14, "Anti-PD-1 → autoimunidade endócrina", "prova 2024 P4"),
 (1462038188179, "V-pilar", B_, 16, "Graves: anticorpo estimula o receptor", "Janeway 15.15"),
 (1488418525490, "V-pilar", B_, 16, "Miastenia: anticorpo bloqueia o receptor", "Janeway 15.15"),
 (1581890934727, "V-pilar", B_, 16, "LES: imunocomplexos e complemento", "Janeway 15.16; prova 2024 P3"),
 (1487815347337, "V-prova", B_, 16, "LES: anti-dsDNA e anti-Sm", "prova 2024 P3"),
 (1487727814679, "R-detalhe", B_, 17, "Complemento precoce: infecções piogênicas", "Janeway 13.16"),
 (1487815316366, "V-prova", B_, 17, "Complemento precoce e LES", "Abbas p. 231; provas 2024 P3 e 2016 P1"),
 # C. Imunodeficiências
 (1544832356705, "A-aula", C_, 18, "Imunodeficiência primária: riscos", "Janeway 13.7"),
 (1577804124702, "A-step", C_, 18, "Imunodeficiência e linfoma", "Abbas p. 238"),
 (1539873617585, "V-pilar", C_, 19, "B → bactérias; T → fungos e vírus", "Janeway 13.7"),
 (1500404833072, "V-pilar", C_, 19, "B, anticorpo ou complemento → encapsuladas", "Janeway 13.7"),
 (1487727769430, "A-aula", C_, 19, "Deficiência B → encapsuladas", "Abbas Fig. 12-1"),
 (1487727777884, "A-aula", C_, 19, "Deficiência B → bactéria, enterovírus, Giardia", "Janeway 13.14"),
 (1487727785545, "A-aula", C_, 19, "Deficiência T → vírus e fungos", "Abbas Fig. 12-1"),
 (1487727812574, "A-aula", C_, 24, "Complemento terminal → Neisseria", "Janeway 13.16"),
 (1487727534510, "V-pilar", C_, 20, "SCID: receptor de IL-2 (γc)", "Abbas p. 226"),
 (1487727537386, "R-detalhe", C_, 20, "SCID por γc: ligada ao X", "Abbas p. 226"),
 (1476498858782, "V-pilar", C_, 20, "SCID: ADA", "Abbas p. 227"),
 (1487727526313, "A-step", C_, 20, "SCID: enzima deficiente", "Abbas p. 227"),
 (1476498854265, "R-detalhe", C_, 20, "ADA na via de recuperação de purinas", "Janeway 13.10"),
 (1476498861750, "A-step", C_, 20, "ADA: dATP tóxico", "Janeway 13.10"),
 (1487727529450, "A-step", C_, 20, "ADA: dATP tóxico para linfócitos", "Abbas p. 227"),
 (1487727532142, "R-detalhe", C_, 20, "SCID por ADA: autossômica recessiva", "Abbas p. 227"),
 (1582321770897, "A-step", C_, 20, "SCID: RAG", "Abbas p. 227; Janeway 13.11"),
 (1487727559962, "A-step", C_, 20, "SCID: TRECs baixos", "Janeway 13.9 (sem timo funcional)"),
 (1487727562925, "A-step", C_, 20, "SCID: sem sombra tímica", "Abbas p. 226"),
 (1487727566026, "A-step", C_, 20, "SCID: sem centros germinativos", "Abbas p. 227"),
 (1487727568569, "A-step", C_, 20, "SCID: sem células T", "Abbas p. 227"),
 (1487727477833, "A-step", C_, 21, "DiGeorge: 3ª e 4ª bolsas faríngeas", "Abbas p. 229"),
 (1487727483197, "A-step", C_, 21, "DiGeorge: 22q11", "Janeway 13.13"),
 (1487727508642, "A-step", C_, 21, "DiGeorge: poucas células T", "Abbas p. 229"),
 (1486945186009, "A-step", C_, 21, "DiGeorge: paracórtex pobre", "Abbas p. 229 (zona T)"),
 (1577801724794, "A-step", C_, 21, "DiGeorge: infecções intracelulares", "Janeway 13.13"),
 (1487727571098, "V-pilar", C_, 22, "XLA: BTK", "Abbas pp. 227–228"),
 (1487727578609, "R-detalhe", C_, 22, "BTK é tirosina-cinase", "Abbas p. 228"),
 (1487727581060, "R-detalhe", C_, 22, "XLA: ligada ao X", "Abbas p. 228"),
 (1487727583313, "A-step", C_, 22, "XLA: sem células B no sangue", "Abbas p. 228"),
 (1487727589236, "A-step", C_, 22, "XLA: todas as classes de Ig baixas", "Abbas p. 228"),
 (1487727591641, "A-step", C_, 22, "XLA e SCID: linfonodos e tonsilas escassos", "Abbas Fig. 12-3"),
 (1487727596629, "A-step", C_, 22, "XLA: começa aos 6 meses", "Janeway 13.14 (IgG materna)"),
 (1487727603426, "A-step", C_, 22, "XLA: sem maturação B", "Abbas p. 228"),
 (1577803662725, "A-step", C_, 22, "XLA: encapsuladas e enterovírus", "Janeway 13.14"),
 (1487727606729, "A-step", C_, 22, "CVID: sem plasmócitos", "Abbas p. 229"),
 (1487727609159, "R-detalhe", C_, 22, "CVID: começa após a puberdade", "Janeway 13.15"),
 (1487727615686, "A-step", C_, 22, "CVID: Ig baixa por falta de plasmócitos", "Abbas p. 229"),
 (1487727618491, "R-detalhe", C_, 22, "CVID: autoimunidade e linfoma", "Abbas p. 230"),
 (1487727624742, "A-aula", C_, 22, "Deficiência de IgA: a primária mais comum", "Abbas p. 229; Janeway 13.7"),
 (1487727627992, "R-detalhe", C_, 22, "Deficiência de IgA: IgG e IgM normais", "Janeway 13.15"),
 (1487727631557, "R-detalhe", C_, 22, "Deficiência de IgA: anafilaxia a hemoderivado", "Janeway 13.15"),
 (1487121978005, "R-detalhe", C_, 22, "Imunização passiva na deficiência de IgA", "Janeway 13.15"),
 (1487727634083, "R-detalhe", C_, 22, "Deficiência de IgA: infecções de mucosa", "Janeway 13.15"),
 (1487727647861, "A-step", C_, 22, "Hiper-IgM: sem troca de classe", "Abbas p. 229"),
 (1487727650568, "A-step", C_, 22, "Hiper-IgM: IgA, IgG e IgE baixas", "Abbas p. 229"),
 (1487727658056, "R-detalhe", C_, 22, "Hiper-IgM: ligada ao X", "Abbas p. 229"),
 (1487727660381, "R-detalhe", C_, 22, "Hiper-IgM: infecções piogênicas", "Janeway 13.15"),
 (1487727666057, "A-step", C_, 22, "Hiper-IgM: sem centros germinativos", "Janeway Fig. 13.12"),
 (1487642739271, "V-pilar", C_, 23, "DGC: catalase-positivos e granulomas", "Abbas p. 231"),
 (1487642736949, "R-detalhe", C_, 23, "DGC: ligada ao X", "Janeway 13.17"),
 (1500234392681, "A-step", C_, 23, "DGC: Candida e Aspergillus", "Janeway 13.17"),
 (1506204165300, "R-detalhe", C_, 23, "DGC: Nocardia", "Janeway 13.17"),
 (1506212687876, "R-detalhe", C_, 23, "DGC: Pseudomonas", "Janeway 13.17"),
 (1581896616838, "A-step", C_, 23, "DGC: granulomas em qualquer órgão", "Abbas p. 231"),
 (1487642628188, "R-detalhe", C_, 23, "LAD: autossômica recessiva", "Janeway 13.17"),
 (1581896116295, "A-step", C_, 23, "LAD: infecções sem pus", "Janeway 13.17"),
 (1487642678318, "R-detalhe", C_, 23, "Chédiak-Higashi: microtúbulos", "Janeway 13.17"),
 (1487642685688, "R-detalhe", C_, 23, "Chédiak-Higashi: autossômica recessiva", "Janeway 13.17"),
 (1487642693791, "R-detalhe", C_, 23, "Chédiak-Higashi: grânulos gigantes", "Janeway 13.17"),
 (1487642705376, "R-detalhe", C_, 23, "Chédiak-Higashi: infecções piogênicas", "Abbas p. 232"),
 (1487642707794, "R-detalhe", C_, 23, "Chédiak-Higashi: neutropenia", "Janeway 13.17"),
 (1502066834360, "V-pilar", C_, 25, "HIV: gp120 liga CD4 + CCR5/CXCR4", "Abbas p. 234"),
 (1502068052536, "V-pilar", C_, 25, "AIDS: CD4 < 200", "Abbas p. 237"),
 # D. Autoinflamatórias
 (1487550507064, "R-detalhe", D_, 27, "FMF: neutrófilos", "Janeway 13.18"),
 (1487550517104, "R-detalhe", D_, 27, "FMF: autossômica recessiva", "Janeway 13.18"),
 (1487550504664, "A-step", D_, 27, "SAA aumentada na FMF", "Janeway 13.18 (fase aguda)"),
 (1487550515135, "A-step", D_, 27, "FMF: amiloide AA", "Janeway 13.18"),
 (1497215831699, "A-aula", D_, 27, "Febres periódicas: canakinumabe", "Janeway 13.18"),
 (1497215299862, "A-aula", D_, 27, "Canakinumabe bloqueia IL-1β", "Janeway 13.18; aula 08"),
]

CARDS = [
 # ---------- A. O que pode falhar (roteiro 2–3) ----------
 au("au-tres-grupos", ORG("How the <b>immune system</b> fails:<br>1. Too weak a response: {{c1::immunodeficiency}}<br>"
                          "2. Adaptive response against self: {{c1::autoimmunity}}<br>3. Innate inflammation with no trigger: {{c1::autoinflammatory}} disease"),
    "V-pilar", A_, "Três grupos de distúrbio imune", 2, "roteiro lâmina 2; apostila UC3.pdf (falha → autoagressão ou imunodeficiência); fala de Davi",
    extra="- Each group is a different failure: defense, self-tolerance, or the brake on inflammation<br>- An exaggerated response to a harmless foreign antigen is hypersensitivity (lesson 64)",
    espelhos=(1488248049633, 1539873617585, 1487815322485)),
 au("au-autoimune-x-autoinflamatoria", "<b>Autoimmune</b> diseases come from {{c1::adaptive::innate/adaptive}} immunity, and <b>autoinflammatory</b> diseases from {{c1::innate::innate/adaptive}} immunity",
    "V-pilar", A_, "Autoimune × autoinflamatória", 3, "roteiro lâmina 3; prova 2024 P1 2.12 (inflamação de baixo grau × autoimune)",
    extra="- Autoimmunity has a self antigen, autoantibodies and autoreactive T cells<br>- Autoinflammation has none of them: the inflammasome or cytokine brakes fail",
    espelhos=(1539873617585, 1486867513384, 1486867606359)),
 # ---------- B. Autoimunidade (roteiro 4–17) ----------
 au("au-tolerancia", "Self-tolerance induced in the <b>thymus or bone marrow</b> is {{c1::central::central/peripheral}}, and in <b>tissues</b> is {{c1::peripheral::central/peripheral}}",
    "V-pilar", B_, "Tolerância central × periférica", 4, "roteiro lâmina 4; prova 2025 P3 4.1 (timo e tolerância periférica)",
    extra="- Central: immature lymphocytes meet self antigens where they are made<br>- Peripheral: mature lymphocytes meet self antigens that never reached the thymus",
    espelhos=(1486952615115, 1486952612312, 1495599255138)),
 sh(1791625423808, "verde", B_, "Seleção negativa na medula tímica", 5, "V-hy: tolerância central T; Abbas p. 173; nota viva da aula 45"),
 sh(1791625423683, "verde", B_, "Seleção negativa: apoptose ou Treg", 5, "V-hy: Abbas Fig. 9-2; nota viva da aula 45"),
 sh(1791625423932, "verde", B_, "AIRE no timo", 5, "V-prova: prova 2015 P2 (APECED); nota viva da aula 45"),
 sh(1791629587897, "azul", B_, "Edição de receptor na célula B", 6, "A-aula: Abbas p. 180; nota viva da aula 49"),
 au("au-periferica", ORG("<b>Peripheral tolerance</b> of mature T cells:<br>1. {{c1::Anergy}} (antigen without costimulation)<br>"
                         "2. Suppression by {{c1::regulatory T}} cells<br>3. {{c1::Deletion}} by apoptosis"),
    "V-pilar", B_, "Três mecanismos de tolerância periférica", 7, "roteiro lâmina 7; prova 2018 P1 2.3 (regulação periférica) e 2025 P3 4.1",
    extra="- Each mechanism has a single-gene disease when it fails: FOXP3 (IPEX) for Treg, FAS (ALPS) for deletion",
    espelhos=(1488248049633, 1487117366290, 1487116960234)),
 sh(1791625428657, "verde", B_, "Anergia sem coestimulação", 8, "V-hy: Abbas Fig. 9-4; nota viva da aula 45"),
 sh(1791625428782, "azul", B_, "CTLA-4 inibe a ativação", 8, "A-aula: Abbas p. 176; nota viva da aula 45"),
 sh(1791625435108, "verde", B_, "Treg mantém a tolerância", 9, "V-hy: Abbas p. 177; nota viva da aula 45"),
 sh(1791625434757, "azul", B_, "Treg: CD25 e FOXP3", 9, "A-aula: Abbas p. 178; prova 2025 P3; nota viva da aula 45"),
 sh(1791625435233, "rosa", B_, "Treg: IL-10, IL-35, TGF-β", 9, "R-detalhe: Abbas p. 178; nota viva da aula 45"),
 sh(1791625432907, "rosa", B_, "Treg induzida por TGF-β e IL-2", 9, "R-detalhe: Abbas p. 178; nota viva da aula 45"),
 sh(1791625429533, "azul", B_, "Deleção por Fas–FasL (AICD)", 10, "A-aula: Abbas Fig. 9-6; nota viva da aula 45"),
 sh(1791054010623, "verde", B_, "HLA DR3/DR4 no DM1", 11, "V-hy: Abbas Fig. 9-11; nota viva do GR2"),
 sh(1791746130130, "verde", B_, "Mimetismo molecular", 12, "V-pilar: Abbas p. 185; nota viva da aula 35"),
 sh(1791625424057, "azul", B_, "AIRE → APS-1", 13, "V-prova: prova 2015 P2; nota viva da aula 45"),
 sh(1791625435783, "azul", B_, "FOXP3 → IPEX", 13, "V-prova: prova 2015 P2; nota viva da aula 45"),
 au("au-orgao-sistemica", "<b>Autoimmune diseases</b> are {{c1::organ-specific::organ-specific/systemic}} when one organ is attacked (Graves, type 1 diabetes) and {{c1::systemic::organ-specific/systemic}} when many are (SLE)",
    "A-aula", B_, "Órgão-específica × sistêmica", 15, "roteiro lâmina 15; provas 2024 P1 2.4 (Hashimoto) e 2024 P3 (LES)",
    extra="- The target antigen explains it: TSH receptor or insulin live in one organ, DNA and chromatin are in every cell",
    espelhos=(1539873617585, 1487815499468, 1585170002247)),
 sh(1791054010997, "verde", B_, "DM1: destruição por CD8", 16, "V-hy: Janeway 15.17; nota viva do GR2"),
 sh(1791667099713, "verde", B_, "Complemento precoce e LES", 17, "V-prova: provas 2024 P3 e 2016 P1; nota viva da aula 31"),
 # ---------- C. Imunodeficiências (roteiro 18–25) ----------
 au("au-primaria-secundaria", "<b>Immunodeficiencies</b> are {{c1::primary::primary/secondary}} when inherited and {{c1::secondary::primary/secondary}} when acquired, as in HIV, malnutrition or chemotherapy",
    "V-pilar", C_, "Primária × secundária", 18, "roteiro lâmina 18; apostila UC3.pdf (AIDS e imunossupressores); prova 2024 P3 3.1",
    extra="- Secondary forms are far more common: the system was normal and something removed part of it",
    espelhos=(1539873617585, 1544832356705, 1487727624742)),
 sh(1791626779153, "azul", C_, "Deficiência T → Candida superficial", 19, "A-aula: Janeway 13.7; nota viva das aulas 44/50"),
 sh(1791625424233, "azul", C_, "SCID por deficiência de MHC II", 20, "V-prova: prova 2015 P2 (seleção tímica); nota viva da aula 45"),
 sh(1791629593673, "azul", C_, "Hiper-IgM: CD40L", 22, "A-aula: Abbas p. 229; nota viva da aula 49"),
 sh(1791743343884, "verde", C_, "DGC: NADPH oxidase", 23, "V-hy: Abbas p. 230; nota viva das aulas 22/37"),
 sh(1791743343209, "verde", C_, "LAD 1: CD18", 23, "V-hy: Abbas p. 231; nota viva das aulas 37/38"),
 sh(1791780358431, "rosa", C_, "LAD 2: sialil-Lewis X", 23, "R-detalhe: Janeway 13.17; nota viva da aula 38"),
 sh(1791743343383, "verde", C_, "LAD: neutrofilia no sangue", 23, "V-hy: Janeway 13.17; nota viva da aula 37"),
 sh(1791743343509, "verde", C_, "LAD: sem neutrófilos no foco", 23, "V-hy: Janeway 13.17; nota viva da aula 37"),
 sh(1791780359109, "verde", C_, "LAD: sem pus", 23, "V-hy: Janeway 13.17; nota viva da aula 38"),
 sh(1791780362329, "azul", C_, "Chédiak-Higashi: fagolisossomo", 23, "A-step: Abbas p. 232; nota viva da aula 38"),
 sh(1791780362456, "rosa", C_, "Chédiak-Higashi: LYST", 23, "R-detalhe: Janeway 13.17; nota viva da aula 38"),
 sh(1791667100513, "verde", C_, "C5–C9 → Neisseria", 24, "V-hy: Janeway 13.16; nota viva da aula 31"),
 sh(1791667099963, "rosa", C_, "Inibidor de C1 → angioedema hereditário", 24, "R-detalhe: Janeway 13.16; nota viva da aula 31"),
 # ---------- D. Autoinflamatórias (roteiro 26–27) ----------
 sh(1791743339740, "rosa", D_, "Inflamassoma: sensor citoplasmático", 26, "R-detalhe: Janeway 13.18; nota viva da aula 08"),
 sh(1791743339860, "verde", D_, "Inflamassoma → IL-1β e IL-18", 26, "V-pilar: Janeway 13.18; nota viva da aula 08"),
 sh(1791780343453, "azul", D_, "NLRP3 + ASC + caspase-1", 26, "A-aula: Janeway 13.18; nota viva da aula 08"),
 au("au-autoinflam-sindromes", ORG("Mutated protein in each <b>autoinflammatory syndrome</b>:<br>1. Familial Mediterranean fever: {{c1::pyrin}} (MEFV gene)<br>"
                                   "2. Cryopyrin-associated periodic syndromes (Muckle-Wells): {{c1::NLRP3}}"),
    "A-aula", D_, "Síndromes autoinflamatórias e o gene", 27, "roteiro lâmina 27 (fala de Davi: principais síndromes por cima); Janeway 13.18",
    extra="- Both make the inflammasome release IL-1β without a trigger, so attacks of fever respond to IL-1 blockade<br>- TRAPS is the TNF version: a mutated TNF receptor 1 is not shed, so TNF signaling persists",
    espelhos=(1488248049633, 1497215831699, 1520715849479)),
]
CARDS += [ak(f"ak{n}", n, cod, bl, alvo, sl, mot) for n, cod, bl, sl, alvo, mot in AK]

finalizar(CARDS, HERE, BUSCA)

VERSO = {
 "ak1486952612312": "- Central tolerance: immature B cells that bind self antigen strongly in the marrow die (or edit their receptor)",
 "ak1489970994844": "- CD25 is the IL-2 receptor α chain; Tregs live on IL-2 and also deprive effector T cells of it",
 "ak1487983915856": "- HLA alleles raise risk because they present certain self peptides to T cells; they do not cause the disease alone",
 "ak1581890934727": "- Immune complexes deposit in small vessels (kidney, skin, joints) and attract neutrophils through complement",
 "ak1500404833072": "- Capsules resist phagocytosis until antibody and complement opsonize them",
 "ak1487727769430": "- Without antibodies, capsules cannot be opsonized for phagocytes",
 "ak1487727785545": "- Viruses and fungi hide inside cells or need Th1/Th17 help, which only T cells provide",
 "ak1476498858782": "- Toxic purine metabolites accumulate in dividing lymphocytes, so both T and B cells fail to mature",
 "ak1476498854265": "- ADA removes adenosine; without it, deoxyadenosine piles up and poisons lymphocytes",
 "ak1582321770897": "- RAG cuts DNA for V(D)J recombination; no receptor means no T or B cells",
 "ak1487727566026": "- Germinal centers need T cell help to form, and SCID has no T cells",
 "ak1487727477833": "- These pouches form the thymus and parathyroids, so T cells cannot mature",
 "ak1487727483197": "- The deleted region contains TBX1, needed for the thymic epithelium",
 "ak1486945186009": "- The paracortex is the T cell zone of the lymph node, empty without a thymus",
 "ak1487727589236": "- No mature B cells means no plasma cells, so every class falls",
 "ak1487727627992": "- Only the IgA class switch fails; most patients have no symptoms",
 "ak1487727631557": "- Never having made IgA, the patient makes antibodies against transfused IgA",
 "ak1487727658056": "- The CD40 ligand gene is on the X chromosome",
 "ak1487727666057": "- Without CD40L help, B cells cannot start germinal centers or switch class",
 "ak1506204165300": "- Catalase destroys the bacterium's own H2O2, which phagocytes without NADPH oxidase would borrow to kill it",
 "ak1581896616838": "- Macrophages that cannot kill keep calling T cells, so granulomas form wherever microbes persist",
 "ak1487642628188": "- Integrin CD18 genes are autosomal, unlike the X-linked CGD and XLA",
 "ak1487642678318": "- LYST controls lysosome traffic along microtubules, so phagosomes and lysosomes do not fuse",
 "ak1487642685688": "- A recessive defect in the LYST gene",
}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {
 "au-tres-grupos": "ganho: organiza os três grupos da aula; os cards de acervo citam imunodeficiência só como exemplo isolado",
 "au-tolerancia": "ganho: contrasta onde a tolerância é induzida; os cards de acervo tratam cada mecanismo isolado",
 "au-periferica": "ganho: reúne os três mecanismos periféricos que a aula classifica; anergia e Treg têm cards próprios do fato",
 "au-primaria-secundaria": "ganho: define primária × secundária, que os cards de acervo usam sem definir",
}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {
 "despejo": "Despejo lido inteiro (103 notas próprias): frentes completas, clozes certos, versos com porquê (24 versos novos), cores pela rubrica; o cloze aninhado da nota do HIV conferido renderizado no Anki (3 cards corretos).",
 "corrigidos": [],
}
ESCOPO = {
 "objetivo": "Classificar os distúrbios do sistema imune pelo mecanismo que falhou: imunodeficiência (defesa), autoimunidade (tolerância) e autoinflamação (freio da inflamação inata), com as principais síndromes por cima.",
 "centrais": [
   ("três falhas", "au-tres-grupos", "au-autoimune-x-autoinflamatoria"),
   ("tolerância e sua quebra", "au-tolerancia", "au-periferica", "ak1486952612312", "ak1486952615115", "ak1487117363961", "ak1487983926461", "ak1503089543399",
    "ak1462038188179", "ak1488418525490", "ak1581890934727"),
   ("autoimunidade cobrada em prova", "ak1495629799342", "ak1487815347337", "ak1487815316366"),
   ("classificação das imunodeficiências", "au-primaria-secundaria", "ak1539873617585", "ak1500404833072", "ak1487727534510", "ak1476498858782",
    "ak1487727571098", "ak1487642739271", "ak1502066834360", "ak1502068052536"),
 ],
 "exemplos": ["Graves", "miastenia", "LES", "DM1", "febre reumática", "SCID", "DiGeorge", "XLA", "DGC", "HIV"],
 "outras_aulas": [("seleção tímica e Treg", "45 Ativação de linfócitos T"), ("tolerância B", "49 Ativação de células B"), ("complemento", "31 Sistema complemento"),
                  ("inflamassoma", "08 Reconhecimento inato"), ("hipersensibilidade", "64 Reações de hipersensibilidade"), ("regulação", "72 Regulação do sistema imune")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
