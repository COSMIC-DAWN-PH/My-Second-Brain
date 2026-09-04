"""Generate the 2026-09-04 learning-progress snapshot."""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


COLORS = {
    "understood": "#2ca02c",
    "getting there": "#1f77b4",
    "vague": "#ff7f0e",
    "don't understand": "#d62728",
}
SCORE = {
    "don't understand": 1,
    "vague": 2,
    "getting there": 3,
    "understood": 4,
}

# Canonical graph notes are grouped by computed dependency tier. Supplementary
# notes are shown separately and do not receive a fabricated canonical tier.
tier_data = [
    ("Tier 0: Qubit Basics", [
        ("Qubit-State-and-Superposition", "understood"),
    ]),
    ("Tier 1: Math & Platform", [
        ("Optical-Tweezer-Arrays", "don't understand"),
        ("Tensor-Product", "getting there"),
        ("Pauli-Matrices", "getting there"),
    ]),
    ("Tier 2: Single & Two Qubit", [
        ("Anti-Commutation", "vague"),
        ("Two-Qubit-State-and-Entanglement", "getting there"),
        ("Single-Qubit-Gates", "getting there"),
        ("Gate-Eigenstates", "getting there"),
    ]),
    ("Tier 3: Dynamics & Gates", [
        ("AC-Stark-Effect", "don't understand"),
        ("Rabi-Flopping", "vague"),
        ("Quantum-Zeno-Effect", "vague"),
        ("Two-Qubit-Gates", "getting there"),
    ]),
    ("Tier 4: Algorithms & CZ", [
        ("Grover-Search", "don't understand"),
        ("Quantum-Phase-Estimation", "don't understand"),
        ("CZ-Gate", "getting there"),
    ]),
    ("Tier 5: Blockade & QEC", [
        ("Rydberg-Blockade", "don't understand"),
        ("QEC", "vague"),
    ]),
    ("Tier 6: Fault Tolerance & Platform", [
        ("Surface-Code", "vague"),
        ("Transversal-Gate", "vague"),
        ("Neutral_Atom_Test", "vague"),
    ]),
    ("Tier 7: Teleportation", [
        ("Transversal-Teleportation", "don't understand"),
    ]),
    ("Tier 8: Deep Circuit", [
        ("Deep-Circuit-Execution", "don't understand"),
    ]),
    ("Supplementary Notes", [
        ("Basis-Transformation", "getting there"),
        ("SU2-SO3-and-Euler-Decomposition", "vague"),
        ("Entangling-Gate", "vague"),
        ("Fine-Structure", "vague"),
        ("Hyperfine-Structure", "getting there"),
        ("Zeeman-Effect", "vague"),
        ("Color-Code", "vague"),
    ]),
]

notes = []
tier_boundaries = []
tier_labels = []
index = 0
for tier_label, members in tier_data:
    tier_boundaries.append(index)
    tier_labels.append(tier_label)
    for name, level in members:
        notes.append((name, level, tier_label))
        index += 1

n_notes = len(notes)
y_positions = np.arange(n_notes)

fig, ax = plt.subplots(figsize=(15, 14), facecolor="#fafbfc")
ax.set_facecolor("#fafbfc")

for i, (name, level, _) in enumerate(notes):
    score = SCORE[level]
    ax.barh(
        i,
        score,
        height=0.7,
        color=COLORS[level],
        edgecolor="white",
        linewidth=1.2,
        zorder=2,
    )
    ax.text(
        -0.05,
        i,
        name,
        ha="right",
        va="center",
        fontsize=8.5,
        color="#2d3436",
        zorder=3,
    )
    ax.text(
        score + 0.05,
        i,
        str(score),
        ha="left",
        va="center",
        fontsize=9,
        fontweight="bold",
        color=COLORS[level],
        zorder=3,
    )

for boundary in tier_boundaries[1:]:
    ax.axhline(
        y=boundary - 0.5,
        color="#b2bec3",
        linewidth=1.5,
        ls="--",
        zorder=1,
        alpha=0.7,
    )

for i, (boundary, label) in enumerate(zip(tier_boundaries, tier_labels)):
    next_boundary = tier_boundaries[i + 1] if i + 1 < len(tier_boundaries) else n_notes
    mid_y = (boundary + next_boundary - 1) / 2
    ax.text(
        4.28,
        mid_y,
        label,
        ha="left",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#636e72",
        style="italic",
        zorder=3,
    )

ax.set_xlim(-0.1, 5.0)
ax.set_ylim(n_notes - 0.5, -0.5)
ax.set_yticks([])
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(
    [
        "1: Don't Understand",
        "2: Vague",
        "3: Getting There",
        "4: Understood",
    ],
    fontsize=10,
    color="#2d3436",
)
ax.set_xlabel("Comprehension Level", fontsize=12, color="#2d3436", labelpad=10)
ax.set_title(
    "Learning Progress - Neutral Atom Quantum Computing (2026-09-04)",
    fontsize=16,
    fontweight="bold",
    color="#2d3436",
    pad=15,
)
plt.sca(ax)
plt.grid(alpha=0.3, ls=":", zorder=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

counts = {level: 0 for level in SCORE}
for _, level, _ in notes:
    counts[level] += 1

legend_patches = [
    mpatches.Patch(color=COLORS["understood"], label=f"Understood ({counts['understood']})"),
    mpatches.Patch(color=COLORS["getting there"], label=f"Getting There ({counts['getting there']})"),
    mpatches.Patch(color=COLORS["vague"], label=f"Vague ({counts['vague']})"),
    mpatches.Patch(color=COLORS["don't understand"], label=f"Don't Understand ({counts["don't understand"]})"),
]
fig.legend(
    handles=legend_patches,
    loc="lower center",
    ncol=4,
    fontsize=11,
    frameon=False,
    bbox_to_anchor=(0.5, 0.01),
)

weighted = sum(SCORE[level] for _, level, _ in notes)
pct = weighted / (n_notes * 4) * 100
fig.text(
    0.5,
    0.04,
    f"Total: {n_notes} classified notes  |  Weighted Progress: {pct:.0f}%  |  1 metadata-incomplete file excluded",
    ha="center",
    fontsize=11,
    color="#636e72",
)

plt.tight_layout(rect=[0, 0.07, 1, 0.97])
plt.savefig(
    Path(__file__).with_suffix(".png"),
    dpi=150,
    bbox_inches="tight",
    facecolor="#fafbfc",
)
print(f"Chart saved. {n_notes} classified notes, weighted progress: {pct:.0f}%")