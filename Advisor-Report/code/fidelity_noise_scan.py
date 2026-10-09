"""Fidelity sensitivity scan for a Rydberg CZ gate.

Simple error budget model: gate infidelity contributions from
  - laser detuning noise (off-resonant drive)
  - Rydberg state decay during the gate
  - imperfect blockade (finite V/Omega)

Each term is plotted separately to show which noise dominates.
Analytic estimates, order-of-magnitude level.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Detuning error: area error of a pi pulse, P_error ~ (Delta/Omega)^2 / 2
delta_over_omega = np.linspace(0, 0.3, 200)
infid_detuning = 0.5 * delta_over_omega**2

# 2. Decay error: infidelity ~ t_gate / tau (Rydberg lifetime)
t_gate = 0.5  # us
tau = np.linspace(20, 200, 200)  # us, Rydberg lifetime
infid_decay = t_gate / tau

# 3. Blockade error: leakage ~ (Omega/V)^2 (order of magnitude)
v_over_omega = np.linspace(5, 100, 200)
infid_blockade = 1.0 / v_over_omega**2

fig, axes = plt.subplots(1, 3, figsize=(13, 4))

axes[0].semilogy(delta_over_omega * 100, infid_detuning, lw=2, color="tab:blue")
axes[0].set_xlabel(r"Detuning noise $\Delta/\Omega$ (%)")
axes[0].set_ylabel("Gate infidelity")
axes[0].set_title("Detuning error")
axes[0].grid(alpha=0.3, ls=":")

axes[1].semilogy(tau, infid_decay, lw=2, color="tab:red")
axes[1].set_xlabel(r"Rydberg lifetime $\tau$ ($\mu$s)")
axes[1].set_title(r"Decay error ($t_{\rm gate}=0.5\,\mu$s)")
axes[1].grid(alpha=0.3, ls=":")

axes[2].loglog(v_over_omega, infid_blockade, lw=2, color="tab:purple")
axes[2].set_xlabel(r"Blockade strength $V/\Omega$")
axes[2].set_title("Imperfect-blockade leakage")
axes[2].grid(alpha=0.3, ls=":")

for ax in axes:
    ax.axhline(1e-2, color="gray", ls="--", lw=1)
    ax.axhline(1e-3, color="gray", ls=":", lw=1)

plt.suptitle("CZ Gate Error Budget: Which Noise Dominates?", y=1.02)
plt.tight_layout()
plt.show()
