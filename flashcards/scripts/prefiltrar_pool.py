#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prefiltrar_pool.py -- afina o pool da Camada 2 ANTES de a sessao ler.

O unico lugar onde a curadoria gasta tokens e a Camada 2: a sessao le o
anking-pool-<slug>.json card-a-card (100-156 cards de raw0 cheio de HTML). Este
script corta esse custo de duas formas, sem decidir nada sozinho:

  1. HEURISTICA DE RUIDO: separa por uma blocklist de patologia/fora-de-escopo
     (dissection, aneurysm, carcinoma, syndrome, ...) os cards que quase certeza
     sao RUIDO para uma aula que ensina anatomia/via/mecanismo -- nao a doenca.
     A sessao SO PASSA O OLHO nesses (decisao do Davi: revisar os cortados, nao
     cortar cego) e resgata falso-positivo.
  2. POOL-SLIM: emite so a FRENTE limpa (sem HTML, sem raw0, sem verso),
     truncada, com guid visivel. E isso que a sessao le a fundo. O raw0 continua
     no pool cheio (o apply casa por texto la); nao precisa entrar no contexto.

Saida: arquivos-trabalho/anking-pool-<slug>-slim.md (PROVAVEIS-BONS + RUIDO).

Uso:
    python flashcards/scripts/prefiltrar_pool.py <slug>
    python flashcards/scripts/prefiltrar_pool.py <slug> --extra "shunt,fistula"
    python flashcards/scripts/prefiltrar_pool.py <slug> --trunc 160
"""
import argparse
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# blocklist default: termos que quase sempre marcam patologia/clinica de doenca
# ou detalhe fora do recorte de uma aula de anatomia macro / via / mecanismo.
# A sessao revisa os cortados -- entao errar pro lado do corte aqui e barato.
BLOCKLIST = [
    "dissection", "aneurysm", "aneurysmal", "carcinoma", "sarcoma", "lymphoma",
    "syndrome", "infarct", "ischemia", "ischemic", "stenosis", "regurgitation",
    "thrombosis", "embolism", "embolus", "neoplasm", "malignan", "metasta",
    "tumor", "tumour", "abscess", "hemorrhage", "haemorrhage", "necrosis",
    "fibrosis", "hyperplasia", "dysplasia", "atrophy", "edema", "oedema",
    "murmur", "prolapse", "insufficiency", "failure", "deficiency", "disease",
    "disorder", "cancer", "palsy", "fistula", "hernia", "rupture",
]


def carregar_pool(slug):
    caminho = os.path.join(RAIZ, "arquivos-trabalho", f"anking-pool-{slug}.json")
    if not os.path.exists(caminho):
        return None, caminho
    with open(caminho, encoding="utf-8") as f:
        return json.load(f), caminho


def _leaf(card):
    tags = card.get("tags") or []
    if tags:
        return "::".join(tags[0].split("::")[2:]) or tags[0]
    return "?"


def _hit(card, rx):
    """Termo da blocklist que casou (front+tags), ou None."""
    alvo = (card.get("front", "") + " " + " ".join(card.get("tags", []))).lower()
    m = rx.search(alvo)
    return m.group(0) if m else None


def particionar(cards, blocklist):
    rx = re.compile(r"(?:%s)" % "|".join(re.escape(t) for t in blocklist), re.IGNORECASE)
    bons, ruido = [], []
    for c in cards:
        tags = c.get("tags") or []
        step2 = any("step2" in t.lower() or "step_2" in t.lower() for t in tags)
        step1 = any("step1" in t.lower() or "step_1" in t.lower() or "only_step_1" in t.lower() for t in tags)
        termo = "Step2-only" if step2 and not step1 else _hit(c, rx)
        if termo:
            ruido.append((c, termo))
        else:
            bons.append(c)
    return bons, ruido


def render(slug, bons, ruido, trunc):
    out = []
    total = len(bons) + len(ruido)
    out.append(f"# Camada 2 pre-filtrada — {slug}")
    out.append(f"# {total} cards no pool: {len(bons)} provaveis-bons, "
               f"{len(ruido)} ruido-provavel (blocklist de patologia).")
    out.append("# LER A FUNDO os provaveis-bons; PASSAR O OLHO no ruido e resgatar "
               "falso-positivo.")
    out.append("# keep = anote o guid + id de conceito da checklist. Precisao > recall.\n")

    out.append(f"## PROVAVEIS-BONS ({len(bons)}) — ler a fundo, keep/drop card-a-card\n")
    for i, c in enumerate(bons, 1):
        f = (c.get("front", "") or "").strip()
        if len(f) > trunc:
            f = f[:trunc].rstrip() + "…"
        out.append(f"- [{i}] `{c.get('guid','?')}` ({_leaf(c)}) — {f}")

    out.append(f"\n## RUIDO-PROVAVEL ({len(ruido)}) — passar o olho, resgatar bom cortado\n")
    for c, termo in ruido:
        f = (c.get("front", "") or "").strip()
        if len(f) > 90:
            f = f[:90].rstrip() + "…"
        out.append(f"- `{c.get('guid','?')}` ({_leaf(c)}) — {f}  ⟨corte: {termo}⟩")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Pre-filtra o pool da Camada 2 (menos tokens).")
    ap.add_argument("slug", help="slug da aula (le arquivos-trabalho/anking-pool-<slug>.json)")
    ap.add_argument("--extra", default="", help="termos extra pra blocklist, separados por virgula")
    ap.add_argument("--trunc", type=int, default=200, help="truncar a frente dos bons (chars)")
    ap.add_argument("--print", dest="imprimir", action="store_true", help="imprime em vez de gravar")
    args = ap.parse_args()

    pool, caminho = carregar_pool(args.slug)
    if pool is None:
        print(f"ERRO: pool nao encontrado: {os.path.relpath(caminho, RAIZ)}", file=sys.stderr)
        print("  gere antes com extrair_cards_anking.py \"<tags>\" --slug <slug>.", file=sys.stderr)
        return 2

    blocklist = list(BLOCKLIST)
    blocklist += [t.strip() for t in args.extra.split(",") if t.strip()]
    cards = pool.get("cards", [])
    bons, ruido = particionar(cards, blocklist)
    md = render(args.slug, bons, ruido, args.trunc)

    # estimativa grosseira de economia de tokens (chars/4)
    slim_chars = len(md)
    cheio_chars = len(json.dumps(cards, ensure_ascii=False))

    if args.imprimir:
        print(md)
    else:
        destino = os.path.join(RAIZ, "arquivos-trabalho", f"anking-pool-{args.slug}-slim.md")
        with open(destino, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"OK: {os.path.relpath(destino, RAIZ)}")
    print(f"  provaveis-bons: {len(bons)} | ruido-provavel: {len(ruido)} | total: {len(cards)}")
    print(f"  ~tokens Camada 2: slim ~{slim_chars // 4} vs pool cheio ~{cheio_chars // 4} "
          f"(economia ~{100 - (slim_chars * 100 // max(cheio_chars, 1))}%).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
