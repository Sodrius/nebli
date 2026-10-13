# Especificação curada — Ativação de células B e plasticidade da resposta humoral (UC03 P3, Imunologia; aula 09 da turma; 62 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-im49-20261010a"
SHORT = "im49"
LESSON = "2026-uc03-imunologia-49-ativacao-celulas-b"
DECK = "NEBLI::UC03::P3::Imunologia::Ativação de células B"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-02) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 46 consultas), tags de seção FirstAid de B cells, anticorpos, isótipos, imunidade passiva e vacinas (busca/tags-secao.txt), 10/10: ")
EXCLUIDOS = [
 (1486945114357, "TdT: não citada na aula"),
 (1486867718130, "TCR rígido: a aula compara só valência e secreção"),
 (1487117055356, "papaína/pepsina: fora da aula"),
 (1487117081885, "IgM liga 10 antígenos: HY5, valência já no pentâmero"),
 (1487117161213, "IL-4/IL-13 → IgE: repete il4-ige compartilhado"),
 (1489970973404, "CD40L em Th: repete o card CD40 compartilhado"),
 (1487727647861, "hiper-IgM sem troca de classe: repete hiper-igm"),
 (1487117104655, "IgM na resposta primária: repete igm-primeira"),
 (1487117240890, "IgA não fixa complemento: tabela da lâmina 39 coberta por fixa-complemento"),
 (1487121952455, "imunização passiva genérica: a aula só usa placenta e leite"),
 (1487121965148, "IgA do leite como imunização passiva: repete iga-leite + passiva-placenta"),
 (1486945159596, "folículo primário dormente: linfonodo já coberto pelo folículo secundário compartilhado"),
]
FORA_DO_RECORTE = ["complemento C3a/C5a e MAC (aula 31)", "imunodeficiências humorais além da hiper-IgM", "linfomas e mieloma", "calendário vacinal"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_, G_, H_, I_, J_ = ("A-ontogenia", "B-bcr-recombinacao", "C-b1-b2", "D-imunoglobulinas", "E-ativacao", "F-mudancas",
                                          "G-efetoras", "H-mucosa-passiva", "I-cinetica", "J-vacinas-fdc")
CARDS = [
 # ---------- A. Ontogenia (slides 2–5) ----------
 ak("pro-b", 1486952589995, {1: V}, A_, "Pró-B sem μ", 3, "Verde: HY; primeiro estágio da lâmina 3."),
 ak("pre-b", 1486952594655, {1: Z}, A_, "Pré-B com μ citoplasmática", 3, "Azul: estágio da lâmina 3."),
 ak("imatura", 1486952598683, {1: V}, A_, "B imatura: IgM sem IgD", 3, "Verde: HY; lâminas 3 e 5."),
 ak("naive-igm-igd", 1486867654077, {1: V}, A_, "B madura naive: IgM e IgD", 3, "Verde: HY; dois BCRs da B madura (transcrição)."),
 ak("plasmocito-ig", 1486952603043, {1: V}, A_, "Plasmócito: Ig citoplasmática", 3, "Verde: HY; quem secreta anticorpo é o plasmócito."),
 ak("memoria-b", 1486952607566, {1: V}, A_, "B de memória com IgG/IgA/IgE", 3, "Verde: HY; produto da fase dependente de antígeno."),
 au("selecao-medula", "Immature B cells that bind self antigen strongly in the bone marrow die by {{c1::apoptosis}}", {1: Z}, A_,
    "Seleção negativa na medula", "4; transcrição", "central", "AnKing só tem seleção negativa do timo.", [1486952598683, 1540066474869], "Azul: lâmina 4."),
 au("edicao", "Unlike T cells, self-reactive immature B cells can rescue themselves by receptor {{c1::editing}}", {1: Z}, A_,
    "Edição do receptor", "4; transcrição", "central", "consulta 'receptor editing' sem card.", [1486952598683, 1486945105493],
    "Azul: diferença B × T destacada na transcrição.", extra="- They rearrange their light-chain genes again, lowering self-affinity"),
 ak("naive-secundario", 1540066474869, {1: V}, A_, "B naive vai ao órgão linfoide secundário", 5, "Verde: HY; lâmina 5."),
 # ---------- B. BCR e recombinação (slides 6–12) ----------
 ak("cadeias", 1486867658485, {1: V}, B_, "Duas pesadas e duas leves", 6, "Verde: HY; estrutura do BCR (lâminas 6 e 17)."),
 ak("idiotipo", 1486867676959, {1: V, 2: Z}, B_, "Fab define o idiótipo", 6, "Verde c1 (HY), azul c2."),
 ak("isotipo-fc", 1486867685826, {1: V, 2: Z}, B_, "Fc define o isótipo", 6, "Verde c1 (HY), azul c2; troca de classe muda o Fc."),
 ak("pesada", 1486867696248, {1: V}, B_, "Pesada no Fab e Fc", 6, "Verde: HY; lâmina 6."),
 ak("leve", 1486867700749, {1: Z}, B_, "Leve só no Fab", 6, "Azul: HY que repete o recíproco pesada (F-20261010-CLAUDE-03).", hy_repete="pesada"),
 ak("tcr-monovalente", 1486867708925, {1: V}, B_, "TCR αβ monovalente", 7, "Verde: HY; comparação TCR × Ig (lâmina 7)."),
 au("tcr-secretado", "Unlike antibodies, the T-cell receptor is never {{c1::secreted}}", {1: Z}, B_,
    "TCR nunca é secretado", "7", "central", "AnKing compara valência, não secreção.", [1486867708925, 1486867658485], "Azul: lâmina 7."),
 ak("combinacao", 1486945119290, {1: V}, B_, "Pareamento aleatório pesada-leve", 7, "Verde: HY; cada cadeia recombina sozinha (lâmina 7)."),
 au("antes-antigeno", "V(D)J recombination happens in immature lymphocytes, before they ever meet {{c1::antigen}}", {1: Z}, B_,
    "Recombinação antes do antígeno", "8; transcrição", "central", "AnKing diz 'antigen-independent' sem o momento.", [1486945028810, 1486945119290],
    "Azul: lâmina 8.", extra="- B cells in the bone marrow, T cells in the thymus, while not proliferating"),
 ak("rag", 1486945105493, {1: V}, B_, "RAG1 e RAG2", 8, "Verde: enzimas nomeadas na lâmina 8."),
 ak("vdj-pesada", 1486945028810, {1: V, 2: V}, B_, "V(D)J na pesada", 9, "Verdes: HY; lâminas 9 e 11."),
 ak("dj-primeiro", 1486945095844, {1: V}, B_, "D-J antes de V-DJ", 9, "Verde: HY; sequência da lâmina 9."),
 ak("vj-leve", 1486945100917, {1: V, 2: Z}, B_, "VJ na leve", 10, "Verde c1 (HY), azul c2; lâmina 10."),
 # ---------- C. B-1 × B-2 e plasmócito (slides 13–14) ----------
 au("b1-cavidades", "B-1 cells arise in fetal life and renew themselves in the pleural and peritoneal {{c1::cavities}}", {1: Z}, C_,
    "B-1: origem fetal e cavidades", "13; transcrição", "central", "consultas B-1/B1 sem card de B-1.", [1486952598683, 1540066474869], "Azul: lâmina 13."),
 au("b1-cd5", "B-1 cells are marked by surface {{c1::CD5}}", {1: R}, C_,
    "B-1 é CD5+", "13; transcrição", "lateral", "sem card nos acervos.", [1486952594655, 1486952598683], "Rosa: marcador da lâmina 13."),
 au("b1-igm", "B-1 cells secrete natural {{c1::polyreactive}} IgM", {1: Z}, C_,
    "IgM natural polirreativa", "13; transcrição; monitoria", "central", "sem card nos acervos.", [1487117025756, 1487117011573], "Azul: lâmina 13."),
 au("b2", "Conventional B-2 cells are continuously replenished from the {{c1::bone marrow}}", {1: Z}, C_,
    "B-2 convencional", "13; transcrição", "central", "sem card nos acervos.", [1486867654077, 1487117045399], "Azul: lâmina 13."),
 au("plasmocito-mhc", "Plasma cells lose surface Ig and MHC II, so unlike resting B cells they no longer {{c1::present antigen}}", {1: Z}, C_,
    "Plasmócito × B em repouso", "14; transcrição", "central", "AnKing só tem Ig citoplasmática no plasmócito.", [1486952603043, 1487116998408], "Azul: lâmina 14."),
 # ---------- D. Imunoglobulinas (slides 15–21) ----------
 ak("rer", 1468101790635, {1: V}, D_, "RER abundante no plasmócito", 16, "Verde: HY; síntese da lâmina 16."),
 ak("dobradica", 1486867662727, {1: Z, 2: Z}, D_, "Dobradiça dá flexibilidade", 17, "Azuis: lâmina 17."),
 ak("kappa-lambda", 1496110724165, {1: Z}, D_, "Leve κ ou λ, nunca mista", 17, "Azul: lâmina 17 e transcrição."),
 ak("kappa-ratio", 1496110744913, {1: R}, D_, "κ:λ ≈ 3:1", 17, "Rosa: 'muito mais κ' (transcrição)."),
 ak("igab", 1486867667014, {1: V}, D_, "Igα/Igβ sinalizam", 18, "Verde: HY; cauda curta do BCR precisa de acessórias (transcrição)."),
 au("cd19", "{{c1::CD19}} is the signaling chain of the B-cell coreceptor, together with CD21 and CD81", {1: Z}, D_,
    "Correceptor CD19/CD21/CD81", "18–19; transcrição", "central", "AnKing cita CD19 só como marcador.", [1503855271322, 1486867667014], "Azul: lâmina 19."),
 ak("cr2-c3d", 1503855271322, {1: Z}, D_, "CD21 liga C3d", 19, "Azul: correceptor da lâmina 19."),
 au("cd22", "{{c1::CD22}} is an inhibitory B-cell coreceptor that recruits the phosphatase SHP-1", {1: Z}, D_,
    "CD22 inibitório", "19; transcrição", "central", "consulta CD22 só com linfomas e terapias.", [1503855271322, 1486867667014],
    "Azul: feedback negativo da transcrição.", extra="- It gives negative feedback when B cells are strongly activated"),
 ak("igm-pentamero", 1487117077263, {1: V, 2: Z}, D_, "IgM pentâmero com J", 20, "Verde c1 (HY), azul c2; lâmina 20."),
 ak("iga-dimero", 1487117219869, {1: V, 2: Z}, D_, "IgA dímero com J", 20, "Verde c1 (HY), azul c2; lâmina 20."),
 ak("igm-membrana", 1487117074086, {1: Z}, D_, "IgM monômero na membrana", 20, "Azul: HY recíproco de igm-pentamero (F-20261010-CLAUDE-03).", hy_repete="igm-pentamero"),
 au("fcr-nome", "Receptors for the Fc portion of IgG are called {{c1::Fcγ}} receptors", {1: R}, D_,
    "Receptores Fc", "21; transcrição", "lateral", "sem card de receptores Fc.", [1500404728172, 1487117328797],
    "Rosa: lâmina 21.", extra="- Some FcγRs activate the cell and others inhibit it"),
 # ---------- E. Ativação T-independente e T-dependente (slides 22–32) ----------
 au("ti-crosslink", "Thymus-independent antigens with repeating epitopes activate B cells by {{c1::cross-linking}} many BCRs", {1: V}, E_,
    "TI ativa por ligação cruzada", "23, 25; transcrição; monitoria", "central", "AnKing diz que estimulam B diretamente, sem o mecanismo.",
    [1487117011573, 1487117038124], "Verde: mecanismo central da ativação TI."),
 sh(1791625426282, "verde", E_, "Antígeno sem peptídeo estimula B direto", 25, "Verde: nota já existente de Ativação de linfócitos T."),
 ak("ti-igm", 1487117025756, {1: V}, E_, "TI só gera IgM", 25, "Verde: HY; provas 2017 P3 5.2."),
 ak("ti-memoria", 1487117018684, {1: V}, E_, "TI sem memória", 25, "Verde: HY; prova 2018 P2 2.7."),
 ak("lps", 1487117038124, {1: V}, E_, "LPS é antígeno TI", 25, "Verde: HY; exemplo da transcrição."),
 au("ti-baff", "Cytokines such as {{c1::BAFF}} let some thymus-independent antigens induce class switching", {1: R}, E_,
    "TI-2 com citocinas troca isótipo", "25; transcrição", "lateral", "sem card nos acervos.", [1487117025756, 1487117152018],
    "Rosa: lâmina 25.", extra="- Example: pneumococcal polysaccharide vaccine"),
 ak("td-memoria", 1487117045399, {1: Z}, E_, "TD gera memória", 23, "Azul: HY que repete o contraste de ti-memoria (F-20261010-CLAUDE-03).", hy_repete="ti-memoria"),
 ak("b-apc-mhc2", 1487116998408, {1: V}, E_, "B apresenta em MHC II ao T", 27, "Verde: HY; lâminas 27 e 30."),
 au("conjugada", "Conjugate vaccines link a polysaccharide to a {{c1::protein}} carrier so that helper T cells can be recruited", {1: V}, E_,
    "Vacina conjugada", "28, 61; transcrição; prova 2018 P2 2.7", "prova", "AnKing tem Hib e PCV, sem o mecanismo.", [1515891214525, 1485803767833],
    "Verde: prova 2018.", extra="- The result is class-switched IgG and memory against the polysaccharide"),
 ak("hib", 1515891214525, {1: Z, 2: Z}, E_, "Hib conjugada ao toxoide diftérico", 28, "Verde c1 (HY), azul c2. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("pcv-igg", 1485803767833, {1: Z}, E_, "PCV gera IgG", 28, "Azul: conjugada → IgG."),
 sh(1791625431258, "verde", E_, "CD40–CD40L ativa o B", 29, "Verde: nota já existente de Ativação de linfócitos T."),
 au("cd40l-induzivel", "CD40 is constitutive on B cells, whereas CD40L is {{c1::induced}} on helper T cells after activation", {1: Z}, E_,
    "CD40L é induzível", "29; transcrição", "central", "AnKing não diz o que é constitutivo.", [1487117002637, 1489970973404], "Azul: lâmina 29."),
 sh(1791625431383, "verde", E_, "Troca de classe por CD40L e citocinas", 29, "Verde: nota já existente de Ativação de linfócitos T."),
 ak("hiper-igm", 1487727642575, {1: Z, 2: Z}, E_, "Hiper-IgM por CD40L defeituoso", 29, "Azuis: prova 2017 P3 5.2 (CD40 KO)."),
 sh(1791625425757, "verde", E_, "Folículo secundário com centro germinativo", 31, "Verde: nota já existente de Ativação de linfócitos T."),
 ak("centro-humoral", 1700925803760, {1: V}, E_, "Centro germinativo cresce na resposta humoral", 31, "Verde: HY; lâmina 31."),
 au("borda", "Activated helper T cells and antigen-bearing B cells meet at the edge of the {{c1::follicle}}", {1: Z}, E_,
    "Encontro T:B na borda do folículo", "32; transcrição", "central", "sem card nos acervos.", [1486945164044, 1487116998408], "Azul: lâmina 32."),
 # ---------- F. Mudanças induzidas pela ativação (slides 33–40) ----------
 au("secretada", "Plasma cells release antibody as a {{c1::secreted}} protein instead of a membrane receptor", {1: Z}, F_,
    "Membrana → secretada", "34; transcrição", "central", "sem card nos acervos.", [1486952603043, 1487117074086], "Azul: lâmina 34."),
 ak("afinidade", 1487117121383, {1: V, 2: V}, F_, "Hipermutação somática e maturação de afinidade", 35, "Verdes: HY; lâminas 35 e 40."),
 ak("switch-local", 1487117143873, {1: V}, F_, "Troca no centro germinativo", 32, "Verde: HY; lâminas 32 e 40."),
 au("troca-constante", "Class switching keeps the antibody {{c1::variable}} region, so specificity is unchanged", {1: V}, F_,
    "Troca de classe muda só a região constante", "36–37; transcrição; prova 2017 P1 4.4", "prova", "AnKing tem onde e quem, não o que muda.",
    [1487117152018, 1486867685826], "Verde: prova 2017.", extra="- Only the heavy-chain constant region (Fc) changes"),
 ak("tgfb-iga", 1487117156031, {1: R, 2: Z}, F_, "TGF-β → IgA", 38, "Azul c2 (IgA; prova 2015 P2 5.2), rosa c1 (IL-5)."),
 sh(1791625434208, "azul", F_, "IFN-γ → IgG", 38, "Azul: nota já existente de Ativação de linfócitos T."),
 sh(1791625434333, "azul", F_, "IL-4 → IgE", 38, "Azul: nota já existente de Ativação de linfócitos T."),
 au("cdr", "Affinity-raising somatic mutations are selected and accumulate in the {{c1::CDRs}}", {1: Z}, F_,
    "Mutações nos CDR", "40; transcrição", "central", "consulta hypervariable/CDR sem card imunológico.", [1487117121383, 1486867676959], "Azul: lâmina 40."),
 au("aid", "Somatic hypermutation and class switching both depend on the enzyme {{c1::AID}}", {1: V}, F_,
    "AID", "40; transcrição; monitoria; prova 2017 P3 5.2", "prova", "consulta 'activation-induced' sem card.", [1487117121383, 1487117143873],
    "Verde: prova 2017 (AID KO).", extra="- Activation-induced cytidine deaminase, expressed after T-cell help"),
 # ---------- G. Funções efetoras (slides 41–52) ----------
 au("neutralizacao", "Neutralizing antibodies block microbes or toxins from binding host {{c1::cell receptors}}", {1: V}, G_,
    "Neutralização", "42–43; transcrição", "central", "consulta neutraliz* sem card de definição.", [1487117197858, 1487117238120], "Verde: primeira função efetora."),
 ak("opsonizacao-igg", 1487117197858, {1: V}, G_, "IgG opsoniza", 44, "Verde: HY; lâminas 39 e 44."),
 ak("capsula-igg", 1500404728172, {1: V, 2: Z}, G_, "IgG → FcR ou complemento", 45, "Verde c1 (HY), azul c2."),
 ak("fixa-complemento", 1487117187498, {1: V}, G_, "IgM e IgG fixam complemento", 47, "Verde: HY; lâminas 39 e 47."),
 au("igm-complemento", "Bound, but not free, IgM exposes its binding sites for {{c1::C1q}}", {1: Z}, G_,
    "IgM ligada ativa complemento", "46–47; transcrição", "central", "consulta C1q IgM sem card.", [1487117187498, 1487117077263], "Azul: lâmina 47."),
 au("igg-duas", "A single bound IgM can start the classical pathway, but IgG needs {{c1::two}} adjacent molecules", {1: Z}, G_,
    "IgG precisa de moléculas adjacentes", "47; transcrição", "central", "sem card nos acervos.", [1487117187498, 1487117174952], "Azul: lâmina 47."),
 ak("adcc-igg", 1487117328797, {1: V}, G_, "IgG medeia ADCC", 50, "Verde: HY; lâmina 50."),
 au("nk-cd16", "In ADCC, NK cells bind antibody-coated cells through the low-affinity receptor {{c1::FcγRIII}} (CD16)", {1: Z}, G_,
    "NK usa FcγRIII", "50", "central", "consulta ADCC sem o receptor.", [1487117328797, 1500404728172], "Azul: lâmina 50."),
 ak("ige-helminto", 1487117266817, {1: V}, G_, "IgE e eosinófilos contra helmintos", 50, "Verde: HY; lâmina 50."),
 ak("ige-mastocito", 1487117260690, {1: V}, G_, "IgE liga mastócitos", 51, "Verde: HY; lâmina 51."),
 ak("ige-crosslink", 1487640136892, {1: V}, G_, "Ligação cruzada de IgE ativa mastócito", 51, "Verde: HY; lâmina 51."),
 # ---------- H. Mucosa e imunidade passiva (slides 53–57) ----------
 ak("iga-mais-produzida", 1487117209824, {1: V}, H_, "IgA é a mais produzida", 54, "Verde: HY; imunoglobulina de mucosa."),
 sh(1790980915277, "azul", H_, "Plasmócitos IgA na lâmina própria", 54, "Azul: lâmina 54. Nota já existente de Intestinos (UC08)."),
 ak("pigr", 1487117251418, {1: V, 2: V}, H_, "Cadeia J + receptor poli-Ig", 54, "Verdes: HY; prova 2015 P2 5.3."),
 ak("transcitose", 1487117223955, {1: Z}, H_, "IgA atravessa por transcitose", 54, "Azul: lâmina 54."),
 ak("componente-secretor", 1487117255825, {1: V}, H_, "Componente secretor protege a IgA", 54, "Verde: HY; prova 2015 P2 5.3."),
 ak("iga-secrecoes", 1487117238120, {1: V}, H_, "IgA nas secreções", 55, "Verde: HY; lâmina 55."),
 ak("igg-placenta", 1487117191334, {1: V}, H_, "IgG cruza a placenta", 56, "Verde: HY; prova 2017 P3 1.5."),
 ak("passiva-placenta", 1487121969591, {1: Z}, H_, "IgG materna = imunização passiva", 56, "Azul: HY que repete igg-placenta (F-20261010-CLAUDE-03).", hy_repete="igg-placenta"),
 ak("iga-leite", 1487117234083, {1: V}, H_, "IgA no colostro", 56, "Verde: HY; lâminas 56–57."),
 au("colostro", "IgA in colostrum is about {{c1::2000}} times more concentrated than in saliva", {1: R}, H_,
    "IgA no colostro × saliva", "57; transcrição", "lateral", "sem card nos acervos.", [1487117234083, 1487121969591],
    "Rosa: número da lâmina 57.", extra="- About 20 g/L on day 2 after birth versus 0.01 g/L in saliva"),
 # ---------- I. Cinética (slides 58–60) ----------
 ak("igm-primeira", 1487117100809, {1: V}, I_, "IgM é a primeira", 59, "Verde: HY; lâmina 59."),
 ak("igg-secundaria", 1487117165317, {1: V}, I_, "IgG domina a resposta secundária", 59, "Verde: HY; lâmina 59."),
 au("secundaria-rapida", "Compared with the primary response, the secondary antibody response has a shorter lag and a {{c1::higher}} peak", {1: V}, I_,
    "Resposta secundária mais rápida e maior", "58, 60; transcrição", "central", "consulta primary/secondary response só com isótipos.",
    [1487117165317, 1487117100809], "Verde: lâminas 58 e 60.", extra="- Memory B cells and higher-affinity antibodies explain the difference"),
 au("sorologia-igm", "Pathogen-specific IgM without IgG suggests a {{c1::recent primary}} infection", {1: V}, I_,
    "Sorologia IgM × IgG", "59; transcrição; prova 2023 P2 2.2", "prova", "sem card de sorologia geral.", [1487117100809, 1487122118000],
    "Verde: prova 2023.", extra="- Example: rubella IgM and IgG testing in pregnancy"),
 ak("igm-neonato", 1487122118000, {1: Z}, I_, "IgM diagnostica infecção neonatal", 59, "Verde: HY; IgM não cruza a placenta. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 # ---------- J. Vacinas e células dendríticas foliculares (slides 61–62) ----------
 ak("polio-oral", 1516219843437, {1: V}, J_, "Pólio oral gera IgA", 61, "Verde: lâmina 61 e prova 2015 P2 5.2."),
 ak("toxoide", 1520350606644, {1: Z}, J_, "Toxoide contra toxinas", 61, "Verde: HY; tétano e difteria (lâmina 61). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("hbv-subunidade", 1520349768071, {1: Z}, J_, "Vacina HBV de subunidade", 61, "Verde: HY; proteína recombinante (lâmina 61). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 au("fdc", "{{c1::Follicular dendritic}} cells keep intact antigen on their surface and sustain memory B cells", {1: Z}, J_,
    "Células dendríticas foliculares", "32, 62; transcrição; monitoria", "central", "consulta 'follicular dendritic' sem card AnKing.",
    [1486945164044, 1700925803760], "Azul: lâmina 62.", extra="- They hold antigen with Fc and complement receptors"),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {'pro-b': '- First committed stage in the bone marrow, before heavy-chain rearrangement is complete',
 'pre-b': '- The μ chain pairs with a surrogate light chain to form the pre-BCR',
 'imatura': '- IgD appears only when the cell finishes maturing in a secondary lymphoid organ',
 'naive-igm-igd': '- Both BCRs share the same variable region, so the same specificity',
 'plasmocito-ig': '- They make large amounts of antibody but no longer present antigen',
 'memoria-b': '- They respond faster on re-exposure to the same antigen',
 'selecao-medula': '- Weak self-recognition lets the cell leave for the blood',
 'cadeias': '- Light chains are kappa or lambda; heavy chains define the isotype',
 'pesada': '- Variable + constant domains; CH2/CH3 form the Fc',
 'leve': '- One variable and one constant domain',
 'tcr-secretado': '- Antibodies exist both as membrane BCR and as secreted protein',
 'combinacao': '- Heavy and light chains rearrange independently, then pair',
 'dj-primeiro': '- Done by RAG1/RAG2 before the cell meets antigen',
 'vj-leve': '- Light-chain loci have no D segments',
 'b1-cavidades': '- They are not continuously replaced by the bone marrow',
 'b1-cd5': '- Conventional B-2 cells are CD5 negative',
 'b1-igm': '- Mostly against carbohydrates, e.g., ABO blood group antigens',
 'b2': '- They make high-affinity, class-switched antibodies against proteins',
 'plasmocito-mhc': '- Resting B cells express MHC II and present antigen but secrete little Ig',
 'rer': '- Ig is made in the RER, glycosylated in the Golgi and secreted in vesicles',
 'dobradica': '- Lets the two Fab arms reach antigens at different distances',
 'cd19': '- The BCR tail is too short to signal on its own',
 'ti-crosslink': '- Example: LPS and capsular polysaccharides',
 'lps': '- Repeating sugar units bind many identical BCRs',
 'b-apc-mhc2': '- Signal 1 is TCR–MHC II; signal 2 is costimulation (B7–CD28, CD40–CD40L)',
 'cd40l-induzivel': '- B7–CD28 signaling first activates the T cell, which then expresses CD40L',
 'borda': '- Chemokine receptors guide both cells to the same region',
 'secretada': '- The antigen-binding site is unchanged',
 'tgfb-iga': '- TGF-β is abundant in the gut, so oral antigens favor IgA',
 'cdr': '- Mutations are random; the selection by antigen enriches the useful ones',
 'neutralizacao': '- IgG is the main neutralizing antibody in blood; IgA on mucosae',
 'capsula-igg': '- Phagocytes bind opsonized microbes through FcγRI',
 'igm-complemento': '- C1q is the first protein of the classical pathway',
 'fixa-complemento': '- A single bound IgM pentamer is enough to start the classical pathway',
 'igg-duas': '- IgG4 does not activate complement',
 'nk-cd16': '- The NK cell then kills the target by apoptosis',
 'ige-helminto': '- Eosinophils bind IgE by FcεRI and release toxic basic proteins',
 'ige-mastocito': '- Mast cells carry the high-affinity receptor FcεRI',
 'transcitose': '- The poly-Ig receptor carries dimeric IgA from the basal to the luminal side',
 'iga-secrecoes': '- IgA in mucus neutralizes microbes before they reach the epithelium',
 'passiva-placenta': '- A specific receptor transports maternal IgG across the placenta',
 'iga-leite': '- Colostrum also contains IgG',
 'igm-primeira': '- Later, cytokines drive class switching to IgG, IgA or IgE',
 'toxoide': '- Neutralizing IgG blocks tetanus and diphtheria toxins'}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
DUPLICACAO = {}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]
