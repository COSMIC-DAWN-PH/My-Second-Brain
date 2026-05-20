import os
import numpy as np
import matplotlib.pyplot as plt

# Set plotting style using standard fonts to avoid CJK glyph warnings
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 11

# Ensure directory exists
output_dir = r"C:\Personal Profile\Profile\ScienceResearch\Quantum Computing\Handout by AI"
os.makedirs(output_dir, exist_ok=True)

# ==========================================
# 1. Plot Rabi Oscillations
# ==========================================
def plot_rabi_oscillations():
    t = np.linspace(0, 3.0, 300)  # Time in units of pi/Omega
    
    # Resonance (Delta = 0)
    P_res = np.sin(np.pi * t / 2) ** 2
    
    # Detuned (Delta = 1.5 * Omega)
    tilde_omega = np.sqrt(1.0 + 1.5**2)
    P_detuned = (1.0 / tilde_omega**2) * np.sin(tilde_omega * np.pi * t / 2) ** 2
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(t, P_res, '-', color='#1f77b4', lw=2.5, label=r'Resonant ($\Delta = 0$)')
    plt.plot(t, P_detuned, '--', color='#ff7f0e', lw=2.5, label=r'Detuned ($\Delta = 1.5\,\Omega$)')
    
    plt.xlabel(r'Time $t$ ($\pi/\Omega$)')
    plt.ylabel(r'Transition Probability $P_{|1\rangle}(t)$')
    plt.title('Rabi Oscillations Coherent Dynamics')
    plt.ylim(-0.05, 1.05)
    plt.grid(True, alpha=0.3, ls=':')
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()
    
    path = os.path.join(output_dir, "rabi_oscillations.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# 2. Plot Rydberg Blockade and Blockade Radius
# ==========================================
def plot_rydberg_blockade():
    r = np.linspace(1.5, 6.0, 500)  # Distance in um
    C6 = 28800.0  # MHz * um^6
    V = C6 / (r ** 6)
    
    Omega = 4.6  # MHz (Rabi frequency)
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(r, V, '-', color='#d62728', lw=2.5, label=r'Van der Waals $V(r) = C_6/r^6$')
    plt.axhline(y=Omega, color='#2ca02c', ls='-.', lw=2, label=r'Laser Coupling $\Omega = 2\pi \times 4.6\,\mathrm{MHz}$')
    
    # Blockade radius Rb
    Rb = (C6 / Omega) ** (1/6)
    plt.axvline(x=Rb, color='#9467bd', ls=':', lw=2, label=f'Blockade Radius $R_b \\approx {Rb:.2f}\\,\\mu\\mathrm{{m}}$')
    
    # Fill blockade regime
    plt.fill_between(r[r <= Rb], 0, V[r <= Rb], color='#d62728', alpha=0.1, label='Blockade Regime')
    
    # Annotate work point (2.0 um, V = 450 MHz)
    plt.scatter([2.0], [450.0], color='black', s=80, zorder=5)
    plt.annotate(r'Work distance $d = 2.0\,\mu\mathrm{m}$' '\n' r'$V(d)/2\pi \approx 450\,\mathrm{MHz} \gg \Omega$',
                 xy=(2.0, 450.0), xytext=(2.8, 400.0),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6))
    
    plt.yscale('log')
    plt.ylim(1e-1, 2e4)
    plt.xlim(1.5, 6.0)
    plt.xlabel(r'Atom Distance $r$ ($\mu\mathrm{m}$)')
    plt.ylabel(r'Interaction Energy $V(r)/2\pi$ ($\mathrm{MHz}$)')
    plt.title('Rydberg Van der Waals Potential & Blockade Effect')
    plt.grid(True, which="both", alpha=0.3, ls=':')
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()
    
    path = os.path.join(output_dir, "rydberg_blockade.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# 3. Plot Gate Waveform Profiles
# ==========================================
def plot_gate_waveforms():
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.5))
    
    # ------------------
    # Time-Optimal Gate
    # ------------------
    Omega = 2 * np.pi * 4.6  # rad/us => 4.6 MHz
    T_to = 1.215 * 1000 / 4.6  # ns
    t_to = np.linspace(0, T_to, 300)
    
    A = 2 * np.pi * 0.1122
    omega_to = 1.0431 * (Omega / 1000)  # rad/ns
    phi_0 = -0.7318
    phi_to = A * np.cos(omega_to * t_to - phi_0)
    
    omega_amp_to = np.ones_like(t_to) * 4.6
    for i in range(len(t_to)):
        if t_to[i] < 15:
            omega_amp_to[i] *= np.sin(np.pi * t_to[i] / 30)**2
        elif t_to[i] > T_to - 15:
            omega_amp_to[i] *= np.sin(np.pi * (T_to - t_to[i]) / 30)**2
            
    axes[0, 0].plot(t_to, omega_amp_to, color='#1f77b4', lw=2.5)
    axes[0, 0].set_ylabel(r'Rabi Frequency $\Omega(t)/2\pi$ (MHz)')
    axes[0, 0].set_title('Time-Optimal Gate - Amplitude')
    axes[0, 0].grid(True, alpha=0.3, ls=':')
    axes[0, 0].set_ylim(-0.5, 5.5)
    
    axes[1, 0].plot(t_to, phi_to / (2*np.pi), color='#ff7f0e', lw=2.5)
    axes[1, 0].set_xlabel('Time $t$ (ns)')
    axes[1, 0].set_ylabel(r'Laser Phase $\phi(t)/2\pi$')
    axes[1, 0].set_title('Time-Optimal Gate - Phase')
    axes[1, 0].grid(True, alpha=0.3, ls=':')
    axes[1, 0].set_ylim(-0.2, 0.2)
    
    # --------------------
    # Smooth-Amplitude Gate
    # --------------------
    T_sa = 1.207 * 1000 / 4.6  # ns
    t_sa = np.linspace(0, T_sa, 300)
    tau = t_sa - T_sa / 2  # ns
    
    Omega_0 = 32.7403
    Omega_1 = -31.1404
    omega_0 = 0.2668 * (Omega / 1000)  # rad/ns
    alpha = -0.1131
    delta_0 = -0.9491 * (Omega / 1000)  # rad/ns
    B = 2 * np.pi * 0.2503
    lambd = 0.9372 * (Omega / 1000)  # rad/ns
    
    amp_ratio = Omega_0 + Omega_1 * (1.0 / np.cosh(omega_0 * tau))**alpha
    amp_sa = amp_ratio * (4.6 / np.max(amp_ratio))
    phi_sa = delta_0 * tau + B * np.tanh(lambd * tau)
    
    axes[0, 1].plot(t_sa, amp_sa, color='#2ca02c', lw=2.5)
    axes[0, 1].set_title('Smooth-Amplitude Gate - Amplitude')
    axes[0, 1].grid(True, alpha=0.3, ls=':')
    axes[0, 1].set_ylim(-0.5, 5.5)
    
    axes[1, 1].plot(t_sa, phi_sa / (2*np.pi), color='#d62728', lw=2.5)
    axes[1, 1].set_xlabel('Time $t$ (ns)')
    axes[1, 1].set_title('Smooth-Amplitude Gate - Phase')
    axes[1, 1].grid(True, alpha=0.3, ls=':')
    axes[1, 1].set_ylim(-0.4, 0.4)
    
    plt.tight_layout()
    path = os.path.join(output_dir, "gate_waveforms.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# 4. Simulate Dark-State Physics & Population
# ==========================================
def simulate_dark_state_physics():
    Delta = 7.8 * 1000  # 7.8 GHz = 7800 MHz
    Om_r = 303.0        # 1013nm Rabi = 303 MHz
    Om_b = 237.0        # 420nm Rabi = 237 MHz
    
    T = 275.0
    dt = 0.1
    steps = int(T / dt)
    t = np.linspace(0, T, steps)
    
    A = 2 * np.pi * 0.1122
    omega = 1.0431 * (2 * np.pi * 4.6 / 1000)  # rad/ns
    phi_0 = -0.7318
    delta_profile = A * (omega * 1000 / (2*np.pi)) * np.sin(omega * t - phi_0)
    
    coeff = 2 * np.pi / 1000.0
    
    def solve_se(sign):
        psi = np.array([1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j])
        P_intermediate = []
        
        for idx in range(len(t)):
            curr_t = t[idx]
            curr_delta = sign * delta_profile[idx]
            
            scale = 1.0
            if curr_t < 15.0:
                scale = np.sin(np.pi * curr_t / 30.0)**2
            elif curr_t > T - 15.0:
                scale = np.sin(np.pi * (T - curr_t) / 30.0)**2
                
            H = np.zeros((3, 3), dtype=complex)
            H[0, 1] = (Om_b * scale) / 2.0
            H[1, 0] = (Om_b * scale) / 2.0
            H[1, 2] = Om_r / 2.0
            H[2, 1] = Om_r / 2.0
            H[1, 1] = -Delta
            H[2, 2] = -curr_delta
            
            H_ns = H * coeff
            
            k1 = -1j * np.dot(H_ns, psi)
            k2 = -1j * np.dot(H_ns, psi + k1 * dt / 2)
            k3 = -1j * np.dot(H_ns, psi + k2 * dt / 2)
            k4 = -1j * np.dot(H_ns, psi + k3 * dt)
            
            psi = psi + (k1 + 2*k2 + 2*k3 + k4) * dt / 6.0
            psi = psi / np.linalg.norm(psi)
            
            P_intermediate.append(np.abs(psi[1])**2)
            
        return P_intermediate

    P_bad = solve_se(1)   # delta * Delta > 0
    P_good = solve_se(-1)  # delta * Delta < 0
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(t, np.array(P_bad) * 1e4, '-', color='#d62728', lw=2, label=r'Bright State Branch ($\delta\Delta > 0$)')
    plt.plot(t, np.array(P_good) * 1e4, '-', color='#2ca02c', lw=2.5, label=r'Dark State Branch ($\delta\Delta < 0$, paper choice)')
    
    plt.xlabel('Time $t$ (ns)')
    plt.ylabel(r'Intermediate State Population $P_{|e\rangle}(t)$ ($\times 10^{-4}$)')
    plt.title(r'Dark/Bright Branch Suppression ($\Delta = 7.8\,\mathrm{GHz}$)')
    plt.ylim(-0.5, 6.5)
    plt.grid(True, alpha=0.3, ls=':')
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()
    
    path = os.path.join(output_dir, "dark_state_physics.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# Run all plotting functions
# ==========================================
if __name__ == "__main__":
    plot_rabi_oscillations()
    plot_rydberg_blockade()
    plot_gate_waveforms()
    simulate_dark_state_physics()
