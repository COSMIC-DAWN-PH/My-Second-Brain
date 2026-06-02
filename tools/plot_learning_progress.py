import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data: comprehension counts per tier
# Order: [understood, getting_there, vague, dont_understand]
tiers = [
    'Tier 0\nFoundation',
    'Tier 1\nMath & Platform',
    'Tier 2\nGate Operations',
    'Tier 3\nPhysical Impl.',
    'Tier 4\nEntangling Gate',
    'Tier 5\nSystem & QEC',
    'Tier 6\nAdvanced',
    'Tier 7\nDeep FT',
]

data = [
    [1, 0, 0, 0],  # Tier 0
    [0, 1, 2, 0],  # Tier 1
    [0, 2, 2, 0],  # Tier 2
    [0, 1, 2, 1],  # Tier 3
    [0, 0, 1, 1],  # Tier 4
    [0, 0, 2, 0],  # Tier 5
    [0, 0, 2, 2],  # Tier 6
    [0, 0, 0, 2],  # Tier 7
]

colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']
labels = ['Understood', 'Getting There', 'Vague', 'Dont Understand']

fig, ax = plt.subplots(figsize=(13, 7))

y_pos = np.arange(len(tiers))
bar_height = 0.6

# Build stacked horizontal bars
lefts = np.zeros(len(tiers))
for i, (label, color) in enumerate(zip(labels, colors)):
    values = [row[i] for row in data]
    ax.barh(y_pos, values, bar_height, left=lefts, color=color, label=label, edgecolor='white', linewidth=0.5)
    # Add count labels inside bars
    for j, (v, l) in enumerate(zip(values, lefts)):
        if v > 0:
            ax.text(l + v / 2, y_pos[j], str(v), ha='center', va='center',
                    fontsize=12, fontweight='bold', color='white')
    lefts += values

# Add total count at end of each bar
totals = [sum(row) for row in data]
for i, total in enumerate(totals):
    ax.text(lefts[i] + 0.15, y_pos[i], f'{total} notes',
            ha='left', va='center', fontsize=10, color='#555555')

ax.set_yticks(y_pos)
ax.set_yticklabels(tiers, fontsize=10)
ax.set_xlabel('Number of Knowledge Notes', fontsize=12)
ax.set_title('Learning Progress by Dependency Tier', fontsize=15, fontweight='bold', pad=15)
ax.legend(loc='lower right', frameon=False, fontsize=10)
ax.set_xlim(0, max(totals) + 1.5)
ax.grid(axis='x', alpha=0.3, ls=':')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.invert_yaxis()

plt.tight_layout()
plt.savefig('Rydberg atom/attachments/learning-progress-2026-06-02.png', dpi=150, bbox_inches='tight')
print('Chart saved successfully.')
