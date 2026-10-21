"""Prepara e controla a Referência externa Kenhub; não reutiliza as regras da UC07.

Uso:
  ./kenhub-referencia preparar
  ./kenhub-referencia status
  ./kenhub-referencia autorizar --confirmar-piloto   # somente depois do OK explícito de Davi
  ./kenhub-referencia piloto --dry-run

`preparar` é totalmente local. Coleta de rede e escrita no Anki são bloqueadas sem
o arquivo de autorização. A instalação continuará sendo serial e exclusivamente
por `nebli.decks.escrita()` quando o montador da Fase 1 for liberado.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from nebli.kenhub.caminhos import RAIZ

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "config" / "referencia-externa-kenhub.json"
PRIVATE = RAIZ / "referencia-externa"
MANIFEST = PRIVATE / "manifesto.json"
STATE = PRIVATE / "estado.jsonl"

STATES = ("DISCOVERED", "COLLECTED", "NORMALIZED", "BUILT", "GATED", "REVIEWED", "STAGED", "INSTALLED", "VERIFIED")
EXPECTED_ROOT = "Referências::Referências Externas::Kenhub"
EXPECTED_SCOPE = {"anatomia", "histologia", "fisiologia"}


def _read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def config_gates(cfg: dict) -> list[str]:
    problems = []
    if cfg.get("mode") != "referencia_kenhub": problems.append("G31 modo não é referencia_kenhub")
    if cfg.get("deck_root") != EXPECTED_ROOT: problems.append("G31 raiz divergente")
    if set(cfg.get("scope", [])) != EXPECTED_SCOPE: problems.append("G32 escopo deve ser anatomia+histologia+fisiologia")
    if "neuroanatomia" not in cfg.get("exclude", []): problems.append("G33 neuroanatomia não foi excluída")
    if cfg.get("initial_suspension") is not True: problems.append("G34 cards não entram todos suspensos")
    if cfg.get("content_phase_1") != "identificacao_visual": problems.append("G35 fase 1 não é identificação visual")
    if cfg.get("content_phase_2") != "texto_dos_quizzes": problems.append("G35 quizzes não ficaram para a fase 2")
    if cfg.get("visual_themes") != ["ciano"]: problems.append("G36 produção deve usar somente o tema ciano")
    if cfg.get("production", {}).get("selected_theme") != "ciano": problems.append("G36 tema definitivo não é ciano")
    if cfg.get("private_only") is not True: problems.append("G37 acervo não está marcado como privado")
    if cfg.get("background_only_after_authentication") is not True:
        problems.append("G45 navegador de produção deve permanecer invisível")
    production = cfg.get("production", {})
    if production.get("batch_size_units") != 50: problems.append("G40 produção não está em levas de 50 unidades")
    if production.get("checkpoint_requires_complete_coverage") is not True:
        problems.append("G41 checkpoint não exige completude")
    if production.get("text_phase_separate") is not True: problems.append("G42 texto não ficou em leva separada")
    if cfg.get("hierarchy") != ["dominio", "modulo_oficial", "secao_oficial", "unidade_oficial"]:
        problems.append("G43 hierarquia não segue domínio → módulo → seção → unidade")
    write = cfg.get("anki_write_policy", {})
    expected_write = {"prepare_outside_anki": True, "single_write_session": True,
                      "vectorized_actions_only": True, "single_final_readback": True,
                      "sync_while_studying": False}
    if write != expected_write: problems.append("G44 política de escrita única no Anki divergente")
    pilot = cfg.get("pilot", {})
    if len(pilot.get("unit_profiles", [])) != 3: problems.append("G38 piloto precisa de três perfis heterogêneos")
    if pilot.get("review_percent") != 100 or len(pilot.get("render_targets", [])) != 4:
        problems.append("G39 piloto não revisa/renderiza 100% nos quatro estados")
    return problems


def checkpoint_gate(batch: dict, final: bool = False) -> list[str]:
    """Uma leva só fecha se reconciliar todos os alvos de todas as unidades."""
    problems=[]; units=batch.get("units", [])
    if not units: return ["G41 checkpoint vazio"]
    if len(units) != 50 and not final: problems.append(f"G40 leva com {len(units)} unidades, esperado 50")
    for u in units:
        found=int(u.get("targets", 0)); built=int(u.get("built", 0)); reused=int(u.get("reused", 0)); exceptions=u.get("exceptions", [])
        if found <= 0: problems.append(f"G41 {u.get('slug','?')}: nenhum alvo descoberto")
        written=int(u.get("written", 0))
        unresolved=[e for e in exceptions if e.get("reason") == "sem_figura" and not e.get("written_id")]
        if found != built + reused + written: problems.append(f"G41 {u.get('slug','?')}: {found} alvos != {built} visuais + {reused} reusos + {written} escritos")
        if unresolved: problems.append(f"G46 {u.get('slug','?')}: {len(unresolved)} alvos sem figura ainda sem card escrito")
        if u.get("state") != "VERIFIED": problems.append(f"G41 {u.get('slug','?')}: estado {u.get('state')} != VERIFIED")
        if not u.get("module_order") or not u.get("section_order") or not u.get("unit_order"): problems.append(f"G43 {u.get('slug','?')}: ordem oficial de módulo/seção/unidade ausente")
    return problems


def anki_write_plan_gate(plan: dict) -> list[str]:
    """Impede instaladores que ocupem o Anki com escrita incremental por card."""
    problems = []
    if plan.get("prepared_outside_anki") is not True:
        problems.append("G44 lote não foi preparado integralmente fora do Anki")
    if plan.get("write_sessions") != 1:
        problems.append("G44 escrita deve ocorrer em uma única janela")
    if plan.get("readbacks") != 1:
        problems.append("G44 deve haver um único readback ao fim da janela")
    if plan.get("per_card_calls", 0) != 0:
        problems.append("G44 chamadas de escrita por card são proibidas")
    if plan.get("sync") is not False:
        problems.append("G44 lote concorrente ao estudo deve ficar sem sync")
    return problems


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def preparar() -> None:
    cfg = _read(CONFIG)
    problems = config_gates(cfg)
    if problems:
        raise SystemExit("\n".join(problems))
    PRIVATE.mkdir(parents=True, exist_ok=True)
    if not MANIFEST.exists():
        MANIFEST.write_text(json.dumps({
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "config_sha256": _sha(CONFIG),
            "deck_root": EXPECTED_ROOT,
            "catalog": [],
            "pilot_units": [],
            "states": list(STATES),
            "installation": "blocked_until_explicit_approval"
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not STATE.exists():
        STATE.write_text("", encoding="utf-8")
    print(f"PRONTO: {EXPECTED_ROOT}")
    print(f"manifesto privado: {MANIFEST}")
    print("rede: BLOQUEADA | Anki: BLOQUEADO | piloto: aguardando OK explícito")


def _approval(cfg: dict) -> Path:
    return PRIVATE / cfg["authorization"]["approval_file"]


def autorizar(args: list[str]) -> None:
    if args != ["--confirmar-piloto"]:
        raise SystemExit("autorização recusada: use --confirmar-piloto somente após o OK explícito de Davi")
    preparar()
    cfg = _read(CONFIG)
    _approval(cfg).write_text(json.dumps({
        "scope": "pilot_only",
        "approved_at": datetime.now(timezone.utc).isoformat(),
        "config_sha256": _sha(CONFIG),
        "anki_write": False
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("piloto autorizado para descoberta/coleta; escrita no Anki continua bloqueada")


def status() -> None:
    cfg = _read(CONFIG)
    problems = config_gates(cfg)
    app = _approval(cfg)
    manifest = _read(MANIFEST) if MANIFEST.exists() else {}
    print(json.dumps({
        "ready": not problems and MANIFEST.exists(),
        "problems": problems,
        "root": cfg.get("deck_root"),
        "scope": cfg.get("scope"),
        "neuro_excluded": "neuroanatomia" in cfg.get("exclude", []),
        "suspended": cfg.get("initial_suspension"),
        "themes": cfg.get("visual_themes"),
        "authorized": app.exists() and _read(app).get("config_sha256") == _sha(CONFIG),
        "pilot_units": manifest.get("pilot_units", []),
        "anki_write": False
    }, ensure_ascii=False, indent=2))


def piloto(args: list[str]) -> None:
    cfg = _read(CONFIG)
    app = _approval(cfg)
    if not app.exists() or _read(app).get("config_sha256") != _sha(CONFIG):
        raise SystemExit("PILOTO BLOQUEADO: falta OK explícito e `autorizar --confirmar-piloto`")
    if args != ["--dry-run"]:
        raise SystemExit("nesta etapa só é permitido `piloto --dry-run`; instalação permanece bloqueada")
    manifest = _read(MANIFEST)
    print("PILOTO LIBERADO EM DRY-RUN")
    print("próxima transição: descobrir catálogo → selecionar 3 unidades pelos perfis → coletar serialmente")
    print(f"perfis: {', '.join(cfg['pilot']['unit_profiles'])}")
    print(f"unidades selecionadas: {len(manifest.get('pilot_units', []))}; Anki: BLOQUEADO")


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "preparar": preparar()
    elif cmd == "status": status()
    elif cmd == "autorizar": autorizar(args)
    elif cmd == "piloto": piloto(args)
    else: raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
