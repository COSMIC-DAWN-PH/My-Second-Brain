---
aliases:
  - 塞曼效应
  - Zeeman Effect
  - Zeeman effect
  - 塞曼分裂
tags:
  - Physics
  - Atomic
  - Quantum
date: 2026-06-05
status: WIP
source: "[[start_up]]"
comprehension: "vague"
---

# 塞曼效应（Zeeman Effect）

> 来源：原子物理基础 / 中性原子量子计算比特编码
> 本笔记介绍塞曼效应的物理机制及其在中性原子量子计算中的核心意义——$m_F = 0$ 的 clock state 为何能实现长相干时间。

---

## 1. 物理直觉：磁场打破对称性

在没有外磁场时，原子的能级具有**旋转对称性**——空间中所有方向等价，因此磁量子数 $m$ 不同的态具有相同的能量（简并）。

当施加外磁场 $\mathbf{B}$ 后，这个对称性被打破了。磁场定义了一个**特殊方向**（取为 $z$ 轴），不同 $m$ 值的态沿着这个方向"感受"到不同的能量——**简并被解除，能级发生分裂**。

> [!tip] 物理直觉
> 塞曼效应就像陀螺在地球磁场中的进动——不同取向的陀螺（不同 $m$）与磁场的耦合能量不同，因此能量不再相同。原本"平躺"的能级扇面被磁场"掰开"了。

---

## 2. 塞曼哈密顿量

### 2.1 磁矩与磁场的耦合

原子的总磁矩 $\boldsymbol{\mu}$ 与外磁场 $\mathbf{B}$ 的相互作用能为：

$$
H_Z = -\boldsymbol{\mu} \cdot \mathbf{B}
$$

对于总角动量 $\mathbf{J} = \mathbf{L} + \mathbf{S}$，磁矩为：

$$
\boldsymbol{\mu} = -\frac{\mu_B}{\hbar}(g_L \mathbf{L} + g_S \mathbf{S})
$$

其中 $\mu_B = e\hbar / 2m_e$ 是玻尔磁子，$g_L \approx 1$，$g_S \approx 2$。

取 $\mathbf{B} = B\hat{z}$，塞曼哈密顿量为：

$$
H_Z = \frac{\mu_B B}{\hbar}(g_L L_z + g_S S_z)
$$

---

## 3. 弱磁场：反常塞曼效应（Anomalous Zeeman Effect）

### 3.1 Lande g 因子

在弱磁场下（$H_Z \ll H_{\text{SO}}$），自旋-轨道耦合仍然占主导，$\mathbf{J} = \mathbf{L} + \mathbf{S}$ 是好量子数。此时能量修正只需对 $\vert j, m_j\rangle$ 态取期望值：

$$
\Delta E = g_j \, \mu_B \, m_j \, B
$$

其中 **Landé g 因子**为：

$$
g_j = 1 + \frac{j(j+1) - l(l+1) + s(s+1)}{2j(j+1)}
$$

> [!info] Landé g 因子的物理含义
> $g_j$ 度量的是"总角动量 $\mathbf{J}$ 方向上，磁矩的有效投影"。它介于纯轨道（$g_L = 1$）和纯自旋（$g_S = 2$）之间，具体取值取决于 $\mathbf{L}$ 和 $\mathbf{S}$ 的相对贡献。

### 3.2 分裂特征

- 每个能级分裂为 $2j+1$ 个子能级
- 相邻子能级间距 $\Delta E = g_j \mu_B B$（等间距）
- $g_j \neq 1$ 时，不同能级的分裂间距不同——这就是"反常"塞曼效应（历史上称为反常，实际上是 $g_j \neq 1$ 的结果）

---

## 4. 强磁场：Paschen-Back 效应

当外磁场远强于自旋-轨道耦合（$\mu_B B \gg \lambda_{\text{SO}}$）时，$\mathbf{L}$ 和 $\mathbf{S}$ 分别绕 $\mathbf{B}$ 进动，$\mathbf{J}$ 不再是好量子数。此时 $m_l$ 和 $m_s$ 成为好量子数：

$$
\Delta E = \mu_B B (m_l + 2m_s)
$$

> [!warning] 弱场 vs 强场
> - **弱场**（$H_Z \ll H_{\text{SO}}$）：$j, m_j$ 是好量子数 → 反常塞曼效应
> - **强场**（$H_Z \gg H_{\text{SO}}$）：$l, m_l, s, m_s$ 是好量子数 → 正常塞曼效应（Paschen-Back）
> - 中间区域需要数值对角化

---

## 5. QC 核心：超精细态的塞曼效应与 Clock States

### 5.1 超精细态的塞曼分裂

在中性原子量子计算中，真正的量子比特编码在**超精细能级**（hyperfine levels）上。考虑超精细量子数 $F$（$\mathbf{F} = \mathbf{J} + \mathbf{I}$），塞曼效应为：

$$
\Delta E = g_F \, \mu_B \, m_F \, B
$$

其中 **超精细 Landé g 因子**为：

$$
g_F = g_J \cdot \frac{F(F+1) + J(J+1) - I(I+1)}{2F(F+1)}
$$

> [!info] 对于 $J = 1/2$ 的基态
> 当 $J = 1/2$ 时，上式可以简化为：
> $g_F = \pm \frac{1}{2I+1}$（正负号取决于 $F = I \pm 1/2$）

### 5.2 Rb-87 的具体数值

对于 $^{87}\text{Rb}$（核自旋 $I = 3/2$，基态 $5S_{1/2}$，$J = 1/2$）：

| 超精细态 | $F$ | $g_F$ | 备注 |
|---------|-----|-------|------|
| $F = 1$ | 1 | $\approx -1/2$ | 低能超精细态 |
| $F = 2$ | 2 | $\approx +1/2$ | 高能超精细态 |

### 5.3 $m_F = 0$：Clock State 的秘密

> [!tip] 这是整篇笔记的核心
> 当 $m_F = 0$ 时，塞曼能量偏移为：
> $$\Delta E = g_F \cdot \mu_B \cdot 0 \cdot B = 0$$
> **一阶塞曼偏移为零！**

这意味着 $m_F = 0$ 的态对磁场的一阶扰动完全不敏感。在中性原子量子计算中，$m_F = 0$ 的态被称为 **clock state**（钟态），正是因为它们的跃迁频率几乎不受磁场波动影响。

**因果链**：

$$
m_F = 0 \;\Rightarrow\; \text{一阶塞曼偏移} = 0 \;\Rightarrow\; 对磁场噪声不敏感 \;\Rightarrow\; \text{长相干时间} \;\Rightarrow\; \text{好的量子比特}
$$

> [!warning] 二阶效应仍然存在
> 虽然一阶偏移为零，但 $m_F = 0$ 态仍有**二阶塞曼偏移**（来自与相邻 $m_F = \pm 1$ 态的微扰混合）：
> $$\Delta E^{(2)} \propto \frac{(\mu_B B)^2}{\Delta E_{\text{hfs}}}$$
> 但这个效应远小于一阶效应，因此 clock state 仍然对磁场高度不敏感。

### 5.4 量子比特编码选择

在 $^{87}\text{Rb}$ 中性原子量子计算机中：

| 量子比特态 | 超精细态 | 磁敏感性 | 相干时间 |
|-----------|---------|---------|---------|
| $\vert 0\rangle$ | $\vert F=1, m_F=0\rangle$ | 一阶不敏感 | 长（$\sim$ 秒级） |
| $\vert 1\rangle$ | $\vert F=2, m_F=0\rangle$ | 一阶不敏感 | 长（$\sim$ 秒级） |

跃迁频率 $\nu_0 \approx 6.834\,\text{GHz}$（$^{87}\text{Rb}$ 超精细分裂），对磁场一阶不敏感。

> [!example] 对比：非 clock state
> 如果选择 $m_F \neq 0$ 的态作为量子比特（例如 $\vert F=1, m_F=-1\rangle$ 和 $\vert F=2, m_F=-1\rangle$），则一阶塞曼偏移 $\Delta E = g_F \mu_B m_F B \neq 0$，磁场波动会直接转化为相位噪声，相干时间大大缩短。

---

## 6. 塞曼效应的 QC 视角总结

| 物理量 | 公式 | QC 意义 |
|-------|------|--------|
| 塞曼哈密顿量 | $H_Z = -\boldsymbol{\mu} \cdot \mathbf{B}$ | 磁场与原子磁矩的耦合 |
| Landé g 因子 | $g_j = 1 + \frac{j(j+1) - l(l+1) + s(s+1)}{2j(j+1)}$ | 有效磁矩的缩放因子 |
| 超精细 g 因子 | $g_F = g_J \cdot \frac{F(F+1) + J(J+1) - I(I+1)}{2F(F+1)}$ | 决定超精细态对磁场的敏感度 |
| 一阶偏移 | $\Delta E = g_F \mu_B m_F B$ | $m_F = 0$ 时为零 → clock state |
| 二阶偏移 | $\Delta E^{(2)} \propto (\mu_B B)^2 / \Delta E_{\text{hfs}}$ | 残余磁场敏感性，但很小 |
| Rb-87 $g_F$ | $g_{F=1} \approx -1/2$，$g_{F=2} \approx +1/2$ | 两个超精细态的 g 因子大小相近、符号相反 |

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|------|------|------|
| $H_Z$ | 塞曼哈密顿量 | $H_Z = \frac{\mu_B B}{\hbar}(g_L L_z + g_S S_z)$ |
| $g_j$ | Landé g 因子 | $g_j = 1 + \frac{j(j+1) - l(l+1) + s(s+1)}{2j(j+1)}$ |
| $g_F$ | 超精细 g 因子 | $g_F = g_J \cdot \frac{F(F+1) + J(J+1) - I(I+1)}{2F(F+1)}$ |
| $\Delta E_{\text{weak}}$ | 弱场偏移 | $\Delta E = g_j \mu_B m_j B$ |
| $\Delta E_{\text{strong}}$ | 强场偏移（Paschen-Back） | $\Delta E = \mu_B B(m_l + 2m_s)$ |
| $\Delta E_{\text{hfs}}$ | 超精细态塞曼偏移 | $\Delta E = g_F \mu_B m_F B$ |
| $\mu_B$ | 玻尔磁子 | $\mu_B = e\hbar / 2m_e \approx 9.274 \times 10^{-24}\,\text{J/T}$ |

---

## 🔗 相关笔记

- [[Hyperfine-Structure]] — 超精细结构是塞曼效应在 QC 中应用的直接前置知识
- [[Fine-Structure]] — 自旋-轨道耦合决定了弱场下 $\mathbf{J}$ 的好量子数地位
- [[start_up#2. 利用表象理论定义量子比特]] — 量子比特编码的物理基础，clock state 的选择依据
- [[Single-Qubit-Gates]] — 单比特门操作依赖于定义良好的量子比特态
- [[Rabi-Flopping]] — 驱动 clock state 之间跃迁的微波脉冲

## 📝 更新记录

- 2026-06-05: 初始创建，涵盖弱场/强场塞曼效应、Landé g 因子、超精细态塞曼效应、$m_F=0$ clock state 的 QC 意义

^260605