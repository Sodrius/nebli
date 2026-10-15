# Especificação curada — Micoses subcutâneas (UC03 P3, Microbiologia; Prof. Benedito Corrêa, 2026; 42 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-mb48-20261010a"
SHORT = "mb48"
LESSON = "2026-uc03-microbiologia-48-micoses-subcutaneas"
DECK = "NEBLI::UC03::P3::Microbiologia::Micoses subcutâneas"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-02) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {"mb48-sporothrix-margarida.png": "img/mb48-sporothrix-margarida.png", "mb48-lobo-cadeias.png": "img/mb48-lobo-cadeias.png"}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 14 consultas, 10/10): ")
EXCLUIDOS = [
 (1500055049050, "hifas como roseira: repete 1500054938635"),
 (1500055726473, "granulomas na biópsia: detalhe não citado na aula"),
 (1500416255031, "Actinomyces e Nocardia ramificados: o contraste da aula é anaeróbio × aeróbio"),
 (1510011869046, "micetoma cervicofacial por Actinomyces: bacteriologia fora da aula"),
]
FORA_DO_RECORTE = ["micoses sistêmicas (aula seguinte)", "bacteriologia de Actinomyces e Nocardia além do contraste anaeróbio × aeróbio", "feo-hifomicose (só no livro)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_ = ("A-conceito", "B-esporotricose", "C-cromomicose", "D-micetomas", "E-jorge-lobo")
CARDS = [
 # ---------- A. Conceito e classificação (slides 2–3) ----------
 au("subcut-def", "Subcutaneous mycoses begin when saprobic fungi from soil or plants are {{c1::implanted}} through a skin wound", {1: V}, A_,
    "Micose subcutânea = implantação traumática", "2; transcrição; Trabulsi cap. 68", "central", "sem card de definição de micose subcutânea (consulta 'subcutaneous mycos*').",
    [1500054719314, 1500055544157], "Verde: conceito que abre a aula.", extra="- They usually stay near the inoculation site; some spread along lymphatics"),
 # ---------- B. Esporotricose (slides 6–25) ----------
 au("gatos", "In Brazil's sporotrichosis epidemic, which began in Rio de Janeiro, the fungus is spread to humans mainly by {{c1::cats}}", {1: V}, B_,
    "Epidemia brasileira por gatos", "6, 8, 20–21; transcrição; Trabulsi", "central", "AnKing só tem a via vegetal (espinho).", [1500054719314, 1500054558583],
    "Verde: transmissão zoonótica, centro da epidemiologia atual.", extra="- Cats get severe disease and transmit by scratches and secretions"),
 au("brasiliensis", "{{c1::Sporothrix brasiliensis}}, recognized only with molecular methods, is the most frequent species of the S. schenckii complex in Brazil", {1: Z}, B_,
    "S. brasiliensis no complexo S. schenckii", "7; transcrição", "central", "AnKing só cita S. schenckii.", [1500054558583, 1500054777136], "Azul: lâmina 7."),
 ak("espinho", 1500054719314, {1: V, 2: V}, B_, "Inoculação por espinho de rosa e plantas", 8, "Verdes: HY; reservatório solo/vegetais e via direta (lâminas 8 e 10)."),
 au("ocupacional", "Gardeners, farmers and hunters are at risk because sporotrichosis is an {{c1::occupational}} mycosis", {1: R}, B_,
    "Micose ocupacional", "9; Trabulsi", "lateral", "sem card nos acervos.", [1500054719314, 1500054558583], "Rosa: lâmina 9."),
 ak("dimorfico", 1500054777136, {1: V}, B_, "Sporothrix é dimórfico", 11, "Verde: HY; lâmina 11."),
 ak("hifas-25", 1500054938635, {1: Z}, B_, "Hifas a 25 °C", 11, "Azul: fase de bolor a 25 °C (lâmina 11)."),
 au("linfocutanea", "The {{c1::lymphocutaneous}} form causes 80–90% of sporotrichosis cases", {1: Z}, B_,
    "Linfocutânea é a mais comum", "11, 15–16; transcrição; monitoria; Trabulsi", "central", "AnKing descreve a disseminação linfática, não a frequência da forma.",
    [1500055367426, 1500056181436], "Azul: formas clínicas da lâmina 11."),
 au("fixa", "Unlike the lymphocutaneous form, fixed cutaneous sporotrichosis shows no {{c1::nodular lymphangitis}}", {1: Z}, B_,
    "Forma cutânea fixa", "11, 13–14, 17", "central", "sem card nos acervos.", [1500055544157, 1500055367426], "Azul: lâminas 13–14 e 17."),
 au("disseminada", "Disseminated sporotrichosis occurs mainly in {{c1::immunocompromised}} patients, such as those with AIDS", {1: Z}, B_,
    "Forma disseminada", "11 e 19; transcrição; Trabulsi", "central", "sem card nos acervos.", [1499968803765, 1500055367426], "Azul: lâmina 19."),
 ak("lesao-inicial", 1500055544157, {1: V}, B_, "Pústula/úlcera inicial e nódulos", 12, "Verde: HY; lesão inicial (lâmina 12)."),
 ak("linfangite", 1500056181436, {1: V, 3: Z}, B_, "Linfangite ascendente e levedura em charuto", 15, "Verde c1 (HY), azul c3; lâminas 15–18."),
 ak("ascendente", 1500055367426, {1: V, 2: Z}, B_, "Disseminação ascendente pelo linfático", 15, "Verde c1 (HY), azul c2; forma linfocutânea."),
 ak("charuto", 1500055361936, {1: Z, 2: Z}, B_, "Levedura em charuto ao microscópio", 22, "Azuis: exame direto da lâmina 22."),
 au("margarida", "At 25ºC, Sporothrix conidia cluster at the tip of the conidiophore in a {{c1::daisy}}-like pattern", {1: Z}, B_,
    "Conídios em margarida", "23–24; transcrição; Trabulsi fig. 68.1", "central", "AnKing compara as hifas à roseira, não os conídios em flor.", [1500054938635, 1500055049050],
    "Azul: lâmina 24.", extra="- The colony is membranous and darkens with time<br><img src=\"mb48-sporothrix-margarida.png\" width=\"300\">"),
 ak("levedura-tecido", 1500151811249, {1: V}, B_, "Levedura em tecido, bolor em cultura", 25, "Verde: HY; fase leveduriforme (lâmina 25)."),
 au("reversao", "In the lab, converting Sporothrix from mold to yeast at {{c1::37}}ºC confirms the identification", {1: Z}, B_,
    "Reversão térmica confirma Sporothrix", "25; transcrição; Trabulsi", "central", "sem card nos acervos.", [1500054777136, 1500055687581], "Azul: diagnóstico laboratorial."),
 ak("cultura", 1500055687581, {1: Z}, B_, "Diagnóstico confirmado por cultura", 25, "Azul: o exame direto falha com frequência (transcrição)."),
 ak("itraconazol", 1500055896708, {1: Z}, B_, "Itraconazol na esporotricose", 25, "Verde: HY; tratamento na monitoria. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("ki", 1500056127804, {1: R}, B_, "Iodeto de potássio na esporotricose", 25, "Verde: HY; tratamento clássico (monitoria, Trabulsi). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 # ---------- C. Cromomicose (slides 26–32) ----------
 au("cromo-agentes", "Chromoblastomycosis is caused by pigmented (dematiaceous) molds, mainly {{c1::Fonsecaea pedrosoi}} in Brazil", {1: Z}, C_,
    "Agentes da cromomicose", "26 e 30; monitoria; Trabulsi", "central", "consultas chromoblastomycosis/Fonsecaea sem card.", [1500054558583, 1500054777136],
    "Azul: lâmina 26.", extra="- Other genera: Cladophialophora, Phialophora, Rhinocladiella"),
 au("cromo-ocupacional", "Chromoblastomycosis usually affects the {{c1::lower limbs}}", {1: Z}, C_,
    "Epidemiologia e local da cromomicose", "26; transcrição; Trabulsi", "central", "sem card nos acervos.", [1500054719314, 1500055544157], "Azul: lâmina 26."),
 au("couve-flor", "Chromoblastomycosis grows slowly as warty nodules that merge into {{c1::cauliflower}}-like lesions", {1: Z}, C_,
    "Lesões verrucosas em couve-flor", "27; transcrição; monitoria; Trabulsi", "central", "sem card nos acervos.", [1500055544157, 1500055367426], "Azul: lâmina 27."),
 au("corpos-escleroticos", "The diagnostic finding of chromoblastomycosis is brown, thick-walled {{c1::sclerotic bodies}} in pus, crusts or tissue", {1: V}, C_,
    "Corpos escleróticos", "29 e 32; transcrição", "central", "consulta 'sclerotic bodies' sem card.", [1500055361936, 1500050268188],
    "Verde: achado que, com a clínica, define o diagnóstico.", extra="- Also called muriform cells or copper pennies; they divide by septation"),
 au("conidiacao", "{{c1::Fonsecaea pedrosoi}} is notable for showing three different conidiation types in culture", {1: R}, C_,
    "Três tipos de conidiação", "31; transcrição; monitoria", "lateral", "sem card nos acervos.", [1500054938635, 1500052968870], "Rosa: lâmina 31."),
 # ---------- D. Micetomas (slides 33–37) ----------
 au("micetoma-tipos", "Mycetomas are caused either by fungi or by filamentous {{c1::bacteria}} such as Actinomyces and Nocardia", {1: Z}, D_,
    "Micetoma fúngico × bacteriano", "34; transcrição", "central", "consulta 'mycetoma' só com o micetoma cervicofacial por Actinomyces.", [1510011869046, 1506204527586],
    "Azul: lâmina 34."),
 ak("actinomyces", 1500498780974, {1: Z, 2: Z}, D_, "Actinomyces é anaeróbio obrigatório", 34, "Verdes: HY; actinomicose = bactérias anaeróbias (lâmina 34). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("nocardia", 1506203795560, {1: Z}, D_, "Nocardia é aeróbio obrigatório", 34, "Verde: HY; nocardiose = bactérias aeróbias (lâmina 34). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 au("triade", "A mycetoma is defined by the triad of tumor-like swelling, draining sinuses and {{c1::grains}}", {1: V}, D_,
    "Tríade do micetoma", "33, 35–36; transcrição", "central", "sem card da tríade nos acervos.", [1510012018998, 1510011869046],
    "Verde: lâmina 35.", extra="- Grains are clumps of hyphae, seen on direct exam or biopsy"),
 au("madurella", "{{c1::Madurella grisea}}, the main eumycetoma agent in Brazil, forms black grains", {1: R}, D_,
    "Madurella e grãos negros", "3 e 36; transcrição", "lateral", "consulta 'Madurella' sem card.", [1510011869046, 1500420421531], "Rosa: agente da lâmina 3."),
 # ---------- E. Doença de Jorge Lobo (slides 38–42) ----------
 au("lacazia", "Jorge Lobo disease (lobomycosis) is caused by the fungus {{c1::Lacazia loboi}}", {1: Z}, E_,
    "Agente da doença de Jorge Lobo", "38; transcrição", "central", "consultas lobomycosis/Lacazia sem card.", [1500054558583, 1500055361936], "Azul: lâmina 38."),
 au("lobo-epi", "Lobomycosis mostly affects men working in the Amazon rainforest, such as rubber tappers, and also infects {{c1::dolphins}}", {1: R}, E_,
    "Epidemiologia de Jorge Lobo", "39; transcrição", "lateral", "sem card nos acervos.", [1500054719314, 1500054558583], "Rosa: lâmina 39."),
 au("queloide", "Jorge Lobo disease produces {{c1::keloid}}-like skin nodules", {1: Z}, E_,
    "Lesões queloidianas", "40; transcrição", "central", "sem card nos acervos.", [1500055544157, 1500055367426], "Azul: lâmina 40."),
 au("lobo-cultura", "Lacazia loboi has never been grown in {{c1::culture}}", {1: Z}, E_,
    "Jorge Lobo não se cultiva", "41–42; transcrição", "central", "sem card nos acervos.", [1500055687581, 1500055361936],
    "Azul: lâmina 41.", extra="- Diagnosis: direct exam and biopsy show round, thick-walled cells in chains"),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 "brasiliensis": "- Other complex members: S. schenckii, S. globosa, S. mexicana",
 "ocupacional": "- Most cases: men aged 20–50 handling plants or soil",
 "linfocutanea": "- Nodules ascend along the lymphatic chain from the inoculation site",
 "fixa": "- The lesion stays at the inoculation site, e.g. face or finger",
 "disseminada": "- Severe cases are treated with amphotericin B",
 "reversao": "- Look-alike environmental molds do not convert to yeast",
 "couve-flor": "- Growth is slow, over years",
 "conidiacao": "- Phialides, acrogenous chains and acropleurogenous conidia",
 "cromo-ocupacional": "- Occupational mycosis of tropical regions (soil and wood)",
 "micetoma-tipos": "- Fungal = eumycetoma (maduromycosis); bacterial = actinomycetoma",
 "madurella": "- Grains are seen on direct exam or biopsy",
 "lacazia": "- First described by Jorge Lobo in Recife, in a patient from the Amazon",
 "lobo-epi": "- Mostly men aged 20–45",
 "queloide": "- Often on the ear",
 "levedura-tecido": "- Lab culture at 37ºC also gives the yeast phase",
 "actinomyces": "- With Nocardia, a bacterial cause of mycetoma (actinomycetoma)",
}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
DUPLICACAO = {"fixa": "ganho: a resposta repete linfangite, mas a pergunta é a ausência dela que define a forma fixa (lâminas 13–14 × 15)"}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]


# ---- Revisão do Opus (11/10/2026, REVISAO-OPUS.md; F-20261011-CLAUDE-04) ----
import re as _re
def _c(key):
    return next(c for c in CARDS if c["key"] == key)


def _cor(key, cor):
    c = _c(key); c["flags"] = {n: cor for n in c["flags"]}
    if c["kind"] == "text": c["clinica_lateral"] = True


def _ak(key, text=None, extra=None, flags=None, **kw):
    c = _c(key); fo = c.setdefault("fields_override", {})
    if text: fo["Text"] = text
    if extra is not None: c.pop("extra_add", None); fo["Extra"] = extra
    if flags: c["flags"] = flags
    c.update(kw)


def _au(key, text=None, extra=None, cor=None):
    c = _c(key)
    if text:
        c["text"] = text
        c["flags"] = {int(n): (cor or list(c["flags"].values())[0]) for n in sorted({int(x) for x in _re.findall(r"\{\{c(\d+)::", text)})}
    if extra is not None: c["extra"] = extra
    if cor and not text: c["flags"] = {k: cor for k in c["flags"]}


_ESP = [c["src"] for c in CARDS if c["kind"] == "text"][:2]


def _novo(key, text, cor, ref, alvo, slide, autoria, extra=""):
    n = sorted({int(x) for x in _re.findall(r"\{\{c(\d+)::", text)})
    CARDS.append(au(key, text, {i: cor for i in n}, _c(ref)["bloco"], alvo, slide, autoria, "sem card nos acervos (revisão do Opus).", _ESP, "Revisão do Opus.", extra=extra))
_ak("levedura-tecido", text="<b>Sporothrix</b> is a thermally dimorphic fungus, a cigar-shaped budding {{c1::yeast}} in tissue and a mold on plants and soil", extra="- In Brazil the main species is S. brasiliensis")
_au("lacazia", extra="- Now named Paracoccidioides loboi (synonyms Lacazia loboi, Loboa loboi)")
_au("lobo-epi", extra="- In dolphins the agent is now called P. ceti")
_ak("actinomyces", extra="- Actinomyces is an anaerobic bacterium, unlike the aerobic Nocardia")
for k in ("hifas-25", "actinomyces", "nocardia"): _cor(k, R)
_cor("brasiliensis", V); _cor("madurella", Z)
CARDS[:] = [c for c in CARDS if c["key"] not in ("linfangite", "ascendente", "dimorfico")]
_novo("pulmonar-primaria", "Inhaled <b>Sporothrix</b> conidia can rarely cause {{c1::primary pulmonary}} sporotrichosis", R, "brasiliensis", "Forma pulmonar primária", "11", "lateral", "- Disseminated forms occur in AIDS, diabetes and chronic kidney disease")
_novo("hialino", "Unlike the agents of chromoblastomycosis, <b>Sporothrix</b> hyphae are {{c1::hyaline}} (not pigmented)", Z, "brasiliensis", "Sporothrix é hialino", "16; transcrição", "central")
_novo("grocott", "In <b>sporotrichosis</b> biopsies, the scarce yeasts are best seen with Gomori-{{c1::Grocott}} silver stain", R, "brasiliensis", "Grocott na esporotricose", "22; transcrição", "lateral")
_novo("micetoma-pe", "<b>Eumycetoma</b> (maduromycosis) most often affects the {{c1::foot}}", Z, "madurella", "Micetoma no pé", "33, 37", "central", "- Hence the name Madura foot")
_novo("grao-hifas", "The <b>grains</b> of eumycetoma are compact clumps of fungal {{c1::hyphae}}", Z, "madurella", "Grão de hifas", "36", "central", "- Seen on direct exam of sinus pus or on histopathology")
_novo("grao-branco", "<b>Pseudallescheria boydii</b> and Acremonium form {{c1::white}} grains, whereas Madurella forms black grains", R, "madurella", "Cor do grão", "36; transcrição", "lateral")
_novo("lobo-cadeias", "Direct exam in <b>lobomycosis</b> shows round, thick-walled, refractile cells in {{c1::chains}}", Z, "lacazia", "Células em cadeia na lobomicose", "41", "central", extra="- Left: fresh direct exam; right: histology with silver stain<br><img src=\"mb48-lobo-cadeias.png\" width=\"460\">")
_novo("gato-levedura", "Cat-transmitted <b>sporotrichosis</b> progresses faster because the fungus arrives already in the {{c1::yeast}} form", R, "brasiliensis", "Transmissão felina já em levedura", "22; monitoria", "lateral")

# negrito aplicado ao vivo em 11/10 (correcao-comentarios-2026-10-11/negrito.json), trazido à spec
_NEGRITO_VIVO = {
"subcut-def": "<b>Subcutaneous mycoses</b> begin when <b>saprobic fungi</b> from soil or plants are {{c1::implanted}} through a <b>skin wound</b>",
"gatos": "In Brazil's <b>sporotrichosis epidemic</b>, which began in <b>Rio de Janeiro</b>, the fungus is spread to <b>humans</b> mainly by {{c1::cats}}",
"brasiliensis": "{{c1::Sporothrix brasiliensis}}, recognized only with <b>molecular methods</b>, is the most frequent species of the <b>S. schenckii complex</b> in Brazil",
"ocupacional": "<b>Gardeners, farmers and hunters</b> are at risk because <b>sporotrichosis</b> is an {{c1::occupational}} mycosis",
"linfocutanea": "The {{c1::lymphocutaneous}} form causes <b>80–90% of sporotrichosis cases</b>",
"fixa": "Unlike the lymphocutaneous form, <b>fixed cutaneous sporotrichosis</b> shows no {{c1::nodular lymphangitis}}",
"disseminada": "<b>Disseminated sporotrichosis</b> occurs mainly in {{c1::immunocompromised}} patients, such as those with <b>AIDS</b>",
"margarida": "At <b>25ºC</b>, Sporothrix conidia cluster at the tip of the <b>conidiophore</b> in a {{c1::daisy}}-like pattern",
"reversao": "In the lab, converting Sporothrix from <b>mold to yeast</b> at {{c1::37}}ºC confirms the <b>identification</b>",
"cromo-agentes": "Chromoblastomycosis is caused by <b>pigmented (dematiaceous) molds</b>, mainly {{c1::Fonsecaea pedrosoi}} in <b>Brazil</b>",
"cromo-ocupacional": "<b>Chromoblastomycosis</b> usually affects the {{c1::lower limbs}}",
"couve-flor": "Chromoblastomycosis grows slowly as <b>warty nodules</b> that merge into {{c1::cauliflower}}-like <b>lesions</b>",
"corpos-escleroticos": "The diagnostic finding of chromoblastomycosis is <b>brown, thick-walled</b> {{c1::sclerotic bodies}} in <b>pus, crusts or tissue</b>",
"conidiacao": "{{c1::Fonsecaea pedrosoi}} is notable for showing <b>three different conidiation types</b> in <b>culture</b>",
"micetoma-tipos": "<b>Mycetomas</b> are caused either by fungi or by filamentous {{c1::bacteria}} such as <b>Actinomyces and Nocardia</b>",
"triade": "A <b>mycetoma</b> is defined by the triad of <b>tumor-like swelling, draining sinuses</b> and {{c1::grains}}",
"madurella": "{{c1::Madurella grisea}}, the main <b>eumycetoma</b> agent in Brazil, forms <b>black grains</b>",
"lacazia": "<b>Jorge Lobo disease (lobomycosis)</b> is caused by the <b>fungus</b> {{c1::Lacazia loboi}}",
"lobo-epi": "<b>Lobomycosis</b> mostly affects men working in the <b>Amazon rainforest</b>, such as <b>rubber tappers</b>, and also infects {{c1::dolphins}}",
"queloide": "<b>Jorge Lobo disease</b> produces {{c1::keloid}}-like <b>skin nodules</b>",
"lobo-cultura": "<b>Lacazia loboi</b> has never been grown in {{c1::culture}}"
}
for _k, _t in _NEGRITO_VIVO.items():
    _c(_k)["text"] = _t
for _k, _x in {"hialino": "- Chromoblastomycosis agents (Fonsecaea) are dematiaceous, with dark melanin walls",
               "grocott": "- Yeasts are scarce in human lesions, unlike in cats",
               "gato-levedura": "- Cat lesions are rich in yeasts, transmitted by scratches and bites",
               "grao-branco": "- Grain color hints at the agent before culture",
               "lobo-cadeias": "- The fungus does not grow in culture"}.items():
    _c(_k)["extra"] = _x
_c("gato-levedura")["duplicacao_ok"] = "ganho: por que a transmissão felina evolui mais rápido (forma de levedura), não só que o gato transmite"

# ---- Revisão por prova 15/10 (F-20261015-CLAUDE-03): organizadores de mapa mental, em tópicos ----
ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
_MOT = "Revisão 15/10: organizador de mapa mental pedido por Davi."
def _sl(c): return int(_re.search(r"\d+", str(c["evid"])).group())
def _no_slide(n, card):
    i = next(i for i, c in enumerate(CARDS) if _sl(c) >= n); CARDS.insert(i, card)
_no_slide(3, au("org-subcutaneas", ORG("Main <b>subcutaneous mycoses</b> (agent):<br>- {{c1::sporotrichosis}} (Sporothrix brasiliensis)<br>- {{c2::chromoblastomycosis}} (Fonsecaea pedrosoi)<br>- {{c3::eumycetoma}} (Madurella grisea)<br>- {{c4::Jorge Lobo disease}} (Lacazia loboi)"),
    {1: V, 2: V, 3: V, 4: V}, A_, "Principais micoses subcutâneas", "3", "central", "nenhum card dos acervos.", _ESP, "Verde: lâmina 3. " + _MOT,
    extra="- All are implanted through the skin by minor trauma with soil or plants", duplicacao_ok="organizador; cada doença tem seus cards"))
_no_slide(11, au("org-formas-esporo", ORG("Forms of <b>sporotrichosis</b>:<br>- {{c1::lymphocutaneous}}: nodules along lymphatics (most common)<br>- {{c2::fixed cutaneous}}: stays at the wound<br>- {{c3::disseminated}}: immunocompromised<br>- pulmonary: inhaled conidia (rare)"),
    {1: V, 2: Z, 3: Z}, B_, "Formas clínicas da esporotricose", "11", "central", "nenhum card dos acervos.", _ESP, "Verde/azul: lâmina 11 (resumo das formas). " + _MOT,
    duplicacao_ok="organizador; cada forma tem card próprio"))

# textos vivos (correções de comentários de Davi feitas ao vivo) trazidos à spec, 15/10
_c('cromo-ocupacional')["text"] = "Because the fungus is implanted by minor trauma from soil and plants, <b>chromoblastomycosis</b> mostly affects the {{c1::lower limbs}}"
_c('cromo-ocupacional')["extra"] = "- Typical patients are rural workers who walk barefoot or handle wood and thorny plants"
_c('cromo-ocupacional')["flags"] = {n: list(_c('cromo-ocupacional')["flags"].values())[0] for n in [1]}
_c('subcut-def')["text"] = "<b>Subcutaneous mycoses</b> start when soil or plant fungi are pushed through the skin by a minor injury, called traumatic {{c1::implantation}}"
_c('subcut-def')["extra"] = "- The fungus then grows in the dermis and subcutis near the wound; some spread along lymphatics"
_c('subcut-def')["flags"] = {n: list(_c('subcut-def')["flags"].values())[0] for n in [1]}
for _c_ in CARDS:
    if _c_["key"] == "org-formas-esporo": _c_["extra"] = "- The host's immunity decides how far the fungus spreads from the inoculation site"
    if _c_["key"] == "org-subcutaneas": _c_["extra"] = "- All are implanted through the skin by minor trauma with soil or plants"

# textos vivos (correções de comentários de Davi feitas ao vivo) trazidos à spec, 15/10
_c('subcut-def')["text"] = "{{c1::Subcutaneous}}<b>&nbsp;mycoses</b> start when soil or plant fungi are pushed through the skin by a minor injury, called traumatic implantation"
_c('subcut-def')["extra"] = "- The fungus then grows in the dermis and subcutis near the wound; some spread along lymphatics"
_c('subcut-def')["flags"] = {n: list(_c('subcut-def')["flags"].values())[0] for n in [1]}

IMAGENS_VISTAS = {"mb48-sporothrix-margarida.png": "Lâmina 24 (figura sem o texto): conídios em margarida na ponta do conidióforo, cultivo a 25 °C; no Extra (pedido de Davi 15/10).", "mb48-lobo-cadeias.png": "Lâmina 42 recortada sem o título: exame direto a fresco e histologia com células redondas de parede espessa em cadeia; no Extra (pedido de Davi 15/10)."}
