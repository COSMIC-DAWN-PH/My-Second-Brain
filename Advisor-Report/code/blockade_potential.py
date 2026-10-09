"""Rydberg blockade potential.

Van der Waals interaction between two Rydberg atoms:
    V(R) = C6 / R^6
Blockade sets in when V >> Omega. The blockade radius
    R_b = (C6 / Omega)^(1/6)
marks the crossover. Distances below R_b: only one atom can be excited.
"""

import numpy as np
import matplotlib.pyplot as plt

# Typical numbers for Rb-87 n=60 S-state (order of magnitude)
C6 = 2 * np.pi * 1000.0  # MHz * um^6 (illustrative)
Omega = 2 * np.pi * 5.0  # MHz * 2pi -> use MHz consistently below

C6_MHz = C6 / (2 * np.pi)  # 1000 MHz um^6
Omega_MHz = Omega / (2 * np.pi)  # 5 MHz

R = np.linspace(2, 10, 500)  # um
V = C6_MHz / R**6  # MHz

R_b = (C6_MHz / Omega_MHz) ** (1 / 6)

plt.figure(figsize=(8, 4.5))
plt.semilogy(R, V, lw=2, color="tab:purple", label=r"$V(R) = C_6/R^6$")
plt.axhline(Omega_MHz, color="tab:red", ls="--", lw=1.5,
            label=rf"$\Omega/2\pi = {Omega_MHz:g}$ MHz")
plt.axvline(R_b, color="gray", ls=":", lw=1.5,
            label=rf"Blockade radius $R_b \approx {R_b:.1f}\,\mu$m")

plt.fill_between(R, V, Omega_MHz, where=(V > Omega_MHz),
                 color="tab:purple", alpha=0.12, label="Blockaded region")

plt.xlabel(r"Interatomic distance $R$ ($\mu$m)")
plt.ylabel(r"Interaction $V/2\pi$ (MHz)")
plt.title(r"Rydberg Blockade: $V \gg \Omega$ inside $R_b$")
plt.grid(alpha=0.3, ls=":")
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
