# Especificação curada — Prática 1: morfologia e técnicas de assepsia e cultivo (UC03 P2, Microbiologia; roteiro de 36 pp., T/P1–T/P2). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-mb28-20261010a"
SHORT = "mb28"
LESSON = "2026-uc03-microbiologia-28-pratica-1"
DECK = "NEBLI::UC03::P2::Microbiologia::Prática 1 — morfologia e assepsia"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-04) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 9 consultas); notas NEBLI de Morfologia e Fisiologia bacteriana conferidas para associar, 10/10: ")
EXCLUIDOS = []  # (nid, motivo) de candidatos lidos e recusados
FORA_DO_RECORTE = ["T/P3–T/P5 do roteiro (outras práticas)", "clínica das bactérias citadas como exemplo"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_ = ("A-biosseguranca", "B-morfologia", "C-coloracao", "D-meios")
CARDS = [
 # ---------- A. Biossegurança (p. 3) ----------
 au("risco-classes", "Biosafety risk class {{c1::4}} means high risk for both the individual and the community", {1: Z}, A_,
    "Classes de risco biológico", "3", "central", "consultas biosafety/BSL sem card.", [1402177515133, 1500490858110],
    "Azul: norma de segurança da prática.", extra="- Class 1: rarely pathogenic; class 2: moderate individual risk, limited community spread"),
 au("epc", "Biosafety cabinets and emergency showers are examples of {{c1::collective}} protective equipment", {1: R}, A_,
    "EPI × EPC", "3", "lateral", "sem card nos acervos.", [1402177515133, 1500490858110], "Rosa: norma de segurança."),
 # ---------- B. Morfologia (p. 4) — notas de Morfologia (aula 26) ----------
 sh(1791576666442, "verde", B_, "Formas bacterianas", 4, "Verde: nota já existente de Morfologia."),
 sh(1791576666842, "azul", B_, "Estreptococos em cadeia", 4, "Azul: nota já existente de Morfologia."),
 sh(1791576667142, "azul", B_, "Estreptobacilos", 4, "Azul: nota já existente de Morfologia."),
 sh(1791576666993, "azul", B_, "Estafilococos em cacho", 4, "Azul: nota já existente de Morfologia."),
 au("sarcina", "Cocci that stay together in cubic packets after dividing are called {{c1::sarcinae}}", {1: R}, B_,
    "Sarcinas", "4", "lateral", "sem card nos acervos.", [1500420138936, 1500490858110], "Rosa: arranjo da p. 4."),
 sh(1791576667442, "azul", B_, "Espiroquetas × espirilos", 4, "Azul: nota já existente de Morfologia."),
 sh(1791576667293, "rosa", B_, "Vibrião em vírgula", 4, "Rosa: nota já existente de Morfologia."),
 # ---------- C. Colorações (pp. 5–7) ----------
 au("corante-basico", "Bacterial cells are negatively charged, so they bind {{c1::basic}} dyes such as crystal violet and safranin", {1: Z}, C_,
    "Corantes básicos", "5", "central", "sem card nos acervos.", [1500417256509, 1500418458789], "Azul: p. 5."),
 au("diferencial", "Unlike a simple stain, a {{c1::differential}} stain such as Gram or Ziehl-Neelsen sorts bacteria into groups", {1: Z}, C_,
    "Colorações simples × diferenciais", "5; prova 2023 P2 3.3", "prova", "sem card nos acervos.", [1500418458789, 1500417256509],
    "Azul: p. 5.", extra="- Special stains show spores, capsules or flagella"),
 au("mordente", "In the Gram stain, iodine (Lugol) acts as a {{c1::mordant}}, fixing crystal violet into a complex", {1: V}, C_,
    "Iodo como mordente", "5–6", "central", "consulta mordant sem card.", [1500417256509, 1500418458789],
    "Verde: passo-chave do Gram.", extra="- The complex stays trapped in thick peptidoglycan"),
 sh(1791576668792, "verde", C_, "Álcool descora Gram-negativas", 5, "Verde: nota já existente de Morfologia."),
 sh(1791576668942, "verde", C_, "Peptidoglicano retém o cristal violeta", 5, "Verde: nota já existente de Morfologia."),
 au("fixacao", "Passing a dried smear through a flame {{c1::fixes}} the bacteria so they are not washed off during staining", {1: R}, C_,
    "Fixação do esfregaço", "6", "lateral", "sem card nos acervos.", [1500417256509, 1500418458789], "Rosa: procedimento da p. 6."),
 au("contracorante", "The final Gram stain step is a {{c1::counterstain}} with basic fuchsin or safranin", {1: Z}, C_,
    "Contracorante", "6", "central", "sem card nos acervos.", [1500417256509, 1500401591194], "Azul: p. 6.",
    extra="- Order: crystal violet → iodine → alcohol → fuchsin"),
 sh(1791163024625, "azul", C_, "Roxo = Gram-positivo", 7, "Azul: nota já existente de Morfologia."),
 sh(1791163025158, "azul", C_, "Rosa = Gram-negativo", 7, "Azul: nota já existente de Morfologia."),
 # ---------- D. Meios e cultivo (pp. 8–15) — notas de Fisiologia (aula 27) ----------
 au("agar-2", "A solid medium has the same composition as its broth plus about 2% {{c1::agar}}", {1: Z}, D_,
    "Ágar a 2%", "8", "central", "sem card nos acervos.", [1500490858110, 1500491213487], "Azul: p. 8."),
 sh(1791647815469, "azul", D_, "Crescimento turva o caldo", 10, "Azul: nota de Fisiologia bacteriana (turvação)."),
 sh(1791647815594, "verde", D_, "Esgotamento → colônias isoladas", 9, "Verde: nota de Fisiologia bacteriana."),
 au("meio-minimo", "A {{c1::minimal}} medium contains only mineral salts and a carbon source such as glucose", {1: Z}, D_,
    "Meio mínimo", "11", "central", "sem card nos acervos.", [1500491274684, 1500490858110],
    "Azul: p. 11.", extra="- Complex media add protein hydrolysates for a wider range of bacteria"),
 au("mueller", "{{c1::Mueller-Hinton}} agar is the standard medium for antibiotic susceptibility testing", {1: Z}, D_,
    "Mueller-Hinton", "11", "central", "consulta Mueller-Hinton sem card.", [1500491213487, 1500490858110], "Azul: p. 11."),
 sh(1791647817820, "azul", D_, "Ágar sangue não seletivo", 11, "Azul: nota de Fisiologia bacteriana."),
 sh(1791647817944, "verde", D_, "β-hemólise", 11, "Verde: nota de Fisiologia bacteriana."),
 sh(1791647818070, "azul", D_, "α-hemólise", 11, "Azul: nota de Fisiologia bacteriana."),
 sh(1791647818194, "azul", D_, "γ-hemólise", 11, "Azul: nota de Fisiologia bacteriana."),
 au("hemolise-exemplos", "{{c1::Streptococcus pyogenes}} is the classic beta-hemolytic streptococcus", {1: Z}, D_,
    "Exemplos de hemólise", "11", "central", "consulta de hemólise só traz endocardite e clínica.", [1500492032825, 1500492267320],
    "Azul: exemplos da p. 11.", extra="- Alpha: S. pneumoniae and viridans streptococci; gamma: Enterococcus faecalis"),
 sh(1791647818320, "azul", D_, "Ágar chocolate", 12, "Azul: nota de Fisiologia bacteriana."),
 sh(1791647818444, "azul", D_, "Fatores X e V", 12, "Azul: nota de Fisiologia bacteriana."),
 ak("thayer-martin", 1402177515133, {1: V}, D_, "Thayer-Martin isola Neisseria", 12, "Verde: HY; p. 12."),
 ak("thayer-vanco", 1500494650205, {1: Z, 2: Z}, D_, "Vancomicina no Thayer-Martin", 12, "Azuis: composição da p. 12."),
 sh(1791647817219, "verde", D_, "MacConkey seleciona Gram-negativos", 12, "Verde: nota de Fisiologia bacteriana."),
 sh(1791647817444, "verde", D_, "MacConkey diferencia lactose", 12, "Verde: nota de Fisiologia bacteriana."),
 au("lac-negativo", "On MacConkey agar, lactose non-fermenters such as Salmonella and Shigella form {{c1::colorless}} colonies", {1: Z}, D_,
    "Lac-negativos incolores", "12", "central", "sem card nos acervos.", [1500496166406, 1402600814505], "Azul: p. 12."),
 au("manitol-sal", "Mannitol salt agar selects staphylococci with {{c1::7.5%}} NaCl", {1: Z}, D_,
    "Ágar manitol-sal", "13", "central", "AnKing cobra só a cor.", [1484871827392, 1484871933740], "Azul: p. 13."),
 ak("manitol-amarelo", 1484871827392, {1: V}, D_, "S. aureus amarelo no manitol-sal", 13, "Verde: p. 13."),
 au("cetrimida", "Cetrimide agar is selective for {{c1::Pseudomonas aeruginosa}}", {1: R}, D_,
    "Ágar cetrimida", "13", "lateral", "consulta cetrimide sem card.", [1506212759173, 1487642780676], "Rosa: p. 13."),
 sh(1791647816844, "azul", D_, "Meio seletivo", 14, "Azul: nota de Fisiologia bacteriana."),
 sh(1791647816720, "azul", D_, "Meio indicador", 15, "Azul: nota de Fisiologia bacteriana."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {'epc': '- PPE (gloves, gown, goggles, mask) protects the individual worker',
 'sarcina': '- The arrangement reflects the planes in which the cells divide',
 'corante-basico': '- Basic dyes carry the color on their positive ion',
 'fixacao': '- The smear is first air-dried',
 'agar-2': '- Agar is a seaweed polysaccharide that bacteria do not digest',
 'mueller': '- It is a complex (protein hydrolysate) medium',
 'lac-negativo': '- Lactose fermenters such as Escherichia coli form red-pink colonies',
 'manitol-sal': '- Phenol red shows mannitol fermentation',
 'cetrimida': '- It favors pyocyanin, the blue-green pigment; cetrimide is a detergent'}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
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
