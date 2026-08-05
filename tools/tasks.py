"""tools/tasks.py — vault task runner (works without `make` on Windows).

Exposes the same targets a Makefile would, as plain subprocesses:

    python tools/tasks.py verify-assets      # byte-compare committed PNGs vs current scripts (read-only)
    python tools/tasks.py regenerate-assets  # regenerate every plot asset in place (writes PNGs)
    python tools/tasks.py test               # run plotting-pipeline smoke tests (no file writes)
    python tools/tasks.py check-rules-sync   # fail if AGENTS.md / CLAUDE.md drifted on core rules

Each target exits non-zero when its check fails or a script errors.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PYTHON = sys.executable

# Every generator script that writes a committed PNG (in dependency-safe order).
GENERATORS = [
    "Handout by AI/generate_assets.py",
    "Rydberg atom/attachments/rabi_oscillation_resonant.py",
    "Rydberg atom/attachments/rabi_oscillation_detuned.py",
    "Rydberg atom/attachments/rabi_freq_vs_intensity.py",
    "Rydberg atom/attachments/learning-progress-2026-06-02.py",
    "Rydberg atom/attachments/learning-progress-2026-06-10.py",
    "tools/gen_progress_chart.py",
    "tools/plot_learning_progress.py",
]


def _run(argv: list) -> int:
    proc = subprocess.run(argv, cwd=ROOT)
    return proc.returncode


def target_verify_assets() -> int:
    return _run([PYTHON, str(ROOT / "tools" / "verify_assets.py")])


def target_regenerate_assets() -> int:
    code = 0
    for script in GENERATORS:
        print(f"\n--- {script} ---")
        code |= _run([PYTHON, str(ROOT / script)])
    return code


def target_test() -> int:
    return _run([PYTHON, "-m", "pytest", "tests/", "-q"])


def target_check_rules_sync() -> int:
    return _run([PYTHON, str(ROOT / "tools" / "check_rule_sync.py")])


TARGETS = {
    "verify-assets": target_verify_assets,
    "regenerate-assets": target_regenerate_assets,
    "test": target_test,
    "check-rules-sync": target_check_rules_sync,
}


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in TARGETS:
        print(__doc__.strip())
        print("\nAvailable targets: " + ", ".join(sorted(TARGETS)))
        return 2
    return TARGETS[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
