---
aliases:
  - Rydberg Blockade
  - 里德堡阻塞
  - Rydberg Blockade Mechanism
  - 阻塞机制
tags:
  - Physics
  - Quantum
  - NeutralAtom
  - RydbergAtom
  - Gates
  - Entanglement
date: 2026-06-01
status: WIP
source: "[[generall quantum 2026]]"
comprehension: "don't understand"
---

# 里德堡阻塞（Rydberg Blockade）

> 📄 来源文献：[[generall quantum 2026]]
> 来源批注：*"Rydberg blockade"* — Bluvstein et al., 2026
> 本笔记是中性原子量子计算的核心概念。里德堡阻塞是实现两量子比特门（CZ 门）的物理机制，也是整个中性原子量子计算平台的基石。

---

## 1. 物理直觉：什么是里德堡阻塞？

### 1.1 从"两个孩子抢一把椅子"说起

想象一个场景：房间里只有一把椅子，两个孩子都想坐。如果一个孩子已经坐在椅子上了，另一个孩子就**坐不上去**——椅子被"占"了。

里德堡阻塞的物理图像与此类似：

> **当一个原子被激发到里德堡态（Rydberg state）后，它会"阻塞"附近的另一个原子，使后者无法也被激发到里德堡态。**

这不是因为激光不够强，而是因为**两个里德堡原子之间的相互作用太强了**——强到第二个原子的能级被大幅移动，激光频率完全无法共振激发它。

> [!tip] 核心类比
> 里德堡阻塞就像"两个孩子抢一把椅子"——一个原子坐了里德堡态的"椅子"，另一个就坐不上去。这不是因为第二个孩子不想坐，而是椅子被"占"了（能级被移走了）。

### 1.2 什么是里德堡态？

里德堡态是原子的**极高激发态**——主量子数 $n$ 很大（通常 $n \sim 50-100$）的态。

里德堡原子的特殊性质：

| 性质 | 标度关系 | 物理含义 |
|------|---------|---------|
| 轨道半径 | $r \propto n^2$ | $n=60$ 时轨道半径约 $0.3\,\mu\text{m}$，比基态大 3600 倍 |
| 极化率 | $\alpha \propto n^7$ | 对电场极其敏感 |
| 相互作用能 | $V \propto n^{11}$ | 两个里德堡原子间的作用力极强 |
| 寿命 | $\tau \propto n^3$ | 激发态寿命较长（$\sim 100\,\mu\text{s}$） |

**关键**：$V \propto n^{11}$ 的标度关系意味着，只要 $n$ 足够大，两个里德堡原子之间的相互作用能可以远大于激光的[[Rabi-Flopping#^1212|拉比频率]]，从而产生"阻塞"效应。

---

## 2. 数学描述：阻塞条件

### 2.1 两原子系统

考虑两个相邻的原子 1 和 2，每个原子有两个能级参与工作：
- $\vert g\rangle$：基态（ground state，量子比特的 $\vert 0\rangle$）
- $\vert r\rangle$：里德堡态（Rydberg state，量子比特的 $\vert 1\rangle$）

激光驱动 $\vert g\rangle \leftrightarrow \vert r\rangle$ 跃迁，拉比频率为 $\Omega$，失谐为 $\Delta$。

**无相互作用时**的哈密顿量（单原子）：

$$
H_i = -\Delta \vert r\rangle\langle r| + \frac{\Omega}{2}(\vert g\rangle\langle r| + \vert r\rangle\langle g|)
$$

**有相互作用时**，两原子系统的完整哈密顿量：

$$
H = H_1 + H_2 + V_{12} \vert r\rangle\langle r| \otimes \vert r\rangle\langle r|
$$

最后一项 $V_{12} \vert r\rangle\langle r| \otimes \vert r\rangle\langle r|$ 中的 [[Tensor-Product|张量积]] 是关键——**只有当两个原子同时处于里德堡态时，相互作用才生效**。

### 2.2 相互作用的来源：van der Waals 力

两个里德堡原子之间的相互作用主要是**长程 van der Waals 相互作用**：

$$
V_{12} = \frac{C_6}{R^6}
$$

其中：
- $R$ 是两个原子之间的距离
- $C_6$ 是 van der Waals 系数，$C_6 \propto n^{11}$（随主量子数急剧增大）

对于 $n \sim 60$ 的里德堡态，$C_6$ 非常大，即使在几微米的距离上，$V_{12}$ 也可以达到 $\sim \text{MHz}$ 量级。

### 2.3 阻塞条件

**阻塞发生的条件**：相互作用能 $V_{12}$ 远大于激光的拉比频率 $\Omega$：

$$
V_{12} \gg \Omega
$$

此时，能级图变为：

```
无相互作用：                    有相互作用（阻塞）：
|g,g⟩  ─────────              |g,g⟩  ─────────
                                    ↑ Ω (允许)
|g,r⟩  ──── ↑ Ω ────           |g,r⟩  ──── ↑ Ω ────
                                    ↓ Ω (允许)
|r,g⟩  ──── ↑ Ω ────           |r,g⟩  ──── ↑ Ω ────
                                    ↑↑ 被阻塞！
|r,r⟩  ──── ↑ Ω ────           |r,r⟩  ───────── + V₁₂
                                    (能级偏移太大，激光无法共振)
```

当两个原子同时处于 $\vert r\rangle$ 时，$\vert r,r\rangle$ 的能量被抬高了 $V_{12}$。如果 $V_{12} \gg \Omega$，激光的频率远远无法共振到 $\vert r,r\rangle$ 态——**第二个原子的激发被"阻塞"了**。

### 2.4 阻塞半径

定义**阻塞半径** $R_b$ 为相互作用能等于拉比频率时的距离：

$$
V_{12}(R_b) = \Omega \quad \Rightarrow \quad R_b = \left(\frac{C_6}{\Omega}\right)^{1/6}
$$

**物理含义**：
- 当两个原子距离 $R < R_b$ 时，阻塞效应显著——不能同时激发两个原子
- 当 $R > R_b$ 时，相互作用很弱，两个原子可以独立激发

典型的阻塞半径在 $R_b \sim 5-15\,\mu\text{m}$（取决于 $n$ 和 $\Omega$）。

```python
import matplotlib.pyplot as plt
import numpy as np

# Physical parameters
n_principal = 60
C6 = 5.0e9  # MHz * um^6 (typical for n~60)
Omega = 2 * np.pi * 1.0  # Rabi frequency in MHz (2*pi*1 MHz)

# Distance range
R = np.linspace(1, 25, 500)  # in micrometers

# van der Waals interaction
V = C6 / R**6

# Blockade radius
R_b = (C6 / Omega)**(1/6)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# --- Left panel: V(R) and blockade radius ---
ax1.plot(R, V, color='#1f77b4', linewidth=2.5, label=r'$V_{12}(R) = C_6 / R^6$')
ax1.axhline(y=Omega, color='#d62728', linewidth=2, linestyle='--',
            label=r'Rabi frequency $\Omega$')
ax1.axvline(x=R_b, color='#ff7f0e', linewidth=2, linestyle=':',
            label=r'Blockade radius $R_b$')

# Shade blocked region
ax1.fill_between(R, 0, V, where=(R < R_b), alpha=0.15, color='#d62728',
                 label='Blockade regime')

ax1.set_xlabel(r'Inter-atomic distance $R$ ($\mu$m)', fontsize=12)
ax1.set_ylabel(r'Interaction energy $V_{12}$ (MHz)', fontsize=12)
ax1.set_title('van der Waals Interaction vs Distance', fontsize=13, fontweight='bold')
ax1.set_yscale('log')
ax1.set_xlim(1, 25)
ax1.set_ylim(1e-2, 1e6)
ax1.legend(frameon=False, fontsize=9, loc='upper right')
ax1.grid(alpha=0.3, ls=':')

# Annotate blockade radius
ax1.annotate(rf'$R_b \approx {R_b:.1f}\,\mu$m',
             xy=(R_b, Omega), xytext=(R_b + 3, Omega * 50),
             fontsize=11, color='#ff7f0e', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=1.5))

# --- Right panel: Energy level diagram ---
ax2.set_xlim(0, 10)
ax2.set_ylim(-1, 7)
ax2.axis('off')
ax2.set_title('Energy Levels: Blockade Mechanism', fontsize=13, fontweight='bold')

c_g = '#2ca02c'
c_r = '#d62728'
c_blocked = '#ff7f0e'

# |g,g> level
ax2.plot([0.5, 2.5], [0, 0], color=c_g, linewidth=3)
ax2.text(1.5, -0.4, r'$\vert g,g\rangle$', fontsize=11, ha='center', color=c_g, fontweight='bold')

# |g,r> level
ax2.plot([0.5, 2.5], [2, 2], color='#1f77b4', linewidth=3)
ax2.text(1.5, 1.6, r'$\vert g,r\rangle$', fontsize=11, ha='center', color='#1f77b4', fontweight='bold')

# |r,g> level
ax2.plot([0.5, 2.5], [4, 4], color='#1f77b4', linewidth=3)
ax2.text(1.5, 3.6, r'$\vert r,g\rangle$', fontsize=11, ha='center', color='#1f77b4', fontweight='bold')

# |r,r> level (shifted up by V12)
ax2.plot([0.5, 2.5], [6.5, 6.5], color=c_blocked, linewidth=3, linestyle='--')
ax2.text(1.5, 6.9, r'$\vert r,r\rangle + V_{12}$', fontsize=11, ha='center',
         color=c_blocked, fontweight='bold')

# Allowed transitions (green arrows)
ax2.annotate('', xy=(1.5, 1.9), xytext=(1.5, 0.1),
             arrowprops=dict(arrowstyle='<->', color=c_g, lw=2))
ax2.annotate('', xy=(1.5, 3.9), xytext=(1.5, 2.1),
             arrowprops=dict(arrowstyle='<->', color=c_g, lw=2))
ax2.text(0.3, 1.0, r'$\Omega$', fontsize=12, color=c_g, fontweight='bold')
ax2.text(0.3, 3.0, r'$\Omega$', fontsize=12, color=c_g, fontweight='bold')

# Blocked transition (red X)
ax2.annotate('', xy=(1.5, 6.4), xytext=(1.5, 4.1),
             arrowprops=dict(arrowstyle='->', color=c_blocked, lw=2, linestyle='dashed'))
ax2.text(0.3, 5.2, 'BLOCKED', fontsize=10, color=c_blocked, fontweight='bold', rotation=90)

# V12 annotation
ax2.annotate('', xy=(3.5, 6.5), xytext=(3.5, 4.0),
             arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
ax2.text(4.2, 5.25, r'$V_{12} \gg \Omega$', fontsize=11, color='gray', fontweight='bold')

# Labels
ax2.text(7, 6.5, 'Without blockade:', fontsize=10, fontweight='bold', va='center')
ax2.text(7, 6.0, r'$\vert r,r\rangle$ accessible', fontsize=10, va='center', color='gray')
ax2.text(7, 3.0, 'With blockade:', fontsize=10, fontweight='bold', va='center')
ax2.text(7, 2.5, r'$\vert r,r\rangle$ shifted far away', fontsize=10, va='center', color=c_blocked)
ax2.text(7, 2.0, r'$\Rightarrow$ second atom cannot be excited', fontsize=10, va='center', color=c_blocked)

plt.tight_layout()
plt.show()
```

### 2.5 集体 Rabi 频率（√2Ω）

#### 物理图像

当两个原子处于阻塞半径之内，并被同一束激光（拉比频率 $\Omega$）驱动时，系统并不是简单地对每个原子独立地以 $\Omega$ 做 Rabi 振荡。由于阻塞的存在，$\vert r,r\rangle$ 被排除在外，系统的有效演化空间变为 $\{\vert g,g\rangle,\ \vert g,r\rangle,\ \vert r,g\rangle\}$ 这个三能级子空间。

关键在于：从 $\vert g,g\rangle$ 出发，激光可以经由两条路径到达单激发态——先激发原子 1（$\vert g,g\rangle \to \vert r,g\rangle$），或者先激发原子 2（$\vert g,g\rangle \to \vert g,r\rangle$）。这两条量子路径会**相干叠加**，产生 $\sqrt{2}$ 的增强因子。

#### 数学推导

两原子系统的哈密顿量在 $\{\vert g,g\rangle,\ \vert g,r\rangle,\ \vert r,g\rangle,\ \vert r,r\rangle\}$ 基底下写为：

$$
H = \frac{\Omega}{2}\Big(\vert g,r\rangle\langle g,g\vert + \vert r,g\rangle\langle g,g\vert + \vert r,r\rangle\langle g,r\vert + \vert r,r\rangle\langle r,g\vert + \text{h.c.}\Big) + V_{12}\vert r,r\rangle\langle r,r\vert
$$

其中 $\Omega/2$ 来自单原子的激光耦合强度（旋转波近似，rotating-wave approximation，下的 Rabi 频率的一半）。

在阻塞区间 $V_{12} \gg \Omega$，$\vert r,r\rangle$ 被能量排斥，可以用 [[Adiabatic-Elimination|绝热消去]] 的直觉从动力学中近似移除。简单说，$\vert r,r\rangle$ 像一个被推到很高处的能级，激光虽然仍然“看得见”它，但因为能量失配太大，系统几乎不会真正跑到那里；它主要只通过微小的 off-resonant coupling（非共振耦合）留下二阶修正。定义对称的 W 态：

$$
\vert W\rangle = \frac{1}{\sqrt{2}}\big(\vert g,r\rangle + \vert r,g\rangle\big)
$$

则 $\vert g,g\rangle$ 通过激光耦合到 $\vert W\rangle$ 的矩阵元为：

$$
\langle W\vert\, H_{\text{coupling}}\, \vert g,g\rangle = \frac{1}{\sqrt{2}} \cdot \frac{\Omega}{2} + \frac{1}{\sqrt{2}} \cdot \frac{\Omega}{2} = \frac{\Omega}{\sqrt{2}}
$$

两条路径（先激原子 1 和先激原子 2）各贡献 $\Omega/(2\sqrt{2})$，相干叠加后总耦合为 $\Omega/\sqrt{2}$，对应的集体 Rabi 频率为：

$$
\Omega_{\text{eff}} = \sqrt{2}\,\Omega
$$

因此，在阻塞区间内，$\{\vert g,g\rangle,\ \vert W\rangle\}$ 构成一个有效的二能级系统，以增强的 Rabi 频率 $\sqrt{2}\,\Omega$ 振荡。

> [!tip] 物理直觉
> √2 的增强来自**量子干涉**：两条路径（先激原子 1 或先激原子 2）不可区分，量子力学要求把概率幅相加再取模平方——两条等幅路径相干叠加，振幅变为单路径的 √2 倍。这与双缝干涉中"两个狭缝各贡献一半振幅，合起来光强翻倍"是同一个道理。
>
> 在 $\{\vert g,g\rangle,\ \vert W\rangle,\ \vert r,r\rangle\}$ 的 W 态表象下，图像更清晰：阻塞把 $\vert r,r\rangle$ 的能级抬高到远处，剩下的 $\{\vert g,g\rangle,\ \vert W\rangle\}$ 是一个二能级系统，耦合强度恰好是 $\sqrt{2}\,\Omega$。

#### 物理意义

- **√2 增强是量子干涉效应**：不是经典的"两个原子各驱动一次"，而是两条量子路径的相干叠加。
- **W 态子空间**：在阻塞区间内，系统的动力学被限制在三维子空间 $\{\vert g,g\rangle,\ \vert W\rangle,\ \vert r,r\rangle\}$ 中；由于 $\vert r,r\rangle$ 被排斥，实际演化的有效空间是 $\{\vert g,g\rangle,\ \vert W\rangle\}$ 这个二能级系统。
- **CZ 门的优化脉冲设计**：在设计 CZ 门的脉冲时，需要使用 $\sqrt{2}\,\Omega$ 而非 $\Omega$ 来计算 $\pi$ 脉冲或 $2\pi$ 脉冲的持续时间，否则会得到错误的相位。例如，$\pi$ 脉冲时间为 $t_\pi = \pi / (\sqrt{2}\,\Omega)$。

> [!info] 与 start_up 笔记的联系
> 关于 $\sqrt{2}$ 因子的更详细推导（含数值模拟），参见 [[start_up#2. 双原子希尔伯特空间的演维与 \sqrt{2} 的魔力]]。该笔记从 $\vert g,g\rangle \to \vert r,r\rangle$ 的双光子过程出发，展示了阻塞如何将四维空间压缩为二维，并用 Python 模拟了 Rabi 振荡的增强效应。

---

## 3. 里德堡阻塞如何实现 CZ 门？

### 3.1 CZ 门回顾

[[CZ-Gate]] 的作用是：当且仅当两个 qubit 都处于 $\vert 1\rangle$ 时，引入 $\pi$ 相位：

$$
\text{CZ} = \text{diag}(1, 1, 1, -1)
$$

在中性原子系统中，我们将逻辑态映射为：
- $\vert 0\rangle \equiv \vert g\rangle$（基态）
- $\vert 1\rangle \equiv \vert r\rangle$（里德堡态）

> [!warning] 简化模型说明
> 这里为了突出阻塞机制，把逻辑态简化写成 $\vert g\rangle$ 与 $\vert r\rangle$ 的二能级模型。真实的中性原子量子比特通常编码在两个长寿命 ground / hyperfine states（基态或超精细态）中，Rydberg state 更多作为门操作中的辅助激发态；实际脉冲会先把某个逻辑态临时耦合到里德堡态，再利用阻塞产生条件相位。

### 3.2 阻塞实现 CZ 的步骤

**目标**：对两个原子施加 CZ 门，使得 $\vert r,r\rangle$ 获得 $-1$ 相位，其他态不变。

**方法**：利用里德堡阻塞，让 $\vert g,r\rangle$、$\vert r,g\rangle$、$\vert g,g\rangle$ 正常演化，但 $\vert r,r\rangle$ 因为阻塞而**不参与演化**。

具体步骤：

**Step 1：初始化**
- 原子 1（控制比特）处于任意态 $\alpha\vert g\rangle + \beta\vert r\rangle$
- 原子 2（目标比特）处于 $\vert g\rangle$

**Step 2：对原子 2 施加 $\pi$ 脉冲**
- 如果原子 1 在 $\vert g\rangle$：原子 2 从 $\vert g\rangle \to \vert r\rangle$（正常激发）
- 如果原子 1 在 $\vert r\rangle$：原子 2 的激发被阻塞，**保持在 $\vert g\rangle$**

**Step 3：对两个原子同时施加 $2\pi$ 脉冲**
- 这个脉冲让 $\vert g\rangle \to \vert r\rangle \to \vert g\rangle$，积累 $-1$ 相位
- 但由于阻塞，$\vert r,r\rangle$ 不参与这个过程

**Step 4：对原子 2 施加 $\pi$ 脉冲（反向）**
- 将原子 2 的状态恢复

最终效果：

| 初始态 | 演化过程 | 最终态 | 相位 |
|--------|---------|--------|------|
| $\vert g,g\rangle$ | 正常 | $\vert g,g\rangle$ | $+1$ |
| $\vert g,r\rangle$ | 正常 | $\vert g,r\rangle$ | $+1$ |
| $\vert r,g\rangle$ | 被阻塞 | $\vert r,g\rangle$ | $+1$ |
| $\vert r,r\rangle$ | 被阻塞 | $-\vert r,r\rangle$ | $-1$ |

这正是 CZ 门的效果！

> [!example] HTML 动态解释：Rydberg blockade 实现 CZ
> 这是重新生成的紧凑版交互图：无内部滚动依赖，所有控制按钮都放在顶部。若 Obsidian iframe 仍然显示异常，请直接看下面的 Python fallback 图表。

<iframe src="file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/tools/rydberg_blockade_cz_dynamic.html" width="100%" height="690" style="border:1px solid #d8dee9; border-radius:8px;"></iframe>

> [!example] Python 图表：Rydberg blockade 实现 CZ 的步骤
> 下图用稳定的 Python + matplotlib 代码块展示 CZ gate 的脉冲时序与 blockade 物理图像。若需要交互版本，必须先确认 HTML/iframe 能在 Obsidian 中稳定渲染；否则优先保留此 Python fallback。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# --- Left panel: CZ gate implementation timeline ---
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('CZ Gate via Rydberg Blockade', fontsize=13, fontweight='bold')

c_ctrl = '#1f77b4'
c_tgt = '#d62728'
c_block = '#ff7f0e'

ax.plot([1, 9], [3, 3], 'k-', linewidth=1, alpha=0.3)

steps = [
    (1.5, 'Init', r'$\alpha\vert g\rangle+\beta\vert r\rangle$', r'$\vert g\rangle$', c_ctrl, c_tgt),
    (3.5, r'$\pi$ pulse', 'No change', r'$\vert g\rangle \to \vert r\rangle$', c_ctrl, c_tgt),
    (5.5, r'$2\pi$ pulse', r'Phase $-1$ if $\vert r\rangle$', 'BLOCKED!', c_ctrl, c_block),
    (7.5, r'Reverse $\pi$', 'No change', r'$\vert r\rangle \to \vert g\rangle$', c_ctrl, c_tgt),
]

for x, label, ctrl_txt, tgt_txt, ctrl_col, tgt_col in steps:
    ax.add_patch(mpatches.FancyBboxPatch(
        (x - 0.8, 4.2), 1.6, 0.8,
        boxstyle='round,pad=0.1', facecolor=c_ctrl,
        edgecolor='black', alpha=0.75
    ))
    ax.text(x, 4.6, label, ha='center', va='center', fontsize=9,
            color='white', fontweight='bold')

    ax.add_patch(mpatches.FancyBboxPatch(
        (x - 0.8, 2.0), 1.6, 0.8,
        boxstyle='round,pad=0.1', facecolor=tgt_col,
        edgecolor='black', alpha=0.75
    ))
    ax.text(x, 2.4, tgt_txt, ha='center', va='center', fontsize=8, color='white')
    ax.text(x, 5.45, ctrl_txt, ha='center', va='center', fontsize=8, color=c_ctrl)

ax.text(1.5, 5.85, 'Control qubit', fontsize=9, fontweight='bold', ha='center', color=c_ctrl)
ax.text(1.5, 1.2, 'Target qubit', fontsize=9, fontweight='bold', ha='center', color=c_tgt)
ax.text(5, 0.45, r'Result: only $\vert r,r\rangle$ gets phase $-1$ = CZ gate',
        fontsize=10, ha='center', color=c_block, fontweight='bold')

# --- Right panel: conditional blockade diagram ---
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 7)
ax2.axis('off')
ax2.set_title('Conditional Target Excitation', fontsize=13, fontweight='bold')

# Case A: control in |g>
ax2.text(0.5, 6.2, r'Case A: control in $\vert g\rangle$', fontsize=11, color=c_ctrl, fontweight='bold')
ax2.plot([1.2, 3.0], [5.2, 5.2], color=c_ctrl, lw=3)
ax2.text(2.1, 5.45, r'$\vert g\rangle$', ha='center', fontsize=10, color=c_ctrl)
ax2.plot([5.0, 6.8], [5.2, 5.2], color=c_tgt, lw=3)
ax2.text(5.9, 5.45, r'$\vert g\rangle \to \vert r\rangle$', ha='center', fontsize=10, color=c_tgt)
ax2.annotate('', xy=(4.7, 5.2), xytext=(3.3, 5.2),
             arrowprops=dict(arrowstyle='->', color='#2ca02c', lw=2))
ax2.text(3.95, 5.55, r'allowed $\pi$ pulse', ha='center', fontsize=9, color='#2ca02c')

# Case B: control in |r>
ax2.text(0.5, 3.6, r'Case B: control in $\vert r\rangle$', fontsize=11, color=c_ctrl, fontweight='bold')
ax2.plot([1.2, 3.0], [2.6, 2.6], color=c_ctrl, lw=3)
ax2.text(2.1, 2.85, r'$\vert r\rangle$', ha='center', fontsize=10, color=c_ctrl)
ax2.plot([5.0, 6.8], [2.6, 2.6], color=c_tgt, lw=3)
ax2.text(5.9, 2.85, r'target stays $\vert g\rangle$', ha='center', fontsize=10, color=c_tgt)
ax2.annotate('', xy=(4.7, 2.6), xytext=(3.3, 2.6),
             arrowprops=dict(arrowstyle='->', color=c_block, lw=2, linestyle='--'))
ax2.text(3.95, 2.95, 'blocked', ha='center', fontsize=10, color=c_block, fontweight='bold')
ax2.plot([3.55, 4.45], [2.15, 3.05], color=c_block, lw=4)
ax2.plot([4.45, 3.55], [2.15, 3.05], color=c_block, lw=4)

# Phase table
rows = [
    (r'$\vert g,g\rangle$', '+1'),
    (r'$\vert g,r\rangle$', '+1'),
    (r'$\vert r,g\rangle$', '+1'),
    (r'$\vert r,r\rangle$', '-1'),
]
for i, (state, phase) in enumerate(rows):
    y = 1.0 - 0.35 * i
    color = c_block if phase == '-1' else '#334155'
    ax2.text(1.0, y, state, fontsize=10, color=color)
    ax2.text(3.5, y, phase, fontsize=10, color=color, fontweight='bold')
ax2.text(1.0, 1.35, 'Input state', fontsize=10, fontweight='bold')
ax2.text(3.5, 1.35, 'Final phase', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()
```

---

## 4. 阻塞条件的定量分析

### 4.1 什么情况下阻塞有效？

阻塞有效的条件是：

$$
\frac{V_{12}}{\Omega} \gg 1
$$

这个比值决定了 CZ 门的保真度。比值越大，$\vert r,r\rangle$ 被激发的概率越小，门保真度越高。

> [!warning] 常见误解
> 里德堡阻塞不是说"激光不够强所以激发不了第二个原子"。即使激光很强，只要 $V_{12} \gg \Omega$，第二个原子的能级被移走了，激光频率完全无法共振——这是能级失配的问题，不是强度问题。

具体来说，$\vert r,r\rangle$ 被错误激发的概率为：

$$
P_{\text{error}} \sim \left(\frac{\Omega}{V_{12}}\right)^2
$$

**数值例子**：
- $\Omega = 2\pi \times 1\,\text{MHz}$（典型拉比频率）
- $V_{12} = 2\pi \times 100\,\text{MHz}$（$R = 5\,\mu\text{m}$，$n = 60$）
- $P_{\text{error}} \sim (1/100)^2 = 10^{-4}$

这意味着 CZ 门的保真度可以达到 $\sim 99.99\%$！

> [!info] 典型实验数值参考
> Bluvstein et al. (2026) 报道的实验参数：$^{87}\text{Rb}$ 原子，$\vert 70S_{1/2}\rangle$ 里德堡态，阻塞半径 $R_b \approx 10\,\mu\text{m}$，CZ 门保真度 $\sim 99.5\%$，门操作时间 $\sim 0.3\,\mu\text{s}$。实际保真度受限于退相干、自发辐射和脉冲不完美等因素，理论上限 $\sim 99.99\%$ 在实验中尚未完全达到。

### 4.2 影响阻塞半径的因素

$$
R_b = \left(\frac{C_6}{\Omega}\right)^{1/6}
$$

| 增大 $R_b$ 的方法 | 效果 | 代价 |
|------------------|------|------|
| 增大 $n$（主量子数） | $C_6 \propto n^{11}$，效果极强 | 里德堡态寿命变长，但退相干也增加 |
| 减小 $\Omega$（拉比频率） | $R_b$ 增大 | 门操作变慢，退相干影响增大 |

实际实验中需要在两者之间权衡，通常选择 $n \sim 60-80$，$\Omega \sim 2\pi \times (0.5-5)\,\text{MHz}$。

---

## 5. 里德堡阻塞在中性原子量子计算中的角色

### 5.1 作为两比特门的基础

里德堡阻塞是中性原子平台实现**所有两比特门**的物理基础：

- **CZ 门**：直接利用阻塞（如上所述）
- **CNOT 门**：CZ + [[Single-Qubit-Gates|单比特门]]组合
- **横向 CZ 门**：[[Transversal-Gate]] 中对多个原子对并行施加 CZ
- **[[Transversal-Teleportation]]**：利用横向 CZ 作为纠缠资源

### 5.2 在量子纠错中的应用

- **[[Surface-Code]]** 的 stabilizer 测量需要两比特门 → 由里德堡阻塞介导的 CZ 门实现
- **[[Deep-Circuit-Execution]]** 中的横向隐形传态依赖高保真度的并行 CZ 门
- **Magic state distillation** 需要大量 CZ 门 → 里德堡阻塞的并行性是关键优势

### 5.3 实验参数（Bluvstein et al., 2026）

论文中使用的典型参数：
- 原子种类：$^{87}\text{Rb}$（铷-87）
- 里德堡态：$\vert r\rangle = \vert 70S_{1/2}\rangle$（$n = 70$）
- 阻塞半径：$R_b \approx 10\,\mu\text{m}$
- CZ 门保真度：$\sim 99.5\%$
- 门操作时间：$\sim 0.3\,\mu\text{s}$

---

## 📐 核心公式摘要

| 符号 | 物理含义 | 理论公式 / 数值 |
|---|---|---|
| $V_{12}$ | 两原子 van der Waals 相互作用 | $V_{12} = C_6 / R^6$ |
| $C_6$ | van der Waals 系数 | $C_6 \propto n^{11}$ |
| $R_b$ | 阻塞半径 | $R_b = (C_6 / \Omega)^{1/6}$ |
| $V_{12} \gg \Omega$ | 阻塞有效的判据 | 相互作用能远大于激光 Rabi 频率 |
| $P_{\text{error}}$ | 错误激发概率 | $P_{\text{error}} \sim (\Omega / V_{12})^2$ |
| $\Omega_{\text{eff}}$ | 集体 Rabi 频率（阻塞区间） | $\Omega_{\text{eff}} = \sqrt{2}\,\Omega$ |
| $\vert W\rangle$ | 对称 W 态 | $\vert W\rangle = (\vert g,r\rangle + \vert r,g\rangle)/\sqrt{2}$ |
| $H$ | 两原子哈密顿量 | $H = H_1 + H_2 + V_{12}\vert r\rangle\langle r\vert \otimes \vert r\rangle\langle r\vert$ |


---

## 🔗 相关笔记

- [[Entangling-Gate]] — 纠缠门的概念总览：定义、判据、分类、各平台实现
- [[Two-Qubit-Gates]] — 两比特门总览：里德堡阻塞是实现 CZ 门的核心物理机制
- [[CZ-Gate]] — 里德堡阻塞实现的门操作的逻辑定义
- [[Rabi-Flopping]] — 驱动 $\vert g\rangle \leftrightarrow \vert r\rangle$ 跃迁的物理机制
- [[Transversal-Gate]] — 并行施加多个 CZ 门的容错方案
- [[Transversal-Teleportation]] — 利用横向 CZ 实现逻辑态传送
- [[Deep-Circuit-Execution]] — 里德堡阻塞在深度电路中的应用
- [[Optical-Tweezer-Arrays]] — 囚禁和排列原子的硬件平台
- [[QEC]] — stabilizer 测量依赖 CZ 门
- [[Tensor-Product]] — 两原子哈密顿量中复合系统空间的基本结构
- [[Adiabatic-Elimination]] — 解释阻塞区间中 $\vert r,r\rangle$ 如何被近似移出有效动力学
- [[Single-Qubit-Gates]] — CNOT 可由 CZ 与单比特门组合得到

## 📝 更新记录

- 2026-06-03: 修复 Markdown 表格中的 ket 写法，将 `\|...\rangle` 改为 `\vert ...\rangle`，避免表格渲染错乱。
- 2026-06-01: 初始创建，包含阻塞条件、CZ 门实现、Python 图表 ×2
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
- 2026-06-04: 新增 §2.5 集体 Rabi 频率（√2Ω），含物理图像、数学推导、W 态子空间分析及与 start_up 笔记的交叉链接；更新核心公式摘要
- 2026-06-06: [doc-audit] 格式审查与增强
  - 补全现有概念链接：[[Tensor-Product]]、[[Adiabatic-Elimination]]、[[Single-Qubit-Gates]]
  - 将核心公式摘要改为三列表格
  - 修复 Python 图表代码中的 LaTeX raw string / f-string 写法，保留 `plt.show()` 可执行代码块
  - 补充来源文献行、CZ 门简化模型 warning 与绝热消去直觉说明
- 2026-06-06: 将 §3.2 的 CZ 静态 Python 图表替换为 `tools/rydberg_blockade_cz_dynamic.html` 动态交互解释。
- 2026-06-06: ?? ?3.2 ?? HTML ? ??? ?????? iframe ???? `?` ????
- 2026-06-06: ? ?3.2 ???? HTML/iframe ?????????? Python fallback ????? iframe ??????????
- 2026-06-06: ???? ?3.2 ??? HTML ???????? Python fallback?
