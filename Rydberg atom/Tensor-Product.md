---
aliases: [Tensor Product, 张量积, 直积, Kronecker Product, ⊗]
tags: [Physics, Quantum, Mathematics, LinearAlgebra]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "vague"
---

# 张量积（Tensor Product）

> 来源批注：评价中列出 "张量积的数学公式" — Bluvstein et al., 2026

## 1. 为什么需要张量积？

单个量子比特的态空间是 $\mathbb{C}^2$（由 $|0\rangle, |1\rangle$ 张开）。

**两个量子比特的联合态空间** 是各自态空间的**张量积**：

$$
\mathcal{H}_{12} = \mathcal{H}_1 \otimes \mathcal{H}_2 \cong \mathbb{C}^4
$$

这解释了为什么 2 个 qubit 有 4 个基矢 $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$，$n$ 个 qubit 有 $2^n$ 个基矢（量子计算指数级加速的来源）。

> [!tip] 为什么需要张量积？
> 张量积的物理意义是组合独立系统。两个独立量子比特的状态空间不能简单相加（直和），而必须用张量积来描述，因为联合系统的状态可能包含纠缠态——无法分解为各自独立状态的乘积。

## 2. 向量的张量积

两个列向量 $|\psi\rangle = \begin{pmatrix}a\\b\end{pmatrix}$ 和 $|\phi\rangle = \begin{pmatrix}c\\d\end{pmatrix}$ 的张量积：

$$
|\psi\rangle \otimes |\phi\rangle = \begin{pmatrix}a\\b\end{pmatrix} \otimes \begin{pmatrix}c\\d\end{pmatrix} = \begin{pmatrix}ac\\ad\\bc\\bd\end{pmatrix}
$$

**具体例子：**

$$
|0\rangle \otimes |1\rangle = \begin{pmatrix}1\\0\end{pmatrix} \otimes \begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\1\\0\\0\end{pmatrix} = |01\rangle
$$

## 3. 矩阵的张量积（Kronecker 积）

对于算符 $A$ 和 $B$，$A \otimes B$ 的计算规则：

$$
A \otimes B = \begin{pmatrix}a_{11}B & a_{12}B \\ a_{21}B & a_{22}B\end{pmatrix}
$$

**例子：$X \otimes Z$（$X$ 作用在第一个 qubit，$Z$ 作用在第二个）**

$$
X \otimes Z = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} \otimes \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix} = \begin{pmatrix}0\cdot Z & 1\cdot Z \\ 1\cdot Z & 0\cdot Z\end{pmatrix} = \begin{pmatrix}0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0\end{pmatrix}
$$

> [!warning] 常见误区：张量积 ≠ 矩阵乘法
> $A \otimes B$ 不等于 $A \times B$（矩阵乘法）。张量积会扩大矩阵维度（$2\times2 \otimes 2\times2 = 4\times4$），而矩阵乘法要求维度匹配且结果维度不变。初学者常把 Kronecker 积与普通矩阵乘法混淆。

## 4. 重要性质

| 性质 | 说明 |
|---|---|
| $(A\otimes B)(C\otimes D) = AC\otimes BD$ | 复合操作的张量积可以分块计算 |
| $(A\otimes B)^\dagger = A^\dagger \otimes B^\dagger$ | 厄米共轭可分配到每个算符 |
| $\text{tr}(A\otimes B) = \text{tr}(A)\cdot\text{tr}(B)$ | 迹的乘法性 |

## 5. 与量子纠错的关系

在 [[表面码 (Surface Code)]] 中，稳定子算符如 $X_1 X_2 X_3 X_4$ 就是四个 Pauli $X$ 算符的张量积：

$$
X^{\otimes 4} = X \otimes X \otimes X \otimes X
$$

在 [[反对易关系 (Anti-Commutation)]] 的计算中，张量积结构决定了哪些算符对易、哪些反对易。

> [!info] 稳定子算符作为 Pauli 张量积
> 稳定子码（如表面码）中的稳定子算符本质上是 Pauli 矩阵的张量积，例如 $X^{\otimes 4} = X \otimes X \otimes X \otimes X$。每个稳定子只在局部 qubit 上作用一个 Pauli 矩阵，整体通过张量积构建。这种结构使得 syndrome 提取可以并行执行。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $\otimes$ | 张量积 | $\begin{pmatrix}a\\b\end{pmatrix}\otimes\begin{pmatrix}c\\d\end{pmatrix} = \begin{pmatrix}ac\\ad\\bc\\bd\end{pmatrix}$ |
| $\mathcal{H}_n$ | $n$ qubit 态空间维数 | $\dim = 2^n$ |
| $(A\otimes B)(C\otimes D)$ | 张量积复合 | $= AC \otimes BD$ |

## 📝 更新记录

- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
