"""O vocabulário que o gerador emite tem de existir no Companion.

Em 2026-08-12 o commit #19 renomeou o modo de Image Occlusion de
`hide_all_guess_all` para `hide_two_guess_two` nos dois lados do repo — e o
deck seguinte morreu na instalação, porque o APK do tablet ainda era do #18 e
não conhecia o nome novo. O lote inteiro caiu no primeiro card IO, com
rollback, depois de 23 cards criados.

Nada no repo podia ter previsto isso: nenhum teste comparava o vocabulário do
gerador Python com o do gate Java. Estes testes fazem essa comparação, e
prendem também o token do aparelho declarado em `config/pipeline.json`.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "flashcards" / "scripts"))

from gerar_manifesto_ankidroid import (  # noqa: E402
    IO_MODE_CANONICAL,
    IO_MODE_TOKENS,
)

CARD_RULES = (REPO / "android-companion" / "app" / "src" / "main" / "java"
              / "com" / "sodrius" / "nebli" / "companion" / "CardRules.java")


def _tokens_accepted_by_companion() -> set[str]:
    """Lê do fonte Java o conjunto de modos IO aceitos em runtime."""
    source = CARD_RULES.read_text(encoding="utf-8")
    block = re.search(r"IO_MODES\s*=.*?;", source, re.S)
    assert block, "CardRules.java não declara mais IO_MODES"
    return set(re.findall(r'"([a-z0-9_]+)"', block.group(0)))


def test_every_token_the_generator_can_emit_is_accepted_by_the_companion():
    accepted = _tokens_accepted_by_companion()
    unsupported = sorted(set(IO_MODE_TOKENS) - accepted)
    assert not unsupported, (
        "o gerador pode emitir modos que o Companion recusa: "
        + ", ".join(unsupported)
    )


def test_canonical_token_is_the_first_one_the_companion_lists():
    assert IO_MODE_CANONICAL in _tokens_accepted_by_companion()


def test_configured_device_token_is_understood_by_both_sides():
    config = json.loads((REPO / "config" / "pipeline.json").read_text(encoding="utf-8"))
    installed = config["ankidroid"]["installed_companion"]
    token = installed["io_mode_token"]
    assert token in IO_MODE_TOKENS, "o gerador não sabe emitir o token do aparelho"
    assert token in _tokens_accepted_by_companion(), (
        "o token declarado como instalado no aparelho não é aceito pelo "
        "Companion deste repo — ou o config está velho, ou o alias foi removido "
        "cedo demais"
    )
    assert installed["io_mode_contract"] == IO_MODE_CANONICAL


def test_legacy_alias_survives_until_the_device_is_reinstalled():
    """Só remover o alias depois que o config apontar para o token canônico."""
    config = json.loads((REPO / "config" / "pipeline.json").read_text(encoding="utf-8"))
    token = config["ankidroid"]["installed_companion"]["io_mode_token"]
    if token != IO_MODE_CANONICAL:
        assert token in _tokens_accepted_by_companion(), (
            "o aparelho ainda depende do alias; removê-lo quebra a instalação"
        )
