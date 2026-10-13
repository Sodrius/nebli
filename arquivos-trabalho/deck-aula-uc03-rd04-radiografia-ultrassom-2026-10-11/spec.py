# Especificação curada — Radiografia e ultrassom (UC03 P1, Radiologia; Preceptoria Radiologia 2024/2023/2020; 45 lâminas remontadas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas de fontes/slides.pdf (I = base de 2024; III acrescenta tubo, artefatos e mamografia).
# AnKing → externos (Cloze-Lightyear 'Ultrasound physics') → autoral curto só para item do material de base sem card nos acervos.
RUN_ID = "uc03-rd04-20261012a"
SHORT = "rd04"
LESSON = "2026-uc03-radiologia-04-radiografia-ultrassom"
DECK = "NEBLI::UC03::P1::Radiologia::Radiografia e ultrassom"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20261012-CLAUDE-01) + plano vigente, 12/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing Step e Referências Externas em texto livre (busca/anking.txt, 40 consultas sobre física do RX e do US, FAST, Doppler, silhueta, "
         "magnificação; busca/ext.txt, 8 consultas), tags de seção sem resultado útil, 12/10: ")
EXCLUIDOS = [
 (1701781530436, "aparência de nervo e músculo no US: ultrassom musculoesquelético, fora do recorte"),
 (1701805714594, "anisotropia no US: detalhe de ultrassom musculoesquelético, não dado na aula"),
 (1701744971045, "faixa 3 a 12 MHz e profundidade <5 cm: números de sonda sem ganho além do card de frequência × resolução"),
 (1701780430346, "frequência e profundidade máxima de sondas Sonosite: detalhe de equipamento específico"),
 (1701783439046, "profundidades de plexo braquial e nervos: bloqueio anestésico, fora do recorte"),
 (1701793231648, "zona focal do feixe: física avançada não ensinada na aula"),
 (1701809310916, "resolução axial e lateral: definição só no texto de apoio, não ensinada na aula"),
 (1701745110911, "reflexão e resolução temporal: física avançada, fora da aula"),
 (1701745337516, "visualização de agulhas pelo ângulo de insonação: ultrassom intervencionista"),
 (1712696475481, "ângulo ideal do Doppler (<20°): detalhe não dado na aula"),
 (1554151136934, "equação do efeito Doppler (MCAT): física quantitativa fora da aula"),
 (1555869206450, "efeito Doppler genérico (MCAT, fonte e detector): coberto por card próprio para o sangue e o transdutor"),
 (1578744787353, "pseudocisto pancreático anecoico: patologia de outra aula"),
 (1536707052087, "algoritmo de trauma abdominal fechado: manejo, fora da aula de princípios"),
 (1493074820825, "conduta com FAST positivo: manejo do trauma, não é objetivo desta aula"),
]
FORA_DO_RECORTE = [
 "Efeitos fotoelétrico, Compton e Rayleigh e camada semirredutora (e-book, cap. 1): o slide não os ensina; pergunta ao Davi.",
 "Grade antiespalhamento, doses (kerma, DEP, PAD) e qualidade de imagem do e-book: fora do recorte.",
 "Velocidade do som (1540 m/s) e resolução axial e lateral do texto de apoio de US: não aparecem na lâmina nem na fala.",
 "Bário e iodo como contrastes (fala da professora): tema da aula de contrastes (aula 56); fica no Extra de card compartilhado.",
 "Casos de exemplo das lâminas (cálculo biliar, hemangioma, pneumonia no tórax, caixa com pedras): ilustração do conceito, não vira card próprio.",
 "Radioterapia e dose-resposta: aula 84; aqui só o mecanismo do efeito biológico.",
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


def io(key, page, name, cor, bloco, alvo, motivo, lines=(), search=(), rects=(), mask_rects=(), remarks=""):
    return dict(key=key, kind="slideio", page=page, half="full", title_size=99, lines=list(lines), search=list(search), rects=list(rects),
                mask_rects=list(mask_rects), name=name, remarks=remarks, aponta="estrutura", flags={1: cor}, bloco=bloco, alvo=alvo,
                evid=f"Slide {page}", motivo=motivo,
                busca=BUSCA + "nenhuma figura equivalente com rótulo nos acervos para este achado (imagem da própria aula).")


A_, B_, C_, D_, E_, F_, G_, H_, I_ = ("A-por-que-rx", "B-producao-do-rx", "C-formacao-da-imagem-rx", "D-projecao-e-incidencias", "E-magnificacao-e-silhueta",
                                      "F-us-vantagens-e-doppler", "G-fisica-do-us", "H-ecogenicidade-e-artefatos", "I-fast")
EP_US = [1701743548002, 1701779007226, 1701782440595]
EP_RX = [1511123760396, 1544202588173, 1475287477002]
EP_RAD = [1488680231742, 1511123760396, 1544202588173]
EP_FAST = [1532785810173, 1536157834210, 1530471987357]
EP_DOP = [1610405450819, 1555869206450, 1610488754352]
EP_TERM = [1475287477002, 1550944864586, 1578744787353]
EP_IMG = [1511234010517, 1530303581189, 1495151598103]
# nids vivos da aula 02 (plan.json da corrida rd02 conferido em 12/10 após a revisão Codex)
RD02 = dict(rx_leito=1791810584247, rx_inicial=1791810584997, rx_escuro=1791810584496, radiopaco=1791810584619, radiolucente=1791810584747,
            exogeno=1791810575245, cumulativa=1791810574247, gravidez=1791810574372, nao_seccional=1791810569222, inc_pa_lat=1791810586046,
            pa_costas=1791810586171, plano_sag=1791810569472, plano_cor=1791810569598, plano_ax=1791810569777, us_leito=1791810569898,
            us_sem_rad=1791810571022, us_doppler=1791810572322, us_operador=1791810571147, us_limites=1791810570272, us_hiper=1791810571947,
            us_hipo=1791810572071, cisto=1791810570147, us_biliar=1791810565995)

CARDS = [
 # ---------- A. Por que usar radiografia (lâmina 2) ----------
 sh(RD02["rx_leito"], "verde", A_, "Radiografia é rápida e pode ir ao leito", 2, "Verde: primeira vantagem da radiografia dada na aula (card da aula 02)."),
 sh(RD02["rx_inicial"], "azul", A_, "Radiografia como exame inicial por custo e disponibilidade", 2, "Azul: vantagem pedida em P1 2016 e 2017."),
 au("rx-triagem", "A normal <b>radiograph</b> makes serious disease less likely, so it works as a {{c1::triage}} test", {1: R}, A_,
    "Radiografia normal ajuda a excluir doença grave (triagem)", 2, "lateral", "nenhum card dos acervos sobre radiografia como triagem.", EP_RX,
    "Rosa: comentário da professora, útil à prova.", extra="- Not always definitive, but fast, cheap and available in nearly every hospital"),
 # ---------- B. Produção do raio X (lâminas 3-11) ----------
 au("roentgen", "<b>X-rays</b> were discovered by {{c1::Röntgen}} in 1895", {1: R}, B_, "Descoberta por Röntgen em 1895", 3, "lateral",
    "nenhum card dos acervos sobre a descoberta do raio X.", EP_RX, "Rosa: dado histórico do slide.", extra="- Named X because the radiation was unknown<br>- First Nobel Prize in Physics, 1901"),
 au("radiacao-def", "<b>Radiation</b> is energy in transit, as particles or {{c1::electromagnetic waves}}", {1: Z}, B_, "Radiação é energia em trânsito", 4, "central",
    "nenhum card dos acervos define radiação para a aula.", EP_RAD, "Azul: conceito guarda-chuva do slide.",
    extra="- Sources include nuclear reactors, X-ray tubes, radionuclides and cosmic radiation"),
 au("xray-em", "<b>X-rays</b> are {{c1::electromagnetic}} waves of high energy and very short wavelength", {1: V}, B_, "Raio X é onda eletromagnética de alta energia", 5,
    "central", "nenhum card dos acervos sobre a natureza do raio X.", EP_RAD, "Verde: natureza do raio X, base da aula.", extra="- X-rays lie above ultraviolet light in frequency"),
 au("xray-lambda", "<b>X-ray</b> wavelength is on the order of {{c1::10<sup>-12</sup> m}}", {1: R}, B_, "Comprimento de onda do raio X", 5, "lateral",
    "nenhum card dos acervos.", EP_RAD, "Rosa: número específico do slide.", extra="- Frequency is on the order of 10<sup>16</sup> Hz"),
 au("tubo-filamento", "In the <b>X-ray tube</b>, a heated {{c1::tungsten}} filament in the cathode releases electrons", {1: Z}, B_,
    "Filamento de tungstênio aquecido libera elétrons", 6, "prova", "nenhum card dos acervos sobre o tubo de raio X.", EP_RAD,
    "Azul: P2 2024 1.1 e P1 2017 3.1 pedem o filamento de tungstênio.", extra="- Electrons leave the filament only when it is heated"),
 au("tubo-aceleracao", "A <b>potential difference</b> accelerates the electrons from the cathode toward the {{c1::anode}}", {1: Z}, B_,
    "Diferença de potencial acelera elétrons ao ânodo", 6, "prova", "nenhum card dos acervos.", EP_RAD, "Azul: etapa do tubo descrita na aula."),
 au("tubo-colisao", "Electrons striking the <b>tungsten target</b> of the anode produce {{c1::X-rays}} and heat", {1: Z}, B_,
    "Choque no alvo de tungstênio produz raios X", 6, "prova", "nenhum card dos acervos.", EP_RAD, "Azul: produção do raio X, pedida na prova."),
 au("tungstenio", "<b>Tungsten</b> suits the anode because of its high atomic number and high {{c1::melting point}}", {1: Z}, B_,
    "Tungstênio: Z e ponto de fusão altos", 7, "prova", "nenhum card dos acervos.", EP_RAD, "Azul: justificativa do material dada em slide e monitoria.",
    extra="- It does not melt with the heat of the tube, above 3,000 °C"),
 au("tubo-chumbo", "The <b>X-ray tube</b> is housed in {{c1::lead}}, with a single opening for the beam", {1: Z}, B_, "Tubo revestido de chumbo com abertura única", 8, "central",
    "nenhum card dos acervos.", EP_RAD, "Azul: slide e monitoria.", extra="- Lead absorbs the X-rays emitted in other directions"),
 au("tubo-oleo-vacuo", "A layer of <b>oil</b> around the X-ray tube {{c1::cools}} it", {1: R}, B_, "Óleo resfria o tubo; vácuo interno", 8, "lateral",
    "nenhum card dos acervos.", EP_RAD, "Rosa: detalhe construtivo do slide.", extra="- Inside the glass tube there is a vacuum"),
 au("tubo-calor", "Only 1 to 2 percent of the energy of the <b>electron beam</b> becomes X-rays, and the rest is {{c1::heat}}", {1: R}, B_,
    "Maior parte da energia vira calor", 9, "lateral", "nenhum card dos acervos.", EP_RAD, "Rosa: o slide marca o calor; percentual vem do livro.",
    extra="- This is why the anode needs a high melting point and cooling"),
 au("bremsstrahlung", "<b>X-rays</b> produced when electrons decelerate near an atomic nucleus are called {{c1::bremsstrahlung}} radiation", {1: R}, B_,
    "Radiação de frenagem", 9, "lateral", "nenhum card dos acervos.", EP_RAD, "Rosa: um dos processos listados no slide e na monitoria.",
    extra="- The energy lost by the electron is released as X-ray photons"),
 au("caracteristica", "<b>Characteristic</b> X-rays arise when electrons fill {{c1::inner-shell}} vacancies in the atoms of the target", {1: R}, B_,
    "Radiação característica", 9, "lateral", "nenhum card dos acervos.", EP_RAD, "Rosa: outro processo do slide, com explicação do e-book.",
    extra="- Their energy equals the difference between atomic energy levels"),
 au("rx-so-ligado", "An <b>X-ray tube</b> emits radiation only while it is {{c1::switched on}}", {1: R}, B_, "Aparelho só emite quando ligado", 10, "lateral",
    "nenhum card dos acervos.", EP_RAD, "Rosa: contraste com radionuclídeos, na fala da professora.", extra="- Radionuclides emit until they become stable"),
 au("detector", "In <b>radiography</b> the patient lies between the X-ray source and the {{c1::detector}}", {1: Z}, B_, "Paciente entre a fonte e o detector", 11, "central",
    "nenhum card dos acervos.", EP_RAD, "Azul: arranjo do exame, pedido para entender a projeção.", extra="- The transmitted X-rays form the image on the detector"),
 au("film-digital", "<b>Radiographic detectors</b> were once film and now produce {{c1::digital}} images", {1: R}, B_, "Detectores: filme e depois digital", 11, "lateral",
    "nenhum card dos acervos.", EP_RAD, "Rosa: detalhe histórico do equipamento.", extra="- The digital image goes straight to a computer"),
 # ---------- C. Formação da imagem radiográfica (lâminas 13-17) ----------
 au("atenuacao-imagem", "The <b>radiographic image</b> reflects how much each structure {{c1::attenuates}} the X-ray beam", {1: V}, C_,
    "Imagem depende da atenuação do feixe", 13, "central", "nenhum card dos acervos explica a formação da imagem radiográfica.", EP_RX,
    "Verde: mecanismo central da aula, pedido em P1 2017, P1 2018 e P2 2024.", extra="- Attenuation depends on thickness and on absorption capacity"),
 sh(RD02["rx_escuro"], "verde", C_, "Quanto mais denso, mais raio X absorve e mais branco", 13, "Verde: relação central entre densidade e brilho (card da aula 02)."),
 au("espessura", "A <b>thicker</b> object absorbs {{c1::more}} X-rays than a thinner one of the same material", {1: Z}, C_, "Espessura e absorção", 13, "central",
    "nenhum card dos acervos.", EP_RX, "Azul: fator citado no slide e na monitoria.", extra="- Composition matters as much as thickness"),
 au("densidades", "Radiographic densities from darkest to whitest are <b>air</b>, {{c1::fat}}, {{c2::water}}, {{c3::calcium}} and {{c4::metal}}", {1: V, 2: V, 3: V, 4: V},
    C_, "Cinco densidades radiológicas em ordem", 14, "central", "AnKing não traz a sequência das cinco densidades.", EP_RX,
    "Verde: sequência do slide, cobrada na prova.", extra="- Soft tissue behaves like water<br>- Metal blocks the beam almost completely"),
 sh(RD02["radiopaco"], "azul", C_, "Radiopaco: bloqueia o raio X e fica branco", 14, "Azul: termo da radiografia pedido nas provas (card da aula 02)."),
 sh(RD02["radiolucente"], "azul", C_, "Radiotransparente: pulmão cheio de ar", 14, "Azul: termo da radiografia pedido nas provas (card da aula 02)."),
 au("hiperatenuante", "On <b>radiographs</b>, a whiter area that absorbs more X-rays is also called {{c1::hyperattenuating}}", {1: Z}, C_,
    "Hiperatenuante é o termo técnico para áreas brancas", 14, "prova", "AnKing cobre hiperdenso na TC, não o termo na radiografia.", EP_TERM,
    "Azul: P1 2015 pede 'como se denominam as áreas mais brancas' na radiografia.", extra="- A darker area is hypoattenuating"),
 sh(RD02["exogeno"], "azul", C_, "Contraste exógeno quando as densidades são parecidas", 16, "Azul: resposta da lâmina 'e quando as densidades são iguais' (card da aula 02)."),
 au("ionizante-def", "<b>Ionizing radiation</b> has enough energy to remove {{c1::electrons}} from the atoms it crosses", {1: Z}, C_,
    "Radiação ionizante remove elétrons", 17, "central", "nenhum card dos acervos.", EP_RAD, "Azul: pré-requisito do efeito biológico.",
    extra="- X-rays are ionizing radiation"),
 au("efeito-direto", "The <b>direct effect</b> of radiation is damage to molecules such as {{c1::DNA}}", {1: V}, C_, "Efeito biológico direto: dano ao DNA", 17, "central",
    "AnKing só cobre radiação ultravioleta no DNA da pele.", EP_RAD, "Verde: mecanismo do efeito biológico, base da proteção e da radioterapia.",
    extra="- Damaged DNA can mutate, be repaired or lead to cell death"),
 au("efeito-indireto", "The <b>indirect effect</b> of radiation comes from {{c1::free radicals}} formed by the splitting of water molecules", {1: V}, C_,
    "Efeito indireto: radicais livres da água", 17, "central", "nenhum card dos acervos.", EP_RAD, "Verde: segundo mecanismo do efeito biológico.",
    extra="- Free radicals then injure molecules much like the direct effect"),
 au("radioterapia", "The cell-killing effect of <b>ionizing radiation</b> is used in {{c1::radiotherapy}} to control tumors", {1: Z}, C_,
    "Uso terapêutico: radioterapia", 17, "central", "nenhum card dos acervos.", EP_RAD, "Azul: o slide cita o uso na radioterapia, que terá aula própria."),
 au("estocastico", "<b>Radiation effects</b> that are not strictly dose-dependent and accumulate silently are called {{c1::stochastic}}", {1: R}, C_,
    "Efeitos estocásticos", 17, "lateral", "nenhum card dos acervos.", EP_RAD, "Rosa: nuance dita pela professora ('nem sempre dose dependente')."),
 sh(RD02["cumulativa"], "azul", C_, "Radiação é cumulativa", 17, "Azul: cuidado citado no slide III e na fala (card da aula 02)."),
 sh(RD02["gravidez"], "azul", C_, "Evitar radiação ionizante na gestação", 17, "Azul: efeito teratogênico citado no slide III e na monitoria (card da aula 02)."),
 au("protecao", "<b>Radiological protection</b> means limiting unnecessary exams and the exposure of patients and {{c1::professionals}}", {1: Z}, C_,
    "Proteção radiológica", 17, "central", "nenhum card dos acervos.", EP_RAD, "Azul: item final do slide de efeito biológico.",
    extra="- The X-ray beam diverges, so staff nearby also need shielding"),
 # ---------- D. Projeção e incidências (lâminas 18-23) ----------
 au("perda-dimensao", "Because a radiograph is a <b>projection</b>, {{c1::one}} of the three body dimensions is lost", {1: V}, D_,
    "Projeção perde uma dimensão", 19, "central", "AnKing cobre sobreposição, não a perda de uma dimensão.", EP_RX,
    "Verde: conceito do exercício prático, base para pedir duas incidências.", extra="- The lost dimension is the one along the beam"),
 sh(RD02["nao_seccional"], "verde", D_, "Radiografia não é seccional: estruturas se sobrepõem", 19, "Verde: consequência da projeção (card da aula 02)."),
 au("perfil-profundidade", "An opacity seen only on a <b>PA</b> film cannot be placed in depth, so a {{c1::lateral}} view is added", {1: V}, D_,
    "Perfil localiza a lesão em profundidade", 20, "central", "nenhum card dos acervos.", EP_RX, "Verde: razão de pedir duas incidências.",
    extra="- The lateral view adds the anteroposterior dimension"),
 sh(RD02["plano_sag"], "azul", D_, "Plano sagital", 21, "Azul: planos da figura de eixos e planos do corpo (card da aula 02)."),
 sh(RD02["plano_cor"], "azul", D_, "Plano coronal", 21, "Azul: planos da figura de eixos e planos do corpo (card da aula 02)."),
 sh(RD02["plano_ax"], "azul", D_, "Plano transversal", 21, "Azul: planos da figura de eixos e planos do corpo (card da aula 02)."),
 io("io-pa", 22, "Posteroanterior (PA) chest radiograph", Z, D_, "Reconhecer a radiografia de tórax em PA", "Azul: incidência padrão do tórax, pedida na prova P1 2017.",
    lines=["PA"]),
 sh(RD02["inc_pa_lat"], "azul", D_, "Tórax em PA e perfil", 22, "Azul: duas incidências de rotina (card da aula 02)."),
 sh(RD02["pa_costas"], "azul", D_, "PA: feixe entra pelas costas", 22, "Azul: definição da incidência PA (card da aula 02)."),
 au("eixos-corpo", "The three <b>body axes</b> are longitudinal, anteroposterior and {{c1::laterolateral}}", {1: R}, D_, "Eixos do corpo", 21, "lateral",
    "nenhum card dos acervos.", EP_RX, "Rosa: rótulos da figura de planos e eixos.", extra="- Each plane is perpendicular to one of these axes"),
 au("pa-paciente", "In a <b>PA</b> chest view the patient faces the {{c1::detector}} while the beam enters from behind", {1: Z}, D_, "PA: paciente de frente para o detector", 22, "central",
    "nenhum card dos acervos.", EP_RX, "Azul: arranjo da incidência mostrado em foto e esquema.", extra="- Standing PA is the standard chest exam, and it keeps the heart close to the detector"),
 au("perfil-feixe", "In a <b>lateral</b> chest view the X-ray beam crosses the patient from {{c1::side to side}}", {1: Z}, D_, "Perfil: feixe de lado a lado", 23, "central",
    "nenhum card dos acervos.", EP_RX, "Azul: arranjo da incidência em perfil.", extra="- The patient raises the arms and stands sideways to the detector"),
 io("io-perfil", 23, "Lateral (profile) chest radiograph", Z, D_, "Reconhecer a radiografia de tórax em perfil", "Azul: segunda incidência de rotina.", lines=["Perfil"]),
 # ---------- E. Magnificação e sinal da silhueta (lâminas 24-30) ----------
 au("magnificacao", "On a radiograph, an object farther from the <b>detector</b> appears {{c1::larger}}", {1: V}, E_, "Objeto afastado do detector é ampliado", 24, "central",
    "nenhum card dos acervos sobre magnificação.", EP_RX, "Verde: conceito do exercício, cobrado em P1 2015.", extra="- Like the shadow of an object near a point light source"),
 au("divergencia", "<b>Magnification</b> happens because X-rays diverge from a {{c1::point}} source", {1: Z}, E_, "Magnificação vem da divergência do feixe", 25, "central",
    "nenhum card dos acervos.", EP_RX, "Azul: explica a magnificação (analogia da sombra).", extra="- The closer the object is to the detector, the smaller its image"),
 au("pa-magnificacao", "A <b>chest radiograph</b> is taken in PA, with the heart near the detector, to limit {{c1::magnification}}", {1: V}, E_,
    "Por que o tórax é feito em PA", 26, "prova", "nenhum card dos acervos.", EP_RX, "Verde: P1 2015 1.1 pergunta direto por que fazer em PA.",
    extra="- In PA the anterior chest wall, and so the heart, lies closest to the detector"),
 au("ap-coracao", "On a bedside <b>AP</b> chest film, the heart appears falsely {{c1::enlarged}}", {1: V}, E_, "AP no leito aumenta falsamente o coração", 26, "prova",
    "nenhum card dos acervos.", EP_RX, "Verde: consequência clínica da magnificação, ressaltada na fala.", extra="- Patients who cannot stand are examined in AP, so this must be considered"),
 au("aorta", "The <b>aorta</b> is seen on chest radiographs because {{c1::air}} in the lungs surrounds it", {1: R}, E_, "Aorta visível no tórax por causa do ar", 28, "lateral",
    "nenhum card dos acervos.", EP_RX, "Rosa: exemplo da fala para o sinal da silhueta.", extra="- In the abdomen fat and muscle of similar density surround it, so it is not seen"),
 au("silhueta-def", "Adjacent structures of similar radiographic density lose their {{c1::contours}}, known as the <b>silhouette sign</b>", {1: V}, E_,
    "Sinal da silhueta", 29, "central", "AnKing não traz o sinal da silhueta.", EP_RX, "Verde: conceito do exercício e da monitoria.",
    extra="- Seen on chest films when a lesion touches the heart border or the diaphragm"),
 au("silhueta-separadas", "<b>Structures</b> of similar density keep visible borders when {{c1::air}} or another density separates them", {1: Z}, E_,
    "Densidades parecidas separadas mantêm contorno", 29, "central", "nenhum card dos acervos.", EP_RX, "Azul: face inversa do sinal da silhueta.",
    extra="- The same stone stays visible when surrounded by air and fades when surrounded by cement"),
 au("silhueta-pneumonia", "A <b>pneumonia</b> touching the cardiac border blurs the {{c1::heart}} contour", {1: V}, E_,
    "Pneumonia em contato apaga a silhueta cardíaca", 29, "prova", "AnKing não traz a aplicação do sinal da silhueta.", EP_RX,
    "Verde: aplicação central do sinal, descrita na monitoria.",
    extra="- Fluid replaces air in the alveoli, so the lung becomes as dense as the heart<br>- A posterior pneumonia that does not touch the heart leaves its border visible"),
 au("mamografia", "<b>Mammography</b> uses breast {{c1::compression}} to image the whole structure evenly", {1: R}, E_, "Mamografia comprime a mama", 27, "lateral",
    "nenhum card dos acervos.", EP_RX, "Rosa: exemplo de espessura da monitoria (lâmina III p.21).", extra="- Image quality depends on the amount and thickness of material crossed"),
 au("orientacao-rx", "On <b>radiographs</b>, the right side of the image is the patient's {{c1::right}} side", {1: Z}, E_, "Convenção de lateralidade", 30, "central",
    "nenhum card dos acervos.", EP_RX, "Azul: convenção da lâmina de orientação.", extra="- The same convention applies to CT and other imaging exams"),
 # ---------- F. Ultrassonografia: vantagens e Doppler (lâminas 31-33) ----------
 sh(RD02["us_leito"], "verde", F_, "Ultrassom é rápido, dinâmico e vai ao leito", 32, "Verde: vantagem central do ultrassom (card da aula 02)."),
 sh(RD02["us_sem_rad"], "verde", F_, "Ultrassom sem radiação ionizante", 32, "Verde: vantagem pedida em P1 2016 e P2 2025 (card da aula 02)."),
 au("minimamente-invasivo", "<b>Ultrasound</b> is minimally invasive when it guides procedures such as {{c1::punctures}}", {1: Z}, F_, "Minimamente invasivo ao guiar punções", 32, "central",
    "nenhum card dos acervos.", EP_IMG, "Azul: vantagem do slide.", extra="- Otherwise it is non-invasive"),
 au("barato-portatil", "<b>Ultrasound</b> is the cheapest and most {{c1::portable}} imaging device", {1: Z}, F_, "Mais barato e mais portátil", 32, "prova",
    "nenhum card dos acervos.", EP_IMG, "Azul: vantagem pedida nas provas.", extra="- It can be taken to patients who cannot move"),
 ak("doppler-def", 1610405450819, {1: Z}, F_, "Efeito Doppler: mudança de frequência", 32,
    "Azul: base do Doppler pedido em P1 2024 2.7.", origin="Referências Externas",
    extra="- In ultrasound the moving source is the blood and the observer is the transducer<br>- A siren that rises in pitch as it approaches is the classic example"),
 au("doppler-direcao", "In <b>Doppler</b> ultrasound, flow toward the transducer {{c1::raises}} the echo frequency and flow away {{c2::lowers}} it", {1: V, 2: V}, F_,
    "Fluxo em direção ao transdutor aumenta a frequência do eco", 32, "prova", "AnKing só traz o Doppler como exame de escolha, sem o princípio.", EP_DOP,
    "Verde: P1 2024 2.7 pede o princípio do Doppler.", extra="- The shift gives the velocity and direction of flow"),
 sh(RD02["us_doppler"], "azul", F_, "Doppler avalia o fluxo sanguíneo", 32, "Azul: vantagem do slide (card da aula 02)."),
 ak("doppler-cor", 1610488754352, {1: R}, F_, "Doppler colorido: vermelho e azul, matiz e velocidade", 32,
    "Rosa: convenção de cores do Doppler, útil na leitura de imagens.", origin="Referências Externas",
    extra="- <b>BART</b> means blue away, red toward<br><img src=\"aw.png\"><br>- Colors are assigned by the machine and can vary between devices"),
 au("doppler-estenose", "<b>Doppler</b> measures flow velocity, which helps diagnose vascular {{c1::stenosis}}", {1: Z}, F_, "Doppler mede velocidade e ajuda na estenose", 32, "central",
    "nenhum card dos acervos.", EP_DOP, "Azul: nota da apostila de veteranos.", extra="- It studies the hemodynamics without invasion"),
 au("doppler-enxerto", "<b>Ultrasound with Doppler</b> assesses organ perfusion without {{c1::contrast}}, which suits patients with renal impairment", {1: Z}, F_,
    "Doppler avalia perfusão sem contraste", 32, "prova", "nenhum card dos acervos.", EP_DOP, "Azul: P3 2025 4.5 pede esse raciocínio para o enxerto renal.",
    extra="- Example: perfusion of a transplanted kidney"),
 au("figado-us", "The first imaging test for the <b>liver</b> parenchyma is {{c1::ultrasound}}", {1: Z}, F_, "US como exame inicial do fígado", 32, "prova",
    "AnKing cobre o US para vesícula, não para o parênquima hepático.", EP_IMG, "Azul: P1 2015 4.1 e P2 2015 2.8.",
    extra="- Low cost, no radiation and it shows the echotexture of the parenchyma"),
 sh(RD02["us_biliar"], "azul", F_, "Doença biliar: ultrassom é o primeiro exame", 32, "Azul: aplicação da vantagem do US (card da aula 02)."),
 au("ecocardiograma", "<b>Echocardiography</b> is ultrasound of the {{c1::heart}}, usually with Doppler", {1: Z}, F_, "Ecocardiograma é ultrassom do coração", 32, "prova",
    "nenhum card dos acervos.", EP_DOP, "Azul: P4 2025 1.7 e P1 2015 sub 2.5.", extra="- It shows the chambers, valves and ventricular function"),
 sh(RD02["us_operador"], "azul", F_, "Qualidade depende do operador", 33, "Azul: desvantagem do slide (card da aula 02)."),
 sh(RD02["us_limites"], "azul", F_, "Limitado por gás, gordura e osso", 33, "Azul: desvantagens do slide (card da aula 02)."),
 # ---------- G. Física do ultrassom (lâminas 34-39) ----------
 au("onda-mecanica", "<b>Sound</b> is a {{c1::mechanical}} wave that needs a medium, unlike electromagnetic waves", {1: V}, G_, "Som é onda mecânica", 34, "central",
    "nenhum card dos acervos.", EP_US, "Verde: conceito central do ultrassom, diferença para o raio X.", extra="- X-rays need no medium"),
 au("ultrassom-hz", "<b>Ultrasound</b> is sound with frequency above {{c1::20,000}} Hz", {1: R}, G_, "Ultrassom acima de 20.000 Hz", 34, "lateral",
    "nenhum card dos acervos.", EP_US, "Rosa: número do slide e do livro.", extra="- Audible sound spans 20 to 20,000 Hz and infrasound lies below it"),
 ak("piezo", 1701782440595, {1: V}, G_, "Cristais piezoelétricos no transdutor", 35, "Verde: peça-chave do ultrassom, pedida em P1 2018 e P1 2024.",
    origin="Referências Externas"),
 au("piezo-recebe", "The same <b>piezoelectric</b> crystals that emit sound also {{c1::receive}} the returning echoes", {1: V}, G_, "Transdutor emite e recebe", 35, "prova",
    "nenhum card dos acervos.", EP_US, "Verde: P1 2024 2.6 pede o mecanismo (efeito piezoelétrico inverso).", extra="- They turn the echo into an electrical signal"),
 au("tempo-profundidade", "The <b>depth</b> of a reflecting interface is calculated from the {{c1::time}} the echo takes to return", {1: Z}, G_,
    "Tempo do eco dá a profundidade", 35, "prova", "nenhum card dos acervos.", EP_US, "Azul: P1 2024 2.6 cita tempo e intensidade; texto de apoio do US.",
    extra="- Later echoes are drawn lower on the screen"),
 au("intensidade-brilho", "The <b>brightness</b> of a point on the image reflects the {{c1::intensity}} of the returning echo", {1: Z}, G_,
    "Intensidade do eco dá o brilho", 35, "prova", "nenhum card dos acervos.", EP_US, "Azul: P1 2024 2.6.", extra="- Strong echoes are bright and weak echoes are dark"),
 au("impedancia-reflexao", "The amount of <b>reflection</b> at a tissue interface depends on the difference in acoustic {{c1::impedance}}", {1: Z}, G_,
    "Reflexão depende da diferença de impedância", 35, "central", "AnKing não traz a relação entre impedância e reflexão.", EP_US,
    "Azul: explica a ecogenicidade ensinada na lâmina de descritores.", extra="- With no difference the beam is fully transmitted"),
 ak("impedancia-def", 1712509799325, {1: R}, G_, "Impedância depende de densidade e velocidade do som", 35, "Rosa: definição de impedância acústica.",
    origin="Referências Externas"),
 ak("gel", 1701804937884, {1: Z}, G_, "Gel elimina o ar entre transdutor e pele", 35, "Azul: consequência de o som ser onda mecânica, citada na fala.",
    origin="Referências Externas"),
 ak("freq-resolucao", 1701743548002, {1: V}, G_, "Frequência alta: mais resolução e menos penetração", 37, "Verde: princípio dito na fala e no texto de apoio.",
    origin="Referências Externas"),
 ak("atenuacao", 1701775518633, {1: Z}, G_, "Atenuação e frequência", 37, "Azul: atenuação cresce com a frequência.", origin="Referências Externas"),
 ak("bamb", 1701779007226, {1: Z}, G_, "Atenuação: osso, ar, músculo, sangue", 37, "Azul: explica por que osso e gás limitam o US.", origin="Referências Externas"),
 ak("pgr", 1701779472592, {1: R}, G_, "Penetração baixa frequência, resolução alta", 37, "Rosa: mnemônico para escolher a frequência.", origin="Referências Externas"),
 au("freq-superficial", "<b>Superficial</b> structures such as the thyroid and breast are imaged with {{c1::high}}-frequency transducers", {1: Z}, G_,
    "Alta frequência para estruturas superficiais", 37, "prova", "nenhum card dos acervos.", EP_US, "Azul: aplicação da escolha do transdutor, na fala.",
    extra="- Deep abdominal and pelvic structures use lower frequencies"),
 au("cavitario", "The <b>transvaginal</b> probe uses a {{c1::higher}} frequency than the abdominal convex probe", {1: R}, G_, "Sonda cavitária tem frequência maior", 37, "lateral",
    "nenhum card dos acervos.", EP_US, "Rosa: exemplo dado na fala.", extra="- It sits close to the target, so less penetration is needed"),
 au("us-transversal", "A <b>transverse</b> ultrasound scan produces an {{c1::axial}} section of the patient", {1: Z}, G_, "Corte transversal gera imagem axial", 38, "central",
    "nenhum card dos acervos.", EP_US, "Azul: orientação do método seccional.", extra="- The right side of the screen is the patient's right"),
 au("us-topo-tela", "On an <b>ultrasound</b> screen, the top of the image shows the structures {{c1::closest}} to the transducer", {1: Z}, G_,
    "Topo da tela é o mais próximo do transdutor", 38, "central", "nenhum card dos acervos.", EP_US, "Azul: convenção de orientação.", extra="- In practice the top of the screen is anterior"),
 au("us-longitudinal", "A <b>longitudinal</b> ultrasound scan along the craniocaudal axis produces a {{c1::sagittal}} section", {1: Z}, G_, "Corte longitudinal gera imagem sagital", 39,
    "central", "nenhum card dos acervos.", EP_US, "Azul: orientação do método seccional.", extra="- The transducer lies anterior to the structure"),
 # ---------- H. Ecogenicidade e artefatos (lâminas 40-43) ----------
 sh(RD02["us_hiper"], "azul", H_, "Hiperecogênico", 40, "Azul: descritor do slide (card da aula 02)."),
 sh(RD02["us_hipo"], "azul", H_, "Hipoecogênico", 40, "Azul: descritor do slide (card da aula 02)."),
 au("isoecogenico", "A <b>structure</b> with the same <b>echogenicity</b> as its surroundings is {{c1::isoechoic}}", {1: Z}, H_, "Isoecogênico", 40, "prova",
    "AnKing não cobre isoecogênico.", EP_TERM, "Azul: quarto descritor do slide.", extra="- Different tissues can share the same echogenicity"),
 sh(RD02["cisto"], "verde", H_, "Cisto simples é anecoico", 40, "Verde: líquido é anecoico, HY 1 (card da aula 02)."),
 au("anecoico-liquido", "<b>Fluid-filled</b> structures such as the bladder, vessels and ascites are {{c1::anechoic}}", {1: V}, H_,
    "Estruturas líquidas são anecoicas", 40, "prova", "AnKing traz o cisto renal anecoico, não a regra geral para o líquido.", EP_TERM,
    "Verde: descritor central, pedido em P1 2016 e nas provas de 2024-2025.", extra="- They return no echoes and look black"),
 au("gordura-us", "<b>Fat</b> looks dark on radiography but relatively {{c1::bright}} on ultrasound", {1: R}, H_, "Gordura: escura no RX, clara no US", 40, "lateral",
    "nenhum card dos acervos.", EP_TERM, "Rosa: lembrete da fala de que os descritores não se transpõem.", extra="- X-ray descriptors cannot be transposed to ultrasound"),
 au("descritor-modalidade", "Terms such as <b>hyperechoic</b> and <b>hypoechoic</b> identify an {{c1::ultrasound}} exam", {1: Z}, H_, "Descritores identificam a modalidade", 40, "prova",
    "nenhum card dos acervos.", EP_TERM, "Azul: P1 2015 P2 3.1 e P4 2025 3.1 pedem inferir o exame pelo termo.",
    extra="- Radiography uses radiolucent and radiopaque, CT uses hypodense and hyperdense, MRI uses hypointense and hyperintense"),
 au("artefato-us", "<b>Ultrasound artifacts</b> are errors in image presentation caused by equipment, technique or {{c1::sound-tissue interaction}}", {1: Z}, H_,
    "Artefatos: três causas", 41, "central", "nenhum card dos acervos.", EP_US, "Azul: definição do slide III.", extra="- Some artifacts help the diagnosis"),
 au("sombra-mec", "A <b>posterior acoustic shadow</b> forms behind highly {{c1::attenuating}} or reflective structures", {1: V}, H_,
    "Sombra acústica posterior: mecanismo", 42, "prova", "AnKing só cita sombra em cisto dermoide.", EP_US,
    "Verde: P1 2015 sub 1.1 pede o mecanismo.", extra="- Few echoes pass through, so the area behind looks dark"),
 au("calculo-us", "On ultrasound, a calcified <b>stone</b> is {{c1::hyperechoic}} and casts a posterior acoustic {{c2::shadow}}", {1: Z, 2: Z}, H_,
    "Cálculo: hiperecogênico com sombra", 42, "prova", "nenhum card dos acervos.", EP_TERM, "Azul: P1 2015 2.1 pergunta o aspecto do cálculo renal.",
    extra="- Gallstones, renal stones, calcifications and bone behave this way"),
 au("sombra-suja", "<b>Bowel gas</b> causes a weaker, {{c1::'dirty'}} posterior acoustic shadow", {1: R}, H_, "Sombra suja do gás intestinal", 42, "lateral",
    "nenhum card dos acervos.", EP_US, "Rosa: variante descrita no texto de apoio.", extra="- The gas interface reflects the beam less completely than calcium"),
 io("io-sombra", 42, "Posterior acoustic shadow", Z, H_, "Reconhecer a sombra acústica posterior", "Azul: reconhecer o artefato na imagem, como em P1 2016 4.2.",
    rects=[(400, 305, 475, 405)], mask_rects=[(28, 128, 268, 154)]),
 au("reforco-us", "A <b>cyst</b> or other fluid-filled structure produces posterior acoustic {{c1::enhancement}}", {1: V}, H_, "Reforço acústico posterior", 43, "prova",
    "AnKing só cita o reforço no cisto ovariano.", EP_US, "Verde: P1 2016 4.2 descreve cisto mamário anecoico com reforço.",
    extra="- A brighter band appears behind the bladder, gallbladder, vessels and cysts"),
 au("reforco-mec", "<b>Posterior acoustic enhancement</b> occurs because fluid {{c1::attenuates}} the beam less than adjacent tissue", {1: Z}, H_,
    "Reforço acústico: baixa atenuação", 43, "prova", "nenhum card dos acervos.", EP_US, "Azul: comparação decisiva com a sombra.",
    extra="- The machine over-compensates the deeper echoes, which look brighter"),
 io("io-reforco", 43, "Posterior acoustic enhancement", Z, H_, "Reconhecer o reforço acústico posterior", "Azul: reconhecer o artefato na imagem.",
    rects=[(425, 235, 575, 345)], mask_rects=[(28, 128, 268, 154)]),
 # ---------- I. FAST (lâmina 44) ----------
 au("fast-def", "<b>FAST</b> is a rapid bedside ultrasound used in trauma to detect {{c1::hemorrhage}}", {1: Z}, I_, "FAST em trauma", 44, "central",
    "AnKing cobre FAST só como etapa de manejo do trauma.", EP_FAST, "Azul: aplicação final da aula.",
    extra="- Focused Assessment with Sonography for Trauma<br>- It helps decide whether emergency surgery is needed"),
 au("fast-liquido", "On <b>FAST</b>, free intraperitoneal blood appears as an {{c1::anechoic}} stripe between organs such as the liver and kidney", {1: V}, I_,
    "Sangue livre é anecoico no espaço hepatorrenal", 44, "central", "nenhum card dos acervos.", EP_FAST,
    "Verde: liga o descritor anecoico à aplicação do slide.", extra="- A normal exam shows only tissue between the liver and the kidney"),
 au("fast-pontos", "<b>FAST</b> checks the pericardium, the hepatorenal space, the splenorenal space and the {{c1::pelvis}}", {1: Z}, I_, "Quatro janelas do FAST", 44, "central",
    "nenhum card dos acervos.", EP_FAST, "Azul: sequência fixa de quatro pontos, descrita na fala.", extra="- The scan starts at the subxiphoid window"),
 ak("fast-retroperitoneo", 1536157834210, {1: R}, I_, "FAST não vê líquido retroperitoneal", 44, "Rosa: limite do FAST."),
]

SEM_IMAGEM = "conceito, termo ou comparação sem estrutura própria a identificar; a imagem do assunto está nos cards de oclusão do slide desta aula e nas imagens dos cards associados"
for c in CARDS:
    if c["kind"] in ("text", "autoral", "anatoking") and "sem_imagem" not in c:
        c["sem_imagem"] = SEM_IMAGEM

# Linha curta no verso dos cards que chegavam sem explicação (F-20261003-CLAUDE-15); AnKing preservado (extra_add), autoral em extra.
VERSO = {
    "tubo-aceleracao": "- The accelerating voltage gives the electrons their energy",
    "tubo-colisao": "- The collision happens at the tungsten target of the anode",
    "radioterapia": "- In imaging the aim is a diagnostic image without harm",
    "estocastico": "- Stochastic effects can arise even from small cumulative doses",
    "impedancia-def": "- Acoustic impedance is the resistance of a medium to the passage of sound",
    "freq-resolucao": "- High frequency means shorter wavelength and better detail but more attenuation",
    "gel": "- Air between probe and skin would reflect almost all the beam",
}  # chave: "- linha curta" para card sem Extra (gate de verso); AnKing recebe em extra_add
DUPLICACAO = {
    "freq-superficial": "ganho: escolha clínica do transdutor para estruturas superficiais, além da relação geral entre frequência e resolução",
    "cavitario": "ganho: exemplo de sonda cavitária (transvaginal) da fala, sem repetir a relação geral",
    "reforco-us": "ganho: aspecto do achado (cisto com banda clara posterior), com o mecanismo no card seguinte",
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


# ---- revisão Opus (12/10) ----
def _cc(key):
    return next(c for c in CARDS if c["key"] == key)
_cc("orientacao-rx")["text"] = "On a <b>radiograph</b>, the patient's right side appears on the viewer's {{c1::left}}, as if facing the patient"
_cc("xray-lambda")["extra"] = "- Diagnostic X-rays span roughly 10<sup>-11</sup> to 10<sup>-10</sup> m"
CARDS[:] = [c for c in CARDS if c["key"] != "xray-lambda"]  # valor da lâmina (10^-12 m) diverge da faixa diagnóstica; número sem ganho


# Análise do deck-prova 2026-10-13 (F-20261013-CLAUDE-03): cards tirados desta aula, com motivo.
RETIRADOS_ANALISE = {
 "rx-triagem": "detalhe",
 "roentgen": "historia",
 "tubo-aceleracao": "detalhe-tecnico",
 "tungstenio": "detalhe-tecnico",
 "tubo-chumbo": "detalhe-tecnico",
 "tubo-oleo-vacuo": "detalhe-tecnico",
 "tubo-calor": "detalhe-numerico",
 "bremsstrahlung": "detalhe-tecnico",
 "caracteristica": "detalhe-tecnico",
 "film-digital": "detalhe",
 "eixos-corpo": "repetido",
 "divergencia": "detalhe-tecnico",
 "mamografia": "exemplo",
 "minimamente-invasivo": "detalhe",
 "barato-portatil": "repetido",
 "doppler-cor": "detalhe",
 "doppler-estenose": "clinica",
 "doppler-enxerto": "clinica",
 "figado-us": "repetido",
 "impedancia-def": "detalhe-tecnico",
 "bamb": "detalhe",
 "pgr": "detalhe",
 "cavitario": "detalhe",
 "sombra-suja": "detalhe",
 "fast-def": "clinica",
 "fast-pontos": "clinica",
 "fast-retroperitoneo": "clinica"
}
CARDS = [c for c in CARDS if c['key'] not in RETIRADOS_ANALISE]


# Análise do deck-prova 2026-10-13 (F-20261013-CLAUDE-03): cards tirados desta aula, com motivo.
RETIRADOS_ANALISE = {
 "sh-1791810586171": "repetido"
}
CARDS = [c for c in CARDS if c['key'] not in RETIRADOS_ANALISE]
