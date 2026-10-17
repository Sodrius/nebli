# Especificação curada — Declaração de óbito: conceitos gerais (UC03 P1, Patologia; 20 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing não tem as regras da DO brasileira → autoral só para elas (lacuna provada, busca/cobertura.tsv); os elos das cadeias causais
# dos casos (lâminas 7–16) entram por AnKing ou cópias NEBLI vivas (Edema e congestão, Correlação 2, UC08).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing)
    "_FirstAid_06_Public_Health_04_Healthcare_Delivery_06_Common_causes_of_death_US_by_age.txt",
]
AUTORAL_EXCECAO = ("Aula de regras da Declaração de Óbito brasileira (SIM, quem assina, SVO/IML, Partes I e II, causa básica, modos de morrer, "
                   "morte metatraumática): nenhum card em AnKing, MCAT ou NEBLI vivo (busca/anking.txt: death certificate/underlying cause "
                   "só em 'cause of death' de doenças; busca/semantica.jsonl); os elos dos casos entram por AnKing e cópias NEBLI")
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt14-20261017a"
SHORT = "pt14n"
LESSON = "2026-uc03-patologia-14-declaracao-obito"
DECK = "NEBLI::UC03::P1::Patologia::Declaração de óbito"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"pt14-{n}.png": f"img/pt14-{n}.png" for n in ("parte-i", "caso1")}
IMG = lambda n, w=460: f'<img src="pt14-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (causas de morte por idade, morte súbita, mortalidade; busca/secoes); palavra-chave "
         "em AnKing e Referências Externas (busca/anking.txt: death certificate, underlying cause, autopsy, medical examiner, fetal death, "
         "cardiac arrest, multiple organ failure); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1489981061376, "seção Common causes of death (US): ranking dos EUA (<1 ano), diferente do brasileiro; a aula não dá ranking de causas"),
 (1489981065383, "seção Common causes of death (US): ranking dos EUA (1–44 anos); no Brasil predominam causas externas; a aula não dá ranking"),
 (1489981070253, "seção Common causes of death (US): ranking dos EUA (45–64 anos: câncer); no Brasil, doenças circulatórias; fora da aula"),
 (1489981076139, "seção Common causes of death (US): ranking dos EUA (>65 anos); a aula não dá ranking de causas"),
 (1471914969111, "IC esquerda → edema pulmonar: entra a cópia NEBLI da aula Edema e congestão (sh-1791169086563)"),
 (1482203756188, "varizes por hipertensão portal: entra a cópia NEBLI da Correlação 2 (sh-1791022175126)"),
 (1482203769705, "rotura de varizes → hematêmese: entra a cópia NEBLI da Correlação 2 (sh-1791022175254)"),
 (1403046909909, "Chagas: megacólon, megaesôfago, cardiomiopatia: entra a cópia NEBLI da UC08 (sh-1790972065836)"),
 (1482289603147, "volvo do sigmoide no idoso: entra a cópia NEBLI da UC08 (sh-1790974691357)"),
]
FORA_DO_RECORTE = [
 "Ranking de causas de morte (EUA ou Brasil): a aula fala do uso estatístico da DO, não do ranking.",
 "Campos administrativos da DO (vias, cartório, CID, codificação da causa básica): Manual da DO, sem cobrança.",
 "Morte encefálica, diretivas antecipadas e doação de órgãos: outras aulas.",
]
A_, B_, C_, D_ = "A-documento", "B-quem-assina", "C-preenchimento", "D-casos"

CARDS = [
 # ---------- A. O documento (lâminas 2–3) ----------
 au("au-sim", "The <b>death certificate</b> (Declaração de Óbito) is the base document of Brazil's {{c1::Mortality Information System}}",
    "A-aula", A_, "DO é a base do SIM", 2, "lâmina 2; Manual da DO; monitoria",
    extra="- It is also the basis for the legal death record (certidão), mortality statistics and epidemiological surveillance<br>- Mortality statistics are tabulated by the underlying cause"),
 au("au-quando", "A <b>fetal death</b> requires a death certificate from {{c1::20 weeks}} of gestation or 500 g",
    "A-aula", A_, "Quando emitir a DO", 3, "lâmina 3; Manual da DO (quando não emitir); monitoria",
    extra="- Any child who dies after a live birth needs one, whatever the weight or gestational age<br>"
          "- Adults: natural or violent deaths alike"),
 # ---------- B. Quem assina (lâminas 4–5, 18–19) ----------
 au("au-natural", "A <b>natural death</b> without medical care, or without a known cause, is certified by the {{c1::SVO}} (death verification service)",
    "A-aula", B_, "Morte natural sem assistência → SVO", 4, "lâminas 4 e 19 (PS sem diagnóstico prévio); monitoria; prova 2016 P1 5.3 (autópsia e DO)",
    extra="- With medical care, the attending or on-duty physician signs<br>- A DO does not require an autopsy<br>"
          "- In a natural death, also record the absence of signs of violence (field 59)"),
 au("au-violenta", "In a <b>violent death</b> (external causes), the death certificate is signed by the {{c1::forensic physician}} of the IML",
    "A-aula", B_, "Morte violenta → IML", 5, "lâmina 5; Manual da DO; monitoria",
    extra="- Where there is no IML, by a physician appointed by the judge or police<br>- External causes: homicide, suicide, accident, suspicious death"),
 # ---------- C. Preenchimento (lâminas 6, 8, 17, 19) ----------
 au("au-parte-i", "In <b>Part I</b>, the last filled line holds the {{c1::underlying cause}}, the disease that started the chain",
    "V-prova", C_, "Parte I: causa básica na última linha", 6, "lâmina 6; provas 2016 P2 2.12 e 2019 P1 1.12; Manual da DO",
    extra="- Line a is the immediate cause; each line is due to the one below<br>- Write the time from onset to death on each line<br>" + IMG("parte-i")),
 au("au-parte-ii", "Conditions that contributed to death without being in the causal chain go in {{c1::Part II}} of the <b>death certificate</b>",
    "V-prova", C_, "Parte II: condições contribuintes", 8, "lâminas 6, 8, 10, 12, 14 e 16; prova 2019 P1 1.12",
    extra="- Example: prostate cancer in the hypertensive patient who died of acute pulmonary edema<br>" + IMG("caso1")),
 au("au-erros", "<b>Cardiorespiratory arrest</b> and multiple organ failure should not be written as causes, because they are {{c1::modes of dying}}",
    "V-pilar", C_, "Modos de morrer não são causa", 17, "lâmina 17; monitoria; casos 2 e 3 (PCR verificada, não declarada)",
    extra="- Every death ends in arrest; the DO must name the disease behind it"),
 au("au-metatraumatica", "A <b>death after trauma</b>, even from later pneumonia, is still a {{c1::violent}} death that goes to the IML",
    "A-aula", C_, "Morte metatraumática", 19, "lâmina 19 (queda → fratura de fêmur → broncopneumonia)",
    extra="- The underlying cause is the circumstance of the injury (the fall)"),
 # ---------- D. Elos das cadeias causais dos casos (lâminas 7–16) ----------
 ak("ak-has-icfep", 1579474089606, "A-aula", D_, "Hipertensão crônica → insuficiência cardíaca", 7, "caso 1 (hipertensão → cardiopatia → ICC)"),
 sh(1791169086563, "azul", D_, "IC esquerda → edema pulmonar", 7, "caso 1 (edema agudo de pulmão, causa imediata); card de Edema e congestão"),
 ak("ak-schisto-portal", 1510016604369, "A-aula", D_, "S. mansoni → hipertensão portal", 9, "caso 2 (esquistossomose, causa básica)"),
 sh(1791022175126, "azul", D_, "Hipertensão portal → varizes de esôfago", 9, "caso 2; card da Correlação 2"),
 sh(1791022175254, "azul", D_, "Rotura de varizes → hematêmese", 9, "caso 2; card da Correlação 2"),
 sh(1791022175426, "azul", D_, "Varizes: causa comum de morte no cirrótico", 9, "caso 2; card da Correlação 2"),
 ak("ak-choque-hipovolemico", 1472161014695, "A-aula", D_, "Hemorragia → choque hipovolêmico", 9, "casos 2 e 5 (choque, causa imediata)"),
 sh(1790972065836, "azul", D_, "Chagas: megacólon, megaesôfago e cardiomiopatia", 11, "caso 3 (megacólon chagásico; cardiopatia na Parte II); card da UC08"),
 sh(1790974691357, "azul", D_, "Volvo do sigmoide", 11, "caso 3; card da UC08"),
 ak("ak-sepse-intestino", 1500573565493, "A-aula", D_, "Ruptura da parede intestinal → sepse por Gram-negativos", 11, "caso 3 (peritonite → choque séptico)"),
 ak("ak-corona-sdra", 1516242261236, "A-aula", D_, "Coronavírus pode levar à SDRA", 13, "caso 4 (SDRA ← COVID-19)"),
 ak("ak-sdra", 1473707363543, "A-step", D_, "SDRA: insuficiência respiratória aguda com opacidades bilaterais", 14, "caso 4 (causa imediata)"),
 ak("ak-aaa-rotura", 1471824920983, "A-aula", D_, "Aneurisma de aorta > 5 cm rompe", 15, "caso 5 (aneurisma de 10 cm)"),
 ak("ak-aaa-triade", 1471824932558, "A-step", D_, "Rotura do aneurisma: hipotensão, massa pulsátil, dor", 15, "caso 5"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "regra ou elo causal sem estrutura a reconhecer; as figuras que ensinam (formulário da Parte I, caso 1 preenchido) estão nos cards do conceito"
SLIDE_SEM_ALT = "formulário oficial da DO mostrado na aula, sem equivalente nos acervos"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pt14-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "ak-has-icfep": "- In case 1: hypertension (underlying cause) → hypertensive cardiopathy → heart failure → acute pulmonary edema",
 "ak-schisto-portal": "- In case 2, schistosomiasis is the underlying cause, on the last line",
 "ak-choque-hipovolemico": "- Shock is the immediate cause (line a); the disease that bled goes below",
 "ak-sepse-intestino": "- In case 3: Chagas megacolon → sigmoid volvulus → acute peritonitis → septic shock",
 "ak-corona-sdra": "- In case 4: ARDS (line a) due to COVID-19; diabetes goes in Part II",
 "ak-sdra": "- Respiratory failure itself is a mode of dying; name ARDS and its cause",
 "ak-aaa-rotura": "- In case 5, COVID-19 had no role in the rupture, so it goes in Part II",
 "ak-aaa-triade": "- Rupture causes hemorrhage and hypovolemic shock within minutes",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "pt14-parte-i.png": "Lâmina 6: Parte I da DO com as linhas a (imediata), b–c (intermediárias), d (básica) e o texto da Parte II; verso de au-parte-i.",
 "pt14-caso1.png": "Lâmina 8: DO do caso 1 preenchida (edema agudo ← ICC ← cardiopatia ← hipertensão; câncer de próstata na Parte II, com tempos); verso de au-parte-ii.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Saber para que serve a DO, quando emiti-la, quem a assina (assistente, SVO, IML) e como preencher a Parte I (cadeia causal até a "
             "causa básica) e a Parte II, evitando modos de morrer como causa.",
 "centrais": [
   ("documento", "au-sim"),
   ("quem assina", "au-natural", "au-violenta"),
   ("preenchimento", "au-parte-i", "au-parte-ii", "au-erros"),
 ],
 "exemplos": ["caso 1 hipertensão", "caso 2 esquistossomose", "caso 3 Chagas", "caso 4 COVID-19", "caso 5 aneurisma", "queda com fratura"],
 "outras_aulas": [("edema pulmonar da IC", "Edema e congestão (sh)"), ("varizes de esôfago", "Correlação 2 (sh)"), ("Chagas e volvo", "UC08 (sh)"),
                  ("autópsia", "03 Diagnóstico patológico")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
