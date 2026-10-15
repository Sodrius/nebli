# Especificação curada — Lesão celular, necrose e apoptose (UC03 P1, Patologia; Prof. Luiz F. Ferraz da Silva).
# Sequência única = lâminas Ia (47): 1–20 mecanismos de lesão; 21–47 necrose e apoptose (= Ib, versão da pasta pessoal).
# Adaptação = aula 11; caseosa em detalhe = 47; resposta T citotóxica = 45; infarto em detalhe = aula própria. Aula antiga: entra suspensa.
RUN_ID = "uc03-pt09-20261014a"
SHORT = "pt09"
LESSON = "2026-uc03-patologia-09-lesao-celular"
DECK = "NEBLI::UC03::P1::Patologia::Lesão celular, necrose e apoptose"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {"pt09-tubulo.jpeg": "img/pt09-tubulo.jpeg", "pt09-coagulativa.jpeg": "img/pt09-coagulativa.jpeg"}
F = lambda n, w=440: f'<img src="pt09-{n}.jpeg" width="{w}">'
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por seções inteiras (B&B Cell Injury, Free Radicals, Apoptosis, Necrosis; FirstAid Cellular Injury; Pathoma Cellular Injury; "
         "busca/tags-secao.txt) e cópias NEBLI vivas conferidas por nid de origem, 14/10: ")
EXCLUIDOS = [
 (1487463907439, "hallmark de irreversibilidade (membrana): coberto pelo organizador b-criterios, que traz os dois critérios da aula"),
 (1487469750801, "picnose: coberta pelo organizador d-nucleo (sequência pedida por Davi em tópicos)"),
 (1487469755479, "cariorrexe: coberta pelo organizador d-nucleo"),
 (1487469759701, "cariólise: coberta pelo organizador d-nucleo"),
 (1487470222716, "DNA laddering: técnica laboratorial não ensinada nas lâminas"),
 (1481335336072, "t(14;18)/BCL-2 no linfoma folicular: aula de neoplasias"),
 (1487463922315, "vacuolização mitocondrial: detalhe ultraestrutural (o professor: “não nesse nível de detalhes”)"),
 (1471899221722, "necrose em banda de contração: aula de infarto"),
 (1487469944925, "necrose caseosa “cottage cheese”: já viva no GR3 (associada por sh)"),
]
FORA_DO_RECORTE = [
 "Adaptação celular (hipertrofia, atrofia): aula 11 Acúmulos e adaptação.",
 "Detalhes ultraestruturais além do edema, bolhas, desligamento de ribossomos e cromatina: o professor disse que não precisam nesse nível.",
 "Necroptose: citada sem detalhe (Ia 45).",
 "Necrose caseosa e granuloma em detalhe: aula 47.",
 "Infarto do miocárdio e enzimas cardíacas em detalhe: aula própria de infarto.",
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


ORG = lambda s: f'<div data-nebli-organizacao="true">{s}</div>'
G = lambda *k: {i: V for i in k}
NAO = "o AnKing não tem este conjunto/nome como card (só fatos isolados ou outra formulação)."
EP_CONJ = [1487469763555, 1487470255062, 1487470148526]       # conjunto nomeado de mecanismos/enzimas
EP_FATO = [1487463871778, 1487469733350, 1487463914329]       # fato pontual de lesão celular

A_, B_, C_, D_, E_ = "A-causas-e-desfechos", "B-reversivel-irreversivel", "C-mecanismos", "D-necrose", "E-apoptose"

CARDS = [
 # ---------- A. Resposta à agressão (Ia 2–6) ----------
 ak("ak-dois-mecanismos", 1487469763555, G(1, 2), A_, "Necrose e apoptose: os dois tipos de morte", 2, "Verde: HY 2; esquema da lâmina 2."),
 ak("ak-angina", 1471880379381, G(1), A_, "Angina = lesão reversível", 3, "Verde: HY 2; exemplo de lesão reversível (lâmina 3)."),
 ak("ak-iam", 1471898845279, G(1), A_, "Infarto = lesão irreversível", 3, "Verde: HY 1; exemplo de lesão irreversível (lâmina 3)."),
 au("a-hipoxia", "The most common cause of <b>cell injury</b> is {{c1::hypoxia}}, usually due to ischemia", G(1), A_,
    "Causa mais comum de lesão celular", "5; cruzadas 15", "central", NAO, EP_FATO, "Verde: primeira causa da lâmina 5.",
    extra="- Other causes: physical and chemical agents, infections, immune reactions, genetic and nutritional disorders"),
 au("a-gross", "After lethal <b>cell injury</b>, function and biochemistry change first, and {{c1::gross}} morphologic changes appear last",
    {1: Z}, A_, "Sequência temporal das alterações", "6; cruzadas 26", "central", NAO, EP_FATO, "Azul: gráfico da lâmina 6.",
    extra="- An infarcted heart still looks normal to the naked eye after 1 hour"),

 # ---------- B. Reversível × irreversível (Ia 7–11) ----------
 ak("ak-edema", 1487463887140, G(1), B_, "Marca da lesão reversível: edema celular", 7, "Verde: HY 1; lâmina 7."),
 ak("ak-bolhas", 1487463894466, G(1, 2), B_, "Bolhas e perda de microvilosidades", 7, "Verde: HY 1; lâmina 7."),
 ak("ak-ribossomos", 1487463900987, G(1, 2, 3), B_, "Desligamento de ribossomos", 7, "Verde: HY 1; lâmina 7 (cruzadas 22)."),
 ak("ak-cromatina", 1521136890400, G(1, 2), B_, "Condensação da cromatina", "7; 10", "Verde: HY 1; lâminas 7 e 10."),
 au("b-criterios", ORG("<b>Irreversible cell injury</b> is defined by:<br>- loss of plasma {{c1::membrane}} integrity<br>- extensive damage to {{c2::DNA}} and proteins"),
    G(1, 2), B_, "Dois critérios de irreversibilidade", "8; prova 2024 P1 2.8", "prova", NAO, EP_CONJ, "Verde: lâmina 8; prova 2024.", duplicacao_ok="ganho: organizador dos dois critérios; os AnKing perguntam sinais isolados",
    extra="- In hypoxia, membrane damage usually comes first; in genetic damage, DNA destruction does"),
 ak("ak-nucleo", 1487469733350, G(1), B_, "Perda do núcleo marca morte celular", 9, "Verde: HY 1; túbulos da lâmina 9.",
    extra_add="- A normal, B reversible injury (swelling), C irreversible injury (nuclei lost)<br>" + F("tubulo")),
 ak("ak-enzimas", 1487463914329, G(1), B_, "Enzimas no sangue = lesão irreversível", 11, "Verde: HY 2; lâmina 11 (provas 2017, 2015)."),
 au("b-transaminases", "Elevated serum {{c1::transaminases}} (AST, ALT) show that <b>hepatocytes</b> suffered irreversible injury",
    {1: Z}, B_, "Transaminases e lesão hepatocitária", "11; prova 2018 P3 1.4; cruzadas 13", "prova", NAO, EP_FATO, "Azul: prova 2018.",
    extra="- Troponin and CK-MB play the same role for the heart; lipase and amylase for the pancreas"),

 # ---------- C. Mecanismos (Ia 12–20) ----------
 au("c-mecanismos", ORG("Core mechanisms of <b>cell injury</b>:<br>- {{c1::ATP}} depletion<br>- {{c2::mitochondrial}} damage<br>- {{c3::calcium}} influx<br>- {{c4::free radicals}} (oxidative stress)"),
    G(1, 2, 3, 4), C_, "Organizador dos mecanismos de lesão", "12; 18", "central", NAO, EP_CONJ, "Verde: lâminas 12 e 18.", duplicacao_ok="ganho: composição do conjunto de mecanismos; os AnKing aprofundam cada um",
    extra="- They feed each other and converge on membrane and DNA damage"),
 ak("ak-atp", 1487463871778, G(1), C_, "Falta de ATP na hipóxia", 13, "Verde: HY 1; lâmina 13."),
 ak("ak-bombas", 1487463879752, G(1), C_, "Bombas de Na⁺/K⁺ e Ca²⁺ param", 13, "Verde: HY 1; lâmina 13.",
    extra_add="- Na⁺ and water enter, so the cell and its organelles swell"),
 au("c-lactato", "In <b>hypoxic cells</b>, anaerobic glycolysis accumulates {{c1::lactic acid}}, which lowers pH and clumps nuclear chromatin",
    G(1), C_, "Glicólise anaeróbia e ácido lático", "13; cruzadas 3", "central", NAO, EP_FATO, "Verde: lâmina 13.",
    extra="- Glycogen stores are consumed in the process"),
 au("c-reducao", "Oxygen <b>free radicals</b> arise mainly from {{c1::incomplete reduction}} of oxygen in the mitochondrial respiratory chain",
    {1: Z}, C_, "Origem dos radicais livres", "14; cruzadas 28", "central", NAO, EP_FATO, "Azul: lâmina 14."),
 ak("ak-superoxido", 1487470227188, {1: Z}, C_, "Superóxido", 14, "Azul: HY 3; esquema da lâmina 14."),
 ak("ak-sod", 1487470252945, G(1), C_, "Superóxido dismutase", 14, "Verde: HY 2; lâmina 14."),
 ak("ak-catalase", 1487470255062, G(1), C_, "Catalase e glutationa peroxidase", 14, "Verde: HY 1; lâmina 14."),
 ak("ak-glutationa", 1478995091598, {1: Z}, C_, "Glutationa reduzida neutraliza H₂O₂", 14, "Azul: HY 3; cruzadas 23."),
 ak("ak-peroxidacao", 1487470244885, G(1), C_, "Peroxidação de lipídios", 14, "Verde: HY 2; lâmina 14 (cruzadas 14)."),
 ak("ak-reperfusao", 1487470274721, G(1), C_, "Lesão de reperfusão", 15, "Verde: HY 1; lâmina 15; prova 2015.",
    extra_add="- Also why a transplanted kidney loses function right after its vessels are reconnected"),
 au("c-mitocondria", ORG("<b>Injured mitochondria</b> lead to:<br>- necrosis, through loss of membrane potential and {{c1::ATP}}<br>- apoptosis, through leakage of {{c2::cytochrome c}}"),
    G(1, 2), C_, "Mitocôndria lesada → necrose ou apoptose", "16; cruzadas 35", "central", NAO, EP_CONJ, "Verde: lâmina 16.",
    duplicacao_ok="ganho: as duas saídas da mitocôndria lesada; o organizador c-mecanismos só lista os mecanismos"),
 au("c-calcio", ORG("Increased cytosolic <b>Ca²⁺</b> activates:<br>- {{c1::phospholipases}}, damaging membranes<br>- {{c2::proteases}}, breaking the cytoskeleton<br>- {{c3::endonucleases}}, fragmenting DNA<br>- {{c4::ATPases}}, depleting ATP"),
    G(1, 2, 3, 4), C_, "Enzimas ativadas pelo cálcio", "17; prova 2024 P1 2.8; cruzadas 25", "prova", NAO, EP_CONJ, "Verde: lâmina 17; prova 2024.",
    extra="- Ca²⁺ comes from outside the cell and from mitochondria and ER stores"),
 au("c-chaperonas", "Misfolded proteins that {{c1::chaperones}} cannot refold accumulate and trigger <b>apoptosis</b>",
    {1: Z}, C_, "Dobramento proteico e chaperonas", "20; cruzadas 30", "central", NAO, EP_FATO, "Azul: lâmina 20.",
    extra="- Neurodegenerative diseases such as Alzheimer involve this mechanism"),

 # ---------- D. Necrose (Ia 23–35) ----------
 ak("ak-nunca-fisiologica", 1487469766823, {1: Z}, D_, "Necrose nunca é fisiológica", 23, "Azul: HY 3; comparação da lâmina 23."),
 ak("ak-apoptose-sem-inflamacao", 1487470122628, G(1), D_, "Apoptose sem inflamação", 23, "Verde: HY 2; lâmina 23 (cruzadas 4)."),
 ak("ak-lisossomos", 1487463924702, G(1), D_, "Enzimas lisossômicas digerem a célula", 25, "Verde: HY 2; lâmina 25."),
 ak("ak-eosinofilia", 1520442532258, G(1), D_, "Eosinofilia da necrose", 27, "Verde: HY 2; lâmina 27 (cruzadas 6)."),
 au("d-nucleo", ORG("Nuclear changes of <b>necrosis</b>, in sequence:<br>- {{c1::pyknosis}} (condensation)<br>- {{c2::karyorrhexis}} (fragmentation)<br>- {{c3::karyolysis}} (dissolution)"),
    G(1, 2, 3), D_, "Sequência das alterações nucleares", "27; cruzadas 19; prova 2015 P1sub", "prova", NAO, EP_CONJ, "Verde: lâmina 27."),
 ak("ak-coagulativa", 1487469807276, G(1, 2), D_, "Necrose coagulativa: contornos mantidos, núcleo some", 28, "Verde: HY 1; lâmina 28 (cruzadas 21).",
    extra_add=F("coagulativa")),
 ak("ak-coagulativa-isquemia", 1487469816961, G(1, 2, 3), D_, "Coagulativa = infarto isquêmico, exceto cérebro", 28, "Verde: HY 1; lâmina 28."),
 ak("ak-liquefativa", 1487469877849, G(1), D_, "Liquefativa: cérebro e abscesso", 29, "Verde: HY 1; lâmina 29 (cruzadas 36; prova 2018)."),
 sh(1791716427402, "azul", D_, "Necrose caseosa", 30, "Azul: lâmina 30; viva no GR3 (detalhe na 47)."),
 ak("ak-gordurosa", 1482971299269, G(1), D_, "Necrose gordurosa na pancreatite", 32, "Verde: HY 1; lâmina 32 (prova 2016, 2023)."),
 ak("ak-saponificacao", 1487469981667, {1: Z}, D_, "Saponificação", 32, "Azul: HY 4; prova 2023 P1 1.6."),
 ak("ak-fibrinoide", 1487470100826, G(1), D_, "Necrose fibrinoide em vasos", 34, "Verde: HY 2; lâmina 34."),
 ak("ak-gangrenosa", 1487469931164, G(1, 2, 3), D_, "Gangrena", 35, "Verde: HY 2; lâmina 35; prova 2024 P1 2.1."),

 # ---------- E. Apoptose (Ia 36–44) ----------
 au("e-fisiologica", ORG("Physiologic causes of <b>apoptosis</b>:<br>- {{c1::embryogenesis}}<br>- {{c1::hormone-dependent}} involution (e.g., endometrium)<br>- deletion of self-reactive {{c1::lymphocytes}}"),
    {1: Z}, E_, "Causas fisiológicas de apoptose", "36; cruzadas 20", "central", NAO, EP_CONJ, "Azul: lâmina 36; conjunto recuperado junto.",
    extra="- Pathologic causes: DNA damage, misfolded proteins, intracellular infections, pathologic atrophy"),
 ak("ak-atrofia", 1487461041752, G(1), E_, "Atrofia ocorre por apoptose", 36, "Verde: HY 1; lâmina 36; prova 2017 P1 1.3."),
 ak("ak-bcl2-citc", 1487470164855, G(1), E_, "BCL-2 impede saída do citocromo c", 38, "Verde: HY 1; lâmina 38."),
 ak("ak-bax", 1487470180854, G(1), E_, "BAX/BAK pró-apoptóticas", "38; 42", "Verde: HY 1; tabela da lâmina 42."),
 ak("ak-bcl2-anti", 1487470187106, G(1), E_, "BCL-2/BCL-xL antiapoptóticas", "38; 42", "Verde: HY 1; tabela da lâmina 42; prova 2016."),
 ak("ak-p53", 1496161930377, G(1, 2), E_, "p53 ativa BAX/BAK", "38; 44", "Verde: HY 1; lâmina 44 (cruzadas 34)."),
 ak("ak-citc-caspases", 1496161956265, G(1, 2), E_, "Citocromo c ativa caspases iniciadoras", 38, "Verde: HY 1; lâmina 38 (cruzadas 1)."),
 sh(1791625429657, "verde", E_, "Via extrínseca: Fas-L/CD95 e TNF", 38, "Verde: lâmina 38 (cruzadas 27); viva na 45."),
 ak("ak-caspases", 1487470148526, G(1), E_, "Caspases executam a apoptose", 38, "Verde: HY 1; lâmina 38 (cruzadas 32)."),
 ak("ak-morfologia-apoptose", 1487470128060, G(1), E_, "Morfologia da apoptose", "39–40", "Verde: HY 1; lâminas 39–40."),
 ak("ak-corpos-apoptoticos", 1487470141075, {1: Z}, E_, "Corpos apoptóticos fagocitados", "40–41", "Azul: HY 3; cruzadas 11 e 33."),
 sh(1791625429957, "azul", E_, "CD8 induz apoptose", 44, "Azul: correlação da lâmina 44 (cruzadas 16); viva na 45/61."),
 au("e-doencas", ORG("<b>Apoptosis</b> and disease:<br>- too little: {{c1::cancer}} and autoimmunity<br>- too much: {{c2::neurodegenerative}} diseases"),
    {1: Z, 2: Z}, E_, "Apoptose deficiente × excessiva", "44; cruzadas 18", "central", NAO, EP_CONJ, "Azul: lâmina 44."),
]

SEM_IMAGEM = "fato ou conjunto sem estrutura própria a reconhecer; as imagens que ensinam estão nos cards de núcleo (túbulo) e de necrose coagulativa"
SLIDE_SEM_ALT = "figura da própria lâmina da aula (Robbins), sem equivalente no AnKing"
for c in CARDS:
    blob = c.get("text", "") + c.get("extra", "") + c.get("extra_add", "")
    if c["kind"] in ("text", "autoral") and "<img" not in blob:
        c["sem_imagem"] = SEM_IMAGEM
    if "pt09-" in blob:
        c["slide_sem_alternativa"] = SLIDE_SEM_ALT

VERSO = {
 "ak-angina": "- Blood flow returns before cells pass the point of no return",
 "ak-iam": "- Prolonged ischemia (more than ~30 min) kills cardiomyocytes",
 "ak-cromatina": "- Low pH from lactic acid clumps the chromatin",
 "ak-enzimas": "- Enzymes can only leave the cell through a damaged plasma membrane",
 "c-reducao": "- Antioxidants (SOD, catalase, glutathione peroxidase) normally remove them",
 "ak-sod": "- H2O2 is then removed by catalase or glutathione peroxidase",
 "c-mitocondria": "- The same organelle decides between the two forms of death",
 "ak-apoptose-sem-inflamacao": "- The membrane stays intact and apoptotic bodies are phagocytosed",
 "d-nucleo": "- Loss of the nucleus is the hallmark of cell death",
 "ak-coagulativa-isquemia": "- The brain liquefies because it lacks a collagen framework",
 "ak-gangrenosa": "- Dry gangrene is coagulative; superinfection makes it wet (liquefactive)",
 "ak-caspases": "- Initiator caspases (8, 9) activate executioner caspases",
 "ak-morfologia-apoptose": "- The cell shrinks instead of swelling, unlike necrosis",
 "ak-corpos-apoptoticos": "- Rapid removal prevents leakage and inflammation",
 "e-doencas": "- Example of excess: neuronal loss in Alzheimer disease",
}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if k in VERSO:
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {
 "pt09-tubulo.jpeg": "Lâmina Ia 9 (Robbins): túbulos normais (A), lesão reversível com edema (B) e irreversível sem núcleos (C); letras sem legenda; no verso.",
 "pt09-coagulativa.jpeg": "Lâmina Ia 28: miocárdio com necrose coagulativa (fibras eosinofílicas sem núcleo) e neutrófilos; no verso.",
}
REVISAO = {}
ESCOPO = {
 "objetivo": "Entender como uma agressão leva a lesão reversível ou irreversível, pelos mecanismos (ATP, mitocôndria, cálcio, radicais livres), e reconhecer os dois tipos de morte celular: necrose (com seus padrões) e apoptose (vias e morfologia).",
 "centrais": [
   ("desfechos da agressão", "ak-dois-mecanismos", "ak-angina", "ak-iam", "a-hipoxia", "a-gross"),
   ("reversível × irreversível", "ak-edema", "ak-bolhas", "ak-ribossomos", "ak-cromatina", "b-criterios", "ak-nucleo", "ak-enzimas", "b-transaminases"),
   ("mecanismos de lesão", "c-mecanismos", "ak-atp", "ak-bombas", "c-lactato", "c-reducao", "ak-superoxido", "ak-sod", "ak-catalase", "ak-glutationa", "ak-peroxidacao", "ak-reperfusao", "c-mitocondria", "c-calcio", "c-chaperonas"),
   ("necrose", "ak-nunca-fisiologica", "ak-apoptose-sem-inflamacao", "ak-lisossomos", "ak-eosinofilia", "d-nucleo", "ak-coagulativa", "ak-coagulativa-isquemia", "ak-liquefativa", "sh-1791716427402", "ak-gordurosa", "ak-saponificacao", "ak-fibrinoide", "ak-gangrenosa"),
   ("apoptose", "e-fisiologica", "ak-atrofia", "ak-bcl2-citc", "ak-bax", "ak-bcl2-anti", "ak-p53", "ak-citc-caspases", "sh-1791625429657", "ak-caspases", "ak-morfologia-apoptose", "ak-corpos-apoptoticos", "sh-1791625429957", "e-doencas"),
 ],
 "exemplos": ["hipertensão/Alzheimer (adaptação)", "hepatite aguda", "queimadura solar", "transplante renal (reperfusão)"],
 "outras_aulas": [("adaptação", "11 Acúmulos e adaptação"), ("granuloma e caseosa", "47 Inflamação granulomatosa"), ("CD8 e Fas", "45 Ativação de linfócitos T"), ("infarto", "aula de infarto")],
}

import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
# Ajuste 15/10 noite (F-20261015-CLAUDE-05): apostila guia de Patologia Aula 2 e monitoria P1 (Pato aula 1) lidas; Robbins cap. 1 já lido.
_M3 = "Ajuste 15/10 noite (F-20261015-CLAUDE-05)."
CARDS += [
 au("a-causas", ORG("Main causes of <b>cell injury</b>:<br>1. {{c1::oxygen deprivation}}<br>2. physical agents<br>3. chemicals and drugs<br>4. infectious agents<br>5. {{c2::immunologic}} reactions<br>6. genetic derangements<br>7. nutritional imbalances"),
    {1: Z, 2: Z}, A_, "Causas de lesão celular", "5", "central", NAO, EP_CONJ, "Azul: lâmina 5, apostila guia Aula 2 cap. 1 e monitoria P1 aula 1. " + _M3,
    extra="- Ischemia, the commonest, combines hypoxia with loss of nutrients"),
 au("a-isquemia", "<b>Ischemia</b> injures cells faster than {{c1::hypoxia}} alone, because it also cuts off nutrients and lets toxic metabolites accumulate",
    {1: Z}, A_, "Isquemia × hipóxia", "5", "central", NAO, EP_FATO, "Azul: apostila guia Aula 2 cap. 1 (isquemia × hipóxia por pneumonia, anemia, CO). " + _M3,
    extra="- Hypoxia without ischemia: pneumonia, anemia, carbon monoxide poisoning"),
 au("b-gordura", "Besides cell swelling, the other light-microscopic change of reversible <b>cell injury</b> is {{c1::fatty change}}, seen mostly in liver and heart",
    {1: Z}, B_, "Alteração gordurosa na lesão reversível", "7", "central", NAO, EP_FATO, "Azul: lâmina 7 e monitoria P1 aula 1. " + _M3,
    extra="- It comes from disrupted lipid metabolism inside the injured cell"),
 ak("ak-caseosa-tb", 1487469962274, {1: V}, D_, "Caseosa: tuberculose e fungos", "30", "Verde: lâmina 30, apostila guia Aula 2 cap. 4 e monitoria P1 aula 1. " + _M3,
    extra_add="- Unlike coagulative necrosis, tissue architecture is completely lost"),
 au("e-fosfatidilserina", "<b>Apoptotic cells</b> flip {{c1::phosphatidylserine}} to the outer leaflet of the membrane, an eat-me signal for macrophages",
    {1: Z}, E_, "Fosfatidilserina: sinal de remoção", "40", "central", "consulta phosphatidylserine sem card (15/10 noite).", EP_FATO, "Azul: lâmina 37 (etapa de remoção) e Robbins cap. 1. " + _M3,
    extra="- Quick removal keeps cell contents from leaking and causing inflammation"),
 au("e-necroptose", "{{c1::Necroptosis}} is a programmed form of <b>necrosis</b> triggered by death receptors through RIP kinases, without caspases",
    {1: R}, E_, "Necroptose", "45", "lateral", NAO, EP_FATO, "Rosa: lâmina 45 (o professor mostrou sem detalhar); Robbins cap. 1. " + _M3,
    extra="- It looks like necrosis but is regulated like apoptosis"),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
CARDS += [
 au("e-iniciadoras", "The initiator caspase of the <b>intrinsic</b> (mitochondrial) pathway is caspase-{{c1::9::8/9}}, and that of the extrinsic (death-receptor) pathway is caspase-{{c1::8::8/9}}",
    {1: Z}, E_, "Caspases iniciadoras 9 e 8", "38", "central", "consultas caspase-9/caspase-8 sem card AnKing (15/10 noite).", EP_FATO, "Azul: apostila guia Aula 2 cap. 6 (caspases desencadeantes 8 e 9; executoras). " + _M3,
    extra="- Both converge on executioner caspases that cleave the cell's components"),
 au("e-bh3", "Stress sensors of the <b>BCL-2 family</b>, the {{c1::BH3-only}} proteins, tip the balance toward mitochondrial leak and apoptosis",
    {1: R}, E_, "Sensores BH3", "38", "lateral", NAO, EP_FATO, "Rosa: apostila guia Aula 2 cap. 6 e Robbins cap. 1. " + _M3,
    extra="- They activate BAX/BAK and neutralize BCL-2"),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
_SI2 = "conceito/mecanismo sem estrutura a reconhecer em imagem (ajuste 15/10 noite)"
for _c_ in CARDS:
    if _c_["key"] in ("a-causas", "a-isquemia", "b-gordura", "e-fosfatidilserina", "e-necroptose", "e-iniciadoras", "e-bh3", "ak-caseosa-tb"):
        _c_.setdefault("sem_imagem", _SI2)
import json as _json, pathlib as _pl
_cv = _json.loads((_pl.Path(__file__).parent / "correcoes-vivas.json").read_text())
for _c_ in CARDS:
    if _c_["key"] in _cv and "Extra" in _cv[_c_["key"]]:
        _c_["extra"] = _cv[_c_["key"]]["Extra"]; _c_.pop("extra_add", None)
