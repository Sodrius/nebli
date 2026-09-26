"""Plano do piloto E1 + cards de Edema e congestão (Claude, 25/09/2026).

Gera plan.json. Não escreve no Anki. Textos finais, origem, objetivo, cor e motivo
ficam aqui para a revisão; apply.py só executa o que o plano diz.
"""
import hashlib, json
from pathlib import Path
from anki import call

ROOT = Path(__file__).resolve().parent
LESSON = "2026-uc03-patologia-23-edema-congestao"
DECK = "NEBLI::UC03::P2::Patologia::Edema e congestão"
V3 = "NEBLI AnKing independente - v3"
SLIDE = ('<br><span style="font-size: 10pt;"><i>Imagem: slide da aula Edema e Congestão '
         '(Prof. Luiz Fernando Ferraz da Silva, FMUSP UC03).</i></span>')

def img(name, width=500):
    return f'<img src="{name}" width="{width}">'

def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

# Mídia do slide que vai para a coleção (origem local → nome na coleção)
MEDIA = {
    "midia/slide-p03-img3.png": "nebli_edema_hiperemia_conjuntival.png",
    "midia/slide-p06-img2.png": "nebli_edema_hidrotorax_autopsia.png",
    "midia/slide-p06-img3.png": "nebli_edema_hidropericardio_autopsia.png",
    "midia/slide-p08-fluxo.png": "nebli_edema_ic_sraa.png",
    "midia/slide-p09-img2.png": "nebli_edema_pulmonar_he.png",
    "midia/slide-p10-fluxo.png": "nebli_edema_nefrotica_fluxo.png",
    "midia/slide-p11-fluxo.png": "nebli_edema_cirrose_ascite_fluxo.png",
    "midia/slide-p12-img4.png": "nebli_edema_nozmoscada_macro.png",
    "midia/slide-p12-img5.png": "nebli_edema_nozmoscada_micro.png",
    "midia/slide-p13-fluxo.png": "nebli_edema_sdra_fluxo.png",
    "midia/slide-p15-img3.png": "nebli_edema_membrana_hialina.png",
}
M = {v.split("nebli_edema_")[1].rsplit(".", 1)[0]: v for v in MEDIA.values()}

# action: create (nota nova) | update (cópia NEBLI existente, mesma contagem de clozes)
#         | recreate (cópia existente cuja contagem de clozes muda: apagar e criar)
E = []
def add(key, objective, origin, source_nid, action, text, extra, flag, motive, existing_nid=None):
    E.append(dict(key=key, objective=objective, origin=origin, source_nid=source_nid, action=action,
                  existing_nid=existing_nid, fields={"Text": text, "Extra": extra}, flag=flag, motive=motive))

# ---------- B. Forças de Starling e linfa ----------
add("linfa-retorna", "B-starling", "AnKing", 1471466870844, "create",
    '<div>The <i>excess</i> fluid filtered out of the capillaries is <b>returned to the circulation</b> via {{c1::lymph}}</div>',
    'Lymph also returns filtered protein, which keeps interstitial oncotic pressure low.<br><br>'
    '<div><img alt="Lymphatic capillaries in tissue spaces" src="e6418f212ae9e4f73c75b14bffef168c.webp" width="600"></div>'
    '<i><span style="font-size: 10pt;">Photo credit: <a href="https://openstax.org/books/anatomy-and-physiology-2e/pages/21-1-anatomy-of-the-lymphatic-and-immune-systems">OpenStax</a>, '
    '<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></span></i>',
    3, "Base de todo o capítulo: sem o papel da linfa não se explica edema, linfedema nem edema pulmonar.")
add("limiar-edema", "B-starling", "AnKing", 1471466881536, "recreate",
    '<div><b>Capillary fluid transudation</b> results in <u>clinically apparent edema</u> when the {{c1::fluid outflow (net plasma filtration)}} has risen sufficiently to overwhelm the resorptive capacity of tissue lymphatics</div>',
    'Lymph flow can rise several-fold before fluid accumulates (edema safety margin); edema appears when filtration exceeds that reserve or when lymphatics are blocked.<br><br>'
    'In most tissues there is little sustained reabsorption at the venous end: lymph returns most of the filtrate (revised Starling principle).',
    3, "Define o limiar do edema; transferível a todo órgão.", existing_nid=1790264436914)

# ---------- C. Cinco mecanismos (causa → mecanismo, como a prova cobra) ----------
add("mec-hidrostatica", "C-mecanismos", "AnKing", 1471466884199, "update",
    '<div><b>Heart failure</b> and <b>venous obstruction</b> (e.g., DVT) cause edema by increasing capillary {{c1::hydrostatic pressure}}</div>',
    'Venous obstruction → local edema (one limb); heart failure → generalized, dependent edema. The fluid is a protein-poor <b>transudate</b>.<br>'
    '<span style="font-size: 10pt;">PT: pressão hidrostática aumentada.</span>',
    3, "Mecanismo mais cobrado nas provas (edema pulmonar pós-IAM, derrame por IC).", existing_nid=1790264437008)
add("mec-oncotica", "C-mecanismos", "AnKing", 1471466893190, "update",
    '<div><b>Nephrotic syndrome</b>, <b>liver failure</b> and <b>protein malnutrition</b> cause edema by decreasing plasma {{c1::oncotic pressure}}</div>',
    'Albumin, the main source of plasma oncotic pressure, is lost in urine (nephrotic syndrome) or not synthesized in adequate amounts (liver failure, severe protein malnutrition). Edema is generalized; the fluid is a transudate.<br>'
    '<span style="font-size: 10pt;">PT: pressão oncótica (coloidosmótica) reduzida.</span>',
    3, "Segundo mecanismo central; reaparece em rim, fígado e nutrição.", existing_nid=1790264437101)
add("mec-permeabilidade", "C-mecanismos", "AnKing", 1471466900946, "update",
    '<div><b>Inflammation</b>, <b>burns</b> and <b>toxins</b> cause edema by increasing vascular {{c1::permeability}}</div>',
    'Endothelial gaps (histamine, bradykinin, leukotrienes) or direct endothelial injury let proteins and cells escape → protein- and cell-rich <b>exudate</b> (vs. the transudate of hydrostatic/oncotic edema).',
    3, "Único mecanismo que gera exsudato inflamatório; eixo de várias questões de prova.", existing_nid=1790264437196)
add("mec-linfatico", "C-mecanismos", "AnKing", 1521170206006, "update",
    '<div><b>Tumor invasion</b>, <b>lymph node dissection/radiation</b> and <b>filariasis</b> cause edema by {{c1::lymphatic obstruction}}</div>',
    '- Protein-rich interstitial fluid accumulates slowly<br>- Starts as pitting edema → progresses to <b>non-pitting</b> edema with firm, thickened skin (fibrosis)<br>'
    '- Localized to the obstructed drainage territory (e.g., one limb)<br><br>'
    '<div><img alt="Lower limb lymphedema" src="9756547cec1b9cf4476f5d2d6ef05076.png" width="420"></div>',
    3, "Terceiro termo da equação; explica linfedema e ascite/quilotórax.", existing_nid=1790264438478)
add("mec-sodio", "C-mecanismos", "AnKing", 1521169448163, "update",
    '<b>Renal failure</b> causes edema through primary retention of {{c1::sodium}} and {{c1::water}}',
    'The expanded intravascular volume raises capillary hydrostatic pressure <i>and</i> dilutes plasma proteins (↓ oncotic pressure).<br>'
    'Contrast: in heart failure and cirrhosis, Na⁺ retention is <i>secondary</i> to a low effective circulating volume.',
    3, "Fecha os cinco mecanismos; distingue retenção primária de secundária.", existing_nid=1790264438391)

# ---------- E. Formas específicas: insuficiência cardíaca ----------
add("ic-sraa", "E-ic", "AnKing", 1471914992993, "create",
    '<div><b>Left heart failure</b> causes <u>decreased forward perfusion</u> to the kidneys, resulting in activation of the {{c1::renin-angiotensin}} system</div>',
    '↓ stroke volume → ↓ renal perfusion → renin → angiotensin II/aldosterone → Na⁺/H₂O retention → ↑ venous and capillary pressure → more edema (vicious cycle).<br><br>'
    + img(M["ic_sraa"], 520) + SLIDE,
    3, "Ciclo vicioso da IC (slide 8); base da cardiologia e da farmacologia futura.")
add("ic-esquerda", "E-ic", "AnKing", 1471914938644, "recreate",
    '<div>Clinical features of <b>left heart failure</b> are due to decreased <u>forward perfusion</u> with consequent <b>{{c1::pulmonary}} congestion</b></div>',
    'Blood backs up behind the failing left ventricle into the pulmonary veins and capillaries → pulmonary congestion and edema.',
    3, "Localiza o órgão congesto pela câmara que falha.", existing_nid=1790264437298)
add("ic-direita", "E-ic", "AnKing", 1471914999950, "update",
    '<div>Clinical features of <b>right heart failure</b> are due to {{c1::systemic}} congestion</div>',
    'Backup into the systemic veins: jugular distension, congested liver, dependent peripheral edema and, with time, ascites. The most common cause of right heart failure is left heart failure.',
    3, "Par da IC esquerda; explica fígado em noz-moscada e edema periférico.", existing_nid=1790264437452)
add("ic-cacifo", "F-morfologia", "AnKing", 1471915101703, "create",
    '<div><b>Heart failure</b> may present with <i>dependent</i> {{c1::pitting edema}} due to <u>increased</u> hydrostatic pressure</div>',
    'Dependent = follows gravity (ankles when upright, sacrum when bedridden). Pitting = low-protein fluid is displaced by finger pressure.<br>'
    'Contrast: periorbital edema in renal disease; firm, non-pitting edema in chronic lymphedema.<br>'
    '<span style="font-size: 10pt;">PT: sinal do cacifo (godet).</span>',
    3, "Correspondente macroscópico do edema hidrostático; sinal de exame físico de uso permanente.")
add("ic-celulas", "F-morfologia", "AnKing", 1471914979068, "create",
    '<div><b>Chronic left heart failure</b> may present with {{c1::<b>hemosiderin-laden macrophages</b>}}, known as <b>heart failure cells</b>, in the <u>lungs</u></div>',
    '- Small, congested capillaries burst → intra-alveolar hemorrhage → red cells phagocytosed by alveolar macrophages<br>'
    '- Hemosiderin: coarse <b>brown</b> pigment (Prussian blue positive); with septal fibrosis → "brown induration" of the lung<br><br>'
    '<img src="75921df3bc8f4b27de6c4fd56b9b8879.jpg" width="520"><div><span style="font-size: 10pt;"><em>Photo credit: '
    '<a href="https://commons.wikimedia.org/wiki/File:Pulmonary_haemorrhage_-_high_mag.jpg">Nephron</a>, '
    '<a href="https://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a>, via Wikimedia Commons</em></span></div>',
    3, "Marca microscópica da congestão pulmonar crônica; reaparece em patologia pulmonar e cardíaca.")
add("nozmoscada", "F-morfologia", "AnKing", 1471915035278, "create",
    '<div>Chronic passive congestion from <b>right heart failure</b> gives the liver a {{c1::<b>nutmeg</b>}} pattern: dark, congested {{c2::<b>centrilobular</b>}} areas alternating with paler parenchyma</div>',
    'Blood backs up from the IVC → hepatic veins → central veins. Centrilobular (zone 3) hepatocytes, the last to receive oxygenated blood, undergo hypoxic atrophy/necrosis; periportal cells may show fatty change. Long-standing congestion → centrilobular fibrosis.<br><br>'
    + img(M["nozmoscada_macro"], 380) + " " + img(M["nozmoscada_micro"], 420) + SLIDE +
    '<br><span style="font-size: 10pt;">PT: fígado em noz-moscada; congestão centrolobular.</span>',
    3, "Macro e micro da congestão hepática (objetivo 4); o princípio da zona 3 vale para isquemia e toxinas.")

# ---------- E. Edema pulmonar e SDRA ----------
add("pulm-cardio-vs-nao", "E-pulmao", "AnKing", 1532735591750, "update",
    '<div>{{c1::Cardiogenic::Cardiogenic/Non-cardiogenic}} pulmonary edema = due to ↑ pulmonary <u>hydrostatic</u> pressure</div><br><div>{{c1::Non-cardiogenic::Cardiogenic/Non-cardiogenic}} pulmonary edema = due to ↑ pulmonary <u>capillary permeability</u></div>',
    'Cardiogenic (left heart failure): intact barrier, high capillary pressure → protein-poor transudate.<br>'
    'Non-cardiogenic (e.g., ARDS): injured alveolar-capillary barrier, normal capillary pressure → protein-rich exudate (in ARDS, with hyaline membranes).',
    3, "Distinção cobrada em prova (IAM × choque séptico); decide conduta na clínica.", existing_nid=1790264438575)
add("pulm-histologia", "F-morfologia", "Autoral", None, "create",
    img(M["pulmonar_he"], 480) + '<br>Lung (H&amp;E): the homogeneous pale-pink material filling these alveoli is {{c1::edema fluid}}',
    'Pulmonary edema: protein-poor fluid with few cells; septal capillaries congested (red). Macro: heavy, wet lungs with frothy fluid in the airways.<br>'
    'Contrast: diffuse alveolar damage adds <b>hyaline membranes</b> lining alveolar walls; pneumonia fills alveoli with neutrophils.' + SLIDE,
    3, "Reconhecimento microscópico pedido no objetivo 4; nenhum card AnKing/externo testa a imagem do edema pulmonar.")
add("sdra-interface", "E-pulmao", "AnKing", 1473707286558, "create",
    '<b>ARDS</b> is caused by <u>diffuse alveolar damage</u> with impairment of the {{c1::<b>alveolar-capillary</b>}} <b>interface</b>',
    'The interface is formed by <b>type I pneumocytes</b> and <b>capillary endothelial cells</b>; its injury lets plasma proteins flood the alveoli (non-cardiogenic edema).',
    3, "Define a lesão-alvo da SDRA; base para o edema de permeabilidade.")
add("sdra-hialina", "F-morfologia", "AnKing", 1473707313998, "create",
    '<div>In <b>acute respiratory distress syndrome </b>(ARDS), leakage of <i>protein-rich fluid</i> leads to formation of <u>intra-alveolar</u> {{c1::<b>hyaline</b>}}<b> membranes</b></div><br>'
    + img(M["membrana_hialina"], 360),
    'Membranes = <b>fibrin</b> + protein-rich edema fluid + remnants of necrotic epithelial cells, lining the alveolar walls (pink bands in the image). Absent in purely cardiogenic edema.' + SLIDE,
    3, "Assinatura morfológica do edema de permeabilidade no pulmão; imagem da aula na frente para reconhecimento.")
add("sdra-neutrofilos", "E-pulmao", "AnKing", 1473707401320, "create",
    '<div>In <b>ARDS</b>, <u>activation</u> of {{c1::<b>neutrophils</b>}} by proinflammatory <b>cytokines</b> induces free radical and protease-mediated damage of both type I and II pneumocytes</div>',
    'Injury → alveolar macrophages release TNF, IL-8, IL-1 → neutrophil recruitment/activation → PAF, leukotrienes, proteases, ROS → endothelial and pneumocyte injury → ↑ permeability, plasma leak, hyaline membranes.<br><br>'
    + img(M["sdra_fluxo"], 620) + SLIDE,
    4, "Detalhe da cadeia (célula efetora); reconstruível pelo que se sabe de inflamação aguda.")
add("sdra-fibrose", "E-pulmao", "AnKing", 1473707419762, "create",
    '<div>Recovery of <b>ARDS</b> may be complicated by {{c1::interstitial fibrosis/scarring}} due to <u>loss</u> of <b>type II pneumocytes</b></div>',
    'Repair instead of regeneration: activated fibroblasts deposit procollagen (left branch of the lesson\'s ARDS scheme).',
    4, "Desfecho mostrado no esquema do slide; menor custo de esquecer que o mecanismo central.")

# ---------- E. Nefrótica e cirrose ----------
add("nefrotica-sodio", "E-rim-figado", "AnKing", 1475363769043, "recreate",
    '<div><b>Nephrotic edema</b> results from low plasma oncotic pressure plus renal {{c1::sodium retention}}</div>',
    'Proteinuria → hypoalbuminemia (↓ oncotic pressure) and, within the nephron, ↑ tubular Na⁺ reabsorption (<i>primary</i> retention, "overfill"). A low effective volume can add RAAS-driven <i>secondary</i> retention ("underfill"). Periorbital edema is typical (loose tissue).<br><br>'
    + img(M["nefrotica_fluxo"], 560) + SLIDE,
    3, "Esquema do slide 10: o edema nefrótico não é só albumina baixa; explica resistência a diurético.", existing_nid=1790264437931)
add("cirrose-ascite", "E-rim-figado", "AnKing", 1581191946613, "create",
    '<b>Ascites</b> and <b>hepatorenal syndrome</b> (2° to cirrhosis) are caused by {{c1::<b>splanchnic arterial</b>}} <b>dilation</b> due to <u>increased</u> release of {{c1::<b>nitric oxide</b> (NO)}}',
    'Portal hypertension → splanchnic vasodilation (NO) → ↓ effective circulating volume → RAAS, sympathetic tone, ADH →<br>'
    '(1) renal Na⁺/water avidity → <b>ascites</b> (fluid leaks where sinusoidal/splanchnic pressure is high and albumin is low)<br>'
    '(2) intense renal vasoconstriction → <b>hepatorenal syndrome</b> (functional; kidneys structurally normal)<br><br>'
    + img(M["cirrose_ascite_fluxo"], 520) + SLIDE,
    3, "Esquema do slide 11; o paradoxo do volume efetivo baixo com sobrecarga de água é reutilizado na clínica.")

# ---------- A. Definições ----------
add("hiperemia-congestao", "A-definicoes", "Autoral", None, "create",
    'Arteriolar dilation (e.g., red conjunctiva) causes {{c1::hyperemia}}; impaired venous outflow (e.g., failing heart) causes {{c1::congestion}}',
    '<b>Hyperemia</b>: active, ↑ inflow of oxygenated blood → bright red (exercise, inflammation).<br>'
    '<b>Congestion</b>: passive, deoxygenated blood pools → dusky/cyanotic; chronic congestion → hypoxia, microhemorrhage, hemosiderin, fibrosis.<br><br>'
    + img(M["hiperemia_conjuntival"], 420) + SLIDE +
    '<br><span style="font-size: 10pt;">PT: hiperemia (ativa) × congestão (passiva).</span>',
    3, "Objetivo 1 do slide; nenhum card AnKing/externo define o par patológico (só a hiperemia funcional da fisiologia).")
add("anasarca", "A-definicoes", "Autoral", None, "create",
    'Severe, generalized edema of the subcutaneous tissue (e.g., advanced nephrotic syndrome) is called {{c1::anasarca}}',
    'Collections are named by cavity: pleura → <b>hydrothorax</b>; pericardium → <b>hydropericardium</b>; peritoneum → <b>ascites</b> (hydroperitoneum). The names say where the fluid is, not why.<br><br>'
    + img(M["hidrotorax_autopsia"], 300) + " " + img(M["hidropericardio_autopsia"], 300) + SLIDE +
    '<br><span style="font-size: 10pt;">PT: anasarca; hidrotórax; hidropericárdio; ascite.</span>',
    4, "Objetivo 2 (terminologia); nome, não mecanismo — menor custo de esquecer.")

ASSOCIATE = [dict(nid=1790253536913, cards=[1790253536913, 1790253536914], objective="D-transudato-exsudato", flag=3,
                  motive="Transudato × exsudato é a pergunta mais recorrente das provas de edema; nota da Inflamação aguda, mesma identidade.")]

# Cópias antigas (Codex, 24/09) que saem: autorais em PT redundantes e AnKing sem ganho
REMOVE_REASONS = {
    1790264437571: "IC direita → edema periférico: já coberto por ic-direita + ic-cacifo",
    1790264437753: "Derrame transudativo por ↑ hidrostática: coberto por mec-hidrostatica + nota exsudato/transudato",
    1790264437836: "Derrame transudativo por ↓ oncótica: coberto por mec-oncotica + nota exsudato/transudato",
    1790264438140: "IRA → retenção de Na/H2O com HAS/IC: repete mec-sodio com clínica lateral",
    1790264438689: "Congestão hepática passiva = IC direita: coberto por nozmoscada",
}

def main():
    deck_notes = sorted({c["note"] for c in call("cardsInfo", cards=call("findCards", query=f'"deck:{DECK}"'))})
    info = {n["noteId"]: n for n in call("notesInfo", notes=deck_notes)}
    keep_existing = {e["existing_nid"] for e in E if e["existing_nid"] and e["action"] == "update"}
    recreate = {e["existing_nid"] for e in E if e["action"] == "recreate"}
    remove = []
    for nid, n in info.items():
        if nid in keep_existing: continue
        other = [t for t in n["tags"] if t.startswith("NEBLI::2026") and LESSON not in t]
        if other: raise SystemExit(f"nota {nid} associada a outra aula: {other}")
        if nid in recreate: reason = "recriada com nova contagem de clozes (mesma origem, sem histórico: reps=0)"
        elif nid in REMOVE_REASONS: reason = REMOVE_REASONS[nid]
        elif "NEBLI::origem::Autoral" in n["tags"]: reason = "autoral antigo em PT: alvo coberto por AnKing ou autoral novo em inglês"
        else: raise SystemExit(f"nota {nid} sem decisão")
        remove.append(dict(nid=nid, cards=n["cards"], reason=reason, text=n["fields"]["Text"]["value"]))
    for e in E:
        if e["source_nid"]:
            src = call("notesInfo", notes=[e["source_nid"]])[0]
            e["source_model"] = src["modelName"]; e["source_fields_hash"] = digest({k: v["value"] for k, v in src["fields"].items()})
            e["source_tags"] = src["tags"]
        e["expected_cards"] = len({m for m in __import__("re").findall(r"{{c(\d+)::", e["fields"]["Text"])})
    plan = dict(lesson_id=LESSON, target_deck=DECK, profile=call("getActiveProfile"), media=MEDIA, entries=E,
                associate=ASSOCIATE, remove=remove,
                totals=dict(notes=len(E), cards=sum(e["expected_cards"] for e in E),
                            authored=sum(e["origin"] == "Autoral" for e in E),
                            green=sum(e["expected_cards"] for e in E if e["flag"] == 3) + sum(len(a["cards"]) for a in ASSOCIATE if a["flag"] == 3),
                            blue=sum(e["expected_cards"] for e in E if e["flag"] == 4),
                            removed_notes=len(remove), removed_cards=sum(len(r["cards"]) for r in remove)))
    (ROOT / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(plan["totals"], ensure_ascii=False))
    for r in remove: print("REMOVE", r["nid"], len(r["cards"]), r["reason"][:70])

if __name__ == "__main__":
    main()
