import os
import numpy as np
import matplotlib.pyplot as plt

# 设置画图风格与中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 11

# 确保文件夹存在
output_dir = r"C:\Personal Profile\Profile\ScienceResearch\Quantum Computing\Handout by AI"
os.makedirs(output_dir, exist_ok=True)

# ==========================================
# 1. 绘制拉比振荡 (Rabi Oscillations)
# ==========================================
def plot_rabi_oscillations():
    t = np.linspace(0, 3.0, 300)  # 时间单位：pi/Omega
    
    # 共振 (Delta = 0)
    P_res = np.sin(np.pi * t / 2) ** 2
    
    # 非共振 (Delta = 1.5 * Omega)
    # P = (Omega/tilde_Omega)^2 * sin^2(tilde_Omega * t / 2)
    # Let Omega = 1, Delta = 1.5 => tilde_Omega = sqrt(1 + 2.25) = sqrt(3.25) approx 1.8027
    tilde_omega = np.sqrt(1.0 + 1.5**2)
    P_detuned = (1.0 / tilde_omega**2) * np.sin(tilde_omega * np.pi * t / 2) ** 2
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(t, P_res, '-', color='#1f77b4', lw=2.5, label=r'共振共轭阻尼 ($\Delta = 0$)')
    plt.plot(t, P_detuned, '--', color='#ff7f0e', lw=2.5, label=r'大失谐 ($\Delta = 1.5\,\Omega$)')
    
    plt.xlabel(r'时间 $t$ (以无量纲时间 $\pi/\Omega$ 为单位)')
    plt.ylabel(r'激发态概率 $P_{|1\rangle}(t)$')
    plt.title('二能级系统下的拉比振荡相干动力学')
    plt.ylim(-0.05, 1.05)
    plt.grid(True, alpha=0.3, ls=':')
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()
    
    path = os.path.join(output_dir, "rabi_oscillations.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# 2. 绘制里德伯相互作用与阻塞半径 (Rydberg Blockade)
# ==========================================
def plot_rydberg_blockade():
    r = np.linspace(1.5, 6.0, 500)  # 距离以 um 为单位
    # V(r) = C6 / r^6. 已知 C6 / 2pi = 28800 MHz * um^6
    C6 = 28800.0  # MHz * um^6
    V = C6 / (r ** 6)
    
    Omega = 4.6  # MHz (Rabi 频率)
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(r, V, '-', color='#d62728', lw=2.5, label=r'范德华相互作用势 $V(r) = C_6/r^6$')
    plt.axhline(y=Omega, color='#2ca02c', ls='-.', lw=2, label=r'激光耦合强度 $\Omega = 2\pi \times 4.6\,\mathrm{MHz}$')
    
    # 标出阻塞半径 Rb = (C6 / Omega)^(1/6)
    Rb = (C6 / Omega) ** (1/6)
    plt.axvline(x=Rb, color='#9467bd', ls=':', lw=2, label=f'里德伯阻塞半径 $R_b \\approx {Rb:.2f}\\,\\mu\\mathrm{{m}}$')
    
    # 填充强相互作用区间 (里德伯阻塞区)
    plt.fill_between(r[r <= Rb], 0, V[r <= Rb], color='#d62728', alpha=0.1, label='强相互作用阻滞区 (Blockade Regime)')
    
    # 标注典型工作点 (2.0 um, V = 450 MHz)
    plt.scatter([2.0], [450.0], color='black', s=80, zorder=5)
    plt.annotate(r'工作间距 $d = 2.0\,\mu\mathrm{m}$' '\n' r'$V(d)/2\pi \approx 450\,\mathrm{MHz} \gg \Omega$',
                 xy=(2.0, 450.0), xytext=(2.8, 400.0),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6))
    
    plt.yscale('log')
    plt.ylim(1e-1, 2e4)
    plt.xlim(1.5, 6.0)
    plt.xlabel(r'原子间距 $r$ ($\mu\mathrm{m}$)')
    plt.ylabel(r'相互作用势能 $V(r)/2\pi$ ($\mathrm{MHz}$)')
    plt.title('里德伯范德华力随距离演化与阻塞效应')
    plt.grid(True, which="both", alpha=0.3, ls=':')
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()
    
    path = os.path.join(output_dir, "rydberg_blockade.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# 3. 绘制门波形参数 (Gate Waveforms)
# ==========================================
def plot_gate_waveforms():
    # 时间最优门和平滑振幅门波形
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.5))
    
    # ------------------
    # Time-Optimal Gate
    # ------------------
    # Duration: Omega*T/2pi = 1.215 => T = 264 ns for Omega = 2pi * 4.6 MHz
    # Formula: phi(t) = A cos(omega * t - phi_0) + delta_0 * t
    Omega = 2 * np.pi * 4.6  # rad/us => 4.6 MHz
    T_to = 1.215 * 1000 / 4.6  # ns approx 264 ns
    t_to = np.linspace(0, T_to, 300)
    
    A = 2 * np.pi * 0.1122
    omega_to = 1.0431 * (Omega / 1000)  # rad/ns
    phi_0 = -0.7318
    phi_to = A * np.cos(omega_to * t_to - phi_0)
    
    # Rabi amplitude for Time-optimal is constant
    # (except for a small 10ns rise/fall time which we can draw dynamically)
    omega_amp_to = np.ones_like(t_to) * 4.6
    # Smooth edges representing AOM rise/fall
    for i in range(len(t_to)):
        if t_to[i] < 15:
            omega_amp_to[i] *= np.sin(np.pi * t_to[i] / 30)**2
        elif t_to[i] > T_to - 15:
            omega_amp_to[i] *= np.sin(np.pi * (T_to - t_to[i]) / 30)**2
            
    axes[0, 0].plot(t_to, omega_amp_to, color='#1f77b4', lw=2.5)
    axes[0, 0].set_ylabel(r'拉比频率 $\Omega(t)/2\pi$ (MHz)')
    axes[0, 0].set_title('时间最优门 (Time-Optimal) - 振幅')
    axes[0, 0].grid(True, alpha=0.3, ls=':')
    axes[0, 0].set_ylim(-0.5, 5.5)
    
    axes[1, 0].plot(t_to, phi_to / (2*np.pi), color='#ff7f0e', lw=2.5)
    axes[1, 0].set_xlabel('时间 $t$ (ns)')
    axes[1, 0].set_ylabel(r'激光相位 $\phi(t)/2\pi$')
    axes[1, 0].set_title('时间最优门 (Time-Optimal) - 相位')
    axes[1, 0].grid(True, alpha=0.3, ls=':')
    axes[1, 0].set_ylim(-0.2, 0.2)
    
    # --------------------
    # Smooth-Amplitude Gate
    # --------------------
    # Duration: Omega*T/2pi = 1.207 => T = 262 ns
    T_sa = 1.207 * 1000 / 4.6  # ns approx 262 ns
    t_sa = np.linspace(0, T_sa, 300)
    tau = t_sa - T_sa / 2  # ns
    
    # Formulas:
    # Omega_420(t)/Omega_1013 = Omega_0 + Omega_1 sech[omega_0 * tau]^alpha
    # phi(t) = delta_0 * tau + B * tanh(lambda * tau)
    # The parameters are given in units of Omega (here Omega/2pi = 4.6 MHz => Omega_rad = 2pi*4.6 rad/us)
    # To plot, we can normalize to have similar shape as Nature paper Fig. 1c
    Omega_0 = 32.7403
    Omega_1 = -31.1404
    omega_0 = 0.2668 * (Omega / 1000)  # rad/ns
    alpha = -0.1131
    delta_0 = -0.9491 * (Omega / 1000)  # rad/ns
    B = 2 * np.pi * 0.2503
    lambd = 0.9372 * (Omega / 1000)  # rad/ns
    
    # Amplitude: Omega_420 / Omega_1013
    amp_ratio = Omega_0 + Omega_1 * (1.0 / np.cosh(omega_0 * tau))**alpha
    # We scale it to match realistic Rabi frequency profile (peak around 4.6 MHz)
    amp_sa = amp_ratio * (4.6 / np.max(amp_ratio))
    
    # Phase
    phi_sa = delta_0 * tau + B * np.tanh(lambd * tau)
    
    axes[0, 1].plot(t_sa, amp_sa, color='#2ca02c', lw=2.5)
    axes[0, 1].set_title('平滑振幅门 (Smooth-Amplitude) - 振幅')
    axes[0, 1].grid(True, alpha=0.3, ls=':')
    axes[0, 1].set_ylim(-0.5, 5.5)
    
    axes[1, 1].plot(t_sa, phi_sa / (2*np.pi), color='#d62728', lw=2.5)
    axes[1, 1].set_xlabel('时间 $t$ (ns)')
    axes[1, 1].set_title('平滑振幅门 (Smooth-Amplitude) - 相位')
    axes[1, 1].grid(True, alpha=0.3, ls=':')
    axes[1, 1].set_ylim(-0.4, 0.4)
    
    plt.tight_layout()
    path = os.path.join(output_dir, "gate_waveforms.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# 4. 模拟暗态物理 (Dark-State Physics & Population)
# ==========================================
def simulate_dark_state_physics():
    # 模拟三能级系统受激光驱动
    # Hamilton:
    # H = [[0, Om_b/2, 0],
    #      [Om_b/2, -Delta, Om_r/2],
    #      [0, Om_r/2, -delta]]
    # 模拟参数:
    Delta = 7.8 * 1000  # 7.8 GHz = 7800 MHz
    Om_r = 303.0        # 1013nm Rabi = 303 MHz
    Om_b = 237.0        # 420nm Rabi = 237 MHz
    
    # 我们运行两个模拟，对应 delta*Delta > 0 和 delta*Delta < 0
    # 时间最优门，时间从 0 到 275 ns
    T = 275.0
    dt = 0.1
    steps = int(T / dt)
    t = np.linspace(0, T, steps)
    
    # 极小相位调制对应的二光子失谐
    A = 2 * np.pi * 0.1122
    omega = 1.0431 * (2 * np.pi * 4.6 / 1000)  # rad/ns
    phi_0 = -0.7318
    
    # phase phi(t) = A * cos(omega*t - phi_0)
    # detuning delta(t) = -dphi/dt = A * omega * sin(omega*t - phi_0) (in rad/ns) => convert to MHz
    # delta(t) / 2pi = A * (omega / 2pi) * sin(omega*t - phi_0)
    delta_profile = A * (omega * 1000 / (2*np.pi)) * np.sin(omega * t - phi_0)
    
    # 求解薛定谔方程 H |psi> = i d|psi>/dt (以 hbar = 1, 频率以 MHz, 时间以 ns, 则 1/ns = 10^9 rad/s = 2pi * 159 MHz)
    # 为了求解简便，我们将 H 转换为 rad/ns。
    # 频率在 MHz 时，转换为 rad/ns 的系数为 2pi / 1000
    coeff = 2 * np.pi / 1000.0
    
    def solve_se(sign):
        # sign = +1 对应 delta*Delta > 0, sign = -1 对应 delta*Delta < 0
        # 初始状态 |psi(0)> = |1> = [1, 0, 0]
        psi = np.array([1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j])
        P_intermediate = []
        
        for idx in range(len(t)):
            curr_t = t[idx]
            curr_delta = sign * delta_profile[idx]
            
            # 振幅平滑上升沿 (15ns) 与下降沿 (15ns)
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
            
            # 转为 rad/ns
            H_ns = H * coeff
            
            # RK4 单步演化
            k1 = -1j * np.dot(H_ns, psi)
            k2 = -1j * np.dot(H_ns, psi + k1 * dt / 2)
            k3 = -1j * np.dot(H_ns, psi + k2 * dt / 2)
            k4 = -1j * np.dot(H_ns, psi + k3 * dt)
            
            psi = psi + (k1 + 2*k2 + 2*k3 + k4) * dt / 6.0
            # 归一化
            psi = psi / np.linalg.norm(psi)
            
            # 记录中间态概率 |psi[1]|^2
            P_intermediate.append(np.abs(psi[1])**2)
            
        return P_intermediate

    P_bad = solve_se(1)   # delta * Delta > 0
    P_good = solve_se(-1)  # delta * Delta < 0 (暗态选择)
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(t, np.array(P_bad) * 1e4, '-', color='#d62728', lw=2, label=r'亮态分支 ($\delta\Delta > 0$)')
    plt.plot(t, np.array(P_good) * 1e4, '-', color='#2ca02c', lw=2.5, label=r'暗态分支 ($\delta\Delta < 0$, 论文所选)')
    
    plt.xlabel('时间 $t$ (ns)')
    plt.ylabel(r'中间态居量 $P_{|e\rangle}(t)$ ($\times 10^{-4}$)')
    plt.title(r'双光子门中的暗态/亮态抑制机制（$\Delta = 7.8\,\mathrm{GHz}$）')
    plt.ylim(-0.5, 6.5)
    plt.grid(True, alpha=0.3, ls=':')
    plt.legend(frameon=True, facecolor='white', edgecolor='none')
    plt.tight_layout()
    
    path = os.path.join(output_dir, "dark_state_physics.png")
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

# ==========================================
# 执行所有生成函数
# ==========================================
if __name__ == "__main__":
    plot_rabi_oscillations()
    plot_rydberg_blockade()
    plot_gate_waveforms()
    simulate_dark_state_physics()
