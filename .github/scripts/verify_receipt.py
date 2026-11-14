#!/usr/bin/env python3
"""Controleer elke build_receipt.json in de repo.

Rekent van elk bestand onder "artifacts" de sha256 na en vergelijkt die met
de receipt. Stopt met exitcode 1 bij een ontbrekend bestand of een afwijkende
hash. Alleen de standaardbibliotheek, geen netwerk.
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def main() -> int:
    receipts = sorted(
        p for p in ROOT.rglob("build_receipt.json") if ".git" not in p.parts
    )
    if not receipts:
        print("FOUT: geen build_receipt.json gevonden")
        return 1

    checked = 0
    problems = []
    for receipt in receipts:
        try:
            artifacts = json.loads(receipt.read_text(encoding="utf-8"))["artifacts"]
        except (ValueError, KeyError) as exc:
            problems.append(f"{receipt.relative_to(ROOT)}: onleesbaar ({exc!r})")
            continue
        for rel, expected in sorted(artifacts.items()):
            target = receipt.parent / rel
            shown = target.relative_to(ROOT)
            checked += 1
            if not target.is_file():
                problems.append(f"{shown}: ontbreekt")
                continue
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
            if actual != expected:
                problems.append(
                    f"{shown}: hash wijkt af (receipt {expected[:12]}…, bestand {actual[:12]}…)"
                )

    for line in problems:
        print(f"FOUT  {line}")
    status = "FOUT" if problems else "OK"
    print(
        f"{status}: {checked - len(problems)}/{checked} hashes kloppen "
        f"in {len(receipts)} receipts"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
