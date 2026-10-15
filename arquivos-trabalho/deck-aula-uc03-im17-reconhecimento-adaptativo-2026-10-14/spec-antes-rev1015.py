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
 au("a-memoria", "Mice immunized with attenuated bacterium Y still die from virulent X, showing that <b>acquired immunity</b> is {{c1::specific}}",
    G(1), A_, "Especificidade e memória", "5", "central", NAO, EP, "Verde: lâmina 5; transcrição."),
 au("a-humoral", ORG("Classic definition by <b>transfer</b>:<br>- immunity transferred by {{c1::serum}}: humoral<br>- immunity transferred only by {{c2::cells}}: cellular"),
    G(1, 2), A_, "Humoral × celular", "6; 18", "central", NAO, EP, "Verde: lâmina 6; resumo (lâmina 18).",
    extra="- Today the two overlap: humoral responses also depend on T cells"),
 au("a-b-direto", "{{c1::B cells::T or B}} recognize native antigen directly through their clonal receptors, without needing <b>antigen-presenting cells</b>",
    {1: Z}, A_, "B reconhece diretamente", "6; 4", "central", NAO, EP, "Azul: lâmina 4; transcrição.",
    extra="- T cells then decide, through their signals, whether the B cell responds"),
 # B — anticorpos no soro (7–10)
 au("b-gama", "<b>Hyperimmunization</b> raises the {{c1::gamma}}-globulin peak on serum electrophoresis, which is why antibodies were first identified as gamma-globulins",
    G(1), B_, "Anticorpos = gamaglobulinas", "7", "central", NAO, EP, "Verde: lâmina 7.",
    extra="- A normal immune response does not change the electrophoretic profile, because antibodies are made all the time"),
 sh(1792029316961, "verde", B_, "Mieloma: pico monoclonal", "8", "Verde: lâmina 8; viva na aula 18."),
 au("b-dreyer", "<b>Myeloma proteins</b> share a constant part and differ in a variable part of one chain, suggesting {{c1::two genes}} encode one polypeptide",
    {1: Z}, B_, "Dreyer e Bennett", "9", "central", NAO, EP, "Azul: lâmina 9; transcrição.",
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
 au("c-dominio", "The <b>immunoglobulin domain</b> is a fold of about {{c1::110}} amino acids that resists proteolysis",
    {1: R}, C_, "Domínio de Ig", "11", "lateral", NAO, EP, "Rosa: lâmina 11; transcrição.",
    extra="- That is why papain cuts only at the exposed hinge"),
 au("c-tipos", ORG("Kinds of <b>antibody variation</b>:<br>- {{c1::isotypes}}: same in the whole species<br>- {{c2::allotypes}}: differ between individuals<br>- {{c3::idiotypes}}: differ within one individual"),
    G(1, 2, 3), C_, "Isotipos, alotipos, idiotipos", "12; 2", "central", NAO, EP, "Verde: lâmina 12; objetivo 2.",
    extra="- Isotypes are the classes and subclasses; allotypes are allelic variants; idiotypes are variable regions<br>- Repeated transfusions can immunize a patient against donor allotypes"),
 sh(1791629588272, "azul", C_, "Idiotipo no Fab", "12", "Azul: lâmina 12; viva na aula 49."),
 sh(1791629588447, "azul", C_, "Isotipo no Fc", "12", "Azul: lâmina 12; viva na aula 49."),
 # D — propriedades e classes (13–15)
 au("d-cdr", "The <b>antigen-binding site</b> is formed by small loops of the variable regions called {{c1::complementarity-determining regions}} (CDRs)",
    G(1), D_, "CDR", "13", "central", NAO, EP, "Verde: lâmina 13; transcrição.",
    extra="- Changing a few CDR amino acids changes specificity"),
 au("d-fab", "By binding alone (<b>Fab</b>), antibodies neutralize viruses and toxins and {{c1::block adherence}} of bacteria",
    G(1), D_, "Funções do Fab", "13; prova 2017 P3 5.2", "prova", NAO, EP, "Verde: lâmina 13; prova 2017 (Fab × Fc)."),
 au("d-fc", ORG("Functions that depend on the <b>Fc</b> region:<br>- transport across epithelia (placenta, milk)<br>- {{c1::opsonization}}<br>- {{c2::complement}} activation<br>- cell activation"),
    G(1, 2), D_, "Funções do Fc", "13; provas 2017 P3 5.2 e 2024 P3 3.2", "prova", NAO, EP, "Verde: lâmina 13; provas 2017 e 2024."),
 au("d-graves", "In {{c1::Graves}} disease, <b>antibodies</b> stimulate the TSH receptor and drive the thyroid independently of the pituitary",
    {1: Z}, D_, "Anticorpo que ativa célula", "13", "central", NAO, EP, "Azul: transcrição (exemplo de ativação celular).",
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
 au("d-ige", "For <b>emergencies</b> needing violent reactions, such as coughing, sneezing or expelling worms, the body makes {{c1::IgE}}",
    G(1), D_, "IgE", "14", "central", NAO, EP, "Verde: lâmina 14; transcrição.",
    extra="- It sits bound to mast cells, so little circulates; it was discovered through allergy"),
 au("d-iga", "On <b>mucosae</b>, where inflammation would be harmful, the body uses the anti-inflammatory {{c1::IgA}}, the antibody it produces in greatest amount",
    G(1), D_, "IgA anti-inflamatória", "14", "central", NAO, EP, "Verde: lâmina 14; transcrição.",
    extra="- It neutralizes and blocks adherence without starting inflammation"),
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
         "d-fab": "- Neutralization is the term for viruses and toxins", "d-fc": "- These functions depend on the heavy-chain constant region", "ak-igg-soro": "- IgA is produced in greater amount but is secreted onto mucosae",
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
   ("estrutura", "ak-papaina", "ak-pepsina", "sh-1791629588145", "c-leves", "c-dominio", "c-tipos", "sh-1791629588272", "sh-1791629588447"),
   ("classes e funções", "d-cdr", "d-fab", "d-fc", "d-graves", "sh-1791629591646", "d-igm", "d-igg", "sh-1791629597298", "ak-igg-soro", "d-ige", "d-iga", "sh-1791629587397", "d-avidez"),
   ("diversidade", "e-jerne", "ak-tcr-mhc", "e-tcr"),
 ],
 "exemplos": ["camundongos e bactérias atenuadas", "mieloma múltiplo", "doença de Graves", "Jerne e Tonegawa"],
 "outras_aulas": [("recombinação", "18"), ("ativação de B", "49"), ("MHC", "20")],
}
import re as _re
CARDS.sort(key=lambda c: int(_re.search(r"\d+", c["evid"]).group()))
