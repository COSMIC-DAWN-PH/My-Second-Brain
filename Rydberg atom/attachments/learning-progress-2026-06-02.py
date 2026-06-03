import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────────
LEVELS = ["understood", "getting there", "vague", "don't understand"]
COLORS = {
    "understood":       "#2ca02c",
    "getting there":    "#1f77b4",
    "vague":            "#ff7f0e",
    "don't understand": "#d62728",
}

tier_data = {
    "Tier 0\nQubit Basics": {
        "understood": ["Qubit-State"],
        "getting there": [],
        "vague": [],
        "don't understand": [],
    },
    "Tier 1\nMath & Platform": {
        "understood": [],
        "getting there": ["Pauli-Matrices"],
        "vague": ["Tensor-Product"],
        "don't understand": ["AC-Stark-Effect"],
    },
    "Tier 2\nSingle & Two Qubit": {
        "understood": [],
        "getting there": ["Single-Qubit", "Two-Qubit-State"],
        "vague": ["Gate-Eigenstates", "Optical-Tweezers"],
        "don't understand": [],
    },
    "Tier 3\nGates & Blockade": {
        "understood": [],
        "getting there": ["Two-Qubit-Gates"],
        "vague": ["Rabi-Flopping", "Anti-Commut.", "CZ-Gate", "QZE"],
        "don't understand": ["Rydberg-Blockade"],
    },
    "Tier 4\nAlgorithms & QEC": {
        "understood": [],
        "getting there": [],
        "vague": ["QEC", "Surface-Code", "Transversal-Gate", "Neutral-Atom"],
        "don't understand": ["Grover", "QPE"],
    },
    "Tier 5\nFault Tolerance": {
        "understood": [],
        "getting there": [],
        "vague": [],
        "don't understand": ["Transversal-Tele.", "Deep-Circuit"],
    },
}

# ── Build figure ──────────────────────────────────────────────────────────────
fig, (ax_main, ax_detail) = plt.subplots(
    1, 2, figsize=(16, 9),
    gridspec_kw={"width_ratios": [3, 2], "wspace": 0.28},
    facecolor="#fafbfc",
)
ax_main.set_facecolor("#fafbfc")
ax_detail.set_facecolor("#fafbfc")

tier_names = list(tier_data.keys())
n_tiers = len(tier_names)
y_positions = np.arange(n_tiers)

# ── Left panel: stacked bar ──────────────────────────────────────────────────
for i, (tier_name, counts) in enumerate(tier_data.items()):
    left = 0
    total = sum(len(v) for v in counts.values())
    for level in LEVELS:
        notes = counts[level]
        width = len(notes)
        if width > 0:
            ax_main.barh(
                i, width, left=left, height=0.55,
                color=COLORS[level], edgecolor="white", linewidth=1.5,
                zorder=2,
            )
            # Add count label inside the segment
            if width >= 1:
                ax_main.text(
                    left + width / 2, i,
                    str(width),
                    ha="center", va="center",
                    fontsize=13, fontweight="bold", color="white",
                    zorder=3,
                )
            left += width

    # Tier label & total
    ax_main.text(
        -0.15, i, tier_name,
        ha="right", va="center", fontsize=11, fontweight="bold",
        color="#2d3436",
    )
    ax_main.text(
        total + 0.15, i, f"{total}",
        ha="left", va="center", fontsize=10, fontweight="bold",
        color="#636e72",
    )

ax_main.set_yticks([])
ax_main.set_xlim(0, 7)
ax_main.set_ylim(-0.6, n_tiers - 0.4)
ax_main.invert_yaxis()
ax_main.set_xlabel("Number of Notes", fontsize=12, color="#2d3436")
ax_main.set_title(
    "Comprehension by Tier",
    fontsize=14, fontweight="bold", color="#2d3436", pad=15,
)
ax_main.grid(axis="x", alpha=0.3, ls=":", zorder=0)
ax_main.spines["top"].set_visible(False)
ax_main.spines["right"].set_visible(False)

# ── Right panel: note-level detail ───────────────────────────────────────────
note_details = [
    ("Qubit-State", "understood", 0),
    ("Pauli-Matrices", "getting there", 1),
    ("Tensor-Product", "vague", 1),
    ("AC-Stark-Effect", "don't understand", 1),
    ("Single-Qubit-Gates", "getting there", 2),
    ("Two-Qubit-State", "getting there", 2),
    ("Gate-Eigenstates", "vague", 2),
    ("Optical-Tweezers", "vague", 2),
    ("Two-Qubit-Gates", "getting there", 3),
    ("Rabi-Flopping", "vague", 3),
    ("Anti-Commutation", "vague", 3),
    ("CZ-Gate", "vague", 3),
    ("QZE", "vague", 3),
    ("Rydberg-Blockade", "don't understand", 3),
    ("QEC", "vague", 4),
    ("Surface-Code", "vague", 4),
    ("Transversal-Gate", "vague", 4),
    ("Neutral-Atom-Test", "vague", 4),
    ("Grover-Search", "don't understand", 4),
    ("QPE", "don't understand", 4),
    ("Transversal-Tele.", "don't understand", 5),
    ("Deep-Circuit", "don't understand", 5),
]

y_note = np.arange(len(note_details))
labels = [d[0] for d in note_details]
colors = [COLORS[d[1]] for d in note_details]

ax_detail.barh(y_note, 1, height=0.65, color=colors, edgecolor="white", linewidth=1.2, zorder=2)

for idx, (name, level, _) in enumerate(note_details):
    ax_detail.text(0.02, idx, name, ha="left", va="center", fontsize=8.5, color="white", fontweight="bold", zorder=3)

ax_detail.set_yticks([])
ax_detail.set_xlim(0, 1.0)
ax_detail.set_ylim(-0.5, len(note_details) - 0.5)
ax_detail.invert_yaxis()
ax_detail.set_title(
    "All 22 Knowledge Notes",
    fontsize=14, fontweight="bold", color="#2d3436", pad=15,
)
ax_detail.spines["top"].set_visible(False)
ax_detail.spines["right"].set_visible(False)
ax_detail.spines["bottom"].set_visible(False)
ax_detail.set_xticks([])

# ── Legend ─────────────────────────────────────────────────────────────────────
legend_patches = [
    mpatches.Patch(color=COLORS["understood"],       label=f"Understood (1)"),
    mpatches.Patch(color=COLORS["getting there"],    label=f"Getting There (6)"),
    mpatches.Patch(color=COLORS["vague"],            label=f"Vague (8)"),
    mpatches.Patch(color=COLORS["don't understand"], label=f"Don't Understand (7)"),
]
fig.legend(
    handles=legend_patches,
    loc="lower center",
    ncol=4,
    fontsize=11,
    frameon=False,
    bbox_to_anchor=(0.5, 0.01),
)

# ── Final ─────────────────────────────────────────────────────────────────────
fig.suptitle(
    "Learning Progress — Neutral-Atom Quantum Computing  |  Overall: 45%",
    fontsize=16, fontweight="bold", color="#2d3436", y=0.98,
)
plt.tight_layout(rect=[0, 0.06, 1, 0.94])
plt.savefig(
    r"C:\Personal Profile\Profile\ScienceResearch\Quantum Computing\Rydberg atom\attachments\learning-progress-2026-06-02.png",
    dpi=180, bbox_inches="tight", facecolor="#fafbfc",
)
print("Chart saved successfully.")
