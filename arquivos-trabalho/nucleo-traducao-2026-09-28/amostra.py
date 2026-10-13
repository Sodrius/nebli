"""Amostra editorial local: apenas leitura Anki; não é motor de tradução/apply."""
import hashlib
import html
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent
SPECS = {
    1790347332525: (
        "Sinal clínico compreensível",
        {"Text": "Depressão persistente após pressionar uma área edemaciada caracteriza {{c1::edema com cacifo (sinal de Godet)}}."},
        "Preserva o achado e a resposta; mantém a explicação causal já existente no verso.",
    ),
    1790190268556: (
        "Mecanismo",
        {"Text": "Na inflamação, a hepcidina reduz a concentração de {{c1::ferro}} no sangue, limitando sua disponibilidade para microrganismos."},
        "Preserva a direção do efeito e sua consequência; não acrescenta um alvo à frente.",
    ),
    1790190268210: (
        "Contraste e nome científico",
        {"Text": "<i>S. aureus</i> tolera altas concentrações de sal, mas não depende delas para crescer: é {{c1::halotolerante}}."},
        "O contraste é tolerar versus exigir alta salinidade; nome científico e imagem ficam intactos.",
    ),
    1790190269338: (
        "Cloze c2 e localização numérica",
        {"Text": "Uma população bacteriana passa de 1.000 para 2.000 células em um {{c2::tempo de geração (duplicação)}}."},
        "Mantém c2; os separadores mudam, mas os valores permanecem mil e dois mil. Não cria c1.",
    ),
    1790271540358: (
        "Uma nota, quatro recuperações",
        {"Text": "As {{c1::criptas de Lieberkühn}} são {{c2::glândulas tubulares curtas entre as vilosidades}}. Suas {{c3::células-tronco multipotentes}} repõem {{c4::enterócitos}} e outras células do epitélio intestinal."},
        "Preserva c1–c4 e seus alvos. Simplificar a nota é decisão didática separada; traduzir não divide nem funde cards.",
    ),
    1790263339347: (
        "AnatoKing: pergunta e identificação",
        {"Header": "Identifique a estrutura destacada", "Text": "{{c1::Estômago}}"},
        "Traduz Header e resposta; não altera imagem, máscara, identidade ou modelo. Não promove a representante verde.",
    ),
}


def read_anki(action, params):
    if action not in {"notesInfo", "cardsInfo"}:
        raise ValueError("Somente leitura")
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    req = urllib.request.Request("http://127.0.0.1:8765", data=payload)
    with urllib.request.urlopen(req, timeout=20) as response:
        result = json.load(response)
    if result["error"]:
        raise RuntimeError(result["error"])
    return result["result"]


def main():
    if (BASE / "amostra.json").exists():
        raise SystemExit("Amostra já existe; não sobrescrever a base histórica desta execução.")
    notes = read_anki("notesInfo", {"notes": list(SPECS)})
    cards = read_anki("cardsInfo", {"cards": [cid for n in notes for cid in n["cards"]]})
    rows = []
    for note in notes:
        title, proposed, decision = SPECS[note["noteId"]]
        before = {k: v["value"] for k, v in note["fields"].items()}
        for field, translated in proposed.items():
            # Só confere os marcadores simples desta amostra, não clozes gerais.
            assert re.findall(r"\{\{c(\d+)::", before[field]) == re.findall(r"\{\{c(\d+)::", translated)
            assert re.findall(r"<img[^>]+>", before[field]) == re.findall(r"<img[^>]+>", translated)
        rows.append({
            "note_id": note["noteId"], "model_name": note["modelName"],
            "card_ids": note["cards"], "case": title,
            "card_map": [{"card_id": c["cardId"], "ordinal": c["ord"]} for c in cards if c["note"] == note["noteId"]],
            "nebli_base_fields": before,
            "base_fields_hash": hashlib.sha256(json.dumps(before, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
            "proposed_fields": proposed, "decision": decision,
            "change_kind": "translation", "state": "draft",
            "review": {
                "language": "leitura editorial efetuada",
                "structure": "marcadores simples e mídia preservados; geração no Anki não testada",
                "visual": "comparação estática, não renderização do template Anki",
                "scientific": "sem revisão bibliográfica integral nesta amostra",
            },
        })
    artifact = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "amostra local, somente leitura; não aplicada",
        "notes": len(notes), "cards": len(cards), "rows": rows,
    }
    (BASE / "amostra.json").write_text(json.dumps(artifact, ensure_ascii=False, indent=2))
    sections = []
    for row in rows:
        def display(value):
            # Escapa o HTML da origem: comparação textual, sem scripts herdados.
            value = re.sub(r"<[^>]+>", "", value)
            return re.sub(r"\{\{c(\d+)::([^{}]+)\}\}", r'<mark title="c\1">\2</mark>', html.escape(value))
        before = row["nebli_base_fields"]
        source = "".join("<p>" + display(before[k]) + "</p>" for k in row["proposed_fields"])
        target = "".join("<p>" + display(v) + "</p>" for v in row["proposed_fields"].values())
        sections.append(
            "<section><h2>" + html.escape(row["case"]) + "</h2><small>Nota " + str(row["note_id"]) +
            '</small><div class="pair"><div><h3>Texto atual</h3>' + source +
            "</div><div><h3>Proposta PT-BR</h3>" + target + "</div></div><p>" +
            html.escape(row["decision"]) + "</p></section>"
        )
    page = '''<!doctype html><html lang="pt-BR"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NEBLI · amostra de tradução</title><style>
body{margin:0;background:#f4f5f7;color:#202938;font:17px/1.6 system-ui}
main{max-width:1050px;margin:auto;padding:24px}h1{line-height:1.2}
h2{font-size:20px;margin:0}h3{font-size:14px;color:#566379}
section{background:white;border:1px solid #d7dfe7;border-radius:12px;padding:24px;margin:24px 0}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:28px}.pair>div{min-width:0}
mark{background:#dcebf8;color:#163654;padding:1px 3px;border-radius:3px}
@media(max-width:600px){main{padding:16px}section{padding:16px}.pair{grid-template-columns:1fr;gap:0}}
</style><main><h1>Tradução que preserva a pergunta</h1>
<p>Seis notas reais, nove cards. Comparação editorial local; nenhuma alteração aplicada ao Anki.
Os destaques mostram respostas abertas para conferir significado. Esta página não reproduz os templates de estudo nem as imagens.</p>
''' + "".join(sections) + "</main></html>"
    (BASE / "amostra.html").write_text(page)
    (BASE / "render-jobs.json").write_text(json.dumps([
        {"name": "amostra-desktop", "html": "amostra.html", "width": 1100},
        {"name": "amostra-mobile", "html": "amostra.html", "width": 390},
    ]))
    print(json.dumps({"notes": len(notes), "cards": len(cards), "anki_writes": 0, "output": str(BASE / "amostra.html")}))


if __name__ == "__main__":
    main()
