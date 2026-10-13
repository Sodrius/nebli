"""Revisão explícita de alvos para esta corrida; produz mapa previsto antes da escrita."""
import json
from pathlib import Path

HERE = Path(__file__).parent
M = {
    "s02-definir-edema-hiperemia-congestao": ["edema", "hiperemia-ativa", "congestao"],
    "s02-nomear-colecoes-serosas": ["hidrotorax", "hidropericardio", "ascite", "anasarca"],
    "s02-explicar-mecanismos-edema": ["hidrostatica", "oncotica", "linfa-retorno", "permeabilidade-capilar-edema"],
    "s02-reconhecer-morfologia": ["morfologia-pulmonar-s09", "morfologia-pulmonar-s13", "morfologia-pulmonar-s14"],
    "s03-edema-definicao-compartimento": ["edema"],
    "s03-hiperemia-ativa": ["hiperemia-ativa"],
    "s03-congestao-passiva": ["congestao"],
    "s03-edema-depressivel": ["hidrostatica"],
    "s04-hidrostatica-filtracao": ["gradiente-hidrostatico-capilar", "filtracao"],
    "s04-oncotica-reabsorcao": ["oncotica", "reabsorcao", "gradiente-hidrostatico-capilar"],
    "s04-linfa-excedente": ["linfa-retorno"],
    "s04-gradiente-capilar": ["gradiente-hidrostatico-capilar", "filtracao", "reabsorcao"],
    "s05-hidrostatica-limitacao-fluxo": ["hidrostatica", "insuficiencia-esquerda"],
    "s05-oncotica-perda-proteina": ["sindrome-nefrotica"],
    "s05-oncotica-producao-proteina": ["cirrose-edema"],
    "s05-permeabilidade": ["permeabilidade-capilar-edema"],
    "s06-colecoes-cavitarias-macroscopia": ["hidrotorax", "hidropericardio"],
    "s06-edema-por-hidrostatica": ["hidrostatica", "transudato-hidrostatica"],
    "s07-anasarca": ["anasarca"],
    "s07-ascite-macroscopia": ["ascite", "ascite-portal"],
    "s08-insuficiencia-cardiaca-pressao": ["disfuncao-bomba", "insuficiencia-esquerda"],
    "s08-insuficiencia-cardiaca-raas": ["raas-insuficiencia-cardiaca", "raas-agrava-edema", "sodio-agua"],
    "s08-insuficiencia-cardiaca-edema": ["insuficiencia-esquerda", "insuficiencia-esquerda-congestao", "insuficiencia-direita"],
    "s09-edema-pulmonar-macroscopia": ["morfologia-pulmonar-s09"],
    "s09-edema-pulmonar-radiografia": ["edema-pulmonar-rx"],
    "s09-edema-pulmonar-microscopia": ["edema-pulmonar-venoso", "hipertensao-venosa-pulmonar", "morfologia-pulmonar-s13"],
    "s10-proteinuria-hipoalbuminemia": ["sindrome-nefrotica"],
    "s10-retencao-sodio-edema": ["retencao-renal-primaria", "nefrite-retencao-sal", "nefrite-versus-nefrotica"],
    "s10-sindrome-nefrotica": ["sindrome-nefrotica", "retencao-renal-primaria", "nefrite-aguda-anasarca"],
    "s11-hipertensao-portal": ["hipertensao-portal-cirrose", "vasodilatacao-esplancnica"],
    "s11-cirrose-raas-ascite": ["raas-cirrose", "ascite-portal"],
    "s11-cirrose-hipoalbuminemia": ["cirrose-edema"],
    "s12-lesao-alveolocapilar": ["lesao-alveolocapilar", "contracao-endotelial", "neutrofilos-lesao-alveolar"],
    "s12-edema-permeabilidade": ["permeabilidade-exsudato", "edema-proteico-ards", "cardiogenico-versus-permeabilidade"],
    "s12-membrana-hialina": ["membrana-hialina"],
    "s13-edema-pulmonar-histologia": ["morfologia-pulmonar-s13"],
    "s14-congestao-pulmonar-histologia": ["morfologia-pulmonar-s14"],
    "s14-extravasamento-hemacias": ["celulas-insuficiencia-cardiaca", "morfologia-pulmonar-s14"],
    "s15-morfologia-pulmonar": ["morfologia-pulmonar-s13", "morfologia-pulmonar-s14"],
    "ex-edema-inflamatorio-composicao": ["exsudato-proteina", "permeabilidade-exsudato"],
    "ex-mediadores-edema-inicial": ["histamina-permeabilidade", "bradicinina-permeabilidade", "leucotrienos-permeabilidade", "contracao-endotelial"],
    "ex-morfologia-inflamacao-aguda": ["hiperemia-ativa", "permeabilidade-exsudato"],
    "livro-transudato-exsudato": ["transudato-proteina", "exsudato-proteina"],
    "livro-linfedema": ["linfedema-obstrucao"],
    "livro-congestao-hepatica": ["congestao-hepatica", "nutmeg-direita"],
    "livro-congestao-pulmonar-cronica": ["celulas-insuficiencia-cardiaca"],
}

if __name__ == "__main__":
    inventory = json.loads((HERE / "inventario-aula.json").read_text())
    plan = json.loads((HERE / "plan.json").read_text())
    items = [i for s in inventory["slides"] for i in s.get("itens", [])]
    items += inventory["exercicios"] + inventory["capitulo"]
    keys = {e["key"] for e in plan["entries"]}
    assert set(M) == {i["id"] for i in items}, (sorted(set(M) - {i["id"] for i in items}),
                                                    sorted({i["id"] for i in items} - set(M)))
    assert all(set(cards) <= keys for cards in M.values())
    (HERE / "mapa-previsto.json").write_text(json.dumps(
        [{"id": item["id"], "alvo": item["alvo"], "cards": M[item["id"]]} for item in items],
        ensure_ascii=False, indent=2))
    print(len(items), "itens;", len(set(k for v in M.values() for k in v)), "chaves usadas")
