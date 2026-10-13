"""Busca de candidatos: q.py "<termos Anki>" ... (AnKing Step por padrão; prefixo EXT: para Referências Externas)."""
import html, re, sys
sys.path.insert(0, "/Users/davisousa/NEBLI")
from nebli.decks import Anki
A = Anki()
st = lambda s: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()
for q in sys.argv[1:]:
    deck = '"deck:Referências::Referências Externas*"' if q.startswith("EXT:") else '"deck:Referências::Anking Step Deck*"'
    q = q.removeprefix("EXT:")
    ids = A("findNotes", query=f"{deck} {q}")
    print(f"### {q} -> {len(ids)}")
    for n in A("notesInfo", notes=ids[:14]):
        f = n["fields"]; t = f.get("Text", f.get("Front", {"value": ""}))["value"]
        live = A("findNotes", query=f'"tag:NEBLI::source::nid-{n["noteId"]}"')
        print(n["noteId"], "IMG" if "<img" in f.get("Extra", {"value": ""})["value"] else "   ", "NEBLI!" if live else "", st(t)[:210])
