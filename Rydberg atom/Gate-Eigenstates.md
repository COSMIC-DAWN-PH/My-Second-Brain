---
aliases: [Gate Eigenstates, 门算符本征态, 本征态, Eigenstate]
tags: [Physics, Quantum, Mathematics, Gates, LinearAlgebra]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "vague"
---

# 门算符本征态（Gate Operator Eigenstates）

> 来源批注：评价中列出 "门算符本征态" — Bluvstein et al., 2026

## 1. 本征方程回顾

对于算符（矩阵）$\hat{A}$，**本征态** $|\lambda\rangle$ 满足：

$$
\hat{A}|\lambda\rangle = \lambda|\lambda\rangle
$$

其中 $\lambda$ 是对应的**本征值**。

物理含义：若系统处于本征态，对 $\hat{A}$ 的测量结果**确定**为 $\lambda$（无态坍缩的随机性）。

> [!tip] 本征态的直观理解
> 本征态就是"被算符作用后除了一个相位因子外保持不变"的状态。比如 $Z|0\rangle = +1 \cdot |0\rangle$，系统完全没有变化；$Z|1\rangle = -1 \cdot |1\rangle$，只多了一个全局相位（物理上不可观测）。

## 2. Pauli 门的本征态

量子门通常是 Pauli 矩阵的组合。以下是三个 Pauli 门的本征态：

### $Z$ 门（$\sigma_z$）
$$
Z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$

| 本征值 | 本征态 |
|---|---|
| $+1$ | $|0\rangle = \begin{pmatrix}1\\0\end{pmatrix}$ |
| $-1$ | $|1\rangle = \begin{pmatrix}0\\1\end{pmatrix}$ |

### $X$ 门（$\sigma_x$）
$$
X = \begin{pmatrix}0&1\\1&0\end{pmatrix}
$$

| 本征值 | 本征态 |
|---|---|
| $+1$ | $|+\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{|0\rangle+|1\rangle}{\sqrt{2}}$ |
| $-1$ | $|-\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix} = \frac{|0\rangle-|1\rangle}{\sqrt{2}}$ |

### $Y$ 门（$\sigma_y$）
$$
Y = \begin{pmatrix}0&-i\\i&0\end{pmatrix}
$$

| 本征值 | 本征态 |
|---|---|
| $+1$ | $|i\rangle = \frac{|0\rangle+i|1\rangle}{\sqrt{2}}$ |
| $-1$ | $|-i\rangle = \frac{|0\rangle-i|1\rangle}{\sqrt{2}}$ |

> [!warning] X 本征态 vs Z 本征态
> 注意区分：Z 的本征态是计算基 $\{|0\rangle, |1\rangle\}$，而 X 的本征态是叠加态 $\{|\pm\rangle\}$。这两组基完全不同——它们是对易关系 $[X,Z] \neq 0$ 的直接体现。在 QEC 中，X 型和 Z 型稳定子测量对应不同的本征基。

## 3. 为什么本征态在 QEC 中重要？

在 [[QEC]] 中，**稳定子**就是门算符，**逻辑码字**就是这些稳定子的**本征值 $+1$ 的本征态**：

$$
S_i|\psi\rangle_L = +1 \cdot |\psi\rangle_L \quad \forall i
$$

当错误发生时，某些稳定子的本征值从 $+1$ 变为 $-1$，这就是 syndrome 信号。这本质上就是测量"某些门算符作用后状态变没变"。

> [!info] 为什么稳定子本征态定义了码空间
> 稳定子码的码空间是所有稳定子本征值为 $+1$ 的本征态的交集。这相当于同时对所有稳定子测量结果为"无错误"的子空间。任何错误都会将系统推出这个子空间，使某些稳定子的本征值变为 $-1$，从而暴露错误位置。

## 4. 旋转门的本征态

旋转门 $R_z(\theta) = e^{-i\theta Z/2}$ 的本征态与 $Z$ 相同（因为 $e^{-i\theta Z/2}|0\rangle = e^{-i\theta/2}|0\rangle$），只是本征值从 $\pm 1$ 变为 $e^{\mp i\theta/2}$。

这也是为什么计算基 $\{|0\rangle, |1\rangle\}$ 在 Rydberg 体系中如此重要——它既是 $Z$ 门的本征基，也是 [[Rabi-Flopping]] 的自然量子化轴。

---

## 📐 核心公式摘要

- **算符**：本征值 $+1$ 态 — 本征值 $-1$ 态
- **Z**：$ — 0\rangle$
- **X**：$ — +\rangle = (
- **Y**：$( — 0\rangle+i


## 📝 更新记录

- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
