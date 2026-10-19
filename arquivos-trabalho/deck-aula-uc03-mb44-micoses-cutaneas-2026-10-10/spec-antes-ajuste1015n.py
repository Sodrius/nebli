# Especificação curada — Micoses superficiais e cutâneas (UC03 P3, Microbiologia; Prof. Benedito Corrêa, aula de 2026; 55 lâminas). Gerada a partir de inventario.py (escrito antes).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-mb44-20261010a"
SHORT = "mb44"
LESSON = "2026-uc03-microbiologia-44-micoses-cutaneas"
DECK = "NEBLI::UC03::P3::Microbiologia::Micoses superficiais e cutâneas"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-02) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 21 consultas, e 10 consultas pontuais em 10/10): ")
EXCLUIDOS = [
 (1500053129177, "lâmpada de Wood para Microsporum: não está na aula de 2026"),
 (1517329278337, "dermatite seborreica: só nos slides antigos (Taborda); fora da aula de 2026"),
 (1500234023725, "tubo germinativo: aula de micologia prática/candidíase"),
 (1557752933497, "hifas septadas ramificadas no KOH: repete 1500052968870"),
 (1500053322321, "tratamento tópico: a aula não trata de tratamento"),
]
FORA_DO_RECORTE = ["tratamento das dermatofitoses", "micoses subcutâneas e sistêmicas (aulas seguintes)", "dermatite seborreica e foliculite por Malassezia (slides antigos)"]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = ("A-classificacao-e-superficiais", "B-dermatofitos-epidemiologia-e-patogenia", "C-formas-clinicas",
                          "D-diagnostico-laboratorial", "E-pitiriase-versicolor", "F-candida")
BV = "Verde"
CARDS = [
 # ---------- A. Manifestações, classificação e micoses superficiais (slides 2–5) ----------
 au("tipos-doenca", "Besides allergies and toxicoses, fungi cause disease by {{c1::invading}} living tissue", {1: Z}, A_,
    "Três tipos de manifestação", "2", "central", "sem card nos acervos sobre os três tipos de doença fúngica.", [1517779158524, 1500051969973],
    "Azul: abertura da aula (lâmina 2)."),
 au("classificacao", "Pityriasis versicolor is a {{c1::superficial}} mycosis, whereas dermatophytosis and cutaneous candidiasis are cutaneous mycoses", {1: Z}, A_,
    "Superficial × cutânea", "3 e 5; objetivo 1 (lâmina 55)", "prova", "AnKing tem cada doença isolada, sem a classificação.", [1500050017109, 1500051969973],
    "Azul: objetivo 'citar 2 exemplos de micoses cutâneas'."),
 ak("dermatofitos-tinea", 1500051969973, {1: V, 2: Z}, A_, "Dermatófitos causam tinha", 5, "Verde c1 (HY): dermatófitos do slide 3; azul c2."),
 au("dermatofitose-def", "Dermatophytosis is an infection of skin, hair or nails by fungi that feed on {{c1::keratin}}", {1: V}, A_,
    "Definição de dermatofitose", "5; objetivo 2", "central", "AnKing define tinha, não dermatofitose pela queratina.", [1500051969973, 1500152000410],
    "Verde: definição pedida nos objetivos."),
 au("superficial-imune", "Superficial mycoses stay in the stratum corneum and trigger {{c1::almost no}} immune response", {1: Z}, A_,
    "Superficial: pouca ou nenhuma resposta imune", "5", "central", "sem card sobre a resposta imune nas superficiais.", [1500051183614, 1500050370771],
    "Azul: esquema da lâmina 5."),
 ak("estrato-corneo-pv", 1500051183614, {1: Z}, A_, "M. furfur no estrato córneo", 5, "Azul: camada das micoses superficiais (lâmina 5)."),
 au("piedra-negra", "{{c1::Black piedra}}, caused by Piedraia hortae, forms hard dark nodules firmly attached to scalp hair", {1: R}, A_,
    "Piedra negra", "5; monitoria P2 aula 10; Trabulsi tab. 66.1", "lateral", "sem card de piedra nos acervos.", [1500050017109, 1500051183614],
    "Rosa: nome na lâmina 5; agente e aspecto da monitoria."),
 au("piedra-branca", "{{c1::White piedra}}, caused by Trichosporon species, forms soft pale nodules loosely attached to hair shafts", {1: R}, A_,
    "Piedra branca", "5; monitoria; Trabulsi tab. 66.1", "lateral", "sem card de piedra nos acervos.", [1500050017109, 1500051183614],
    "Rosa: nome na lâmina 5; agente e aspecto da monitoria."),
 au("tinea-nigra", "{{c1::Tinea nigra}}, caused by the salt-loving yeast Hortaea werneckii, produces dark patches on the palms", {1: R}, A_,
    "Tinha negra", "5; monitoria; slides 2024", "lateral", "sem card de tinea nigra nos acervos.", [1500050017109, 1500050525224],
    "Rosa: nome na lâmina 5; agente da monitoria."),
 au("filamentoso", "Unlike budding yeasts, dermatophytes are {{c1::filamentous}} fungi that form septate hyphae and conidia", {1: Z}, A_,
    "Dermatófito filamentoso × levedura", "5; prova 2024 P3 2.6", "prova", "AnKing não compara dermatófito e levedura.", [1500052968870, 1500233665851],
    "Azul: cobrado em 2024 (levedura × dermatófito)."),
 # ---------- B. Dermatófitos: habitat, fontes, localização, virulência, patogenia (slides 8–13) ----------
 au("habitat", "Dermatophytes living in soil are {{c1::geophilic}}, those adapted to animals are {{c2::zoophilic}}, and those adapted to humans are {{c3::anthropophilic}}", {1: V, 2: V, 3: V}, B_,
    "Grupos por habitat", "8; objetivo 3; prova 2019 P2 3.1", "prova", "sem card de habitat dos dermatófitos.", [1500052841281, 1500052358184],
    "Verdes: objetivo da aula e prova 2019."),
 au("geofilico-grave", "Geophilic and zoophilic dermatophytes, less adapted to humans, cause {{c1::more inflammatory}} infections than anthropophilic ones", {1: Z}, B_,
    "Geofílicos/zoofílicos: infecção mais grave", "8", "central", "sem card nos acervos.", [1500052841281, 1500052912297], "Azul: quadro da lâmina 8."),
 ak("pets", 1500052841281, {1: V}, B_, "Animais como fonte", 9, "Verde: transmissão direta (lâmina 9) e prova 2019."),
 au("transmissao-indireta", "Dermatophytes also spread indirectly through {{c1::fomites}}, such as shared floors, towels and combs", {1: Z}, B_,
    "Transmissão indireta", "9; monitoria", "central", "sem card de fômites para dermatófitos.", [1500052841281, 1500052763799], "Azul: lâmina 9."),
 au("localizacao", "Trichophyton infects skin, hair and nails, {{c1::Microsporum}} spares the nails, and {{c2::Epidermophyton}} spares the hair", {1: Z, 2: Z}, B_,
    "Localização por gênero", "10; objetivo 4", "prova", "AnKing só lista os três gêneros (1500052358184).", [1500052358184, 1500152247775],
    "Azuis: quadro da lâmina 10.", extra="- Nannizzia, like Microsporum, spares the nails"),
 sh(1791557945582, "verde", B_, "Queratinase dos dermatófitos", 11, "Verde: fator de virulência central (lâmina 11; objetivo 5; prova 2025). Nota NEBLI do deck de Fungos."),
 au("outras-enzimas", "Besides keratinases, dermatophytes secrete {{c1::elastases}}, collagenase and DNase", {1: R}, B_,
    "Outras enzimas de virulência", "11; Trabulsi", "lateral", "sem card nos acervos.", [1500152000410, 1500052968870], "Rosa: lista da lâmina 11."),
 au("artroconidios", "Dermatophytosis begins when {{c1::arthroconidia}} or hyphal fragments land on skin with a small wound", {1: Z}, B_,
    "Inoculação de artroconídios", "12; monitoria", "central", "sem card de patogenia dos dermatófitos.", [1500052968870, 1500152000410], "Azul: lâmina 12."),
 au("crescimento-centrifugo", "Dermatophytes grow outward from the inoculation site in a circle, producing the {{c1::ring}}-shaped lesion with an active border", {1: V}, B_,
    "Crescimento centrífugo → lesão anular", "12", "central", "AnKing diz 'ringworm', não o porquê do anel.", [1500052444077, 1505160761819],
    "Verde: explica o aspecto clínico de todas as tinhas."),
 au("estrato-corneo-inflamacao", "Dermatophytes rarely invade below the {{c1::stratum corneum}}", {1: Z}, B_,
    "Limitado ao estrato córneo, mas inflamatório", "12; prova 2025 P3 4.4", "prova", "sem card nos acervos.", [1500051183614, 1500152000410],
    "Azul: cobrado em 2025.", extra="- Itching and scaling are a host reaction to fungal products, not deep invasion"),
 ak("atletas", 1500052763799, {1: Z}, B_, "Atletas em risco", 13, "Azul: calçado, umidade e populações fechadas (lâmina 13)."),
 au("imunidade-t", "Defective {{c1::cell-mediated}} (T cell) immunity makes dermatophytosis more extensive and recurrent", {1: Z}, B_,
    "Imunossupressão e dermatofitose", "13; prova 2025 P3 4.4", "prova", "AnKing liga células T só à Candida (1502224452270).", [1502224452270, 1500152247775],
    "Azul: 'fatores imunológicos' (lâmina 13) e prova 2025."),
 # ---------- C. Formas clínicas (slides 14–31) ----------
 ak("ringworm", 1500052444077, {1: Z}, C_, "Tinha = ringworm", 14, "Verde: HY. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("tinea-corporis", 1500052605836, {1: Z}, C_, "Tinea corporis: corpo", 14, "Azul: lâminas 14–15."),
 ak("pruriginosa", 1500052912297, {1: R}, C_, "Tinha é pruriginosa", 14, "Verde: HY. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("corporis-imagem", 1505160761819, {1: Z}, C_, "Reconhecer tinea corporis", 14, "Azul: reconhecimento da lesão anular (lâminas 14–15)."),
 au("tinea-pedis", "Athlete's foot, often starting between the toes, is tinea {{c1::pedis}}", {1: Z}, C_,
    "Tinea pedis", "16 e 18", "central", "AnKing cita tinea pedis só em complicações (1581260145423).", [1500052626060, 1500052605836], "Azul: lâminas 16 e 18."),
 au("imbricata", "Tinea imbricata, with concentric rings of scale, is caused by Trichophyton {{c1::concentricum}}", {1: R}, C_,
    "Tinha imbricata", "17", "lateral", "sem card nos acervos.", [1500052605836, 1500052444077], "Rosa: lâmina 17."),
 ak("tinea-cruris", 1500052626060, {1: Z}, C_, "Tinea cruris: virilha", 19, "Azul: lâminas 19–20. Extra do AnKing sem a linha de crédito DermNet (resto preservado).",
    extra='<div>- AKA "jock itch"</div><br><div>- Recall that <b>crura</b> attaches the base of the penis to the ischiopubic rami</div><br><div><img alt="Raised border and central clearing" src="6162814eb02f42194b0b7d9c5a004a99.webp" width="518"><img src="7c95acc786ed7e81a4a4d6ac9818c3b9.webp" width="290"></div>'),
 ak("recorrencia-cruris", 1555800414777, {1: R}, C_, "Tinea cruris recorre por tinea pedis", 19, "Rosa: ligação pé–virilha."),
 au("tinea-manum", "Dermatophytosis of the hands is called tinea {{c1::manuum}}", {1: R}, C_,
    "Tinea manum", "21", "lateral", "sem card nos acervos.", [1500052605836, 1500052626060], "Rosa: lâmina 21.", extra="- Often dry scaling of one palm, with tinea pedis on both feet"),
 au("indotineae", "Trichophyton indotineae, an emerging dermatophyte, resists terbinafine through mutations in {{c1::squalene epoxidase}}", {1: R}, C_,
    "T. indotineae e resistência à terbinafina", "22; slides 2024", "lateral", "sem card de resistência a terbinafina.", [1509741919338, 1509751441530],
    "Rosa: lâmina 22 (1º caso no Brasil)."),
 ak("alilaminas", 1509741919338, {1: V, 2: V}, C_, "Alilaminas inibem esqualeno epoxidase", 22, "Verdes: HY; alvo da mutação do T. indotineae."),
 au("dermatofitide", "A sterile eruption on the hands caused by an immune reaction to a distant dermatophyte focus is a {{c1::dermatophytid}}", {1: Z}, C_,
    "Dermatofítides", "23; monitoria P2", "central", "consultas 'id reaction' e 'dermatophytid' sem card pertinente.", [1500052912297, 1555800414777],
    "Azul: lâmina 23 e monitoria.", extra="- Usually from tinea pedis; no fungi in the id lesions"),
 ak("onicomicose", 1500053417089, {1: V, 2: V}, C_, "Onicomicose por dermatófito", 24, "Verdes: HY; lâminas 24 e 26."),
 au("onicomicose-distal", "Dermatophyte onychomycosis usually starts at the {{c1::distal}} nail edge, whereas Candida starts at the proximal nail fold", {1: Z}, C_,
    "Onicomicose: distal × prega proximal", "25 e 27; monitoria", "central", "AnKing não tem a progressão nem a distinção com Candida.", [1500053417089, 1680461059715],
    "Azul: lâmina 25 (diferenciação das onicomicoses).", extra="- Candida nail infection often comes with paronychia"),
 ak("sapinho", 1500243661654, {1: Z}, F_, "Sapinho por C. albicans", 28, "Verde: HY; lâmina 28. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("candida-t", 1502224452270, {1: Z}, F_, "Deficiência T → Candida superficial", 28, "Azul: liga candidose mucocutânea à imunidade celular."),
 ak("intertrigo", 1535402608704, {1: Z}, F_, "Intertrigo por Candida", 29, "Azul: candidose cutânea das dobras (lâmina 29)."),
 ak("tinea-capitis", 1500152247775, {1: Z}, C_, "Tinea capitis em crianças", 30, "Verde: HY; lâmina 30. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("capitis-tonsurans", 1578250039053, {1: Z}, C_, "Tinea capitis por T. tonsurans", 30, "Azul: agente da lâmina 30."),
 au("canis-animais", "Tinea capitis in children is often caused by {{c1::Microsporum canis}}, caught from cats and dogs", {1: Z}, C_,
    "M. canis vem de cães e gatos", "30–31", "central", "AnKing só tem pets como fonte genérica (1500052841281).", [1500052841281, 1500152247775],
    "Azul: lâminas 30–31.", duplicacao_ok="ganho: agente zoofílico específico; pets cobra só a fonte"),
 # ---------- D. Diagnóstico laboratorial (slides 32–47) ----------
 au("its", "Molecular identification of dermatophytes sequences the {{c1::ITS}} region of ribosomal DNA", {1: R}, D_,
    "Identificação molecular (ITS)", "32", "lateral", "sem card nos acervos.", [1500052968870, 1500246419118], "Rosa: lâmina 32."),
 au("rubrum-prevalencia", "{{c1::Trichophyton rubrum}} is the most common dermatophyte isolated in Brazil", {1: Z}, D_,
    "T. rubrum predomina", "33; slides 2024", "central", "sem card de prevalência por espécie.", [1500052358184, 1500152247775], "Azul: lâmina 33 (66% no Brasil)."),
 au("cicloheximida", "Dermatophytes are cultured on Sabouraud agar with chloramphenicol and {{c1::cycloheximide}}, which suppress bacteria and contaminant molds", {1: Z}, D_,
    "Meio seletivo (Mycosel)", "34; slides 2024", "central", "AnKing cita Sabouraud só para Cryptococcus (1500246419118).", [1500246419118, 1500052968870],
    "Azul: lâmina 34; objetivo 'procedimentos laboratoriais'."),
 au("carpete", "To find dermatophytes on healthy animal carriers, the {{c1::carpet}} technique brushes the fur and presses it onto culture plates", {1: R}, D_,
    "Técnica do carpete", "35", "lateral", "sem card nos acervos.", [1500052841281, 1500052968870], "Rosa: lâmina 35."),
 au("coleta-borda", "Skin scrapings for dermatophytes are taken from the {{c1::active border}} of the lesion", {1: Z}, D_,
    "Coleta na borda da lesão", "36; slides 2024", "central", "sem card de coleta nos acervos.", [1500052968870, 1546271297640], "Azul: lâmina 36."),
 ak("koh-hifas", 1500052968870, {1: V, 2: V, 3: Z}, D_, "KOH mostra hifas de dermatófito", 37, "Verdes c1–c2 (KOH, hifas), azul c3; lâminas 37–38."),
 ak("koh-onicomicose", 1546271297640, {1: Z}, D_, "Onicomicose confirmada por KOH", 37, "Azul: exame direto na unha."),
 au("ectothrix", "In microsporia, Microsporum spores coat the outside of the hair shaft, an {{c1::ectothrix}} invasion", {1: Z}, D_,
    "Microsporia: ectotrix", "39–40; Trabulsi tab. 66.1", "central", "consulta 'ectothrix' sem card.", [1500152247775, 1578250039053],
    "Azul: lâminas 39–40 (pelo parasitado)."),
 au("microcultivo", "{{c1::Slide culture}} (microculture) keeps conidia in place for microscopic identification of the fungus", {1: R}, D_,
    "Microcultivo", "42", "lateral", "sem card nos acervos.", [1500052968870, 1500246419118], "Rosa: lâmina 42."),
 au("canis-macroconidio", "Microsporum canis forms spindle-shaped, thick-walled {{c1::macroconidia}}", {1: Z}, D_,
    "M. canis: macroconídios fusiformes", "43 e 41", "central", "consulta 'macroconidia' sem card.", [1500052968870, 1500152247775], "Azul: lâmina 43."),
 au("gypsea", "Nannizzia gypsea (formerly Microsporum gypseum) forms ellipsoid macroconidia with {{c1::thin}} walls", {1: R}, D_,
    "N. gypsea", "44 e 41", "lateral", "sem card nos acervos.", [1500052968870, 1500052358184], "Rosa: lâmina 44."),
 au("mentagrophytes", "Trichophyton mentagrophytes forms round {{c1::microconidia}} in grape-like clusters", {1: R}, D_,
    "T. mentagrophytes", "45", "lateral", "sem card nos acervos.", [1500052968870, 1500052358184], "Rosa: lâmina 45."),
 au("rubrum-reverso", "Trichophyton rubrum colonies show a {{c1::red}} pigment on the reverse of the plate", {1: Z}, D_,
    "T. rubrum: reverso vermelho", "46", "central", "sem card nos acervos.", [1500052968870, 1500052358184], "Azul: lâmina 46; espécie mais comum."),
 au("epidermophyton", "Epidermophyton floccosum forms club-shaped macroconidia and no {{c1::microconidia}}", {1: Z}, D_,
    "E. floccosum", "47", "central", "sem card nos acervos.", [1500052968870, 1500052358184], "Azul: lâmina 47."),
 # ---------- E. Pitiríase versicolor (slides 48–52) ----------
 ak("malassezia-pv", 1500050017109, {1: V, 2: V}, E_, "Malassezia causa pitiríase versicolor", 48, "Verdes: HY; lâmina 48."),
 ak("pv-manchas", 1500050525224, {1: Z}, E_, "Manchas hipo/hipercrômicas", 49, "Verde: HY; lâmina 49. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("pv-tronco", 1500050773382, {1: R}, E_, "Tórax e dorso", 49, "Verde: HY; fotos da lâmina 49. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("furfur-flora", 1500050370771, {1: V, 2: Z, 3: Z}, E_, "Flora da pele, calor e umidade", 50, "Verde c1 (HY), azuis c2–c3; epidemiologia tropical (lâmina 50)."),
 au("pv-sebo", "Pityriasis versicolor peaks in adolescents and young adults, whose skin produces more {{c1::sebum}}", {1: Z}, E_,
    "PV em adolescentes e adultos jovens", "50; objetivo 7", "prova", "AnKing tem calor e umidade, não a idade/oleosidade.", [1500050370771, 1500050773382],
    "Azul: objetivo 'epidemiologia da pitiríase versicolor'."),
 ak("pv-acido", 1500050853067, {1: V, 2: Z}, E_, "Ácidos de lipídeos lesam melanócitos", 50, "Verde c1 (HY), azul c2; monitoria."),
 ak("spaghetti", 1500050268188, {1: V}, E_, "Espaguete e almôndegas no KOH", 51, "Verde: HY; diagnóstico da PV (lâmina 51)."),
 ak("furfur-imagem", 1556238897815, {1: Z}, E_, "Reconhecer Malassezia", 51, "Verde: HY; reconhecimento da lâmina 51. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 au("lipodependente", "Malassezia is lipid-dependent, so its culture medium needs added {{c1::oil}}", {1: Z}, E_,
    "Malassezia exige lipídeos no meio", "52; Trabulsi tab. 66.1; slides 2024", "central", "AnKing cita só o caráter lipofílico na NPT (1500051612651).",
    [1500051612651, 1500050370771], "Azul: isolamento da lâmina 52."),
 # ---------- F. Candidíase cutânea: diagnóstico (slides 53–54) ----------
 ak("koh-candida", 1500235321247, {1: Z}, F_, "KOH para candidíase", 53, "Verde: HY; lâmina 53. Rebaixado: foco em compreensão, clínica não cobrada pela aula (F-20261010-CLAUDE-04).", clinica_lateral=True),
 ak("pseudohifas", 1548722722826, {1: Z}, F_, "Pseudo-hifas = Candida", 53, "Azul: exame direto da lâmina 53."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 "tipos-doenca": "- Allergy (hypersensitivity) and toxicosis (mycetism, mycotoxicosis) need no invasion",
 "classificacao": "- Superficial: stratum corneum only; cutaneous: also hair and nails, with inflammation",
 "dermatofitose-def": "- Genera: Trichophyton, Microsporum, Nannizzia, Epidermophyton",
 "superficial-imune": "- Examples: pityriasis versicolor, black and white piedra, tinea nigra",
 "piedra-negra": "- Mostly in tropical regions",
 "piedra-branca": "- Mostly on genital, axillary and facial hair",
 "tinea-nigra": "- Lives in salty environments (sea, sand)",
 "filamentoso": "- Cryptococcus and Candida are yeasts that reproduce by budding",
 "habitat": "- Anthropophilic species spread person to person",
 "geofilico-grave": "- Anthropophilic species cause milder, chronic lesions",
 "pets": "- Microsporum canis from cats and dogs is the classic example",
 "transmissao-indireta": "- Shed skin scales and hairs carry the fungus",
 "outras-enzimas": "- They help digest keratinized tissue",
 "artroconidios": "- Moisture and occlusion favor implantation",
 "crescimento-centrifugo": "- Active, scaly border with central clearing",
 "imunidade-t": "- Also diabetes, corticosteroids and immunosuppression",
 "tinea-corporis": "- Annular, scaly, itchy plaques",
 "pruriginosa": "- Itch and scaling come from the host reaction",
 "corporis-imagem": "- Ring-shaped lesion with active border",
 "tinea-pedis": "- Usually caused by Trichophyton rubrum or T. interdigitale",
 "imbricata": "- Concentric scaly rings over large areas",
 "indotineae": "- Spreading from India; first Brazilian case in São Paulo",
 "alilaminas": "- Squalene builds up and ergosterol falls",
 "canis-animais": "- A zoophilic species",
 "its": "- Used when morphology is inconclusive",
 "rubrum-prevalencia": "- Mainly tinea pedis and tinea unguium",
 "cicloheximida": "- Dermatophytes tolerate cycloheximide; contaminant molds do not",
 "carpete": "- Animals can carry dermatophytes without lesions",
 "coleta-borda": "- Clean with 70% alcohol before scraping",
 "koh-onicomicose": "- KOH dissolves keratin and leaves fungal hyphae visible",
 "ectothrix": "- Trichophyton tonsurans invades inside the shaft (endothrix)",
 "microcultivo": "- A block of agar on a slide, covered by a coverslip",
 "canis-macroconidio": "- Colony with yellow reverse",
 "gypsea": "- A geophilic species from soil",
 "mentagrophytes": "- Zoophilic and anthropophilic strains exist",
 "rubrum-reverso": "- Few teardrop microconidia along the hyphae",
 "epidermophyton": "- Infects skin and nails, not hair",
 "pv-sebo": "- Less common in children and the elderly",
 "spaghetti": "- Short hyphae (spaghetti) plus round yeasts (meatballs)",
 "furfur-imagem": "- Clusters of round yeasts with short hyphae",
 "lipodependente": "- Colonies are creamy white and shiny",
 "koh-candida": "- Shows budding yeasts and pseudohyphae",
 "pseudohifas": "- Candida also forms creamy colonies on Sabouraud agar",
}
DUPLICACAO = {
 "estrato-corneo-inflamacao": "ganho: profundidade da invasão do dermatófito; estrato-corneo-pv cobra onde fica a Malassezia",
 "indotineae": "ganho: mecanismo de resistência emergente; alilaminas cobra o alvo do fármaco",
}
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
_ak("onicomicose", text="{{c1::Onychomycosis}} is fungal infection of the nails, and when caused by dermatophytes it is called {{c2::tinea unguium}}", flags={1: V, 2: V})
_ak("pseudohifas", text="<b>Pseudohyphae with budding yeasts</b> on KOH prep suggest {{c1::Candida}}")
_au("classificacao", extra="- Superficial: outermost keratin (stratum corneum or hair shaft) with almost no host response<br>- Cutaneous: skin, hair and nails with an inflammatory response")
for k in ("rubrum-reverso", "epidermophyton", "dermatofitide", "pv-sebo", "lipodependente", "recorrencia-cruris", "intertrigo"): _cor(k, R)
_cor("outras-enzimas", Z)
_ak("capitis-tonsurans", extra="- Diagnosis is by KOH and culture of hair")
CARDS[:] = [c for c in CARDS if c["key"] not in ("ringworm", "furfur-imagem")]
_novo("nao-dermatofitos", "Besides dermatophytes and Candida, {{c1::non-dermatophyte}} <b>molds</b> can also cause cutaneous mycoses", Z, "classificacao", "Não dermatófitos", "5", "central", "- Mainly onychomycosis")
_novo("portadores", "Many people carry <b>dermatophytes</b> on their skin as {{c1::asymptomatic}} carriers", R, "classificacao", "Portadores assintomáticos", "7, 13", "lateral", "- Dermatophytes can be part of the normal skin microbiota")
_novo("estrato-imunidade", "The <b>stratum corneum</b> lacks a {{c1::specific immune}} response, so dermatophytes spread there until inflammation forms at the border", Z, "classificacao", "Estrato córneo sem imunidade específica", "12", "central")
_novo("umidade", "Local {{c1::moisture}} and breaks in <b>epidermal integrity</b> favor dermatophyte colonization", Z, "classificacao", "Fatores do hospedeiro", "13", "central", "- Footwear, hygiene and crowded settings also matter")
_novo("endotrix", "<b>Trichophyton tonsurans</b> grows inside the <b>hair shaft</b>, an {{c1::endothrix}} invasion", Z, "capitis-tonsurans", "Tricofícia endotrix", "40", "central", "- Microsporum canis coats the outside (ectothrix)")
_novo("candidiase-cutanea", "<b>Cutaneous candidiasis</b> favors moist sites such as the {{c1::interdigital}} spaces and the corners of the mouth", Z, "intertrigo", "Candidíase cutânea", "29", "central")
_novo("cultivo-25", "<b>Dermatophyte cultures</b> are incubated at {{c1::25}} °C for 1–2 weeks", R, "capitis-tonsurans", "Cultivo de dermatófitos", "34", "lateral", "- Dermatophyte Test Medium (DTM) is an alternative")
_novo("candida-sabouraud", "On <b>Sabouraud agar</b>, Candida albicans forms {{c1::creamy}}, cream-colored colonies", Z, "pseudohifas", "Colônia de C. albicans", "54", "central")

# negrito aplicado ao vivo em 11/10 (correcao-comentarios-2026-10-11/negrito.json), trazido à spec
_NEGRITO_VIVO = {
"tipos-doenca": "Besides <b>allergies and toxicoses</b>, fungi cause disease by {{c1::invading}} <b>living tissue</b>",
"classificacao": "<b>Pityriasis versicolor</b> is a {{c1::superficial}} mycosis, whereas <b>dermatophytosis and cutaneous candidiasis</b> are cutaneous mycoses",
"dermatofitose-def": "<b>Dermatophytosis</b> is an infection of <b>skin, hair or nails</b> by fungi that feed on {{c1::keratin}}",
"superficial-imune": "<b>Superficial mycoses</b> stay in the <b>stratum corneum</b> and trigger {{c1::almost no}} immune response",
"piedra-negra": "{{c1::Black piedra}}, caused by <b>Piedraia hortae</b>, forms <b>hard dark nodules</b> firmly attached to <b>scalp hair</b>",
"piedra-branca": "{{c1::White piedra}}, caused by <b>Trichosporon</b> species, forms <b>soft pale nodules</b> loosely attached to <b>hair shafts</b>",
"tinea-nigra": "{{c1::Tinea nigra}}, caused by the salt-loving yeast <b>Hortaea werneckii</b>, produces <b>dark patches</b> on the <b>palms</b>",
"filamentoso": "Unlike <b>budding yeasts</b>, <b>dermatophytes</b> are {{c1::filamentous}} fungi that form <b>septate hyphae and conidia</b>",
"habitat": "Dermatophytes living in <b>soil</b> are {{c1::geophilic}}, those adapted to <b>animals</b> are {{c2::zoophilic}}, and those adapted to <b>humans</b> are {{c3::anthropophilic}}",
"geofilico-grave": "<b>Geophilic and zoophilic</b> dermatophytes, less adapted to humans, cause {{c1::more inflammatory}} infections than <b>anthropophilic</b> ones",
"transmissao-indireta": "Dermatophytes also spread <b>indirectly</b> through {{c1::fomites}}, such as <b>shared floors, towels and combs</b>",
"localizacao": "<b>Trichophyton</b> infects skin, <b>hair</b> and <b>nails</b>, {{c1::Microsporum}} spares the nails, and {{c2::Epidermophyton}} spares the hair",
"outras-enzimas": "Besides <b>keratinases</b>, dermatophytes secrete {{c1::elastases}}, <b>collagenase and DNase</b>",
"artroconidios": "<b>Dermatophytosis begins</b> when {{c1::arthroconidia}} or hyphal fragments land on skin with a <b>small wound</b>",
"crescimento-centrifugo": "Dermatophytes grow outward from the inoculation site in a <b>circle</b>, producing the {{c1::ring}}-shaped lesion with an <b>active border</b>",
"estrato-corneo-inflamacao": "<b>Dermatophytes rarely invade</b> below the {{c1::stratum corneum}}",
"imunidade-t": "<b>Defective</b> {{c1::cell-mediated}} (T cell) immunity makes <b>dermatophytosis more extensive and recurrent</b>",
"tinea-pedis": "<b>Athlete's foot</b>, often starting <b>between the toes</b>, is tinea {{c1::pedis}}",
"imbricata": "<b>Tinea imbricata</b>, with <b>concentric rings of scale</b>, is caused by Trichophyton {{c1::concentricum}}",
"tinea-manum": "Dermatophytosis of the <b>hands</b> is called tinea {{c1::manuum}}",
"indotineae": "<b>Trichophyton indotineae</b>, an emerging dermatophyte, resists <b>terbinafine</b> through mutations in {{c1::squalene epoxidase}}",
"dermatofitide": "A <b>sterile eruption on the hands</b> caused by an immune reaction to a <b>distant dermatophyte focus</b> is a {{c1::dermatophytid}}",
"onicomicose-distal": "<b>Dermatophyte onychomycosis</b> usually starts at the {{c1::distal}} nail edge, whereas <b>Candida</b> starts at the {{c1::proximal}}<b>&nbsp;nail fold</b>",
"canis-animais": "<b>Tinea capitis in children</b> is often caused by {{c1::Microsporum canis}}, caught from <b>cats and dogs</b>",
"its": "<b>Molecular identification</b> of dermatophytes sequences the {{c1::ITS}} region of <b>ribosomal DNA</b>",
"rubrum-prevalencia": "{{c1::Trichophyton rubrum}} is the <b>most common dermatophyte</b> isolated in <b>Brazil</b>",
"cicloheximida": "Dermatophytes are cultured on <b>Sabouraud agar</b> with <b>chloramphenicol</b> and {{c1::cycloheximide}}, which suppress <b>bacteria and contaminant molds</b>",
"carpete": "To find dermatophytes on <b>healthy animal carriers</b>, the {{c1::carpet}} technique brushes the <b>fur</b> and presses it onto culture plates",
"coleta-borda": "<b>Skin scrapings</b> for dermatophytes are taken from the {{c1::active border}} of the <b>lesion</b>",
"ectothrix": "In <b>microsporia</b>, Microsporum spores coat the <b>outside of the hair shaft</b>, an {{c1::ectothrix}} invasion",
"microcultivo": "{{c1::Slide culture}} (microculture) keeps conidia in place for <b>microscopic identification</b> of the fungus",
"canis-macroconidio": "<b>Microsporum canis</b> forms <b>spindle-shaped, thick-walled</b> {{c1::macroconidia}}",
"gypsea": "<b>Nannizzia gypsea</b> (formerly Microsporum gypseum) forms ellipsoid macroconidia with {{c1::thin}} walls",
"mentagrophytes": "<b>Trichophyton mentagrophytes</b> forms round {{c1::microconidia}} in <b>grape-like clusters</b>",
"rubrum-reverso": "<b>Trichophyton rubrum</b> colonies show a {{c1::red}} pigment on the <b>reverse of the plate</b>",
"epidermophyton": "<b>Epidermophyton floccosum</b> forms <b>club-shaped macroconidia</b> and no {{c1::microconidia}}",
"pv-sebo": "<b>Pityriasis versicolor</b> peaks in <b>adolescents and young adults</b>, whose skin produces more {{c1::sebum}}",
"lipodependente": "<b>Malassezia</b> is <b>lipid-dependent</b>, so its culture medium needs added {{c1::oil}}"
}
for _k, _t in _NEGRITO_VIVO.items():
    _c(_k)["text"] = _t
for _k, _x in {"estrato-imunidade": "- Hence the active, inflamed border and the clearer center of the ring",
               "candidiase-cutanea": "- Moisture and maceration favor Candida, as in intertrigo",
               "candida-sabouraud": "- Microscopy shows budding yeasts"}.items():
    _c(_k)["extra"] = _x

# ---- Revisão por prova 15/10 (F-20261015-CLAUDE-03): organizadores de mapa mental, em tópicos, no ponto em que cada grupo aparece ----
ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
_MOT = "Revisão 15/10: organizador de mapa mental pedido por Davi (‘quais as principais superficiais, diferença superficial × cutânea, principais cutâneas’)."
def _antes(ref, card):
    i = next(i for i, c in enumerate(CARDS) if c["key"] == ref); CARDS.insert(i, card)
_c("tipos-doenca")["text"] = ORG("Three ways <b>fungi</b> cause disease:<br>- {{c1::allergies}} (hypersensitivity)<br>- {{c2::toxicoses}} (mycetism and mycotoxicosis)<br>- {{c3::infections}} (invasion of living tissue)")
_c("tipos-doenca")["flags"] = {1: V, 2: V, 3: V}; _c("tipos-doenca")["motivo"] = "Verde: lâmina 2. " + _MOT + " Antes o cloze estava no verbo ‘invading’."
_c("classificacao")["text"] = ORG("<b>Superficial</b> × <b>cutaneous</b> mycoses:<br>- superficial: only the {{c1::stratum corneum}} or hair surface, no immune response<br>- cutaneous: fungi digest the {{c2::keratin}} of skin, hair, nails, with inflammation")
_c("classificacao")["flags"] = {1: V, 2: V}; _c("classificacao")["motivo"] = "Verde: lâminas 3 e 5; provas 2025 P3 4.4 e 2024 P3 2.6. " + _MOT
_c("classificacao")["extra"] = "- Subcutaneous mycoses are implanted below the skin; systemic ones are usually inhaled"
_c("classificacao")["duplicacao_ok"] = "organizador: o critério que separa os grupos"
CARDS[:] = [c for c in CARDS if c["key"] != "superficial-imune"]
_antes("classificacao", au("org-classificacao", ORG("<b>Mycoses</b> by depth of invasion:<br>- {{c1::superficial}}: pityriasis versicolor<br>- {{c2::cutaneous}}: dermatophytosis, candidiasis<br>- {{c3::subcutaneous}}: sporotrichosis, chromoblastomycosis<br>- {{c4::systemic}}: histoplasmosis, paracoccidioidomycosis, cryptococcosis"),
    {1: V, 2: V, 3: V, 4: V}, A_, "Classificação das micoses por profundidade", "3", "central", "nenhum card dos acervos.", _ESP, "Verde: lâminas 3–4 (repetidas nas aulas 48 e 50). " + _MOT,
    extra="- The depth reached by the fungus defines the group, from keratin to internal organs", duplicacao_ok="organizador da matéria inteira"))
_antes("estrato-corneo-pv", au("org-superficiais", ORG("Main <b>superficial mycoses</b> (agent):<br>- {{c1::pityriasis versicolor}} (Malassezia)<br>- {{c2::black piedra}} (Piedraia hortae)<br>- {{c3::white piedra}} (Trichosporon)<br>- {{c4::tinea nigra}} (Hortaea werneckii)"),
    {1: V, 2: V, 3: V, 4: V}, A_, "Principais micoses superficiais", "5", "central", "nenhum card dos acervos.", _ESP, "Verde: lâmina 5. " + _MOT, extra="- All stay in dead keratin, so they are mainly cosmetic",
    duplicacao_ok="organizador; os cards de cada item cobram o agente e o aspecto"))
_antes("estrato-corneo-pv", au("org-cutaneas", ORG("Main <b>cutaneous mycoses</b>:<br>- {{c1::dermatophytosis}} (tinea)<br>- cutaneous {{c2::candidiasis}}<br>- infection by {{c3::non-dermatophyte}} molds"),
    {1: V, 2: V, 3: V}, A_, "Principais micoses cutâneas", "5", "central", "nenhum card dos acervos.", _ESP, "Verde: lâminas 3 e 5. " + _MOT, extra="- Dermatophytes are by far the most common cause",
    duplicacao_ok="organizador"))
_antes("estrato-corneo-pv", au("org-generos", ORG("The three <b>dermatophyte</b> genera:<br>- {{c1::Trichophyton}}<br>- {{c2::Microsporum}} (now partly Nannizzia)<br>- {{c3::Epidermophyton}}"),
    {1: V, 2: V, 3: V}, A_, "Gêneros de dermatófitos", "5", "prova", "nenhum card dos acervos.", _ESP, "Verde: lâmina 3; prova 2019 P2 3.1 (gêneros e fontes). " + _MOT, extra="- Sources: soil (geophilic), animals (zoophilic), people (anthropophilic)",
    duplicacao_ok="organizador; a tabela de locais cobra onde cada gênero infecta"))
_ref14 = next(c["key"] for c in sorted(CARDS, key=lambda c: int(_re.search(r"\d+", c["evid"]).group())) if int(_re.search(r"\d+", c["evid"]).group()) >= 14)
_antes(_ref14, au("org-tinhas", ORG("<b>Tinea</b> is named by the site:<br>- scalp: tinea {{c1::capitis}}<br>- body: tinea {{c2::corporis}}<br>- groin: tinea {{c3::cruris}}<br>- feet: tinea {{c4::pedis}}<br>- nails: tinea {{c5::unguium}}"),
    {1: Z, 2: Z, 3: Z, 4: Z, 5: Z}, C_, "Tinhas por local", "14", "central", "nenhum card dos acervos.", _ESP, "Azul: lâminas 14–30. " + _MOT, extra="- Tinea = dermatophytosis; the Latin name only says where it is",
    duplicacao_ok="organizador; os cards de cada tinha trazem a clínica"))

# tabela gênero × local feita ao vivo (comentário de Davi, CORRIGIDO 14/10) trazida à spec, 15/10
_c("localizacao")["text"] = "<div data-nebli-organizacao=\"true\">Sites infected by each <b>dermatophyte</b> genus:<br><table style=\"margin:auto;border-collapse:collapse\"><tr><th></th><th>&nbsp;Skin&nbsp;</th><th>&nbsp;Hair&nbsp;</th><th>&nbsp;Nails&nbsp;</th></tr><tr><td><i>Trichophyton</i></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td><i>Microsporum</i></td><td>✓</td><td>{{c1::✓}}</td><td>{{c1::✗}}</td></tr><tr><td><i>Epidermophyton</i></td><td>✓</td><td>{{c2::✗}}</td><td>{{c2::✓}}</td></tr></table></div>"
_c("localizacao")["extra"] = "- Microsporum spares the nails; Epidermophyton spares the hair<br>- Nannizzia, like Microsporum, spares the nails"

# textos vivos (correções de comentários de Davi feitas ao vivo) trazidos à spec, 15/10
_c('localizacao')["text"] = "<div data-nebli-organizacao=\"true\">Sites infected by each <b>dermatophyte</b> genus:<br><table style=\"margin:auto;border-collapse:collapse\"><tbody><tr><th></th><th>&nbsp;Skin&nbsp;</th><th>&nbsp;Hair&nbsp;</th><th>&nbsp;Nails&nbsp;</th></tr><tr><td><i>Trichophyton</i></td><td>{{c2::Yes}}</td><td>{{c2::Yes}}</td><td>{{c2::Yes}}</td></tr><tr><td><i>Microsporum</i></td><td>{{c3::Yes}}</td><td>{{c3::Yes}}</td><td>{{c3::Rarely}}</td></tr><tr><td><i>Epidermophyton</i></td><td>{{c1::Yes}}</td><td>{{c1::No}}</td><td>{{c2::Yes}}</td></tr></tbody></table></div>"
_c('localizacao')["extra"] = "- Microsporum is the classic agent of scalp ringworm (tinea capitis) and rarely reaches the nails<br>- Epidermophyton spares the hair"
_c('localizacao')["flags"] = {n: list(_c('localizacao')["flags"].values())[0] for n in [1, 2, 3]}

# textos vivos (correções de comentários de Davi feitas ao vivo) trazidos à spec, 15/10
_c('localizacao')["text"] = "<div data-nebli-organizacao=\"true\">Sites infected by each <b>dermatophyte</b> genus:<br><table style=\"margin:auto;border-collapse:collapse\"><tbody><tr><th></th><th>&nbsp;Skin&nbsp;</th><th>&nbsp;Hair&nbsp;</th><th>&nbsp;Nails&nbsp;</th></tr><tr><td><i>Trichophyton</i></td><td>{{c2::Yes}}</td><td>{{c2::Yes}}</td><td>{{c2::Yes}}</td></tr><tr><td><i>Microsporum</i></td><td>{{c3::Yes}}</td><td>{{c3::Yes}}</td><td>{{c3::Rarely}}</td></tr><tr><td><i>Epidermophyton</i></td><td>{{c1::Yes}}</td><td>{{c1::No}}</td><td>{{c1::Yes}}</td></tr></tbody></table></div>"
_c('localizacao')["extra"] = "Dermatophytes are&nbsp;"
_c('localizacao')["flags"] = {n: list(_c('localizacao')["flags"].values())[0] for n in [1, 2, 3]}
