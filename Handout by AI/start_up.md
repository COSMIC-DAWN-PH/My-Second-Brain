---
aliases: [Lukin 2023 Parallel Gates Handout, 并行门讲义, start_up]
tags: [Physics, Quantum, Handout, NeutralAtom, Rydberg]
date: 2026-05-20
status: WIP
---

# 🚀 极速起步：中性原子并行纠缠门文献研读讲义 (start_up)

> **导言**
> 欢迎来到中性原子量子计算的最前沿！本讲义专为物理系大二的你设计。你已经学习了**原子物理学中的自旋**以及**量子力学中的表象理论**，这些正是理解本篇里程碑式论文——*“High-fidelity parallel entangling gates on a neutral-atom quantum computer” (Nature 2023, Lukin Group)*——所需要的核心工具。
> 本讲义将摒弃繁琐晦涩的工程细节，专注于**物理图像的建立**与**循循善诱的数学推导**。通过本讲义，你将发现你所学到的抽象量子算符和基矢表象，是如何直接变成控制数十个原子发生纠缠的“物理魔法”的。

---

## 🔬 第一部分：物理载体——如何在中性原子中编码量子比特？

在开始复杂的门操控之前，我们首先要问一个最根本的物理问题：**量子比特 $|0\rangle$ 和 $|1\rangle$ 到底是什么？**

在超导量子计算中，量子比特是人工设计的约瑟夫森结微腔；在离子阱中，是带电离子的能级。而在本篇论文所代表的**中性原子平台**中，量子比特被编码在**单个中性铷-87 ($^{87}\mathrm{Rb}$) 原子**的超精细基态中。

### 1. 从原子物理的自旋耦合谈起

让我们复习一下原子物理中经典的**自旋-轨道耦合（Spin-Orbit Coupling）**与**超精细结构（Hyperfine Structure）**。
铷-87 ($^{87}\mathrm{Rb}$) 是碱金属原子，其最外层只有一个价电子。
- 它的核自旋为 $I = 3/2$。
- 电子的总角动量在基态 $5S_{1/2}$ 时，轨道角动量 $L = 0$，电子自旋 $S = 1/2$，因此电子总角动量为 $J = 1/2$。

根据角动量耦合理论，原子核自旋与电子总角动量会发生超精细耦合：
$$
\mathbf{F} = \mathbf{I} + \mathbf{J}
$$
由于 $I=3/2, J=1/2$，耦合后的总角动量量子数 $F$ 只能取两个值：
- $F = I + J = 2$ （共 $2F+1 = 5$ 个磁子能级（magnetic sublevel / Zeeman sublevel），即 $m_F = -2, -1, 0, 1, 2$）
- $F = I - J = 1$ （共 $2F+1 = 3$ 个磁子能级，即 $m_F = -1, 0, 1$）

这两个超精细能级之间的能量差在零外场下非常精确地等于 $6.8347\,\mathrm{GHz}$，这属于微波波段。

### 2. 利用表象理论定义量子比特

在量子力学中，我们选择一个合适的表象来写出状态矢。在这里，我们选择**超精细磁能级表象** $|F, m_F\rangle$。

为了构建一个二能级量子比特系统，本论文将量子比特编码在基态超精细结构的两个特定子能级上：
- $|0\rangle \equiv |F=1, m_F=0\rangle$
- $|1\rangle \equiv |F=2, m_F=0\rangle$

这两个能级在学术上被称为**“钟跃迁”（Clock Transition）**。

> 💡 **建立物理直觉：为什么非要选择 $m_F=0$ 的状态？**
> 想象一下，如果实验室里有微弱的杂散磁场波动。根据 Zeeman 效应，磁子能级会发生分裂，移动大小为 $\Delta E = g_F \mu_B B m_F$。
> 如果我们选 $m_F \neq 0$ 的态，磁场的微小波动就会剧烈改变 $|0\rangle$ 和 $|1\rangle$ 的能量差，导致相位漂移，也就是去相干（decoherence）！
> 而由于我们选了 $m_F = 0$，**一阶 Zeeman 位移恰好为零**！这使得编码在其中的量子比特对磁场涨落有极强的免疫力，相干时间（$T_2^*$）极大延长。这就是用单原子做量子比特的天然优势——高度一致且极其稳定。

在实验中，研究人员利用 [[Optical-Tweezer-Arrays|光镊阵列]] 将一个个铷原子囚禁在高度聚焦的激光束中，排列成一维或二维的阵列，每个光镊里刚好装一个原子，从而构建出极其整齐的量子比特阵列。

^260605
---

## ⚡ 第二部分：相干操控与拉比振荡

有了量子比特，我们如何让它在 $|0\rangle$ 和 $|1\rangle$ 之间变换，或者创造两者的叠加态？这就是**相干驱动**。

### 1. 单比特相干驱动：拉比振荡

如果你还记得 [[Rabi-Flopping|拉比振荡]]的物理图像：当一束微波或拉曼激光共振地照射原子时，原子会在 $|0\rangle$ 和 $|1\rangle$ 之间周期性地摆动。
在基矢表象 $\{|0\rangle, |1\rangle\}$ 下，系统的共振驱动 Hamiltonian 写为：
$$
H = \frac{\hbar\Omega}{2} \sigma_x = \frac{\hbar\Omega}{2} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$
如果初始状态为 $|0\rangle$，那么在驱动时间 $t$ 之后，系统跃迁到 $|1\rangle$ 的概率为：
$$
P_{|1\rangle}(t) = \sin^2\left(\frac{\Omega t}{2}\right)
$$
这就是最基础的共振拉比振荡（resonant Rabi oscillation）。如果施加一个时间满足 $\Omega t = \pi$ 的脉冲（即 $\pi$ 脉冲），就能实现量子比特的完全翻转（等效于 Pauli $X$ 门）。

你可以通过以下 Python 代码在 Obsidian 中实时绘制并感受共振与非共振下拉比振荡的物理图像区别：

```python
import matplotlib.pyplot as plt
import numpy as np

# Compatible with Obsidian Execute Code plugin
t = np.linspace(0, 3.0, 300) # Time in units of pi/Omega
P_res = np.sin(np.pi * t / 2) ** 2
tilde_omega = np.sqrt(1.0 + 1.5**2)
P_detuned = (1.0 / tilde_omega**2) * np.sin(tilde_omega * np.pi * t / 2) ** 2

plt.figure(figsize=(7, 4.0))
plt.plot(t, P_res, '-', color='#1f77b4', lw=2, label=r'Resonant ($\Delta = 0$)')
plt.plot(t, P_detuned, '--', color='#ff7f0e', lw=2, label=r'Detuned ($\Delta = 1.5\,\Omega$)')
plt.xlabel(r'Time $t$ ($\pi/\Omega$)')
plt.ylabel(r'Transition Probability $P_{|1\rangle}$')
plt.title('Rabi Oscillations Coherent Dynamics')
plt.grid(alpha=0.3, ls=':')
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
```

![拉比振荡](file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/Handout%20by%20AI/rabi_oscillations.png)

### 2. 双光子跃迁与中间态消去

然而，本篇论文的核心任务不是简单的单比特门，而是要实现**两比特纠缠门**。为了实现纠缠，我们必须将原子从基态 $|1\rangle$ 激发到能量极高的**里德伯态（Rydberg State，记为 $|r\rangle$）**。

> ❓ **这里有一个技术痛点**：
> 从基态 $|1\rangle$ 直接跃迁到里德伯态 $|r\rangle$ 需要波长非常短的深紫外激光（例如 $297\,\mathrm{nm}$）。这种紫外激光光子能量极高，不仅产生困难，而且极易导致原子电离或散射，带来不可容忍的噪声。
>
> **物理学家的绝妙解决方案**：**双光子共振过渡（two-photon resonance transition）**！
> 我们用两束激光：一束蓝色激光 ($420\,\mathrm{nm}$) 和一束红色激光 ($1013\,\mathrm{nm}$)，它们通过一个处于中间的短寿命激发态 $|e\rangle \equiv |6P_{3/2}\rangle$ 间接地将原子送上去！

现在，我们的系统从二能级变成了三能级，基底为 $\{|1\rangle, |e\rangle, |r\rangle\}$。
蓝色激光以拉比频率 $\Omega_b$ 驱动 $|1\rangle \to |e\rangle$，且有极大的单光子失谐 $\Delta$；红色激光以拉比频率 $\Omega_r$ 驱动 $|e\rangle \to |r\rangle$，同样有失谐 $\Delta$，从而使得整体依然保持**双光子共振**（或微小两光子失谐 $\delta$）。

写出三能级系统的 Hamiltonian 表象：
$$
H = \hbar \begin{pmatrix} 0 & \Omega_b/2 & 0 \\ \Omega_b/2 & -\Delta & \Omega_r/2 \\ 0 & \Omega_r/2 & -\delta \end{pmatrix}
$$

当单光子失谐 $\Delta$ 远大于激光的拉比频率时（即 $\Delta \gg \Omega_b, \Omega_r$），原子的电子几乎“没有时间”真正停留在中间态 $|e\rangle$。在物理上，我们可以将中间态 $|e\rangle$ **绝热消去（Adiabatic Elimination）**。
消去后，系统重新退化为一个有效二能级系统（effective two-level system） $\{|1\rangle, |r\rangle\}$，其有效拉比频率为：
$$
\Omega_{\mathrm{eff}} \approx \frac{\Omega_b \Omega_r}{2\Delta}
$$

> ⚠️ **关键的物理缺陷：自发辐射**
> 中间态 $|e\rangle$ 毕竟是有寿命的（寿命 $\tau_e \approx 110\,\mathrm{ns}$），即使我们使用了很大的失谐 $\Delta$，电子依然有极其微小的概率被激发到 $|e\rangle$ 并发生随机的自发辐射。这种自发辐射是这篇 Nature 论文之前限制门保真度（gate fidelity）的最主要物理噪声源！

### 3. 暗态物理学——化阻碍为武器

本篇论文取得 $99.5\%$ 超高保真度的绝对核心突破之一，就是利用了量子光学中的**暗态（Dark State）**物理！

让我们仔细分析上面那个三能级 Hamiltonian 的[[Gate-Eigenstates|门本征态]]。当双光子刚好共振（$\delta = 0$）时，我们发现存在一个特殊的本征态，它的中间态 $|e\rangle$ 组分**严格为零**！
定义参数 $\alpha \equiv \Omega_b / \Omega_r$，这个状态写为：
$$
|D\rangle = \frac{1}{\sqrt{1+\alpha^2}} |1\rangle - \frac{\alpha}{\sqrt{1+\alpha^2}} |r\rangle
$$
因为这个状态不包含任何短寿命中间态 $|e\rangle$ 的成分，所以即使它处于强激光照耀下，也绝对不会发生自发辐射散射！这在物理上被称为**相干完美相消（coherent perfect cancellation）**，该本征态即为**暗态**。
相反，另外两个本征态会包含 $|e\rangle$ 的成分，称为**明态（Bright State）**：
$$
|B\rangle \approx \frac{\alpha}{\sqrt{1+\alpha^2}} |1\rangle + \frac{\alpha\Omega_r}{2\Delta} |e\rangle + \frac{1}{\sqrt{1+\alpha^2}} |r\rangle
$$

> 💡 **论文的相干 dressing 图像**：
> 论文通过巧妙地在脉冲开始前调节蓝色与红色激光的相对相位，让初始处于基态 $|1\rangle$ 的原子在激光开启时**只投影并锁定在暗态 $|D\rangle$ 上**，从而在整个跃迁过程中几乎彻底避免了中间态 $|e\rangle$ 的自发散射误差！

以下 Python 仿真代码（严格使用论文的物理参数：$\Delta = 7.8\,\mathrm{GHz}$, $\Omega_r = 303\,\mathrm{MHz}$, $\Omega_b = 237\,\mathrm{MHz}$）展示了选择不同相位的分支（暗态 vs 亮态）时，中间态居量 $P_{|e\rangle}$ 的天壤之别：

```python
import matplotlib.pyplot as plt
import numpy as np

# Simulation parameters (in MHz, ns)
Delta = 7800.0  
Om_r = 303.0        
Om_b = 237.0        
T = 275.0
dt = 0.1
t = np.arange(0, T, dt)

# Detuning profile from two-photon phase modulation
A = 2 * np.pi * 0.1122
omega = 1.0431 * (2 * np.pi * 4.6 / 1000)
phi_0 = -0.7318
delta_profile = A * (omega * 1000 / (2*np.pi)) * np.sin(omega * t - phi_0)

def simulate(sign):
    psi = np.array([1.0+0.0j, 0.0j, 0.0j])
    P_e = []
    coeff = 2 * np.pi / 1000.0
    for idx in range(len(t)):
        curr_t = t[idx]
        scale = 1.0
        if curr_t < 15.0:
            scale = np.sin(np.pi * curr_t / 30.0)**2
        elif curr_t > T - 15.0:
            scale = np.sin(np.pi * (T - curr_t) / 30.0)**2
            
        H = np.zeros((3, 3), dtype=complex)
        H[0, 1] = H[1, 0] = (Om_b * scale) / 2.0
        H[1, 2] = H[2, 1] = Om_r / 2.0
        H[1, 1] = -Delta
        H[2, 2] = -sign * delta_profile[idx]
        
        # RK4 Time Evolution
        k1 = -1j * np.dot(H * coeff, psi)
        k2 = -1j * np.dot(H * coeff, psi + k1 * dt / 2)
        k3 = -1j * np.dot(H * coeff, psi + k2 * dt / 2)
        k4 = -1j * np.dot(H * coeff, psi + k3 * dt)
        psi = psi + (k1 + 2*k2 + 2*k3 + k4) * dt / 6.0
        psi /= np.linalg.norm(psi)
        P_e.append(np.abs(psi[1])**2)
    return P_e

P_bad = simulate(1)
P_good = simulate(-1)

plt.figure(figsize=(7, 4.0))
plt.plot(t, np.array(P_bad) * 1e4, '-', color='#d62728', label=r'Bright State Branch ($\delta\Delta > 0$)')
plt.plot(t, np.array(P_good) * 1e4, '-', color='#2ca02c', lw=2, label=r'Dark State Branch ($\delta\Delta < 0$)')
plt.xlabel('Time $t$ (ns)')
plt.ylabel(r'Intermediate State Population $P_{|e\rangle}$ ($\times 10^{-4}$)')
plt.title(r'Dark State Suppression ($\Delta = 7.8\,\mathrm{GHz}$)')
plt.grid(alpha=0.3, ls=':')
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
```

![暗态物理](file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/Handout%20by%20AI/dark_state_physics.png)

---

## 🛑 第三部分：里德伯阻塞与两粒子希尔伯特空间的奇妙膨胀

单比特控制好了，现在我们要让两个量子比特发生关联，制造量子纠缠。在中性原子体系中，唯一的纠缠魔法道具就是：**[[Rydberg-Blockade|里德伯阻塞（Rydberg Blockade）]]**。

### 1. 物理图像：为什么主量子数 $n=53$ 的态相互作用如此巨大？

当铷原子处于基态时，电子紧紧束缚在核附近，原子半径极小（约 $0.2\,\mathrm{nm}$），原子之间几乎没有任何相互作用。
但当我们把原子激发到主量子数极其巨大的里德伯态（例如 $n = 53$）时，原子会发生令人震惊的物理膨胀：
- **轨道半径**：以 $n^2$ 的速度急剧膨胀，半径达到 $\sim 150\,\mathrm{nm}$（放大了近千倍！电子轨道就像气球一样鼓起来）。
- **偶极矩**：以 $n^2$ 的速度增大。
- **范德华（Van der Waals）相互作用**：两个里德伯原子之间的偶极-偶极相互作用能量随着距离 $r$ 满足强烈的范德华指数衰减：
  $$
  V_{\mathrm{Ryd}}(r) = \frac{C_6}{r^6}
  $$
  最不可思议的是，范德华相互作用系数 $C_6 \propto n^{11}$！主量子数的 11 次方！这使得里德伯原子之间的相互作用比基态原子整整强了 **11 个数量级**！

里德伯阻塞的物理过程非常直白：
如果两个原子挨得很近（距离为 $r$），当一个原子已经被激发到里德伯态 $|r\rangle$ 时，它会给旁边的第二个原子施加一个巨大的能量移动 $V_{\mathrm{Ryd}}(r)$。如果激光只和单原子共振，那么因为能量不匹配，**第二个原子就绝对无法被激发到里德伯态**！这种一个原子的激发“霸占”了周围空间，使得其余原子被“阻塞”在基态的现象，就是**里德伯阻塞**。

我们定义**阻塞半径（blockade radius）** $R_b$ 为相互作用能量刚好等于激光驱动强度 $\Omega$ 的位置：
$$
\frac{C_6}{R_b^6} = \hbar\Omega \implies R_b = \left(\frac{C_6}{\hbar\Omega}\right)^{1/6}
$$
- 在本论文中，激光拉比频率为 $\Omega = 2\pi \times 4.6\,\mathrm{MHz}$，对于 $n=53$ 的里德伯态，计算得到阻塞半径 $R_b \approx 4.3\,\mu\mathrm{m}$。
- 而论文中原子的实际工作排布间距为 $d = 2.0\,\mu\mathrm{m} < R_b$。在这个距离下，范德华相互作用势高达 $V(d)/2\pi \approx 450\,\mathrm{MHz}$，整整是激光驱动强度的 **100倍**！因此，阻塞是绝对完美的。

```python
import matplotlib.pyplot as plt
import numpy as np

# Van der Waals interaction potential
r = np.linspace(1.5, 6.0, 500)
C6 = 28800.0  # MHz * um^6
V = C6 / (r ** 6)
Omega = 4.6

plt.figure(figsize=(7, 4.0))
plt.plot(r, V, '-', color='#d62728', lw=2, label=r'Van der Waals Potential $V(r) = C_6/r^6$')
plt.axhline(y=Omega, color='#2ca02c', ls='-.', label=r'Rabi Frequency $\Omega = 4.6\,\mathrm{MHz}$')
Rb = (C6 / Omega) ** (1/6)
plt.axvline(x=Rb, color='#9467bd', ls=':', label=fr'Blockade Radius $R_b \approx {Rb:.2f}\,\mu m$')
plt.fill_between(r[r <= Rb], 0, V[r <= Rb], color='#d62728', alpha=0.1, label='Blockade Region')
plt.scatter([2.0], [450.0], color='black', zorder=5)
plt.annotate(r'Operating Point $d = 2.0\,\mu m$', xy=(2.0, 450.0), xytext=(2.6, 300.0),
             arrowprops=dict(facecolor='black', shrink=0.08, width=0.5, headwidth=4))
plt.yscale('log')
plt.ylim(1e-1, 2e4)
plt.xlabel(r'Atomic Separation $r$ ($\mu m$)')
plt.ylabel(r'Interaction Energy $V(r)/2\pi$ (MHz)')
plt.grid(alpha=0.3, ls=':')
plt.legend(frameon=False)
plt.tight_layout()
plt.show()
```

![里德伯阻塞](file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/Handout%20by%20AI/rydberg_blockade.png)

### 2. 双原子希尔伯特空间的演维与 $\sqrt{2}$ 的魔力

现在，请用大二量子力学中熟练的**表象与算符理论**来推导两粒子系统在里德伯阻塞下的表现。

对于两个靠得很近（$d < R_b$）的原子，它们的联合状态处于四维计算基空间：
$$
\mathcal{H}_{\mathrm{comp}} = \operatorname{span}\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}
$$
根据门操作协议，状态 $|0\rangle$ 的原子对里德伯激发激光是不响应的。因此，激光只作用在基态 $|1\rangle$ 上。
让我们对不同的初始输入状态，分别写出它们在里德伯激光照射下的动力学行为：

#### 情况 A：初始态为 $|00\rangle$
由于两个原子都在 $|0\rangle$，对激光完全没有响应，状态保持不变，不积累任何相位：
$$
|00\rangle \to |00\rangle
$$

#### 情况 B：初始态为 $|01\rangle$ 或 $|10\rangle$
以 $|01\rangle$ 为例。第一个原子处于 $|0\rangle$ 保持静止。第二个原子处于 $|1\rangle$，它会被激光驱动到其里德伯态 $|r\rangle$。
此时系统的演化基矢空间为 $\{|01\rangle, |0r\rangle\}$。系统的有效驱动 Hamiltonian 就是最经典的单粒子二能级矩阵：
$$
H_{1Q} = \frac{\hbar}{2} \begin{pmatrix} 0 & \Omega \\ \Omega & 0 \end{pmatrix}
$$
如果整个门脉冲驱动原子从 $|1\rangle$ 绕一圈回到 $|1\rangle$，系统将积累一个单比特相位 $\phi_{1Q}$：
$$
|01\rangle \to e^{i\phi_{1Q}} |01\rangle, \quad |10\rangle \to e^{i\phi_{1Q}} |10\rangle
$$

#### 情况 C：初始态为 $|11\rangle$ —— 阻塞发生！
当两个原子都处于 $|1\rangle$ 时，它们都有可能被激发。如果没有里德伯相互作用，双原子演化空间应该包含状态 $|rr\rangle$。
然而，因为两原子距离太近，$|rr\rangle$ 的能量被抬高了 $V_{\mathrm{Ryd}} \approx 450\,\mathrm{MHz}$，远远偏离了共振。所以在表象理论中，我们可以**安全地从空间中将状态 $|rr\rangle$ 丢弃**！

这使得双原子被激光激发的演化空间被限制在三维空间中：
$$
\mathcal{H}_{\mathrm{active}} = \operatorname{span}\{|11\rangle, |1r\rangle, |r1\rangle\}
$$
在这组基下，激光均匀地作用于两个原子，驱动项为：
$$
H_{\text{drive}} = \frac{\hbar\Omega}{2} (|1r\rangle\langle 11| + |r1\rangle\langle 11|) + \mathrm{h.c.}
$$
为了看清物理本质，我们进行**基矢变换（basis transformation）**（表象理论的基底变换）。我们注意到，系统具有左右原子的交换对称性，因此我们定义对称和反对称基矢：
- 对称基（又称 W 态）：$|W\rangle \equiv \frac{|1r\rangle + |r1\rangle}{\sqrt{2}}$
- 反对称基：$|A\rangle \equiv \frac{|1r\rangle - |r1\rangle}{\sqrt{2}}$

现在，我们将 $H_{\text{drive}}$ 作用于这组新基上：
- $H_{\text{drive}}|A\rangle = 0$ （反对称态由于对称性，无法被单模全球激光（global laser beam）耦合，被完全隔离）。
- $H_{\text{drive}}|11\rangle = \frac{\hbar\Omega}{2} (|1r\rangle + |r1\rangle) = \frac{\hbar\sqrt{2}\Omega}{2} |W\rangle$。

这简直是魔术！在计算基 $|11\rangle$ 与对称激发态 $|W\rangle$ 构成的有效二能级子空间中，系统哈密顿量（Hamiltonian）写为：
$$
H_{2Q} = \frac{\hbar}{2} \begin{pmatrix} 0 & \sqrt{2}\Omega \\ \sqrt{2}\Omega & 0 \end{pmatrix}
$$

> 📐 **物理图像的跃迁：$\sqrt{2}$ 倍拉比频率的诞生！**
> 仔细观察上面的哈密顿量，双原子系统在完美的里德伯阻塞下， $|11\rangle \to |W\rangle$ 的相干物理摆动速度，竟然是单原子激发速度的 **$\sqrt{2}$ 倍**！
> 这就是多体量子相干增强的直接体现。正是由于这个 $\sqrt{2}$ 的出现，双量子比特状态 $|11\rangle$ 在脉冲作用下，在 Hilbert 空间中摆动的速度和轨迹，与单比特 $|01\rangle$ 完全不同。这就为我们创造“两比特纠缠相位”提供了最本质的物理机制！

---

## 🎨 第四部分：最佳控制门方案——时间最优门（Time-Optimal Gate）与平滑振幅门（Smooth-Amplitude Gate）

现在我们有了实现纠缠的筹码：单原子状态以速度 $\Omega$ 摆动，双原子状态以速度 $\sqrt{2}\Omega$ 摆动。那么我们如何设计一束精确的激光脉冲，让它们演化完毕后，刚好实现一个 [[CZ-Gate|CZ 纠缠门]] 呢？

### 1. CZ 门的目标条件

根据定义，一个对称的 $\mathrm{CZ}$ 门必须实现以下相位积累（排除单比特相位的自发积累）：
- $|00\rangle \to |00\rangle$ （积累相位 $0$）
- $|01\rangle \to e^{i\phi_{1Q}} |01\rangle$
- $|10\rangle \to e^{i\phi_{1Q}} |10\rangle$
- $|11\rangle \to e^{i\phi_{2Q}} |11\rangle$

要使这是一个纯粹的两比特 $\mathrm{CZ}$ 门，系统在计算基空间经过演化必须完全闭合（即高保真度返回计算基），且积累的非线性两比特净相位必须满足：
$$
\Delta \Phi \equiv \phi_{2Q} - 2\phi_{1Q} = (2k+1)\pi \pmod{2\pi}
$$
通常我们选择 $\Delta \Phi = \pi$。单比特积累的额外相位 $\phi_{1Q}$ 可以通过非常简单且无误差的“虚拟 Z 门（virtual Z gate）”（在激光控制软件中直接给后续脉冲改变一个相位参考）来完美补偿。

### 2. 脉冲设计方案：时间最优门 vs 平滑振幅门

在这篇 Nature 论文中，作者精心对比了两种最佳控制门方案（参数见 `physics-manager` 核心公式规范）：

#### A. 时间最优门 (Time-Optimal Gate)
- **物理图像**：保持激光振幅 $\Omega$ 恒定，仅对激光的相位 $\phi(t)$ 进行连续的高频调制。
- **相位公式**：
  $$
  \phi(t) = A \cos(\omega t - \phi_0) + \delta_0 t
  $$
  根据论文给出的精确优化参数：$A = 2\pi \times 0.1122$, $\omega = 1.0431\Omega$, $\phi_0 = -0.7318$, $\delta_0 = 0$。
- **演化时间**：总时间极短，仅为 $\Omega T / 2\pi = 1.215$（对于 $4.6\,\mathrm{MHz}$，相当于约 $264\,\mathrm{ns}$）。

#### B. 平滑振幅门 (Smooth-Amplitude Gate)
- **物理图像**：同时对激光的振幅 $\Omega(t)$ 和相位 $\phi(t)$ 进行平滑调制。
- **物理优势**：这能够让原子在演化过程中**始终完美地贴合在瞬时暗态 $|D\rangle$ 上**，几乎完全消除了中间激发态 $|e\rangle$ 的居量，从而获得了最强的自发辐射散射抑制力。
- **波形公式**：
  $$
  \Omega_{420}(t) = \Omega_{1013} \left( \Omega_0 + \Omega_1 \operatorname{sech}[\omega_0 (t - T/2)]^\alpha \right)
  $$
  $$
  \phi(t) = \delta_0 (t - T/2) + B \tanh[\lambda (t - T/2)]
  $$

你可以利用下面的 Python 脚本绘制出这两种截然不同的门控制脉冲，并在布洛赫球的动态演化中体会其美妙的物理图像：

```python
import matplotlib.pyplot as plt
import numpy as np

# Plotting the two gate waveforms from the paper
fig, axes = plt.subplots(2, 2, figsize=(10, 7.0))

# 1. Time-optimal Waveform
Omega_val = 4.6
T_to = 1.215 * 1000 / Omega_val
t_to = np.linspace(0, T_to, 300)
A = 2 * np.pi * 0.1122
omega_to = 1.0431 * (2 * np.pi * Omega_val / 1000)
phi_0 = -0.7318
phi_to = A * np.cos(omega_to * t_to - phi_0)

amp_to = np.ones_like(t_to) * 4.6
for i in range(len(t_to)):
    if t_to[i] < 15: amp_to[i] *= np.sin(np.pi * t_to[i] / 30)**2
    elif t_to[i] > T_to - 15: amp_to[i] *= np.sin(np.pi * (T_to - t_to[i]) / 30)**2

axes[0, 0].plot(t_to, amp_to, color='#1f77b4', lw=2)
axes[0, 0].set_ylabel('Rabi Frequency (MHz)')
axes[0, 0].set_title('Time-Optimal Gate: Amplitude')
axes[0, 0].grid(alpha=0.3, ls=':')

axes[1, 0].plot(t_to, phi_to / (2*np.pi), color='#ff7f0e', lw=2)
axes[1, 0].set_xlabel('Time $t$ (ns)')
axes[1, 0].set_ylabel(r'Laser Phase $\phi/(2\pi)$')
axes[1, 0].set_title('Time-Optimal Gate: Phase')
axes[1, 0].grid(alpha=0.3, ls=':')

# 2. Smooth-amplitude Waveform
T_sa = 1.207 * 1000 / Omega_val
t_sa = np.linspace(0, T_sa, 300)
tau = t_sa - T_sa / 2
omega_0 = 0.2668 * (2 * np.pi * Omega_val / 1000)
delta_0 = -0.9491 * (2 * np.pi * Omega_val / 1000)
B = 2 * np.pi * 0.2503
lambd = 0.9372 * (2 * np.pi * Omega_val / 1000)

amp_ratio = 32.7403 - 31.1404 * (1.0 / np.cosh(omega_0 * tau))**(-0.1131)
amp_sa = amp_ratio * (4.6 / np.max(amp_ratio))
phi_sa = delta_0 * tau + B * np.tanh(lambd * tau)

axes[0, 1].plot(t_sa, amp_sa, color='#2ca02c', lw=2)
axes[0, 1].set_title('Smooth-Amplitude Gate: Amplitude')
axes[0, 1].grid(alpha=0.3, ls=':')

axes[1, 1].plot(t_sa, phi_sa / (2*np.pi), color='#d62728', lw=2)
axes[1, 1].set_xlabel('Time $t$ (ns)')
axes[1, 1].set_title('Smooth-Amplitude Gate: Phase')
axes[1, 1].grid(alpha=0.3, ls=':')

plt.tight_layout()
plt.show()
```

![门波形参数](file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/Handout%20by%20AI/gate_waveforms.png)

---

## 📊 第五部分：基准测试——如何证明门保真度达到了 99.5%？

在物理实验中，声称自己做出了 $99.5\%$ 的超高保真度门，需要极其严苛的实验证明。单纯制备一个贝尔态（Bell state）并去测量它是远远不够的。

### 1. 为什么 Bell 态直接测量保真度会有上限？

如果你直接做一次 $\mathrm{CZ}$ 门，制备一个纠缠贝尔态：
$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$
然后去测它的保真度，你可能会得到一个 $98.0\%$ 的数值。
但这并不代表门保真度只有 $98\%$！因为在实验中，**状态的初始化准备**（State Preparation）和**最后的成像测量**（Measurement）本身就分别有约 $0.5\%$ 的固有误差。这种误差在学术上被称为 **SPAM 误差（State Preparation and Measurement error）**。
直接测量会把 SPAM 误差算在门操作的头上，从而低估了门的纯保真度。

### 2. 论文的物理妙招：门累积与指数衰减拟合（exponential decay fitting）

为了彻底剥离 SPAM 误差，论文采用了一种非常经典的量子信息表征方法：**相干门列车（coherent gate train）**（门累积法）。
- 如图 2c 所示，作者在两个原子上连续施加奇数个 $\mathrm{CZ}$ 门（如 $1, 5, 9, 13$ 个）。
- 每施加两个 $\mathrm{CZ}$ 门，系统理论上会经历“纠缠 $\to$ 解纠缠”的完整循环，重新回到初始状态。
- 如果门本身有误差，那么随着门施加次数 $N_{\mathrm{CZ}}$ 的增加，最终测得的态保真度会发生相干衰减。
- 我们将衰减曲线拟合为指数衰减形式：
  $$
  F(N_{\mathrm{CZ}}) = A \cdot (F_{\mathrm{CZ}})^{N_{\mathrm{CZ}}} + B
  $$
- 关键的数学直觉：**SPAM 误差只影响常数系数 $A$，而每一次门发生的纯粹物理误差则决定了衰减的快慢（底数 $F_{\mathrm{CZ}}$）**！

通过这种方式，作者成功剥离了测量仪器和准备过程的噪声，提取出纯粹的 $\mathrm{CZ}$ 两比特纠缠门物理保真度高达 **$99.52(4)\%$**，这一数值成功跨越了量子纠错著名的“表面码阈值（surface code threshold）”（$99\%$），成为中性原子量子计算历史上的重大里程碑！

---

## 📐 核心公式摘要

在学完本讲义后，请确保你完全掌握了以下核心物理量和数学表达的对应关系：

| 符号 | 物理含义 | 理论公式 / 数值 |
|---|---|---|
| $\vert 0\rangle, \vert 1\rangle$ | 铷-87 超精细钟跃迁量子比特能级 | $\vert F=1, m_F=0\rangle$, $\vert F=2, m_F=0\rangle$ |
| $\Omega_{\mathrm{eff}}$ | 双光子跃迁有效拉比频率 | $\Omega_{\mathrm{eff}} \approx \frac{\Omega_b \Omega_r}{2\Delta}$ |
| $\vert D\rangle$ | 三能级系统中的不自发辐射**暗态** | $\frac{1}{\sqrt{1+\alpha^2}}\vert 1\rangle - \frac{\alpha}{\sqrt{1+\alpha^2}}\vert r\rangle$ |
| $R_b$ | 里德伯阻塞半径 | $R_b = (C_6 / \hbar\Omega)^{1/6} \approx 4.3\,\mu\mathrm{m}$ |
| $H_{2Q}$ | 阻塞下双原子对称演化哈密顿量 | $\frac{\hbar}{2}\begin{pmatrix} 0 & \sqrt{2}\Omega \\\\ \sqrt{2}\Omega & 0 \end{pmatrix}$ （拉比频率增强 $\sqrt{2}$ 倍） |
| $\Delta\Phi$ | $\mathrm{CZ}$ 纠缠门的物理相位要求 | $\phi_{2Q} - 2\phi_{1Q} = (2k+1)\pi$ |
| $F_{\mathrm{CZ}}$ | 本论文实现的纠缠门最高保真度 | $99.52(4)\%$ |

祝贺你！你现在已经彻底建立起了这篇 Nature 论文的全部核心物理图像，并用大二的量子力学工具推导了其最本质的动力学。现在，充满信心地去打开 `2023-parallel gates.pdf` 原文吧，你一定会势如破竹！

---

## 💡 新知识点补全提醒

以下概念在本次讲义中首次出现，目前尚未被收录到你的两个知识库中，建议补充笔记：

### 1. Adiabatic Elimination — 绝热消去
> 当中间态失谐 $\Delta$ 远大于驱动强度时，可以"消去"中间态自由度，将三能级系统约化为有效二能级。核心结果：$\Omega_{\text{eff}} \approx \Omega_b\Omega_r/(2\Delta)$。
> 📍 **建议位置**：`Rydberg atom/Adiabatic-Elimination.md`
> 🔗 **建议链接**：[[Rabi-Flopping]]、[[Rydberg-Blockade]]

### 2. Dark State / Bright State — 暗态与亮态（完整笔记）
> 你的 Rydberg-Blockade.md 目前还是空文件。建议补全暗态的完整推导：暗态 $|D\rangle$ 与中间态耦合为零，完全避免散射；明态 $|B\rangle$ 包含中间态成分，容易产生自发辐射。
> 📍 **建议位置**：`Rydberg atom/Rydberg-Blockade.md`（已有文件，补充内容）
> 🔗 **建议链接**：[[Gate-Eigenstates]]、[[Rabi-Flopping]]

### 3. Symmetric / Antisymmetric Basis (W State) — 对称/反对称基矢
> 里德堡阻塞下双原子系统的对称基 $|W\rangle = (|1r\rangle + |r1\rangle)/\sqrt{2}$ 和反对称基 $|A\rangle = (|1r\rangle - |r1\rangle)/\sqrt{2}$。$|W\rangle$ 态是纠缠态，其三体版本是 GHZ 态之外的另一类多体纠缠态。
> 📍 **建议位置**：`Rydberg atom/W-State.md`
> 🔗 **建议链接**：[[Tensor-Product]]、[[CZ-Gate]]

### 4. Coherent Gate Train — 相干门列车方法
> 通过连续施加奇数个 CZ 门（1, 5, 9, 13…），测量保真度随门次数的指数衰减，从而**剥离 SPAM 误差**提取纯粹门保真度。
> 📍 **建议位置**：`Rydberg atom/Coherent-Gate-Train.md`
> 🔗 **建议链接**：[[CZ-Gate]]、[[QEC]]

### 5. SPAM Error — 初始化和测量误差
> State Preparation and Measurement Error：实验中初始化（光泵浦需 $\sim 99.5\%$）和测量（荧光读取）固有的误差。必须通过门累积或 RB 等方法剥离，不能通过单次 Bell 态测量来标定门保真度。
> 📍 **建议位置**：`Rydberg atom/SPAM-Error.md`
> 🔗 **建议链接**：[[QEC]]、[[Randomized-Benchmarking]]

### 6. Virtual Z Gate — 虚拟 Z 门
> 单比特相位 $\phi_{1Q}$ 可以通过在后续激光脉冲中改变相位参考来**零成本补偿**，无需物理执行任何门操作。这是量子编译中的标准技巧。
> 📍 **建议位置**：`Rydberg atom/Virtual-Z-Gate.md`
> 🔗 **建议链接**：[[CZ-Gate]]、[[Pauli-Matrices]]
