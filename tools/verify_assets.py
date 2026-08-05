"""tools/verify_assets.py — read-only verification of committed vault plot assets.

Regenerates every registered plot script into a temporary directory (nothing is
written to the repository) and byte-compares each produced PNG against the
committed file. Reports one line per asset and exits non-zero when any asset is
stale, missing, or not produced by its script.

Exit codes:
    0  every expected asset matches its committed file
    1  at least one asset is stale / missing / not produced
    2  a generator script crashed while running

Usage:
    python tools/verify_assets.py             # verify every registered asset
    python tools/verify_assets.py --list      # print the (script -> asset) map
    python tools/verify_assets.py --dry-run   # print what would be verified; write nothing
"""
import argparse
import pathlib
import runpy
import tempfile

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (generator script, declared output PNG) — both relative to the vault root.
ASSETS = [
    ("Handout by AI/generate_assets.py", "Handout by AI/rabi_oscillations.png"),
    ("Handout by AI/generate_assets.py", "Handout by AI/rydberg_blockade.png"),
    ("Handout by AI/generate_assets.py", "Handout by AI/gate_waveforms.png"),
    ("Handout by AI/generate_assets.py", "Handout by AI/dark_state_physics.png"),
    ("Rydberg atom/attachments/rabi_oscillation_resonant.py", "Rydberg atom/attachments/rabi_oscillation_resonant.png"),
    ("Rydberg atom/attachments/rabi_oscillation_detuned.py", "Rydberg atom/attachments/rabi_oscillation_detuned.png"),
    ("Rydberg atom/attachments/rabi_freq_vs_intensity.py", "Rydberg atom/attachments/rabi_freq_vs_intensity.png"),
    ("Rydberg atom/attachments/learning-progress-2026-06-02.py", "Rydberg atom/attachments/learning-progress-2026-06-02.png"),
    ("Rydberg atom/attachments/learning-progress-2026-06-10.py", "Rydberg atom/attachments/learning-progress-2026-06-10.png"),
    ("tools/gen_progress_chart.py", "Rydberg atom/attachments/learning-progress-2026-06-04.png"),
    ("tools/plot_learning_progress.py", "Rydberg atom/attachments/learning-progress-2026-06-02.png"),
]


def _capture(script_rel: str, tmp: pathlib.Path) -> dict:
    """Run one generator with plt.savefig redirected under tmp.

    Returns {output_rel: pathlib.Path} for every file the script tried to write.
    """
    captured = {}
    real_savefig = plt.savefig
    real_show = plt.show

    def redirected(path, *args, **kwargs):
        p = pathlib.Path(path)
        if not p.is_absolute():
            p = ROOT / p
        try:
            rel = p.resolve().relative_to(ROOT.resolve())
        except ValueError:
            # Output outside the vault (should not happen); keep it debuggable.
            rel = pathlib.Path("__external__") / p.name
        target = tmp / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        captured[str(rel).replace("\\", "/")] = target
        return real_savefig(str(target), *args, **kwargs)

    plt.savefig = redirected
    plt.show = lambda *a, **k: None
    try:
        runpy.run_path(str(ROOT / script_rel), run_name="__main__")
    finally:
        plt.savefig = real_savefig
        plt.show = real_show
        plt.close("all")
    return captured


def verify() -> int:
    errors = []
    scripts_seen = set()

    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        for script_rel, output_rel in ASSETS:
            # Capture each script once, reuse the map across its rows.
            if script_rel not in scripts_seen:
                try:
                    produced = _capture(script_rel, tmp)
                except Exception as exc:  # noqa: BLE001 — report and continue
                    print(f"SCRIPT CRASHED: {script_rel} — {exc}")
                    return 2
                scripts_seen.add(script_rel)

            committed = ROOT / output_rel
            generated = produced.get(output_rel)

            if not committed.is_file():
                print(f"MISSING committed asset: {output_rel}")
                errors.append(output_rel)
            elif generated is None:
                print(f"NOT PRODUCED: {output_rel} (script wrote no file there)")
                errors.append(output_rel)
            elif committed.read_bytes() == generated.read_bytes():
                print(f"OK: {output_rel}")
            else:
                print(f"STALE: {output_rel} differs from current script output")
                errors.append(output_rel)

    if errors:
        print(f"\n{len(errors)} asset(s) out of date.")
        return 1
    print("\nAll registered assets are current.")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n")[1],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--list", action="store_true", help="Print the script -> asset map.")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be verified; write nothing.")
    args = parser.parse_args()

    if args.list:
        for script, asset in ASSETS:
            print(f"{script}  ->  {asset}")
        return 0
    if args.dry_run:
        print(f"Would verify {len(ASSETS)} asset(s) from {len({s for s, _ in ASSETS})} script(s).")
        return 0
    sys_exit(verify())


def sys_exit(code: int) -> None:
    import sys

    sys.exit(code)


if __name__ == "__main__":
    main()
