# Especificação curada — Micoses sistêmicas (UC03 P3, Microbiologia; Prof. Benedito Corrêa; 63 + 81 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-mb50-20261010a"
SHORT = "mb50"
LESSON = "2026-uc03-microbiologia-50-micoses-sistemicas"
DECK = "NEBLI::UC03::P3::Microbiologia::Micoses sistêmicas"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-02) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 22 consultas), seções FirstAid de micoses sistêmicas e oportunistas (busca/tags-secao.txt), 10/10: ")
EXCLUIDOS = [
 (1499969725882, "Histoplasma no centro-oeste dos EUA: a aula não trata distribuição norte-americana"),
 (1499971579973, "vales do Mississippi/Ohio: idem"),
 (1499971032936, "disseminação em imunodeprimido: repete histo-sre"),
 (1500236922530, "tratamento sistêmico de Candida: fora da aula"),
 (1500245756888, "aglutinação em látex: não citada"),
]
FORA_DO_RECORTE = ["Blastomyces, Coccidioides, Aspergillus, Mucor (outras aulas ou fora da UC)", "tratamento detalhado de candidose e criptococose", "datas históricas"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_ = ("A-gerais", "B-paracoccidioidomicose", "C-histoplasmose", "D-candidose", "E-criptococose")
CARDS = [
 # ---------- A. Características gerais (slides 2–4) ----------
 au("sist-caracteristicas", "Systemic mycoses are acquired mainly by {{c1::inhaling}} fungi from soil or animal droppings", {1: V}, A_,
    "Características comuns das micoses sistêmicas", "2, 4, 66; monitoria; Trabulsi cap. 69", "central", "AnKing trata cada fungo isolado.",
    [1499976310064, 1499969788030], "Verde: abre a aula.", extra="- They also share a defined geographic distribution"),
 sh(1791557944155, "verde", A_, "Bolor no solo, levedura no corpo", 4, "Verde: nota já existente de Biologia dos fungos."),
 # ---------- B. Paracoccidioidomicose (slides 5–20, 67–92) ----------
 ak("pcm-america", 1499975610400, {1: V, 2: Z}, B_, "PCM restrita à América do Sul", 5, "Verde c1 (HY), azul c2; lâminas 5 e 73."),
 au("pcm-especies", "Paracoccidioidomycosis is caused by Paracoccidioides brasiliensis and P. {{c1::lutzii}}", {1: Z}, B_,
    "P. brasiliensis e P. lutzii", "6, 70", "central", "consulta Paracoccidioid* sem P. lutzii.", [1499975610400, 1499975827249], "Azul: lâminas 6 e 70."),
 ak("pcm-inalacao", 1499976310064, {1: V}, B_, "PCM por inalação", 7, "Verde: HY; lâmina 7."),
 au("pcm-cafe", "Paracoccidioides was first isolated from the soil of a {{c1::coffee}} plantation", {1: R}, B_,
    "Solo de cafezal", "8, 71", "lateral", "sem card nos acervos.", [1499976310064, 1499975610400],
    "Rosa: lâmina 8.", extra="- Countries with coffee-growing tradition have the highest incidence"),
 au("pcm-tatu", "The {{c1::armadillo}} is a suspected natural reservoir of Paracoccidioides", {1: Z}, B_,
    "Tatu como reservatório", "8, 71; Trabulsi", "central", "sem card nos acervos.", [1499976310064, 1499975610400], "Azul: lâmina 8."),
 au("pcm-homem", "Paracoccidioidomycosis affects men about {{c1::15}} times more often than women", {1: Z}, B_,
    "Predomínio masculino 15:1", "8, 72; Trabulsi", "central", "sem card nos acervos.", [1499976310064, 1499975610400],
    "Azul: lâmina 72.", extra="- Mostly agricultural workers over 30"),
 au("pcm-estrogenio", "In women, {{c1::17-β-estradiol}} blocks the mycelium-to-yeast transition that Paracoccidioides needs to cause disease", {1: V}, B_,
    "Estrógeno protege", "8, 72; monitoria; Trabulsi", "central", "sem card nos acervos.", [1499976133630, 1499976310064],
    "Verde: explica o 15:1.", extra="- The mycelium is the infective form; the yeast is the parasitic form"),
 au("pcm-mortalidade", "In Brazil, paracoccidioidomycosis was the {{c1::8th}} cause of death among infectious and parasitic diseases (1980–1995)", {1: R}, B_,
    "Mortalidade da PCM", "9, 74", "lateral", "sem card nos acervos.", [1499975610400, 1499976310064], "Rosa: lâmina 9."),
 au("pcm-cronica", "The {{c1::chronic}} adult form causes about 90% of paracoccidioidomycosis cases", {1: V}, B_,
    "Forma crônica do adulto", "10, 76; Trabulsi", "central", "sem card das formas clínicas.", [1499976619643, 1499976536055],
    "Verde: lâmina 10.", extra="- Mostly men aged 30–40; it may take years to appear"),
 au("pcm-juvenil", "The acute juvenile form causes only {{c1::3–5%}} of paracoccidioidomycosis cases but is the most severe", {1: Z}, B_,
    "Forma aguda juvenil", "10, 76; Trabulsi", "central", "sem card nos acervos.", [1499976355327, 1499976619643],
    "Azul: lâmina 10.", extra="- Young patients; rapid spread through lymph nodes"),
 ak("pcm-linfonodos", 1499976355327, {1: Z, 2: Z}, B_, "Linfadenopatia disseminada", 10, "Verde c1 (HY), azul c2; forma juvenil. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("pcm-mucosa", 1499976619643, {1: V, 2: Z, 3: Z}, B_, "Úlceras de mucosa oral e respiratória", 11, "Verde c1 (HY), azuis c2–c3; forma crônica."),
 ak("pcm-pulmao", 1499976536055, {1: V, 2: Z}, B_, "Granulomas pulmonares", 11, "Verde c1 (HY), azul c2."),
 ak("pcm-brotos", 1499975827249, {1: V}, B_, "Levedura com múltiplos brotos", 12, "Verde: HY; exame direto (lâminas 12 e 83)."),
 sh(1791557944405, "azul", B_, "Paracoccidioides é dimórfico", 81, "Azul: nota já existente de Biologia dos fungos."),
 au("pcm-cerebriforme", "At 37ºC, Paracoccidioides grows as {{c1::cerebriform}} yeast colonies", {1: R}, B_,
    "Colônia cerebriforme a 37 °C", "16, 87", "lateral", "sem card nos acervos.", [1499975827249, 1499976133630],
    "Rosa: lâmina 16.", extra="- At 25ºC the colony is white, with septate hyphae and few conidia"),
 au("pcm-grocott", "Paracoccidioides yeasts in tissue are shown best by Gomori-{{c1::Grocott}} silver stain", {1: Z}, B_,
    "Coloração de Grocott", "17, 80, 89; Trabulsi", "central", "consulta 'silver stain' sem card de PCM.", [1499975827249, 1499976536055], "Azul: lâmina 17."),
 au("pcm-glucana", "The yeast wall of Paracoccidioides is rich in {{c1::α-glucan}}, whereas the mold wall has mostly β-glucan", {1: V}, B_,
    "α-glucana na fase Y", "18, 90; prova 2025 P3 1.2", "prova", "sem card nos acervos.", [1499976133630, 1499975827249],
    "Verde: prova 2025.", extra="- α-glucan is the outer layer that resists phagocyte β-glucanase"),
 au("pcm-disseminacao", "If phagocytes fail to destroy the inhaled mold phase, Paracoccidioides turns into yeast and {{c1::disseminates}}", {1: Z}, B_,
    "Defesa deficiente → levedura e disseminação", "19, 91", "central", "sem card nos acervos.", [1499976355327, 1499976133630],
    "Azul: lâmina 19.", extra="- With intact defenses, β-glucanase digests the mold phase and infection is prevented"),
 ak("pcm-itraconazol", 1499976865408, {1: Z}, B_, "Itraconazol na PCM leve", 20, "Verde: HY; tratamento (monitoria). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("pcm-anfo", 1499976938219, {1: R}, B_, "Anfotericina B na PCM disseminada", 20, "Azul: tratamento (monitoria, histórico de 1958). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 # ---------- C. Histoplasmose (slides 21–33, 93–109) ----------
 ak("histo-fezes", 1499968902834, {1: V, 2: V}, C_, "Fezes de morcego e aves", 21, "Verdes: HY; prova 2025 P3 1.1."),
 ak("histo-resp", 1499969788030, {1: Z}, C_, "Histoplasma pela via respiratória", 21, "Azul: lâmina 21."),
 au("histo-microconidio", "Histoplasma infects people when its {{c1::microconidia}} are inhaled from contaminated soil", {1: V}, C_,
    "Microconídios inalados", "22–24, 94–96; prova 2025 P3 1.1", "prova", "AnKing diz só via respiratória.", [1499968902834, 1499969788030],
    "Verde: prova 2025.", extra="- Risk: caves, chicken coops and other places with bird or bat droppings"),
 ak("histo-macrofago", 1499969898257, {1: V, 2: Z}, C_, "Leveduras dentro de macrófagos", 24, "Verde c1 (HY), azul c2; lâminas 24 e 31."),
 ak("histo-sre", 1499970930064, {1: V, 2: Z}, C_, "Histoplasma no sistema reticuloendotelial", 25, "Verde c1 (HY), azul c2; lâmina 25."),
 ak("histo-dimorfico", 1499970254984, {1: V}, C_, "Histoplasma é dimórfico", 26, "Verde: HY; lâmina 26."),
 au("histo-tuberculado", "At 25ºC, Histoplasma forms thick-walled {{c1::tuberculate}} macroconidia", {1: Z}, C_,
    "Macroconídios tuberculados", "27–28, 100, 102; monitoria", "central", "consulta 'tuberculate macroconidia' sem card.", [1499970254984, 1499968902834],
    "Azul: lâmina 27.", extra="- Also called stalagmospores; small microconidia form too"),
 au("histo-boca", "The most frequent visible lesions of disseminated histoplasmosis are on the {{c1::tongue}} and palate", {1: Z}, C_,
    "Lesões bucofaríngeas", "32, 107", "central", "sem card nos acervos.", [1499970930064, 1499970467218], "Azul: lâmina 32."),
 ak("histo-tb", 1499970467218, {1: Z, 2: Z}, C_, "Histoplasmose crônica imita TB", 33, "Verde c1 (HY), azul c2; forma crônica (monitoria). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 au("histo-cultura", "Because Histoplasma is hard to see on direct exam, diagnosis relies on fungal {{c1::culture}}", {1: Z}, C_,
    "Diagnóstico por cultivo", "33; monitoria", "central", "sem card nos acervos.", [1499969898257, 1499970254984], "Azul: monitoria."),
 ak("histo-azol", 1499971065440, {1: Z}, C_, "Azóis na histoplasmose leve", 33, "Verde: HY; tratamento (monitoria). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("histo-anfo", 1499971295935, {1: R}, C_, "Anfotericina B na histoplasmose grave", 33, "Azul: tratamento (monitoria). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 # ---------- D. Candidose (slides 35–53, 111–129) ----------
 au("cand-especies", "Candida albicans causes about {{c1::60%}} of candidiasis cases", {1: Z}, D_,
    "C. albicans é a principal espécie", "35, 111", "central", "AnKing não traz a proporção.", [1500233417765, 1500234684400],
    "Azul: lâmina 111.", extra="- Others: C. tropicalis, C. glabrata, C. krusei, C. parapsilosis, C. auris"),
 ak("cand-flora", 1500234684400, {1: V}, D_, "Candida na microbiota", "35, 112", "Verde: HY; lâmina 112."),
 ak("cand-oportunista", 1500233417765, {1: V}, D_, "Candida é a micose oportunista mais comum", "35, 113", "Verde: HY; lâmina 113."),
 au("cand-virulencia", "Candida attaches to host cells through surface {{c1::adhesins}}", {1: Z}, D_,
    "Adesinas e virulência", "36, 121; Trabulsi", "central", "sem card de virulência.", [1500234149130, 1500233417765],
    "Azul: lâmina 36.", extra="- Other virulence factors: pseudohyphae, proteinases and phospholipases"),
 ak("cand-diabetes", 1500235637454, {1: Z}, D_, "Diabetes predispõe", 37, "Verde: HY; lâmina 37. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("cand-neutropenia", 1502224462650, {1: Z}, D_, "Neutropenia → candidose disseminada", 37, "Azul: lâminas 37 e 119."),
 sh(1791626779153, "azul", D_, "Deficiência T → candidose superficial", 37, "Azul: nota já existente de Micoses cutâneas."),
 sh(1791626779028, "azul", D_, "Sapinho por C. albicans", 38, "Azul: clínica; nota já existente de Micoses cutâneas (F-20261010-CLAUDE-04)."),
 ak("cand-vaginal-med", 1500235811939, {1: Z}, D_, "Medicamentos predispõem à candidíase vaginal", "37, 118", "Verde: HY; lâmina 118. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("cand-vaginal-queijo", 1500243739726, {1: R}, D_, "Corrimento em queijo cottage", "37, 118", "Verde: HY; vulvovaginite. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("cand-endocardite", 1500236481845, {1: R, 2: R}, D_, "Endocardite por Candida em UDIV", "37, 119", "Verde c1 (HY), azul c2; candidíase sistêmica (coração). Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("cand-pseudo", 1500234149130, {1: V}, D_, "Levedura com pseudo-hifas", 45, "Verde: HY; colônia e tecido."),
 sh(1791626784376, "azul", D_, "KOH no exame direto", "45, 122", "Azul: nota já existente de Micoses cutâneas."),
 ak("cand-tubo", 1500243540399, {1: V}, D_, "Tubo germinativo indica C. albicans", "45, 124", "Verde: HY; lâmina 124."),
 ak("cand-tubo-37", 1500234023725, {1: Z}, D_, "Tubo germinativo a 37 °C", "45, 124", "Azul: HY que repete cand-tubo (F-20261010-CLAUDE-03).", hy_repete="cand-tubo"),
 au("cand-clamido", "On corn meal agar at 25ºC, Candida albicans forms {{c1::chlamydospores}}", {1: Z}, D_,
    "Clamidósporos em ágar fubá", "47, 126; Trabulsi", "central", "consulta chlamydospore* sem card.", [1500243540399, 1500234149130], "Azul: lâmina 126."),
 au("cand-auxanograma", "An {{c1::auxanogram}} identifies yeasts by the carbon and nitrogen sources they assimilate", {1: Z}, D_,
    "Auxanograma", "51–52, 127–128", "central", "sem card nos acervos.", [1500243540399, 1500246419118], "Azul: lâmina 127."),
 au("cand-zimograma", "A {{c1::zymogram}} identifies yeasts by the sugars they ferment", {1: R}, D_,
    "Zimograma", "53, 129", "lateral", "sem card nos acervos.", [1500243540399, 1500246419118], "Rosa: lâmina 129."),
 # ---------- E. Criptococose (slides 54–63, 130–144) ----------
 ak("crypto-capsula", 1500243301914, {1: V}, E_, "Cryptococcus é encapsulado", "59, 131", "Verde: HY; prova 2024 P3 2.4."),
 sh(1791557941758, "verde", E_, "Cápsula antifagocitária", "59, 131", "Verde: prova 2024 P3 2.5. Nota já existente de Biologia dos fungos."),
 ak("crypto-oportunista", 1500244855818, {1: Z}, E_, "Oportunista em HIV", "56, 132", "Azul: lâminas 132 e 139."),
 ak("crypto-pombo", 1500244584091, {1: V, 2: V}, E_, "Fezes de pombo e solo", "55, 133", "Verdes: HY; lâmina 133."),
 sh(1791557941633, "azul", E_, "Cryptococcus é levedura", "55, 134", "Azul: nota já existente de Biologia dos fungos."),
 au("crypto-sne", "After a lung infection, Cryptococcus shows marked tropism for the {{c1::meninges}}", {1: V}, E_,
    "Tropismo pelo SNC", "56, 137", "central", "AnKing tem meningite, não o tropismo.", [1500244913534, 1500244699744], "Verde: lâminas 56 e 137."),
 ak("crypto-inalacao", 1500244699744, {1: V}, E_, "Inalação, primária no pulmão", "56, 138", "Verde: HY; lâmina 138."),
 ak("crypto-meningite", 1500244913534, {1: V, 2: V}, E_, "Causa mais comum de meningite fúngica", "56, 138", "Verdes: infecção secundária do SNC."),
 au("crypto-gattii", "Cryptococcus gattii (serotypes B and C) is linked to {{c1::eucalyptus}} trees", {1: Z}, E_,
    "C. gattii e eucalipto", "55, 133, 140; Trabulsi", "central", "consulta gattii sem card.", [1500244584091, 1500243301914],
    "Azul: lâmina 140.", extra="- C. neoformans var. neoformans has serotypes A and D"),
 ak("crypto-nanquim", 1500245573893, {1: V, 2: Z}, E_, "Tinta nanquim mostra a cápsula", "59, 143", "Verde c1 (HY), azul c2; lâminas 59–61."),
 ak("crypto-mucicarmim", 1500245435059, {1: Z, 2: R, 3: Z}, E_, "Mucicarmim no tecido", "59, 141", "Azuis c1/c3, rosa c2 (cor); lâmina 141."),
 ak("crypto-sabouraud", 1500246419118, {1: V}, E_, "Cultivo em Sabouraud", "58, 142", "Verde: HY; lâmina 142."),
 au("crypto-cgb", "On CGB agar, C. gattii grows and turns the medium {{c1::blue}}, whereas C. neoformans does not grow", {1: R}, E_,
    "Meio CGB", "62; Trabulsi", "lateral", "sem card nos acervos.", [1500246419118, 1500244771798],
    "Rosa: lâmina 62.", extra="- CGB = canavanine, glycine and bromothymol blue"),
 ak("crypto-urease", 1500244771798, {1: V}, E_, "Cryptococcus é urease-positivo", "63, 144", "Verde: HY; urease + × Candida − (lâmina 144)."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {'pcm-especies': '- P. lutzii (Pb01-like) occurs mainly in Mato Grosso, Rondônia and Ecuador',
 'pcm-tatu': '- Its geographic range matches the disease; the fungus was found in road-killed armadillos',
 'pcm-mortalidade': '- 3181 deaths in Brazil from 1980 to 1995',
 'pcm-linfonodos': '- Typical of the acute juvenile form',
 'pcm-grocott': '- The silver stain colors the fungal wall black',
 'pcm-itraconazol': '- Treatment is long',
 'pcm-anfo': '- Amphotericin B entered PCM treatment in 1958',
 'histo-boca': '- They usually appear as ulcers',
 'histo-cultura': '- Yeasts are small and hidden inside macrophages',
 'cand-diabetes': '- Other risks: AIDS, old age, pregnancy, antibiotics, corticosteroids',
 'cand-clamido': '- Thick-walled resting spores at the tip of pseudohyphae',
 'cand-auxanograma': '- Example: Cryptococcus assimilates glucose and sucrose but not lactose',
 'cand-zimograma': '- Used with the auxanogram to name the Candida species',
 'crypto-sne': '- It causes meningitis or meningoencephalitis',
 'cand-tubo-37': '- Test: incubate in serum at 37ºC for 3 hours',
 'crypto-capsula': '- The capsule is polysaccharide',
 'crypto-oportunista': '- Risk: AIDS, transplant, cancer, corticosteroids',
 'crypto-pombo': '- Also eucalyptus trees, mainly for C. gattii',
 'crypto-inalacao': '- The CNS is reached secondarily',
 'crypto-mucicarmim': '- It highlights the polysaccharide capsule in tissue sections',
 'crypto-nanquim': '- Used on CSF'}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
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
