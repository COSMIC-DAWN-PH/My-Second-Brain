"""Smoke tests for the vault's Python plotting pipeline.

Each generator script is imported (and, where the script guards its plotting
behind ``__main__``, executed) with ``matplotlib`` on the Agg backend and with
``plt.savefig`` / ``plt.show`` patched to no-ops, so no PNG is ever written to
the repository. A failure here means the script cannot even build its figure.

Run with:  python -m pytest tests/ -q
"""
import importlib.util
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pytest  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Every tracked plot script, relative to the vault root (POSIX separators).
PLOT_SCRIPTS = [
    "Handout by AI/generate_assets.py",
    "Rydberg atom/attachments/rabi_oscillation_resonant.py",
    "Rydberg atom/attachments/rabi_oscillation_detuned.py",
    "Rydberg atom/attachments/rabi_freq_vs_intensity.py",
    "Rydberg atom/attachments/learning-progress-2026-06-02.py",
    "Rydberg atom/attachments/learning-progress-2026-06-10.py",
    "tools/gen_progress_chart.py",
    "tools/plot_learning_progress.py",
]

# Functions exercised in addition to import for the main- guarded script.
_MAIN_GUARDED_EXTRA = {
    "Handout by AI/generate_assets.py": (
        "plot_rabi_oscillations",
        "plot_rydberg_blockade",
        "plot_gate_waveforms",
        "simulate_dark_state_physics",
    ),
}


def _slug(rel_path: str) -> str:
    return pathlib.Path(rel_path).stem.replace("-", "_").replace(" ", "_")


@pytest.mark.parametrize("script", PLOT_SCRIPTS)
def test_plot_script_builds_figure(script, monkeypatch):
    # Block every possible file write and interactive show.
    monkeypatch.setattr(plt, "savefig", lambda *a, **k: None)
    monkeypatch.setattr(plt, "show", lambda *a, **k: None)

    path = (ROOT / script).resolve()
    assert path.is_file(), f"generator script missing: {script}"

    module_name = f"vault_plot_{_slug(script)}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # main-guarded scripts did not plot on import; exercise their functions.
    for fn in _MAIN_GUARDED_EXTRA.get(script, ()):
        getattr(module, fn)()
