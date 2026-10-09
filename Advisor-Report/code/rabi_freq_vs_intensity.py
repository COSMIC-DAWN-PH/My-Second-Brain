"""Rabi frequency vs laser intensity.

Omega = d * E / hbar, and intensity I is proportional to E^2,
so Omega scales as sqrt(I). This is the standard calibration curve
used to set pulse areas in the lab.
"""

import numpy as np
import matplotlib.pyplot as plt

I = np.linspace(0, 10, 200)  # intensity (arb. units)
Omega = 2 * np.pi * 3.0 * np.sqrt(I / 10)  # MHz * 2pi, calibrated at I=10

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(I, Omega / (2 * np.pi), lw=2, color="tab:blue")
axes[0].set_xlabel("Laser intensity $I$ (arb. units)")
axes[0].set_ylabel(r"Rabi frequency $\Omega/2\pi$ (MHz)")
axes[0].set_title(r"Calibration: $\Omega \propto \sqrt{I}$")
axes[0].grid(alpha=0.3, ls=":")

# pulse duration for a pi pulse vs intensity (skip I=0 to avoid division by zero)
with np.errstate(divide="ignore", invalid="ignore"):
    t_pi = np.pi / Omega  # us
t_pi[I == 0] = np.nan
axes[1].plot(I[1:], t_pi[1:] * 1e0, lw=2, color="tab:red")
axes[1].set_xlabel("Laser intensity $I$ (arb. units)")
axes[1].set_ylabel(r"$\pi$-pulse duration $t_\pi$ ($\mu$s)")
axes[1].set_title(r"$\pi$-pulse time $t_\pi = \pi/\Omega$")
axes[1].grid(alpha=0.3, ls=":")

plt.tight_layout()
plt.show()
