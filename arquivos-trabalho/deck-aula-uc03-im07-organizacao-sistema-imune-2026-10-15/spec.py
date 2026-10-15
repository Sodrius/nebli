# Especificação curada — Organização e funcionamento do sistema imune (UC03 P1, Imunologia; Prof. José Alexandre Barbuto; 26 lâminas).
# Feita do zero em 15/10 (a corrida de 11/10 do Codex ficou só no molde). Inventário por informação: lâminas + transcrição inteira + provas imuno-01.
# Aula-guarda-chuva da imunologia: órgãos linfoides, recirculação, endereçamento, resposta × tolerância. Detalhes de PRR (08), MHC (20), efetores (22) e
# subtipos T (45) ficam nas aulas próprias; aqui entram os princípios e as relações, com sh() de cards dessas aulas quando a lâmina os retoma.
RUN_ID = "uc03-im07-20261015a"
SHORT = "im07"
LESSON = "2026-uc03-imunologia-07-organizacao-sistema-imune"
DECK = "NEBLI::UC03::P1::Imunologia::Organização do sistema imune"
CRITERIOS = "MEMORY.md (§2 cobertura longitudinal, §5–6 conexão/compreensão) + ANTI-EXEMPLARES-CARDS + auditoria 15/10, 15/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (primary lymphoid organ, thymus, bone marrow, secondary lymphoid, paracortex, high endothelial venules, PALS, white pulp, "
         "germinal center, follicle, M cell, Peyer, MALT, selectin, integrin, chemokine, natural Treg, tertiary lymphoid) e cópias NEBLI vivas "
         "(08, 17, 20, 22, 45, 62), 15/10: ")
EXCLUIDOS = []
FORA_DO_RECORTE = ["Recapitulação da UC02 (repertório, seleção): princípios retomados aqui em card próprio.",
                   "Lista de quimiocinas (lâmina 23): famílias por cisteínas já cobradas na aula 08.",
                   "Leitura complementar (26): lista de artigos."]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não tem este princípio da aula como card."
EP = [1486945131833, 1486945128758, 1486945178237]
A_, B_, C_, D_, E_, F_, H_, I_ = ("A-papel-do-sistema", "B-resposta-inata-no-tecido", "C-orgaos-primarios", "D-recirculacao",
                                  "E-sistema-em-acao", "F-orgaos-secundarios", "H-eferencia", "I-enderecamento")

CARDS = [
 # A — papel do sistema (4–5)
 au("a-exterior", "Besides the <b>nervous system</b>, the body system that includes the outside world in keeping homeostasis, reading <b>molecular signals</b>, is the {{c1::immune system}}",
    {1: Z}, A_, "Sistema imune considera o exterior", "4", "central", NAO, EP, "Azul: lâmina 4.",
    extra="- Most body systems only watch internal signals; immunity reads molecules from outside"),
 au("a-antigeno", "The <b>immune system</b> recognizes almost anything because lymphocytes carry a complete repertoire of clonally distributed receptors, and what they recognize is called an {{c1::antigen}}",
    G(1), A_, "Tradutor universal: repertório clonal e antígeno", "5", "central", NAO, EP, "Verde: lâmina 5.",
    extra="- Each lymphocyte carries one receptor; the whole population covers almost every molecule of the right size"),
 # B — o sistema em ação no tecido (6–9)
 au("b-alarmes", ORG("<b>Tissue alarms</b> when homeostasis is disturbed:<br>- damaged tissue cells: {{c1::DAMPs}}<br>- macrophages: cytokines and chemokines<br>- mast cells: {{c2::inflammatory mediators}}, fast<br>- endothelial cells: {{c3::adhesion molecules}}"),
    G(1, 2, 3), B_, "Células residentes e seus alarmes", "6", "prova", NAO, EP, "Verde: lâminas 6 e 9; prova 2024 P2 2.1 (elementos da inata).",
    extra="- Innate lymphoid cells (ILCs) help steer the type of response; an adaptive response always develops in parallel<br>- All this sits behind anatomical, functional and biological barriers"),
 sh(1792029611637, "verde", B_, "Fagocitose", "7", "Verde: lâmina 7; organizador vivo na aula 08."),
 sh(1792054600579, "verde", B_, "Citotoxicidade", "8", "Verde: lâmina 8; organizador vivo na aula 08."),
 sh(1792055399868, "verde", B_, "Especificidade e memória: inata × adquirida", "9", "Verde: prova 2024 P1 2.11 (diferença inata × adquirida); organizador vivo na aula 17."),
 # C — órgãos linfoides primários (10)
 au("c-primarios", ORG("<b>Primary lymphoid organs</b>, where the repertoire is made:<br>- {{c1::thymus}}: T cells<br>- {{c2::bone marrow}}: B cells"),
    G(1, 2), C_, "Órgãos linfoides primários", "10", "central", NAO, EP, "Verde: lâminas 10–11.",
    extra="- Receptor genes are assembled and useful receptors selected here, shielded from the outside<br>- Receptor genes do not exist in the germline"),
 au("c-selecao-timo", ORG("Selection of <b>thymocytes</b>:<br>1. TCR must bind self MHC, or the cell dies: {{c1::positive selection}}<br>2. strongly self-reactive cells: {{c2::clonal deletion}} or become {{c3::regulatory T cells}}"),
    G(1, 2, 3), C_, "Critérios de seleção no timo", "10", "prova", NAO, EP, "Verde: lâmina 10; prova ‘quais os processos e critérios de seleção no timo?’.",
    extra="- Almost every adaptive response depends on T cells, so thymic selection is the strictest"),
 sh(1791625434632, "azul", C_, "Treg natural nasce no timo", "10", "Azul: lâmina 10 (desvio funcional para Treg); prova 2025 (timo e tolerância periférica); viva na aula 45."),
 au("c-medula-menos-estrita", "<b>Selection of B cells</b> in the bone marrow can be less strict than in the thymus because antibody responses still need help from {{c1::T cells}}",
    {1: Z}, C_, "Por que a seleção na medula é menos estrita", "10", "prova", NAO, EP, "Azul: prova ‘justifique a seleção na medula ser menos estrita que no timo’; conexão com a aula 49.",
    extra="- A self-reactive B cell that escapes still finds no T-cell help, because those T cells were deleted in the thymus"),
 # D — recirculação (11–15)
 au("d-secundarios", ORG("<b>Secondary lymphoid organs</b>, where antigens are recognized:<br>- {{c1::lymph nodes}}<br>- {{c2::spleen}}<br>- mucosa-associated lymphoid tissue ({{c3::MALT}}): Peyer patches, appendix, Waldeyer ring"),
    G(1, 2, 3), D_, "Órgãos linfoides secundários", "11", "central", NAO, EP, "Verde: lâmina 11.",
    extra="- The mucosa is where the immune system spends most of its energy", duplicacao_ok="organizador; o AnKing cobra só o papel geral"),
 ak("ak-secundarios", 1486945131833, G(1), D_, "Secundários: interação com antígeno", "11", "Verde: HY 1; lâmina 11."),
 au("d-naive", "<b>Naive lymphocytes</b> recirculate from blood into secondary lymphoid organs and back to the blood through the {{c1::lymph}}, never returning to the primary organ",
    G(1), D_, "Via dos linfócitos naive", "13", "central", NAO, EP, "Verde: lâmina 13 e transcrição (via de mão única do órgão primário).",
    extra="- Recognition happens in the secondary organ; action happens in the tissue"),
 sh(1791625425583, "verde", D_, "HEV: porta de entrada no linfonodo", "13", "Verde: lâmina 13 (HEV); viva na aula 45."),
 au("d-por-que", "<b>Lymphocytes</b> must recirculate because each one recognizes only a {{c1::single antigen}}, so no lymph node holds the whole repertoire at once",
    {1: Z}, D_, "Por que recircular", "13", "central", NAO, EP, "Azul: transcrição; card de conexão (repertório clonal → recirculação).",
    extra="- Recirculation keeps every lymph node sampled by the whole repertoire over time"),
 au("d-ativados", "After activation, T cells change their <b>adhesion molecules</b>, stop homing to lymph nodes and patrol tissues with disturbed homeostasis, called immune {{c1::surveillance}}",
    G(1), D_, "Linfócitos T ativados e vigilância", "14", "central", NAO, EP, "Verde: lâmina 14 e transcrição.",
    duplicacao_ok="ganho: vigilância e troca de moléculas de adesão; a 22 cobra o destino do efetor",
    extra="- Endothelium at sites of disturbed homeostasis expresses the molecules activated cells now recognize"),
 au("d-fluidez", ORG("Structural features of the <b>immune system</b>:<br>- somatic, random generation of the repertoire<br>- random distribution among lymphoid organs<br>- continuous {{c1::recirculation}}<br>→ histological and functional {{c2::fluidity}}"),
    {1: Z, 2: Z}, D_, "Características: geração, distribuição, redistribuição, fluidez", "15", "central", NAO, EP, "Azul: lâmina 15.",
    extra="- Lymphocytes tend to recirculate through the kind of organ where they were activated (mucosa vs lymph node)<br>- Hence the timing and site of a response are never fully predictable"),
 # E — o sistema em ação (16; 24)
 au("e-paisagem", "<b>Lymph</b> carries the whole {{c1::molecular landscape}} of a tissue, not only the antigen, to the lymph node that drains it",
    {1: Z}, E_, "Paisagem molecular", "16", "central", NAO, EP, "Azul: lâminas 16 e 24 e transcrição.",
    extra="- Plasma leaking into injured tissue raises the pressure that pushes all this into the lymph"),
 sh(1792065578750, "verde", E_, "O estado do tecido decide resposta × tolerância", "16", "Verde: lâminas 16 e 24; viva na aula 08."),
 au("e-coexistem", "<b>Response and tolerance</b> are not exclusive, since every adaptive response mixes {{c1::effector}} and regulatory cells and the balance decides the outcome",
    {1: Z}, E_, "Resposta e tolerância simultâneas", "16", "central", NAO, EP, "Azul: transcrição (‘não é ou, é isso e aquilo’).",
    extra="- Tissue injury tips the balance toward response; without injury it tips toward tolerance"),
 au("e-vacina", "<b>Vaccination</b> works by raising, in advance, the {{c1::probability}} that an antigen meets its specific clonal receptor, so the next response starts faster",
    {1: Z}, E_, "Conexão: estatística do encontro e vacina", "17", "central", NAO, EP, "Azul: lâmina 17 e transcrição (‘muito da resposta imune é estatística’).",
    extra="- At the next alarm, specific cells and antibodies already join the innate response"),
 # F — órgãos linfoides secundários (17–20)
 sh(1792044192107, "verde", F_, "APCs profissionais", "18", "Verde: lâmina 18; organizador vivo na aula 20."),
 sh(1791625426408, "verde", F_, "DC ativa o T naive", "18", "Verde: lâmina 18; viva na aula 20."),
 sh(1791625427531, "azul", F_, "Apresentação cruzada", "18", "Azul: lâmina 18 (exemplo da hepatite B na transcrição); viva na aula 20."),
 au("f-b-seletiva", "<b>B cells</b> present antigen selectively, since their {{c1::BCR}} captures its specific antigen even at concentrations far too low for phagocytes",
    {1: Z}, F_, "Apresentação seletiva pelo linfócito B", "18", "central", NAO, EP, "Azul: lâmina 18 e transcrição (afinidade ~10.000× maior).",
    extra="- This couples antibody production to help from T cells that see the same antigen"),
 au("f-aferencia", ORG("Where information reaches each <b>secondary organ</b>:<br>- lymph node: afferent {{c1::lymph}} from tissues<br>- spleen: {{c2::blood}}<br>- MALT: the lumen, through {{c3::M cells}} and dendritic cells"),
    G(1, 2, 3), F_, "Aferência de informação", "19", "central", NAO, EP, "Verde: lâmina 19 e transcrição.",
    extra="- Splenic responses deal with blood-borne threats, which spread faster<br>- Lymphocytes leave the lymph node through the efferent lymph, not the blood"),
 au("f-areas", ORG("Areas of <b>secondary lymphoid organs</b>:<br>- T-cell (thymus-dependent): {{c1::paracortex}} in the lymph node, periarteriolar sheath in the spleen<br>- B-cell (thymus-independent): {{c2::follicles}}, which form germinal centers"),
    G(1, 2), F_, "Áreas timo-dependentes e independentes", "20", "central", NAO, EP, "Verde: lâmina 20 e transcrição (timectomia esvazia as áreas T).",
    extra="- An enlarged paracortex means T-cell expansion; germinal centers mean B-cell expansion and antibody"),
 ak("ak-pals", 1486945322037, G(1), F_, "T no baço: PALS", "20", "Verde: HY 1; lâmina 20."),
 sh(1791625425757, "verde", F_, "Folículos secundários com centro germinativo", "20", "Verde: lâmina 20; viva nas aulas 45 e 49."),
 au("f-fdc", "<b>Follicular dendritic cells</b> do not present antigen to T cells but hold intact antigen, often bound to antibody, for {{c1::B cells}}, helping keep memory for years",
    G(1), F_, "Célula dendrítica folicular", "20", "central", NAO, EP, "Verde: lâmina 20 e transcrição (‘nome que confunde muito’).",
    extra="- Different origin and function from the dendritic cell that presents to T cells"),
 # H — eferência (21)
 au("h-plasmocitos", "<b>Plasma cells</b> settle in lymph node medullary cords, splenic red pulp and above all the {{c1::bone marrow}}, which is why myeloma arises there",
    G(1), H_, "Destino dos plasmócitos", "21", "central", NAO, EP, "Verde: lâmina 21 e transcrição.",
    extra="- The bone marrow is thus a primary and also a secondary lymphoid organ"),
 au("h-duas-semanas", "A full, measurable <b>adaptive response</b> takes about {{c1::two weeks}} after the antigen reaches the lymphoid organ",
    G(1), H_, "Tempo da resposta adquirida", "21", "central", NAO, EP, "Verde: transcrição (expansão clonal ~2 semanas; linfonodo ‘fecha a porta’).",
    extra="- Before that, antibodies may be undetectable: the immunological window of HIV testing"),
 sh(1791983685631, "azul", H_, "Órgãos linfoides terciários", "21", "Azul: prova 2024 P1 (folículos na tireoidite de Hashimoto); viva na aula 62."),
 # I — endereçamento (22–23)
 au("i-adesao", ORG("<b>Adhesion molecule</b> families that address leukocytes:<br>- {{c1::selectins}}: bind carbohydrates, first contact<br>- {{c2::integrins}}: leukocyte β2 (CD18)<br>- Ig superfamily: ICAM, VCAM, MAdCAM<br>- mucin-like: CD34, GlyCAM"),
    {1: Z, 2: Z}, I_, "Famílias de moléculas de adesão", "22", "central", NAO, EP, "Azul: lâmina 22 e transcrição (objetivo 4).",
    extra="- They engage in sequence: selectins first, then integrins and their Ig-superfamily ligands"),
 au("i-quimiotaticas", "Besides chemokines, <b>leukocytes</b> migrate toward complement fragments C3a and C5a and lipid mediators such as {{c1::leukotrienes}}",
    {1: R}, I_, "Moléculas quimiotáticas", "23", "lateral", NAO, EP, "Rosa: lâmina 23 (as famílias de quimiocinas são da aula 08).",
    extra="- Adhesion molecules make cells stick; chemotactic molecules tell them where to go"),
]
SEM_IMAGEM = "princípio de organização sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"ak-secundarios": "- Lymph nodes, spleen and MALT gather antigen, APCs and naive lymphocytes in one place",
         "ak-pals": "- The PALS and follicles form the white pulp"}
for c in CARDS:
    if VERSO.get(c["key"]) and c["kind"] == "text":
        c["extra_add"] = VERSO[c["key"]]
DUPLICACAO = {}
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Descrever órgãos linfoides primários e secundários e suas funções, a recirculação e o endereçamento dos linfócitos (adesão e quimiotaxia), e como o sistema decide entre resposta e tolerância a partir da paisagem molecular do tecido.",
 "centrais": [
   ("papel", "a-exterior", "a-antigeno"),
   ("em ação", "b-alarmes", "sh-1792029611637", "sh-1792054600579", "sh-1792055399868"),
   ("primários", "c-primarios", "c-selecao-timo", "sh-1791625434632", "c-medula-menos-estrita"),
   ("recirculação", "d-secundarios", "ak-secundarios", "d-naive", "sh-1791625425583", "d-por-que", "d-ativados", "d-fluidez"),
   ("resposta × tolerância", "e-paisagem", "sh-1792065578750", "e-coexistem", "e-vacina"),
   ("secundários", "sh-1792044192107", "sh-1791625426408", "sh-1791625427531", "f-b-seletiva", "f-aferencia", "f-areas", "ak-pals", "sh-1791625425757", "f-fdc"),
   ("eferência", "h-plasmocitos", "h-duas-semanas", "sh-1791983685631"),
   ("endereçamento", "i-adesao", "i-quimiotaticas"),
 ],
 "exemplos": ["vírus da hepatite B (apresentação cruzada)", "janela imunológica do HIV", "mieloma na medula", "COVID-19 (predomínio T × B)"],
 "outras_aulas": [("PRR e alarmes moleculares", "08"), ("MHC e APCs", "20"), ("efetores", "22"), ("seleção tímica e Treg", "45"), ("células B", "49")],
}
