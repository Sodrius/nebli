#!/usr/bin/env python3
"""Final hard gate for the canonical E1 + deck pipeline.

Draft work may validate a contract while the private AnKing source is pending.
A final release always requires both a frozen v3 contract and the real APKG.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from audit_apkg import audit
from validate_lesson_contract import validate


def enforce_card_count(package: dict, contract: dict) -> dict:
    package.setdefault("errors", [])
    package.setdefault("warnings", [])
    expected = contract.get("expected_total_cards", 0)
    hard_max = contract.get("card_hard_max", 0)
    actual = package.get("cards", 0)
    if actual != expected:
        package["errors"].append(
            f"APKG contém {actual} cards; contrato congelou {expected}"
        )
    if hard_max and actual > hard_max:
        package["errors"].append(
            f"APKG contém {actual} cards e excede hard_max={hard_max}"
        )
    package["passed"] = bool(package.get("passed") and not package["errors"])
    return package


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--apkg", type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    contract = validate(spec, args.manifest.resolve(), allow_pending_private=False)
    if spec.get("status") != "frozen":
        contract["errors"].append("release exige contrato status=frozen")
        contract["passed"] = False
    try:
        package = audit(args.apkg.resolve())
    except Exception as exc:
        package = {"passed": False, "errors": [str(exc)], "warnings": []}
    package = enforce_card_count(package, contract)
    result = {
        "passed": bool(contract["passed"] and package["passed"]),
        "contract": contract,
        "apkg": package,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
