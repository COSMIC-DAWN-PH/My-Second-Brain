"""
Rabi Frequency vs Laser Intensity: Omega ~ sqrt(I)
"""
import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
I = np.linspace(0, 4, 500)  # normalized intensity I/I_0
Omega = np.sqrt(I)          # normalized Rabi frequency Omega/Omega_0

# --- Plot ---
fig, ax = plt.subplots(figsize=(8, 4.5))

ax.plot(I, Omega, color='#1f77b4', lw=2.5, label=r'$\Omega/\Omega_0 = \sqrt{I/I_0}$')

# Mark the I = 2 point
I_mark = 2.0
Omega_mark = np.sqrt(I_mark)
ax.plot(I_mark, Omega_mark, 'o', color='#ff7f0e', ms=9, zorder=5)
ax.annotate(f'$\\times 2$ intensity\n$\\Omega \\times \\sqrt{{2}} \\approx {Omega_mark:.2f}$',
            xy=(I_mark, Omega_mark),
            xytext=(I_mark + 0.4, Omega_mark - 0.15),
            fontsize=11, color='#333333',
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2))

# Formatting
ax.set_xlabel(r'Laser Intensity  $I / I_0$', fontsize=13)
ax.set_ylabel(r'Rabi Frequency  $\Omega / \Omega_0$', fontsize=13)
ax.set_title(r'Rabi Frequency $\propto \sqrt{\mathrm{Intensity}}$', fontsize=15, fontweight='bold', pad=12)
ax.set_xlim(0, 4.2)
ax.set_ylim(0, 2.15)
ax.legend(fontsize=11, loc='upper left', frameon=False)
ax.grid(alpha=0.3, ls=':')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('C:/Personal Profile/Profile/ScienceResearch/Quantum Computing/Rydberg atom/attachments/rabi_freq_vs_intensity.png',
            dpi=180, bbox_inches='tight')
plt.close()
print("Done: rabi_freq_vs_intensity.png")
