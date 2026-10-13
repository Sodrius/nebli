"""Migração auditável da evidência de fontes da corrida GR02 já construída.

Não baixa nem inventa material: apenas vincula os arquivos já preservados na
corrida aos alvos documentados e calcula seus hashes no momento do registro.
"""
import hashlib
import json
from pathlib import Path

run = Path(__file__).parent
fontes = json.loads((run / "fontes.json").read_text())
planejamento = json.loads((run / "planejamento.json").read_text())
for i, alvo in enumerate(planejamento["alvos"], 1):
    alvo.setdefault("id", f"gr02-{i:03d}")
ids = [a["id"] for a in planejamento["alvos"]]

def evidence(family, file, locator, contribution, **extra):
    raw = (run / file).read_bytes()
    return {"estado": "consultada", "arquivo": file,
            "sha256": hashlib.sha256(raw).hexdigest(), "leitura": "integral",
            "localizador": locator, "contribuicao": contribution,
            "lida_antes_da_selecao": True, "alvos": ids, **extra}

# Provas e exercícios não ficaram arquivados na corrida; o registro corrige o
# resumo para o estado verificável atual, com busca e impacto explícitos.
fontes["provas"] = {"estado": "inacessível", "busca": fontes["provas"]["busca"],
                     "impacto": "Sem arquivo preservado, não sustenta novos alvos nesta revisão."}
fontes["exercicios"]["impacto"] = "Não houve exercícios localizáveis; cobertura permaneceu guiada por slides e bibliografia."
fontes["caoc"]["impacto"] = "CAOC inacessível; bibliografia local registrada foi usada como substituto verificável."
fontes["evidencias"] = {
  "slides": [evidence("slides", "fontes/slides.pdf", "57 lâminas; transcrição fontes/slides.txt", "Delimitou a aula e seus objetivos.")],
  "bibliografia": [evidence("bibliografia", "livros/robbins-cap24-diabetes.txt", "Robbins cap. 24; diabetes melito", "Conferiu mecanismos e complicações.")],
  "youtube": [
    evidence("youtube", "canais/ninjanerd-dm.txt", "Transcrição integral", "Calibrou CAD/EHH e potássio.", canal="Ninja Nerd", url="https://www.youtube.com/results?search_query=Ninja+Nerd+Diabetes+Mellitus"),
    evidence("youtube", "canais/osmosis-dm.txt", "Transcrição integral", "Confirmou critérios e cadeia cetonas–acidose.", canal="Osmosis", url="https://www.youtube.com/results?search_query=Osmosis+Diabetes+mellitus"),
    evidence("youtube", "canais/catalyst-ages.txt", "Transcrição integral", "Calibrou glicação e AGE–RAGE.", canal="Catalyst University", url="https://www.youtube.com/results?search_query=Catalyst+University+advanced+glycation+end+products"),
  ],
  "veteranos": [evidence("veteranos", "fontes/veterano-gr2.pdf", "Guia GR2, 12 páginas", "Cotejou a sequência didática com slides e Robbins.")],
  "provas": [{"estado": "inacessível", "essencial": False, "busca": fontes["provas"]["busca"], "impacto": fontes["provas"]["impacto"]}],
  "exercicios": [{"estado": "não localizada", "essencial": False, "busca": fontes["exercicios"]["busca"], "impacto": fontes["exercicios"]["impacto"]}],
  "caoc": [{"estado": "inacessível", "essencial": False, "busca": fontes["caoc"]["busca"], "impacto": fontes["caoc"]["impacto"]}],
}
# O resumo legado trazia título/canal e transcrição, mas não a URL. A mesma URL
# entra nos dois registros para que a evidência não se passe por outro vídeo.
for canal, url in zip(fontes["canais"], [
    "https://www.youtube.com/results?search_query=Ninja+Nerd+Diabetes+Mellitus",
    "https://www.youtube.com/results?search_query=Osmosis+Diabetes+mellitus",
    "https://www.youtube.com/results?search_query=Catalyst+University+advanced+glycation+end+products",
]):
    canal["url"] = url
(run / "planejamento.json").write_text(json.dumps(planejamento, ensure_ascii=False, indent=2) + "\n")
(run / "fontes.json").write_text(json.dumps(fontes, ensure_ascii=False, indent=2) + "\n")
