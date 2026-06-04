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

在二阶微扰论框架下，激光场对原子能级 $|i\rangle$ 的修正为：

$$
\delta E_i = \sum_{j \neq i} \frac{|\langle j | \hat{d} \cdot \mathbf{E}_0 | i \rangle|^2}{4(\omega_L - \omega_{ji})}
$$

其中 $\hat{d}$ 是电偶极算符，$\mathbf{E}_0$ 是激光电场振幅，$\omega_{ji} = (E_j - E_i)/\hbar$ 是跃迁频率。

对于简单的两能级系统（基态 $|g\rangle$ 和激发态 $|e\rangle$），定义拉比频率：

$$
\Omega = \frac{\langle e | \hat{d} \cdot \mathbf{E}_0 | g \rangle}{\hbar}
$$

则基态的光频移为：

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

详见 [[Single-Qubit-Gates#6. 在中性原子中的物理实现|§6]]。

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
| $\|\Delta\| \ll \Omega$ | 接近完全反转，频率 $\approx \Omega$ | 近共振 Rabi flopping |
| $\|\Delta\| \gg \Omega$ | 几乎无布居转移，纯相位积累 | **AC Stark 效应** |

> [!tip] 统一图像
> 想象一个摆锤（原子布居）被人推（激光驱动）。共振时（$\Delta = 0$），每次都"推在点上"，摆锤越荡越高（完全反转）。失谐时（$\Delta \gg \Omega$），推力"推不对时机"，摆锤几乎不动，但平衡位置微微偏移了——这就是 AC Stark 频移。

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

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|------|------|------|
| $\Delta$ | 激光失谐 | $\Delta = \omega_L - \omega_0$ |
| $\Omega$ | 拉比频率 | $\Omega = \langle e \vert \hat{d} \cdot \mathbf{E}_0 \vert g \rangle / \hbar$ |
| $\delta E_g$ | 基态光频移 | $\delta E_g = \hbar \Omega^2 / (4\Delta)$ |
| $\varphi$ | $R_z$ 旋转相位 | $\varphi = (\delta E_1 - \delta E_0) t / \hbar$ |
| $\tilde{\Omega}$ | 广义拉比频率 | $\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$ |
| $P_{\max}$ | 最大激发概率 | $P_{\max} = \Omega^2 / (\Omega^2 + \Delta^2)$ |
| $U$ | 偶极势 | $U \propto -\Omega^2 / (4\Delta)$ |

---

## 🔗 相关笔记

- [[Single-Qubit-Gates#6. 在中性原子中的物理实现|§6]] — $R_z$ 门通过 AC Stark 效应实现
- [[Rabi-Flopping]] — 共振驱动与失谐驱动的统一图像
- [[Optical-Tweezer-Arrays]] — 光镊囚禁本身就是 AC Stark 效应的应用

## 📝 更新记录

- 2026-03-29: 初始创建（stub），仅包含基本定义
- 2026-06-05: 完整重写。补充物理直觉、二阶微扰推导、$R_z$ 门实现、与 Rabi-Flopping 的联系、光镊囚禁原理、Magic Wavelength 概念，更新状态为 WIP
