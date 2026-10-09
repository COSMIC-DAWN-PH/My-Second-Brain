"""QuTiP simulation of a Rydberg-blockade CZ gate.

Protocol (Saffman-style pulse sequence):
  1. pi-pulse on the control atom   (|1> -> |r>)
  2. 2pi-pulse on the target atom   (blocked if control is in |r>)
  3. pi-pulse on the control atom   (|r> -> |1>)

If the control was in |1>, the target's 2pi rotation is blocked by the
interaction V, so the target picks up no phase; if the control was in
|0>, the target completes a 2pi cycle and picks up a pi phase.
Net effect: |11> acquires a pi phase -> CZ up to single-qubit phases.

We track computational-basis populations for the input |11>.
"""

import numpy as np
import matplotlib.pyplot as plt
import qutip as qt

# Single-atom basis: |g> = |1> (coupled to Rydberg), |r>
g = qt.basis(2, 0)
r = qt.basis(2, 1)
sm = g * r.dag()  # |g><r|

I2 = qt.qeye(2)

def op_on_atom(op, atom):
    """Embed a single-atom operator into the two-atom space."""
    return qt.tensor(op, I2) if atom == 0 else qt.tensor(I2, op)

# Drive Hamiltonians (Omega/2)(|r><g| + |g><r|) on each atom
H1 = op_on_atom(sm + sm.dag(), 0)  # control
H2 = op_on_atom(sm + sm.dag(), 1)  # target

# Interaction: V |rr><rr|
rr = qt.tensor(r, r)
H_int = rr * rr.dag()

Omega = 2 * np.pi * 5.0   # MHz * 2pi
V = 2 * np.pi * 200.0     # MHz * 2pi  (V >> Omega: blockade regime)

t_pi = np.pi / Omega
t_2pi = 2 * np.pi / Omega

# Input state |11> = |gg>
psi0 = qt.tensor(g, g)

# Three pulses: (drive Hamiltonian, duration)
pulses = [
    (0.5 * Omega * H1 + V * H_int, t_pi),    # pi on control
    (0.5 * Omega * H2 + V * H_int, t_2pi),   # 2pi on target (blocked)
    (0.5 * Omega * H1 + V * H_int, t_pi),    # pi on control
]

# Computational basis projectors
P_gg = qt.tensor(g * g.dag(), g * g.dag())
P_gr = qt.tensor(g * g.dag(), r * r.dag())
P_rg = qt.tensor(r * r.dag(), g * g.dag())
P_rr = rr * rr.dag()

times = []
states = []
t0 = 0.0
for H, dur in pulses:
    ts = np.linspace(0, dur, 200)
    res = qt.sesolve(H, psi0 if t0 == 0 else states[-1], ts)
    states.extend(res.states[1:] if t0 > 0 else res.states)
    times.extend((ts[1:] + t0) if t0 > 0 else ts)
    t0 += dur

pop_gg = [qt.expect(P_gg, s) for s in states]
pop_gr = [qt.expect(P_gr, s) for s in states]
pop_rg = [qt.expect(P_rg, s) for s in states]
pop_rr = [qt.expect(P_rr, s) for s in states]

plt.figure(figsize=(8, 4.5))
plt.plot(times, pop_gg, lw=2, label=r"$|11\rangle = |gg\rangle$")
plt.plot(times, pop_gr, lw=1.5, label=r"$|g r\rangle$")
plt.plot(times, pop_rg, lw=1.5, ls="--", label=r"$|r g\rangle$")
plt.plot(times, pop_rr, lw=1.5, ls=":", label=r"$|rr\rangle$")

for boundary in [t_pi, t_pi + t_2pi]:
    plt.axvline(boundary, color="gray", ls=":", lw=1)

plt.xlabel(r"Time ($\mu$s)")
plt.ylabel("Population")
plt.title(r"Rydberg-blockade CZ: input $|11\rangle$ ($\pi$-$2\pi$-$\pi$ sequence)")
plt.grid(alpha=0.3, ls=":")
plt.legend(frameon=False)
plt.tight_layout()
plt.show()

print(f"Final |11> population: {pop_gg[-1]:.4f}")
print(f"Blockade leakage to |rr>: max = {max(pop_rr):.2e}")
