#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""aplicar_curadoria_anking.py -- aplica a curadoria card-a-card no deck do Davi.

Le flashcards/curadoria/<slug>-curado.json, marca os notes curados com a tag-ancora
NEBLI::<slug> na colecao (via AnkiConnect), dessuspende esses cards e atualiza
o painel flashcards/curadoria/_INDEX.md (o aviso vivo de "o que ja esta no deck").

A marca NEBLI::<slug> persiste a escolha CARD-A-CARD dentro da colecao: reaplicar
e idempotente, e reverter e trivial (--reverter re-suspende a mesma marca).

Schema do <slug>-curado.json:
    {
      "slug": "anato-06-circulatorio-linfatico-II",
      "tag_ancora": "NEBLI::anato-06-circulatorio-linfatico-II",   # opcional
      "tags_puras": [ "#AK_Step1_v12::#SketchyAnatomy::02_Thorax::03_Vasculature::02_Superior_Vena_Cava" ],
      "impuras": [
         { "tag": "#AK_Step1_v12::#FirstAid::07_Cardiovascular::02_Anatomy",
           "guids_kept": ["a1b2...", "c3d4..."] }
      ]
    }

guids_kept aceita duas formas (compat retroativa):
  - string simples: "a1b2..."
  - objeto auditavel: {"guid": "a1b2...", "conceito": "2.3", "motivo": "retorno venoso ..."}
Os campos conceito/motivo sao so documentacao (auditavel/reusavel); o apply usa
apenas o guid. Ver _guids_kept().

Uso:
    python flashcards/scripts/aplicar_curadoria_anking.py <slug> --dry-run
    python flashcards/scripts/aplicar_curadoria_anking.py <slug>
    python flashcards/scripts/aplicar_curadoria_anking.py <slug> --reverter
"""
import json, sys, os, argparse, datetime, re, urllib.request, urllib.error

_WS = re.compile(r"\s+")


def _norm(txt):
    """Normaliza o campo 1 bruto pra casar export x colecao (colapsa espaco)."""
    return _WS.sub(" ", (txt or "").replace("​", "")).strip()

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ANKICONNECT = "http://localhost:8765"
PREFIXO = "#AK_Step1_v12"
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
INDEX = os.path.join(RAIZ, "flashcards", "curadoria", "_INDEX.md")


# --- helpers AnkiConnect (mesma base do dessuspender_anking.py) ---
def _invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT, payload)
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    if data.get("error") is not None:
        raise RuntimeError(data["error"])
    return data["result"]


def _anki_vivo():
    try:
        _invoke("version")
        return True
    except (urllib.error.URLError, OSError, RuntimeError):
        return False


def _normalizar(tag):
    tag = tag.strip().strip('"')
    if not tag:
        return None
    if not tag.startswith(PREFIXO):
        tag = f"{PREFIXO}::{tag}"
    return tag


def _busca(tag):
    return f'"tag:{tag}" OR "tag:{tag}::*"'


# --- resolucao dos notes a marcar ---
def _carregar_pool(slug):
    """guid -> campo 1 bruto normalizado, do pool arquivos-trabalho/anking-pool-<slug>.json."""
    caminho = os.path.join(RAIZ, "arquivos-trabalho", f"anking-pool-{slug}.json")
    if not os.path.exists(caminho):
        return None
    with open(caminho, encoding="utf-8") as f:
        pool = json.load(f)
    return {c["guid"]: _norm(c.get("raw0", "")) for c in pool.get("cards", [])}


def _primeiro_campo(note):
    campos = note.get("fields", {})
    if not campos:
        return ""
    # ordem de insercao = ordem dos campos; campo 1 = frente
    return next(iter(campos.values()), {}).get("value", "")


def _guids_kept(bloco):
    """Normaliza guids_kept: aceita ["guid", ...] ou [{"guid":..,"conceito":..}, ...]."""
    out = []
    for g in bloco.get("guids_kept", []):
        if isinstance(g, dict):
            gid = g.get("guid")
            if gid:
                out.append(gid)
        elif g:
            out.append(g)
    return out


def _notes_de_tag_pura(tag):
    return set(_invoke("findNotes", query=_busca(tag)))


def _notes_de_tag_impura(tag, guids_kept, poolmap):
    """Notes da tag filtrados aos curados. Casa por guid (se o AnkiConnect expuser)
    ou, no fallback, pelo texto bruto do campo 1 (poolmap: guid -> raw0 normalizado)."""
    nids = _invoke("findNotes", query=_busca(tag))
    if not nids:
        return set()
    info = _invoke("notesInfo", notes=nids)
    alvo_guid = set(guids_kept)
    alvo_txt = {poolmap[g] for g in guids_kept if poolmap and g in poolmap}
    achados = set()
    for n in info:
        if n.get("guid") in alvo_guid:                 # caminho ideal (versoes novas)
            achados.add(n["noteId"])
        elif alvo_txt and _norm(_primeiro_campo(n)) in alvo_txt:  # fallback por texto
            achados.add(n["noteId"])
    return achados


def resolver_notes(spec, poolmap):
    nids = set()
    faltas = []
    for tag in spec.get("tags_puras", []):
        nids |= _notes_de_tag_pura(_normalizar(tag))
    for bloco in spec.get("impuras", []):
        tag = _normalizar(bloco["tag"])
        kept = _guids_kept(bloco)
        achados = _notes_de_tag_impura(tag, kept, poolmap)
        nids |= achados
        if len(achados) < len(kept):
            faltas.append((tag, len(kept), len(achados)))
    return nids, faltas


# --- atualizacao do painel _INDEX.md ---
def atualizar_index(slug, n_cards, tag_ancora, cobertura="—", lacunas="—", uc="UC0?/P?"):
    if not os.path.exists(INDEX):
        return False
    hoje = datetime.date.today().isoformat()
    linha = (f"| {slug} | {uc} | aplicado (card-a-card) | {n_cards} | {hoje} | "
             f"{cobertura} | {lacunas} | `{tag_ancora}` |")
    with open(INDEX, encoding="utf-8") as f:
        linhas = f.readlines()
    alvo_prefixo = f"| {slug} |"
    for i, l in enumerate(linhas):
        if l.startswith(alvo_prefixo):
            linhas[i] = linha + "\n"
            break
    else:
        # inserir antes da linha de Total
        for i, l in enumerate(linhas):
            if l.startswith("**Total"):
                linhas.insert(i, linha + "\n")
                break
        else:
            linhas.append(linha + "\n")
    with open(INDEX, "w", encoding="utf-8") as f:
        f.writelines(linhas)
    return True


def _fallback_manual(spec, tag_ancora):
    print("AnkiConnect nao respondeu (Anki fechado ou add-on 2055492159 ausente).")
    print("Fallback -- no Browse do Anki, marque manualmente e dessuspenda:\n")
    for tag in spec.get("tags_puras", []):
        print(f"# tag pura (marcar TODOS): {_normalizar(tag)}")
        print(f"  busca: {_busca(_normalizar(tag))}")
        print(f"  -> selecione tudo, add tag '{tag_ancora}', Ctrl+J (dessuspender)\n")
    for bloco in spec.get("impuras", []):
        print(f"# tag impura (marcar SO os {len(bloco.get('guids_kept', []))} curados): {_normalizar(bloco['tag'])}")
        print(f"  busca: {_busca(_normalizar(bloco['tag']))}")
        print(f"  -> keep/drop pela lista do manifesto; nos kept add '{tag_ancora}' + Ctrl+J\n")
    print("Depois de marcar, dessuspenda todos de uma vez com:  tag:" + tag_ancora)
    print("\nDeixe o Anki aberto com AnkiConnect pra eu fazer isso direto.")


def main():
    ap = argparse.ArgumentParser(description="Aplica curadoria AnKing (marca NEBLI::<slug> + dessuspende).")
    ap.add_argument("slug", help="slug da aula (le flashcards/curadoria/<slug>-curado.json)")
    ap.add_argument("--dry-run", action="store_true", help="conta, nao modifica a colecao")
    ap.add_argument("--reverter", action="store_true", help="re-suspende a tag-ancora (desfaz)")
    args = ap.parse_args()

    caminho = os.path.join(RAIZ, "flashcards", "curadoria", f"{args.slug}-curado.json")
    if not os.path.exists(caminho):
        ap.error(f"nao achei {os.path.relpath(caminho, RAIZ)} -- gere o manifesto primeiro")
    with open(caminho, encoding="utf-8") as f:
        spec = json.load(f)
    tag_ancora = spec.get("tag_ancora") or f"NEBLI::{args.slug}"

    if not _anki_vivo():
        if args.reverter:
            print("AnkiConnect fora do ar; para reverter: no Browse busque 'tag:%s' e Ctrl+J." % tag_ancora)
            sys.exit(3)
        _fallback_manual(spec, tag_ancora)
        sys.exit(3)

    if args.reverter:
        cards = _invoke("findCards", query=f'"tag:{tag_ancora}"')
        print(f"Reverter {args.slug}: {len(cards)} cards sob {tag_ancora}.")
        if not args.dry_run and cards:
            _invoke("suspend", cards=cards)
            print("  -> re-suspensos (a marca NEBLI:: fica, dá pra reaplicar).")
        return

    poolmap = _carregar_pool(args.slug)
    if poolmap is None and any(b.get("guids_kept") for b in spec.get("impuras", [])):
        print(f"! pool arquivos-trabalho/anking-pool-{args.slug}.json ausente — "
              f"regenere com extrair_cards_anking.py (necessário p/ casar por texto).")
    print(f"Resolvendo notes curados de {args.slug}...{'  [DRY-RUN]' if args.dry_run else ''}")
    nids, faltas = resolver_notes(spec, poolmap)
    print(f"  notes a marcar com {tag_ancora}: {len(nids)}")
    for tag, pedidos, achou in faltas:
        print(f"  ! {tag}: pedi {pedidos} guids, casei {achou} (guid divergente? confira o pool)")

    if args.dry_run:
        # simular contagem de cards (findCards por tag ainda nao existe; estimar por notes)
        print(f"\nSeriam marcados {len(nids)} notes e dessuspensos os cards deles.")
        print("Rode sem --dry-run para aplicar.")
        return

    if nids:
        _invoke("addTags", notes=sorted(nids), tags=tag_ancora)
    cards = _invoke("findCards", query=f'"tag:{tag_ancora}"')
    if cards:
        _invoke("unsuspend", cards=cards)
    print(f"\nMarcados {len(nids)} notes; dessuspensos {len(cards)} cards sob {tag_ancora}.")

    ok = atualizar_index(args.slug, len(cards), tag_ancora)
    print("Painel _INDEX.md atualizado." if ok else "! _INDEX.md nao encontrado; atualize a mao.")


if __name__ == "__main__":
    main()
