import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Data: 25 notes sorted by tier, then by comprehension within tier
notes = [
    # Tier 0
    ('Qubit State', 'understood', 0),
    # Tier 1
    ('Pauli Matrices', 'getting there', 1),
    ('Tensor Product', 'getting there', 1),
    ('Optical Tweezers', "don't understand", 1),
    ('Basis Transform.', 'getting there', 1),
    # Tier 2
    ('Anti-Commutat.', 'vague', 2),
    ('Gate Eigenstates', 'getting there', 2),
    ('SU(2)/SO(3)', 'vague', 2),
    ('2-Qubit State', 'getting there', 2),
    ('Single-Q Gates', 'getting there', 2),
    # Tier 3
    ('AC Stark Effect', "don't understand", 3),
    ('Rabi Flopping', 'vague', 3),
    ('Zeno Effect', 'vague', 3),
    ('Entangling Gate', 'vague', 3),
    ('2-Qubit Gates', 'getting there', 3),
    # Tier 4
    ('Grover Search', "don't understand", 4),
    ('QPE', "don't understand", 4),
    ('CZ Gate', 'getting there', 4),
    # Tier 5
    ('Rydberg Block.', "don't understand", 5),
    ('QEC', 'vague', 5),
    # Tier 6
    ('Surface Code', 'vague', 6),
    ('Transvers. Gate', 'vague', 6),
    ('Neutral Atom', 'vague', 6),
    # Tier 7
    ('Transv. Telep.', "don't understand", 7),
    # Tier 8
    ('Deep Circuit', "don't understand", 8),
]

colors_map = {
    'understood': '#2ca02c',
    'getting there': '#1f77b4',
    'vague': '#ff7f0e',
    "don't understand": '#d62728',
}

labels = [n[0] for n in notes]
comprehensions = [n[1] for n in notes]
tiers = [n[2] for n in notes]
bar_colors = [colors_map[c] for c in comprehensions]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), gridspec_kw={'width_ratios': [3, 1]})

# Left: horizontal bar chart
y_pos = np.arange(len(notes))
bars = ax1.barh(y_pos, [1]*len(notes), color=bar_colors, edgecolor='white', linewidth=0.5, height=0.7)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(labels, fontsize=9)
ax1.invert_yaxis()
ax1.set_xlim(0, 1.15)
ax1.set_xticks([])
ax1.set_title('Comprehension by Note (grouped by Tier)', fontsize=13, fontweight='bold', pad=12)

# Add tier separators and labels
prev_tier = -1
for i, t in enumerate(tiers):
    if t != prev_tier:
        if prev_tier != -1:
            ax1.axhline(y=i - 0.5, color='#cccccc', linewidth=0.8, linestyle='--')
        ax1.text(1.02, i, f'T{t}', fontsize=8, color='#666666', va='center')
        prev_tier = t

# Add comprehension labels on bars
short_map = {
    'understood': 'OK',
    'getting there': '~OK',
    'vague': '?',
    "don't understand": 'X',
}
for i, c in enumerate(comprehensions):
    ax1.text(0.5, i, short_map[c], ha='center', va='center', fontsize=8, color='white', fontweight='bold')

# Right: pie chart
comp_counts = {'understood': 0, 'getting there': 0, 'vague': 0, "don't understand": 0}
for c in comprehensions:
    comp_counts[c] += 1

pie_labels = ['Understood', 'Getting There', 'Vague', "Don't Understand"]
pie_sizes = [comp_counts['understood'], comp_counts['getting there'], comp_counts['vague'], comp_counts["don't understand"]]
pie_colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']

wedges, texts, autotexts = ax2.pie(
    pie_sizes, labels=pie_labels, colors=pie_colors, autopct='%1.0f%%',
    startangle=90, textprops={'fontsize': 9},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
)
for t in autotexts:
    t.set_fontsize(10)
    t.set_fontweight('bold')

ax2.set_title(
    'Comprehension Distribution (n=25)\nWeighted Progress: 54%',
    fontsize=12, fontweight='bold', pad=12
)

# Legend
legend_elements = [
    Patch(facecolor='#2ca02c', label='Understood (4pts)'),
    Patch(facecolor='#1f77b4', label='Getting There (3pts)'),
    Patch(facecolor='#ff7f0e', label='Vague (2pts)'),
    Patch(facecolor='#d62728', label="Don't Understand (1pt)"),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=4, fontsize=9, frameon=False,
           bbox_to_anchor=(0.5, 0.01))

fig.suptitle('Learning Progress - Neutral Atom Quantum Computing', fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.grid(alpha=0.3, ls=':')

outpath = 'Rydberg atom/attachments/learning-progress-2026-06-04.png'
plt.savefig(outpath, dpi=150, bbox_inches='tight', facecolor='white')
print(f'Chart saved to: {outpath}')
