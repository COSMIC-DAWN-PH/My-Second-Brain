"""Rabi oscillations: resonant vs detuned drive.

Two-level atom driven by a classical field. Population of the excited
state oscillates at the generalized Rabi frequency
    Omega_eff = sqrt(Omega^2 + Delta^2)
with contrast reduced by (Omega / Omega_eff)^2 when detuned.
"""

import numpy as np
import matplotlib.pyplot as plt

Omega = 2 * np.pi * 1.0  # resonant Rabi frequency (MHz * 2pi)
detunings = [0.0, 1.0, 3.0]  # Delta / Omega ratios

t = np.linspace(0, 4, 800)  # time in units of 1/Omega * 2pi ... use us

plt.figure(figsize=(8, 4.5))
for ratio in detunings:
    Delta = ratio * Omega
    Omega_eff = np.sqrt(Omega**2 + Delta**2)
    P_e = (Omega / Omega_eff) ** 2 * np.sin(Omega_eff * t / 2) ** 2
    label = (
        r"Resonant $\Delta=0$"
        if ratio == 0
        else rf"Detuned $\Delta = {ratio:g}\,\Omega$"
    )
    plt.plot(t, P_e, lw=1.8, label=label)

plt.xlabel(r"Time ($\mu$s, $\Omega = 2\pi\times 1$ MHz)")
plt.ylabel(r"Excited-state population $P_e$")
plt.title("Rabi Oscillations: Resonant vs Detuned Drive")
plt.ylim(-0.02, 1.05)
plt.grid(alpha=0.3, ls=":")
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
