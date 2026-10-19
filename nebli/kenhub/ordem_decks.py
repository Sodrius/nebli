"""Nomes de deck que fazem a árvore da UC07 seguir a ordem oficial do Kenhub.

O Anki não guarda uma ordem manual para decks: ele os exibe pelo nome. Por isso a
ordem faz parte do nome visível (``01 Introdução...``), enquanto lesson_id, tags,
GUIDs e nomes das notas continuam inalterados.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PLANO = ROOT / "flashcards/projeto/PLANO-UC07-NEUROANATOMIA-COMPLETA-2026-10-17.md"


@dataclass(frozen=True)
class Unidade:
    ordem: int
    modulo: str
    submodulo: str
    slug: str


def unidades() -> list[Unidade]:
    out: list[Unidade] = []
    for linha in PLANO.read_text(encoding="utf-8").splitlines():
        cols = [c.strip() for c in linha.split("|")]
        # | Ordem cronograma | Aula | # Kenhub | Módulo | Submódulo | `slug` | ... |
        if len(cols) > 7 and cols[1].isdigit() and cols[3].isdigit() and cols[6].startswith("`"):
            out.append(Unidade(int(cols[3]), cols[4], cols[5], cols[6].strip("`")))
    if not out or len({u.ordem for u in out}) != len(out) or len({u.slug for u in out}) != len(out):
        raise RuntimeError("[G29 ordem Kenhub] plano vazio ou com ordem/slug duplicado")
    return sorted(out, key=lambda u: u.ordem)


def _indices_modulos(catalogo: list[Unidade]) -> dict[str, int]:
    primeira = {m: min(u.ordem for u in catalogo if u.modulo == m) for m in {u.modulo for u in catalogo}}
    return {m: i for i, (m, _) in enumerate(sorted(primeira.items(), key=lambda x: x[1]), 1)}


def nome_deck(modulo: str, submodulo: str, slug: str) -> str:
    catalogo = unidades()
    achados = [u for u in catalogo if u.slug == slug]
    if len(achados) != 1 or (achados[0].modulo, achados[0].submodulo) != (modulo, submodulo):
        raise ValueError(f"[G29 ordem Kenhub] unidade não cadastrada ou nomes divergentes: {slug!r}")
    u = achados[0]
    im = _indices_modulos(catalogo)[modulo]
    return f"NEBLI::UC07::{im:02d} {modulo}::{u.ordem:02d} {submodulo}"


def nome_deck_por_slug(slug: str) -> str:
    achados = [u for u in unidades() if u.slug == slug]
    if len(achados) != 1:
        raise ValueError(f"[G29 ordem Kenhub] slug ausente ou duplicado: {slug!r}")
    u = achados[0]
    return nome_deck(u.modulo, u.submodulo, u.slug)


def plano_renomeacao() -> dict[str, str]:
    """Árvore antiga → ordenada; inclui pais para preservar seus IDs na migração."""
    catalogo = unidades()
    indices = _indices_modulos(catalogo)
    plano: dict[str, str] = {}
    for u in catalogo:
        velho_mod = f"NEBLI::UC07::{u.modulo}"
        novo_mod = f"NEBLI::UC07::{indices[u.modulo]:02d} {u.modulo}"
        plano[velho_mod] = novo_mod
        plano[f"{velho_mod}::{u.submodulo}"] = f"{novo_mod}::{u.ordem:02d} {u.submodulo}"
    return plano
