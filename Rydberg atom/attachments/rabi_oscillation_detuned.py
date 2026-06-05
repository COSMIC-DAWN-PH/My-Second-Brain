"""
Detuned Rabi Oscillation: P_1(t) for different detuning values
"""
import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
t = np.linspace(0, 6 * np.pi, 1200)  # t in units of 1/Omega
delta_over_omega = [0, 0.5, 1.0, 2.0]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
styles = ['-', '--', ':', '-.']
labels = [r'$\Delta/\Omega = 0$', r'$\Delta/\Omega = 0.5$',
          r'$\Delta/\Omega = 1$', r'$\Delta/\Omega = 2$']

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 5))

for d, c, ls, lab in zip(delta_over_omega, colors, styles, labels):
    omega_tilde = np.sqrt(1 + d**2)  # normalized generalised Rabi freq
    amplitude = 1.0 / (1 + d**2)     # (Omega / Omega_tilde)^2
    P1 = amplitude * np.sin(omega_tilde * t / 2) ** 2
    ax.plot(t / np.pi, P1, color=c, ls=ls, lw=2.5, label=lab)

# Formatting
ax.set_xlabel(r'Time  $t \cdot \Omega / \pi$', fontsize=13)
ax.set_ylabel(r'$P_{|1\rangle}(t)$', fontsize=13)
ax.set_title('Effect of Detuning on Rabi Oscillation', fontsize=15, fontweight='bold', pad=12)
ax.set_xlim(0, 6)
ax.set_ylim(-0.03, 1.08)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
ax.legend(fontsize=11, loc='upper right', frameon=False)
ax.grid(alpha=0.3, ls=':')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('C:/Personal Profile/Profile/ScienceResearch/Quantum Computing/Rydberg atom/attachments/rabi_oscillation_detuned.png',
            dpi=180, bbox_inches='tight')
plt.close()
print("Done: rabi_oscillation_detuned.png")
