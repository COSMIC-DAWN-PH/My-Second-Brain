"""
Resonant Rabi Oscillation: P_0(t) and P_1(t) vs time
"""
import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
t = np.linspace(0, 2 * np.pi, 1000)  # t in units of 1/Omega, so Omega*t goes 0..2pi

# Probabilities
P0 = np.cos(t / 2) ** 2
P1 = np.sin(t / 2) ** 2

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(t / np.pi, P0, color='#1f77b4', lw=2.5, label=r'$P_{|0\rangle}(t) = \cos^2(\Omega t/2)$')
ax.plot(t / np.pi, P1, color='#d62728', lw=2.5, label=r'$P_{|1\rangle}(t) = \sin^2(\Omega t/2)$')

# Annotate pi/2 and pi pulse times
for t_mark, label in [(0.5, r'$\pi/2$ pulse'), (1.0, r'$\pi$ pulse')]:
    ax.axvline(x=t_mark, color='gray', ls='--', lw=1.2, alpha=0.6)
    ax.annotate(label,
                xy=(t_mark, 0.5), xytext=(t_mark + 0.06, 0.62),
                fontsize=11, color='#333333',
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2))

# Mark key points
ax.plot(0.5, 0.5, 'o', color='#ff7f0e', ms=8, zorder=5)
ax.plot(1.0, 1.0, 'o', color='#ff7f0e', ms=8, zorder=5)
ax.plot(1.0, 0.0, 'o', color='#ff7f0e', ms=8, zorder=5)

# Formatting
ax.set_xlabel(r'Time  $t \cdot \Omega / \pi$', fontsize=13)
ax.set_ylabel('Population', fontsize=13)
ax.set_title('Resonant Rabi Oscillation ($\\Delta = 0$)', fontsize=15, fontweight='bold', pad=12)
ax.set_xlim(0, 2)
ax.set_ylim(-0.03, 1.08)
ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_xticklabels(['0', r'$\frac{1}{2}$', '1', r'$\frac{3}{2}$', '2'])
ax.legend(fontsize=11, loc='center right', frameon=False)
ax.grid(alpha=0.3, ls=':')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('C:/Personal Profile/Profile/ScienceResearch/Quantum Computing/Rydberg atom/attachments/rabi_oscillation_resonant.png',
            dpi=180, bbox_inches='tight')
plt.close()
print("Done: rabi_oscillation_resonant.png")
