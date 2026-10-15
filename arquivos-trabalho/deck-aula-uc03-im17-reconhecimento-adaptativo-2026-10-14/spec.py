# Especificação curada — Reconhecimento pelo sistema imune na resposta adquirida (UC03 P1, Imunologia; Prof. Barbuto; 18 lâminas = Anb.pdf, versão 2026).
# A aula 49 (Ativação de células B) e a 18 (Recombinação) já têm estrutura, classes e recombinação: entram por sh(). Esta aula acrescenta a história, Fab/Fc e funções por classe.
RUN_ID = "uc03-im17-20261014a"
SHORT = "im17"
LESSON = "2026-uc03-imunologia-17-reconhecimento-adaptativo"
DECK = "NEBLI::UC03::P1::Imunologia::Reconhecimento imune adaptativo"
CRITERIOS = "MEMORY.md + ANTI-EXEMPLARES-CARDS (14/10) + PLANO-CONTINUACAO-DECKS, 14/10/2026"
MEDIA = {}
V, Z, R = 3, 4, 5
BUSCA = ("AnKing por frases (IgM, IgE, IgA, papain, allotype, idiotype, avidity, complementarity, IgD, T-cell receptor, humoral, thyroid-stimulating immunoglobulin, colostrum; "
         "busca/anking.txt) e cópias NEBLI vivas das aulas 49 e 18, 14/10: ")
EXCLUIDOS = [(1486867718130, "TCR rígido sem dobradiça: detalhe estrutural fora da aula")]
FORA_DO_RECORTE = ["Seleção nos órgãos linfoides primários (lâmina 3): recapitulação da aula 07.", "Mecanismo molecular da recombinação: aula 18.", "Experimentos históricos do TCR (Allison, Davis): Tab."]


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
NAO = "o AnKing não tem este fato da aula como card."
EP = [1487117055356, 1487117063416, 1486867654077]
A_, B_, C_, D_, E_ = "A-imunidade-adquirida", "B-anticorpos-no-soro", "C-estrutura", "D-classes-e-funcoes", "E-diversidade"

CARDS = [
 # A — características (4–6)
 au("a-memoria", ORG("Two hallmarks of <b>acquired immunity</b>, absent from innate immunity:<br>- {{c1::specificity}}<br>- {{c2::memory}}"),
    G(1, 2), A_, "Especificidade e memória", "5; prova 2024 P1 2.11", "prova", NAO, EP, "Verde: lâmina 5; prova 2024 (diferença inata × adquirida). Revisão 15/10: o cloze estava no adjetivo de um experimento histórico.",
    extra="- Mice immunized with attenuated bacterium Y still die from virulent X: protection is specific"),
 au("a-humoral", ORG("Classic definition by <b>transfer</b>:<br>- immunity transferred by {{c1::serum}}: humoral<br>- immunity transferred only by {{c2::cells}}: cellular"),
    G(1, 2), A_, "Humoral × celular", "6; 18", "central", NAO, EP, "Verde: lâmina 6; resumo (lâmina 18).",
    extra="- Today the two overlap: humoral responses also depend on T cells"),
 au("a-b-direto", "{{c1::B cells::T or B}} recognize native antigen directly through their clonal receptors, without needing <b>antigen-presenting cells</b>",
    {1: Z}, A_, "B reconhece diretamente", "6; 4", "central", NAO, EP, "Azul: lâmina 4; transcrição.",
    extra="- T cells then decide, through their signals, whether the B cell responds"),
 # B — anticorpos no soro (7–10)
 au("b-gama", "<b>Hyperimmunization</b> raises the {{c1::gamma}}-globulin peak on serum electrophoresis, which is why antibodies were first identified as gamma-globulins",
    {1: Z}, B_, "Anticorpos = gamaglobulinas", "7", "central", NAO, EP, "Azul: lâmina 7; histórico (revisão 15/10).",
    extra="- A normal immune response does not change the electrophoretic profile, because antibodies are made all the time"),
 sh(1792029316961, "verde", B_, "Mieloma: pico monoclonal", "8", "Verde: lâmina 8; viva na aula 18."),
 au("b-dreyer", "<b>Myeloma proteins</b> share a constant part and differ in a variable part of one chain, suggesting {{c1::two genes}} encode one polypeptide",
    {1: R}, B_, "Dreyer e Bennett", "9", "lateral", NAO, EP, "Rosa: lâmina 9; histórico (revisão 15/10).",
    extra="- First clue to somatic recombination (1965)"),
 au("b-troca", "During a <b>primary response</b>, IgM comes first and IgG follows, both with the same {{c1::specificity}}",
    G(1), B_, "Troca de classes com a mesma especificidade", "10; prova 2017 P3 1.6", "prova", NAO, EP, "Verde: lâmina 10; prova 2017.",
    extra="- The same plasma cell lineage can switch from IgM to IgG"),
 sh(1792029321811, "azul", B_, "Troca de classe por deleção de DNA", "10", "Azul: prova 2017 P3 1.6 (mecanismo); viva na aula 18."),
 # C — estrutura (11–12)
 ak("ak-papaina", 1487117055356, G(1), C_, "Papaína: 2 Fab + Fc", "11; prova 2024 P1 1.7", "Verde: lâmina 11; prova 2024 (Fab × Fc cristalizável).",
    extra_add="- Fab = fragment antigen binding; Fc = fragment crystallizable"),
 ak("ak-pepsina", 1487117063416, {1: Z}, C_, "Pepsina: F(ab′)2", "11", "Azul: lâmina 11."),
 sh(1791629588145, "verde", C_, "Duas cadeias pesadas e duas leves", "11", "Verde: lâmina 11; viva na aula 49."),
 au("c-leves", "Each <b>antibody</b> uses one of two light-chain types, {{c1::kappa and lambda}}, combined with any heavy chain",
    {1: Z}, C_, "Cadeias leves kappa e lambda", "11", "central", NAO, EP, "Azul: lâmina 11.",
    extra="- The heavy chain (μ, δ, γ, ε, α) defines the class"),
 au("c-tipos", ORG("Kinds of <b>antibody variation</b>:<br>- {{c1::isotypes}}: same in the whole species<br>- {{c2::allotypes}}: differ between individuals<br>- {{c3::idiotypes}}: differ within one individual"),
    G(1, 2, 3), C_, "Isotipos, alotipos, idiotipos", "12; 2", "central", NAO, EP, "Verde: lâmina 12; objetivo 2.",
    extra="- Isotypes are the classes and subclasses; allotypes are allelic variants; idiotypes are variable regions<br>- Repeated transfusions can immunize a patient against donor allotypes"),
 sh(1791629588272, "azul", C_, "Idiotipo no Fab", "12", "Azul: lâmina 12; viva na aula 49."),
 sh(1791629588447, "azul", C_, "Isotipo no Fc", "12", "Azul: lâmina 12; viva na aula 49."),
 # D — propriedades e classes (13–15)
 au("d-cdr", "The <b>antigen-binding site</b> is formed by small loops of the variable regions called {{c1::complementarity-determining regions}} (CDRs)",
    G(1), D_, "CDR", "13", "central", NAO, EP, "Verde: lâmina 13; transcrição.",
    extra="- Changing a few CDR amino acids changes specificity"),
 au("d-fc", ORG("<b>Antibody</b> functions by region:<br>- Fab alone: {{c1::neutralization}} of viruses and toxins, block of adherence<br>- Fc: {{c2::opsonization}}, {{c3::complement}} activation, transport across epithelia, cell activation"),
    G(1, 2, 3), D_, "Funções do Fc", "13; provas 2017 P3 5.2 e 2024 P3 3.2", "prova", NAO, EP, "Verde: lâmina 13; provas 2017 e 2024."),
 au("d-graves", "In {{c1::Graves}} disease, <b>antibodies</b> stimulate the TSH receptor and drive the thyroid independently of the pituitary",
    {1: R}, D_, "Anticorpo que ativa célula", "13", "lateral", NAO, EP, "Rosa: exemplo clínico da transcrição (revisão 15/10).",
    extra="- Hyperthyroidism results"),
 sh(1791629591646, "verde", D_, "IgM pentâmero", "14", "Verde: lâmina 14; viva na aula 49."),
 au("d-igm", "Early in the response, pentameric <b>IgM</b> binds even with low affinity because of its high {{c1::avidity}}, and it activates complement strongly",
    G(1), D_, "IgM: avidez e complemento", "14", "central", NAO, EP, "Verde: lâmina 14; transcrição.",
    extra="- Ten binding sites act like ten hands"),
 au("d-igg", "<b>IgG</b> dominates the mature response because it opsonizes directly, diffuses into tissues and has a long {{c1::half-life}} in serum",
    {1: Z}, D_, "Por que IgG na resposta madura", "14", "central", NAO, EP, "Azul: lâmina 14; transcrição.",
    duplicacao_ok="ganho: vantagens da IgG; sh cobre a placenta", extra="- Memory responses rely mainly on IgG"),
 sh(1791629597298, "verde", D_, "IgG atravessa a placenta", "14", "Verde: lâmina 13–14; viva na aula 49."),
 ak("ak-igg-soro", 1487117169828, G(1), D_, "IgG é a mais abundante no soro", "14", "Verde: transcrição."),
 au("d-ige", "Bound to <b>mast cells</b>, {{c1::IgE}} triggers immediate defensive reactions such as sneezing, coughing and expulsion of worms",
    G(1), D_, "IgE", "14", "central", NAO, EP, "Verde: lâmina 14; transcrição.",
    extra="- Because it sits on mast cells, little IgE circulates; it was discovered through allergy"),
 au("d-iga", "On <b>mucosae</b>, where inflammation would be harmful, the body uses the anti-inflammatory {{c1::IgA}}, the antibody it produces in greatest amount",
    G(1), D_, "IgA anti-inflamatória", "14", "central", NAO, EP, "Verde: lâmina 14; transcrição.",
    extra="- It neutralizes and blocks adherence without starting inflammation"),
 sh(1791629596747, "azul", D_, "IgA atravessa o epitélio: cadeia J + receptor poli-Ig", "14; prova (IgA chega à luz intestinal)", "Azul: prova imuno-03 (como a IgA alcança a luz); viva na aula 49. Revisão 15/10."),
 sh(1791629587397, "azul", D_, "IgM e IgD no B naive", "15", "Azul: lâmina 15 (IgD como receptor); viva na aula 49."),
 au("d-avidez", "Changing <b>antibody class</b> does not change specificity or affinity, but it does change {{c1::avidity}}",
    G(1), D_, "Classe muda avidez, não afinidade", "15", "central", NAO, EP, "Verde: lâmina 15 e transcrição ('guardem isso').",
    extra="- Affinity is per binding site; avidity is the overall strength of the molecule",
    duplicacao_ok="ganho: regra geral sobre classe; d-igm cobra a IgM"),
 # E — diversidade (16–17)
 au("e-jerne", "<b>Jerne</b> proposed, and Tonegawa proved, that receptor diversity arises by {{c1::somatic}} rearrangement in lymphocytes rather than from ready-made germline genes",
    {1: Z}, E_, "Geração somática", "16", "central", NAO, EP, "Azul: lâmina 16; transcrição.",
    extra="- Nobel prizes: Jerne 1984, Tonegawa 1987"),
 ak("ak-tcr-mhc", 1486952617561, G(1), E_, "TCR reconhece peptídeo no MHC", "17", "Verde: lâmina 17; transcrição (TCR restrito pelo MHC)."),
 au("e-tcr", "<b>T-cell receptors</b> are generated by the same {{c1::recombination}} mechanism as antibodies, but recognize antigen only when presented by MHC",
    {1: Z}, E_, "TCR: mesma geração de diversidade", "17; 18", "central", NAO, EP, "Azul: lâminas 17–18.",
    duplicacao_ok="ganho: o TCR usa o mesmo mecanismo; ak-tcr-mhc cobra o MHC", extra="- Unlike antibodies, TCRs are never secreted"),
]
SEM_IMAGEM = "fato imunológico sem estrutura a reconhecer em imagem"
for c in CARDS:
    if c["kind"] in ("text", "autoral") and "<img" not in c.get("text", "") + c.get("extra", "") + c.get("extra_add", ""):
        c["sem_imagem"] = SEM_IMAGEM
VERSO = {"a-memoria": "- Mice immunized with attenuated X survive virulent X weeks later: memory", "ak-pepsina": "- Pepsin cuts below the hinge, so F(ab′)2 binds two antigens",
         "d-fc": "- These functions depend on the heavy-chain constant region", "ak-igg-soro": "- IgA is produced in greater amount but is secreted onto mucosae",
         "ak-tcr-mhc": "- That is why the T-cell receptor was so hard to find"}
DUPLICACAO = {}
for c in CARDS:
    k = c["key"]
    if VERSO.get(k):
        if c["kind"] == "autoral":
            c["extra"] = (c["extra"] + "<br>" if c["extra"] else "") + VERSO[k]
        else:
            c["extra_add"] = VERSO[k] + ("<br>" + c["extra_add"] if c.get("extra_add") else "")
IMAGENS_VISTAS = {}
REVISAO = {}
ESCOPO = {
 "objetivo": "Descrever as características da resposta adquirida (especificidade, memória, humoral × celular), os anticorpos (gamaglobulinas, Fab/Fc, isotipos/alotipos/idiotipos, CDR, funções por classe) e a troca de classes como pista da recombinação somática que gera BCR e TCR.",
 "centrais": [
   ("imunidade adquirida", "a-memoria", "a-humoral", "a-b-direto"),
   ("anticorpos no soro", "b-gama", "sh-1792029316961", "b-dreyer", "b-troca", "sh-1792029321811"),
   ("estrutura", "ak-papaina", "ak-pepsina", "sh-1791629588145", "c-leves", "c-tipos", "sh-1791629588272", "sh-1791629588447"),
   ("classes e funções", "d-cdr", "d-fc", "d-graves", "sh-1791629591646", "d-igm", "d-igg", "sh-1791629597298", "ak-igg-soro", "d-ige", "d-iga", "sh-1791629596747", "sh-1791629587397", "d-avidez"),
   ("diversidade", "e-jerne", "ak-tcr-mhc", "e-tcr"),
 ],
 "exemplos": ["camundongos e bactérias atenuadas", "mieloma múltiplo", "doença de Graves", "Jerne e Tonegawa"],
 "outras_aulas": [("recombinação", "18"), ("ativação de B", "49"), ("MHC", "20")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
# Ajuste 15/10 noite (F-20261015-CLAUDE-05): Abbas Básica cap. 4 (receptores antigênicos: anticorpos) lido; apostila guia Aula 3 e
# monitoria P1 aula 3 conferidas (itens de seleção/recombinação da monitoria entram associados às aulas 18/45/49, rosa).
_M3 = "Ajuste 15/10 noite (F-20261015-CLAUDE-05)."
_MON = "Rosa: monitoria P1 aula 3 (recapitulação de seleção e recombinação); viva em outra aula. " + _M3
CARDS += [
 sh(1791625425082, "rosa", A_, "Só 5–10% dos timócitos sobrevivem", "3", _MON),
 sh(1791625423932, "rosa", A_, "AIRE expõe antígenos próprios no timo", "3", _MON),
 sh(1791625434632, "rosa", A_, "Treg natural (FOXP3) nasce no timo", "3", _MON),
 sh(1791629587897, "rosa", A_, "Edição do receptor do B", "3", _MON),
 sh(1791629589372, "rosa", A_, "RAG1 e RAG2 recombinam os genes", "3", _MON),
 au("b-cinetica", "In a <b>primary response</b> antibodies appear only after about {{c1::10–12 days}}, whereas a secondary response produces IgG within about 3 days",
    {1: R}, B_, "Cinética primária × secundária", "10", "lateral", NAO, EP, "Rosa: apostila guia Aula 3 cap. 2. " + _M3,
    extra="- Memory B cells that already switched class explain the speed"),
 sh(1791629598047, "azul", B_, "IgG domina a resposta secundária", "10", "Azul: apostila guia Aula 3 cap. 3 (resposta secundária). " + _M3),
 au("c-isotipo", "The <b>antibody class</b>, or isotype, is defined by the constant region of the {{c1::heavy::heavy/light}} chain",
    G(1), C_, "Cadeia pesada define a classe", "11; 12", "central", "AnKing não tem a regra geral (só isotipo no Fc); 15/10 noite.", EP, "Verde: Abbas cap. 4 e apostila guia Aula 3 cap. 2. " + _M3,
    extra="- The five heavy chains are μ, δ, γ, ε and α"),
 au("c-dominio-ig", "<b>Antibody chains</b> fold into repeated {{c1::immunoglobulin domains}}, β-sheet units also found in TCR, MHC and adhesion molecules",
    {1: R}, C_, "Domínio de Ig e superfamília", "11", "lateral", NAO, EP, "Rosa: lâmina 11 (domínios) e Abbas cap. 4. " + _M3,
    extra="- A light chain has one V and one C domain; a heavy chain has one V and three or four C domains"),
 sh(1791629590722, "rosa", C_, "Região de dobradiça", "11", "Rosa: lâmina 11 e Abbas cap. 4 (região de junção dá flexibilidade aos Fab). " + _M3),
 au("c-membrana", "The same <b>antibody</b> exists as a membrane BCR, anchored by the end of its {{c1::heavy}} chain, or as a secreted protein",
    {1: Z}, C_, "Forma de membrana × secretada", "13", "central", NAO, EP, "Azul: Abbas cap. 4 e apostila guia Aula 3 cap. 2. " + _M3,
    extra="- Light chains never anchor to the membrane; the TCR exists only on the membrane"),
 au("c-igab", "<b>Membrane Ig</b> has a tiny cytoplasmic tail, so B-cell receptor signals are carried by the associated chains {{c1::Igα and Igβ}}",
    {1: Z}, C_, "Igα e Igβ sinalizam o BCR", "13", "central", "consultas Igα/CD79 sem card (15/10 noite).", EP, "Azul: Abbas cap. 4 (complexo BCR). " + _M3,
    extra="- On T cells, CD3 plays the same role for the TCR"),
 au("c-cdr3", "Of the three hypervariable loops in each <b>variable region</b>, {{c1::CDR3}} is the most variable and contributes most to antigen binding",
    {1: Z}, C_, "CDR3", "13", "central", "consulta CDR3 sem card (15/10 noite).", EP, "Azul: Abbas cap. 4 e apostila guia Aula 3 cap. 2. " + _M3,
    extra="- It lies at the junction where gene segments were joined"),
 sh(1792029316710, "azul", C_, "Epítopo", "13", "Azul: Abbas cap. 4; viva na 18. " + _M3),
 au("c-conformacional", "<b>Antibodies</b> bind linear epitopes and also {{c1::conformational}} epitopes, formed by the folded shape of a protein",
    {1: Z}, C_, "Epítopo linear × conformacional", "13", "central", NAO, EP, "Azul: Abbas cap. 4. " + _M3,
    extra="- T cells see only linear peptides, since the protein is cut up before presentation"),
 ak("ak-afinidade", 1487117112350, {1: V}, D_, "Afinidade", "15", "Verde: lâmina 15 (afinidade × avidez) e Abbas cap. 4. " + _M3,
    extra_add="- Avidity is the total binding strength of all sites of one molecule"),
 ak("ak-valencia", 1487117108862, {1: V}, D_, "Valência", "15", "Verde: Abbas cap. 4 (IgG 2, IgA 4, IgM 10 sítios); HY 1. " + _M3,
    extra='<b>Avidity</b> refers to the <u>overall strength</u> of <u>all interactions combined</u> and is <u>dependent on</u>:<div>- <b>Affinity</b></div><div>- <b>Valence</b></div><div>- <b>Structural arrangement of all the parts</b></div><div><br><div>- e.g., IgM typically has a lower affinity than IgG, but a higher avidity due to more possible binding sites (10 binding sites)</div></div><br>- IgG has 2 binding sites, dimeric IgA 4 and pentameric IgM 10'),
 au("d-reacao-cruzada", "Binding of an <b>antibody</b> to a structurally similar epitope on a different antigen is called {{c1::cross-reaction}}",
    {1: Z}, D_, "Reação cruzada", "15", "central", NAO, [1484704852145, 1480564052470], "Azul: Abbas cap. 4. " + _M3,
    extra="- Example: antistreptococcal antibodies that bind heart myosin in rheumatic fever"),
 sh(1791629591820, "azul", D_, "IgA dímero com cadeia J", "14", "Azul: apostila guia Aula 3 cap. 2 (IgA dímero nas mucosas). " + _M3),
]
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
CARDS.append(au("a-selecao-clonal", "Only the <b>lymphocyte</b> whose receptor binds the antigen proliferates into a clone with that same specificity, the principle of {{c1::clonal selection}}",
    G(1), A_, "Seleção clonal (Burnet)", "5", "central", "consulta 'clonal selection' sem card do princípio (15/10 noite).", EP, "Verde: UC3.pdf p. 122 (teoria da seleção clonal, parte central da imunidade adaptativa) e bibliografia histórica (Burnet). " + _M3,
    extra="- One antigen with several epitopes selects several clones (polyclonal response)"))
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
for _c_ in CARDS:
    if _c_["key"] == "ak-pepsina": _c_["hy_repete"] = "papaína e pepsina: ak-papaina (verde) já cobra Fab/Fc; pepsina é o par"
