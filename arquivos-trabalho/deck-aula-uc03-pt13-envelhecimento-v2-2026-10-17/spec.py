# Especificação curada — Envelhecimento celular e tecidual (UC03 P1, Patologia; 22 lâminas).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing (seções FirstAid Telomerase, Respiratory changes in the elderly, Presbyopia, Presbycusis, Normal aging, Changes in the elderly)
# → cards da 09 e da 11 por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing)
    "_FirstAid_01_Biochem_01_Molecular_06_DNA_replication_10_Telomerase.txt",
    "_FirstAid_16_Respiratory_03_Physiology_Respiratory_System_Changes_in_the_Elderly.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_05_Ophthalmology_04_Lens_disorders_01_Presbyopia.txt",
    "_FirstAid_12_Neurology_and_Special_Senses_04_Otology_04_Common_causes_of_hearing_loss_02_Presbycusis.txt",
    "_FirstAid_07_Cardiovascular_04_Pathology_28_Cardiomyopathies_Normal_Aging.txt",
    "_FirstAid_13_Psych_01_Psychology_Changes_in_the_Elderly.txt",
]
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt13-20261017a"
SHORT = "pt13n"
LESSON = "2026-uc03-patologia-13-envelhecimento"
DECK = "NEBLI::UC03::P1::Patologia::Envelhecimento celular e tecidual"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {f"pt13-{n}.png": f"img/pt13-{n}.png" for n in ("reserva", "telomeros", "werner")}
IMG = lambda n, w=440: f'<img src="pt13-{n}.png" width="{w}">'
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid telomerase, mudanças no idoso, presbiopia, presbiacusia, envelhecimento "
         "normal do coração; busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt: telomere, senescence, Werner, "
         "sirtuin, aging, elderly, lipofuscin, chaperone, wrinkles, osteopenia); significado em todos os acervos e NEBLI vivo (busca/semantica.jsonl). ")
# Vagas da 11 (ainda não instalada): ao instalar a 11, preencher com os nids das cópias NEBLI de 1486590985316 e 1486590997246.
PT11 = {"LIPO": 1792240581792, "LIPO_LOCAIS": 1792240582292}
EXCLUIDOS = [
 (1467771917029, "seção Telomerase: repete ak-telomerase-rt (telomerase é transcriptase reversa)"),
 (1489891684955, "seção Changes in the elderly: suicídio no idoso — psicologia do idoso, UC16 Ciclos da vida; fora das lâminas"),
 (1489977102023, "seção Changes in the elderly: libido no idoso — UC16 Ciclos da vida; fora das lâminas"),
 (1486590985316, "lipofuscina do envelhecimento: card da aula 11 — entra a cópia NEBLI dela (vaga PT11)"),
 (1486590997246, "lipofuscina por peroxidação lipídica: card da aula 11 — entra a cópia NEBLI dela (vaga PT11)"),
 (1487470244885, "radicais livres lesam lipídios, DNA e proteínas — entra a cópia NEBLI da 09 (sh-1792117369568)"),
 (1495595300874, "ubiquitinação recruta o proteassomo: card da aula 11"),
 (1522105602652, "Bloom e envelhecimento precoce: a aula usa Werner; Bloom é síndrome de instabilidade cromossômica de outra aula"),
 (1520906706487, "função renal cai com a idade: repete ak-tfg-idade"),
 (1554353457143, "MCAT: telômeros 'ricos em GC' — impreciso; ak-ttaggg já cobre a sequência"),
 (1722600715295, "MCAT: telômeros TTAGGG — repete ak-ttaggg"),
 (1468101687731, "células permanentes 'senescentes' em G0: outro sentido de senescência (ciclo celular, aula 11)"),
]
FORA_DO_RECORTE = [
 "Psicologia do idoso (suicídio, libido, sono): UC16 Ciclos da vida.",
 "Farmacologia geriátrica (critérios de Beers, benzodiazepínicos, anticolinérgicos): aula de farmacologia; aqui só a TFG para a dose.",
 "Detalhe molecular da telomerase e do reparo do DNA: Biologia Molecular; câncer e marcas do câncer: P4.",
 "Espirometria (Tiffeneau, DPOC) e curvas do fumante: só no verso; a fisiologia respiratória é do 2º ano.",
]
A_, B_, C_ = "A-conceitos", "B-mecanismos", "C-sistemas"

CARDS = [
 # ---------- A. Conceitos (lâminas 2–3, 16) ----------
 au("au-senescencia", "Natural loss of reserve with age is {{c1::senescence}}, while disease-driven change in the <b>elderly</b> is {{c1::senility}}",
    "V-prova", A_, "Senescência × senilidade", 2, "lâmina 2; prova 2024 P1 1.3 (perda óssea × osteoporose com fratura); cruzadas 6 e 11",
    extra="- Bone loss within the expected range is senescence; osteoporosis with a fracture is senility<br>"
          "- Alzheimer disease (lâmina 16) is senility: protein accumulation and atrophy beyond normal aging"),
 au("au-reserva", "<b>Aging</b> keeps basal organ function but shrinks the {{c1::functional reserve}}, the extra capacity used under stress",
    "V-prova", A_, "Reserva funcional", 3, "lâminas 2–3; provas 2018 P1 2.4, 2016 P1 3.5 e 2015 P1sub 3.6; cruzadas 17",
    extra="- Reserve = maximal − basal function; it peaks around 35–40 years<br>"
          "- So the same pneumonia, COVID or renally cleared drug hurts the elderly more<br>" + IMG("reserva", 420)),
 # ---------- B. Mecanismos (lâminas 4–11) ----------
 au("au-replicativa", "Each <b>somatic cell</b> division shortens the telomeres until the cell stops dividing, called replicative {{c1::senescence}}",
    "V-pilar", B_, "Senescência replicativa", 6, "lâminas 5–6; Robbins (encurtamento → resposta a DNA quebrado); cruzadas 3, 6 e 15",
    extra="- Short telomeres are read as broken DNA, which arrests the cell cycle<br>"
          "- Slower cell replacement explains slower healing in the elderly<br>" + IMG("telomeros", 460)),
 ak("ak-ttaggg", 1467771904154, "V-hy", B_, "Telomerase adiciona TTAGGG", 6, "lâmina 6 (telomerase com molde de RNA); prova 2016 P3 2.5; seção FirstAid"),
 ak("ak-telomerase-rt", 1467771911742, "A-step", B_, "Telomerase é transcriptase reversa", 6, "lâmina 6 (molde de RNA); seção FirstAid"),
 ak("ak-telomerase-cancer", 1467771922095, "V-prova", B_, "Telomerase aumentada no câncer", 6, "lâmina 6 (células cancerosas); provas 2016 P3 2.5 e 2017 P4 4.1"),
 ak("ak-cancer-telomerase2", 1496163026982, "R-detalhe", B_, "Câncer expressa telomerase para não encurtar", 6, "transcrição (imortalidade replicativa)"),
 ak("ak-hayflick", 1496164030007, "A-aula", B_, "Potencial replicativo ilimitado (limite de Hayflick)", 6, "transcrição; prova 2017 P4 4.1 (replicação permanente)"),
 ak("ak-progeria", 1467771924957, "R-detalhe", B_, "Telomerase baixa: envelhecimento precoce", 6, "seção FirstAid"),
 sh(1792117369568, "azul", B_, "Radicais livres lesam lipídios, DNA e proteínas", 8, "lâminas 7–8; prova 2018 P1 2.4 (estresse oxidativo); card da 09"),
 au("au-proteostase", "With age, falling {{c1::chaperone}} and proteasome activity lets damaged <b>proteins</b> accumulate",
    "A-aula", B_, "Perda da homeostase proteica", 9, "lâmina 9; transcrição (chaperonas e ubiquitina funcionam pior); Robbins (declínio do proteassomo)",
    extra="- Misfolded proteins that persist impair function and can trigger apoptosis"),
 ak("ak-chaperona", 1468090181130, "A-step", B_, "Chaperonas mantêm o dobramento", 9, "lâmina 9; transcrição"),
 ak("ak-proteassomo-danificada", 1468101821842, "A-step", B_, "Proteassomo degrada proteínas danificadas", 9, "lâmina 9; transcrição"),
 sh(1792117372320, "azul", B_, "Proteína mal dobrada leva à apoptose", 9, "lâmina 9; card da 09"),
 au("au-sirtuinas", "<b>Caloric restriction</b> extends lifespan in animal models, an effect attributed to {{c1::sirtuins}}",
    "A-aula", B_, "Restrição calórica e sirtuínas", 10, "lâmina 10; cruzadas 4; bibliografia (Guarente 2011); Robbins",
    extra="- Sirtuins are NAD-dependent deacetylases that favor DNA repair and protein folding<br>"
          "- Lower insulin/IGF-1 signaling also extends lifespan in animal models"),
 au("au-werner", "<b>Werner syndrome</b> causes premature aging through a defective DNA {{c1::helicase}}, so DNA damage accumulates",
    "A-aula", B_, "Síndrome de Werner", 11, "lâmina 11; cruzadas 10; Robbins (WRN = DNA helicase; a transcrição diz histona desacetilase, corrigido)",
    extra="- Patients look elderly in their 30s–40s<br>" + IMG("werner", 360)),
 # ---------- C. Sistemas (lâminas 12–20) ----------
 ak("ak-massa-gordura", 1489891751592, "A-aula", C_, "Idoso: menos músculo, mais gordura", 12, "lâmina 12 (aumento de peso); seção FirstAid"),
 ak("ak-rugas", 1468531927104, "V-hy", C_, "Rugas: menos colágeno e elastina", 12, "lâmina 12 (elasticidade cutânea); cruzadas 12"),
 ak("ak-rugas-colageno", 1520277707475, "A-step", C_, "Rugas: menos síntese e mais ligação cruzada do colágeno", 12, "lâmina 12"),
 au("au-turgor", "<b>Elderly skin</b> loses turgor because fibroblasts make fewer {{c1::proteoglycans}}, so the matrix holds less water",
    "V-prova", C_, "Turgor cutâneo do idoso", 12, "lâmina 12; transcrição; prova 2019 P1 1.3 (turgor); cruzadas 14",
    extra="- Hydration does not depend on how much water the person drinks"),
 ak("ak-presbiopia", 1484603491110, "A-aula", C_, "Presbiopia: acomodação prejudicada", 12, "lâmina 12; seção FirstAid"),
 ak("ak-presbiopia-cristalino", 1484603493725, "A-aula", C_, "Presbiopia: cristalino menos elástico", 12, "lâmina 12; seção FirstAid"),
 ak("ak-presbiopia-oculos", 1484603496614, "R-detalhe", C_, "Presbiopia: óculos de leitura", 12, "seção FirstAid"),
 ak("ak-presbiopia-miopia", 1523242877135, "R-detalhe", C_, "Presbiopia melhora miopia leve", 12, "seção FirstAid"),
 ak("ak-presbiacusia-def", 1480908640856, "A-aula", C_, "Presbiacusia = perda auditiva da idade", 12, "lâmina 12; seção FirstAid"),
 ak("ak-presbiacusia", 1480908643571, "V-hy", C_, "Presbiacusia: neurossensorial, frequências altas", 12, "lâmina 12; seção FirstAid"),
 ak("ak-presbiacusia-base", 1480908647128, "A-step", C_, "Presbiacusia: perda de células ciliadas da base", 12, "transcrição (órgão de Corti); seção FirstAid"),
 ak("ak-pulm-complacencia", 1473359822159, "V-hy", C_, "Pulmão do idoso: complacência aumentada", 13, "lâmina 13 (menos elasticidade)"),
 ak("ak-parede-complacencia", 1523413845819, "V-hy", C_, "Parede torácica do idoso: complacência menor", 13, "lâmina 13 (expansibilidade); seção FirstAid"),
 ak("ak-musculo-resp", 1523414068153, "A-aula", C_, "Músculos respiratórios mais fracos", 13, "lâmina 13; transcrição; seção FirstAid"),
 ak("ak-vr", 1523413928710, "V-hy", C_, "Volume residual aumentado", 13, "lâmina 13 (volume residual); seção FirstAid"),
 ak("ak-cpt", 1523414001523, "A-step", C_, "CPT não muda", 13, "seção FirstAid"),
 ak("ak-vq", 1523414014382, "A-step", C_, "Envelhecimento causa desequilíbrio V/Q", 13, "seção FirstAid"),
 ak("ak-aa", 1523414047330, "A-step", C_, "Gradiente A-a aumenta", 13, "seção FirstAid"),
 ak("ak-cvf", 1523413975946, "V-hy", C_, "CVF diminui", 14, "lâmina 14 (curvas de CVF); seção FirstAid"),
 ak("ak-vef1", 1523413989466, "V-prova", C_, "VEF1 diminui", 14, "lâmina 14; provas 2019 P1 1.3 e 2015 P1sub 3.6; seção FirstAid"),
 ak("ak-inteligencia", 1489891767721, "A-aula", C_, "Inteligência não muda no idoso", 15, "lâmina 15; monitoria (perdas sem afetar a cognição); seção FirstAid"),
 ak("ak-arterias", 1470850169002, "V-hy", C_, "Artérias mais rígidas", 17, "lâmina 17 (rigidez da parede vascular)"),
 ak("ak-arterias-elastina", 1567733403700, "A-aula", C_, "Parede arterial: menos elastina, mais colágeno e cálcio", 17, "lâmina 17; monitoria"),
 ak("ak-has-sistolica", 1520902682537, "A-step", C_, "Hipertensão sistólica isolada do idoso", 17, "lâmina 17"),
 ak("ak-ea-calcificacao", 1472058775498, "A-aula", C_, "Estenose aórtica por calcificação degenerativa", 17, "lâmina 17 (espessamento valvar); monitoria (colágeno nas valvas)"),
 ak("ak-septo-sigmoide", 1520906439066, "R-detalhe", C_, "Septo sigmoide no coração idoso", 17, "seção FirstAid"),
 au("au-tfg", "Without kidney disease, the <b>glomerular filtration rate</b> of a 90-year-old falls to about {{c1::half}} the young adult value",
    "V-prova", C_, "TFG cai à metade", 18, "lâmina 18 (gráfico da TFG); provas 2017 P1 1.5, 2019 P1 1.3 e 2016 P1 3.5; cruzadas 1",
    extra="- Renal blood flow falls about 1% per year after 50<br>- The aged kidney also concentrates urine poorly, so dehydration comes fast on hot days<br>"
          "- A young kidney donor recovers by compensatory hyperplasia; an elderly donor does poorly"),
 ak("ak-tfg-idade", 1575660680597, "A-step", C_, "TFG cai com a idade: ajustar dose", 18, "lâmina 18; cruzadas 16 (dose menor)"),
 au("au-creatinina", "Serum <b>creatinine</b> can be low in the elderly because {{c1::muscle mass}} falls, despite a lower GFR",
    "V-prova", C_, "Creatinina baixa no idoso", 19, "lâmina 19 (até 50% menos fibras musculares); prova 2023 P1 1.8",
    extra="- Creatinine comes from muscle and is excreted only by the kidney"),
 ak("ak-pico-osso", 1488154106594, "A-aula", C_, "Pico de massa óssea aos 30 anos", 19, "lâmina 19 (osteopenia)"),
 ak("ak-perda-osso", 1488154119895, "A-aula", C_, "Perda óssea < 1% ao ano após os 30", 19, "lâmina 19"),
 ak("ak-artrose", 1488247856555, "A-step", C_, "Artrose: desgaste da cartilagem", 19, "lâmina 19 (cartilagem menos hidratada → degeneração articular)"),
]
_PT11 = [("LIPO", "azul", C_, "Lipofuscina: pigmento do desgaste no envelhecimento", 20, "lâmina 20 (miocárdio); cruzadas 7; card da 11"),
         ("LIPO_LOCAIS", "azul", C_, "Lipofuscina: peroxidação lipídica; coração e fígado do idoso", 20, "lâmina 20 e transcrição; card da 11")]
for _k, _c, _b, _a, _s, _m in _PT11:
    if PT11[_k]:
        CARDS.append(sh(PT11[_k], _c, _b, _a, _s, _m))

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "fato sem estrutura a reconhecer; as figuras que ensinam (curva da reserva, telômeros, Werner) estão nos cards do conceito"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Robbins/Banks), sem equivalente nos acervos para o conceito"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pt13-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "ak-ttaggg": "- Telomerase is highest in germ cells, low in stem cells and absent in most somatic cells",
 "ak-telomerase-rt": "- It carries its own RNA template",
 "ak-telomerase-cancer": "- It lets cancer cells escape replicative senescence",
 "ak-cancer-telomerase2": "- Replicative immortality, not resistance to injury",
 "ak-hayflick": "- Normal somatic cells stop after a fixed number of divisions",
 "ak-progeria": "- Werner syndrome, the lesson's example, is a DNA helicase defect",
 "ak-chaperona": "- With age chaperones work worse, so misfolded proteins accumulate",
 "ak-proteassomo-danificada": "- Proteasome activity declines with age",
 "ak-massa-gordura": "- Also: height falls about 1 cm per decade (dehydrated discs), less body water, hair loss",
 "ak-rugas": "- Fibroblasts of the elderly make less matrix",
 "ak-rugas-colageno": "- Elastic fibers fragment with age",
 "ak-presbiopia": "- Listed among the general changes of aging",
 "ak-presbiopia-cristalino": "- Receptors and structures wear out and are not replaced",
 "ak-presbiopia-oculos": "- Reading glasses magnify near objects",
 "ak-presbiopia-miopia": "- Loss of accommodation offsets mild myopia",
 "ak-presbiacusia-def": "- Listed among the general changes of aging",
 "ak-presbiacusia": "- High frequencies go first",
 "ak-presbiacusia-base": "- The cochlear base encodes high frequencies",
 "ak-pulm-complacencia": "- Loss of elastic recoil",
 "ak-parede-complacencia": "- Weaker muscles and a stiffer chest wall reduce chest expansion",
 "ak-musculo-resp": "- Cough reflex and mucociliary clearance also decline, so infections are more common",
 "ak-vr": "- Air trapping from lower elastic recoil",
 "ak-cpt": "- Higher lung compliance offsets the stiffer chest wall",
 "ak-vq": "- Small airways close earlier",
 "ak-aa": "- Because of the V/Q mismatch",
 "ak-cvf": "- FVC falls faster than FEV1 in normal aging",
 "ak-vef1": "- Smoking speeds the decline; quitting restores the normal slope but not the lost function",
 "ak-inteligencia": "- Normal brain aging loses neurons, weight and conduction speed without necessarily impairing cognition",
 "ak-arterias": "- Elastic fibers fragment and collagen accumulates",
 "ak-arterias-elastina": "- The aged heart and vessels adapt poorly to sudden demand",
 "ak-has-sistolica": "- Stiff arteries raise systolic pressure and pulse pressure",
 "ak-ea-calcificacao": "- Valve thickening is senescence; calcific stenosis with symptoms is senility",
 "ak-septo-sigmoide": "- Part of normal cardiac aging",
 "ak-tfg-idade": "- Renally cleared drugs need lower doses in the elderly",
 "ak-pico-osso": "- Bone loss within the expected range is senescence (osteopenia)",
 "ak-perda-osso": "- Physical activity slows bone loss",
 "ak-artrose": "- Less hydrated cartilage gets thinner, raising friction",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-proteostase": "ganho: a queda com a idade da atividade das chaperonas e do proteassomo; ak-chaperona e ak-proteassomo-danificada só dizem o que eles fazem", "au-tfg": "ganho: a magnitude (metade aos 90) e a TFG normal para a idade da prova 2017; ak-tfg-idade só diz que a TFG cai"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {
 "pt13-reserva.png": "Lâmina 3: curva de função orgânica (máximo × basal) pela idade, reserva funcional marcada, pico aos 40 (Banks 2003); verso de au-reserva.",
 "pt13-telomeros.png": "Lâmina 6: comprimento do telômero × divisões (germinativas, tronco, normal, câncer) e telomerase com molde de RNA (Robbins); verso de au-replicativa.",
 "pt13-werner.png": "Lâmina 11: paciente com síndrome de Werner aos 15 e aos 48 anos; verso de au-werner.",
}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (46 notas novas, 52 cards; frentes, clozes, versos, imagens e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Distinguir senescência de senilidade, entender a perda de reserva funcional e os mecanismos do envelhecimento celular "
             "(telômeros, dano ao DNA, homeostase proteica, sensores de nutrientes) e reconhecer as alterações por sistema.",
 "centrais": [
   ("conceitos", "au-senescencia"),
   ("reserva funcional", "au-reserva", "au-tfg", "au-creatinina"),
   ("senescência replicativa", "au-replicativa", "ak-hayflick"),
   ("mecanismos moleculares", "au-proteostase"),
   ("prova: telomerase e câncer", "ak-telomerase-cancer"),
   ("prova: função pulmonar", "ak-vef1"),
   ("prova: pele", "au-turgor"),
 ],
 "exemplos": ["Werner (fotos)", "Alzheimer", "VEF1 em fumantes", "doação de rim", "COVID no idoso"],
 "outras_aulas": [("radicais livres, proteínas mal dobradas", "09 Lesão celular (sh)"), ("lipofuscina", "11 Acúmulos (sh)"),
                  ("psicologia e farmacologia do idoso", "UC16 Ciclos da vida"), ("telomerase molecular", "Biologia Molecular")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
