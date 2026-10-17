# Especificação curada — Adaptação celular e acúmulos (UC03 P1, Patologia; 60 lâminas, partes I e II).
# Gerada a partir de inventario.py (escrito antes). Ordem = lâminas.
# AnKing → cópias NEBLI vivas (19, 24, 23, 03, 09, GR2, UC08) por sh() → autoral SÓ para lacuna provada (busca/cobertura.tsv).
import pathlib as _pl, re as _re, sys as _sys
HERE = _pl.Path(__file__).parent
_sys.path.insert(0, str(HERE.parents[1]))
from nebli.spec_lib import ak, au, sh, ORG, finalizar  # todos os irmãos, cor pela rubrica, dica de 1ª letra, busca por autoral

PIPELINE_VERSAO = 4
SECOES_DA_AULA = [  # F-20261016-CLAUDE-06 (só notas do baralho AnKing)
    "_FirstAid_Pathology_Cellular_adaptations.txt",
    "_FirstAid_Pathology_Cellular_adaptations_Hypertrophy.txt",
    "_FirstAid_Pathology_Cellular_adaptations_Hyperplasia.txt",
    "_FirstAid_Pathology_Cellular_adaptations_Atrophy.txt",
    "_FirstAid_Pathology_Cellular_adaptations_Metaplasia.txt",
    "_FirstAid_Pathology_Calcification_Metastatic.txt",
    "_FirstAid_Pathology_Calcification_Dystrophic.txt",
    "_FirstAid_Pathology_Lipofuscin.txt",
]
AUTORAL_EXCECAO = ""
PIPELINE = "anking-primeiro"
RUN_ID = "uc03-pt11-20261017a"
SHORT = "pt11n"
LESSON = "2026-uc03-patologia-11-acumulos-adaptacao"
DECK = "NEBLI::UC03::P1::Patologia::Acúmulos e adaptação celular"
CRITERIOS = "MEMORY.md §3/§5/§6/§7/§8 + FEEDBACKS até F-20261016-CLAUDE-11 + ANTI-EXEMPLARES §1–16, 17/10/2026"
MEDIA = {}
BUSCA = ("Três caminhos (17/10): seções de recurso do AnKing (FirstAid adaptações, calcificação, lipofuscina, hemocromatose, esteatose, "
         "glicogenoses; busca/secoes); palavra-chave em AnKing e Referências Externas (busca/anking.txt); significado em todos os acervos e "
         "NEBLI vivo (busca/semantica.jsonl). ")
EXCLUIDOS = [
 (1487461041752, "seção atrofia: atrofia por menos células via apoptose — entra a cópia NEBLI da 09 (sh-1792117383096)"),
 (1487461089160, "seção metaplasia: metaplasia apócrina da mama sem risco — patologia mamária, fora da aula"),
 (1471914979068, "células de insuficiência cardíaca — entra a cópia NEBLI da 23 (sh-1791142466364)"),
 (1488680325485, "tirosina precursora da melanina — repete ak-tirosinase"),
 (1474253821570, "Pompe: o professor diz que não é preciso saber a tabela de glicogenoses; fica só o exemplo de von Gierke"),
 (1474253907723, "McArdle: idem (tabela de glicogenoses dispensada)"),
 (1520440331083, "displasia: não é dada nesta aula (aula de neoplasia)"),
 (1481857721803, "composição da placa neurítica: repete ak-alzheimer-ab"),
]
FORA_DO_RECORTE = [
 "Esquema de lesão celular (lâmina 2): aula 09.",
 "Tabela de glicogenoses (lâmina 48): o professor dispensa; só o exemplo de von Gierke.",
 "Displasia e neoplasia: aulas de carcinogênese (a aula só diz que hiperplasia e metaplasia são terreno fértil).",
 "Metemoglobina e carboxiemoglobina (quadro da lâmina 59): o professor diz que não vem ao caso.",
]
A_, B_, C_, D_, E_, F_, G_, H_ = ("A-tecidos-adaptacao", "B-hipertrofia", "C-hiperplasia", "D-atrofia-hipoplasia", "E-metaplasia",
                                  "F-lipides-proteinas", "G-calcificacao", "H-pigmentos")

CARDS = [
 # ---------- A. Tecidos e adaptação (lâminas 3–5) ----------
 ak("ak-labeis", 1487981487576, "A-aula", A_, "Tecidos lábeis: células-tronco em ciclo contínuo", 3, "lâmina 3; monitoria (lábeis, estáveis, permanentes)"),
 ak("ak-estaveis", 1487981494590, "A-aula", A_, "Tecidos estáveis: voltam ao ciclo quando preciso", 3, "lâminas 3 e 16 (fígado em G0 regenera)"),
 ak("ak-permanentes", 1487460268378, "V-pilar", A_, "Tecidos permanentes só hipertrofiam", 3, "lâminas 3, 8 e 17 (onde não ocorre hiperplasia); seção FirstAid"),
 ak("ak-hipertrofia-def", 1487460256729, "V-pilar", A_, "Hipertrofia = células maiores", 5, "lâminas 5–6; seção FirstAid"),
 ak("ak-hiperplasia-def", 1487458829921, "V-pilar", A_, "Hiperplasia = mais células", 5, "lâminas 5 e 17; seção FirstAid"),
 ak("ak-atrofia-def", 1487460276914, "V-pilar", A_, "Atrofia = menos massa por células menores ou menos células", 5, "lâminas 5 e 20; seção FirstAid"),
 ak("ak-metaplasia-def", 1487461060183, "V-pilar", A_, "Metaplasia = troca de um tipo celular por outro", 5, "lâminas 5 e 28; seção FirstAid"),
 # ---------- B. Hipertrofia (lâminas 6–14) ----------
 ak("ak-hipertrofia-genes", 1487460262238, "A-step", B_, "Hipertrofia: ativação gênica, síntese proteica e organelas", 6, "lâminas 6–7 e transcrição (útero gravídico, filamentos contráteis)"),
 au("au-hipertrofia-gatilhos", "Mechanical {{c1::stretch}} and α-adrenergic agonists trigger cardiac <b>hypertrophy</b> through transcription factors",
    "V-prova", B_, "Gatilhos da hipertrofia cardíaca", 10, "lâminas 10–11; provas 2018 P1 1.4 e 2016 P1 3.2 (estiramento, α-adrenérgicos); bibliografia (Cacciapuoti 2011)",
    extra="- Angiotensin II, endothelin-1 and growth factors (IGF-1) add to the signal<br>- Past its limit, the hypertrophied heart dilates and fails"),
 au("au-hipertrofia-fetal", "Hypertrophied <b>cardiomyocytes</b> re-express fetal genes such as β-myosin heavy chain and atrial {{c1::natriuretic}} factor",
    "V-prova", B_, "Genes fetais na hipertrofia", 13, "lâminas 12–13; prova 2018 P1 1.4 (sinalizações da adaptação cardíaca)",
    extra="- β-myosin has lower ATPase activity, so contraction is slower but more economical<br>- ANF is diuretic and lowers the hemodynamic load"),
 sh(1791983686733, "rosa", B_, "Remodelamento da via aérea na asma", 14, "lâmina 14 (hipertrofia do músculo liso brônquico); card da 62"),
 # ---------- C. Hiperplasia (lâminas 15–19) ----------
 ak("ak-hiperplasia-controlada", 1487460265531, "A-step", C_, "Hiperplasia: proliferação controlada", 15, "lâmina 15; seção FirstAid"),
 ak("ak-endometrio", 1463172394153, "A-step", C_, "Hiperplasia endometrial → risco de carcinoma", 18, "lâmina 18 (estrógeno × progesterona; terreno fértil para neoplasia)"),
 ak("ak-hpb", 1463345947474, "A-step", C_, "HPB não aumenta o risco de câncer", 18, "lâminas 18–19 (andrógenos e hiperplasia prostática)",
    extra_add="- An exception to the rule that hyperplasia is fertile ground for cancer; prostate cancer arises in a different zone"),
 ak("ak-policlonal", 1496110605566, "A-aula", C_, "Hiperplasia é policlonal; neoplasia, monoclonal", 18, "lâmina 18 (diferença com neoplasia: a hiperplasia obedece aos sinais de parada)"),
 # ---------- D. Atrofia e hipoplasia (lâminas 20–27) ----------
 sh(1792117383096, "verde", D_, "Atrofia por menos células: apoptose", 21, "lâmina 21; prova 2017 P1 1.3 (mecanismo da atrofia: apoptose); card da 09"),
 au("au-atrofia-causas", ORG("<b>Causes of pathologic atrophy</b>:<br>1. {{c1::Disuse::D…}}<br>2. Loss of {{c1::innervation::i…}}<br>3. {{c1::Ischemia::I…}}<br>"
                              "4. Inadequate {{c1::nutrition::n…}}<br>5. Loss of {{c1::hormonal::h…}} stimulation<br>6. {{c1::Compression::C…}}"),
    "R-org", D_, "Causas de atrofia", 22, "lâmina 22 (lista do professor); palavras-cruzadas (lesão medular, ex-atleta)",
    extra="- Disuse: bedridden muscle and bone; denervation: spinal cord injury; ischemia: senile brain and heart<br>- Cachexia (TNF), menopause, tissue pressure"),
 ak("ak-ubiquitina-atrofia", 1487461046220, "V-hy", D_, "Atrofia: ubiquitina-proteassomo degrada o citoesqueleto", 23, "lâmina 23; seção FirstAid"),
 ak("ak-autofagia-atrofia", 1487461053514, "V-hy", D_, "Atrofia: autofagia", 23, "lâmina 23; seção FirstAid"),
 ak("ak-proteassomo", 1495595300874, "A-step", D_, "Ubiquitinação recruta o proteassomo", 23, "lâmina 23 (ligases e proteassomo)"),
 sh(1791729316911, "azul", D_, "Glicocorticoides aumentam a proteólise", 24, "lâmina 24 (corticoide degrada proteínas); card da integração II"),
 ak("ak-tireoide-degradacao", 1462038610838, "A-aula", D_, "Hormônio tireoidiano: efeito líquido de degradação proteica", 24, "lâmina 24 (hormônio tireoidiano degrada proteínas)"),
 sh(1791729320088, "azul", D_, "Insulina aumenta a síntese proteica", 24, "lâmina 24 (síntese: insulina); card da integração II"),
 ak("ak-hipoplasia", 1489113000682, "A-aula", D_, "Hipoplasia: desenvolvimento incompleto do órgão", 27, "lâmina 27 (órgão que nunca se desenvolveu)"),
 ak("ak-aplasia", 1489112996871, "A-step", D_, "Aplasia: órgão ausente com tecido primordial presente", 27, "lâmina 27 (no extremo, aplasia)"),
 ak("ak-aplasia-fa", 1487461136378, "R-detalhe", D_, "Aplasia: falha de produção a partir do primórdio", 27, "seção FirstAid adaptações"),
 ak("ak-agenesia", 1489112993482, "R-detalhe", D_, "Agenesia: sem tecido primordial", 27, "par de ak-aplasia"),
 # ---------- E. Metaplasia (lâminas 28–29) ----------
 ak("ak-metaplasia-irritante", 1487461064842, "A-aula", E_, "Metaplasia após irritante crônico (ácido, fumaça)", 28, "lâmina 28 (fumo); seção FirstAid"),
 ak("ak-metaplasia-tronco", 1487461072030, "A-aula", E_, "Metaplasia por reprogramação de células-tronco", 28, "lâmina 28 e transcrição (não é desdiferenciação)"),
 ak("ak-metaplasia-reversivel", 1487461075476, "A-aula", E_, "Metaplasia é reversível", 28, "transcrição (tirado o estímulo, volta a ser ciliado)"),
 ak("ak-metaplasia-cancer", 1487461083189, "A-step", E_, "Estresse persistente: displasia e câncer", 28, "lâmina 28 (transformação maligna se o estímulo persistir)"),
 ak("ak-barrett", 1482203859036, "A-step", E_, "Barrett: escamoso → colunar com caliciformes", 28, "transcrição (refluxo e metaplasia intestinal no esôfago)"),
 sh(1790972065735, "rosa", E_, "Barrett: junção escamocolunar sobe no esôfago", 28, "card da UC08"),
 ak("ak-vit-a", 1487461096732, "R-detalhe", E_, "Deficiência de vitamina A causa metaplasia", 28, "seção FirstAid metaplasia"),
 ak("ak-vit-a-diferenciacao", 1487461099399, "R-detalhe", E_, "Vitamina A diferencia epitélios especializados", 28, "par do anterior"),
 ak("ak-miosite", 1487461107256, "R-detalhe", E_, "Miosite ossificante: músculo vira osso", 29, "lâmina 29 (metaplasia mesenquimal)"),
 # ---------- F. Lípides e proteínas (lâminas 33–48) ----------
 sh(1792117372320, "azul", F_, "Proteínas mal dobradas acumulam e levam à apoptose", 33, "lâminas 33 e 45 (chaperonas, ubiquitina); card da 09"),
 sh(1791022171477, "verde", F_, "Esteatose macrovesicular", 35, "lâminas 35 e 40; provas 2024 P1, 2023 P1, 2016 P1; card da correlação 2"),
 sh(1791022171668, "azul", F_, "Fígado gorduroso do álcool", 35, "lâminas 35, 39–40; card da correlação 2"),
 sh(1791022171771, "azul", F_, "Esteatose reversível com abstinência", 35, "card da correlação 2"),
 ak("ak-ccl4", 1487470267945, "V-prova", F_, "CCl4 reduz apolipoproteína e causa esteatose", 38, "lâminas 36–38 (exportação por VLDL; tetracloreto de carbono); prova 2023 P1 2.5"),
 sh(1791054011671, "verde", F_, "Diabetes: lipólise envia ácidos graxos ao fígado", 37, "lâmina 37 (lipase hormônio-sensível sem insulina); prova 2024 P1 2.10; card do GR2"),
 ak("ak-kwashiorkor", 1476584121141, "A-step", F_, "Kwashiorkor: esteatose por pouca apolipoproteína", 38, "lâmina 38 (inanição reduz lipoproteínas)"),
 ak("ak-nadh", 1474254031118, "V-prova", F_, "Etanol aumenta NADH:NAD+ no fígado", 39, "lâmina 39 (metabolismo do álcool); provas 2016 P1 2.4 e 2023 P1 2.5"),
 sh(1791022172501, "rosa", F_, "Acetaldeído lesa o fígado", 39, "lâmina 39 (ação direta lesiva); card da correlação 2"),
 ak("ak-xantoma", 1472160925535, "A-step", F_, "Xantomas: histiócitos cheios de lípide na pele", 41, "lâmina 41"),
 ak("ak-foam", 1475966877989, "A-step", F_, "Macrófagos cheios de colesterol: células espumosas", 41, "lâminas 41–42 (aterosclerose)"),
 au("au-colesterolose", "Cholesterol-laden macrophages in the <b>gallbladder</b> wall give a speckled “strawberry” mucosa, called {{c1::cholesterolosis}}",
    "R-detalhe", F_, "Colesterolose da vesícula", 43, "lâmina 43 e transcrição (vesícula que parece morango); prova 2016 P1 1.5 (colesterol na parede da vesícula)",
    extra="- The same excess cholesterol in bile can also form gallstones"),
 ak("ak-bence-jones", 1481335899225, "A-step", F_, "Cadeias leves do mieloma nos túbulos renais", 44, "lâmina 44 (mieloma; dificuldade de reabsorção nos túbulos)"),
 ak("ak-alzheimer-ab", 1487550555569, "A-step", F_, "Alzheimer: amiloide β forma placas", 46, "lâmina 46 e transcrição (placa senil por falha de degradação)"),
 ak("ak-von-gierke", 1474253899159, "R-detalhe", F_, "Von Gierke: hipoglicemia de jejum", 47, "lâmina 47 (glicogenoses: falta de uma enzima da degradação)"),
 # ---------- G. Calcificação (lâminas 49–51) ----------
 ak("ak-dist-necrose", 1487470017343, "V-pilar", G_, "Distrófica: após lesão ou necrose", 49, "lâminas 49–50; seção FirstAid"),
 ak("ak-dist-local", 1487470065053, "A-step", G_, "Distrófica é localizada", 50, "seção FirstAid"),
 ak("ak-dist-normocalcemia", 1487470068885, "A-aula", G_, "Distrófica com cálcio sérico normal", 50, "lâmina 49 (independente da concentração de cálcio)"),
 ak("ak-ateroma-calcificado", 1471811951779, "A-step", G_, "Placa aterosclerótica sofre calcificação distrófica", 50, "lâmina 50 (aterosclerose)"),
 ak("ak-meta-normal", 1487470072763, "V-pilar", G_, "Metastática: em tecido normal", 49, "lâminas 49 e 51; seção FirstAid"),
 ak("ak-meta-hipercalcemia", 1487470077436, "A-aula", G_, "Metastática: por hipercalcemia ou hiperfosfatemia", 51, "lâmina 51 (PTH, destruição óssea, vitamina D, insuficiência renal)"),
 ak("ak-meta-difusa", 1487470084914, "A-step", G_, "Metastática é difusa", 51, "transcrição (calcinose generalizada)"),
 ak("ak-meta-calcemia", 1487470089328, "A-step", G_, "Metastática: cálcio sérico alterado", 51, "seção FirstAid"),
 ak("ak-meta-locais", 1487470094124, "A-step", G_, "Metastática: rim, pulmão, mucosa gástrica", 51, "lâmina 51 (cálcio no pulmão)"),
 ak("ak-hpt", 1585609132596, "R-detalhe", G_, "Hiperparatireoidismo causa calcificação metastática", 51, "lâmina 51 (aumento do PTH)"),
 # ---------- H. Pigmentos (lâminas 52–58) ----------
 sh(1791592721894, "verde", H_, "Antracose", 52, "lâmina 52; provas 2017 P1 2.2 e 2016 P1 2.7; card da patologia ambiental"),
 ak("ak-antracose-linfonodo", 1583378287742, "A-step", H_, "Pigmento antracótico nos linfonodos hilares", 52, "prova 2016 P1 2.7 (pulmões e linfonodo enegrecidos)"),
 ak("ak-lipofuscina", 1486590985316, "V-prova", H_, "Lipofuscina: pigmento do desgaste no envelhecimento", 53, "lâmina 53; prova 2016 P1 3.8 (lipofuscina nos neurônios); seção FirstAid"),
 ak("ak-lipofuscina-lisossomo", 1486590994020, "A-step", H_, "Lipofuscina se acumula nos lisossomos", 53, "seção FirstAid"),
 ak("ak-lipofuscina-locais", 1486590997246, "A-step", H_, "Lipofuscina: peroxidação lipídica; fígado, coração", 53, "lâmina 53 (peroxidação lipídica das membranas)"),
 au("au-atrofia-parda", "<b>Lipofuscin</b> in the aging heart and muscle turns them brown, a harmless change called brown {{c1::atrophy}}",
    "A-aula", H_, "Atrofia parda", 53, "lâmina 53 e transcrição (atrofia parda; lipofuscina é atóxica)",
    extra="- Lipofuscin comes from undigested peroxidized membranes after autophagy<br>- It has no pathologic meaning by itself"),
 ak("ak-tirosinase", 1476416094416, "A-step", H_, "Tirosinase: DOPA → melanina", 54, "lâmina 54 (tirosinase nos melanócitos)"),
 sh(1792150762535, "azul", H_, "Prussian blue (Perls) cora o ferro", 55, "lâmina 55 e transcrição (Perls cora o ferro em azul); card da 03"),
 sh(1791142466364, "azul", H_, "Células de insuficiência cardíaca", 55, "hemossiderina em macrófagos; card da 23"),
 ak("ak-hemossiderinuria", 1478915779009, "R-detalhe", H_, "Hemossiderinúria após hemólise intravascular", 56, "lâmina 56 (hemólises); palavras-cruzadas (hemossiderina)"),
 ak("ak-hemocromatose", 1486590838863, "V-hy", H_, "Hemocromatose: cirrose, diabetes, pele bronze", 57, "lâmina 57"),
 ak("ak-hemo-lipo", 1486590976651, "R-detalhe", H_, "Hemossiderina × lipofuscina pelo Prussian blue", 57, "transcrição (bile, ferro e lipofuscina são marrons)"),
 ak("ak-ictericia", 1486522390591, "V-prova", H_, "Icterícia: bilirrubina > 2,5 mg/dL", 58, "lâmina 58; prova 2016 P1 1.5 (bilirrubina na mucosa ocular)"),
 ak("ak-protoporfirina", 1478915717184, "A-step", H_, "Protoporfirina do heme vira bilirrubina", 58, "lâmina 58 e transcrição (bilirrubina deriva da hemoglobina, sem ferro)"),
]

finalizar(CARDS, HERE, BUSCA)

SEM_IMAGEM = "conceito ou mecanismo sem estrutura a reconhecer; as figuras das lâminas são exemplos do professor sem alvo único"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM

VERSO = {
 "ak-hipertrofia-def": "- No new cells: more contractile filaments and organelles in each cell",
 "ak-endometrio": "- Unopposed estrogen keeps the endometrium proliferating",
 "ak-proteassomo": "- In atrophy this pathway removes cytoskeleton and contractile proteins",
 "ak-hipoplasia": "- Unlike atrophy, the organ never reached its normal size",
 "ak-aplasia": "- The extreme of hypoplasia: the organ never formed",
 "ak-vit-a": "- Vitamin A keeps specialized epithelia; its lack favors squamous metaplasia",
 "ak-kwashiorkor": "- Without enough protein, hepatocytes cannot package triglycerides into VLDL",
 "ak-nadh": "- Excess NADH favors fatty acid synthesis and blocks their oxidation, so fat accumulates",
 "ak-xantoma": "- Cholesterol builds up where it does not belong when blood lipids stay high",
 "ak-von-gierke": "- Glucose-6-phosphatase deficiency traps glycogen in liver and kidney",
 "ak-meta-normal": "- Calcium is high in the blood, so it deposits even in healthy tissue",
 "ak-dist-local": "- It follows the injured area; blood calcium is normal",
 "ak-ateroma-calcificado": "- Dead foam cells and debris in the plaque calcify",
 "ak-meta-difusa": "- Widespread calcinosis, for example in the lungs",
 "ak-ictericia": "- Yellow-green staining of skin, sclera and organs",
 "ak-protoporfirina": "- Iron from heme becomes hemosiderin; the rest becomes bilirubin",
}
for c in CARDS:
    if c["key"] in VERSO and VERSO[c["key"]] and c["kind"] != "autoral":
        c["extra_add"] = VERSO[c["key"]] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
DUPLICACAO = {"au-atrofia-parda": "ganho: o nome do achado macroscópico da lipofuscina (atrofia parda); ak-atrofia-def cobra a definição geral"}
for _k, _v in DUPLICACAO.items():
    next(c for c in CARDS if c["key"] == _k)["duplicacao_ok"] = _v
IMAGENS_VISTAS = {}
REVISAO = {"despejo": "Despejo lido inteiro em 17/10 (61 notas novas, 72 cards; frentes, clozes, versos e cores conferidos). Nada a corrigir.", "corrigidos": []}
ESCOPO = {
 "objetivo": "Reconhecer as quatro adaptações celulares (hipertrofia, hiperplasia, atrofia, metaplasia), seus estímulos e mecanismos e a "
             "relação com o tipo de tecido; entender os acúmulos (esteatose, colesterol, proteínas, glicogênio), a calcificação distrófica × "
             "metastática e os pigmentos (antracose, lipofuscina, melanina, hemossiderina, bilirrubina).",
 "centrais": [
   ("adaptações", "ak-permanentes", "ak-hipertrofia-def", "ak-hiperplasia-def", "ak-atrofia-def", "ak-metaplasia-def", "au-hipertrofia-gatilhos", "au-hipertrofia-fetal"),
   ("esteatose", "sh-1791022171477", "ak-ccl4", "ak-nadh", "sh-1791054011671"),
   ("calcificação", "ak-dist-necrose", "ak-meta-normal"),
   ("pigmentos", "sh-1791592721894", "ak-lipofuscina", "ak-ictericia"),
 ],
 "exemplos": ["miocárdio na hipertensão", "útero gravídico", "regeneração hepática", "HPB", "metaplasia no fumante", "Barrett", "álcool e esteatose",
              "aterosclerose", "Alzheimer", "hemocromatose"],
 "outras_aulas": [("lesão e apoptose", "09 (sh)"), ("esteatose na imagem", "19 (sh)"), ("antracose", "24 (sh)"), ("envelhecimento", "13")],
}
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
