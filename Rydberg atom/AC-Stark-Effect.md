---
aliases:
  - AC Stark Effect
  - AC Stark 效应
  - 光频移
  - Light Shift
tags:
  - Physics
  - Quantum
  - AtomicPhysics
  - NeutralAtom
  - QuantumGates
  - Optics
date: 2026-03-29
status: WIP
source: "[[generall quantum 2026]]"
comprehension: "don't understand"
---

# AC Stark 效应（AC Stark Effect / Light Shift）

> 来源批注：中性原子量子计算基础概念
> AC Stark 效应是理解量子门操作、光镊囚禁、以及高保真量子比特操控的核心物理机制。本笔记从物理直觉出发，逐步推导数学公式，并联系中性原子量子计算的实际应用。

---

## 1. 物理直觉：光场如何移动能级？

想象一个原子的两个能级 $|g\rangle$（基态）和 $|e\rangle$（激发态），它们之间的跃迁频率为 $\omega_0$。现在用一束频率为 $\omega_L$ 的激光照射这个原子，但这束激光**不是精确共振的**——它有一个失谐 $\Delta = \omega_L - \omega_0$。

> [!tip] 核心直觉
> 虽然光子的能量"差了一点"不能真正激发原子跃迁，但光场的振荡电场会**"摇晃"**原子中的电子云，使得两个能级都发生偏移——这就是 AC Stark 效应。它本质上是**交流电场的二阶微扰效应**。

物理图像可以这样理解：

- 原子在光场中感受到一个**快速振荡的电场** $E(t) = E_0 \cos(\omega_L t)$
- 这个电场会与原子的电偶极矩耦合，产生一个随时间变化的相互作用
- 在**旋转波近似（RWA）**下，这个快速振荡的相互作用等效为一个**静态的能量偏移**
- 偏移的方向和大小取决于失谐 $\Delta$ 的符号和大小

> [!info] 与 DC Stark 效应的对比
> DC Stark 效应是**静电场**引起的能级分裂（线性或二次），而 AC Stark 效应是**交变电磁场**（光场）引起的能级偏移。两者物理本质不同：DC 效应直接偏转电子云，AC 效应通过"受迫振荡"间接影响能级。

---

## 2. 核心公式：光频移

### 2.1 二阶微扰推导

**第 1 步：写出含时微扰**

激光电场在原子上诱导的相互作用哈密顿量为：

$$
\hat{H}'(t) = -\hat{d} \cdot \mathbf{E}_0 \cos(\omega_L t)
$$

用欧拉公式展开余弦 $\cos(\omega_L t) = (e^{i\omega_L t} + e^{-i\omega_L t})/2$，每一项贡献的矩阵元为 $-\frac{1}{2}\langle j | \hat{d} \cdot \mathbf{E}_0 | i \rangle$——平方后自然出现因子 $1/4$，这正是光频移公式中 $1/4$ 的来历。

**第 2 步：二阶微扰公式**

标准二阶微扰理论给出能级修正：

$$
\delta E_i = \sum_{j \neq i} \frac{|\langle j | \hat{H}' | i \rangle|^2}{E_i - E_j}
$$

其中 $E_i - E_j$ 是"借来"中间态 $|j\rangle$ 的**能量代价**。但由于光场在快速振荡，中间虚过程必须额外吸收或放出一个光子 $\pm\hbar\omega_L$，能量分母相应修正为 $E_i - E_j \mp \hbar\omega_L$。这里 $\hat{d}$ 是电偶极算符，$\mathbf{E}_0$ 是激光电场振幅，$\omega_{ji} = (E_j - E_i)/\hbar$ 是跃迁频率。

**第 3 步：保留近共振项（旋转波近似）**

对基态 $|g\rangle$ 求和时，主导项来自中间态 $|e\rangle$，其分母为：

$$
E_g - E_e + \hbar\omega_L = \hbar(\omega_L - \omega_0) = \hbar\Delta
$$

（另一项 $E_g - E_e - \hbar\omega_L$ 分母远大于零、贡献可忽略，这就是**旋转波近似（RWA）**）。于是：

$$
\delta E_g = \frac{|\langle e | \hat{d} \cdot \mathbf{E}_0 | g \rangle|^2}{4\hbar \Delta}
$$

**第 4 步：用拉比频率化简**

定义[[Rabi-Flopping|拉比频率]]（与拉比振荡笔记中的定义一致）：

$$
\Omega = \frac{\langle e | \hat{d} \cdot \mathbf{E}_0 | g \rangle}{\hbar}
$$

代入并整理，得到基态光频移的最终形式：

$$
\delta E_g = \frac{\hbar \Omega^2}{4 \Delta}
$$

其中 **失谐** $\Delta = \omega_L - \omega_0$（激光频率减去原子跃迁频率）。

> [!warning] 符号约定
> 不同文献对 $\Delta$ 的符号约定不同！本笔记采用 $\Delta = \omega_L - \omega_0$（激光频率减跃迁频率）。使用公式前务必确认所参考文献的约定。

### 2.2 失谐符号的物理意义

| 失谐类型 | 条件 | 能级移动方向 | 物理效果 |
|---------|------|------------|---------|
| 红失谐（Red detuning） | $\Delta > 0$（$\omega_L > \omega_0$） | $\delta E_g > 0$，基态上推 | 原子被吸引到光强最大处 |
| 蓝失谐（Blue detuning） | $\Delta < 0$（$\omega_L < \omega_0$） | $\delta E_g < 0$，基态下推 | 原子被排斥远离光强最大处 |

> [!tip] 记忆技巧
> "**红推蓝拉**"——红失谐把能级往上推（$\delta E > 0$），原子喜欢待在光强高的地方（势能低）；蓝失谐反之。或者记住：红失谐的光子"能量不够"，试图把原子拉向自己。

> [!example] 数值量级
> 以 Rydberg 激发的典型参数为例：拉比频率 $\Omega = 2\pi \times 10$ MHz、失谐 $\Delta = 2\pi \times 200$ MHz，则基态光频移 $\delta E_g/\hbar = \Omega^2/(4\Delta) \approx 2\pi \times 125$ kHz。做 $R_z(\pi)$ 门需要积累相位 $\varphi = \pi$，即脉冲时长 $t = \pi/(\delta E_g/\hbar) \approx 4\ \mu$s——远短于原子相干时间，因此 AC Stark 门可实现高保真操作。

```python
import numpy as np
import matplotlib.pyplot as plt

# Light shift vs detuning: delta_Eg / (hbar * Omega) = Omega / (4 * Delta)
Omega = 1.0
Delta = np.linspace(-5, 5, 1001)
Delta = Delta[Delta != 0]  # remove divergence at Delta = 0

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(Delta, Omega / (4 * Delta), lw=2, color='#1f77b4')
ax.axhline(0, color='gray', lw=0.8, ls='--')
ax.axvline(0, color='gray', lw=0.8, ls='--')
ax.annotate(r'Red detuning ($\Delta > 0$): level pushed up',
            xy=(2.0, 0.125), xytext=(1.2, 0.55),
            arrowprops=dict(arrowstyle='->', color='#ff7f0e'),
            color='#ff7f0e', fontsize=10)
ax.annotate(r'Blue detuning ($\Delta < 0$): level pushed down',
            xy=(-2.0, -0.125), xytext=(-7.0, -0.55),
            arrowprops=dict(arrowstyle='->', color='#2ca02c'),
            color='#2ca02c', fontsize=10)
ax.set_xlabel(r'Detuning $\Delta / \Omega$')
ax.set_ylabel(r'Light shift $\delta E_g / (\hbar \Omega)$')
ax.set_title('AC Stark Light Shift vs Laser Detuning')
ax.set_xlim(-7, 7)
ax.set_ylim(-0.8, 0.8)
ax.grid(alpha=0.3, ls=':')
plt.tight_layout()
plt.show()
```

> [!note] 图 1 解读
> 曲线在 $\Delta = 0$ 处发散（共振处二阶微扰失效），两侧符号相反：红失谐（$\Delta>0$）频移为正、能级上推，蓝失谐（$\Delta<0$）频移为负、能级下推——与 §2.2 表格完全一致。

---

## 3. Rz 门的物理实现

AC Stark 效应在量子计算中最直接的应用就是实现 **$R_z$ 旋转门**——一种不需要布居数转移（population transfer）的纯相位门。

### 3.1 原理

考虑原子的两个计算基态 $|0\rangle$ 和 $|1\rangle$，它们与某个激发态 $|e\rangle$ 的耦合强度不同（或失谐不同）。当施加一个失谐激光脉冲时：

- $|0\rangle$ 能级获得光频移 $\delta E_0$
- $|1\rangle$ 能级获得光频移 $\delta E_1$
- 两个能级的**差分频移**为 $\delta E = \delta E_1 - \delta E_0$

经过时间 $t$ 的辐照后，量子态积累的**相对相位**为：

$$
\varphi = \frac{\delta E \cdot t}{\hbar} = \frac{(\delta E_1 - \delta E_0)}{\hbar} \cdot t
$$

这正好对应一个 $R_z(\varphi)$ 门（在 Bloch 球上绕 z 轴旋转角度 $\varphi$）。

> [!tip] 关键优势
> $R_z$ 门只改变相对相位，**不改变布居数**（$|0\rangle$ 和 $|1\rangle$ 的概率幅不变）。这意味着门操作过程中原子不会被激发到其他态，从而避免了自发辐射带来的退相干。这是 AC Stark 门保真度高的根本原因。

### 3.2 具体实施方案

在中性原子量子计算中，$R_z$ 门通常通过以下方式实现：

1. 选择一个与跃迁有适当失谐的激光频率
2. 控制激光脉冲的持续时间 $t$ 来精确调节旋转角度 $\varphi$
3. 激光关闭后，相位被"冻结"，门操作完成

详见 [[Single-Qubit-Gates#6. 在中性原子中的物理实现|Single-Qubit-Gates §6 在中性原子中的物理实现]]。

---

## 4. 与 Rabi-Flopping 的关系

AC Stark 效应和 [[Rabi-Flopping]]（拉比振荡）本质上是**同一物理机制的两个极限情况**。

### 4.1 失谐拉比振荡

当驱动场失谐 $\Delta \neq 0$ 时，原子仍然会发生拉比振荡，但频率不再是 $\Omega$，而是**广义拉比频率**：

$$
\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}
$$

同时，布居数转移的振幅被抑制——最大激发概率为：

$$
P_{\max} = \frac{\Omega^2}{\Omega^2 + \Delta^2}
$$

### 4.2 两个极限

| 条件 | 行为 | 对应物理 |
|------|------|---------|
| $\vert\Delta\vert \ll \Omega$ | 接近完全反转，频率 $\approx \Omega$ | 近共振 Rabi flopping |
| $\vert\Delta\vert \gg \Omega$ | 几乎无布居转移，纯相位积累 | **AC Stark 效应** |

> [!tip] 统一图像
> 想象一个摆锤（原子布居）被人推（激光驱动）。共振时（$\Delta = 0$），每次都"推在点上"，摆锤越荡越高（完全反转）。失谐时（$\Delta \gg \Omega$），推力"推不对时机"，摆锤几乎不动，但平衡位置微微偏移了——这就是 AC Stark 频移。

```python
import numpy as np
import matplotlib.pyplot as plt

# Detuned Rabi oscillation: generalized Rabi frequency and max excitation
Omega = 1.0
Delta = np.linspace(0, 6, 400)

Omega_tilde = np.sqrt(Omega**2 + Delta**2)   # generalized Rabi frequency
P_max = Omega**2 / (Omega**2 + Delta**2)     # max excitation probability

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

ax = axes[0]
ax.plot(Delta, Omega_tilde, lw=2, color='#1f77b4',
        label=r'$\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$')
ax.axhline(Omega, color='gray', lw=0.8, ls='--', label=r'$\Omega$ (resonance)')
ax.set_xlabel(r'Detuning $|\Delta| / \Omega$')
ax.set_ylabel(r'Generalized Rabi freq $\tilde{\Omega} / \Omega$')
ax.set_title('(a) Generalized Rabi Frequency')
ax.grid(alpha=0.3, ls=':')
ax.legend(frameon=False, loc='lower right')

ax = axes[1]
ax.plot(Delta, P_max, lw=2, color='#ff7f0e')
ax.axhline(1.0, color='gray', lw=0.8, ls='--', label='full inversion')
ax.set_xlabel(r'Detuning $|\Delta| / \Omega$')
ax.set_ylabel(r'Max excitation probability $P_{\max}$')
ax.set_title('(b) Population Transfer Suppression')
ax.grid(alpha=0.3, ls=':')
ax.legend(frameon=False, loc='upper right')

plt.tight_layout()
plt.show()
```

> [!note] 图 2 解读
> 左图：失谐越大，广义拉比频率 $\tilde{\Omega}$ 越高（振荡"变快"）；右图：但最大激发概率 $P_{\max}$ 被抑制（振荡"翻不满"）。两者合起来正是 AC Stark 极限（$\vert\Delta\vert \gg \Omega$）下"几乎不动、只积累相位"的图像。

---

## 5. 光镊囚禁的物理基础

AC Stark 效应不仅用于量子门，它还是 [[Optical-Tweezer-Arrays]] 的物理基础。

### 5.1 偶极势

光镊的激光在空间中形成非均匀光场。原子感受到的**偶极势**为：

$$
U(\mathbf{r}) = -\frac{1}{2} \alpha(\omega_L) |\mathbf{E}(\mathbf{r})|^2
$$

其中 $\alpha(\omega_L)$ 是原子在激光频率处的**动态极化率**。对于两能级近似：

$$
U(\mathbf{r}) \propto -\frac{\Omega^2(\mathbf{r})}{4\Delta}
$$

这里 $\Omega(\mathbf{r})$ 随位置变化，因为光场强度在空间上不均匀。

### 5.2 囚禁条件

- **红失谐**（$\Delta > 0$）：$U < 0$（势能为负），原子被吸引到光强最大处 → 通过聚焦形成光镊陷阱
- **蓝失谐**（$\Delta < 0$）：$U > 0$（势能为正），原子被排斥到光强最小处 → 需要特殊的暗点陷阱

实际光镊系统几乎都使用红失谐光（如 1064 nm 的 Nd:YAG 激光对 Rb/Na 原子），因为聚焦光束自然在焦点处形成势阱。

```python
import numpy as np
import matplotlib.pyplot as plt

# Gaussian tweezer: Omega(r)^2 ~ exp(-2 r^2 / w0^2), U(r) ~ -Omega(r)^2 / (4 Delta)
r = np.linspace(-3, 3, 500)
w0 = 1.0
Omega2 = np.exp(-2 * r**2 / w0**2)   # normalized Omega(r)^2

Delta_red  = +1.0   # red detuning  -> attractive well
Delta_blue = -1.0   # blue detuning -> repulsive barrier

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(r, -Omega2 / (4 * Delta_red), lw=2, color='#1f77b4',
        label=r'Red detuning ($\Delta>0$): trap at focus')
ax.plot(r, -Omega2 / (4 * Delta_blue), lw=2, color='#d62728',
        label=r'Blue detuning ($\Delta<0$): anti-trap')
ax.axhline(0, color='gray', lw=0.8, ls='--')
ax.set_xlabel(r'Radial position $r / w_0$')
ax.set_ylabel(r'Dipole potential $U / (\hbar \Omega_0^2)$')
ax.set_title('Dipole Potential of a Gaussian Optical Tweezer')
ax.grid(alpha=0.3, ls=':')
ax.legend(frameon=False, loc='lower center')
plt.tight_layout()
plt.show()
```

> [!note] 图 3 解读
> 红失谐在焦点（$r=0$）处形成负势阱（原子被吸引），蓝失谐形成正势垒（原子被排斥到边缘）。这就是为什么光镊几乎总是用红失谐光。

> [!warning] 光镊激光也是噪声源
> 光镊激光虽然用于囚禁原子，但同时也会产生 AC Stark 频移——这会改变量子比特的跃迁频率，降低门保真度。这就是为什么需要 "Magic wavelength"（见下节）。

---

## 6. Magic Wavelength

### 6.1 问题

光镊激光会对 $|0\rangle$ 和 $|1\rangle$ 两个能级施加**不同的** AC Stark 频移：

$$
\delta\omega = \frac{\delta E_1 - \delta E_0}{\hbar}
$$

这个频移会改变量子比特的跃迁频率，导致不同位置（光强不同）的原子有不同的共振频率，从而限制门的保真度。

### 6.2 解决方案

**Magic wavelength** 是一个特殊的激光波长，在该波长下：

$$
\alpha_g(\omega_{\text{magic}}) = \alpha_e(\omega_{\text{magic}})
$$

即基态和激发态的极化率**相等**，两个能级获得**相同的** AC Stark 频移。此时跃迁频率 $|0\rangle \to |1\rangle$ 与光强无关：

$$
\delta\omega = \frac{\delta E_1 - \delta E_0}{\hbar} = 0
$$

> [!info] 为什么叫 "Magic"？
> 这个波长让陷阱深度不影响量子比特频率，看起来像是"魔法"——原子在陷阱中任意位置都能以相同频率共振。实际上它是通过精心选择激光波长使得两个能级的 AC Stark 移动恰好相等来实现的。

Magic wavelength 的选择依赖于原子种类和具体的量子比特编码方案，是中性原子量子计算实验中的一个核心技术参数。

```python
import numpy as np
import matplotlib.pyplot as plt

# Schematic dynamic polarizability vs wavelength for the two qubit levels
lam = np.linspace(700, 1100, 800)   # wavelength in nm (schematic curves)
# Ground level: polarizability slowly decreases with wavelength
alpha_g = 1.6 - 0.6 * (lam - 700) / 400
# Excited level: polarizability slowly increases with wavelength
alpha_e = 0.9 + 0.9 * (lam - 700) / 400

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(lam, alpha_g, lw=2, color='#1f77b4', label=r'Level $\vert 0\rangle$: $\alpha_g(\lambda)$')
ax.plot(lam, alpha_e, lw=2, color='#ff7f0e', label=r'Level $\vert 1\rangle$: $\alpha_e(\lambda)$')

# locate the crossing point (magic wavelength) by sign change
diff = alpha_e - alpha_g
cross_idx = np.where(np.diff(np.sign(diff)) != 0)[0]
if len(cross_idx) > 0:
    idx = cross_idx[0]
    lam_magic = lam[idx]
    ax.axvline(lam_magic, color='#2ca02c', lw=1.5, ls='--')
    ax.plot(lam_magic, alpha_g[idx], 'o', color='#2ca02c', ms=7)
    ax.annotate(r'Magic wavelength $\lambda_{\mathrm{magic}}$',
                xy=(lam_magic, alpha_g[idx]),
                xytext=(lam_magic + 50, alpha_g[idx] + 0.22),
                arrowprops=dict(arrowstyle='->', color='#2ca02c'),
                color='#2ca02c', fontsize=10)

ax.set_xlabel(r'Wavelength $\lambda$ (nm)')
ax.set_ylabel(r'Dynamic polarizability $\alpha(\lambda)$ (a.u.)')
ax.set_title('Magic Wavelength: Equal Polarizability of the Two Qubit Levels')
ax.grid(alpha=0.3, ls=':')
ax.legend(frameon=False, loc='lower right')
plt.tight_layout()
plt.show()
```

> [!note] 图 4 解读
> 两能级极化率曲线相交处即为 magic wavelength：该波长下 $\alpha_g = \alpha_e$，AC Stark 频移相同，跃迁频率 $\delta\omega = 0$，与光镊光强（位置）无关。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|------|------|------|
| $\Delta$ | 激光失谐 | $\Delta = \omega_L - \omega_0$ |
| $\Omega$ | 拉比频率 | $\Omega = \langle e \vert \hat{d} \cdot \mathbf{E}_0 \vert g \rangle / \hbar$ |
| $\delta E_g$ | 基态光频移 | $\delta E_g = \hbar \Omega^2 / (4\Delta)$ |
| $\varphi$ | $R_z$ 旋转相位 | $\varphi = (\delta E_1 - \delta E_0) t / \hbar$ |
| $\delta\omega$ | 跃迁差分频移 | $\delta\omega = (\delta E_1 - \delta E_0) / \hbar$ |
| $\tilde{\Omega}$ | 广义拉比频率 | $\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$ |
| $P_{\max}$ | 最大激发概率 | $P_{\max} = \Omega^2 / (\Omega^2 + \Delta^2)$ |
| $U$ | 偶极势 | $U \propto -\Omega^2 / (4\Delta)$ |

---

## 🔗 相关笔记

- [[Single-Qubit-Gates#6. 在中性原子中的物理实现|Single-Qubit-Gates §6 在中性原子中的物理实现]] — $R_z$ 门通过 AC Stark 效应实现
- [[Rabi-Flopping]] — 共振驱动与失谐驱动的统一图像
- [[Optical-Tweezer-Arrays]] — 光镊囚禁本身就是 AC Stark 效应的应用

## 📝 更新记录

- 2026-03-29: 初始创建（stub），仅包含基本定义
- 2026-06-05: 完整重写。补充物理直觉、二阶微扰推导、$R_z$ 门实现、与 Rabi-Flopping 的联系、光镊囚禁原理、Magic Wavelength 概念，更新状态为 WIP
- 2026-08-02: [doc-audit] 格式审查与增强
  - 补全推导：§2.1 二阶微扰 4 步推导（含 RWA 说明与 $1/4$ 因子来源），首次出现处补链 [[Rabi-Flopping]]
  - 新增 4 个 Python 图表代码块（光频移 vs 失谐、失谐振荡双面板、偶极势、Magic wavelength）
  - 修复表格内 `\|\Delta\|` → `\vert\Delta\vert`（§4.2）
  - 修复 2 处章节链接显示文字 `§6` → `Single-Qubit-Gates §6 在中性原子中的物理实现`
  - 核心公式摘要补 $\delta\omega$ 行；新增数值示例与图解读 callout
