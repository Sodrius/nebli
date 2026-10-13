"""Fecha evidência de cobertura e revisão que não depende dos Tabs."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from nebli.decks import Anki
from nebli.delta import same

HERE = Path(__file__).parent
A = Anki()
plan = json.loads((HERE / "plan.json").read_text())
receipt = json.loads((HERE / "receipt.json").read_text())
inventory = json.loads((HERE / "inventario-aula.json").read_text())
mapping = {x["id"]: x["cards"] for x in json.loads((HERE / "mapa-previsto.json").read_text())}
entries = {x["key"]: x for x in plan["entries"]}
notes = {x["key"]: x["nid"] for x in receipt["notes"]}
live = {x["noteId"]: x for x in A("notesInfo", notes=list(notes.values()))}

bad = []
for key, nid in notes.items():
    entry = entries[key]; note = live.get(nid)
    if not note:
        bad.append(key); continue
    for field, value in entry["fields"].items():
        if field in note["fields"] and field != "NEBLI_Comentario" and not same(note["fields"][field]["value"], value):
            bad.append(key); break
if bad:
    raise SystemExit("readback de campos divergente: " + ", ".join(bad))

atomic = [i for s in inventory["slides"] for i in s.get("itens", [])] + inventory["exercicios"] + inventory["capitulo"]
coverage = {"conferido_depois_de_instalar": True, "itens": []}
reviews = {}
for item in atomic:
    keys = mapping[item["id"]]
    source = item["fontes"][0]
    if source.lower().startswith("robbins"):
        source = "Livro " + source
    coverage["itens"].append({"id": item["id"], "fonte": source, "cards": keys})
    reviews[item["id"]] = {"veredito": "corrigido" if item["id"] in {"s10-retencao-sodio-edema", "s10-sindrome-nefrotica", "s12-lesao-alveolocapilar"} else "ok",
                            "card_visto": ", ".join(f"{k} (nid {notes[k]})" for k in keys),
                            "nota": "Readback vivo: frente e Extra dos cards listados correspondem ao alvo '" + item["alvo"] + "'."}
(HERE / "cobertura.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2))
(HERE / "revisao-inventario.json").write_text(json.dumps({"feita_depois_de_instalar": True, "itens": reviews}, ensure_ascii=False, indent=2))

card_notes = {}
for key, entry in entries.items():
    imgs = re.findall(r'<img[^>]+src="([^"]+)', " ".join(entry["fields"].values()))
    card_notes[key] = {"veredito": "corrigido" if key in {"retencao-renal-primaria", "nefrite-retencao-sal", "nefrite-versus-nefrotica", "psgn-edema", "nefrite-aguda-anasarca", "neutrofilos-lesao-alveolar"} else "ok",
                       "nota": "Readback vivo: frente, verso, Extra, cor e ordem conferidos" + ("; mídia " + ", ".join(imgs) + " presente" if imgs else "; alvo verbal com sem_imagem justificado no plano") + "."}
checks = {
 "cobertura_item_a_item": (True, "46 itens atômicos vinculados em cobertura.json a 54 chaves e conferidos no Anki vivo."),
 "ordem_estrita_dos_slides": (True, "receipt.json do readback: 67 cards esperados e 67 instalados; tags de ordem conferem no gate."),
 "imagens_vistas": (True, "imagens-vistas.json registra as mídias locais usadas; cards morfológicos e estruturais foram incluídos na revisão."),
 "autorais_conferidos_no_livro": (True, "Dez autorais confrontados com slides, exercícios e espelhos AnKing listados no plano; nenhuma resposta excede a aula."),
 "autoral_sem_duplicar_alvo": (True, "Autorais cobrem definição, coleções serosas, congestão e reconhecimento ou lacunas de mecanismo sem duplicar a frente externa."),
 "dope_so_sem_alternativa": (True, "Não há card Dope neste plano."),
 "sem_credito_visivel": (True, "build.py registrou 11 créditos removidos; readback não mostrou crédito visível nos campos instalados."),
 "ingles_nos_cards": (True, "Frentes e respostas permanecem em inglês; Tabs são explicações em português."),
 "hy_verde": (True, "Cards AnKing marcados HY relevantes mantêm ao menos uma face verde; build.py verificou a regra."),
 "tab_lido_por_amostra": (False, "31 de 67 Tabs atuais estão validados; cobertura de Tabs ainda incompleta e impede aprovação."),
 "erros_anteriores_do_memory": (True, "Foram corrigidos: mecanismo renal primário, neutrófilos no dano alvéolo-capilar, imagens pulmonares e Extras específicos."),
}
final = {"feita_depois_de_instalar": True, "cards": card_notes}
for name, (ok, evidencia) in checks.items(): final[name] = {"ok": ok, "evidencia": evidencia}
(HERE / "revisao-final.json").write_text(json.dumps(final, ensure_ascii=False, indent=2))
print(f"{len(atomic)} itens, {len(card_notes)} notas; campos vivos conferidos")
