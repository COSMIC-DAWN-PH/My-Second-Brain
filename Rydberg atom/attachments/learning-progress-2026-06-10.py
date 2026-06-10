import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────────
COLORS = {
    "understood":       "#2ca02c",
    "getting there":    "#1f77b4",
    "vague":            "#ff7f0e",
    "don't understand": "#d62728",
}
SCORE = {
    "don't understand": 1,
    "vague":            2,
    "getting there":    3,
    "understood":       4,
}

# Tier assignments: (tier_label, [(note_short_name, comprehension_level)])
tier_data = [
    ("Tier 0: Qubit Basics", [
        ("Qubit-State-and-Superposition", "understood"),
    ]),
    ("Tier 1: Math & Platform", [
        ("Pauli-Matrices",           "getting there"),
        ("Tensor-Product",           "getting there"),
        ("Optical-Tweezer-Arrays",   "don't understand"),
        ("Basis-Transformation",     "getting there"),
        ("Fine-Structure",           "vague"),
    ]),
    ("Tier 2: Single & Two Qubit", [
        ("Hyperfine-Structure",              "getting there"),
        ("Zeeman-Effect",                    "vague"),
        ("Single-Qubit-Gates",               "getting there"),
        ("Two-Qubit-State-and-Entanglement", "getting there"),
        ("Gate-Eigenstates",                 "getting there"),
        ("Anti-Commutation",                 "vague"),
        ("SU2-SO3-and-Euler-Decomposition",  "vague"),
    ]),
    ("Tier 3: Gates & Effects", [
        ("Rabi-Flopping",       "vague"),
        ("AC-Stark-Effect",     "don't understand"),
        ("Quantum-Zeno-Effect", "vague"),
        ("Entangling-Gate",     "vague"),
        ("Two-Qubit-Gates",     "getting there"),
    ]),
    ("Tier 4: Algorithms", [
        ("Grover-Search",           "don't understand"),
        ("Quantum-Phase-Estimation","don't understand"),
        ("CZ-Gate",                 "getting there"),
    ]),
    ("Tier 5: Blockade & QEC", [
        ("Rydberg-Blockade", "don't understand"),
        ("QEC",              "vague"),
    ]),
    ("Tier 6: Surface Code", [
        ("Surface-Code",      "vague"),
        ("Transversal-Gate",  "vague"),
        ("Neutral_Atom_Test", "vague"),
    ]),
    ("Tier 7: Teleportation", [
        ("Transversal-Teleportation", "don't understand"),
    ]),
    ("Tier 8: Deep Circuit", [
        ("Deep-Circuit-Execution", "don't understand"),
    ]),
]

# ── Flatten data ──────────────────────────────────────────────────────────────
notes = []          # list of (note_name, level, tier_label)
tier_boundaries = []  # y-index where each tier starts
tier_labels = []
idx = 0
for tier_label, members in tier_data:
    tier_boundaries.append(idx)
    tier_labels.append(tier_label)
    for name, level in members:
        notes.append((name, level, tier_label))
        idx += 1

n_notes = len(notes)
y_positions = np.arange(n_notes)

# ── Build figure ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 12), facecolor="#fafbfc")
ax.set_facecolor("#fafbfc")

# Draw bars
for i, (name, level, _) in enumerate(notes):
    score = SCORE[level]
    ax.barh(
        i, score, height=0.7,
        color=COLORS[level], edgecolor="white", linewidth=1.2,
        zorder=2,
    )
    # Note name on y-axis
    ax.text(
        -0.05, i, name,
        ha="right", va="center", fontsize=8.5, color="#2d3436",
        zorder=3,
    )
    # Score label on bar
    ax.text(
        score + 0.05, i, str(score),
        ha="left", va="center", fontsize=9, fontweight="bold",
        color=COLORS[level], zorder=3,
    )

# Tier separator lines
for boundary in tier_boundaries[1:]:
    ax.axhline(y=boundary - 0.5, color="#b2bec3", linewidth=1.5, ls="--", zorder=1, alpha=0.7)

# Tier labels on right margin
for i, (boundary, label) in enumerate(zip(tier_boundaries, tier_labels)):
    if i < len(tier_boundaries) - 1:
        mid_y = (boundary + tier_boundaries[i + 1] - 1) / 2
    else:
        mid_y = (boundary + n_notes - 1) / 2
    ax.text(
        4.3, mid_y, label,
        ha="left", va="center", fontsize=9, fontweight="bold",
        color="#636e72", style="italic", zorder=3,
    )

# Axes formatting
ax.set_xlim(-0.1, 4.5)
ax.set_ylim(n_notes - 0.5, -0.5)  # invert so Tier 0 is at top
ax.set_yticks([])
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(
    ["1: Don't Understand", "2: Vague", "3: Getting There", "4: Understood"],
    fontsize=10, color="#2d3436",
)
ax.set_xlabel("Comprehension Level", fontsize=12, color="#2d3436", labelpad=10)
ax.set_title(
    "Learning Progress - Neutral Atom QC (2026-06-10)",
    fontsize=16, fontweight="bold", color="#2d3436", pad=15,
)
ax.grid(axis="x", alpha=0.3, ls=":", zorder=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# ── Legend ─────────────────────────────────────────────────────────────────────
# Count notes per level
counts = {}
for _, level, _ in notes:
    counts[level] = counts.get(level, 0) + 1

legend_patches = [
    mpatches.Patch(color=COLORS["understood"],       label=f"Understood ({counts.get('understood', 0)})"),
    mpatches.Patch(color=COLORS["getting there"],    label=f"Getting There ({counts.get('getting there', 0)})"),
    mpatches.Patch(color=COLORS["vague"],            label=f"Vague ({counts.get('vague', 0)})"),
    mpatches.Patch(color=COLORS["don't understand"], label=f"Don't Understand ({counts.get('don\'t understand', 0)})"),
]
fig.legend(
    handles=legend_patches,
    loc="lower center",
    ncol=4,
    fontsize=11,
    frameon=False,
    bbox_to_anchor=(0.5, 0.01),
)

# ── Summary stats ─────────────────────────────────────────────────────────────
total = n_notes
weighted = sum(SCORE[level] for _, level, _ in notes)
pct = weighted / (total * 4) * 100
fig.text(
    0.5, 0.04,
    f"Total: {total} notes  |  Weighted Progress: {pct:.0f}%",
    ha="center", fontsize=11, color="#636e72",
)

# ── Save ──────────────────────────────────────────────────────────────────────
plt.tight_layout(rect=[0, 0.07, 1, 0.97])
plt.savefig(
    r"C:\Personal Profile\Profile\ScienceResearch\Quantum Computing\Rydberg atom\attachments\learning-progress-2026-06-10.png",
    dpi=150, bbox_inches="tight", facecolor="#fafbfc",
)
print(f"Chart saved. {total} notes, weighted progress: {pct:.0f}%")
