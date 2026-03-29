---
aliases: [CZ Gate, CZ门, Controlled-Z, 控制Z门, 纠缠门]
tags: [Physics, Quantum, Gates, TwoQubit, Entanglement]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
---

# CZ 门（Controlled-Z Gate，纠缠门）

> 来源批注：评价中列出 "纠缠门（CZ门）" — Bluvstein et al., 2026

## 1. 什么是 CZ 门？

CZ 门是一个**两量子比特门**，是中性原子量子计算中最核心的门操作之一。

它的作用是：**当且仅当两个 qubit 都处于 $|1\rangle$ 时，给系统引入一个 $\pi$ 相位**。

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

这是里德堡阻塞最直接的应用之一，也是中性原子量子计算的核心优势。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $\text{CZ}$ | CZ 门矩阵 | $\text{diag}(1,1,1,-1)$ |
| CNOT $\leftrightarrow$ CZ | 门转换 | $\text{CNOT} = (I\otimes H)\cdot\text{CZ}\cdot(I\otimes H)$ |
