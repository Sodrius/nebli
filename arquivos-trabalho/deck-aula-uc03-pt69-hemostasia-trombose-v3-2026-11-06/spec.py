# Especificação curada — 69 Hemostasia, trombose, embolia e infarto (UC03 P4, Patologia; Luiz Fernando Ferraz da Silva; 60 lâminas).
# Ordem = slides. AnKing (seções First Aid do assunto, decididas nota a nota) → NEBLI vivo → autoral SÓ para lacuna provada (busca/cobertura.tsv).
# O professor: "se vocês entenderem essa primeira partezinha de hemostasia normal, toda a parte seguinte fica muito simples" → peso no começo.
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar, acervo

PIPELINE_VERSAO = 16
SECOES_MOTIVO = ""
SECOES_DA_AULA = [l for l in (HERE / "busca" / "secoes-da-aula.txt").read_text(encoding="utf-8").split() if l]
AUTORAL_EXCECAO = ""
MODO = "aula"
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt69-20261106a"
SHORT = "pt69"
LESSON = "2026-uc03-patologia-69-hemostasia-trombose"
DECK = "NEBLI::UC03::P4::Patologia::69 Hemostasia, trombose, embolia e infarto"
CRITERIOS = "MEMORY.md + pipeline v16 + FEEDBACKS até F-20261106-CLAUDE-01 + GUIA-1 a GUIA-4 relidos em 06/11/2026"
_IMGS = ("vasoconstricao", "endotelio", "plaqueta", "arterial-venoso", "destino", "infarto-vermelho", "infarto-branco", "trombina", "virchow", "endotelio-pro", "destino-esquema")
MEDIA = {f"im69-{n}.png": f"img/im69-{n}.png" for n in _IMGS}
IMG = lambda n: f'<br><br><img src="im69-{n}.png" style="width:100%;max-width:850px;height:auto">'
BUSCA = ("Três caminhos (06/11): seções First Aid de hemostasia, trombogênese, cascata, fibrinólise, prevenção da trombose, vitamina K, infartos e embolia pulmonar "
         "(busca/secoes), Bootcamp e B&B lidos como apoio; palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e no NEBLI vivo, "
         "uma consulta por conceito (busca/semantica.jsonl). ")


def K(nid, cod, bloco, alvo, slide, motivo, **kw):
    return acervo(nid, cod, bloco, alvo, slide, motivo, lesson=LESSON, run_id=RUN_ID, **kw)


def F(loc, trecho):
    return [{"localizador": loc, "trecho": trecho}]


A_, B_, C_, D_, E_, F_, G_, H_ = ("A-hemostasia-normal", "B-endotelio", "C-plaquetas", "D-cascata-fibrinolise", "E-virchow",
                                  "F-trombo", "G-embolia", "H-infarto")
_EXT = "fora do princípio da aula"
EXCLUIDOS = [
 (1473986043060, "repete o Ca2+ dos grânulos densos de 1474059949481 e 1473995468409 (verificador por casos 06/11)"),
 (1473995504794, "repete o fator VII da via extrínseca de 1473995568285 (verificador por casos 06/11)"),
 (1488847779733, "repete o tempo de sangramento prolongado de 1473986177028 (verificador por casos 06/11)"),
 (1473986093686, "repete a estase de 1474340539643 e um lado do par entrega o outro (verificador por casos 06/11)"),
 (1474340712036, "repete 1474340718532 (estrogênio aumenta a produção de fatores), sem o mecanismo (verificador por casos 06/11)"),
 (1474426229341, "a resposta (silencioso) já aparece escrita em 1474426238805 e 1474426236322 (verificador por casos 06/11)"),
 (1473986117229, "repete 1473986065214 (GPIIb/IIIa com fibrinogênio formando o plug temporário) (verificador por casos 06/11)"),
 (1474340529919, "repete a aderência à parede de 1474426422178 (trombo pré × post-mortem)"),
 (1474426159910, "repete 1474426163014 (nitrogênio após subida rápida, doença da descompressão)"),
 (1474340571288, "repete o tPA de 1474060036899 e a pista entrega a resposta (plasminogen → plasmin)"),
 (1473995508259, "lista numerada dos fatores intrínsecos: o professor diz que não precisa saber os nomes; a via intrínseca entra por 1473995572360"),
 (1473995525861, "lista numerada dos fatores da via comum: o professor diz que não precisa saber os nomes; a convergência entra por 1473995562419"),
 (1471899426119, "fonte marcada Only_Step_2 (F-20261105-CODEX-05); o trombo mural pós-infarto entra por 1568212550823"),
 (1495883587351, "fonte marcada Only_Step_2 (F-20261105-CODEX-05); o cor pulmonale do TEP maciço entra pelo autoral c-cor-pulmonale"),
 (1473986362035, "mesma resposta (adhesion) de 1473986009866; o defeito de adesão por falta de GPIb fica no Extra de c-adesao-agregacao"),
 (1473986036899, "mesma resposta (GPIIb/IIIa) de 1488847733019, que liga o ADP ao clopidogrel"),
 (1473995463276, "mesma resposta (liver) de 1473995761090, que já liga fígado e hemostasia secundária"),
 (1474340546188, "mesma resposta (thrombosis) de 1474333732502; o exemplo de estase pós-infarto entra por 1568212550823"),
 (1791054019646, "angina instável (NEBLI vivo, suspenso): cardiologia, fora do recorte; a ruptura de placa entra por sh-1791054019772"),
 (1791780360633, "TNF e IL-1 ativando o endotélio (aula 38, suspenso): moléculas de adesão da inflamação aguda, não trombose"),
 (1473982141617, "mesma ideia de 1473986117229 (plug primário frágil), que diz o porquê (GPIIb/IIIa com fibrinogênio)"),
 (1473986004354, "mesma ideia de 1473986117229 em pergunta sim/não"),
 (1473986172487, "contagem normal de plaquetas: valor de laboratório, não é processo da aula"),
 (1525137303328, "PFA-100: detalhe de laboratório"),
 (1473986028528, "repete 1474056842486 (grânulo alfa com vWF)"),
 (1473995704528, "ristocetina: teste diagnóstico de doença hemorrágica, fora do recorte"),
 (1489973497370, "ristocetina em von Willebrand e Bernard-Soulier: teste diagnóstico, fora do recorte"),
 (1473995714094, "desmopressina: tratamento (UC19)"),
 (1525138104051, "tempo de trombina: exame que a aula não cita"),
 (1474340515044, "trombose em artéria e veia: resposta trivial, coberta por c-arterial-venoso"),
 (1474340588031, "homocisteína: causa de dano endotelial que a aula não cita; vitamina (UC08)"),
 (1474340594888, "deficiência de B12/folato e trombose: a aula não cita"),
 (1474340602053, "vitaminas e trombose: a aula não cita"),
 (1474340609370, "deficiência de cistationina beta-sintase: erro inato, outra UC"),
 (1473995528007, "passo isolado XIIa→XI coberto por 1473995508259 (fatores da via intrínseca); o professor pede o processo, não cada ativação"),
 (1473995532126, "passo isolado XIa→IX coberto por 1473995508259"),
 (1473995552377, "passo isolado VIIa→X coberto por 1473995568285 e 1473995504794"),
 (1474132397341, "passo isolado IXa/VIIIa→X coberto por 1473995508259"),
 (1520729623791, "meia-vida dos fatores: farmacologia da varfarina (UC19)"),
 (1705515121724, "deficiência de fator VII: doença, fora do recorte"),
 (1488765251203, "monitorização da varfarina: farmacologia (UC19)"),
 (1488847818071, "classes de trombolíticos: farmacologia (UC19)"),
 (1488850212066, "reversão de trombolíticos: farmacologia (UC19)"),
 (1474060045108, "papel secundário da plasmina (destrói fatores), além da aula"),
 (1474060047292, "papel secundário da plasmina (inibe agregação), além da aula"),
 (1473995716769, "bioquímica da vitamina K (epóxido redutase): UC01/UC19"),
 (1473995718828, "bioquímica da vitamina K (gama-glutamil carboxilase): UC01"),
 (1473995743024, "deficiência de vitamina K no recém-nascido: clínica, fora do recorte"),
 (1473995752044, "deficiência de vitamina K por antibiótico: clínica, fora do recorte"),
 (1473995754384, "deficiência de vitamina K por má absorção: clínica, fora do recorte"),
 (1473995759027, "laboratório da deficiência de vitamina K: clínica, fora do recorte"),
 (1581706459775, "vitamina K no recém-nascido: conduta (Step 2)"),
 (1474426259158, "cintilografia V/Q: diagnóstico do TEP, Pneumologia"),
 (1474426261606, "alcalose respiratória no TEP: fisiologia respiratória, outra UC"),
 (1474426264636, "exame de escolha no TEP: diagnóstico clínico (Step 2)"),
 (1474426282700, "falha de enchimento na TC: radiologia do TEP, fora do recorte"),
 (1474426326611, "orientação da cunha do infarto pulmonar: detalhe macroscópico além da aula"),
 (1474426331306, "morte súbita por êmbolo em sela: repete 1495883587351 (TEP maciço)"),
 (1474426382395, "dissociação eletromecânica: cardiologia, fora do recorte"),
 (1581876990197, "gradiente A-a no TEP: fisiologia respiratória, outra UC"),
 (1474426251470, "apresentação clínica do infarto pulmonar: clínica"),
 (1474426253893, "apresentação clínica do infarto pulmonar: clínica"),
 (1474426256653, "apresentação clínica do infarto pulmonar: clínica"),
 (1524148797489, "ECG S1Q3T3: cardiologia, fora do recorte"),
]
FORA_DO_RECORTE = [
 "Capa, divisórias e encerramento (lâminas 1, 17, 36 e 60).",
 "CIVD, coagulopatia de consumo, petéquias e púrpuras: aula 70 Choque e CIVD.",
 "Nomes e números de todos os fatores da cascata: o professor diz que não precisa saber os nomes; entram as vias, a convergência no X e a retroalimentação da trombina.",
 "Árvore de incidência e mortalidade do TEP (lâmina 40): epidemiologia ilustrativa.",
 "Tratamento e identificação da embolia gasosa e do TEP: conduta (Step 2).",
]

CARDS = [
 # ---------- Lâmina 2: as quatro fases ----------
 au("c-fases", ORG("<b>Hemostasis</b> phases after vessel injury, in order:<br>- <b>arteriole</b> contracts: {{c1::vasoconstriction}}<br>- <b>platelets</b> adhere and aggregate: {{c1::primary}} hemostasis<br>- <b>fibrin</b> cements the plug: {{c1::secondary}} hemostasis<br>- <b>tissue plasminogen activator (tPA) and thrombomodulin</b> limit the clot: {{c1::balance}} phase"),
    "V-pilar", A_, "As quatro fases da hemostasia", 2, "lâmina 2; transcrição p.4", motivacao="m1", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="A hemostasia, ela se dá em, basicamente, quatro fases",
    fontes=F("transcrição p.4", "A hemostasia, ela se dá em, basicamente, quatro fases"),
    sem_imagem="lâmina 2 é texto; as figuras de cada fase estão nos cards seguintes",
    extra="Platelets are bricks and fibrin is the cement, so the primary plug alone is weak.<br>Too much hemostasis causes thrombosis, and too little causes bleeding."),
 K(1474333732502, "A-aula", A_, "Trombose é hemostasia patológica", 2, "lâmina 2: hemostasia demais gera trombose"),
 K(1473985980516, "A-aula", A_, "Primária: plaqueta e parede", 2, "lâmina 2: hemostasia primária"),
 K(1473985992028, "V-hy", A_, "Secundária: cascata", 2, "lâmina 2: hemostasia secundária"),
 # ---------- Lâmina 3: vasoconstrição ----------
 K(1473985997545, "V-hy", A_, "Vasoconstrição reflexa e endotelina", 3, "lâmina 3: endotelina e reflexo"),
 au("c-turbulencia", "Reflex <b>vasoconstriction</b> after vessel injury makes blood flow {{c1::turbulent}}, which pushes platelets from the center onto the exposed <b>matrix</b>",
    "A-aula", A_, "Vasoconstrição turbilhona e leva plaqueta à matriz", 3, "lâmina 3; transcrição p.6", motivacao="m5",
    fontes=F("transcrição p.6", "turbilhono, eu coloco as plaquetas que estavam lá no meio em contato com essa matriz extracelular"),
    sem_imagem="a figura da lâmina 3 mostra a vasoconstrição, não o fluxo turbulento que o card cobra; retirada pelo verificador",
    extra="Laminar flow keeps platelets in the center, away from the wall.<br>Platelets ignore intact endothelium but stick to exposed matrix."),
 # ---------- Lâmina 4: hemostasia primária ----------
 K(1473986009866, "A-aula", A_, "Adesão depois da vasoconstrição", 4, "lâmina 4: adesão"),
 K(1473986015897, "A-aula", A_, "vWF liga o colágeno exposto", 4, "lâmina 4: vWF na matriz"),
 K(1473986031590, "A-aula", A_, "Degranulação após adesão", 4, "lâmina 4: liberação de grânulos"),
 K(1474059949481, "R-detalhe", A_, "Grânulos densos: Ca, ADP, serotonina, histamina", 4, "lâmina 4: ADP liberado"),
 K(1473986034094, "A-aula", A_, "ADP muda a forma da plaqueta", 4, "lâmina 4: mudança de forma"),
 K(1473986040113, "V-hy", A_, "ADP reduz cAMP e ativa", 4, "lâmina 4: ADP ativa"),
 K(1473986059652, "A-aula", A_, "TXA2 promove agregação", 4, "lâmina 4: TXA2"),
 au("c-adesao-agregacao", ORG("<b>Primary hemostasis</b> steps by what the platelet binds:<br>- platelet to <b>exposed matrix</b> through vWF: {{c1::adhesion}}<br>- platelet to <b>platelet</b> through fibrinogen: {{c1::aggregation}}"),
    "V-pilar", A_, "Adesão × agregação", 4, "lâmina 4; transcrição p.8", motivacao="m8", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Então, a adesão é da plaqueta na matriz, e a agregação é da plaqueta na plaqueta",
    fontes=F("transcrição p.8", "Então, a adesão é da plaqueta na matriz, e a agregação é da plaqueta na plaqueta"),
    imagem="im69-plaqueta.png",
    extra="Adhesion uses the GPIb receptor and aggregation uses GPIIb/IIIa, so a defect in either causes bleeding.<br>ADP and thromboxane A2 from the first platelets recruit the next ones." + IMG("plaqueta")),
 # ---------- Lâmina 5: hemostasia secundária ----------
 K(1473985984856, "A-aula", D_, "Secundária estabiliza o plug", 5, "lâmina 5: fibrina cimenta"),
 K(1473995568285, "A-aula", D_, "Fator tecidual ativa o VII", 5, "lâmina 5: fator tecidual do endotélio"),
 K(1473995466091, "A-aula", D_, "Superfície fosfolipídica da plaqueta", 5, "lâmina 5: fosfolipídio da plaqueta ativa a cascata"),
 K(1473995163159, "V-hy", D_, "Trombina converte fibrinogênio em fibrina", 5, "lâmina 5: trombina e fibrina"),
 K(1473995444571, "R-detalhe", D_, "Fator XIIIa faz ligações cruzadas", 5, "lâmina 5: rede de fibrina estável"),
 # ---------- Lâmina 6: o freio ----------
 K(1474060036899, "V-hy", D_, "tPA converte plasminogênio em plasmina", 6, "lâmina 6: ativador de plasminogênio", text="In the first step of <u>fibrinolysis</u>, {{c1::plasminogen}} is converted to {{c2::plasmin}} by an endothelial enzyme, {{c3::tPA}}"),
 K(1474340580166, "A-aula", B_, "Trombomodulina e proteína C", 6, "lâmina 6: trombomodulina"),
 # ---------- Lâminas 7–8: endotélio ----------
 K(1474340549347, "A-aula", B_, "Endotélio esconde colágeno e fator tecidual", 19, "lâmina 19: dano endotelial expõe colágeno e fator tecidual"),
 K(1474340552038, "A-aula", B_, "Endotélio produz PGI2 e NO", 8, "lâmina 8: antiplaquetários"),
 K(1474340554238, "R-detalhe", B_, "PGI2 e NO vasodilatam", 8, "lâmina 8: vasodilatação e fluxo laminar"),
 K(1473986001040, "V-hy", B_, "Balanço TXA2 × PGI2 e NO", 8, "lâmina 8: pró × antiagregação"),
 K(1474340559882, "A-aula", B_, "Heparina-like aumenta antitrombina III", 8, "lâmina 8: moléculas heparina-like"),
 K(1473986024573, "R-detalhe", B_, "vWF dos corpos de Weibel-Palade", 8, "lâmina 8: endotélio produz vWF"),
 K(1474056842486, "R-detalhe", B_, "Grânulo alfa com vWF e fibrinogênio", 8, "lâmina 8: vWF de plaqueta"),
 au("c-endotelio-pro", ORG("<b>Activated endothelium</b> turns procoagulant by releasing:<br>- for <b>platelet adhesion</b>: {{c1::von Willebrand factor}}<br>- to start the <b>extrinsic pathway</b>: {{c1::tissue factor}}<br>- to <b>block fibrinolysis</b>: {{c1::plasminogen activator inhibitor}}"),
    "V-pilar", B_, "Endotélio ativado é pró-trombótico", 8, "lâmina 8; transcrição p.14; prova 2016 P2 2.10", motivacao="m14", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="O endotélio, no começo, tem vários fatores protrombóticos",
    fontes=F("transcrição p.14", "O endotélio, no começo, tem vários fatores protrombóticos"),
    imagem="im69-endotelio-pro.png",
    extra="Injury and inflammatory cytokines activate the endothelium, which is why inflammation is prothrombotic.<br>Resting endothelium does the opposite, with PGI2, NO, thrombomodulin and tPA." + IMG("endotelio-pro")),
 # ---------- Lâminas 9–10: plaquetas ----------
 K(1473986020742, "A-aula", C_, "GPIb liga o vWF", 9, "lâmina 9: adesão pela GPIb"),
 K(1473986065214, "A-aula", C_, "GPIIb/IIIa e fibrinogênio agregam", 9, "lâmina 9: agregação"),
 K(1473986370477, "R-detalhe", C_, "Glanzmann: defeito de GPIIb/IIIa", 9, "lâmina 9: defeito da GPIIb/IIIa"),
 K(1473995668705, "R-detalhe", C_, "von Willebrand: distúrbio hemorrágico herdado mais comum", 9, "lâmina 9: falta de vWF"),
 K(1473986052600, "R-detalhe", C_, "TXA2 feito pela COX-1", 10, "lâmina 10: COX e TXA2"),
 K(1473986398130, "V-hy", C_, "Aspirina inibe COX e TXA2", 10, "lâmina 10: AAS"),
 K(1488847733019, "V-hy", C_, "Clopidogrel bloqueia receptor de ADP", 10, "lâmina 10: clopidogrel"),
 K(1488847772054, "R-detalhe", C_, "Inibidores de GPIIb/IIIa", 10, "lâmina 10: anticorpos contra GPIIb/IIIa"),
 # ---------- Lâminas 11–13: cascata ----------
 K(1473995468409, "A-aula", D_, "Cálcio na cascata", 11, "lâmina 11: cofator cálcio"),
 K(1473995572360, "V-hy", D_, "Colágeno ativa o XII (intrínseca)", 12, "lâmina 12: via intrínseca"),
 K(1473995562419, "V-hy", D_, "Xa ativa a protrombina", 12, "lâmina 12: X → trombina"),
 K(1473995557603, "V-hy", D_, "Trombina ativa o V", 13, "lâminas 12 e 13: retroalimentação e efeitos da trombina"),
 K(1473995720927, "V-hy", D_, "Vitamina K: II, VII, IX, X, C e S", 12, "lâmina 15: proteínas C e S dependentes de K"),
 K(1473995740705, "A-aula", D_, "Falta de K reduz proteína C e S", 12, "lâmina 15: C e S dependentes de vitamina K", text="<div>What anticoagulant proteins have decreased activity in <b>vitamin K deficiency</b>? {{c1::Protein C}} and {{c1::protein S}}</div>"),
 K(1473995761090, "A-aula", D_, "Insuficiência hepática compromete a secundária", 13, "prova 2018 P3 1.5: hepatopatia compromete a hemostasia secundária"),
 K(1486591400578, "V-hy", D_, "Hepatopatia aumenta o TP", 13, "prova 2018 P3 1.5"),
 # ---------- Lâmina 14: fibrinólise ----------
 K(1474060034604, "A-aula", D_, "Fibrinólise remove o trombo", 14, "lâmina 14: fibrinólise"),
 K(1474060042847, "A-aula", D_, "Plasmina cliva fibrina", 14, "lâmina 14: plasmina"),
 K(1474060049763, "R-detalhe", D_, "Alfa-2-antiplasmina", 14, "apostila: elementos antiplasmina"),
 K(1474060020070, "V-hy", D_, "D-dímero vem da fibrina", 14, "lâmina 14: produtos de degradação"),
 K(1474340730687, "R-detalhe", D_, "tPA como trombolítico", 14, "lâmina 14; prova 2015 P1 3.4 (tPA e reperfusão)"),
 # ---------- Lâmina 15: anticoagulação fisiológica ----------
 K(1474340567887, "A-aula", D_, "Antitrombina III inativa trombina", 15, "lâmina 15: antitrombina"),
 K(1474340632913, "A-aula", D_, "Proteína C e S inativam Va e VIIIa", 15, "lâmina 15: proteínas C e S"),
 # ---------- Lâmina 16: exames ----------
 K(1473986177028, "V-hy", D_, "Tempo de sangramento aumenta em distúrbio plaquetário", 16, "lâmina 16: TS avalia plaqueta"),
 K(1473986174744, "R-detalhe", D_, "Tempo de sangramento normal", 16, "lâmina 16: TS"),
 K(1473995480416, "A-aula", D_, "TP mede extrínseca e comum", 16, "lâmina 16: TP"),
 K(1473995492923, "V-hy", D_, "INR calculado do TP", 16, "lâmina 16: INR"),
 K(1473995486704, "A-aula", D_, "TTPA mede intrínseca e comum", 16, "lâmina 16: TTPA"),
 K(1488767931946, "V-hy", D_, "TTPA controla heparina", 16, "lâmina 16: controle de heparina"),
 # ---------- Lâminas 18–19: Virchow e dano endotelial ----------
 K(1474340536548, "V-hy", E_, "Tríade de Virchow", 18, "lâmina 18; provas 2025 P4 1.3 e 2016 P2 2.9", text="<div>What are the three major risk factors for <u>thrombosis</u> ({{c4::Virchow}} triad)?<br>- {{c1::stasis}} of blood flow<br>- {{c1::endothelial}} cell damage<br>- {{c1::hypercoagulability}}</div>"),
 K(1474340539643, "A-aula", E_, "Estase e turbulência aumentam trombose", 24, "lâminas 24 a 27: fluxo"),
 K(1471898867686, "V-hy", E_, "Ruptura de placa e trombose coronária", 20, "lâminas 20 a 22 (exemplo da aterosclerose); provas 2015 P3 1.2 e 2015 P3sub 1.4"),
 K(1568212550823, "R-detalhe", E_, "Estase na parede que não contrai forma trombo mural", 28, "lâminas 28 a 30 (exemplo: miocárdio que não contrai)"),
 # ---------- Lâmina 31: hipercoagulabilidade ----------
 K(1474340615751, "A-aula", E_, "Estado hipercoagulável", 31, "lâmina 31: excesso de pró-coagulante ou falta de anticoagulante"),
 K(1474340622747, "V-hy", E_, "TVP em jovem ou recorrente", 31, "lâmina 31: atenção nos jovens", text="<div>The classic presentation of a <u>hypercoagulable state</u> is {{c1::recurrent}} DVTs or DVT at a {{c2::young age}}</div>"),
 K(1474340675609, "V-hy", E_, "Leiden: causa herdada mais comum", 31, "lâmina 31: fator V de Leiden"),
 K(1474340658912, "A-aula", E_, "Leiden resiste à proteína C", 31, "lâmina 31: fator V muito ativo"),
 K(1474340678804, "A-aula", E_, "Mutação da protrombina", 31, "lâmina 31: aumento de protrombina"),
 K(1474340722065, "A-aula", E_, "Perda gestacional recorrente", 31, "lâmina 31: abortos de repetição", text="<div>{{c2::Hypercoagulable}} <b>states</b> are often complicated by <u>recurrent</u> {{c1::pregnancy}} <b>loss</b> (women)</div>"),
 K(1474340718532, "V-hy", E_, "Estrogênio aumenta fatores", 31, "lâmina 31: anticoncepcionais e gestação"),
 K(1487815405384, "V-hy", E_, "Síndrome antifosfolípide", 31, "lâmina 31: síndrome antifosfolípide"),
 # ---------- Lâminas 32–34: características do trombo ----------
 au("c-arterial-venoso", ORG("<b>Thrombi</b> by what causes them:<br>- <b>turbulence and endothelial damage</b>, mostly platelets and fibrin: {{c1::arterial}}<br>- <b>stasis</b>, rich in red cells: {{c1::venous}}"),
    "V-pilar", F_, "Trombo arterial × venoso", 32, "lâmina 32; apostila cap.1; monitoria", motivacao="m36", organizador=True,
    organizacao_fonte="fontes/slides.txt", organizacao_trecho="Mais avermelhados – por ter mais hemácias",
    fontes=F("lâmina 32", "Mais avermelhados – por ter mais hemácias"),
    imagem="im69-arterial-venoso.png",
    extra="Arterial thrombi grow backward from the injury, in coronary, cerebral and femoral arteries.<br>Venous thrombi grow toward the heart, mostly in deep leg veins, and the figure shows one next to a valve." + IMG("arterial-venoso")),
 K(1474340518305, "V-hy", F_, "Trombose mais comum nas veias profundas", 32, "lâmina 32: veias profundas"),
 K(1474340521075, "V-hy", F_, "Linhas de Zahn", 34, "lâmina 34: linhas de Zahn"),
 K(1474426422178, "V-hy", F_, "Trombo pré × post-mortem", 34, "lâmina 34: trombo × coágulo"),
 # ---------- Lâmina 35: destino ----------
 au("c-destino", ORG("<b>Fates of a thrombus</b>:<br>- dissolved by <b>fibrinolysis</b>: {{c1::resolution}}<br>- <b>fragment</b> travels in the blood: {{c1::embolization}}<br>- <b>granulation tissue</b> invades it and fixes it to the wall: {{c1::organization}}<br>- <b>new channels</b> open through it: {{c1::recanalization}}"),
    "V-pilar", F_, "Destino do trombo", 35, "lâmina 35; transcrição p.62", motivacao="m38", organizador=True,
    organizacao_fonte="fontes/transcricao.txt", organizacao_trecho="Quando eu tenho um trombo no vaso, o que acontece com ele?",
    fontes=F("transcrição p.62", "Quando eu tenho um trombo no vaso, o que acontece com ele?"),
    imagem="im69-destino-esquema.png",
    extra="Organization leaves a narrowed, turbulent segment, covered again by endothelium, that can thrombose again.<br>Recanalized channels restore some flow but are inefficient." + IMG("destino-esquema")),
 # ---------- Lâminas 37–38: embolia ----------
 au("c-embolia", "Any detached solid, liquid or gaseous <b>intravascular mass</b> carried by the blood to a distant site is an {{c1::embolus}}",
    "V-pilar", G_, "Definição de embolia", 37, "lâmina 37; transcrição p.64; apostila cap.2", motivacao="m39",
    fontes=F("lâmina 37", "Massa intravascular líquida, sólida ou gasosa transportada"),
    sem_imagem="definição em texto na lâmina 37; os tipos estão nos cards seguintes",
    extra="Over 95% are pieces of thrombus, and it lodges where the vessel becomes narrower than the embolus.<br>Fat from fractured long bones, nitrogen bubbles in divers and amniotic fluid at delivery are rarer emboli."),
 K(1474423006579, "A-aula", G_, "Tromboêmbolo é o tipo mais comum", 37, "lâmina 37: êmbolo quase sempre é trombo"),
 # ---------- Lâmina 39: TEP ----------
 K(1474426211966, "V-hy", G_, "Êmbolo pulmonar vem das veias profundas", 39, "lâmina 39: origem venosa"),
 K(1474426238805, "V-hy", G_, "Êmbolo pequeno se resolve", 39, "lâmina 39: consequência depende do tamanho"),
 au("c-cor-pulmonale", "Most <b>pulmonary emboli</b> are silent, but blocking more than about {{c1::60%}} of the pulmonary circulation causes acute <b>right heart failure</b>",
    "A-aula", G_, "Obstrução acima de 60%: cor pulmonale", 39, "lâmina 39; transcrição p.66", motivacao="m41",
    fontes=F("lâmina 39", "> 60% de obstrução – Cor pulmonale"),
    sem_imagem="lâmina 39 é texto; o êmbolo está nas fotos dos cards de exemplo",
    extra="The lung has a large functional reserve, so small emboli go unnoticed.<br>A massive embolus makes the right ventricle pump against a sudden rise in pulmonary resistance."),
 K(1474426389805, "A-aula", G_, "Hipertensão pulmonar por êmbolos crônicos", 39, "lâmina 39: consequências tardias"),
 K(1474426307667, "V-hy", G_, "TEP com D-dímero elevado", 39, "lâmina 14 (D-dímero no TEP)"),
 K(1474426236322, "V-hy", G_, "Dupla circulação torna o TEP silencioso", 40, "lâminas 40 a 47 (exemplo do TEP): circulação brônquica", text="<div>Emboli in the <b>lung</b> are often clinically silent because of its dual blood supply, from the pulmonary arteries and the {{c1::bronchial}} arteries</div>"),
 K(1474426241278, "V-hy", G_, "Quando o TEP causa infarto pulmonar", 46, "lâminas 46 e 47 (infarto pulmonar)"),
 K(1474426314905, "V-hy", G_, "Infarto pulmonar hemorrágico em cunha", 46, "lâmina 46 (infarto pulmonar)"),
 # ---------- Lâmina 48: sistêmico ----------
 K(1474426199614, "V-hy", G_, "Êmbolo sistêmico vem do coração esquerdo", 48, "lâmina 48: 80% das cavidades cardíacas"),
 # ---------- Lâminas 49–51: gasosa, gordurosa, amniótica ----------
 K(1474426163014, "V-hy", G_, "Nitrogênio após subida rápida", 49, "lâmina 49: doença da descompressão"),
 K(1474426144108, "A-aula", G_, "Gordura após fratura de osso longo", 50, "lâmina 50: fraturas"),
 K(1474426151822, "V-hy", G_, "Tríade da embolia gordurosa", 50, "lâmina 50: respiratório, neurológico, trombocitopenia", text="{{c4::Fat}} <b>embolism</b> is characterized by a <u>triad</u> of:<br>{{c1::Hypox}}emia<br>{{c1::Neurological}} abnormalities<br>{{c1::Petechial rash}} overlying the chest"),
 K(1474426179963, "V-hy", G_, "Líquido amniótico no parto", 51, "lâmina 51"),
 K(1474426192275, "V-hy", G_, "Células escamosas e queratina no êmbolo amniótico", 51, "lâmina 51: queratina do bebê (fala do professor)"),
 # ---------- Lâminas 52–54: causas do infarto ----------
 K(1471898887090, "A-aula", H_, "Vasoespasmo coronário", 52, "lâmina 52: vasoespasmo"),
 K(1463334152127, "V-hy", H_, "Torção testicular: infarto hemorrágico", 52, "lâmina 52: torção"),
 K(1487469816961, "V-hy", H_, "Necrose coagulativa nos infartos, exceto cérebro", 52, "lâminas 52 e 53: o infarto é necrose coagulativa, salvo no cérebro"),
 K(1487469877849, "V-hy", H_, "Infarto cerebral: necrose liquefativa", 54, "lâmina 54 (exemplo: AVC)"),
 # ---------- Lâminas 55–58: vermelho × branco ----------
 K(1487469843369, "V-hy", H_, "Infarto vermelho", 55, "lâmina 55; provas 2015 P3sub 1.5 e 2016 P2 2.11", extra_add="" + IMG("infarto-vermelho")),
 K(1487469835042, "V-hy", H_, "Infarto pálido", 57, "lâmina 57; prova 2018 P3 3.4", extra_add="" + IMG("infarto-branco")),
 # ---------- Lâmina 59: fatores ----------
 au("c-colateral", "A <b>slowly developing</b> arterial occlusion causes a smaller infarct than a sudden one, because it allows {{c1::collateral circulation}} to develop",
    "A-aula", H_, "Oclusão lenta permite colaterais", 59, "lâmina 59; transcrição p.90; prova 2018 P3 3.4", motivacao="m51",
    fontes=F("transcrição p.90", "Se eu tenho um quadro lento, eu posso ter desenvolvimento de colaterais"),
    sem_imagem="lâmina 59 é lista de fatores sem figura",
    extra="Infarct size also depends on the vessel caliber, the tissue's vulnerability to hypoxia, blood oxygen content and how fast flow is restored."),
 K(1481771752557, "R-detalhe", H_, "Cérebro: dano irreversível após 5 min", 59, "lâmina 59: vulnerabilidade à hipóxia"),
]

STRIP_IMG = {"ak1474340712036": ["6a033fc58b336b6eb6ada44e24a7fa5c.webp"], "ak1474426307667": ["2bcd2eccefc95458787af167a8a211af.webp"],
             "ak1474060020070": ["41b0619843ed58844d7fe182d22d0310.webp"], "ak1471898887090": ["20eb470e4fc57778fed96e9343a5bc57.webp"],
             "ak1463334152127": ["54ec9d91b48700280e8b1fe923f92f58.webp"], "ak1568212550823": ["37456b443a2eb91404576a797577500e.webp"],
             "ak1473986370477": ["753d443cb002375ee5a7936cf6530e6a.webp"], "ak1473986020742": ["753d443cb002375ee5a7936cf6530e6a.webp"]}

finalizar(CARDS, HERE, BUSCA)

from nebli.spec_lib import _call as _chamada
_ids = [c["src"] for c in CARDS if c["kind"] == "text" and "text" not in c]
_vivas = {n["noteId"]: n["fields"].get("Text", {}).get("value", "") for n in (_chamada("notesInfo", notes=_ids) if _ids else [])}
_CZ = _re.compile(r"\{\{c(\d+)::(.*?)\}\}", _re.S)
def _limpa(m):
    return "{{c" + m.group(1) + "::" + _re.sub(r"</?(?:b|i|u|strong|em)>", "", m.group(2)) + "}}"
for _c in CARDS:
    if _c["kind"] == "text" and "text" not in _c:
        _novo = _re.sub(r"\{\{c(\d+)::([^{}:]+?) \(([^()]+)\)\}\}", r"{{c\1::\2}} (\3)", _CZ.sub(_limpa, _vivas.get(_c["src"], "")))
        if _novo and _novo != _vivas.get(_c["src"], ""):
            _c["text"] = _novo

VERSO = {"ak1474423006579": "Fat, nitrogen gas and amniotic fluid emboli are the rare exceptions.",
 "ak1474333732502": "Thrombosis is hemostasis happening where and when it should not, inside an intact or diseased vessel.",
 "ak1473985980516": "The platelets stick to the exposed matrix of the injured wall, mostly through von Willebrand factor.",
 "ak1473985997545": "Endothelium that loses contact with its neighbors releases endothelin.<br>Constriction reduces bleeding and makes flow turbulent.",
 "ak1474060036899": "The endothelium releases tPA once it senses fibrin, so the clot does not grow until it closes the vessel.",
 "ak1474340554238": "Vasodilation restores laminar flow and keeps platelets away from the wall.",
 "ak1473986001040": "The balance tips toward aggregation where the endothelium is injured and toward fluid blood where it is intact.",
 "ak1473995668705": "Lack of vWF prevents platelet adhesion, so it is a defect of primary hemostasis.",
 "ak1488847772054": "They block the fibrinogen receptor, preventing platelet aggregation while adhesion is preserved.",
 "ak1473995504794": "Tissue factor from the endothelium activates factor VII, which then activates factor X.",
 "ak1473995525861": "Both pathways converge on factor X, so blocking the common pathway stops coagulation from either trigger.",
 "ak1474060034604": "Fibrinolysis is the balance phase that keeps the plug from occluding the vessel.",
 "ak1474060042847": "The fragments of fibrin released into the blood include D-dimer.",
 "ak1474060049763": "Antiplasmin keeps plasmin activity local to the clot.",
 "ak1474340730687": "Given early, it dissolves a fresh coronary or cerebral thrombus and restores flow.",
 "ak1474340567887": "Heparin-like molecules on the endothelium enhance it, and heparin works the same way.",
 "ak1473986174744": "A prolonged bleeding time points to a platelet problem, that is, primary hemostasis.",
 "ak1488847779733": "Antiplatelet drugs impair aggregation, so the primary plug takes longer to form.",
 "ak1474340718532": "This is why estrogen-containing contraceptives and pregnancy raise the risk of venous thrombosis.",
 "ak1474426422178": "A post-mortem clot is soft, not attached and not layered, because it formed without flow.",
 "ak1474426238805": "Small emboli are dissolved by fibrinolysis.",
 "ak1474426389805": "Organized emboli narrow the pulmonary arteries and raise resistance over time.",
 "ak1474426236322": "Bronchial arteries keep the lung tissue alive, so infarction is uncommon and, when it happens, hemorrhagic.",
 "ak1474426159910": "Nitrogen dissolved at high pressure comes out as bubbles when pressure drops quickly.",
 "ak1474426179963": "Fetal squamous cells and keratin in the fluid are highly thrombogenic."}
for c in CARDS:
    if c["key"] in VERSO and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"c-fases": "ganho: ordena as quatro fases com o papel de cada uma; os AnKing cobram cada fase solta",
 "c-adesao-agregacao": "ganho: contrasta os dois tipos de ligação que o professor separa; os AnKing cobram o receptor de cada um",
 "c-endotelio-pro": "ganho: reúne o lado pró-trombótico do endotélio ativado com o inibidor do ativador de plasminogênio, ausente no AnKing",
 "c-turbulencia": "ganho: liga a vasoconstrição ao contato da plaqueta com a matriz (fala do professor); 1473986015897 só diz que o vWF liga o colágeno exposto",
 "c-arterial-venoso": "ganho: contrasta trombo arterial e venoso pela causa; 1474340539643 só diz que estase e turbulência aumentam o risco"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "im69-endotelio-pro.png": "lâmina 7 recortada: só o lado que favorece a trombose (adesão por vWF, fator tecidual e via extrínseca)",
 "im69-destino-esquema.png": "lâmina 35 recortada: só o esquema dos quatro destinos do trombo, sem a faixa de histologia",
 "im69-trombina.png": "lâmina 13: trombina no centro com fibrina, agregação plaquetária, ativação do endotélio, de neutrófilos e monócitos",
 "im69-virchow.png": "lâmina 18: triângulo de Virchow com lesão endotelial, fluxo anormal e hipercoagulabilidade",
 "im69-vasoconstricao.png": "lâmina 3: vaso com o local da lesão, endotelina e vasoconstrição reflexa sobre a matriz exposta",
 "im69-endotelio.png": "lâmina 7: endotélio com o lado que favorece (vWF, fator tecidual) e o que inibe (trombomodulina, proteína C, antitrombina, PGI2, NO, tPA) a trombose",
 "im69-plaqueta.png": "lâmina 9: plaqueta aderindo ao vWF pela GPIb e agregando pelo fibrinogênio na GPIIb-IIIa, com os defeitos de cada ponto",
 "im69-arterial-venoso.png": "lâmina 32: trombo venoso vermelho junto à válvula, com o fluxo",
 "im69-destino.png": "lâmina 35: trombo venoso e seus destinos (resolução, embolia ao pulmão, organização e recanalização) com histologia",
 "im69-infarto-vermelho.png": "lâmina 55: infarto vermelho (hemorrágico) macroscópico",
 "im69-infarto-branco.png": "lâmina 57: coração com infarto pálido agudo, subagudo e cicatrizado",
}
REVISAO = {}
ESCOPO = {"objetivo": "Entender a hemostasia normal em quatro fases comandadas pelo endotélio e, como consequência, a trombose (tríade de Virchow, trombo arterial × venoso, destino), a embolia e o infarto (vermelho × branco); doenças e fármacos só como pontos do processo.",
          "centrais": [["Fases", "c-fases"], ["Adesão e agregação", "c-adesao-agregacao"], ["Trombo arterial e venoso", "c-arterial-venoso"], ["Destino do trombo", "c-destino"],
                       ["Embolia", "c-embolia"], ["Endotélio ativado", "c-endotelio-pro"], ["Tríade de Virchow", "ak1474340536548"], ["Infarto vermelho e branco", "ak1487469843369", "sh-1792117377198"]],
          "exemplos": ["sh-1791054019772", "ak1474340546188", "ak1471899426119", "ak1474426236322", "ak1474426241278", "ak1474426314905", "sh-1792117376722", "sh-1792117377748"],
          "outras_aulas": []}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))

for _c in CARDS:
    if _c["key"] == "ak1473995557603":
        _c["extra_add"] = (_c.get("extra_add") or "") + IMG("trombina")
    elif _c["key"] in ("ak1473986020742", "ak1473986370477"):
        _c["extra_add"] = (_c.get("extra_add") or "") + IMG("plaqueta")
    elif _c["key"] == "ak1474340536548":
        _c["extra_add"] = (_c.get("extra_add") or "") + IMG("virchow")
    elif _c["kind"] == "text" and "<img" not in (_c.get("extra_add") or ""):
        _c["sem_imagem"] = "fato de texto do AnKing sem figura focal na aula; a figura do bloco está no card autoral ou no card vizinho"
    if _c["kind"] == "autoral" and _c.get("imagem"):
        _c["slide_sem_alternativa"] = "a figura é do Robbins reproduzida na lâmina da aula, referência do deck; recorte em 230 dpi"
