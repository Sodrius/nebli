# Especificação curada — Grand Round 3, Espondilodiscite tuberculosa (UC03 P3, Grand Round; 48 lâminas; Micobactérias e diagnóstico de TB).
# Ordem = lâminas. AnKing → externos → autoral curto só para item do material de base sem card nos acervos; cards já vivos entram por sh().
import json, re, urllib.request
RUN_ID = "uc03-gr03-20261011a"
SHORT = "gr03"
LESSON = "2026-uc03-grand-round-03-espondilodiscite-tuberculosa"
DECK = "NEBLI::UC03::P3::Grand Round::Grand Round 3 (espondilodiscite tuberculosa)"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261011-CLAUDE-06) + plano vigente, 11/10/2026"
MEDIA = {"gr3-rm.jpg": "img/gr3-rm.jpg", "gr3-tc.jpg": "img/gr3-tc.jpg", "gr3-hist-osso.jpg": "img/gr3-hist-osso.jpg"}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 48 consultas; busca/ext.txt, 30 consultas; busca/extra-lacunas.txt, 32 consultas), cópias NEBLI vivas de "
         "Inflamação granulomatosa, Patogenicidade, Morfologia, Controle microbiológico, Antibióticos, Ativação de linfócitos T e GR2 conferidas (compartilhados), 12/10: ")
EXCLUIDOS = [
    (1503253636167, "BCG falso-positivo no PPD repetido: mesmo alvo do card mantido (1495602797038)"),
    (1557341550076, "Pott = TB das vértebras repetido: mesmo alvo do card mantido (1402595580027)"),
    (1552866512920, "IGRA com menos falsos positivos pela BCG: repete o alvo do card mantido"),
    (1578776293012, "IGRA não é influenciado pela BCG (V/F): repete o alvo do card mantido"),
    (1503253558548, "Exposição à M. tuberculosis sempre positiva no PPD: afirmação enganosa para anergia em HIV"),
    (1503254160003, "TNF e granuloma: o alvo já está em sh 1791716422184 e 1791716458533 (Inflamação granulomatosa)"),
    (1503257240955, "KatG/isoniazida: farmacologia da UC19, sem item no caso"),
    (1467833865131, "Rifamicinas inibem RNA polimerase: farmacologia da UC19; a lâmina cobra a mutação em rpoB"),
]
FORA_DO_RECORTE = [
    "Técnica cirúrgica, antibioticoterapia empírica do caso e esquema de tratamento da TB (lâmina não ensina)",
    "BCG como imunoterapia do câncer (prova de Imuno 2015, aula de Imunologia dos tumores)",
]

_cache = {}
def _nums(src):
    if src not in _cache:
        r = json.load(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8765", json.dumps(
            {"action": "notesInfo", "version": 6, "params": {"notes": [src]}}).encode())))["result"][0]
        _cache[src] = sorted({int(n) for n in re.findall(r"\{\{c(\d+)::", r["fields"]["Text"]["value"])})
    return _cache[src]


def ak(key, src, cor, bloco, alvo, slide, motivo, origin=None, **kw):
    flags = {n: cor for n in _nums(src)}
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, cor, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    n = sorted({int(x) for x in re.findall(r"\{\{c(\d+)::", text)})
    return dict(key=key, kind="autoral", text=text, extra=extra, flags={i: cor for i in n}, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


A_, B_, C_, D_, E_, F_ = ("A-caso-clinico", "B-granuloma-e-histologia", "C-micobacteria-e-virulencia", "D-diagnostico-direto", "E-resistencia", "F-tb-latente")
# espelhos AnKing por função (nids lidos nas buscas)
E_DIAG = [1503250260788, 1503260203735]
E_ZN = [1500418458789, 1500402778103]
E_MEDIO = [1503250389966, 1582847241587]
E_IMUNO = [1503255940872, 1556359015086]
E_RESIST = [1503260203735, 1503251440902, 1503250260788]
E_COLUNA = [1402595580027, 1585757172488, 1523626995563]
E_GRAN = [1503252725841, 1503253919933]
E_BIO = [1503250466324, 1503250702223, 1503250260788]
E_LAM = [1503255940872, 1503250807472]
NB = "sem card no AnKing nem nos externos (anking.txt, ext.txt)."

CARDS = [
 # ---------- A. Caso clínico (lâminas 1–14) ----------
 ak("reativacao", 1503252081815, V, A_, "TB secundária por reativação com imunossupressão (HIV)", 1, "Verde: HY 1, central para o paciente com HIV do caso."),
 sh(1791716438427, "azul", A_, "HIV avançado deixa granulomas mal formados", 1, "Azul: prova 2016 P2 3.4; card da Inflamação granulomatosa."),
 ak("pott-def", 1402595580027, V, A_, "Doença de Pott: TB nos corpos vertebrais", 2, "Verde: HY 1; é o diagnóstico do caso."),
 ak("espondilodiscite", 1609292245422, V, A_, "Infecção vertebral começa como discite e progride a osteomielite; piogênica ou tuberculosa", 2,
    "Verde: define a espondilodiscite do caso e cita a etiologia tuberculosa; frente reescrita sem os blocos HTML do original e extra sem a figura externa.", origin="Referências Externas",
    text="<b>Bacterial infections</b> of the <u>spine</u> usually begin as {{c1::discitis}} before progressing to {{c1::osteomyelitis}}, and can be due to <b>{{c2::pyogenic}}</b> as well as {{c2::tuberculous organisms}}",
    extra="- Chronic back pain without fever or leukocytosis suggests spinal <b>tuberculosis</b><br>- Acute cases show fever, leukocytosis, high ESR and CRP"),
 au("pott-clinica", "<b>Spinal tuberculosis</b> typically causes progressive {{c1::back pain}} with weight loss and low-grade fever", Z, A_,
    "Quadro clínico da TB vertebral", "2; Robbins cap. 26", "central", NB, E_COLUNA, "Azul: lâmina 2 (lombalgia, perda de 12 kg); Robbins.",
    extra="- Pain on movement and local spinal tenderness<br>- Hematogenous seeding from a visceral focus"),
 ak("osteo-vertebral-clinica", 1526330529038, V, A_, "Osteomielite vertebral: dor focal e sintomas constitucionais", 2, "Verde: HY 2; lombalgia com perda de peso do caso."),
 ak("osteo-vertebral-local", 1520180650147, V, A_, "Osteomielite do adulto ocorre nos corpos vertebrais", 2, "Verde: HY 1; localização da infecção do caso."),
 ak("ppd-hiv-falso", 1555875929217, Z, A_, "PPD falsamente negativo no HIV grave", 2, "Azul: o caso tem PPD de 0 mm com HIV; extra do AnKing mantido."),
 au("pcr-vhs", "<b>Vertebral infection</b> typically raises {{c1::ESR and CRP}} markedly", R, A_, "Marcadores inflamatórios na infecção vertebral", "5",
    "central", NB, E_COLUNA, "Rosa: VHS 135 e PCR 145,7 do caso; detalhe de apoio.", extra="- Normal values make spinal infection unlikely"),
 sh(1791054020796, "azul", A_, "RM é o melhor exame para osteomielite", 4, "Azul: lâmina 4; card da Diabetes (GR2)."),
 sh(1791054020921, "azul", A_, "Medula infectada é hiperintensa em T2 com supressão de gordura", 4, "Azul: lâmina 4; card da Diabetes (GR2)."),
 au("rm-espond", '<img src="gr3-rm.jpg"><br>This sagittal lumbar <b>MRI</b> shows infection of the disc and adjacent vertebrae, called {{c1::spondylodiscitis}}', Z, A_,
    "Reconhecer espondilodiscite na RM", "4", "central", NB, E_COLUNA, "Azul: lâmina 4 (RM L2-L3); reconhecimento sem legenda.",
    extra="- <b>T2 fat-sat</b> (right) shows bright marrow and disc<br>- <b>T1</b> (left) shows dark marrow",
    ),
 au("pedir-micobacteria", "In <b>subacute spondylodiscitis</b>, bone samples should also be sent for {{c1::mycobacterial}} culture and PCR", Z, A_,
    "Investigar micobactéria na espondilodiscite subaguda", "6", "central", NB, E_COLUNA, "Azul: lâmina 6, decisão da Infectologia que muda o caso.",
    extra="- Pyogenic cultures alone miss <b>tuberculosis</b>"),
 au("tc-miliar", '<img src="gr3-tc.jpg"><br>Tiny nodules scattered at <b>random</b> through both lungs on CT form a {{c1::miliary}} pattern', Z, A_,
    "Padrão miliar na TC de tórax", "7", "central", NB, E_GRAN, "Azul: lâmina 7; reconhecimento do padrão que sugere disseminação.",
    extra="- Reflects <b>hematogenous</b> dissemination of the bacilli"),
 au("paucibacilar", "In <b>paucibacillary</b> extrapulmonary TB, smear and culture are often {{c1::negative}}", V, A_,
    "Baixa sensibilidade dos testes diretos na TB extrapulmonar", "8; 10", "central", NB, E_DIAG, "Verde: o caso inteiro gira em culturas e BAAR negativos com TB confirmada por TRM e histologia.",
    extra="- Few bacilli per sample<br>- Histology and <b>molecular</b> tests then guide the diagnosis"),
 au("aerossol-precaucao", "<b>Airborne precautions</b> are started when {{c1::pulmonary}} tuberculosis is suspected", R, A_,
    "Precaução para aerossóis", "9", "lateral", NB, E_DIAG, "Rosa: lâmina 9; conduta de proteção.", extra="- Cavitary disease is the main source of <b>aerosols</b>"),
 sh(1791746131901, "azul", A_, "TB esquelética não é contagiosa", 9, "Azul: lâmina 9; explica por que a precaução decorre da suspeita pulmonar."),
 sh(1791592721894, "rosa", A_, "Pigmento antracótico: macrófagos com carbono", 11, "Rosa: pigmento no laudo da biópsia transbrônquica; card da Patologia ambiental."),
 sh(1791716431615, "azul", A_, "Ausência de caseação na biópsia não exclui TB", 11, "Azul: lâmina 11 (biópsia transbrônquica sem granuloma)."),
 au("trace", "An Xpert <b>trace</b> result means {{c1::very low}} MTB DNA, so rifampicin resistance cannot be determined", Z, A_,
    "Resultado em traços do Xpert", "12", "central", NB, E_DIAG, "Azul: lâmina 12 (resistência indeterminada).",
    extra="- Resistance stays <b>inconclusive</b> at this load"),
 au("trace-interpret", "A <b>trace</b> result counts as positive in {{c1::HIV}}, children under 10 and extrapulmonary samples", Z, A_,
    "Interpretar traços no Xpert", "12", "central", NB, E_DIAG, "Azul: regra impressa na lâmina 12 (Ministério da Saúde).",
    extra="- In other groups a trace is <b>inconclusive</b>"),
 au("trm-amostras", "<b>Xpert</b> also works on CSF, pleural fluid, lymph node, biopsies and urine, not only {{c1::sputum}}", Z, D_,
    "Amostras do Xpert (inclui fragmento ósseo do caso)", "13; 41", "central", NB, E_DIAG, "Azul: lâminas 13 e 41.", extra="- Bone fragment of the case gave MTB detected"),
 au("granuloma-osso", "<b>Necrotizing granulomas</b> in bone suggest {{c1::tuberculosis}}, but special stains and cultures must exclude fungi", Z, A_,
    "Granuloma necrotizante no osso exige confirmação", "14", "central", NB, E_GRAN, "Azul: laudo da lâmina 14 (BAAR e fungos inconclusivos).",
    extra="- Fungi such as <b>Paracoccidioides</b> also form granulomas"),
 # ---------- B. Granuloma e histologia (15–22) ----------
 sh(1791716421256, "verde", B_, "APC libera IL-12 e diferencia Th1", 15, "Verde: esquema da lâmina 15; card da Inflamação granulomatosa."),
 sh(1791625436658, "verde", B_, "Th1 libera IFN-γ: epitelioides e células gigantes", 15, "Verde: esquema da lâmina 15; prova 2015."),
 sh(1791716422184, "verde", B_, "TNF mantém o granuloma na TB", 15, "Verde: esquema da lâmina 15."),
 sh(1791716404503, "verde", B_, "Definição de granuloma", 15, "Verde: lâmina 15; Robbins."),
 sh(1791763624470, "azul", B_, "Controle da TB depende de imunidade celular, não de anticorpos", 15, "Azul: lâmina 15; card da Patogenicidade."),
 sh(1791716427876, "azul", B_, "Reconhecer necrose caseosa central com fibrose", 16, "Azul: lâmina 16, histologia."),
 sh(1791716427402, "azul", B_, "Necrose caseosa tem aspecto de queijo", 16, "Azul: lâmina 16."),
 sh(1791716425027, "azul", B_, "Células de Langhans têm núcleos periféricos", 17, "Azul: lâmina 17."),
 au("granuloma-osso-img", '<img src="gr3-hist-osso.jpg"><br>This <b>bone marrow</b> focus with a multinucleated giant cell is a {{c1::granuloma}}', Z, B_,
    "Reconhecer granuloma na medula óssea", "18", "central", NB, E_GRAN, "Azul: lâmina 18; reconhecimento do granuloma ósseo sem legenda.",
    extra="- Epithelioid macrophages and lymphocytes surround the <b>giant cell</b>"),
 sh(1791716437955, "azul", B_, "Padrão miliar pulmonar", 19, "Azul: lâmina 19 (grãos de painço)."),
 sh(1791716437500, "azul", B_, "TB miliar vem de bacteremia", 19, "Azul: lâmina 19."),
 sh(1791716426458, "azul", B_, "Agregado circunscrito de epitelioides é um granuloma", 20, "Azul: lâmina 20."),
 sh(1791716426943, "rosa", B_, "Granulomas do mesmo pulmão diferem em necrose e fibrose", 21, "Rosa: lâmina 21."),
 sh(1791716438930, "rosa", B_, "Granuloma do HIV tem coroa linfocitária escassa", 21, "Rosa: prova 2016 P2 3.4."),
 ak("miliar-orgaos", 1503253919933, V, B_, "TB miliar semeia baço, fígado, suprarrenal e meninges", 22, "Verde: HY 2; macroscopia e histologia da lâmina 22."),
 sh(1791716429751, "verde", B_, "Reconhecer BAAR em fundo azul", 22, "Verde: lâmina 22; card da Inflamação granulomatosa."),
 # ---------- C. Micobactéria e virulência (23–34) ----------
 au("taxonomia", "The genus <b>Mycobacterium</b> belongs to the order {{c1::Actinomycetales}}", R, C_, "Taxonomia", "23; Trabulsi", "lateral", NB, E_BIO,
    "Rosa: lâmina 23; detalhe de classificação.", extra="- Phylum and class <b>Actinobacteria</b><br>- Family Mycobacteriaceae"),
 sh(1791576674292, "verde", C_, "BAAR: ácido micólico e Ziehl-Neelsen", 23, "Verde: lâmina 23; card da Morfologia."),
 ak("aerobio", 1503250466324, V, C_, "M. tuberculosis é aeróbio estrito", 23, "Verde: HY 1; lâmina 23 cita aeróbios.",
    ),
 sh(1791746122586, "azul", C_, "Bactéria intracelular facultativa vive em outras células se necessário", 23, "Azul: lâmina 23; card da Patogenicidade."),
 au("espectro", "Most <b>Mycobacterium</b> species are environmental {{c1::saprophytes}}, whereas M. tuberculosis is an obligate pathogen", R, C_,
    "Saprófitos, oportunistas e patógenos obrigatórios", "23", "lateral", NB, E_BIO, "Rosa: lâmina 23.", extra="- Some are opportunistic, mainly in <b>AIDS</b>"),
 au("rapido", "<b>Rapidly growing</b> mycobacteria form colonies in under {{c1::7 days}} and are mostly environmental", R, C_, "Crescimento rápido", "24", "lateral", NB, E_DIAG,
    "Rosa: lâmina 24 (número).", extra="- The M. tuberculosis complex is <b>slow</b> growing"),
 ak("lento", 1503250260788, V, C_, "M. tuberculosis cresce devagar, semanas", 24, "Verde: HY 2; explica cultura lenta e tratamento longo."),
 au("td-ecoli", "<b>M. tuberculosis</b> divides every few {{c1::hours}}, whereas E. coli divides in about 20 minutes", Z, C_, "Velocidade de divisão", "24; prova 2025 P2 3.2", "prova", NB, E_DIAG,
    "Azul: lâmina 24 e prova 2025.", extra="- Long lag phase and slow log phase on the growth curve"),
 au("parede-lipidos", "About {{c1::60%}} of the mycobacterial <b>cell wall</b> is lipid, mostly mycolic acids", R, C_, "Parede rica em lipídeos", "25; Trabulsi", "lateral", NB, E_ZN,
    "Rosa: número de livro.", extra="- Mycolic acids have 60 to 90 carbons"),
 sh(1791716451309, "rosa", C_, "LAM faz parte do envelope", 25, "Rosa: lâmina 25 (glicolipídeos)."),
 sh(1791716450848, "azul", C_, "Arabinogalactano liga peptidoglicano aos ácidos micólicos", 25, "Azul: lâminas 25 e 26."),
 sh(1791666340566, "azul", C_, "Micobactérias resistem a desinfetantes depois dos esporos", 25, "Azul: prova 2025 P2 3.3 (esterilização)."),
 au("gram-fraco", "<b>Mycobacteria</b> are only {{c1::weakly}} Gram-positive, so Ziehl-Neelsen staining is preferred", Z, C_, "Gram fraco; usar Ziehl-Neelsen", "25; prova 2023 P2 3.3", "prova", NB, E_ZN,
    "Azul: prova 2023.", extra="- Thin peptidoglycan under a thick <b>mycolic</b> acid layer"),
 sh(1791576674542, "azul", C_, "Ziehl-Neelsen usa carbol fucsina", 27, "Azul: lâminas 27 e 28."),
 au("zn-descorante", "In <b>Ziehl-Neelsen</b> staining, {{c1::acid-alcohol}} decolorizes every cell except acid-fast bacilli", Z, C_, "Descoramento com ácido-álcool", "28; Trabulsi", "central", NB, E_ZN,
    "Azul: lâmina 28.", extra="- Bacilli keep the red <b>fuchsin</b>"),
 au("zn-contra", "After decolorization, non-acid-fast cells take up the {{c1::methylene blue}} <b>counterstain</b>", Z, C_, "Contracorante", "28", "central", NB, E_ZN, "Azul: lâmina 28.",
    extra="- Background and other bacteria look blue"),
 au("nb3", "<b>M. tuberculosis</b> cultures are handled in {{c1::biosafety level 3}} laboratories", Z, C_, "Laboratório NB3", "29", "central", NB, E_DIAG, "Azul: lâmina 29.",
    extra="- Because of aerosol transmission"),
 au("aerossol-transm", "<b>Tuberculosis</b> spreads by {{c1::aerosol}} droplet nuclei, so staff need respirators", R, C_, "Transmissão por aerossol e EPI", "29", "lateral", NB, E_DIAG,
    "Rosa: lâmina 29.", extra="- 1 to 10 bacilli can infect"),
 au("mtbc-clonal", "Members of the <b>M. tuberculosis complex</b> are over 99% identical and show no {{c1::horizontal}} gene transfer", Z, C_, "Complexo clonal", "30", "central", NB, E_BIO,
    "Azul: lâmina 30.", extra="- Resistance arises by <b>mutation</b>, not plasmids"),
 au("bcg-rd1", "<b>BCG</b> is an attenuated M. bovis strain that lost the {{c1::RD1}} region", Z, C_, "BCG e RD1", "31", "central", NB, E_IMUNO, "Azul: lâmina 31.",
    extra="- RD1 encodes <b>ESAT-6</b> and CFP-10, the antigens used in IGRA"),
 au("mtbc-hospedeiros", "<b>M. tuberculosis</b> mainly infects humans, whereas M. bovis mainly infects {{c1::cattle}}", R, C_, "Hospedeiros do complexo", "30; 32", "lateral", NB, E_BIO,
    "Rosa: lâminas 30 e 32.", extra="- M. bovis can also infect humans"),
 sh(1791716419358, "verde", C_, "M. tuberculosis vive em macrófagos", 33, "Verde: lâmina 33; card da Inflamação granulomatosa."),
 sh(1791746131503, "verde", C_, "Bloqueio da fusão fagossomo-lisossomo", 33, "Verde: lâmina 33; prova 2025."),
 sh(1791746131627, "azul", C_, "ManLAM bloqueia a maturação do fagossomo", 33, "Azul: lâmina 33; card da Patogenicidade."),
 au("resiste-acido", "Even in acidified <b>phagosomes</b>, M. tuberculosis keeps its own pH with an {{c1::efflux}} pump", Z, C_, "Resistência ao fagossomo ácido", "33; prova 2025 P2 3.4", "prova", NB, E_BIO,
    "Azul: lâmina 33 e prova 2025.", extra="- Acid alone does not kill every bacillus"),
 au("fagossomo-citosol", "Some <b>M. tuberculosis</b> bacilli escape the phagosome and live free in the {{c1::cytosol}}", Z, C_, "Escape para o citosol", "33; prova 2025 P2 3.4", "prova", NB, E_BIO,
    "Azul: lâmina 33 e prova 2025.", extra="- The third persistence mechanism, with blocked fusion and efflux"),
 au("dormencia", "<b>Mycobacteria</b> form no spores but enter {{c1::dormancy}}, in which antibiotics barely act", V, C_, "Dormência", "23; 33", "central", NB, E_BIO,
    "Verde: explica latência e tratamento longo.", extra="- Dormant bacilli reactivate under <b>immunosuppression</b>"),
 au("dormencia-tratamento", "Because dormant bacilli tolerate antibiotics, <b>tuberculosis</b> therapy lasts {{c1::months}}", Z, C_, "Tratamento longo por dormência", "33; prova 2023 P2 3.4", "prova", NB, E_RESIST,
    "Azul: lâmina 33 e prova 2023.", extra="- Several drugs together also prevent resistance"),
 sh(1791668528039, "azul", C_, "Associação de drogas retarda a resistência", 33, "Azul: prova 2023; card dos Antibióticos."),
 sh(1791716448950, "rosa", C_, "Granuloma é rede dinâmica, não parede", 34, "Rosa: lâmina 34 (fortaleza que contém)."),
 sh(1791716405608, "azul", C_, "Granuloma fibrótico ainda abriga bacilos viáveis", 34, "Azul: lâmina 34."),
 au("granuloma-tipos", "Tuberculous <b>granulomas</b> progress from solid to caseous to {{c1::cavitary}} lesions", Z, C_, "Sólido, caseoso e cavitário", "34", "central", NB, E_GRAN,
    "Azul: lâmina 34.", extra="- Cavitation opens the lesion into an airway"),
 sh(1791716436082, "verde", C_, "Cavidade se forma quando o caseum drena para a via aérea", 34, "Verde: lâmina 34."),
 au("bacilifero", "A patient whose <b>cavitary lesion</b> releases bacilli into sputum is called {{c1::bacilliferous}}", Z, C_, "Paciente bacilífero", "34", "central", NB, E_GRAN,
    "Azul: lâmina 34.", extra="- Main source of new infections"),
 # ---------- D. Diagnóstico direto (35–42) ----------
 ak("latente", 1503253427380, V, F_, "TB latente: PPD ou IGRA positivo com radiografia normal", 35, "Verde: HY 2; define TB latente."),
 sh(1791763642743, "azul", F_, "TB latente não tem sintomas nem transmite", 35, "Azul: lâmina 35; card da Patogenicidade."),
 au("escarro-naoh", "<b>Sputum</b> is decontaminated with {{c1::2% NaOH}} before culture", R, D_, "Descontaminação", "36", "lateral", NB, E_DIAG, "Rosa: lâmina 36.",
    extra="- Kills fast-growing contaminants"),
 au("escarro-nalc", "<b>N-acetyl-L-cysteine</b> {{c1::liquefies}} mucus during sputum processing", R, D_, "Liquefação do muco", "36", "lateral", NB, E_DIAG, "Rosa: lâmina 36.",
    extra="- Used with sodium citrate"),
 au("escarro-pbs", "After decontamination, <b>sputum</b> is {{c1::neutralized}} with PBS before smear and culture", R, D_, "Neutralização", "36", "lateral", NB, E_DIAG, "Rosa: lâmina 36.",
    extra="- Neutralized after 15 to 20 minutes"),
 au("bacilo-sens", "<b>Smear microscopy</b> detects 60 to 80% of TB but only {{c1::20 to 30%}} of paucibacillary cases", Z, D_, "Sensibilidade da baciloscopia", "37", "central", NB, E_DIAG,
    "Azul: lâmina 37.", extra="- Sensitivity depends on the <b>bacillary load</b>"),
 au("bacilo-limiar", "A positive <b>smear</b> needs about {{c1::1,000 to 10,000}} CFU/mL in the sample", R, D_, "Limiar da baciloscopia", "37", "lateral", NB, E_DIAG, "Rosa: lâmina 37 (número).",
    extra="- PCR detects as few as 10 organisms"),
 sh(1791716430209, "azul", D_, "BAAR positivo não prova M. tuberculosis", 37, "Azul: lâmina 37 (especificidade)."),
 au("bacilo-seriada", "<b>Smear microscopy</b> should be repeated on up to {{c1::three}} serial samples", R, D_, "Coletas seriadas", "37", "lateral", NB, E_DIAG, "Rosa: lâmina 37.",
    extra="- Raises the chance of finding bacilli"),
 au("bacilo-indicacao", "<b>Smear microscopy</b> is recommended for respiratory symptomatics and in {{c1::extrapulmonary}} TB", R, D_, "Indicações da baciloscopia", "37", "lateral", NB, E_DIAG,
    "Rosa: lâmina 37.", extra="- Also with clinical or radiological suspicion"),
 au("mgit", "In the <b>MGIT</b> system, a fluorescent indicator reports bacterial growth through {{c1::oxygen}} consumption", Z, D_, "Princípio do MGIT", "38", "central", NB, E_MEDIO,
    "Azul: lâmina 38.", extra="- <b>7H9</b> Middlebrook broth with OADC"),
 ak("middlebrook", 1582847241587, Z, D_, "Middlebrook e caldos automatizados", 38, "Azul: lâmina 38 (MGIT 7H9)."),
 ak("lj", 1503250389966, V, D_, "M. tuberculosis cresce em Löwenstein-Jensen", 38, "Verde: HY 2; meio clássico da lâmina 38."),
 au("lj-composicao", "<b>Löwenstein-Jensen</b> medium is egg-based and contains {{c1::malachite green}} to inhibit Gram-positive bacteria", R, D_, "Composição do LJ", "38", "lateral", NB, E_MEDIO,
    "Rosa: lâmina 38.", extra="- Also asparagine, potato starch and glycerol"),
 au("lj-polimixina", "<b>Polymyxin B</b> in Löwenstein-Jensen medium inhibits {{c1::Gram-negative}} bacteria", R, D_, "Polimixina no LJ", "38", "lateral", NB, E_MEDIO,
    "Rosa: lâmina 38.", extra="- Malachite green blocks Gram-positives"),
 au("stonebrink", "<b>Stonebrink</b> medium, used for M. bovis, replaces glycerol with {{c1::pyruvate}}", R, D_, "Stonebrink", "38", "lateral", NB, E_MEDIO, "Rosa: lâmina 38.",
    extra="- Otherwise equal to Löwenstein-Jensen"),
 au("cultura-tempo", "<b>Culture</b> takes 21 to 60 days on Löwenstein-Jensen but only {{c1::7 to 14}} days in MGIT", Z, D_, "Tempo de cultura", "8; 39", "central", NB, E_MEDIO,
    "Azul: lâminas 8 e 39.", extra="- LJ is a solid egg-based medium, MGIT is a liquid broth"),
 au("cultura-sens", "<b>Culture</b> is more sensitive than smear, reaching {{c1::90 to 95%}} in MGIT", R, D_, "Sensibilidade da cultura", "39", "lateral", NB, E_MEDIO,
    "Rosa: lâmina 39 (número).", extra="- Löwenstein-Jensen reaches 80 to 85%"),
 au("cultura-resistencia", "Although slow for diagnosis, <b>culture</b> is essential to define the {{c1::resistance}} profile", Z, D_, "Cultura e antibiograma", "39", "central", NB, E_MEDIO,
    "Azul: lâmina 39.", extra="- Allows phenotypic susceptibility testing"),
 au("xpert-def", "The <b>Xpert MTB/RIF Ultra</b> detects M. tuberculosis and resistance to {{c1::rifampicin}} in a single test", V, D_, "Xpert MTB/RIF Ultra", "35; 40", "central", NB, E_DIAG,
    "Verde: teste rápido central do diagnóstico e do caso.", extra="- Result within hours instead of weeks"),
 au("rpob", "<b>Rifampicin</b> resistance usually arises from mutations in {{c1::rpoB}}, the RNA polymerase beta subunit gene", Z, E_, "Resistência à rifampicina e rpoB", "40; Trabulsi", "central", NB, E_RESIST,
    "Azul: lâmina 40 (RRDR) e Trabulsi.", extra="- About 96% of resistant strains"),
 au("rrdr-95", "Mutations in the <b>RRDR</b> explain about {{c1::95%}} of rifampicin resistance", R, E_, "RRDR", "40", "lateral", NB, E_RESIST, "Rosa: lâmina 40 (número).",
    extra="- RRDR means rifampicin resistance-determining region"),
 au("trm-sens", "<b>Xpert</b> sensitivity is about 98% in smear-positive TB but only {{c1::63 to 90%}} in smear-negative TB", R, D_, "Sensibilidade do Xpert", "41", "lateral", NB, E_DIAG,
    "Rosa: tabela da lâmina 41.", extra="- Rifampicin resistance detection reaches 93 to 95%"),
 au("tblam", "<b>TB-LAM</b> detects {{c1::lipoarabinomannan}} in the urine of patients co-infected with TB and HIV", Z, D_, "TB-LAM", "35; 42", "central", NB, E_LAM,
    "Azul: lâmina 42.", extra="- Point-of-care test for <b>active</b> TB"),
 au("tblam-sens", "<b>TB-LAM</b> is most sensitive when CD4 counts are {{c1::below 100}}", R, D_, "Sensibilidade do TB-LAM", "42", "lateral", NB, E_LAM, "Rosa: tabela da lâmina 42.",
    extra="- Very low in HIV-negative patients"),
 # ---------- E. Resistência (43–46) ----------
 au("dst-fenotipico", "<b>Phenotypic</b> susceptibility tests compare growth with a {{c1::critical concentration}} of each drug", R, E_, "Testes fenotípicos", "43; 46", "lateral", NB, E_RESIST,
    "Rosa: lâmina 43.", extra="- MIC uses several <b>dilutions</b>"),
 au("lpa1", "The <b>LPA-1</b> (MTBDRplus) detects M. tuberculosis complex and resistance to {{c1::rifampicin and isoniazid}}", Z, E_, "LPA-1", "35; 44", "central", NB, E_RESIST,
    "Azul: lâmina 44.", extra="- A line probe assay"),
 au("mdr", "<b>MDR-TB</b> is resistance to at least {{c1::isoniazid and rifampicin}}", Z, E_, "Definição de MDR-TB", "44; Trabulsi", "central", NB, E_RESIST,
    "Azul: Trabulsi; sustenta o LPA-1.", extra="- Both are first-line drugs"),
 au("lpa2", "The <b>LPA-2</b> (MTBDRsl) detects resistance to fluoroquinolones, aminoglycosides and {{c1::ethambutol}}", Z, E_, "LPA-2", "45", "central", NB, E_RESIST, "Azul: lâmina 45.",
    extra="- Tested after resistance in LPA-1"),
 sh(1791746131779, "rosa", E_, "Esquema básico: rifampicina, isoniazida, pirazinamida e etambutol", 45, "Rosa: lista de drogas da lâmina 45; card da Patogenicidade."),
 au("pza-bovis", "<b>M. bovis</b> is intrinsically resistant to {{c1::pyrazinamide}}", Z, E_, "M. bovis e pirazinamida", "45", "central", NB, E_RESIST, "Azul: lâmina 45.",
    extra="- Useful to tell it from <b>M. tuberculosis</b>"),
 au("drogas-novas", "<b>Bedaquiline</b>, delamanid and pretomanid are used against {{c1::drug-resistant}} TB", R, E_, "Drogas para TB resistente", "45", "lateral", NB, E_RESIST,
    "Rosa: lista da lâmina 45.", extra="- Also linezolid and clofazimine"),
 au("fluxo-grupos", "<b>Culture</b> with Xpert is indicated for risk groups such as {{c1::people with HIV}}, prisoners and the homeless", R, E_, "Grupos de risco do fluxograma", "46", "lateral", NB, E_DIAG,
    "Rosa: lista de 12 grupos da lâmina 46.", extra="- Also retreatment cases and healthcare workers"),
 au("fluxo-xpert-resist", "When <b>Xpert</b> shows rifampicin resistance, samples go to LPA-1 and LPA-2 {{c1::simultaneously}}", R, E_, "Fluxo com resistência", "46", "lateral", NB, E_RESIST,
    "Rosa: fluxograma da lâmina 46.", extra="- Then phenotypic tests if resistance is inferred"),
 au("fluxo-xpert-neg", "If <b>Xpert</b> is unavailable or rifampicin-negative, the sample goes first to {{c1::LPA-1}}", R, E_, "Fluxo sem Xpert", "46", "lateral", NB, E_RESIST,
    "Rosa: fluxograma da lâmina 46.", extra="- LPA-2 only follows detected or inferred resistance"),
 # ---------- F. TB latente (47–48) ----------
 sh(1791625436533, "verde", F_, "O PPD é hipersensibilidade tipo IV", 47, "Verde: lâmina 47; card da Ativação de linfócitos T."),
 ak("ppd-leitura", 1556359015086, V, F_, "Ler o PPD pela induração", 47, "Verde: HY 2; leitura correta × incorreta da lâmina 47."),
 au("ppd-72h", "The <b>tuberculin</b> skin test is read {{c1::48 to 72}} hours after injection", R, F_, "Tempo de leitura do PPD", "47; Trabulsi", "lateral", NB, E_IMUNO,
    "Rosa: lâmina 47 diz 72 h e o Trabulsi 48 h.", extra="- Measure the transverse diameter of the induration"),
 ak("bcg-falso", 1495602797038, V, F_, "BCG causa PPD falso-positivo", 47, "Verde: HY 1; prova 2025 P2 5.1."),
 ak("igra-medida", 1503255940872, V, F_, "IGRA mede IFN-γ de Th1", 48, "Verde: HY 1; lâmina 48."),
 ak("igra-bcg", 1503255912501, Z, F_, "IGRA não reage com BCG", 48, "Azul: HY 1 que repete o alvo do IGRA; representante verde é igra-medida.", hy_repete="HY repete o alvo do IGRA, já verde em igra-medida"),
 au("igra-antigenos", "<b>IGRA</b> stimulates T cells with {{c1::ESAT-6 and CFP-10}}, antigens absent from BCG", Z, F_, "Antígenos do IGRA", "48; prova 2025 P2 5.1", "prova", NB, E_IMUNO,
    "Azul: prova 2025.", extra="- Region <b>RD1</b> is deleted in BCG"),
 au("igra-passos", "In an <b>IGRA</b>, blood is stimulated with TB antigens and {{c1::ELISA}} measures the IFN-γ released", R, F_, "Etapas do IGRA", "48", "lateral", NB, E_IMUNO,
    "Rosa: etapas da lâmina 48.", extra="- It detects sensitized <b>T cells</b>, not the bacillus"),
 # ---------- Coluna: Robbins, prova e veteranos ----------
 au("pott-abscesso", "<b>Spinal TB</b> can form a paravertebral {{c1::cold}} abscess that tracks along the psoas", Z, A_, "Abscesso frio paravertebral", "2; Robbins cap. 8", "central", NB, E_COLUNA,
    "Azul: Robbins; complicação direta da espondilodiscite tuberculosa.", extra="- May appear as an abdominal or pelvic mass"),
 au("pott-complicacao", "Severe vertebral destruction in <b>Pott disease</b> causes kyphosis and spinal {{c1::cord}} compression", R, A_, "Complicações da doença de Pott", "2; Robbins cap. 26", "lateral", NB, E_COLUNA,
    "Rosa: Robbins.", extra="- Compression fractures produce kyphotic or scoliotic deformity"),
 au("pott-tc", "On CT, <b>vertebral TB</b> appears as an irregular lesion with a {{c1::hypoattenuating}} center and thick rim", R, A_, "TC da TB vertebral", "4; prova 2025 P2 3.1", "prova", NB, E_COLUNA,
    "Rosa: prova 2025 (RD) e apostila de Radiologia.", extra="- Hypoattenuation reflects <b>osteolysis</b>"),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
    "aerobio": "- Oxygen-rich tissue, such as the lung apex, favors growth",
    "lento": "- Slow division explains weeks of culture and months of therapy",
    "middlebrook": "- MGIT is a Middlebrook 7H9 broth system",
    "lj": "- Slow growth: colonies appear after weeks",
    "ppd-leitura": "- Measure the raised, hard induration, not the redness",
}
DUPLICACAO = {
    "rm-espond": "ganho: reconhecer a espondilodiscite na RM da lâmina 4; o outro card define a doença em texto",
    "tc-miliar": "ganho: reconhecer o padrão miliar na TC da lâmina 7; o outro card cobra os órgãos semeados",
    "granuloma-osso": "ganho: histologia óssea do caso e a necessidade de confirmação etiológica; o outro card é a definição genérica",
}  # chave autoral: "ganho: ..." quando a resposta coincide com outro card
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k]
    if k in DUPLICACAO:
        c["duplicacao_ok"] = DUPLICACAO[k]


# ---- revisão Opus (12/10) ----
def _cc(key):
    return next(c for c in CARDS if c["key"] == key)
_cc("td-ecoli")["extra"] = "- Reported generation times range from about 5 to 24 hours<br>- Long lag phase and slow log phase on the growth curve"
_cc("resiste-acido")["text"] = "<b>M. tuberculosis</b> survives even inside <b>phagosomes</b> that {{c1::acidify}}"
_cc("resiste-acido")["extra"] = "- The other persistence mechanisms are blocked lysosome fusion and escape to the cytosol"
