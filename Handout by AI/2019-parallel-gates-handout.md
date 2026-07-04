---
aliases:
  - Levine 2019 Parallel Gates Handout
  - 2019 并行门讲义
  - 2019-Gates-PRL-Handout
tags:
  - Physics
  - Quantum
  - Handout
  - NeutralAtom
  - Rydberg
  - Gates
date: 2026-07-04
status: WIP
source: "[[2019-Gates PRL]]"
---

# 🚀 极速起步：中性原子高保真并行纠缠门（2019 PRL）

> **导言**
> 本讲义带你精读 Lukin 组 2019 年发表在 *Physical Review Letters* 上的里程碑论文：*"Parallel Implementation of High-Fidelity Multiqubit Gates with Neutral Atoms"*。这是中性原子量子计算领域最早实现**并行高保真两比特门**的实验工作之一，为后续 2023 年 Nature 论文的 99.5% 保真度奠定了关键基础。
>
> 阅读本讲义前，建议你已掌握以下前置知识（均可在你的知识库中找到）：
> - [[Hyperfine-Structure|超精细结构]] 与钟跃迁（Clock Transition）
> - [[Rabi-Flopping|拉比振荡]] 的共振与非共振动力学
> - [[Rydberg-Blockade|里德堡阻塞]] 的物理机制与 $\sqrt{2}\,\Omega$ 集体增强
> - [[CZ-Gate|CZ 门]] 的矩阵定义与逻辑作用
>
> 本讲义将聚焦于这篇论文的**核心创新**——一种仅用**两束全局激光脉冲**即可实现 CZ 门的全新协议，并解释其背后的几何相位物理图像。

---

## 🔬 第一部分：物理载体——光镊阵列中的铷-87 量子比特

### 1.1 实验平台概览

与你在 [[start_up]] 中读到的 2023 年论文类似，本实验同样使用 **$^{87}\mathrm{Rb}$（铷-87）原子**，囚禁在 **[[Optical-Tweezer-Arrays|光镊阵列]]** 中。但 2019 年的这项工作处于平台发展的更早阶段，许多技术细节相对简洁，却同样精巧。

**原子排列**：一维光镊阵列中的原子通过实时反馈排序，被组织成**成对（pairs）或成三（triplets）**的簇（cluster）。论文展示了在**五对原子上并行**执行 CZ 门，以及在**四个三原子上并行**执行 Toffoli 门。

**量子比特编码**：与后续工作完全一致——使用超精细基态的钟跃迁（Clock Transition）：
- $|0\rangle \equiv |5S_{1/2}, F=1, m_F=0\rangle$
- $|1\rangle \equiv |5S_{1/2}, F=2, m_F=0\rangle$

这两个态的能量差为 $6.8347\,\mathrm{GHz}$，属于微波波段。选择 $m_F=0$ 的原因你已熟悉：一阶 Zeeman 位移为零，对磁场涨落免疫。

### 1.2 单比特操控：全局 Raman 激光 + 局域寻址

实验中通过**两种激光**的组合实现单比特门：

| 激光类型 | 波长 | 作用 |
|---------|------|------|
| **全局 Raman 激光** | $795\,\mathrm{nm}$ | 均匀驱动所有原子，实现全局 $X(\theta)$ 旋转 |
| **局域寻址激光** | $420\,\mathrm{nm}$ | 通过声光偏转器（AOD）分束，聚焦到单个原子，产生光移（light shift）实现 $Z(\theta)$ 旋转 |

> [!info] 全局 vs 局域
> 全局激光像"广播"——同时对所有原子说话；局域激光像"耳语"——只对特定原子产生影响。论文中的 CZ 门协议最惊人的一点在于：**它只需要全局激光，不需要局域操控两比特中的任何一个**！

### 1.3 里德堡激发：双光子过程

要将原子从 $|1\rangle$ 激发到里德堡态 $|r\rangle \equiv |70S_{1/2}, m_J=-1/2\rangle$，实验使用**双光子跃迁**：
- $420\,\mathrm{nm}$ 激光：驱动 $|1\rangle \to |6P_{3/2}\rangle$
- $1013\,\mathrm{nm}$ 激光：驱动 $|6P_{3/2}\rangle \to |r\rangle$

两束激光共同作用，产生**有效拉比频率** $\Omega \approx 2\pi \times 3.5\,\mathrm{MHz}$。由于单光子大失谐，中间态 $|6P_{3/2}\rangle$ 被绝热消去，系统等效为 $|1\rangle \leftrightarrow |r\rangle$ 的二能级系统（详见 [[start_up#2. 双光子跃迁与中间态消去]] 的推导）。

**阻塞条件**：最近邻原子间的里德堡相互作用强度为 $V/2\pi = 24\,\mathrm{MHz}$，远大于 $\Omega/2\pi = 3.5\,\mathrm{MHz}$，因此系统处于**强阻塞区间**：
$$
V \gg \Omega \quad \Rightarrow \quad |rr\rangle \text{ 被完全阻塞}
$$

### 1.4 实验标定：Fig. 1 的物理信息

在正式执行门操作之前，实验团队必须完成一系列**系统标定（system calibration）**，确保每个硬件模块都按预期工作。论文 Fig. 1 用四个子图展示了这些关键标定：

**Fig. 1(c) — Rydberg Rabi 振荡**：
将单个原子制备在 $|1\rangle$，施加 Rydberg 激光，测量里德堡态布居随时间的振荡。实验数据展示了清晰的拉比振荡，拟合得到有效拉比频率 $\Omega \approx 2\pi \times 3.5\,\mathrm{MHz}$。**注意**：为了避免两个原子之间的相互作用，实验中每对原子只有一个被制备在 $|1\rangle$。

**Fig. 1(d) — 局域寻址 Ramsey 序列**：
通过 Ramsey 干涉测量局域 $420\,\mathrm{nm}$ 寻址激光对单个原子的光移效果。结果显示：
- 被寻址的原子（紫色曲线）：高对比度振荡，光移 $\delta$ 可被精确调控
- 未被寻址的邻近原子（灰色曲线）：串扰（crosstalk）**小于 2%**

> [!tip] 为什么串扰必须很低？
> 串扰意味着当你想操控原子 A 时，旁边的原子 B 也受到了影响。如果串扰太高，局域 $Z$ 旋转就会"波及"相邻 qubit，破坏量子信息的独立性。$\lt 2\%$ 的串扰在后续需要局域寻址的协议中（如 CNOT 转换、Toffoli 门）至关重要。

**Fig. 1(e) — 单比特 Rabi 振荡**：
用 $795\,\mathrm{nm}$ Raman 激光驱动 $|0\rangle \leftrightarrow |1\rangle$ 跃迁，测量到有效拉比频率 $\Omega_{01} \approx 2\pi \times 250\,\mathrm{kHz}$。这是全局单比特门的速度基准。

---

## ⚡ 第二部分：核心创新——双脉冲全局 CZ 门

这是整篇论文最精彩的部分。传统上，里德堡阻塞实现 CZ 门需要**多个脉冲**和**局域寻址**（例如先操控控制比特、再操控目标比特）。而本论文提出了一种**仅用两束全局脉冲**的新协议，不仅更快，而且完全不需要局域寻址来构建门本身。

### 2.1 CZ 门的目标

在计算基 $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$ 下，CZ 门的作用是：
$$
\text{CZ} = 2|00\rangle\langle 00| - I = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}
$$

论文中实现的映射等价于上述标准 CZ 门，只差一个**单比特相位** $\phi$（可通过后续的单比特旋转补偿）。论文给出的具体映射为：
$$
|00\rangle \to |00\rangle, \quad |01\rangle \to e^{i\phi_{01}}|01\rangle, \quad |10\rangle \to e^{i\phi_{01}}|10\rangle, \quad |11\rangle \to e^{i\phi_{11}}|11\rangle
$$

> [!info] 为什么允许单比特相位？
> 在量子线路编译中，单比特相位 $e^{i\phi_{01}}$ 可以通过**虚拟 Z 门（virtual Z gate）**零成本地补偿——只需调整后续激光脉冲的相位参考，不需要执行任何物理操作。因此，只要满足 **$\phi_{11} - 2\phi_{01} = \pi$**，就等价于实现了标准 CZ 门。

### 2.2 四个基态的不同命运

两束全局脉冲对四个计算基态的作用截然不同，这正是门设计的物理基础：

**① $|00\rangle$：完全不参与**
两个原子都在 $|0\rangle$，而激光只耦合 $|1\rangle \leftrightarrow |r\rangle$。因此 $|00\rangle$ 在整个过程中**完全不受影响**，也不积累任何相位。

**② $|01\rangle$ 和 $|10\rangle$：单原子失谐拉比振荡**
只有一个原子在 $|1\rangle$，它感受到的驱动就是一个标准的**失谐二能级系统**：拉比频率 $\Omega$，失谐 $\Delta$。在旋转框架下，Hamiltonian 为：
$$
H_{01} = \frac{\hbar}{2}\begin{pmatrix} 0 & \Omega \\ \Omega & -2\Delta \end{pmatrix}
$$

这里我们使用**标准原子物理约定**：对角项表示能级在旋转框架中的位置，$|1\rangle$ 的能量为 $0$，$|r\rangle$ 的能量为 $-2\Delta$（相对于激光频率偏移了 $2\Delta$）。非对角耦合为 $\Omega/2$。

> [!warning] 符号约定说明
> 论文原文将 Hamiltonian 写为 $H = \frac{\hbar\Omega}{2}\sigma_x - \hbar\Delta |r\rangle\langle r|$，即 $|r\rangle$ 的能量为 $-\Delta$。本文讲义为了与标准二能级拉比振荡的推导保持一致（见 [[Rabi-Flopping]]），采用 $-2\Delta$ 的约定——两者本质相同，只是将 detuning 定义在 $|r\rangle$ 能级上。最终物理结果（相位、脉冲时间）不受影响。

**③ $|11\rangle$：集体 $\sqrt{2}\,\Omega$ 增强的失谐振荡**
这是里德堡阻塞的魔力所在。由于 $|rr\rangle$ 被能量排斥，两个原子只能以对称方式被激发到 $|1r\rangle$ 和 $|r1\rangle$ 的叠加态——即 **W 态**：
$$
|W\rangle = \frac{|1r\rangle + |r1\rangle}{\sqrt{2}}
$$

在 $\{|11\rangle, |W\rangle\}$ 子空间中，有效 Hamiltonian 为：
$$
H_{11} = \frac{\hbar}{2}\begin{pmatrix} 0 & \sqrt{2}\,\Omega \\ \sqrt{2}\,\Omega & -2\Delta \end{pmatrix}
$$

关键发现：**$|11\rangle$ 系统的有效拉比频率是 $\sqrt{2}\,\Omega$，而 $|01\rangle$ 系统只有 $\Omega$。** 同样的失谐 $\Delta$ 下，两个系统以不同速度在布洛赫球上"奔跑"。

### 2.3 双脉冲协议的几何图像

论文的核心设计精妙绝伦：

**第一束脉冲**（长度 $\tau$，失谐 $\Delta$）：
- $|11\rangle$ 系统：由于拉比频率更大（$\sqrt{2}\,\Omega$），它被设计成**刚好完成一个完整的失谐拉比周期**，回到 $|11\rangle$。
- $|01\rangle$ 系统：拉比频率较小（$\Omega$），它**只完成一个不完整的振荡**，停在布洛赫球上的某处。

**相位跳变**（Phase jump $\xi$）：
在两束脉冲之间，激光相位突然改变 $\xi$。这在物理上相当于将驱动场的方向绕 Z 轴旋转了 $\xi$ 角。

**第二束脉冲**（同样长度 $\tau$，失谐 $\Delta$，但相位偏移 $\xi$）：
- $|01\rangle$ 系统：相位跳变后的驱动方向恰好将之前"未完成"的轨迹**闭合**，使原子回到 $|01\rangle$。
- $|11\rangle$ 系统：再次完成一个完整的失谐周期，回到 $|11\rangle$。

> [!tip] 布洛赫球上的"绕不同轴转圈"
> 想象两个陀螺以不同速度转圈。第一束脉冲让它们各自转了一段时间。然后你突然把"重力方向"偏转了一个角度（相位跳变 $\xi$）。第二束脉冲再让它们继续转。关键是：你要选择偏转角度 $\xi$ 和转圈时间 $\tau$，使得慢陀螺刚好回到起点，而快陀螺也回到起点——但两者在球面上"扫过的面积"不同，积累的**动力学相位**不同！

### 2.4 动力学相位与 CZ 条件的推导

在失谐二能级系统中，一个完整的演化（从 $|1\rangle$ 出发，绕一圈回到 $|1\rangle$）会积累一个**动力学相位（dynamical phase）**，其大小等于布洛赫球轨迹所包围的**立体角的一半**。

我们统一采用与论文一致的约定：Hamiltonian 为 $H = \frac{\hbar}{2}(\Omega \sigma_x - 2\Delta \sigma_z)$，其中 $\Delta$ 是**半失谐**（即激光频率与原子跃迁频率之差的一半）。在此约定下：

- $|01\rangle$ 系统：有效 Rabi 频率 $\Omega_{\text{eff}}^{(01)} = \sqrt{\Omega^2 + (2\Delta)^2} = \sqrt{\Omega^2 + 4\Delta^2}$
- $|11\rangle$ 系统：有效 Rabi 频率 $\Omega_{\text{eff}}^{(11)} = \sqrt{(\sqrt{2}\Omega)^2 + (2\Delta)^2} = \sqrt{2\Omega^2 + 4\Delta^2}$

不过，为了与论文图 2d 的横轴标注（$\Delta/\Omega$）直接对应，后文的数值计算中将采用简化的无量纲约定 $H \propto \Omega \sigma_x + \Delta \sigma_z$，此时有效频率直接写为 $\sqrt{\Omega^2 + \Delta^2}$。这只是一个标度选择，不影响物理结论。

**脉冲时间 $\tau$ 的选择**：
令第一束脉冲使 $|11\rangle$ 系统完成一个完整的失谐周期：
$$
\tau = \frac{2\pi}{\Omega_{\text{eff}}^{(11)}} = \frac{2\pi}{\sqrt{2\Omega^2 + \Delta^2}}
$$

这意味着在 $\tau$ 时间内，$|11\rangle$ 系统刚好转了一圈回到起点。

**动力学相位的计算**：
失谐二能级系统在旋转框架下，一个从 $|1\rangle$ 出发、经过完整周期后回到 $|1\rangle$ 的闭合轨迹，会积累一个**动力学相位（dynamical phase）** $\phi$。这个相位在物理上等于布洛赫球轨迹所包围的**立体角的一半**。它随失谐 $\Delta$ 从 $2\pi$ 连续变化到 $0$（如图 2d 所示）：
- 大失谐时：轨迹靠近赤道，包围面积小，$\phi \to 0$
- 小失谐时：轨迹深入两极，包围面积大，$\phi \to 2\pi$

定量上，$\phi$ 满足：
$$
\phi = \pi\left(1 - \frac{\Delta}{\Omega_{\text{eff}}}\right)
$$

这正是后文 Python 代码中使用的公式。

**CZ 条件**：
门操作完成后，需要满足：
$$
\phi_{11} = 2\phi_{01} - \pi
$$

这个条件的物理含义是：$|11\rangle$ 积累的总相位与两个单激发态积累相位之和相差 $\pi$，这正是 CZ 门引入的**条件相位**。

论文通过数值求解发现，当选择：
$$
\Delta \approx 0.377\,\Omega
$$
时，上述条件精确满足！

> [!tip] 为什么这个协议更快？
> 传统协议（Jaksch et al. 2000）需要四个 $\pi$ 脉冲，总时间为 $4\pi/\Omega$。而这个双脉冲协议的总时间为：
> $$
> T_{\text{gate}} = 2\tau = \frac{4\pi}{\sqrt{2\Omega^2 + \Delta^2}} \approx \frac{2.732\pi}{\Omega}
> $$
> 比传统协议快了约 **32%**！此外，传统协议通常需要对单个原子进行局域寻址，而这个协议**只需要全局耦合**——这是可扩展性的巨大优势。

### 2.5 Python 可视化：布洛赫球轨迹与相位曲线

下面的 Python 代码绘制了 $|01\rangle$ 和 $|11\rangle$ 系统在双脉冲协议中的布洛赫球轨迹，以及动力学相位随失谐的变化曲线（复现论文 Fig. 2d 的核心结果）：

```python
import matplotlib.pyplot as plt
import numpy as np

# --- Helper: exact 2x2 unitary propagator ---
def unitary2(Omega, Delta, dt, xi=0.0):
    """U = exp(-1j * H * dt) for H = [[Delta, Omega/2 * e^{i*xi}], [Omega/2 * e^{-i*xi}, -Delta]]"""
    H = np.array([[Delta, 0.5*Omega*np.exp(1j*xi)], [0.5*Omega*np.exp(-1j*xi), -Delta]], dtype=complex)
    evals, evecs = np.linalg.eigh(H)
    return evecs @ np.diag(np.exp(-1j*evals*dt)) @ evecs.conj().T

# Parameters (in units where Omega = 1)
Omega = 1.0
Delta_vals = np.linspace(0.01, 2.0, 200)

# Effective Rabi frequencies (paper convention)
Omega_eff_01 = np.sqrt(Omega**2 + Delta_vals**2)
Omega_eff_11 = np.sqrt(2*Omega**2 + Delta_vals**2)

# Pulse time: chosen so |11> completes one full cycle
tau = 2 * np.pi / Omega_eff_11

# Dynamical phases for one complete cycle
phi_01 = np.pi * (1 - Delta_vals / Omega_eff_01)
phi_11 = np.pi * (1 - Delta_vals / Omega_eff_11)

# Total phase after two pulses
phi_01_total = 2 * phi_01
phi_11_total = 2 * phi_11

# CZ condition: phi_11 = 2*phi_01 - pi
diff = phi_11_total - phi_01_total
idx = np.argmin(np.abs(diff + np.pi))
Delta_opt = Delta_vals[idx]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Left: Bloch sphere trajectories for optimal Delta ---
ax = axes[0]
ax.set_aspect('equal')
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3, label='Equator')

Delta_opt = 0.377 * Omega
t_total = 2 * tau[idx]
t = np.linspace(0, t_total, 600)
dt = t[1] - t[0]

# |01> trajectory: single atom, detuned Rabi evolution with phase jump
psi = np.array([0.0, 1.0], dtype=complex)  # start in |1>
x01, z01 = [], []
for ti in t:
    xi = 0.0 if ti <= tau[idx] else np.pi  # phase jump between pulses
    psi = unitary2(Omega, Delta_opt, dt, xi) @ psi
    c0, c1 = psi[0], psi[1]
    x01.append(2 * np.real(np.conj(c0) * c1))
    z01.append(np.abs(c0)**2 - np.abs(c1)**2)

# |11> trajectory: collective sqrt(2)*Omega, detuned Rabi evolution
psi2 = np.array([0.0, 1.0], dtype=complex)
x11, z11 = [], []
for ti in t:
    psi2 = unitary2(np.sqrt(2)*Omega, Delta_opt, dt, 0.0) @ psi2
    c0, c1 = psi2[0], psi2[1]
    x11.append(2 * np.real(np.conj(c0) * c1))
    z11.append(np.abs(c0)**2 - np.abs(c1)**2)

ax.plot(x01, z01, color='#1f77b4', lw=2, label=r'$|01\rangle$ trajectory')
ax.plot(x11, z11, color='#ff7f0e', lw=2, label=r'$|11\rangle$ trajectory')
ax.scatter([x01[0]], [z01[0]], color='#1f77b4', s=50, zorder=5)
ax.scatter([x11[0]], [z11[0]], color='#ff7f0e', s=50, zorder=5)
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_title(rf'Bloch Sphere Trajectories ($\Delta = {Delta_opt:.3f}\Omega$)')
ax.legend(frameon=False)
ax.grid(alpha=0.3, ls=':')

# --- Right: Phase vs detuning (reproducing Fig 2d) ---
ax2 = axes[1]
ax2.plot(Delta_vals/Omega, phi_01_total/np.pi, '-', color='#1f77b4', lw=2, label=r'$2\phi_{01}$')
ax2.plot(Delta_vals/Omega, phi_11_total/np.pi, '-', color='#ff7f0e', lw=2, label=r'$\phi_{11}$')
ax2.axhline(y=-1, color='gray', ls='--', alpha=0.5)
ax2.axvline(x=Delta_opt/Omega, color='#d62728', ls=':', label=r'$\Delta \approx 0.377\Omega$')
ax2.set_xlabel(r'Detuning $\Delta / \Omega$')
ax2.set_ylabel(r'Phase ($\pi$)')
ax2.set_title('Dynamical Phases vs Detuning')
ax2.legend(frameon=False)
ax2.grid(alpha=0.3, ls=':')
ax2.set_xlim(0, 2)

plt.tight_layout()
plt.show()
```

> [!warning] 代码说明
> 左图展示了 $|01\rangle$（蓝色）和 $|11\rangle$（橙色）在布洛赫球上的近似轨迹。右图复现了论文 Fig. 2d 的核心结果：两条相位曲线的交点（满足 $2\phi_{01} - \pi = \phi_{11}$）出现在 $\Delta \approx 0.377\,\Omega$ 处，这正是 CZ 门的工作点。

### 2.6 并行门操作的物理机制

论文标题中的关键词 **"Parallel"** 并非噱头，而是这个协议最突出的可扩展性优势之一。让我们深入理解为什么这个双脉冲协议天然适合**并行执行**。

**为什么可以并行？**

在五对原子上同时执行 CZ 门的关键在于：**全局激光对所有原子一视同仁，而不同原子对之间的空间距离足够大**。

- 同一对内的两个原子间距：$d \approx 2.0\,\mu\mathrm{m}$（在阻塞半径 $R_b$ 内）
- 不同对之间的间距：远大于 $R_b$（原子对被光镊排序为分离的簇）

这意味着：
1. **全局 Rydberg 激光同时照射所有原子**——每对原子都感受到相同的拉比频率 $\Omega$ 和失谐 $\Delta$
2. **对间相互作用可忽略**——不同对的原子相距甚远，$V(r) \propto r^{-6}$ 使相互作用衰减到几乎为零
3. **每对内部独立演化**——五对原子各自经历完全相同的 CZ 门动力学，互不影响

> [!tip] 物理图像
> 想象五张乒乓球桌排成一排，每张桌上有一对球（原子）。一阵均匀的风（全局激光）同时吹过所有桌子，每张桌上的两个球以完全相同的方式运动——因为各桌之间距离够远，风的影响不会跨桌传递。这就是并行的本质：
> - **全局均匀驱动** + **局域强相互作用** = 天然并行性

**并行 vs 串行的根本性区别**

| 特性 | 串行门操作 | 并行门操作（本论文） |
|------|----------|-------------------|
| 执行时间 | $N$ 对需要 $N \times t_{\text{gate}}$ | $N$ 对只需 $1 \times t_{\text{gate}}$ |
| 激光需求 | 需要局域寻址逐个激活 | 全局激光一次覆盖全部 |
| 可扩展性 | 随 qubit 数线性变慢 | 门时间与 qubit 数**无关** |
| 误差累积 | 多次操作累积更多误差 | 单次操作，误差更小 |

这种**门时间与体系大小无关**的特性，是中性原子平台相对于某些其他平台的核心优势之一。论文明确提到，同样的方法可以扩展到 **2D 和 3D 原子阵列**中的非局域耦合。

---

## 📊 第三部分：实验验证与基准测试

### 3.1 Bell 态制备与保真度测量

为了表征 CZ 门的性能，论文使用它制备了 **Bell 态** $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$，具体线路为：
1. 初始化所有原子到 $|0\rangle$
2. 全局 $X(\pi/2)$ 脉冲：将每个原子制备到 $|-i\rangle = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$
3. 执行 CZ 门（两束 Rydberg 脉冲，总时间 $0.4\,\mu\mathrm{s}$）
4. 全局 $X(\pi/4)$ 脉冲

> [!info] 为什么需要 echo 序列？
> Rydberg 激光会对超精细基态产生光移（light shift），这会在 CZ 门之外额外叠加不想要的单比特相位。论文将 CZ 门嵌入一个 **echo 序列** 中，通过在对称位置加入全局 $X(\pi)$ 脉冲来抵消光移的影响。此外还加入了一个短光移脉冲来消除单粒子相位 $\phi$。

**Bell 态保真度的测量**：
Bell 态保真度 $F = \langle\Phi^+|\rho|\Phi^+\rangle$ 由两项组成：
1. **布居数（Populations）**：测量 $|00\rangle$ 和 $|11\rangle$ 的出现概率 [Fig. 3(b)]
2. **相干项（Coherence）**：通过 parity 振荡测量 $|00\rangle$ 和 $|11\rangle$ 之间的相位相干性 [Fig. 3(c)]

**原始测量结果**：$F \geq 95.0(2)\%$

**泄漏修正**：论文发现有一小部分原子在操作后仍然留在里德堡态 $|r\rangle$ 或丢失。这些属于**量子比特子空间外的泄漏（leakage）**，会导致布居数被高估。通过单独测量泄漏贡献并从原始数据中扣除，得到更保守的下界 $F \geq 95.0(2)\%$。

### 3.2 SPAM 修正与门本征保真度

$95\%$ 的 Bell 态保真度包含了**态制备与测量误差（SPAM error）**。论文测得每个原子的 SPAM 误差约为 $1.2(1)\%$。为了提取**纯粹的门操作保真度**，需要将 SPAM 误差扣除：
$$
F^{[c]} \geq 97.4(3)\%
$$

这是 2019 年中性原子平台两比特门的最高水平之一，与当时超导、离子阱等领先平台相当。

> [!info] 什么是 SPAM 误差？
> **SPAM** = **S**tate **P**reparation **a**nd **M**easurement。
> - **态制备误差**：光泵浦不完美，原子未完全初始化到 $|0\rangle$（约 $0.5\%$ 残余在 $|1\rangle$）
> - **测量误差**：荧光成像时，$|1\rangle$ 原子未被完全吹走，或 $|0\rangle$ 原子被误判为丢失
> 这些误差是实验系统固有的，与门操作本身无关。如果不修正，会低估门的真实性能。

### 3.3 CNOT 门的真值表验证

为了进一步验证原生 CZ 门，论文将其转换为 **CNOT 门**（通过在目标比特两侧加 $H$ 门，详见 [[CZ-Gate#4. CZ 门与 CNOT 门的关系]]），并测量了 CNOT 的**真值表（truth table）**：

对四个计算基态分别施加 CNOT，测量输出：
- 原始测量保真度：$F_{\text{CNOT}} \geq 94.1(2)\%$
- SPAM 修正后：$F^{[c]}_{\text{CNOT}} \geq 96.5(3)\%$

真值表验证是门操作最直接、最无歧义的表征方法之一。

### 3.4 Fig. 3 详细解读与主要误差来源

论文 Fig. 3 系统展示了 Bell 态制备和 CNOT 验证的完整实验结果。让我们逐面板拆解：

**Fig. 3(a) — Bell 态制备与探测线路**：
```
|0> --[X(pi/2)]--[CZ]--[X(pi)]--[Z(theta)]--[X(pi/2)]-- measure
|0> --[X(pi/2)]--[CZ]--[X(pi)]----------|------------ measure
```
注意中间的 $X(\pi)$ 是 echo 序列的一部分，用于抵消光移。最后的 $Z(\theta)$ 旋转用于扫描 parity 振荡的相位。

**Fig. 3(b) — Bell 态布居数测量**：
- 理想情况下，$|00\rangle$ 和 $|11\rangle$ 各占 $50\%$
- 原始测量（raw）显示 $97.6(2)\%$ 的布居在目标态中
- 扣除泄漏贡献（light shaded）后，布居保真度 $\geq 95.8(3)\%$

**Fig. 3(c) — Parity 振荡**：
Parity 振荡振幅直接反映了 $|00\rangle$ 和 $|11\rangle$ 之间的**量子相干**。测量到的振荡振幅为 $94.2(4)\%$。结合布居数结果，Bell 态保真度的下界为：
$$
F \geq \frac{P_{00} + P_{11}}{2} + \frac{C}{2} \geq 95.0(2)\%
$$
其中 $C$ 是 parity 振荡的相干振幅。

**Fig. 3(e)-(f) — CNOT 真值表**：
四个计算基态作为输入，CNOT 的理想输出为：
| 输入 | 理想输出 |
|------|---------|
| $\vert 00\rangle$ | $\vert 00\rangle$ |
| $\vert 01\rangle$ | $\vert 01\rangle$ |
| $\vert 10\rangle$ | $\vert 11\rangle$ |
| $\vert 11\rangle$ | $\vert 10\rangle$ |

实验测量的 truth table fidelity 为 $F^{[c]}_{\text{CNOT}} \geq 96.5(3)\%$。

**主要误差来源分析**：

论文指出，SPAM 修正后的剩余误差主要来自以下两个物理因素：

1. **有限原子温度（finite atomic temperature）**：
   原子在光镊中有一定的热运动（温度约几微开尔文），导致原子位置在门操作期间有轻微涨落。这会改变原子感受到的激光强度（拉比频率 $\Omega$ 对位置敏感），从而引入门误差。

2. **激光散射（laser scattering）**：
   在 Rydberg 激发期间，激光光子可能被原子散射。即使使用大失谐双光子跃迁来抑制中间态占据，仍有残余的散射概率。每次散射都会破坏量子相干性。

> [!info] 为什么温度效应特别棘手？
> 光镊中的原子虽然已被冷却，但通常未达到量子基态。热运动意味着：
> - 原子在光镊势阱中做简谐振荡，位置不确定度 $\Delta x \sim \sqrt{\hbar / (2m\omega)}$（即使是基态也有有限展宽）
> - 激光束是高斯型的，不同位置感受到的光强不同 $\Omega(r) \propto I(r)$
> - 原子运动越快，门操作期间"穿越"的光强变化越大，拉比频率越不稳定
> 
> 论文指出，这个问题可以通过 **sideband cooling（边带冷却）** 将原子冷却到量子基态来大幅改善——这正是后续 2023 年工作实现 99.5% 保真度的关键技术升级之一。

---

## 🎨 第四部分：三量子比特 Toffoli 门的原理性演示

### 4.1 从 CZ 到 CCZ

在展示了高质量的两比特门之后，论文进一步将控制扩展到**三量子比特**，实现了 **CCZ 门（controlled-controlled-Z）**——即只有当两个控制比特都在 $|1\rangle$ 时，才给目标比特引入 $\pi$ 相位。

在经典计算中，Toffoli 门（CCNOT）是**通用可逆计算**的基石；在量子计算中，CCZ / Toffoli 门对于**量子纠错**、**Grover 搜索**和**Shor 算法**都至关重要。

> [!info] Toffoli 门的线路分解
> 理论上，一个 Toffoli 门可以分解为 **5 个两比特门**（CNOT + 单比特门）。但论文没有走分解路线，而是**直接利用三体里德堡相互作用**实现 CCZ 门——这有潜力比分解方案更高效。

### 4.2 三原子阻塞构型

实验将三个原子排成一行，间距满足：
- 最近邻相互作用：$V_{\text{nn}}/2\pi = 24\,\mathrm{MHz} \gg \Omega$（强阻塞）
- 次近邻（两端原子）相互作用：$V_{\text{nnn}}/2\pi = 0.4\,\mathrm{MHz} \ll \Omega$（弱相互作用，可忽略）

这意味着**两端的控制原子同时阻塞中间的目标原子**。三原子动力学发生在五维子空间中，极为复杂，难以解析求解。

### 4.3 数值最优控制（RedCRAB）

由于三原子系统的解析脉冲设计极其困难，论文采用 **RedCRAB（remote dressed chopped random basis）最优控制算法**来 numerically 构造激光脉冲。该算法通过远程服务器优化激光的**振幅调制和频率调制**，目标是最小化实际演化与理想 CCZ 门之间的保真度差距。

### 4.4 Toffoli 门性能

将 CCZ 门与单比特 Hadamard 门组合（在目标原子上加 $H$），即可得到 Toffoli 门。实验结果：
- 八个计算基态的制备保真度：$95.3(3)\%$
- Toffoli 真值表保真度（原始）：$F_{\text{Toff}} \geq 83.7(3)\%$
- SPAM 修正后：$F^{[c]}_{\text{Toff}} \geq 87.0(4)\%$
- 受限层析（limited tomography）保真度：$F^{[c]}_{\text{LT}} \geq 86.2(6)\%$

> [!warning] 为什么 Toffoli 保真度明显低于 CZ？
> 三比特门保真度更低是预期的：
> 1. **动力学更复杂**：三原子系统的 Hilbert 空间更大，最优控制找到的完美脉冲更难
> 2. **误差累积**：三个原子各自的退相干、散射、温度效应叠加
> 3. **次近邻相互作用**：$0.4\,\mathrm{MHz}$ 虽然不是完全零，但会轻微扰乱动力学
> 4. **证明原理**：这只是一个 proof-of-principle 演示，脉冲优化还有很大提升空间

---

## 🌟 第五部分：结论与展望

### 5.1 论文的核心贡献总结

这篇 2019 年的 PRL 在中性原子量子计算的发展史上具有承前启后的意义。它的核心贡献可以概括为三点：

1. **全新双脉冲全局 CZ 门协议**：首次实现仅用两束全局激光脉冲即可构造高保真 CZ 门，无需局域寻址。门时间 $T_{\text{gate}} \approx 2.732\pi/\Omega$ 比传统协议快约 $32\%$。

2. **实验验证的并行可扩展性**：在五对原子上同时执行 CZ 门，证明了全局门协议与并行操作的天然兼容性——这是通向大规模量子计算的关键一步。

3. **三比特 Toffoli 门的原理性演示**：利用三体里德堡相互作用直接实现 CCZ 门（而非线路分解），展示了中性原子平台在多比特操控上的独特潜力。

### 5.2 从 2019 到 2023 的技术演进线索

如果你已经读过 [[start_up|2023 年 Nature 讲义]]，你会发现一条清晰的技术演进脉络：

| 技术维度 | 2019 年（本论文） | 2023 年（Nature） |
|---------|----------------|-----------------|
| CZ 门保真度 | $97.4(3)\%$ | $99.5\%$ |
| 核心创新 | 双脉冲全局协议 | 暗态（Dark State）相干 dressing |
| 主要误差来源 | 原子温度、激光散射 | 已大幅抑制 |
| 冷却技术 | 未使用 sideband cooling | 使用了 sideband cooling |
| 里德堡态 | $\vert 70S_{1/2}\rangle$ | $\vert 53S_{1/2}\rangle$（经优化选择） |
| 阵列维度 | 1D | 2D |

> [!tip] 关键洞察
> 从 $97.4\%$ 到 $99.5\%$ 的跨越，核心突破口是 **暗态物理** 的引入——通过消除中间态占据来消灭自发辐射这一"天花板级"噪声源。2019 年的论文虽然没有使用暗态，但其双脉冲全局协议的设计思想（用几何相位实现条件操作）在后续工作中得到了继承和发展。

### 5.3 论文展望的扩展方向

论文在结论中明确提出了多个可直接扩展的方向，这些在 2019 年之后逐一被实现：

1. **Sideband cooling（边带冷却）**：将光镊中的原子冷却到量子基态，消除热运动引起的拉比频率涨落。
2. **更高功率激光**：提升拉比频率 $\Omega$，缩短门时间，减少退相干窗口。
3. **更高真空度**：降低背景气体碰撞导致的原子丢失。
4. **非破坏性读出（nondestructive readout）**：实现重复测量而不丢失原子。
5. **2D/3D 原子阵列**：结合当时的二维/三维原子排列技术（Barredo et al., 2016; 2018），将并行门扩展到更大规模。
6. **非局域耦合**：通过额外的失谐激光系统，在稠密阵列中实现局域寻址与全局驱动的组合。
7. **高阶多比特门**：利用更多原子在阻塞体积内的集体效应，直接实现四比特、五比特门。

### 5.4 与同期其他平台的比较（2019 年视角）

论文将自己的结果与当时其他领先平台进行了横向对比：

| 平台 | 同时操控 qubit 数 | 两比特门保真度 |
|------|-----------------|--------------|
| **中性原子（本论文）** | 10+ | $97.4(3)\%$ |
| 超导（Wright et al., IBM） | 11 | 竞争水平 |
| 离子阱（Erhard et al., Innsbruck） | 10+ | 竞争水平 |
| 超导（Gong et al., 中科大） | 12 | 竞争水平 |

中性原子平台在 2019 年已经展现出与其他主流平台**同等水平**的保真度，同时具备**独特的可扩展性优势**（上千个原子的光镊阵列已实现，且门时间与体系大小无关）。

---

## 📐 核心公式摘要

| 符号 | 物理含义 | 公式 / 数值 |
|---|---|---|
| $\vert 0\rangle, \vert 1\rangle$ | 铷-87 超精细钟跃迁量子比特 | $\vert 5S_{1/2}, F=1, m_F=0\rangle$, $\vert 5S_{1/2}, F=2, m_F=0\rangle$ |
| $\vert r\rangle$ | 里德堡辅助态 | $\vert 70S_{1/2}, m_J=-1/2\rangle$ |
| $\Omega$ | 单原子有效拉比频率 | $2\pi \times 3.5\,\mathrm{MHz}$ |
| $V$ | 最近邻里德堡相互作用 | $2\pi \times 24\,\mathrm{MHz}$ |
| $\Omega_{\text{eff}}^{(11)}$ | 双原子集体拉比频率 | $\sqrt{2}\,\Omega$ |
| $\tau$ | 单束脉冲长度（$\vert 11\rangle$ 完成一周） | $2\pi / \sqrt{2\Omega^2 + \Delta^2}$ |
| $\Delta$ | 单光子失谐（CZ 工作点） | $\approx 0.377\,\Omega$ |
| $\xi$ | 两束脉冲间的激光相位跳变 | 由闭合轨迹条件决定 |
| $T_{\text{gate}}$ | CZ 门总时间 | $2\tau \approx 2.732\pi / \Omega \approx 0.4\,\mu\mathrm{s}$ |
| CZ 条件 | 动力学相位匹配 | $\phi_{11} = 2\phi_{01} - \pi$ |
| $F^{[c]}_{\text{CZ}}$ | SPAM 修正后 CZ 门保真度 | $\geq 97.4(3)\%$ |
| $F^{[c]}_{\text{CNOT}}$ | SPAM 修正后 CNOT 保真度 | $\geq 96.5(3)\%$ |
| $F^{[c]}_{\text{Toff}}$ | SPAM 修正后 Toffoli 保真度 | $\geq 87.0(4)\%$ |

---

## 💡 新知识点补全提醒

以下概念在本次讲义中出现，但目前尚未被完整收录到你的知识库中，建议补充笔记：

### 1. Dynamical Phase — 动力学相位
> 在含时或失谐量子演化中，系统沿闭合轨迹回到初态时积累的相位。对于布洛赫球上的轨迹，动力学相位与轨迹包围的"面积"相关。在 CZ 门协议中，正是通过控制不同计算基态的不同轨迹面积，来实现条件相位。
> 📍 **建议位置**：`Rydberg atom/Dynamical-Phase.md`
> 🔗 **建议链接**：[[Rabi-Flopping]]、[[CZ-Gate]]、[[Basis-Transformation]]

### 2. Echo Sequence — 回波序列
> 通过在演化中间插入 $\pi$ 脉冲（或等效操作），将不想要的外部噪声（如光移、磁场漂移）引起的相位误差反转抵消。这是核磁共振和量子信息中的标准技术。论文用 echo 来抵消 Rydberg 激光对超精细基态的光移。
> 📍 **建议位置**：`Rydberg atom/Echo-Sequence.md`
> 🔗 **建议链接**：[[Rabi-Flopping]]、[[AC-Stark-Effect]]

### 3. SPAM Error — 态制备与测量误差
> State Preparation and Measurement Error：实验中量子比特初始化和荧光读取固有的误差（约 $1\%$ 每原子）。必须通过多门累积、随机基准测试（RB）或真值表分析来剥离，不能通过单次 Bell 态测量来标定纯粹门保真度。
> 📍 **建议位置**：`Rydberg atom/SPAM-Error.md`
> 🔗 **建议链接**：[[CZ-Gate]]、[[QEC]]

### 4. Leakage — 量子比特子空间泄漏
> 门操作后，原子有一定概率留在里德堡态 $|r\rangle$ 或丢失，这些状态不属于计算基 $\{|0\rangle, |1\rangle\}$，称为"泄漏"。泄漏会导致保真度被高估（因为 $|r\rangle$ 在测量时表现为"原子缺失"，可能被误判为 $|1\rangle$）。论文通过单独测量来扣除泄漏贡献。
> 📍 **建议位置**：`Rydberg atom/Leakage.md`
> 🔗 **建议链接**：[[Rydberg-Blockade]]、[[CZ-Gate]]

### 5. Optimal Control / RedCRAB — 量子最优控制
> 当多体量子系统的动力学过于复杂、无法解析设计脉冲时，使用数值优化算法（如 RedCRAB、GRAPE）自动搜索最优的激光振幅/频率/相位波形。论文用 RedCRAB 来构造三比特 CCZ 门的脉冲。
> 📍 **建议位置**：`Rydberg atom/Optimal-Control.md`
> 🔗 **建议链接**：[[CZ-Gate]]、[[Entangling-Gate]]

### 6. Truth Table Fidelity — 真值表保真度
> 对门操作的直接表征方法：将门分别作用于所有计算基态，测量输出与理想输出的重叠度。真值表保真度直观、无歧义，但比过程层析（process tomography）或随机基准测试（RB）提供的信息少。
> 📍 **建议位置**：`Rydberg atom/Truth-Table-Fidelity.md`
> 🔗 **建议链接**：[[CZ-Gate]]、[[Entangling-Gate]]

---

## 🔗 相关笔记引用

- [[start_up]] — Lukin 组 2023 年 Nature 并行门讲义（后续高保真度工作，含暗态物理）
- [[Rydberg-Blockade]] — 里德堡阻塞机制与 $\sqrt{2}\,\Omega$ 集体增强的完整推导
- [[CZ-Gate]] — CZ 门的矩阵定义、CNOT 转换、投影算符推导
- [[Rabi-Flopping]] — 共振与非共振拉比振荡的基础推导
- [[Hyperfine-Structure]] — 超精细结构与钟跃迁
- [[Optical-Tweezer-Arrays]] — 光镊囚禁与原子排序
- [[Single-Qubit-Gates]] — 单比特门与 $HXH = Z$ 恒等式

---

## 📝 更新记录

- 2026-07-04: 初始创建，覆盖 2019 PRL 论文的双脉冲全局 CZ 门协议、Bell 态制备与保真度分析、Toffoli 门演示
- 2026-07-04: 添加布洛赫球轨迹与动力学相位曲线的 Python 可视化
- 2026-07-04: 补充 SPAM 修正、泄漏扣除、echo 序列等实验表征概念
- 2026-07-04: 生成新知识点补全提醒（动力学相位、回波序列、SPAM 误差、泄漏、最优控制、真值表保真度）
