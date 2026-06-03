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

## 0. 张量积本身的定义

张量积最容易被误解成“把两个向量直接拼起来”。更准确地说：

> [!tip] 一句话定义
> 如果 $V$ 和 $W$ 是两个向量空间，那么它们的张量积 $V\otimes W$ 是一个新的向量空间。这个新空间的基本元素写作 $v\otimes w$，表示“从 $V$ 里取一个方向 $v$，同时从 $W$ 里取一个方向 $w$”形成的联合方向。

它必须满足**双线性**（bilinear）规则：

$$
(a v_1+b v_2)\otimes w
= a(v_1\otimes w)+b(v_2\otimes w)
$$

$$
v\otimes(a w_1+b w_2)
= a(v\otimes w_1)+b(v\otimes w_2)
$$

这两条规则的意思是：张量积对左边的向量线性，对右边的向量也线性。

如果 $V$ 的一组基是：

$$
\{e_1,e_2,\cdots,e_m\}
$$

$W$ 的一组基是：

$$
\{f_1,f_2,\cdots,f_n\}
$$

那么 $V\otimes W$ 的一组基就是所有成对组合：

$$
\{e_i\otimes f_j\mid i=1,\cdots,m;\ j=1,\cdots,n\}
$$

所以维数相乘：

$$
\dim(V\otimes W)=\dim(V)\dim(W)=mn
$$

> [!warning] “基矢量的组合”只说对了一半
> 对有限维空间来说，张量积空间的基确实可以看成“左边基矢和右边基矢的所有成对组合”。但张量积不只是列出这些组合；它还规定了这些组合如何线性叠加、如何展开，以及如何作为一个新的向量空间来计算。

对列向量来说，张量积就是常见的 Kronecker product。例如：

$$
\begin{pmatrix}a\\b\end{pmatrix}
\otimes
\begin{pmatrix}c\\d\end{pmatrix}
=
\begin{pmatrix}
ac\\
ad\\
bc\\
bd
\end{pmatrix}
$$

这里的四个分量 $ac,ad,bc,bd$ 就是“第一个系统的两个分量”和“第二个系统的两个分量”所有成对相乘的结果。

> [!warning] 这一步本身不会产生纠缠
> 把两个具体向量相乘：
>
> $$
> \begin{pmatrix}a\\b\end{pmatrix}\otimes\begin{pmatrix}c\\d\end{pmatrix}
> =
> \begin{pmatrix}ac\\ad\\bc\\bd\end{pmatrix}
> $$
>
> 得到的是 **product state**，一定不是纠缠态。纠缠不是从“两个向量相乘”这一步冒出来的，而是从下一步冒出来的：我们把所有 $|i\rangle\otimes|j\rangle$ 当作基矢以后，允许它们做任意线性叠加。

所以张量积导致纠缠的逻辑不是：

$$
\text{两个向量做一次 } \otimes \Rightarrow \text{纠缠}
$$

而是：

$$
\text{用 } \otimes \text{ 建立联合态空间}
\Rightarrow
\text{允许所有基矢线性叠加}
\Rightarrow
\text{出现不能拆回单个 } |\psi\rangle_A\otimes|\phi\rangle_B \text{ 的态}
$$

这最后一种态才叫**纠缠态**。

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

### 1.1 张量积空间等价于两个 qubit 能够所在的空间吗？

是的。对于两个 qubit，**张量积空间本身**就是联合系统能够所在的完整 Hilbert space：

$$
\boxed{\mathcal{H}_{AB}=\mathcal{H}_A\otimes\mathcal{H}_B}
$$

但这里有一个非常容易混淆的点：

**张量积空间**：

$$
\mathcal{H}_A\otimes\mathcal{H}_B
= \operatorname{span}\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}
$$

它是由四个计算基矢张成的整个四维空间，**包含纠缠态**。

**Product state**：

$$
|\psi\rangle_A\otimes|\phi\rangle_B
$$

它是两个单 qubit 态直接相乘得到的特殊向量，**本身不包含纠缠**。

也就是说：

$$
\text{product states} \subsetneq \mathcal{H}_A\otimes\mathcal{H}_B
$$

纠缠态的存在并不说明“张量积空间不等价于两 qubit 态空间”。恰恰相反，纠缠态说明：**两 qubit 的完整态空间必须是张量积空间，而不能只取 product states 那一小部分。**

> [!warning] 关键区分
> “张量积空间”不是“所有 product states 的集合”。张量积空间是先把 $|0\rangle_A\otimes|0\rangle_B$、$|0\rangle_A\otimes|1\rangle_B$、$|1\rangle_A\otimes|0\rangle_B$、$|1\rangle_A\otimes|1\rangle_B$ 当作基矢，然后允许它们做任意线性叠加。纠缠态正是这种线性叠加里不能再拆成单个 product state 的向量。

例如：

$$
|00\rangle = |0\rangle_A\otimes|0\rangle_B
$$

是 product state，也是张量积空间里的一个向量。

而：

$$
\frac{|00\rangle+|11\rangle}{\sqrt{2}}
$$

也是张量积空间里的向量，但它不是 product state，所以它是纠缠态。

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

先说结论：

> [!tip] 最核心的逻辑
> 单个 product state 不纠缠；但是两个 qubit 的完整态空间不是“只包含 product state”，而是“由 product basis 张成的整个线性空间”。只要允许线性叠加，就会出现一些向量不能拆成单个 product state，这些向量就是纠缠态。

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

这说明 product state 在四维空间里的系数有一个特殊形状：

$$
\begin{pmatrix}
\alpha\\
\beta\\
\gamma\\
\delta
\end{pmatrix}
=
\begin{pmatrix}
ac\\
ad\\
bc\\
bd
\end{pmatrix}
$$

注意这里四个振幅不是随便的。因为它们来自两个单 qubit 态的成对相乘，所以必须满足：

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

这就是 product state 的“指纹”。如果一个两 qubit 态满足不了这个指纹，就说明它不能拆成两个单 qubit 态的乘积。

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

> [!warning] 因果关系不要说反
> 不是“张量积运算自动制造纠缠”，而是“张量积给出了正确的联合态空间；这个空间比 product states 的集合更大；大出来的那部分就是纠缠态”。

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

- 向量空间张量积：若 $V=\operatorname{span}\{e_i\}$，$W=\operatorname{span}\{f_j\}$，则 $V\otimes W=\operatorname{span}\{e_i\otimes f_j\}$
- $\otimes$：张量积 — $\begin{pmatrix}a\\b\end{pmatrix}\otimes\begin{pmatrix}c\\d\end{pmatrix} = \begin{pmatrix}ac\\ad\\bc\\bd\end{pmatrix}$
- $\mathcal{H}_n$：$n$ qubit 态空间维数 — $\dim(\mathcal{H}_n)=2^n$
- $(A\otimes B)(C\otimes D)$：张量积复合 — $(A\otimes B)(C\otimes D)=AC\otimes BD$
- 两 qubit 可分离判据：若 $|\Psi\rangle=\alpha|00\rangle+\beta|01\rangle+\gamma|10\rangle+\delta|11\rangle$，则 product state 满足 $\alpha\delta=\beta\gamma$
- 关系：$\text{product states} \subsetneq \mathcal{H}_A\otimes\mathcal{H}_B$；纠缠态属于 $\mathcal{H}_A\otimes\mathcal{H}_B$，但不属于 product states
- 纠缠来源：不是单次 $|\psi\rangle_A\otimes|\phi\rangle_B$ 运算产生纠缠，而是 $\mathcal{H}_A\otimes\mathcal{H}_B$ 允许 product basis 的任意线性叠加，其中一部分态不能分解成单个 product state


## 📝 更新记录

- 2026-06-03: 澄清“张量积导致纠缠”的准确含义：单个张量积态不纠缠，完整张量积空间中的不可分解线性叠加才是纠缠态
- 2026-06-03: 增加张量积本身的数学定义、双线性规则，以及“基矢成对组合”与“完整向量空间”的区别
- 2026-06-03: 补充“张量积空间”与“product states 集合”的区别，澄清纠缠态为什么仍然写在张量积空间中
- 2026-06-03: 修复核心公式摘要中的 LaTeX 渲染；补充两 qubit 张量积、$2^n$ 维数来源与纠缠态解释
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
