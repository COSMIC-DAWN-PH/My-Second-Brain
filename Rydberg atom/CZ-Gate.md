---
aliases: [CZ Gate, CZ门, Controlled-Z, 控制Z门, 纠缠门]
tags: [Physics, Quantum, Gates, TwoQubit, Entanglement]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "vague"
---

# CZ 门（Controlled-Z Gate，纠缠门）

> 来源批注：评价中列出 "纠缠门（CZ门）" — Bluvstein et al., 2026

## 1. 什么是 CZ 门？

CZ 门是一个**两量子比特门**，是中性原子量子计算中最核心的门操作之一。

它的作用是：**当且仅当两个 qubit 都处于 $|1\rangle$ 时，给系统引入一个 $\pi$ 相位**。

> [!tip] CZ vs CNOT
> CZ 门是对称的——两个 qubit 地位平等，没有"控制"和"目标"之分。而 CNOT 门有明确的控制比特和目标比特。在中性原子系统中，CZ 门更自然，因为里德堡阻塞对两个原子是对称的。

## 2. 矩阵表示

在计算基 $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$ 下：

$$
\text{CZ} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}
$$

作用规则：
$$
|00\rangle \to |00\rangle, \quad |01\rangle \to |01\rangle, \quad |10\rangle \to |10\rangle, \quad |11\rangle \to -|11\rangle
$$

## 3. CZ 门制造纠缠

对两个处于叠加态的 qubit 施加 CZ 门，会产生**纠缠态**：

$$
|+\rangle|+\rangle = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)
$$

$$
\xrightarrow{\text{CZ}} \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle - |11\rangle) = |\Phi^+\rangle
$$

这是一个**贝尔态**（maximally entangled state），无法写成两个 qubit 态的乘积。

## 4. CZ 门与 CNOT 门的关系

CZ 门和 CNOT 门可以互相转化（只需在目标 qubit 两侧各加一个 $H$ 门）：

$$
\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)
$$

## 5. 在 Rydberg 体系中的实现

中性原子平台利用 **[[里德堡阻塞 (Rydberg Blockade)]]** 实现 CZ 门：

1. 将控制 qubit 激发到里德堡态 $|r\rangle$
2. 由于里德堡阻塞，若控制 qubit 在 $|r\rangle$，目标 qubit 的 $|1\rangle \to |r\rangle$ 跃迁被**阻塞**，积累一个 $\pi$ 相位
3. 将控制 qubit 退激回来

整个过程实现 $|11\rangle \to -|11\rangle$，即 CZ 门。

> [!warning] pi 脉冲序列的注意事项
> 上述 CZ 门实现依赖精确的 $\pi$ 脉冲和 $2\pi$ 脉冲。如果脉冲面积有偏差（如激光功率波动），会导致 $|11\rangle$ 态未获得准确的 $\pi$ 相位，保真度下降。实验中需要通过拉比振荡标定来校准脉冲面积。

这是里德堡阻塞最直接的应用之一，也是中性原子量子计算的核心优势。

> [!info] 为什么中性原子系统偏好 CZ 而非 CNOT？
> 在中性原子系统中，CZ 门可以直接通过里德堡阻塞一步实现，而 CNOT 需要额外的单比特门（H 门）来转换。由于 CZ 门的物理实现与两个原子的对称性天然匹配——阻塞效应对两个原子是对称的，不分"控制"和"目标"——因此 CZ 是更自然、更高效的选择。中性原子平台的量子线路通常以 CZ 门为基础构建。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $\text{CZ}$ | CZ 门矩阵 | $\text{diag}(1,1,1,-1)$ |
| CNOT $\leftrightarrow$ CZ | 门转换 | $\text{CNOT} = (I\otimes H)\cdot\text{CZ}\cdot(I\otimes H)$ |

---

## 🔗 相关笔记

- [[里德堡阻塞 (Rydberg Blockade)]] — CZ 门的物理实现机制
- [[拉比振荡 (Rabi Flopping)]] — $\pi$ 脉冲的物理基础
- [[单量子比特门 (Single-Qubit Gates)]] — 与 CZ 门组合构成通用门集的单比特门
- [[横向纠缠门 (Transversal Gate)]] — 并行施加 CZ 门的容错方案

## 📝 更新记录

- 2026-03-29: 初始创建
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
