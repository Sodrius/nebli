"""Gera fallbacks escritos para alvos Kenhub sem figura, sem tocar no Anki.

Ordem econômica: reuso exato por slug -> sentença relacional local -> Ollama
local opcional. A saída é um catálogo novo com ``written_cards`` e um relatório;
itens que não passam nos gates permanecem explicitamente não resolvidos.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from dataclasses import dataclass, asdict
from pathlib import Path


CLOZE = re.compile(r"\{\{c1::([^{}]+)\}\}")
ENUMERATIVA = re.compile(
    r"(?:\b(?:incluem|inclui|compreendem|são|formado por|composto por)\b[^.]{0,180}(?:,|\be\b).*(?:,|\be\b))"
    r"|(?:^|[.:;])\s*(?:1[.)]|[-•])",
    re.I,
)
RELACAO = re.compile(
    r"\b(?:acompanh\w*|aloj\w*|articul\w*|atravess\w*|conect\w*|continu\w*|cobr\w*|delimit\w*|desemboc\w*|dren\w*|"
    r"agreg\w*|ancor\w*|circund\w*|condu\w*|contribu\w*|cont[eéê]m|contendo|detect\w*|emerg\w*|envolv\w*|estend\w*|focaliz\w*|form\w*|inerv\w*|inser\w*|irrig\w*|lig\w*|ocup\w*|origin\w*|pass\w*|produ\w*|proteg\w*|recobr\w*|receb\w*|regul\w*|relacion\w*|retra\w*|secret\w*|separ\w*|"
    r"situ\w*|supr\w*|un\w*|continuação|accompanies|attaches|connects|contains|continues|covers|drains|"
    r"amplific\w*|armazen\w*|ativ\w*|catalis\w*|caus\w*|classific\w*|compost\w*|control\w*|contrai\w*|converte\w*|define\w*|desencade\w*|execut\w*|facilit\w*|liber\w*|"
    r"degrad\w*|direcion\w*|envi\w*|fornec\w*|mant[eé]\w*|modific\w*|modul\w*|orden\w*|permite\w*|process\w*|projet\w*|re[uú]ne\w*|regener\w*|result\w*|sintetiz\w*|transmit\w*|transport\w*|forms|gives rise|innervates|is located|lies|opens|originates|passes|receives|"
    r"separates|supplies|surrounds|traverses)\b",
    re.I,
)


@dataclass
class Resultado:
    unit: str
    slug: str
    status: str
    metodo: str
    fonte: str = ""
    erro: str = ""


def validar(texto: str, resposta: str | None = None) -> list[str]:
    erros: list[str] = []
    lacunas = CLOZE.findall(texto or "")
    if len(lacunas) != 1:
        erros.append("exige exatamente um cloze c1")
    elif resposta and normalizar(lacunas[0]) != normalizar(resposta):
        erros.append("resposta do cloze diverge do nome")
    visivel = CLOZE.sub("___", texto or "")
    if ENUMERATIVA.search(visivel):
        erros.append("frase enumerativa proibida")
    if not RELACAO.search(visivel):
        erros.append("frase sem relação anatômica recuperável")
    if len(visivel) > 280:
        erros.append("frase longa demais")
    if "kenhub" in visivel.lower():
        erros.append("marca visível proibida")
    return erros


def normalizar(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.casefold()).strip()


def _sentencas(payload: dict) -> list[tuple[str, str]]:
    out = []
    for trecho in payload.get("texto", []):
        bruto = trecho.get("pt") or trecho.get("en") or ""
        for frase in re.split(r"(?<=[.!?])\s+|\n+", bruto):
            frase = re.sub(r"\s+", " ", frase).strip()
            if frase:
                out.append((trecho.get("chave", "texto"), frase))
    return out


def _achar_sentenca(item: dict, payload: dict) -> tuple[str, str] | None:
    nomes = [item.get("nome_en", ""), item.get("nome_pt", "")]
    termos = [normalizar(x) for x in nomes if x]
    slug_tokens = [x for x in item.get("slug", "").split("-") if len(x) > 3]
    candidatos = []
    for chave, frase in _sentencas(payload):
        nf = normalizar(frase)
        hit = max([len(t.split()) for t in termos if t and t in nf] or [0])
        if not hit:
            hit = sum(t in nf for t in slug_tokens)
        if hit and RELACAO.search(frase) and not ENUMERATIVA.search(frase):
            candidatos.append((hit, -len(frase), chave, frase))
    if not candidatos:
        return None
    _, _, chave, frase = max(candidatos)
    return chave, frase


def _cloze_sentenca(frase: str, item: dict) -> str | None:
    """Usa texto PT local apenas quando o nome aparece literalmente."""
    nome = item.get("nome_pt")
    if not nome:
        return None
    m = re.search(re.escape(nome), frase, re.I)
    if not m:
        return None
    texto = frase[:m.start()] + "{{c1::" + nome + "}}" + frase[m.end():]
    return texto if not validar(texto, nome) else None


def indice_reusos(raiz: Path) -> dict[str, dict]:
    """Indexa a versão escrita canônica dos lotes anteriores pelo slug."""
    out: dict[str, dict] = {}
    for arq in sorted(raiz.glob("lote-*/build-ciano/relatorio.json")):
        try:
            data = json.loads(arq.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for card in data.get("written", []):
            if not validar(card.get("text", "")):
                out.setdefault(card["structure"], card)
    return out


def _modelo_ollama() -> str | None:
    exe = shutil.which("ollama")
    if not exe:
        return None
    try:
        p = subprocess.run([exe, "list"], text=True, capture_output=True, timeout=8, check=True)
    except (OSError, subprocess.SubprocessError):
        return None
    linhas = [x.split()[0] for x in p.stdout.splitlines()[1:] if x.strip()]
    return linhas[0] if linhas else None


def _ollama(item: dict, evidencia: tuple[str, str] | None, modelo: str) -> dict | None:
    prompt = {
        "tarefa": "Escreva uma unica frase anatomica relacional em portugues com exatamente um {{c1::resposta}}.",
        "regras": ["nao enumerar", "nao inventar", "nao citar Kenhub", "maximo 35 palavras", "JSON somente"],
        "saida": {"text": "...", "extra": "fonte local sucinta"},
        "alvo": item,
        "evidencia_local": evidencia[1] if evidencia else None,
    }
    try:
        p = subprocess.run(
            ["ollama", "run", modelo, "--format", "json"], input=json.dumps(prompt, ensure_ascii=False),
            text=True, capture_output=True, timeout=120, check=True,
        )
        obj = json.loads(p.stdout)
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError):
        return None
    resposta = item.get("nome_pt")
    return obj if isinstance(obj, dict) and not validar(obj.get("text", ""), resposta) else None


def gerar(catalogo: Path, destino: Path, *, usar_modelo_local: bool = True) -> dict:
    data = json.loads(catalogo.read_text())
    reusos = indice_reusos(catalogo.parent.parent)
    modelo = _modelo_ollama() if usar_modelo_local else None
    resultados: list[Resultado] = []
    resolvidos = 0
    for unit in data.get("units", []):
        fonte = Path(unit["source_dir"]) / "itens.json"
        payload = json.loads(fonte.read_text())
        existentes = {x["structure"]: x for x in unit.get("written_cards", [])}
        escritos = list(unit.get("written_cards", []))
        for item in payload.get("itens", []):
            if not item.get("sem_figura") or item["slug"] in existentes:
                continue
            slug = item["slug"]
            if slug in reusos:
                antigo = reusos[slug]
                escritos.append({"structure": slug, "text": antigo["text"],
                                 "extra": antigo.get("extra") or item.get("nome_en", slug),
                                 "reuse_id": antigo["stable_id"]})
                resultados.append(Resultado(unit["slug"], slug, "resolvido", "reuso_slug"))
                resolvidos += 1
                continue
            evidencia = _achar_sentenca(item, payload)
            texto = _cloze_sentenca(evidencia[1], item) if evidencia else None
            metodo = "sentenca_local"
            obj = {"text": texto, "extra": evidencia[0]} if texto and evidencia else None
            if not obj and modelo:
                obj = _ollama(item, evidencia, modelo)
                metodo = f"ollama:{modelo}"
            if obj:
                escritos.append({"structure": slug, "text": obj["text"],
                                 "extra": obj.get("extra") or item.get("nome_en", slug)})
                resultados.append(Resultado(unit["slug"], slug, "resolvido", metodo,
                                             evidencia[0] if evidencia else ""))
                resolvidos += 1
            else:
                resultados.append(Resultado(unit["slug"], slug, "pendente", "nenhum",
                                             evidencia[0] if evidencia else "", "sem formulação validada"))
        if escritos:
            unit["written_cards"] = escritos
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    relatorio = {"catalogo_entrada": str(catalogo), "catalogo_saida": str(destino),
                 "modelo_local": modelo, "resolvidos": resolvidos,
                 "pendentes": sum(r.status == "pendente" for r in resultados),
                 "resultados": [asdict(r) for r in resultados]}
    destino.with_suffix(".fallbacks.json").write_text(json.dumps(relatorio, ensure_ascii=False, indent=2) + "\n")
    return relatorio


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("catalogo", type=Path)
    p.add_argument("-o", "--saida", type=Path, required=True)
    p.add_argument("--sem-modelo-local", action="store_true")
    args = p.parse_args(argv)
    r = gerar(args.catalogo, args.saida, usar_modelo_local=not args.sem_modelo_local)
    print(json.dumps({k: r[k] for k in ("resolvidos", "pendentes", "modelo_local")}, ensure_ascii=False))
    return 0 if not r["pendentes"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
