---
aliases:
  - Tensor Product
  - 张量积
  - 直积
  - Kronecker Product
  - ⊗
tags:
  - Physics
  - Quantum
  - Mathematics
  - LinearAlgebra
date: 2026-03-29
status: WIP
source: "[[generall quantum 2026]]"
comprehension: getting there
---

# 张量积（Tensor Product）

> 来源批注：评价中列出 "张量积的数学公式" — Bluvstein et al., 2026

## 1. 为什么需要张量积？

单个 qubit 的态空间是 $\mathbb{C}^2$，由两个计算基 $|0\rangle, |1\rangle$ 张开：

$$
\mathcal{H}_A = \operatorname{span}\{|0\rangle_A, |1\rangle_A\} \cong \mathbb{C}^2
$$

如果有两个 qubit，联合系统必须同时记录：

- 第一个 qubit 是 $0$ 还是 $1$；
- 第二个 qubit 是 $0$ 还是 $1$。

所以基矢不是简单的 $|0\rangle_A, |1\rangle_A, |0\rangle_B, |1\rangle_B$ 四个“单体标签”，而是四种**有序组合**：

$$
|0\rangle_A\otimes|0\rangle_B = |00\rangle,\quad
|0\rangle_A\otimes|1\rangle_B = |01\rangle,\quad
|1\rangle_A\otimes|0\rangle_B = |10\rangle,\quad
|1\rangle_A\otimes|1\rangle_B = |11\rangle
$$

因此两个 qubit 的联合态空间是各自态空间的**张量积**：

$$
\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B \cong \mathbb{C}^2 \otimes \mathbb{C}^2 \cong \mathbb{C}^4
$$

维数规则是：

$$
\dim(\mathcal{H}_A \otimes \mathcal{H}_B)
= \dim(\mathcal{H}_A)\dim(\mathcal{H}_B)
= 2\times 2 = 4
$$

这就解释了为什么 2 个 qubit 有 4 个计算基矢：

$$
\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}
$$

推广到 $n$ 个 qubit：

$$
\mathcal{H}_n = (\mathbb{C}^2)^{\otimes n}, \qquad \dim(\mathcal{H}_n)=2^n
$$

也就是说，$n$ 个 qubit 的一般纯态需要写成 $2^n$ 个计算基矢的线性叠加。

> [!tip] 物理直觉：不是“相加”，而是“组合”
> 两个经典 bit 的可能取值也是 $00,01,10,11$ 四种。张量积做的事，就是把“每个子系统的可能状态”组合成“整个系统的可能状态”。量子力学额外多出来的地方在于：联合态不仅可以处在某一个组合上，还可以处在这些组合的**相干叠加**中。

> [!warning] 指数级态空间 ≠ 自动指数级加速
> $2^n$ 维态空间是量子算法可能强大的数学基础，但不是“把 $2^n$ 个答案一次性读出来”。真正的加速来自：指数级多的概率振幅、量子门造成的相位干涉、以及最后测量时把正确答案的概率放大。

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

## 5. 为什么张量积会允许纠缠态？

张量积首先允许我们写出**直积态**（product state）。例如：

$$
|\psi\rangle_A = a|0\rangle + b|1\rangle, \qquad
|\phi\rangle_B = c|0\rangle + d|1\rangle
$$

它们的联合态是：

$$
|\psi\rangle_A\otimes|\phi\rangle_B
= ac|00\rangle + ad|01\rangle + bc|10\rangle + bd|11\rangle
$$

注意这里四个振幅不是随便的，它们必须满足：

$$
(ac)(bd) = (ad)(bc)
$$

也就是如果写成一般形式

$$
|\Psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle
$$

那么可分离态必须满足：

$$
\boxed{\alpha\delta = \beta\gamma}
$$

但是张量积空间里的一个普通向量不一定满足这个条件。例如 Bell state：

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

这里 $\alpha=1/\sqrt{2}$，$\delta=1/\sqrt{2}$，但 $\beta=0$，$\gamma=0$，所以：

$$
\alpha\delta = \frac{1}{2}, \qquad \beta\gamma = 0
$$

两者不相等，因此它**不能**写成 $|\psi\rangle_A\otimes|\phi\rangle_B$。这就是纠缠态：整体态存在，但不能拆成两个 qubit 各自独立的态。更详细的讨论见 [[Two-Qubit-State-and-Entanglement]]。

> [!tip] 纠缠的核心图像
> 纠缠不是“两个粒子靠得很近”，也不是“两个粒子互相影响得很强”。纠缠的数学本质是：联合态向量在 $\mathcal{H}_A\otimes\mathcal{H}_B$ 中，但它不在“可分离态”那一小部分集合里。

## 6. 与量子纠错的关系

在 [[Surface-Code]] 中，稳定子算符如 $X_1 X_2 X_3 X_4$ 就是四个 Pauli $X$ 算符的张量积：

$$
X^{\otimes 4} = X \otimes X \otimes X \otimes X
$$

在 [[Anti-Commutation]] 的计算中，张量积结构决定了哪些算符对易、哪些反对易。

> [!info] 稳定子算符作为 Pauli 张量积
> 稳定子码（如表面码）中的稳定子算符本质上是 Pauli 矩阵的张量积，例如 $X^{\otimes 4} = X \otimes X \otimes X \otimes X$。每个稳定子只在局部 qubit 上作用一个 Pauli 矩阵，整体通过张量积构建。这种结构使得 syndrome 提取可以并行执行。

---

## 📐 核心公式摘要

- $\otimes$：张量积 — $\begin{pmatrix}a\\b\end{pmatrix}\otimes\begin{pmatrix}c\\d\end{pmatrix} = \begin{pmatrix}ac\\ad\\bc\\bd\end{pmatrix}$
- $\mathcal{H}_n$：$n$ qubit 态空间维数 — $\dim(\mathcal{H}_n)=2^n$
- $(A\otimes B)(C\otimes D)$：张量积复合 — $(A\otimes B)(C\otimes D)=AC\otimes BD$
- 两 qubit 可分离判据：若 $|\Psi\rangle=\alpha|00\rangle+\beta|01\rangle+\gamma|10\rangle+\delta|11\rangle$，则 product state 满足 $\alpha\delta=\beta\gamma$


## 📝 更新记录

- 2026-06-03: 修复核心公式摘要中的 LaTeX 渲染；补充两 qubit 张量积、$2^n$ 维数来源与纠缠态解释
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
