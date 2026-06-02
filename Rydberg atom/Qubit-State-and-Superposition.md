---
aliases:
  - Qubit State
  - 量子比特态
  - 叠加态
  - Superposition
  - 相位因子
  - Complex Amplitude
tags:
  - Physics
  - Quantum
  - Qubit
  - Superposition
  - Fundamental
date: 2026-06-02
status: In-Progress
source: "[[generall quantum 2026]]"
comprehension: "getting there"
---

# 量子比特态与叠加态（Qubit State and Superposition）

> 来源批注：量子计算与量子力学基础概念
> 本笔记专门回答一个核心问题：**叠加态到底是什么意思？$\alpha|0\rangle + \beta|1\rangle$ 前面的复数系数（特别是相位因子）在物理上到底意味着什么？**

---

## 1. 从一个具体问题说起

### 1.1 你可能有的困惑

当你第一次看到叠加态的写法时，很可能会有这样的疑问：

> $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$
>
> 这里的 $\alpha$ 和 $\beta$ 为什么必须是**复数**？如果只是"同时处于 0 和 1"，用两个实数概率不就行了？前面乘一个 $e^{i\phi}$ 相位因子有什么意义？它又测不到。

这个困惑非常合理。下面我会从物理出发，一步一步把这个相位因子的意义说清楚。

### 1.2 用你熟悉的东西：自旋

你已经学过自旋（[[Pauli-Matrices|Pauli 矩阵]]）。回忆一下：

$$
|{\uparrow}\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \quad |{\downarrow}\rangle = \begin{pmatrix}0\\1\end{pmatrix}
$$

一个自旋-1/2 粒子可以处于 $|{\uparrow}\rangle$ 和 $|{\downarrow}\rangle$ 的叠加态：

$$
|\psi\rangle = \alpha|{\uparrow}\rangle + \beta|{\downarrow}\rangle
$$

在 Stern-Gerlach 实验中，沿 $z$ 方向测量这个粒子：
- 得到"自旋向上"的概率是 $|\alpha|^2$
- 得到"自旋向下"的概率是 $|\beta|^2$

**关键事实**：概率只取决于 $|\alpha|^2$ 和 $|\beta|^2$——即振幅的**模方**。$\alpha$ 和 $\beta$ 本身的"辐角"（相位）不影响单次测量的概率分布。

那相位有什么用？答案是：**相位决定了不同叠加态之间如何"干涉"**——这是量子力学最核心的效应。

---

## 2. 叠加态到底是什么？

### 2.1 "同时处于 0 和 1"——不完全对

很多教材说"叠加态就是同时处于 0 和 1"。这个说法**不够准确**，容易产生误解。

更准确的说法是：

> 叠加态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ 描述的是一个量子系统在**测量之前**的状态。在这个状态下，系统没有确定的值（0 或 1），但它有一个**概率振幅**——测量时得到 0 的振幅是 $\alpha$，得到 1 的振幅是 $\beta$。

"概率振幅"和"概率"的区别是量子力学最深刻的发现：

| 概念 | 数学形式 | 可以直接测量？ |
|------|---------|------------|
| 概率振幅 | $\alpha$（复数） | **不能** |
| 概率 | $\|\alpha\|^2$（实数，≥ 0） | **能**（频率） |

### 2.2 为什么用复数而不是实数？

**如果只用实数振幅**（$\alpha, \beta \in \mathbb{R}$），量子力学就缺少了干涉效应。具体来说：

- 实数振幅只能产生"相长干涉"或"相消干涉"（同号相长，异号相消）
- 复数振幅可以产生**任意角度**的干涉（因为复数有 360° 的相位角）

> [!tip] 物理直觉：两束水波
> 想象两束水波叠加。如果两束波同相（都向上），它们叠加后变强（相长干涉）。如果反相（一上一下），它们抵消（相消干涉）。但如果两束波相差 90° 呢？它们不会完全抵消，也不会完全加强——而是以一种**特定的角度**叠加。复数相位就是用来描述这种"任意角度叠加"的数学工具。

实际上，量子力学的公理要求态矢量生活在**复希尔伯特空间**中，这不是人为选择，而是**实验事实的数学必然**——Young 双缝实验中的干涉图样无法用实数振幅解释。

---

## 3. 相位因子到底在说什么？

### 3.1 全局相位 vs 相对相位

对 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ 做一个整体的相位变换：

$$
|\psi'\rangle = e^{i\varphi}|\psi\rangle = e^{i\varphi}\alpha|0\rangle + e^{i\varphi}\beta|1\rangle
$$

测量概率：$|e^{i\varphi}\alpha|^2 = |\alpha|^2$，$|e^{i\varphi}\beta|^2 = |\beta|^2$。

**完全一样**。所以 $e^{i\varphi}$ 这个"全局相位"在物理上**不可观测**——你可以随意选择整体相位而不改变任何测量结果。

但如果你**只改变其中一个分量的相位**：

$$
|\psi'\rangle = \alpha|0\rangle + e^{i\phi}\beta|1\rangle
$$

这叫做**相对相位**。它**可以**通过干涉实验观测到。

### 3.2 一个具体的例子：$|+\rangle$ vs $|{-i}\rangle$

考虑两个叠加态：

$$
|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \quad (\text{相对相位} = 0)
$$

$$
|{-i}\rangle = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle) \quad (\text{相对相位} = -\pi/2)
$$

### 什么是"测量基"？

**测量基**就是"你选择沿着哪个方向去测量"。回忆 Stern-Gerlach 实验：同一个自旋态，沿不同方向放磁铁，得到的结果可以完全不同。

在 Bloch 球的语言中，有三种基本测量基：

**$z$ 基测量**——问"是 $|0\rangle$ 还是 $|1\rangle$？"

这是最常见的测量方式。探测器只识别两个超精细基态，沿 $z$ 轴（Bloch 球南北极方向）测量。对叠加态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$：

- 得到 0 的概率是 $|\alpha|^2$
- 得到 1 的概率是 $|\beta|^2$

**$x$ 基测量**——问"是 $|+\rangle$ 还是 $|-\rangle$？"

沿 $x$ 轴（Bloch 球赤道上 $x$ 方向）测量。实验中**无法直接做 $x$ 基测量**，需要先做一个 H 门把信息"旋转"到 $z$ 轴上，再做 $z$ 基测量：

$$
x \text{ 基测量} = H \text{ 门} + z \text{ 基测量}
$$

**$y$ 基测量**——问"是 $|{+i}\rangle$ 还是 $|{-i}\rangle$？"

沿 $y$ 轴（Bloch 球赤道上 $y$ 方向）测量。实验中需要先做一个 $S^\dagger H$ 旋转，再做 $z$ 基测量：

$$
y \text{ 基测量} = S^\dagger H \text{ 门} + z \text{ 基测量}
$$

> [!tip] 统一规则
> 所有物理测量**本质上都是 $z$ 基测量**（探测器只认 $|0\rangle$ 和 $|1\rangle$）。要实现其他基的测量，需要先用量子门把目标信息"旋转"到 $z$ 轴上，再做 $z$ 基测量。这就是量子门在算法中的核心作用之一——**把需要的信息转换到测量基上**。

### 测量基 = Pauli 算符的本征态

测量基不是随便选的"方向"——它有严格的数学定义：**每种测量基对应一个 Pauli 算符的本征态**。

回忆量子力学的测量理论：测量一个可观测量 $\hat{A}$ 时，结果**只能是** $\hat{A}$ 的本征值，测量后系统坍缩到对应的**本征态**。

三个 Pauli 算符各有自己的本征方程和本征态：

**$Z$ 算符**的本征态：

$$
Z|0\rangle = +1 \cdot |0\rangle \quad \Rightarrow \quad |0\rangle \text{ 是本征值 } +1 \text{ 的本征态}
$$

$$
Z|1\rangle = -1 \cdot |1\rangle \quad \Rightarrow \quad |1\rangle \text{ 是本征值 } -1 \text{ 的本征态}
$$

**$X$ 算符**的本征态：

$$
X|+\rangle = +1 \cdot |+\rangle \quad \Rightarrow \quad |+\rangle \text{ 是本征值 } +1 \text{ 的本征态}
$$

$$
X|-\rangle = -1 \cdot |-\rangle \quad \Rightarrow \quad |-\rangle \text{ 是本征值 } -1 \text{ 的本征态}
$$

**$Y$ 算符**的本征态：

$$
Y|{+i}\rangle = +1 \cdot |{+i}\rangle \quad \Rightarrow \quad |{+i}\rangle \text{ 是本征值 } +1 \text{ 的本征态}
$$

$$
Y|{-i}\rangle = -1 \cdot |{-i}\rangle \quad \Rightarrow \quad |{-i}\rangle \text{ 是本征值 } -1 \text{ 的本征态}
$$

所以量子计算的三种"测量基"就是量子力学中三个 Pauli 算符的本征态组：

- $z$ 基测量 = 测量 $Z$ 算符 → 结果是 $+1$（对应 $|0\rangle$）或 $-1$（对应 $|1\rangle$）
- $x$ 基测量 = 测量 $X$ 算符 → 结果是 $+1$（对应 $|+\rangle$）或 $-1$（对应 $|-\rangle$）
- $y$ 基测量 = 测量 $Y$ 算符 → 结果是 $+1$（对应 $|{+i}\rangle$）或 $-1$（对应 $|{-i}\rangle$）

> [!warning] "确定"与"不确定"取决于你测什么
> 一个态是否给出确定的测量结果，**取决于你测量什么算符**：
> - $|+\rangle$ 对 $X$ 测量是**确定的**（$X|+\rangle = +|+\rangle$，100% 得 $+1$）
> - 但 $|+\rangle$ 对 $Z$ 测量是**不确定的**（$|+\rangle$ 不是 $Z$ 的本征态，50-50 得 $+1$ 或 $-1$）
>
> 这就是为什么"测量基"这么重要——同一个态在不同算符的测量下，行为完全不同。

### 两个叠加态在不同基下的测量结果

**$z$ 基测量**（直接问"0 还是 1？"）：

对 $|+\rangle$：$P(0) = |1/\sqrt{2}|^2 = 50\%$，$P(1) = |1/\sqrt{2}|^2 = 50\%$

对 $|{-i}\rangle$：$P(0) = |1/\sqrt{2}|^2 = 50\%$，$P(1) = |-i/\sqrt{2}|^2 = 50\%$

**完全一样**——$z$ 基测量"看不到"相位差异，因为 Born 规则只取模方 $|\beta|^2$，而 $|1|^2 = |-i|^2 = 1$。

**$x$ 基测量**（先做 H 门，再 $z$ 基测量）：

对 $|+\rangle$：

$$
H|+\rangle = |0\rangle \quad \Rightarrow \quad \text{100\% 得到 0}
$$

对 $|{-i}\rangle$：

$$
H|{-i}\rangle = \frac{1-i}{2}|0\rangle + \frac{1+i}{2}|1\rangle \quad \Rightarrow \quad \text{50\% 得到 0，50\% 得到 1}
$$

**结果不同！** $x$ 基测量不能在单次实验中完美区分这两个态，但它们给出的统计分布不同：$|+\rangle$ 总是落到 $x$ 轴正方向，而 $|{-i}\rangle$ 在 $x$ 基下是 50-50。

> [!warning] 关键点
> **相对相位不影响固定 $z$ 基下的 $|0\rangle/|1\rangle$ 概率分布，但它决定了换到 $x/y$ 等其他测量基后得到什么统计结果**。这就是为什么量子门（如 H 门、Z 门）需要精确控制相位——相位差异在后续操作中会被"放大"成可观测的概率差异。

### 3.3 为什么 $\alpha$ 和 $\beta$ 都需要是复数？

假设只有 $\beta$ 有相位，$\alpha$ 是实数：

$$
|\psi\rangle = \alpha|0\rangle + \beta e^{i\phi}|1\rangle
$$

但因为全局相位不可观测，我们可以把 $e^{i\phi}$ "提出来"变成整体相位。所以其实只需要**一个**复数相位就够了。

更一般的写法是：

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle
$$

这里 $\theta$ 和 $\phi$ 两个实参数就完全确定了一个 qubit 态（在 Bloch 球面上的位置）。$\theta$ 控制"0 和 1 的混合比例"，$\phi$ 控制"相对相位"。

---

## 4. 四个最重要的叠加态

用 Bloch 球的参数化 $(\theta, \phi)$ 来看：

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle
$$

### 4.1 $|0\rangle$ 和 $|1\rangle$：确定态

- $|0\rangle$：$\theta = 0$（北极），沿 $z$ 轴测量必定得到 0
- $|1\rangle$：$\theta = \pi$（南极），沿 $z$ 轴测量必定得到 1

这是**经典比特的量子版本**——确定态就是没有叠加。

### 4.2 $|+\rangle$ 和 $|-\rangle$：$x$ 轴基态

- $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$：沿 $x$ 轴测量必定得到 $+$
- $|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$：沿 $x$ 轴测量必定得到 $-$

注意 $|+\rangle$ 和 $|-\rangle$ 的**唯一区别是相对相位的符号**（$+1$ vs $-1$）。这个微小的差异使得它们在 $x$ 轴测量时给出完全确定的（但不同的）结果。

### 4.3 $|{+i}\rangle$ 和 $|{-i}\rangle$：$y$ 轴基态

- $|{+i}\rangle = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$：沿 $y$ 轴测量必定得到 $+i$
- $|{-i}\rangle = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$：沿 $y$ 轴测量必定得到 $-i$

这里的 $i$ 就是相对相位因子——正是这个 $i$（而不是 $+1$ 或 $-1$）使得测量沿 $y$ 轴而非 $x$ 轴时给出确定结果。

### 4.4 小结

> [!tip] 统一视角
> 这里要分清两类态：
> - $|0\rangle$ 和 $|1\rangle$ 是 $z$ 轴本征态，沿 $z$ 轴测量分别是 **100% 得 0** 和 **100% 得 1**，不是 50-50。
> - $|+\rangle, |-\rangle, |{+i}\rangle, |{-i}\rangle$ 都在 Bloch 球赤道上，所以沿 $z$ 轴测量才都是 **50-50**。
>
> 因此，真正正确的说法是：这六个态是三个 Pauli 轴的本征态——$z$ 轴对应 $|0\rangle, |1\rangle$，$x$ 轴对应 $|+\rangle, |-\rangle$，$y$ 轴对应 $|{+i}\rangle, |{-i}\rangle$。每一对态都在自己的测量轴上给出确定结果；而赤道上的四个态虽然在 $z$ 轴上概率分布相同，但相位结构不同，会在 $x/y$ 基测量中表现出差异。
>
> **相位就是量子信息的“方向信息”**：当 $|0\rangle$ 与 $|1\rangle$ 的权重相同、都处在赤道上时，不同的相对相位对应 Bloch 球赤道上的不同方向。

---

## 5. Bloch 球：相位的几何语言

### 5.1 参数化

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle
$$

- $\theta \in [0, \pi]$：极角（决定 $|0\rangle$ 和 $|1\rangle$ 的混合比例）
- $\phi \in [0, 2\pi)$：方位角（决定相对相位）

### 5.2 $\theta$ 和 $\phi$ 的物理含义

**$\theta$ 控制概率分布**：

- $\theta = 0$ → $|0\rangle$（北极）：100% 得 0
- $\theta = \pi/2$ → 赤道上：50-50 分布
- $\theta = \pi$ → $|1\rangle$（南极）：100% 得 1

**$\phi$ 控制相位结构**（不影响 $z$ 轴测量，但影响其他方向的测量）：

- $\phi = 0$ → $|+\rangle$（赤道上 $x$ 轴正方向）
- $\phi = \pi/2$ → $|{+i}\rangle$（赤道上 $y$ 轴正方向）
- $\phi = \pi$ → $|-\rangle$（赤道上 $x$ 轴负方向）
- $\phi = 3\pi/2$ → $|{-i}\rangle$（赤道上 $y$ 轴负方向）

> [!question] 思考题
> 在 Bloch 球赤道上走一圈（$\theta = \pi/2$，$\phi$ 从 0 变到 $2\pi$），对应的是什么物理操作？为什么 $\phi$ 走一圈后量子态"回到原点"（$|\psi\rangle$ 和 $e^{i\phi}|\psi\rangle$ 物理等价）？

---

## 6. 测量与坍缩

### 6.1 测量的基本规则

对处于 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ 的 qubit 做 $z$ 基测量：

1. 得到 **0** 的概率是 $|\alpha|^2$
2. 得到 **1** 的概率是 $|\beta|^2$
3. 测量后，系统的状态**坍缩**到测量结果对应的态（0 或 1）

### 6.2 测量会"毁灭"叠加态

一旦测量完成，叠加态就消失了——系统变成了一个确定态（0 或 1）。你不能通过一次测量"偷看" $\alpha$ 和 $\beta$ 的具体值，只能通过**统计大量重复实验**来推断概率。

> [!warning] 测量不是"发现隐藏的值"
> 经典世界中，硬币在空中翻转时已经有一个确定的结果（只是你不知道）。量子世界中，qubit 在测量前**真的没有确定的值**——测量不是"发现"预先存在的结果，而是**参与创造**结果。这是量子力学和经典统计力学最根本的区别。

### 6.3 相位在测量中的角色

单独做 $z$ 基测量**看不到相位**。要看到相位，需要：

1. 先做一个单比特门（如 H 门），把相位信息"翻译"成概率信息
2. 再做 $z$ 基测量

这就是量子算法的核心策略：**用门操作把需要的信息转换到测量基上，然后通过测量提取出来**。

---

## 7. 在 Rydberg 原子中的具体体现

### 7.1 量子比特的编码

在 [[Optical-Tweezer-Arrays]] 中，一个中性原子（如 $^{87}\text{Rb}$）的两个超精细基态编码 qubit：

$$
|0\rangle \equiv |F=1, m_F=0\rangle, \quad |1\rangle \equiv |F=2, m_F=0\rangle
$$

这两个态之间的超精细分裂约为 6.8 GHz，对应微波频率。

### 7.2 叠加态的制备

从 $|0\rangle$ 出发，施加一个 $\pi/2$ 微波脉冲（即 [[Rabi-Flopping|拉比振荡]] 的 $\pi/2$ 脉冲），就制备出叠加态：

$$
|0\rangle \xrightarrow{\pi/2\text{ 脉冲}} \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)
$$

这个叠加态的**相对相位是 $-i = e^{-i\pi/2}$**——不是 $+1$（$|+\rangle$）也不是 $-1$（$|-\rangle$），而是 $-i$。这是由微波脉冲的**偏振和相位**决定的。

### 7.3 相位操控的实际意义

在 [[Single-Qubit-Gates|单比特门]] 中：

- **$R_x(\theta)$** 旋转：改变 $\theta$（混合比例），**不改变 $\phi$**（相位）
- **$R_z(\theta)$ 旋转**：改变 $\phi$（相位），**不改变 $\theta$**（混合比例）
- **H 门**：把 $\theta$ 和 $\phi$ 都改变——将 $z$ 轴信息"旋转"到 $x$ 轴

> [!info] 为什么 $R_z$ 门这么重要？
> $R_z$ 门（相位旋转）在实验中通过 **AC Stark 效应**实现——用失谐激光给 $|1\rangle$ 态一个额外的相移。虽然它不改变 $z$ 基测量的概率分布，但它改变了态的**干涉能力**。在 Grover 搜索、量子相位估计等算法中，$R_z$ 门的精确控制是成功的关键。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|------|------|------|
| $|\psi\rangle$ | 一般 qubit 态 | $\alpha\|0\rangle + \beta\|1\rangle$，$\|\alpha\|^2 + \|\beta\|^2 = 1$ |
| Bloch 参数化 | 几何表示 | $\cos\frac{\theta}{2}\|0\rangle + e^{i\phi}\sin\frac{\theta}{2}\|1\rangle$ |
| $\theta$ | 极角（混合比例） | $\theta = 0 \to \|0\rangle$，$\theta = \pi \to \|1\rangle$ |
| $\phi$ | 方位角（相对相位） | $\phi = 0 \to \|+\rangle$，$\phi = \pi/2 \to \|{+i}\rangle$ |
| 全局相位 | 物理不可观测 | $e^{i\varphi}\|\psi\rangle \equiv \|\psi\rangle$ |
| 相对相位 | 物理可观测（通过干涉） | 不同 $\phi$ 在不同测量基下给出不同结果 |
| 测量概率 | Born 规则 | $P(0) = \|\alpha\|^2$，$P(1) = \|\beta\|^2$ |

---

## 🔗 相关笔记

- [[Two-Qubit-State-and-Entanglement]] — 两个 qubit 的叠加态如何产生纠缠、并发度、纠缠熵
- [[Single-Qubit-Gates]] — 对叠加态施加的旋转操作（H、X、Z、T 等）
- [[Pauli-Matrices]] — Bloch 球三个轴的旋转生成元
- [[Rabi-Flopping]] — 实验中制备叠加态的物理机制
- [[Gate-Eigenstates]] — Pauli 门的本征态（六种特殊叠加态）
- [[Optical-Tweezer-Arrays]] — 叠加态的硬件平台
- [[Two-Qubit-Gates]] — 两个 qubit 的叠加态如何产生纠缠

## 📝 更新记录

- 2026-06-02: 初始创建，系统讲解叠加态、相位因子、Bloch 球、测量坍缩、Rydberg 原子实现
- 2026-06-02: 修正六个 Pauli 本征态的测量概率表述：$|0\rangle, |1\rangle$ 沿 $z$ 轴不是 50-50，只有赤道态沿 $z$ 轴为 50-50。
