# Especificação curada da AN07 (run uc08-an07-20260929a). Somente cards, sem E1. Novos cards em inglês.
RUN_ID = "uc08-an07-20260929a"
SHORT = "an07"
LESSON = "2026-uc08-anatomia-07-vascularizacao-visceras"
DECK = "NEBLI::UC08::P1::Anatomia::Vascularização das vísceras"
CRITERIOS = "MEMORY.md + FEEDBACKS (até F-20260929-CLAUDE-02) + EXECUCAO-DECK-AULA + RECONSTRUCAO-UC08, 29/09/2026"

MEDIA = {
    "nebli-uc08-an07-s08-porta.jpeg": "fontes/p08_img0.jpeg",
    "nebli-uc08-an07-s09-cisterna.jpeg": "fontes/p09_img2.jpeg",
    "nebli-uc08-an07-s12-ams.jpeg": "fontes/p12_img0.jpeg",
    "nebli-uc08-an07-s18-ami.jpeg": "fontes/p18_img0.jpeg",
    "nebli-uc08-an07-s22-reto.jpeg": "fontes/p22_img0.jpeg",
}
CR = '<br><span style="font-size: 10pt;"><em>{}</em></span>'
SLIDE = lambda f, ref, w=440: f'<img src="{f}" width="{w}">' + CR.format(f"Figure from the lecture slides (Castelucci, UC08 Anatomy); {ref}")

def ak(key, src, flags, bloco, alvo, evid, motivo, **kw):
    return dict(key=key, kind="text", src=src, flags=flags, bloco=bloco, alvo=alvo, evid=evid, uso=kw.pop("uso", "Step 1; cirurgia abdominal."), motivo=motivo, **kw)

CARDS = [
 # ---------- TRONCOS E TERRITÓRIOS ----------
 ak("nivel-celiaco", 1486766393958, {1: 3}, "A-troncos", "Tronco celíaco em T12/L1", "Slides 2, 11 (T12)", "Verde: nível de referência."),
 ak("nivel-ams", 1486767143966, {1: 3}, "A-troncos", "AMS em L1", "Slides 2, 11 (T12/L1)", "Verde."),
 ak("nivel-ami", 1486767150807, {1: 3}, "A-troncos", "AMI em L3", "Slides 2, 11 (L3; slide 18 escreve L4)", "Verde.",
    correcao="Slide 18 rotula L4; slides 2/11 e AnKing dizem L3 — mantido L3 (Q027), divergência registrada."),
 ak("celiaco-anterior", 1486767159823, {1: 3}, "A-troncos", "Celíaco → intestino anterior", "Slides 2–3; questão 1", "Verde (1-HighYield)."),
 ak("ams-medio", 1486767163689, {1: 3}, "A-troncos", "AMS → intestino médio", "Slides 11–12; questões 2, 7; roteiro 13 (área de irrigação)", "Verde."),
 ak("ami-posterior", 1486767179344, {1: 3}, "A-troncos", "AMI → intestino posterior", "Slides 18–20; questão 3", "Verde."),
 # ---------- TRONCO CELÍACO ----------
 ak("ramos-celiaco", 1486767263733, {1: 3, 2: 3, 3: 3}, "B-celiaco", "Três ramos do tronco celíaco", "Slide 3; questão 1; roteiro 11", "Verde: núcleo da aula."),
 ak("hepatica-comum", 1486767276770, {1: 3, 2: 3}, "B-celiaco", "Hepática comum → própria + gastroduodenal", "Slides 3, 5; roteiro 11–12", "Verde."),
 ak("gastrica-direita", 1486767287058, {1: 4, 2: 3}, "B-celiaco", "Hepática própria → gástrica direita", "Slide 3; roteiro 12", "c2 (direita) verde; c1 azul."),
 ak("gastroduodenal-gastromental", 1486767295417, {1: 4, 2: 4}, "B-celiaco", "Gastroduodenal → gastromental direita", "Slide 6", "Azul."),
 ak("gastroduodenal-pd", 1486767304293, {1: 3}, "B-celiaco", "Gastroduodenal → pancreaticoduodenais superiores", "Slides 4, 6; questão 9", "Verde (1-HighYield)."),
 ak("esplenica-ramos", 1486767314237, {1: 3, 2: 3, 3: 4}, "B-celiaco", "Esplênica → gastromental esquerda e gástricas curtas", "Slides 4, 6; roteiro 12", "c1/c2 verdes; c3 azul."),
 ak("gastrica-esq-esofago", 1486767268255, {1: 4}, "B-celiaco", "Gástrica esquerda → ramos esofágicos", "Slide 3", "Azul."),
 ak("curvatura-menor", 1486767367274, {1: 3}, "B-celiaco", "Curvatura menor ← gástricas", "Slides 3–4 (irrigação do estômago); objetivo 4", "Verde."),
 ak("curvatura-maior", 1486767364212, {1: 3}, "B-celiaco", "Curvatura maior ← gastromentais", "Slide 6; roteiro 12", "Verde."),
 ak("fundo-curtas", 1486767395683, {1: 4}, "B-celiaco", "Fundo ← gástricas curtas", "Slide 4", "Azul."),
 ak("anastomose-gastromentais", 1486767349883, {1: 3}, "B-celiaco", "Gastromental esquerda ↔ direita", "Roteiro 12 ('anastomosa-se com a gastromental direita')", "Verde."),
 ak("anastomose-gastricas", 1486767352903, {1: 4}, "B-celiaco", "Gástrica esquerda ↔ direita", "Slides 3–4", "Azul."),
 ak("id-esplenica", 1486767327881, {1: 4}, "B-celiaco", "ID esplênica", "Roteiro 11–12", "Azul: identificação."),
 ak("id-gastromental-dir", 1486767330571, {1: 4}, "B-celiaco", "ID gastromental direita", "Slide 6", "Azul."),
 ak("id-gastromental-esq", 1486767323251, {1: 4}, "B-celiaco", "ID gastromental esquerda", "Slide 6", "Azul."),
 ak("id-gastrica-dir", 1486767335503, {1: 4}, "B-celiaco", "ID gástrica direita", "Slide 3", "Azul."),
 ak("id-gastrica-esq", 1486767333068, {1: 4}, "B-celiaco", "ID gástrica esquerda", "Slides 3, 5", "Azul."),
 ak("id-hepatica-comum", 1486767337959, {1: 4}, "B-celiaco", "ID hepática comum", "Slides 3, 5", "Azul."),
 ak("id-gastroduodenal", 1486767341284, {1: 4}, "B-celiaco", "ID gastroduodenal", "Slides 3, 5–6", "Azul."),
 ak("id-curtas", 1486767346792, {1: 4}, "B-celiaco", "ID gástricas curtas", "Slide 4", "Azul."),
 dict(key="celiaco-dope", kind="dope", src=1349477488376, labels={2: 4, 5: 4}, bloco="B-celiaco",
  alvo="Tronco celíaco e hepática própria na prancha Netter", evid="Slides 3, 5; roteiro 11", uso="Prática.", motivo="Azul.",
  curadoria="Só rótulos 2a (tronco celíaco) e 5a (hepática própria), ausentes dos ID AnKing; demais rótulos já cobertos."),
 dict(key="pd-inferior", kind="text", src=1461962581720, origin="Dope", flags={1: 4}, bloco="B-celiaco",
  text='The inferior pancreaticoduodenal artery arises from the {{c1::SMA}}',
  extra='It anastomoses with the superior pancreaticoduodenal arteries (from the gastroduodenal artery), linking the celiac and SMA territories around the head of the pancreas.',
  alvo="Pancreaticoduodenal inferior da AMS", evid="Slides 6, 11 ('1º ramo da AMS')", uso="Colaterais celíaco–AMS.", motivo="Azul.",
  didatico="Extra: arcada pancreaticoduodenal."),
 # ---------- AMS E AMI ----------
 dict(key="ams-colicas", kind="autoral", flags={1: 3, 2: 3, 3: 3}, bloco="C-mesentericas",
  text=('Colic branches of the SMA: the {{c1::ileocolic}} artery supplies the terminal ileum, cecum and appendix; the {{c2::right colic}} artery, the ascending colon; '
        'and the {{c3::middle colic}} artery, the transverse colon'),
  extra='The SMA also gives the inferior pancreaticoduodenal, jejunal and ileal arteries.<br><br>' + SLIDE("nebli-uc08-an07-s12-ams.jpeg", "Netter, 3rd ed.", 360),
  alvo="Ramos cólicos da AMS e territórios", evid="Slide 12; roteiro 13; questões 2, 5, 10", uso="Colectomias; isquemia.",
  motivo="Verde: território de cada ramo é o núcleo das questões 2/5.", busca="AnKing sem card de ramos cólicos (só cirurgia/ileocólica em ressecção); Dope 1349477488369 identifica sem território; lacuna real."),
 dict(key="ami-ramos", kind="autoral", flags={1: 3, 2: 3, 3: 3}, bloco="C-mesentericas",
  text=('Branches of the IMA: the {{c1::left colic}} artery supplies the descending colon, the {{c2::sigmoid}} arteries the sigmoid colon, '
        'and the {{c3::superior rectal}} artery continues it to the rectum'),
  extra=SLIDE("nebli-uc08-an07-s18-ami.jpeg", "Netter, 3rd ed.", 360),
  alvo="Ramos da AMI", evid="Slides 18–20; roteiro 14; questão 3; caso slide 23 (vólvulo: cite os ramos da AMI)", uso="Colectomias; vólvulo.",
  motivo="Verde.", busca="AnKing só superior retal (1486771346144); Dope identifica; lacuna de território."),
 dict(key="mesentericas-dope", kind="dope", src=1349477488369, labels={2: 4, 4: 3, 5: 4, 6: 4, 7: 4, 9: 4, 10: 4, 11: 4}, bloco="C-mesentericas",
  alvo="Ramos da AMS/AMI e arcada marginal na prancha Netter", evid="Slides 12, 18–20; roteiro 13–14", uso="Prática.",
  motivo="Arcada marginal verde (única fonte de recuperação dela); demais azuis (texto verde nos autorais).",
  curadoria="Rótulos 1a (AMS), 3a (vasos retos, na AN01), 8a (retal superior, em card próprio) e 12a (jejunais/ileais) desativados."),
 ak("retal-superior", 1486771346144, {1: 3}, "C-mesentericas", "Retal superior ← AMI", "Slides 20, 22; roteiro 14", "Verde."),
 ak("retal-inferior", 1486771374861, {1: 3}, "D-reto", "Retal inferior ← pudenda interna", "Slide 22; questão 6", "Verde."),
 dict(key="retal-media", kind="autoral", flags={1: 3}, bloco="D-reto",
  text='The middle rectal artery arises from the {{c1::internal iliac}} artery',
  extra='Rectum: superior rectal (IMA), middle rectal (internal iliac) and inferior rectal (internal pudendal). The veins follow the same pattern: superior rectal → inferior mesenteric (portal); middle and inferior → systemic.<br><br>' + SLIDE("nebli-uc08-an07-s22-reto.jpeg", "Netter, 3rd ed.", 340),
  alvo="Retal média ← ilíaca interna", evid="Slide 22; questões 6, 8", uso="Hemorroidas; cirurgia retal.", motivo="Verde: completa a tríade.",
  busca="AnKing/Dope/Dorian sem card da retal média (Dope 1349477488443 só a veia); lacuna real."),
 # ---------- VEIAS ----------
 dict(key="porta-formacao", kind="autoral", flags={1: 3, 2: 4}, bloco="E-veias",
  text=('The portal vein forms behind the neck of the pancreas from the {{c1::superior mesenteric}} and splenic veins; '
        'the inferior mesenteric vein usually drains into the {{c2::splenic}} vein'),
  extra=('The portal system drains from the lower esophagus to the upper anal canal, plus spleen, pancreas and gallbladder. The veins follow the arteries.<br><br>'
         + SLIDE("nebli-uc08-an07-s08-porta.jpeg", "Netter, 3rd ed.", 380)),
  alvo="Formação e território da veia porta", evid="Slides 7–8, 14, 21; roteiro 'Sistema veia porta'; questões 4–6, 12", uso="Hipertensão portal; metástases hepáticas.",
  motivo="c1 verde; c2 azul.", busca="AnKing só varizes/trombose esplênica; Dope 1349477488443 identifica tributárias; lacuna de formação."),
 dict(key="porta-dope", kind="dope", src=1349477488443, labels={3: 4, 4: 4, 10: 4, 12: 4, 13: 4, 14: 4}, bloco="E-veias",
  alvo="Porta e tributárias na prancha Netter", evid="Slides 7–8, 14, 21", uso="Prática.", motivo="Azul.",
  curadoria="Rótulos 3a, 4a, 10a, 12a, 13a, 14a; demais (paraumbilicais, cólicas, retais média/inferior, esofágicas) desativados."),
 # ---------- LINFÁTICOS ----------
 dict(key="cisterna", kind="autoral", flags={1: 3}, bloco="F-linfa",
  text='The intestinal and lumbar lymphatic trunks drain into the {{c1::cisterna chyli}}, the dilated origin of the thoracic duct at about L1–L2',
  extra=('The thoracic duct carries lymph and chyle to the junction of the left subclavian and internal jugular veins. The preaortic nodes (celiac, superior and inferior mesenteric) lie along the arteries of the same names.<br><br>'
         + SLIDE("nebli-uc08-an07-s09-cisterna.jpeg", "Moore", 300)),
  alvo="Cisterna do quilo e ducto torácico", evid="Slides 9, 14–15 (cisterna L2–L3, troncos intestinal e lombares)", uso="Quilotórax; absorção de lipídios.",
  motivo="Verde.", correcao="Slide escreve L2–L3; Moore/Netter L1–L2 — verso usa 'about L1–L2' e o conflito fica registrado.",
  busca="AnKing só ducto torácico em efusões/quilomícrons; lacuna."),
 ak("quilomicron-ducto", 1482115579210, {1: 4}, "F-linfa", "Quilomícrons chegam ao sangue pelo ducto torácico", "Slides 9, 15", "Azul."),
 ak("linfa-estomago", 1486945231564, {1: 3}, "F-linfa", "Celíacos drenam estômago, baço, fígado, pâncreas", "Slides 10, 14", "Verde (1-HighYield)."),
 ak("linfa-duodeno-alto", 1486945235222, {1: 4}, "F-linfa", "Celíacos drenam duodeno superior", "Slides 10, 14", "Azul."),
 ak("linfa-duodeno-baixo", 1486945239368, {1: 4}, "F-linfa", "Mesentéricos superiores drenam duodeno inferior", "Slide 14", "Azul."),
 ak("linfa-jejuno-ileo", 1486945243332, {1: 3}, "F-linfa", "Mesentéricos superiores drenam jejuno e íleo", "Slides 14–15; questão 4", "Verde."),
 ak("linfa-colon-proximal", 1486945247167, {1: 3}, "F-linfa", "Mesentéricos superiores até a flexura esquerda", "Slide 21; questão 5", "Verde."),
 ak("linfa-colon-distal", 1486945252224, {1: 3}, "F-linfa", "Mesentéricos inferiores: flexura esquerda → reto superior", "Slides 21, 23; questões 5–6", "Verde."),
 # ---------- CLÍNICA ----------
 ak("isquemia-ams", 1482289647560, {1: 3, 2: 4}, "G-clinica", "Isquemia mesentérica aguda por oclusão da AMS", "Caso clínico slides 16–17 ('oclusão da AMS')", "c1 verde (HY); c2 azul.", uso="Clínica direta (Q044)."),
 ak("isquemia-dor", 1482289654584, {1: 4}, "G-clinica", "Dor desproporcional ao exame", "Caso slides 16–17", "Azul."),
 ak("griffiths", 1482886714520, {1: 3, 2: 4}, "G-clinica", "Flexura esquerda: divisor de águas AMS/AMI", "Slides 19–20 (arcada marginal); pista de Davi", "c1 verde (HY); c2 azul.", uso="Colite isquêmica."),
 ak("sudeck", 1520726446562, {1: 4, 2: 4}, "G-clinica", "Ponto de Sudeck (retossigmoide)", "Slides 20, 22", "Azul."),
]

COMPARTILHADOS = {
    1790329086048: "UC03 Patologia · varizes esofágicas: gástrica esquerda ↔ ázigo (AnKing 1486770898373) — slide 7; cores atuais mantidas",
    1790707317210: "AN01 · jejuno: poucas arcadas e vasos retos longos — slide 13 (diferenças jejuno × íleo)",
    1790707317610: "AN01 · prancha de arcadas jejunais/ileais — slides 12–13",
    1790707317312: "AN01 · gordura mesentérica do íleo — slide 13",
    1790707315687: "AN01 · síndrome da AMS (3ª porção do duodeno) — slide 12 (localização da AMS)",
    1790707996585: "AN02 · reto acima da pectinada: a. retal superior — slide 22",
    1790707996686: "AN02 · reto abaixo da pectinada: a. retal inferior — slide 22",
    1790707997011: "AN02 · acima: drenagem portal — slide 22; questão 8",
    1790707997108: "AN02 · abaixo: drenagem sistêmica — slide 22; questão 8",
    1790707996809: "AN02 · acima: linfonodos ilíacos internos — slide 23",
    1790707996912: "AN02 · abaixo: inguinais superficiais — slide 23",
}

EXCLUIDOS = [
 (1556932244893, "Embolização na AMS — redundante com 1482289647560"),
 (1487470289670, "Regiões vulneráveis (flexura esquerda, retossigmoide) — redundante com Griffiths + Sudeck"),
 (1482289661873, "Isquemia mesentérica crônica — clínica além do caso"),
 (1486771299461, "Varizes anorretais — já ligadas pela drenagem portal/sistêmica da AN02"),
 (1527682823473, "Dorian cabeça do pâncreas pelas pancreaticoduodenais — coberto por PD superior + inferior"),
 (1486767190930, "Nível da gonadal — fora da aula"),
]
FORA_DO_RECORTE = [
 "Vasos renais/gonadais e ramos parietais da aorta: fora da aula",
 "Componentes gerais do sistema linfático (slide 8): contexto; cisterna/ducto e grupos pré-aórticos cobertos",
 "Isquemia–reperfusão e estrangulamento (slide 17): ilustração do caso",
]
