"""Rodada 01/11 (b), passo 2: organizadores com uma lacuna por cartão → um índice só (pedido "MAIS CLOZES POR VEZ")."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki, escrita, em_tela
AQUI = Path(__file__).resolve().parent
ORG = '<div data-nebli-organizacao="true">'
T = {
 1791985037727: ORG + "Main causes of <b>chronic inflammation</b>:<br>- persistent {{c1::infections::i…}}<br>- prolonged exposure to {{c1::toxic agents::t…}}<br>- {{c1::immune-mediated::i…}} diseases (autoimmunity, allergy)</div>",
 1792064618158: ORG + "Main <b>superficial mycoses</b> (agent):<br>- {{c1::pityriasis versicolor::p…}} (Malassezia)<br>- {{c1::black piedra::b…}} (Piedraia hortae)<br>- {{c1::white piedra::w…}} (Trichosporon)<br>- {{c1::tinea nigra::t…}} (Hortaea werneckii)</div>",
 1792588686967: ORG + "<b>Via eferente visceral</b> (autônoma):<br>- neurônio pré-ganglionar: corpo no {{c1::SNC::S…}}<br>- sinapse no {{c1::gânglio autônomo::g…}}<br>- neurônio pós-ganglionar: do gânglio ao {{c1::órgão efetor::ó…}}</div>",
 1792713388228: ORG + "<b>Lobos anatômicos do fígado</b>:<br>{{c1::Direito::D…}}<br>{{c1::Esquerdo::E…}}<br>{{c1::Caudado::C…}}<br>{{c1::Quadrado::Q…}}</div>",
 1792713403703: ORG + "<b>Trajeto da bile</b>:<br>Ductos hepáticos direito e esquerdo<br>Ducto {{c1::hepático comum::h…}} + ducto {{c1::cístico::c…}}<br>Ducto colédoco<br>{{c1::Ampola::A…}} hepatopancreática<br>Papila duodenal maior</div>",
}
A = Anki(); antes = A("notesInfo", notes=list(T))
(AQUI / "backup-similares.json").write_text(json.dumps(antes, ensure_ascii=False, indent=1))
rec = []
with escrita(A, "rodada 01/11 (b): organizadores num índice só", sync=False):
    tela = set(em_tela(A))
    for n in antes:
        if n["noteId"] in tela: rec.append({"nid": n["noteId"], "pulado": True}); continue
        A("updateNoteFields", note={"id": n["noteId"], "fields": {"Text": T[n["noteId"]]}})
        sobra = [c["cardId"] for c in A("cardsInfo", cards=n["cards"]) if c["ord"] >= 1]
        A("suspend", cards=sobra); A("addTags", notes=[n["noteId"]], tags="NEBLI::lacuna-fundida::2026-11-01")
        rec.append({"nid": n["noteId"], "sobra_suspensa": sobra})
(AQUI / "recibo-similares.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1)); print(rec)
