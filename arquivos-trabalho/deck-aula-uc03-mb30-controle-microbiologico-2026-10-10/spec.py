# Especificação curada — Controle microbiológico (UC03 P2, Microbiologia, aula 30; Prof. Nilton Lincopan; 57 lâminas de 2026).
# Gerada a partir de inventario.py (escrito antes). Fontes: lâminas, Aula 04 da turma (Profa. Elisabete Vicente, I e II), bibliografias
# (Timenetsky), prova 2025 P2 3.3, monitoria P2 aula 3, guia de veteranos de Micro aula 3, Trabulsi 6ª cap. 7. Vídeos dispensados (F-06).
# Ordem = slides. AnKing → externos → autoral curto só para item do material de base sem card nos acervos. Foco em compreensão (F-04).
RUN_ID = "uc03-mb30-20261010a"
SHORT = "mb30"
LESSON = "2026-uc03-microbiologia-30-controle-microbiologico"
DECK = "NEBLI::UC03::P2::Microbiologia::Controle microbiológico"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261010-CLAUDE-06) + plano de 08/10 ajustado em 10/10, 10/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt: sterilization/autoclave, disinfect/antisep, spore, alcohol, "
         "chlorhexidine/quats/iodine/hypochlorite, peroxide, aldehydes/ethylene oxide, UV, pasteurization, HEPA/filter, cidal/static, prion, "
         "Semmelweis/Lister/hand hygiene, GBS, D value), 10/10: ")
EXCLUIDOS = [
 (1500764054910, "iodo por halogenação: repete o card de iodo (1522249984884)"),
 (1519774077119, "rastreio de GBS 36–38 semanas: diverge da lâmina (35–37) e é clínica; a profilaxia já representa a lâmina 30"),
 (1520355448386, "príons e autoclave: fora da aula"),
 (1467819685605, "reparo por excisão de nucleotídeos: aula de DNA, não de controle"),
 (1500150924946, "Giardia, fervura e iodo: clínica lateral sem ganho de compreensão"),
 (1489092729957, "β-lactâmicos bactericidas: aula de Antibióticos"),
]
FORA_DO_RECORTE = [
 "Lâminas 2–5 e 7–9 (o que são micro-organismos, bactérias em todo lugar, microbiota): contexto de abertura",
 "Lâmina 11 (lista de infecções) e 16 (imunossupressão): contexto; lâmina 32 (caso de Pseudomonas): ilustração",
 "Videoaula da Aula 08 (técnica de semeadura, Prática 1) e roteiro de antibiograma/antimicrobianos naturais: outras aulas",
 "Microondas, ondas supersônicas, centrifugação: só citados",
]


def ak(key, src, flags, bloco, alvo, slide, motivo, origin=None, **kw):
    d = dict(key=key, kind="text", src=src, manter=True, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo, **kw)
    if origin: d["origin"] = origin
    return d


def au(key, text, flags, bloco, alvo, slide, autoria, falta, espelhos, motivo, extra="", duplicacao_ok=""):
    return dict(key=key, kind="autoral", text=text, extra=extra, flags=flags, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", autoria=autoria,
                busca=BUSCA + falta, espelhos=espelhos, motivo=motivo, duplicacao_ok=duplicacao_ok)


def sh(nid, cor, bloco, alvo, slide, motivo):
    return dict(key=f"sh-{nid}", kind="compartilhado", nid=nid, cor=cor, bloco=bloco, alvo=alvo, evid=f"Slide {slide}", motivo=motivo)


DEF = [1500763589237, 1500763397436]
KIL = [1522249843346, 1500764215465]
HEAT = [1500763633935, 1524405599297]
A_, B_, C_, D_, E_, F_, G_ = ("A-abertura", "B-conceitos", "C-resistencia-e-cinetica", "D-historia", "E-calor", "F-filtracao-e-radiacao", "G-quimicos")
CARDS = [
 # ---------- A. Abertura (lâminas 6–16) ----------
 sh(1791647812370, "azul", A_, "Fissão binária", 6, "Nota viva da Fisiologia bacteriana; lâmina 6 repete."),
 au("crescimento-exp", "After n generations of binary fission, N<sub>0</sub> bacteria become N<sub>0</sub> × {{c1::2<sup>n</sup>}}", {1: Z}, A_,
    "Crescimento exponencial", "6", "central", "sem card da fórmula.", [1500763633935, 1522249843346], "Azul: lâmina 6.",
    extra="- With 20-minute generations, one cell exceeds a billion in about 10 hours"),
 au("probioticos", "Live beneficial bacteria such as <i>Lactobacillus casei</i> in yogurt are called {{c1::probiotics}}", {1: R}, A_,
    "Probióticos", "9–10", "lateral", "sem card.", DEF, "Rosa: abertura."),
 au("transmissao", "Bacteria spread by direct contact, as with hands, and indirectly through {{c1::aerosols}}", {1: R}, A_,
    "Modos de transmissão", "12–13", "lateral", "sem card.", DEF, "Rosa: abertura.", extra="- Hands are the main target of infection control"),
 au("zona-perigo", "Food left between 5 °C and 60 °C, the temperature {{c1::danger zone}}, lets bacteria multiply", {1: R}, A_,
    "Crescimento em alimentos", "14–15", "lateral", "sem card.", DEF, "Rosa: abertura.", extra="- Refrigeration below 5 °C keeps growth slow"),
 # ---------- D/B. História e conceitos (lâminas 17–26) ----------
 au("historia", "Ancient Persians stored drinking water in {{c1::copper and silver}} vessels to keep it safe", {1: R}, D_,
    "Controle antes da microbiologia", "18–20; Trabulsi", "lateral", "sem card.", DEF, "Rosa: história.",
    extra="- Egyptians dried mummies with natron salts; salting and drying preserved food"),
 ak("esterilizacao", 1500763589237, {1: V}, B_, "Esterilização", 21, "Verde: conceito central; prova 2025."),
 ak("desinfeccao", 1500763397436, {1: V}, B_, "Desinfecção", 21, "Verde: conceito central."),
 au("desinfeccao-esporos", "Unlike sterilization, {{c1::disinfection}} need not kill bacterial spores", {1: V}, B_,
    "Desinfecção não exige matar esporos", "21, 49; bibliografia; guia", "central", "sem card do contraste.", DEF, "Verde: diferença decisiva.",
    extra="- It targets vegetative pathogens, down to safe levels", duplicacao_ok="ganho: o AnKing define desinfecção; aqui é a diferença com a esterilização (esporos)"),
 au("antissepsia", "Disinfection of living tissue such as skin and mucosa is called {{c1::antisepsis}}", {1: V}, B_,
    "Antissepsia", "21, 25, 49; Trabulsi", "central", "sem card.", DEF, "Verde: lâminas 25 e 49.",
    extra="- Antiseptics must be low in toxicity, since they touch living cells"),
 au("assepsia", "{{c1::Asepsis}} is the set of techniques that keep a sterile object or area from being contaminated", {1: Z}, B_,
    "Assepsia", "21, 36; bibliografia; Trabulsi", "central", "sem card.", DEF, "Azul: termo vizinho.", extra="- Asepsis prevents contamination; antisepsis removes it"),
 au("resistencia-topo", "The microbial forms most resistant to disinfection and sterilization are bacterial {{c1::spores}}", {1: V}, C_,
    "Topo da escala de resistência", "22", "central", "sem card da escala.", KIL, "Verde: lâmina 22.", extra="- So sterilization is validated against spores"),
 sh(1791163038847, "rosa", C_, "Ácido dipicolínico e resistência do esporo", 22, "Nota viva da Morfologia; explica o topo da escala."),
 au("micobacterias", "After bacterial spores, the microbes most resistant to disinfectants are {{c1::mycobacteria}}", {1: V}, C_,
    "Micobactérias na escala", "22; prova 2025 P2 3.3", "prova", "sem card.", KIL, "Verde: cobrado na prova de 2025.",
    extra="- Their lipid-rich wall resists chemicals"),
 au("virus-nus", "Which is more resistant to disinfectants, poliovirus or HIV?<br><br>{{c1::Poliovirus}}", {1: Z}, C_,
    "Vírus sem envelope × envelopados", "22", "central", "sem card.", KIL, "Azul: lâmina 22.",
    extra="- Small viruses without a lipid envelope resist far more than enveloped ones"),
 au("envelopados", "Lipid-enveloped viruses such as HIV and HBV are the {{c1::least}} resistant microbes to disinfectants", {1: V}, C_,
    "Base da escala", "22", "central", "sem card.", KIL, "Verde: ponta da escala.", extra="- Fungi and vegetative bacteria sit between them and non-enveloped viruses"),
 au("alvos", "Disinfectants kill by damaging the cell membrane, denaturing proteins, blocking nucleic acid synthesis or {{c1::oxidizing}} cell components", {1: Z}, C_,
    "Alvos letais", "24; monitoria", "central", "AnKing dá o mecanismo por agente, não o conjunto.", KIL, "Azul: lâmina 24."),
 au("cida-statico", "A {{c1::bacteriostatic}} agent stops growth without killing, so bacteria grow again once it is removed", {1: V}, C_,
    "Cida × stático", "26; aula 04 I; bibliografia; Trabulsi", "central", "AnKing só classifica antibióticos.", KIL, "Verde: lâmina 26.",
    extra="- Bactericidal agents kill; refrigeration acts as a microbiostatic condition"),
 # ---------- C. Cinética de morte (lâminas 27–28) ----------
 au("morte-exponencial", "Under a lethal agent, a fixed fraction dies each minute, so survivors fall {{c1::exponentially}}", {1: V}, C_,
    "Morte exponencial", "27; Trabulsi; guia", "central", "sem card.", HEAT, "Verde: lâmina 27.", extra="- 10<sup>6</sup> → 10<sup>5</sup> → 10<sup>4</sup>…, one log per minute"),
 au("valor-d", "The {{c1::D value}} is the time needed to kill 90% (one log) of a population at a given temperature", {1: V}, C_,
    "Valor D", "27; bibliografia; aula 04 II; guia; Trabulsi", "central", "zero resultado para D value.", HEAT, "Verde: todas as fontes da aula.",
    extra="- 'Kills 99.9%' means a 3-log reduction"),
 au("mata-999", "A disinfectant that kills 99.9% lowers 10<sup>6</sup> bacteria/mL to {{c1::10<sup>3</sup>}} bacteria/mL", {1: Z}, C_,
    "Ler '99,9%' em log", "27; aula 04 II; monitoria", "central", "sem card.", HEAT, "Azul: exemplo da aula 04.",
    extra="- A thousand survivors per mL may still be unsafe"),
 au("carga", "The larger the initial microbial load, the {{c1::longer}} sterilization takes", {1: V}, C_,
    "Carga × tempo", "28; Trabulsi", "central", "sem card.", HEAT, "Verde: lâmina 28.", extra="- Cleaning first lowers the load"),
 au("esteril-prob", "A material is considered sterile when the chance of a surviving microbe falls below one in a {{c1::million}}", {1: R}, C_,
    "Probabilidade de esterilidade", "28; Trabulsi", "lateral", "sem card.", HEAT, "Rosa: detalhe do livro."),
 # ---------- D. Semmelweis, Lister, GBS (lâminas 29–35) ----------
 au("semmelweis", "Semmelweis cut deaths from puerperal fever by having doctors wash their hands in {{c1::chlorinated lime}}", {1: Z}, D_,
    "Semmelweis", "29; aula 04 II; Trabulsi", "central", "zero resultado para Semmelweis.", [1525114974682, 1500763397436], "Azul: história que funda a higiene das mãos.",
    extra="- Doctors came from autopsies carrying 'cadaveric particles'"),
 ak("gbs", 1503601523879, {1: R, 2: R}, D_, "Profilaxia intraparto do GBS", 30, "HY 1, mas clínica lateral à compreensão (F-04); lâmina 30.", clinica_lateral=True),
 au("limpeza", "Surfaces are cleaned before disinfection because organic matter {{c1::inactivates}} many disinfectants", {1: Z}, B_,
    "Limpeza antes de desinfetar", "31; aula 04 I/II; bibliografia", "central", "sem card.", KIL, "Azul: lâmina 31.",
    extra="- Enzymatic detergent, brushes and hot water, with protective equipment"),
 au("lister", "Lister introduced antiseptic surgery using {{c1::phenol}} (carbolic acid)", {1: R}, D_,
    "Lister", "34–35; aula 04 II; Trabulsi", "lateral", "sem card.", DEF, "Rosa: história.", extra="- Phenol is now of historical interest only"),
 # ---------- E. Calor (lâminas 36–42) ----------
 au("metodos-bio", "Biological control methods include antimicrobial drugs, bacteriocins and {{c1::bacteriophages}}", {1: R}, E_,
    "Métodos biológicos", "36", "lateral", "sem card.", DEF, "Rosa: lista da lâmina 36."),
 au("calor-umido-seco", "Moist heat kills microbes by {{c1::denaturing proteins}}, whereas dry heat kills by {{c1::oxidation}}", {1: V}, E_,
    "Calor úmido × seco", "37–40; Trabulsi; guia", "central", "AnKing não compara.", HEAT, "Verde: base do bloco de calor.",
    extra="- Moist heat works at lower temperatures and shorter times"),
 au("flambagem", "A platinum loop is sterilized by flaming it {{c1::red-hot}} in a Bunsen burner", {1: Z}, E_,
    "Flambagem e incineração", "38; Trabulsi", "central", "sem card.", HEAT, "Azul: lâmina 38.", extra="- Incineration destroys hospital waste the same way"),
 au("forno", "Dry-heat sterilization in an oven needs about {{c1::160–180}} °C for 1–2 hours", {1: Z}, E_,
    "Forno Pasteur", "39; aula 04", "central", "sem card.", HEAT, "Azul: lâmina 39.", extra="- Used for glassware and metal instruments"),
 ak("autoclave-vapor", 1500763633935, {1: V}, E_, "Autoclave = vapor sob pressão", 40, "Verde: método padrão."),
 au("autoclave-param", "Standard autoclave sterilization uses steam at {{c1::121}} °C for about 15–20 minutes", {1: V}, E_,
    "Parâmetros da autoclave", "40; aula 04; monitoria; prova 2025", "prova", "AnKing dá a faixa só no Extra.", HEAT, "Verde: prova 2025.",
    extra="- Larger volumes need longer cycles"),
 ak("autoclave-esporo", 1524405599297, {1: V}, E_, "Autoclave mata esporos", 40, "Verde: HY 2."),
 sh(1791163039477, "verde", E_, "Fervura não mata esporos", 37, "Nota viva da Morfologia; explica por que fervura é só desinfecção."),
 au("pasteurizacao", "Pasteurization {{c1::reduces}} microbial numbers without sterilizing, so pasteurized milk must stay refrigerated", {1: V}, E_,
    "Pasteurização não esteriliza", "42; aula 04; Trabulsi; guia", "central", "AnKing só cita leite não pasteurizado.", HEAT, "Verde: lâmina 42."),
 au("pasteur-tempos", "Slow (LTLT) pasteurization uses {{c1::63–65}} °C for 30 min, whereas HTST uses {{c2::72}} °C for 15 s", {1: R, 2: R}, E_,
    "Tempos de pasteurização", "42; aula 04", "lateral", "sem card.", HEAT, "Rosa: números.", extra="- UHT: 130–150 °C for a few seconds"),
 au("tindalizacao", "{{c1::Tyndallization}} repeats boiling with incubation in between, killing spores after they germinate", {1: R}, E_,
    "Tindalização", "37; bibliografia", "lateral", "sem card.", HEAT, "Rosa: citada na lâmina 37.", extra="- Sporicidal but not a true sterilization"),
 au("frio", "Refrigeration and freezing {{c1::stop}} microbial growth without killing, so they preserve rather than sterilize", {1: Z}, E_,
    "Frio é microbiostático", "37; aula 04; Trabulsi", "central", "sem card.", HEAT, "Azul: lâmina 37.", extra="- Freeze-drying (lyophilization) keeps microbes viable for decades"),
 # ---------- F. Filtração e radiação (lâminas 43–48) ----------
 au("filtracao", "Filtration sterilizes heat-sensitive liquids by {{c1::removing}} microbes rather than killing them", {1: V}, F_,
    "Filtração", "43; aula 04; bibliografia; Trabulsi", "central", "sem card.", HEAT, "Verde: lâmina 43."),
 au("filtro-022", "A {{c1::0.22}} µm filter retains most bacteria but lets most viruses through", {1: Z}, F_,
    "Poros e vírus", "44; bibliografia; Trabulsi", "central", "sem card.", HEAT, "Azul: tabela da lâmina 44."),
 au("hepa", "HEPA filters in laminar-flow hoods remove 99.97% of particles of {{c1::0.3}} µm", {1: R}, F_,
    "HEPA", "45", "lateral", "sem card.", HEAT, "Rosa: número.", extra="- They retain microbes but do not sterilize"),
 au("uv-dimero", "UV light kills microbes by forming {{c1::thymine dimers}} in their DNA", {1: V}, F_,
    "Mecanismo do UV", "48; Trabulsi; guia", "central", "AnKing trata dímeros só no reparo.", HEAT, "Verde: lâmina 48.",
    extra="- Germicidal lamps emit about 260 nm, the wavelength DNA absorbs best"),
 au("uv-penetracao", "UV only disinfects exposed surfaces because of its low {{c1::penetration}}", {1: V}, F_,
    "Limite do UV", "47; Trabulsi; guia", "central", "sem card.", HEAT, "Verde: por que UV raramente esteriliza.",
    extra="- It also burns skin and eyes"),
 au("gama", "Gamma radiation sterilizes disposable syringes and gloves by ionizing water into {{c1::free radicals}}", {1: Z}, F_,
    "Radiação ionizante", "47; aula 04; Trabulsi; guia", "central", "sem card.", HEAT, "Azul: radiação ionizante da aula 04.",
    extra="- Cobalt-60 is the usual source"),
 au("indicador-autoclave", "Spores of {{c1::<i>Geobacillus stearothermophilus</i>}} are the biological indicator for autoclave sterilization", {1: V}, F_,
    "Indicador biológico do calor úmido", "40; aula 04; monitoria; Trabulsi", "central", "sem card.", HEAT, "Verde: aula 04 e monitoria.",
    extra="- No growth after the cycle validates the sterilization"),
 au("indicador-seco", "Spores of <i>Bacillus atrophaeus</i> (formerly <i>B. subtilis</i>) indicate {{c1::dry-heat}} and ethylene oxide sterilization", {1: Z}, F_,
    "Indicador do calor seco", "39; aula 04; monitoria; Trabulsi", "central", "sem card.", HEAT, "Azul: par do indicador da autoclave.",
    extra="- <i>Bacillus pumilus</i> spores monitor ionizing radiation"),
 # ---------- G. Químicos (lâminas 49–57) ----------
 au("termossensivel", "Heat-sensitive reusable instruments are sterilized with {{c1::ethylene oxide}} or hydrogen peroxide plasma", {1: V}, G_,
    "Esterilizar o que não tolera calor", "49; aula 04; prova 2025 P2 3.3", "prova", "AnKing só dá o mecanismo do óxido de etileno.", KIL, "Verde: prova 2025.",
    extra="- Plasma works at 35–45 °C in minutes", duplicacao_ok="ganho: escolha do método para material termossensível (prova 2025); o AnKing dá o mecanismo"),
 ak("oxido-etileno", 1582864638285, {1: Z}, G_, "Óxido de etileno alquilante", 49, "Azul: mecanismo."),
 au("glutaraldeido", "{{c1::Glutaraldehyde}} 2% is a liquid chemical sterilant for clean instruments such as endoscopes, needing up to 10 hours", {1: Z}, G_,
    "Esterilização química a frio", "49; aula 04 I; bibliografia; monitoria", "central", "sem card.", KIL, "Azul: aula 04 e prova 2025.",
    extra="- Aldehydes alkylate proteins; toxic and possibly carcinogenic"),
 ak("esporicidas", 1522250006796, {1: Z}, G_, "PEACh esporicidas", 49, "Azul: mnemônico de apoio."),
 ak("nao-esporicidas", 1500764215465, {1: V}, G_, "Álcool, clorexidina e quaternários não matam esporos", 50, "Verde: liga escala de resistência e escolha do agente."),
 au("esporocida-esterilizante", "Every sterilant is sporicidal, but not every {{c1::sporicidal}} agent is a sterilant", {1: Z}, G_,
    "Esporocida × esterilizante", "49; bibliografia; aula 04 II (questão 7)", "central", "sem card.", KIL, "Azul: questão de revisão da aula 04.",
    duplicacao_ok="ganho: relação lógica entre os termos; PEACh lista os agentes"),
 ak("alcool-desnatura", 1522249843346, {1: V}, G_, "Álcool desnatura proteínas", 50, "Verde: lâmina 50."),
 au("alcool-70", "70% alcohol works better than absolute alcohol because {{c1::water}} is needed to denature proteins", {1: V}, G_,
    "Por que 70%", "50; Trabulsi; guia", "central", "sem card.", KIL, "Verde: pergunta da lâmina 50.",
    extra="- Water also slows evaporation, prolonging contact"),
 ak("membranas", 1522249732171, {1: Z}, G_, "Álcool e clorexidina rompem membranas", 50, "Azul: mecanismo."),
 ak("cdiff", 1525114974682, {1: Z}, G_, "C. difficile: sabão e água", 50, "Azul: aplicação de 'álcool não mata esporos'."),
 au("triclosan", "Triclosan, an antiseptic and cosmetic preservative, inhibits bacterial {{c1::fatty acid}} synthesis", {1: R}, G_,
    "Triclosan", "51; Trabulsi", "lateral", "sem card.", KIL, "Rosa: lâmina 51."),
 ak("iodo", 1522249984884, {1: Z}, G_, "Iodo halogena proteínas", 52, "Azul: lâmina 52."),
 au("cloro", "Chlorine kills microbes as {{c1::hypochlorous acid}}, formed when it dissolves in water", {1: Z}, G_,
    "Cloro e HOCl", "53; Trabulsi; guia", "central", "sem card.", KIL, "Azul: lâmina 53.", extra="- Bleach (1% hypochlorite) disinfects surfaces and food"),
 ak("peroxido", 1522249953943, {1: Z}, G_, "H2O2 gera radicais", 54, "Azul: lâmina 54."),
 ak("clorexidina", 1522249931488, {1: Z}, G_, "Clorexidina coagula citoplasma", 55, "Azul: lâmina 55."),
 au("quaternarios", "Quaternary ammonium compounds such as benzalkonium are cationic {{c1::detergents}} that disrupt membranes", {1: Z}, G_,
    "Quaternários de amônio", "56; Trabulsi", "central", "sem card.", KIL, "Azul: lâmina 56.", extra="- Soap, which is anionic, inactivates them"),
 au("resistencia-biocida", "Bacteria resist disinfectants through efflux pumps, enzymatic inactivation and reduced {{c1::permeability}}", {1: R}, G_,
    "Resistência a biocidas", "51; aula 04 I; monitoria", "lateral", "sem card.", KIL, "Rosa: tabela da aula 04."),
 au("antibiotico", "Unlike disinfectants, antibiotics can be given to patients because of their selective {{c1::toxicity}}", {1: V}, G_,
    "Desinfetante × antibiótico", "57; aula 04 II (questão 1); roteiro da aula 08", "central", "sem card.", KIL, "Verde: ponte para Antibióticos."),
]

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
 'esterilizacao': '- Includes endospores; there are no degrees of sterility',
 'desinfeccao': '- Disinfectants are applied to objects and surfaces',
 'autoclave-vapor': '- About 121 °C at 15 psi gauge pressure',
 'oxido-etileno': '- Used for heat-sensitive materials; residues must be aired out',
 'esporicidas': '- Alcohols, chlorhexidine and quaternary ammonium compounds are not sporicidal',
 'alcool-desnatura': '- It also dissolves membrane lipids',
 'membranas': '- Neither kills spores',
 'iodo': '- Tincture of iodine is a surgical antiseptic',
 'peroxido': '- 3% hydrogen peroxide foams in wounds as tissue catalase releases oxygen',
 'clorexidina': '- 0.12–0.20% solutions are used on mucosa',
 'probioticos': '- Lactobacilli ferment sugar into lactic acid in yogurt and cheese',
 'esteril-prob': '- Reached after about 12 D values from 10<sup>6</sup> spores',
 'metodos-bio': '- Physical: heat, filtration, radiation; chemical: disinfectants and antiseptics',
 'triclosan': '- Its target is enoyl-ACP reductase (FabI)',
 'resistencia-biocida': '- Never mix or dilute disinfectants arbitrarily',
 'antibiotico': '- Disinfectants and antiseptics are too toxic to give systemically',
 'virus-nus': '',
 'esporocida-esterilizante': '- A sterilant must kill even the most resistant spores',
 'alvos': '- Most agents hit several targets at once',
 'filtracao': '- Removes bacteria and fungi; most viruses pass',
 'filtro-022': '- 0.45 µm filters retain the largest bacteria',
 'pasteurizacao': '- It kills pathogens transmitted by milk',
 'lister': '',
 'semmelweis': '',
 'flambagem': '',
}
VERSO = {k: v for k, v in VERSO.items() if v}
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
