"""Troca o nome que uma nota do Kenhub mostra pelo nome oficial da aula (F-20261022-CLAUDE-10) e regera a figura com o rótulo.

- NEBLI Kenhub IO v1 (neuro): a figura-base está na mídia (campo Imagem); regera MascaraP/MascaraR (seta e nome na ponta).
- NEBLI Kenhub Referência v1 (demais áreas): a figura-base bruta está em ~/NEBLI-privado/kenhub/referencia-externa/**/itens.json
  (ID (hidden) = khref:<unidade>:<estrutura>:ciano); regera Imagem Frente (seta + “?”) e Imagem Verso (seta + nome), tema ciano.
O nome antigo vai para Sinonimos (IO). Devolve (campos novos, {arquivo de mídia: caminho local}).
"""
from __future__ import annotations

import hashlib
import io
import json
import re
from pathlib import Path

from PIL import Image

from nebli.kenhub import mascara

REF = Path.home() / "NEBLI-privado" / "kenhub" / "referencia-externa"


def _base_ref(id_hidden: str) -> Path:
    m = re.match(r"khref:([^:]+):([^:]+):", re.sub(r"<[^>]+>", "", id_hidden))
    if not m:
        raise ValueError(f"ID da referência sem unidade/estrutura: {id_hidden!r}")
    unidade, estrutura = m.groups()
    for itens in REF.glob("anatomia/**/itens.json"):
        d = json.loads(itens.read_text())
        if d.get("unidade") != unidade:
            continue
        for i in d.get("itens", []):
            if i.get("slug") == estrutura:
                return itens.parent / i["arquivo"]
    raise FileNotFoundError(f"figura-base de {unidade}/{estrutura} não encontrada em {REF}")


def _compor(base: Image.Image, overlay_png: bytes) -> Image.Image:
    over = Image.open(io.BytesIO(overlay_png)).convert("RGBA")
    if over.size != base.size:
        base = base.resize(over.size, Image.LANCZOS)
    out = base.convert("RGBA")
    out.alpha_composite(over)
    return out.convert("RGB")


def renomear(campos: dict, nome: str, destino: Path, midia_dir: Path | None = None):
    """campos: campos atuais da nota (valores HTML). destino: pasta local onde gravar as figuras novas."""
    destino.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha1(nome.encode()).hexdigest()[:8]
    novos, midia = {"Nome PT": nome}, {}
    antigo = re.sub(r"<[^>]+>", "", campos.get("Nome PT", "")).strip()
    if "Sinonimos" in campos and antigo:
        sin = [s.strip() for s in campos["Sinonimos"].split(";") if s.strip()]
        if antigo not in sin:
            novos["Sinonimos"] = "; ".join([antigo] + sin)
    img = lambda campo: re.findall(r'src="([^"]+)"', campos.get(campo, ""))
    if "Imagem Verso" in campos:  # Referência
        base_arq = _base_ref(campos.get("ID (hidden)", ""))
        base = Image.open(base_arq).convert("RGB")
        frente, verso, _ = mascara.overlays(base.size, mascara.regiao(str(base_arq)), nome, cobrir=False, tema="ciano")
        for campo, dado, lado in (("Imagem Frente", frente, "front"), ("Imagem Verso", verso, "back")):
            arq = f"khref-{base_arq.stem[:20]}-{h}-{lado}.jpg"
            _compor(base, dado).save(destino / arq, quality=90)
            novos[campo], midia[arq] = f'<img src="{arq}">', destino / arq
    elif img("MascaraR"):  # IO da neuro
        base_arq = (midia_dir or Path()) / img("Imagem")[0]
        tam = Image.open(base_arq).size
        q, r, _ = mascara.overlays(tam, mascara.regiao(str(base_arq)), nome, cobrir=False)
        for campo, dado, lado in (("MascaraP", q, "Q"), ("MascaraR", r, "R")):
            arq = f"u7-{Path(base_arq).stem}-{lado}-{h}.png"
            (destino / arq).write_bytes(dado)
            novos[campo], midia[arq] = f'<img src="{arq}">', destino / arq
    return novos, midia
