"""tools/check_rule_sync.py — fail when AGENTS.md and CLAUDE.md drift on core rules.

AGENTS.md and CLAUDE.md are the vault's two rule files. They are not
byte-identical (different structure, different audience), but every *core rule*
must appear in both. This script checks a curated list of rule markers in each
file and exits non-zero when any marker is missing from either.

    python tools/check_rule_sync.py          # verify, exit 1 on drift
    python tools/check_rule_sync.py --list   # print the curated markers
"""
import argparse
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = ["AGENTS.md", "CLAUDE.md"]

# Core rule markers that MUST be present in BOTH rule files. When you add a new
# core rule to the vault, add it to both files first, then register its marker.
MARKERS = [
    "双文件同步规则",
    "English-Name",
    "comprehension",
    "AI 禁止修改此字段",
    "\\vert",
    "[!tip]",
    "matplotlib",
    "plt.show",
    "Daily Notes",
    "block reference",
    "SKILL.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--list", action="store_true", help="Print the curated markers.")
    args = parser.parse_args()

    if args.list:
        for m in MARKERS:
            print(m)
        return 0

    contents = {}
    for name in FILES:
        p = ROOT / name
        if not p.is_file():
            print(f"MISSING rule file: {name}")
            return 1
        contents[name] = p.read_text(encoding="utf-8")

    drift = []
    for marker in MARKERS:
        for name in FILES:
            if marker not in contents[name]:
                drift.append((name, marker))

    if drift:
        print(f"{len(drift)} core rule marker(s) missing from one rule file:")
        for name, marker in drift:
            print(f"  {name}  missing: {marker}")
        print("\nUpdate BOTH AGENTS.md and CLAUDE.md so every core rule appears in both.")
        return 1
    print(f"OK: all {len(MARKERS)} core rule markers present in AGENTS.md and CLAUDE.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
