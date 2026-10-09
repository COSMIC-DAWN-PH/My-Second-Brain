"""Blockade suppression scan: double-excitation population vs V/Omega.

Two atoms both driven with Rabi frequency Omega. In the truncated basis
{|gg>, |W> = (|gr>+|rg>)/sqrt(2), |rr>}, the symmetric bright state |W>
couples to |gg> with sqrt(2) Omega/2 and to |rr> with sqrt(2) Omega/2.
The |rr> state is shifted by V. Starting from |gg>, we compute the
maximum double-excitation population as a function of V/Omega.

Expected scaling: P_rr ~ (Omega/V)^2 for V >> Omega (blockade).
"""

import numpy as np
import matplotlib.pyplot as plt

Omega = 1.0  # work in units of Omega

def max_double_excitation(V_over_Omega, t_max=20.0, n_t=2000):
    V = V_over_Omega * Omega
    # Hamiltonian in units of Omega, basis {|gg>, |W>, |rr>}
    s2 = np.sqrt(2) / 2
    H = np.array([
        [0.0, s2 * Omega, 0.0],
        [s2 * Omega, 0.0, s2 * Omega],
        [0.0, s2 * Omega, V],
    ])
    evals, evecs = np.linalg.eigh(H)
    psi0 = np.array([1.0, 0.0, 0.0], dtype=complex)
    c0 = evecs.conj().T @ psi0

    t = np.linspace(0, t_max / Omega, n_t)
    # psi(t) = evecs @ (exp(-i E t) * c0)
    phases = np.exp(-1j * np.outer(t, evals))
    psi_t = (phases * c0) @ evecs.conj().T
    P_rr = np.abs(psi_t[:, 2]) ** 2
    return P_rr.max()

V_ratios = np.logspace(0, 2.3, 25)
P_max = np.array([max_double_excitation(v) for v in V_ratios])

plt.figure(figsize=(8, 4.5))
plt.loglog(V_ratios, P_max, "o-", lw=2, color="tab:purple",
           label="Numerical: max $P_{rr}$")
plt.loglog(V_ratios, 0.5 / V_ratios**2, "--", lw=1.5, color="gray",
           label=r"Scaling $\sim (\Omega/V)^2$")

plt.xlabel(r"Blockade strength $V/\Omega$")
plt.ylabel(r"Max double-excitation population $P_{rr}$")
plt.title("Rydberg Blockade Suppression: $P_{rr}$ vs $V/\\Omega$")
plt.grid(alpha=0.3, ls=":")
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
