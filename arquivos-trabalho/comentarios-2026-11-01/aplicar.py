"""Rodada de comentários 01/11 (F-20261101-CLAUDE-04): correções, bandeiras, comandos e marcas, numa escrita só."""
import base64
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))
from nebli.decks import Anki, escrita, em_tela  # noqa: E402

AQUI = Path(__file__).resolve().parent
IMG = Path("/private/tmp/claude-501/-Users-davisousa/e83cc7a6-ca8e-4f3e-bd70-793b69cb23f9/scratchpad/img")
DATA = "01, 11, 26."
FLAG = {"verde": 3, "azul": 4, "rosa": 5}
RANK = {3: 3, 4: 2, 5: 1}

CAMPOS = {
    1791575026669: {"Text": "During swallowing, the <b>upper esophageal sphincter</b> {{c1::relaxes}} just before the pharyngeal peristaltic wave arrives, and its resting tone keeps {{c2::air}} out of the esophagus",
                    "Extra": "At rest it stays closed at about 40 mmHg.<br>It closes again after the bolus passes, which prevents reflux into the pharynx."},
    1791575032019: {"Text": "Conditions that cause {{c1::vomiting}} include <b>infection</b>, <b>medication</b>, <b>vestibular dysfunction</b> and <b>chemoradiation</b>",
                    "Extra": "Drugs and chemoradiation act on the area postrema.<br>Motion sickness comes through the vestibular system.<br>Stomach distension signals through vagal afferents."},
    1791630175095: {"Text": "When <b>CRISPR/Cas9</b> makes a <u>double-strand break</u> to <b>knock out</b> a gene, the cell repairs it by error-prone {{c1::nonhomologous end joining}}",
                    "Extra": "The small insertions and deletions it leaves disrupt the reading frame, so the gene is lost.<br>A Cas9 nickase making paired single-strand breaks favors homology-directed repair, which is precise.<br><br><div><img src=\"fd83418325844d4377263dff87454648.jpg\" width=\"644\"></div>"},
    1792175889534: {"Text": "<div data-nebli-organizacao=\"true\">Clinical forms of <b>sporotrichosis</b>:<br>- from a skin wound: {{c1::lymphocutaneous::L…}} (most common) and {{c1::fixed cutaneous::F…}}<br>- beyond the skin: {{c2::pulmonary::P…}} after inhalation and {{c2::disseminated::D…}} in the immunocompromised</div>",
                    "Extra": "Lymphocutaneous: ulcer at the wound and nodules climbing the lymphatics. Fixed: the lesion stays at the inoculation site.<br><img src=\"mb48-esporotricose-linfocutanea.png\" width=\"360\">"},
    1792695055212: {"Extra": "Cell fusion spreads infection directly, without free virions. Naked virions usually leave by lysis, with exceptions.<br>The figure shows an enveloped capsid acquiring membrane with viral envelope proteins as it buds.<br><img src=\"mb58-brotamento-slide239-20261101.png\" style=\"width:100%;max-width:420px;height:auto;display:block;margin:18px auto\">"},
    1792695056243: {"Extra": "HA binds sialic acid during attachment. NA cleaves it after budding, so new particles do not stay stuck to the cell; oseltamivir blocks this step.<br><img src=\"mb58-na-slide134-20261101.png\" style=\"width:100%;max-width:900px;height:auto;display:block;margin:18px auto\">"},
    1792713410554: {"Extra": "Paraumbilical veins carry portal blood near the umbilicus. Superficial epigastric veins drain the abdominal wall into the systemic circulation.<br><img src=\"an11-anastomoses-moore-recorte-20261027.png\" style=\"width:100%;max-width:700px;height:auto;display:block;margin:18px auto\">"},
    1784308054074: {"Text": "Em <b>dolicocefalia</b>, dolico- indica {{c1::longo}}.",
                    "Extra": "Dolicocefalia é o crânio proporcionalmente alongado. O oposto é braquicefalia (braqui- = curto)."},
    1784308062198: {"Text": "Em <b>atrofia</b> e <b>hipertrofia</b>, -trofia indica {{c1::desenvolvimento}} do tecido.",
                    "Extra": "Do grego <i>trophḗ</i>, nutrição: o tecido nutrido se desenvolve.<br>Hipertrofia é o aumento do tamanho das células; atrofia é a redução."},
    1784308062300: {"Text": "Em <b>espirometria</b>, -metria indica {{c1::medição}}.",
                    "Extra": "A espirometria mede volumes e fluxos respiratórios. O aparelho leva -metro: espirômetro."},
    1784308070835: {"Text": "Em <b>balanite</b>, balan/o indica {{c1::glande}}.",
                    "Extra": "Balanite é a inflamação da glande (-ite = inflamação)."},
    1791023352068: {"Text": "On the <b>tongue</b>, papillae scattered among the filiform ones, with taste buds on their upper surface, are the {{c1::fungiform}} papillae"},
    1791625427358: {"Text": "<u>Antigen loading</u> onto <b>MHC II</b> occurs after release of the {{c2::invariant chain}} in an <u>acidified</u> {{c1::endosome}}",
                    "Extra": "<img src=\"9c1606051a9932a7bca3218fbee13935.webp\" style=\"width:100%;max-width:640px;height:auto\"><br><br>The invariant chain is made with MHC II in the ER and blocks its groove.<br>In the acidified endosome it is cut down to CLIP, which HLA-DM swaps for a peptide."},
    1791625435907: {"Text": "<b>Tregs</b> barely make their own growth factor, so they <b>survive</b> on {{c1::IL-2}} secreted by activated conventional T cells",
                    "Extra": "FOXP3 blocks IL-2 production in the Treg.<br>Its high CD25 (IL-2 receptor α) captures IL-2 and also deprives effector T cells of it."},
    1791631346241: {"Text": "{{c1::DNA methyltransferases}} use S-adenosylmethionine (SAM) to methylate cytosine at <b>CpG sites</b>, helping establish or maintain <b>transcriptional silencing</b>"},
    1792659587475: {"Text": "<div data-nebli-organizacao=\"true\">The <b>septum transversum</b>, the mesoderm plate below the heart:<br>- is invaded by the growing {{c1::liver}} bud<br>- forms, in its cranial part, the central tendon of the {{c2::diaphragm}}</div>"},
    1792695061296: {"Text": "<b>Non-nucleoside reverse transcriptase inhibitors</b> (NNRTIs) bind an {{c1::allosteric}} pocket of <b>HIV</b> reverse transcriptase, unlike the nucleoside analogs (NRTIs)",
                    "Extra": "<img src=\"3689cb1f06f28b3972651aabff448e06.webp\" style=\"width:100%;max-width:620px;height:auto\"><br><br>NRTIs need phosphorylation and end the DNA chain. NNRTIs need no activation and act only on HIV-1."},
    1791762412899: {"Text": "Once nitric oxide diffuses into muscle cells, it activates soluble (cytosolic) guanylyl cyclase, which converts GTP to {{c1::cGMP}}"},
}
CORRIGIDO = [1790974690103, 1790999271207, 1791557943483, 1791575026669, 1791575032019, 1791627549276, 1791627549652,
             1791630173920, 1791630174545, 1791630175095, 1791630179520, 1791630905957, 1791762422823, 1791983680358,
             1792175889534, 1792624462025, 1792695055212, 1792695055643, 1792695056243, 1792713410554, 1792787428653,
             1793472242503]
VISTO = [1791625431383, 1791627547602, 1791826286795, 1792081423941, 1792588686955, 1792659592051, 1792713394868,
         1792713404156, 1793199677933]
RETIRAR = {1792176893657: "NEBLI::retirado::sem-ganho-comentario"}  # pista geográfica dos EUA; morcego/ave já em 1791630905344
MIDIA = ["mb58-brotamento-slide239-20261101.png", "mb58-na-slide134-20261101.png"]


def main():
    A = Anki()
    rodada = json.loads((AQUI / "RODADA.json").read_text(encoding="utf-8"))
    nids = sorted({i["nid"] for i in rodada["itens"]} | set(CAMPOS))
    antes = A("notesInfo", notes=nids)
    (AQUI / "backup-antes-aplicar.json").write_text(json.dumps(antes, ensure_ascii=False, indent=1), encoding="utf-8")
    por = {n["noteId"]: n for n in antes}
    recibo = {"campos": [], "bandeiras": [], "comandos": [], "marcas": [], "retirados": [], "pulados": []}
    with escrita(A, "rodada de comentários 01/11 (sete passos)", sync=False):
        tela = set(em_tela(A))
        for m in MIDIA:
            A("storeMediaFile", filename=m, data=base64.b64encode((IMG / m).read_bytes()).decode())
        for nid in nids:
            if nid in tela:
                recibo["pulados"].append(nid); continue
            n = por[nid]
            if nid in CAMPOS:
                f = {k: v for k, v in CAMPOS[nid].items() if k in n["fields"]}
                A("updateNoteFields", note={"id": nid, "fields": f}); recibo["campos"].append(nid)
                cards = A("cardsInfo", cards=A("findCards", query=f"nid:{nid}"))
                principal = next(c["deckName"] for c in cards if c["ord"] == 0)
                novos = [c for c in cards if c["cardId"] not in n["cards"]]
                if novos:  # cartão de lacuna nova: mesmo deck e mesma suspensão do primeiro
                    A("changeDeck", cards=[c["cardId"] for c in novos], deck=principal)
                    if all(c["queue"] == -1 for c in A("cardsInfo", cards=n["cards"])):
                        A("suspend", cards=[c["cardId"] for c in novos])
            if nid in RETIRAR:
                A("addTags", notes=[nid], tags=RETIRAR[nid])
                A("suspend", cards=n["cards"]); recibo["retirados"].append(nid)
            cores = [FLAG[t.split("::")[-1]] for t in n["tags"] if t.startswith("NEBLI::cor::") and t.split("::")[-1] in FLAG]
            volta = max(cores, key=RANK.get) if cores else 0
            for c in A("cardsInfo", cards=n["cards"]):
                if c["flags"] == 1:
                    A("setSpecificValueOfCard", card=c["cardId"], keys=["flags"], newValues=[volta], warning_check=True)
                    recibo["bandeiras"].append({"card": c["cardId"], "para": volta})
            cmd = [t for t in n["tags"] if t.startswith("NEBLI::comando::")]
            if cmd:
                A("removeTags", notes=[nid], tags=" ".join(cmd)); recibo["comandos"].append({"nid": nid, "tags": cmd})
            if "NEBLI_Comentario" in n["fields"]:
                marca = "VISTO" if nid in VISTO else "CORRIGIDO"
                atual = n["fields"]["NEBLI_Comentario"]["value"].rstrip()
                novo = (atual + ("<br>" if atual else "") + f"{marca}, {DATA}")
                A("updateNoteFields", note={"id": nid, "fields": {"NEBLI_Comentario": novo}})
                recibo["marcas"].append({"nid": nid, "marca": marca})
    (AQUI / "recibo-aplicar.json").write_text(json.dumps(recibo, ensure_ascii=False, indent=1), encoding="utf-8")
    print({k: len(v) for k, v in recibo.items()}, "pulados:", recibo["pulados"])


if __name__ == "__main__":
    main()
