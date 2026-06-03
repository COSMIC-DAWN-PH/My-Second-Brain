---
aliases:
  - 基变换
  - Basis Change
  - 相似变换
  - Similarity Transformation
  - 线性代数参考
  - Linear Algebra Reference
tags:
  - Physics
  - Quantum
  - Mathematics
  - LinearAlgebra
  - Fundamental
date: 2026-06-03
status: WIP
source: "通用数学基础"
comprehension: "getting there"
---

# 基变换与相似变换：量子门的线性代数语言

> 本笔记是线性代数参考文档，系统讲解**基变换（change of basis）**和**相似变换（similarity transformation）**的数学基础，最终落到量子计算中 $HXH = Z$ 这类恒等式的深层理解。目标读者：大二物理系学生，已学过表象理论和 Dirac notation。

---

## 1. 向量与基：一切的起点

### 1.1 向量空间

在量子力学中，态矢量生活在线性空间（向量空间）里。最基本的例子：

- 单 qubit 态空间：$\mathcal{H}_1 = \mathbb{C}^2$（二维复向量空间）
- 两个 qubit 的态空间：$\mathcal{H}_2 = \mathbb{C}^4$（四维复向量空间）

> [!tip] 直觉
> 向量空间就是一个"可以做加法和数乘"的数学空间。$\mathbb{C}^2$ 中的向量是二维列向量，$\mathbb{C}^4$ 中的向量是四维列向量。

### 1.2 基与坐标

**基（basis）是向量空间中一组线性无关的向量，能够通过线性组合表示空间中的**任意**向量。

以 $\mathbb{C}^2$ 为例，有两组常用的基：

**计算基（computational basis）$\{|0\rangle, |1\rangle\}$**：

$$
|0\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \qquad |1\rangle = \begin{pmatrix}0\\1\end{pmatrix}
$$

**X 基（Hadamard basis）$\{|+\rangle, |-\rangle\}$**：

$$
|+\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}, \qquad |-\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}
$$

同一个量子态在这两组基下的**坐标（系数）不同**。例如：

$$
|0\rangle = 1\cdot|0\rangle + 0\cdot|1\rangle \qquad \text{（计算基下的坐标：$(1, 0)^T$）}
$$

$$
|0\rangle = \frac{1}{\sqrt{2}}|+\rangle + \frac{1}{\sqrt{2}}|-\rangle \qquad \text{（X 基下的坐标：$(\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}})^T$）}
$$

> [!tip] 物理直觉
> 同一个向量，用不同的基去"量"，得到不同的坐标。就像同一个点，用笛卡尔坐标和极坐标描述，数值不同但描述的是同一个点。

### 1.3 基变换矩阵

从一组基到另一组基的转换由一个**可逆矩阵** $S$ 描述：

$$
|e'_j\rangle = \sum_i S_{ij} |e_i\rangle
$$

$S$ 的**第 $j$ 列**就是新基矢 $|e'_j\rangle$ 在旧基下的坐标。

以计算基 $\{|0\rangle, |1\rangle\}$ 到 X 基 $\{|+\rangle, |-\rangle\}$ 的变换为例：

$$
S = H = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
$$

因为：

$$
|+\rangle = H|0\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle \qquad \text{（S 的第 1 列）}
$$

$$
|-\rangle = H|1\rangle = \frac{1}{\sqrt{2}}|0\rangle - \frac{1}{\sqrt{2}}|1\rangle \qquad \text{（S 的第 2 列）}
$$

> [!warning] 基变换矩阵 ≠ 量子门
> 这里恰好 $S = H$（Hadamard 门），但这是因为 H 门本身就是"把计算基映射到 X 基"的门。一般情况下，基变换矩阵和量子门没有直接关系——基变换矩阵描述的是"换坐标系"，量子门描述的是"态的演化"。它们是两个不同的概念，只是在 $HXH = Z$ 这个问题上恰好交汇。

---

## 2. 线性算符的矩阵表示：同一个操作，不同基下长得不一样

### 2.1 核心概念

线性算符 $\hat{A}$ 是一个把向量变成向量的线性映射：$|\psi\rangle \to \hat{A}|\psi\rangle$。

同一个线性算符，在不同基下写出的矩阵不同。

> [!tip] 类比
> 想象一个向量 $\vec{v}$ 在三维空间中指向"右前方"。在笛卡尔坐标系中它写成 $(1, 1, 0)$，在球坐标系中它写成 $(r, \theta, \phi)$。向量本身没变，变的是描述它的"语言"。算符的矩阵表示同理。

### 2.2 具体例子：X 门在两个基下的矩阵

**X 门**的作用：$X|0\rangle = |1\rangle$，$X|1\rangle = |0\rangle$（比特翻转）。

**在计算基 $\{|0\rangle, |1\rangle\}$ 下**：

$$
X_{\text{Z-basis}} = \begin{pmatrix}\langle 0|X|0\rangle & \langle 0|X|1\rangle \\ \langle 1|X|0\rangle & \langle 1|X|1\rangle\end{pmatrix} = \begin{pmatrix}0&1\\1&0\end{pmatrix}
$$

**在 X 基 $\{|+\rangle, |-\rangle\}$ 下**：

$$
X_{\text{X-basis}} = \begin{pmatrix}\langle +|X|+\rangle & \langle +|X|-\rangle \\ \langle -|X|+\rangle & \langle -|X|-\rangle\end{pmatrix}
$$

计算每个元素：

$$
X|+\rangle = |-\rangle, \qquad X|-\rangle = |+\rangle
$$

所以：

$$
X_{\text{X-basis}} = \begin{pmatrix}\langle +|-\rangle & \langle +|+\rangle \\ \langle -|-\rangle & \langle -|+\rangle\end{pmatrix} = \begin{pmatrix}0&1\\1&0\end{pmatrix}
$$

> [!info] 有趣的事实
> X 门在两组基下的矩阵**完全相同**！这是因为 X 门恰好把 $\{|+\rangle, |-\rangle\}$ 互换，就像它把 $\{|0\rangle, |1\rangle\}$ 互换一样。这是一个特殊情况——大多数算符在不同基下的矩阵是不同的。

现在看 Z 门：

**在计算基下**：$Z_{\text{Z-basis}} = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$

**在 X 基下**：$Z|+\rangle = |-\rangle$，$Z|-\rangle = |+\rangle$，所以 $Z_{\text{X-basis}} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$

> [!tip] 关键观察
> Z 门在计算基下是对角矩阵（$\text{diag}(1,-1)$），但在 X 基下变成了非对角矩阵 $\begin{pmatrix}0&1\\1&0\end{pmatrix}$——这恰好就是 X 门的矩阵！也就是说：**Z 在 X 基下的矩阵 = X 在 Z 基下的矩阵**。

---

## 3. 相似变换：基变换的数学公式

### 3.1 核心定理

> [!tip] 相似变换定理（最重要的公式之一）
> 如果算符 $\hat{A}$ 在旧基 $\{|e_i\rangle\}$ 下的矩阵是 $A$，在新基 $\{|e'_j\rangle\}$ 下的矩阵是 $A'$，基变换矩阵是 $S$（第 $j$ 列是 $|e'_j\rangle$ 在旧基下的坐标），则：
>
> $$\boxed{A' = S^{-1} A S}$$
>
> 这就是**相似变换（similarity transformation）**。

### 3.2 推导

设态 $|\psi\rangle$ 在旧基下的坐标是列向量 $v$，在新基下的坐标是 $v'$。基变换关系是：

$$
v = S v' \qquad \Longleftrightarrow \qquad v' = S^{-1} v
$$

算符 $\hat{A}$ 在旧基下把 $v$ 变成 $A v$。在新基下，同样的操作变成：

$$
v' \to S^{-1}(Av) = S^{-1}A(Sv') = (S^{-1}AS)v'
$$

所以新基下的矩阵就是 $A' = S^{-1}AS$。

> [!info] 为什么要这样写？
> 相似变换的本质是："先用 $S$ 从新基翻译回旧基（$S$），在旧基下做操作（$A$），再用 $S^{-1}$ 翻译回新基（$S^{-1}$）"。三步合起来就是 $S^{-1}AS$。

### 3.3 重要性质

相似变换保持以下量不变：

| 量 | 原因 |
|---|------|
| **行列式** $\det(A') = \det(A)$ | $\det(S^{-1}AS) = \det(S^{-1})\det(A)\det(S) = \det(A)$ |
| **迹** $\text{tr}(A') = \text{tr}(A)$ | 迹在相似变换下不变 |
| **本征值** | $A'v = \lambda v$ 和 $Av = \lambda v$ 描述同一个本征方程 |
| **矩阵的秩** | 秩在可逆变换下不变 |

> [!warning] 相似变换 ≠ 相等
> $A'$ 和 $A$ 是**同一个线性算符在不同基下的不同矩阵表示**。它们描述的是同一个物理操作，只是"用不同的语言"说出来。它们的矩阵元素不同，但行列式、迹、本征值都相同。

---

## 4. 酉基变换：量子力学的基变换

### 4.1 为什么量子力学只用酉基变换？

一般线性代数中，基变换矩阵 $S$ 只需要是**可逆**的就行。但在量子力学中，我们要求基矢是**正交归一**的（$\langle e_i|e_j\rangle = \delta_{ij}$），且变换后也要保持正交归一。这个额外约束把 $S$ 限制为**酉矩阵**：

$$
\boxed{S^\dagger S = SS^\dagger = I \qquad \Longleftrightarrow \qquad S^{-1} = S^\dagger}
$$

> [!tip] 酉矩阵 = "保内积的变换"
> 酉矩阵 $S$ 保证变换后向量之间的内积不变：$\langle S\psi|S\phi\rangle = \langle\psi|S^\dagger S|\phi\rangle = \langle\psi|\phi\rangle$。这意味着正交性、归一性、概率——全部保持。

### 4.2 酉基变换的简化公式

因为 $S^{-1} = S^\dagger$，相似变换在酉变换下简化为：

$$
\boxed{A' = S^\dagger A S}
$$

这就是量子力学中最常见的基变换公式。$S^\dagger A S$ 读作："用 $S$ 做基变换，用 $S^\dagger$ 做逆变换"。

### 4.3 Hadamard 门：$S = S^\dagger = S^{-1}$

H 门满足三个等式：

$$
H = H^\dagger \qquad \text{（自伴 / Hermitian）}
$$

$$
H^2 = I \qquad \text{（自逆）}
$$

$$
H^{-1} = H^\dagger = H \qquad \text{（酉 + 自伴 = 自逆）}
$$

所以对 H 门做相似变换：

$$
H^{-1} A H = H A H
$$

**$S^{-1}$ 和 $S$ 都是 $H$ 本身**——这就是为什么 $HXH = Z$ 中出现的是 $H$ "夹住" $X$，而不是 $H^{-1}XH$。它们在数学上是同一件事。

> [!warning] 不是所有酉门都自伴
> $S^{-1} = S^\dagger$ 对所有酉矩阵成立，但 $S^\dagger = S$（自伴）只对部分酉矩阵成立。例如：
> - $H^\dagger = H$ ✓（H 自伴）
> - $X^\dagger = X$ ✓（Pauli-X 自伴）
> - $Z^\dagger = Z$ ✓（Pauli-Z 自伴）
> - $T^\dagger \neq T$ ✗（T 门不是自伴的，$T = \text{diag}(1, e^{i\pi/4})$，$T^\dagger = \text{diag}(1, e^{-i\pi/4})$）
>
> 对于 $T$ 门：$TXT^{-1} = T^\dagger X T \neq T X T$。只有对自伴酉矩阵，才有 $S^{-1}AS = SAS$。

---

## 5. $HXH = Z$ 的完整线性代数解释

现在我们有了所有工具来深入理解 $HXH = Z$。

### 5.1 三种等价的理解方式

#### 方式一：相似变换视角

$HXH$ 是 $X$ 门在 H 定义的新基下的**相似变换**：

$$
HXH = H^{-1} X H
$$

（因为 $H^{-1} = H$，所以 $H^{-1}XH = HXH$）

这就是说：**$Z$ 是 $X$ 门在 X 基下的矩阵表示。**

验证：

$$
Z = H^{-1} X H = S^{-1} X S
$$

其中 $S = H$ 是从计算基到 X 基的变换矩阵。$Z$ 的意思是："在 X 基中，$X$ 门看起来像 $Z$ 门。"

#### 方式二：矩阵乘法视角

这是最直接的验证（详见 [[Single-Qubit-Gates]] §3.4）：

$$
HXH = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} \begin{pmatrix}0&1\\1&0\end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \begin{pmatrix}1&0\\0&-1\end{pmatrix} = Z
$$

#### 方式三：逐态验证视角

对任意态 $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$：

$$
HXH|\psi\rangle = HX(\alpha|+\rangle + \beta|-\rangle)
$$

等等，这个角度最直觉的方式是：

$$
HXH|\psi\rangle = HX \cdot H|\psi\rangle
$$

右边的 $H$ 把 $|\psi\rangle$ 从计算基"翻译"到 X 基。中间的 $X$ 在 X 基中翻转两个基矢（$|+\rangle \leftrightarrow |-\rangle$）。左边的 $H$ 把结果"翻译"回计算基。

而在 X 基中，翻转 $|+\rangle \leftrightarrow |-\rangle$ 正好等于**相位翻转**——这就是 Z。

### 5.2 更深的理解：同一个算符的两种"面貌"

> [!tip] 核心洞察
> $X$ 和 $Z$ 不是"两种不同的操作"——它们是**同一个物理操作在不同基下的不同名字**。
>
> - **$X$**：在计算基（Z 基）下看，"翻转 $|0\rangle \leftrightarrow |1\rangle$"
> - **$Z$**：在 X 基下看，同样的操作变成了"翻转 $|+\rangle \leftrightarrow |-\rangle$"（= 相位翻转）
>
> H 门就是在这两种"观看方式"之间切换的"镜头"。

用数学语言：

$$
Z = H^{-1} X H = S^{-1} X S
$$

这完全等价于说：

> "$Z$ 是 $X$ 在 X 基下的矩阵表示。"

### 5.3 对偶关系 $HZH = X$

同样的逻辑反向也成立：

$$
HZH = H^{-1} Z H
$$

$Z$ 门在 X 基下的矩阵表示 = $X$ 门在 Z 基下的矩阵表示。

| 恒等式 | 含义 |
|--------|------|
| $HXH = Z$ | X 在 X 基下看起来像 Z |
| $HZH = X$ | Z 在 Z 基下看起来像 X |
| $HYH = Y$ | Y 在 X 基下看起来还是 Y（Y 对 H 变换不变） |

### 5.4 为什么 $HYH = Y$？

因为 $Y = iXZ$，而 $HXH = Z$，$HZH = X$，所以：

$$
HYH = H(iXZ)H = i(HXH)(HZH) = iZX = i\cdot(-Y/i) = Y
$$

或者更直接地：Y 在 X 基和 Z 基下的矩阵恰好相同，因为它同时涉及两个基的"混合"。

---

## 6. 共轭转置：为什么 $S^\dagger$ 出现在左边

### 6.1 定义

对矩阵 $A$，其**共轭转置**（conjugate transpose / Hermitian adjoint）$A^\dagger$ 定义为：

$$
(A^\dagger)_{ij} = \overline{A_{ji}}
$$

即：先转置（$A^T$），再对每个元素取复共轭（$\overline{a_{ij}}$）。

**例子**：

$$
A = \begin{pmatrix}1&i\\0&2\end{pmatrix} \quad \Rightarrow \quad A^\dagger = \begin{pmatrix}1&0\\-i&2\end{pmatrix}
$$

> [!warning] 实矩阵的特殊情况
> 如果矩阵所有元素都是实数，共轭不影响，$A^\dagger = A^T$（就是普通转置）。H 门和 Pauli 矩阵都是实矩阵，所以 $H^\dagger = H^T = H$（H 是对称的实矩阵）。

### 6.2 $A^\dagger$ 的物理含义

$A^\dagger$ 是算符 $\hat{A}$ 的**伴随算符**（adjoint operator）。它满足：

$$
\langle\phi|A\psi\rangle = \langle A^\dagger\phi|\psi\rangle
$$

即：把 $A$ 从右边移到左边时，要变成 $A^\dagger$。

> [!tip] 内积的对偶性
> 这个等式的物理含义是："$A$ 作用在右矢（ket）上的效果"等价于"$A^\dagger$ 作用在左矢（bra）上的效果"。bra 和 ket 是一对对偶空间，$A$ 和 $A^\dagger$ 分别是它们各自空间上的算符。

### 6.3 自伴算符（Hermitian）：$A^\dagger = A$

如果一个算符满足 $A^\dagger = A$，它就是**自伴的**（Hermitian）。自伴算符的特点：

- 本征值都是实数
- 对应可观测物理量（量子力学的基本假设）

H 门、Pauli 矩阵（$X, Y, Z$）都是自伴的。

### 6.4 酉算符：$U^\dagger U = I$

酉算符满足 $U^\dagger U = I$，即 $U^\dagger = U^{-1}$。

**酉算符的物理含义**：保持内积不变（= 保持概率守恒）。所有量子门都是酉算符。

> [!info] 自伴 + 酉 = 自逆
> 如果一个矩阵既是自伴的（$A^\dagger = A$）又是酉的（$A^\dagger = A^{-1}$），则 $A = A^{-1}$，即 $A^2 = I$（自逆）。
>
> H 门恰好满足这个条件：$H^\dagger = H$（自伴）且 $H^\dagger = H^{-1}$（酉），所以 $H^2 = I$。
>
> 但不是所有酉门都自伴：$T$ 门是酉的（$T^\dagger T = I$），但 $T^\dagger \neq T$（不自伴）。

---

## 7. 投影算符：基变换的另一面

### 7.1 定义

投影算符 $\hat{P}_i = |e_i\rangle\langle e_i|$ 把任意向量投影到基矢 $|e_i\rangle$ 方向：

$$
\hat{P}_i|\psi\rangle = |e_i\rangle\langle e_i|\psi\rangle
$$

物理含义：提取 $|\psi\rangle$ 中"有多少 $|e_i\rangle$ 的成分"。

### 7.2 完备性关系

$$
\sum_i |e_i\rangle\langle e_i| = I
$$

任何向量都可以用基矢展开，所有投影加起来等于什么都不做。

### 7.3 投影算符与基变换的关系

用投影算符可以写出"在不同基下看到的同一个算符"：

$$
A'_{jk} = \langle e'_j|\hat{A}|e'_k\rangle
$$

如果新基是 $|e'_j\rangle = S|e_j\rangle$（$S$ 是基变换矩阵），则：

$$
A'_{jk} = \langle e_j|S^\dagger \hat{A} S|e_j\rangle
$$

这就是 $A' = S^\dagger A S$ 的分量形式——**相似变换公式**。

### 7.4 在量子门中的应用

CZ 门的投影分解（详见 [[CZ-Gate]] §4.2 和 [[CZ-Linear-Algebra]] §6）：

$$
\text{CZ} = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes Z
$$

读法：投影算符 $|0\rangle\langle 0|$ "选中控制 qubit 为 $|0\rangle$ 的情况"，$|1\rangle\langle 1|$ "选中控制 qubit 为 $|1\rangle$ 的情况"。两个投影互斥且完备，加起来就是整个算符。

---

## 8. 共轭变换的统一框架

### 8.1 一般公式

对任意酉矩阵 $S$，算符 $\hat{A}$ 的**共轭变换**（conjugation）定义为：

$$
\hat{A} \;\xrightarrow{S}\; \hat{A}' = S^\dagger \hat{A} S
$$

这就是基变换的完整数学描述。

### 8.2 常见共轭变换汇总

| 共轭变换 | $S$ | $S^\dagger$ | 结果 | 物理含义 |
|----------|-----|------------|------|---------|
| $HXH$ | $H$ | $H$ | $Z$ | X 在 X 基下 = Z |
| $HZH$ | $H$ | $H$ | $X$ | Z 在 Z 基下 = X |
| $HYH$ | $H$ | $H$ | $Y$ | Y 在 X 基下不变 |
| $XZX$ | $X$ | $X$ | $-Z$ | Z 在 X 基下翻符号（反对易） |
| $ZXZ$ | $Z$ | $Z$ | $-X$ | X 在 Z 基下翻符号（反对易） |
| $TXT^{-1}$ | $T$ | $T^\dagger$ | $e^{i\pi/4}X$ | X 在 T 定义的基下获得相位 |

> [!tip] 记忆规律
> - **$H$ 共轭**：$HXH = Z$，$HZH = X$，$HYH = Y$——H 门交换 X 和 Z 的角色
> - **Pauli 共轭**：$XZX = -Z$，$ZXZ = -X$——Pauli 门之间的共轭产生负号（因为它们反对易）
> - **自伴酉门**（$S^\dagger = S$）：共轭变换 $S^\dagger A S = SAS$，左右两边用同一个矩阵

### 8.3 为什么 $HXH = Z$ 而 $XZX = -Z$？

**$HXH = Z$**：H 门是基变换，它把"计算基下的 X 翻译成 X 基下的 Z"。这是纯粹的基变换，没有额外相位。

**$XZX = -Z$**：X 门不是"基变换"，它是"物理操作"。X 和 Z 是**反对易**的（$XZ = -ZX$），所以：

$$
XZX = XZ \cdot X = (-ZX) \cdot X = -Z \cdot X^2 = -Z \cdot I = -Z
$$

> [!warning] 关键区别
> - $S^\dagger A S$（酉共轭）= 基变换 = **改变观察角度**，不改变物理
> - $BAB$（一般乘法）= 连续施加操作 = **物理演化**，可以改变态
>
> $HXH$ 是"换角度看 X"，$XZX$ 是"先做 Z，再做 X，再做 Z"。前者是被动的坐标变换，后者是主动的物理操作。

---

## 9. 应用：CZ-CNOT 转换的线性代数视角

CZ 门和 CNOT 门的转换（详见 [[CZ-Gate]] §4.2 和 [[CZ-Linear-Algebra]] §8）：

$$
\text{CZ} = (I \otimes H) \cdot \text{CNOT} \cdot (I \otimes H)
$$

从线性代数角度看：

1. **$(I \otimes H)$ 是基变换矩阵**：它把第二个 qubit 从计算基变换到 X 基
2. **CNOT 在新基下**：在 X 基中看，CNOT 的目标操作 $X$ 变成了 $Z$（因为 $HXH = Z$）
3. **$(I \otimes H)$ 是逆变换**：从 X 基回到计算基

所以整个公式的含义是：

> "CNOT 在 X 基下看就是 CZ。$I \otimes H$ 是这个基变换的镜头。"

$$
\underbrace{(I \otimes H)}_{\text{换镜头到 X 基}} \cdot \underbrace{\text{CNOT}}_{\text{在 X 基中操作}} \cdot \underbrace{(I \otimes H)}_{\text{换镜头回 Z 基}} = \text{CZ}
$$

> [!tip] 一句话总结
> **$HXH = Z$ 的本质是：X 门和 Z 门是同一个物理操作在不同基下的不同名字。H 门是这两组基之间的"翻译官"。$S^{-1}AS$（相似变换）是"在新基下重新描述算符 A"的标准数学公式，$HXH$ 只是 $S = H$ 时的特例。**

---

## 10. 查阅索引

以下速查表帮助你在遇到类似恒等式时快速判断：

| 你想知道的 | 查阅章节 |
|-----------|---------|
| 什么是基变换？ | §1、§2 |
| $A' = S^{-1}AS$ 的推导 | §3.2 |
| 为什么量子力学用 $S^\dagger A S$ | §4.2 |
| H 门为什么自逆（$H^2 = I$） | §4.3 |
| $HXH = Z$ 的三种理解 | §5.1 |
| 共轭转置的定义 | §6.1 |
| $A^\dagger = A$ 和 $A^\dagger = A^{-1}$ 的区别 | §6.3、§6.4 |
| 投影算符与基变换的关系 | §7.3 |
| 为什么 $XZX = -Z$ 但 $HXH = Z$ | §8.3 |
| CZ-CNOT 转换的线性代数解释 | §9 |

---

## 📐 核心公式摘要

- **相似变换**：$A' = S^{-1} A S$ — 同一算符在不同基下的矩阵表示
- **酉基变换**：$A' = S^\dagger A S$，$S^{-1} = S^\dagger$ — 量子力学标准形式
- **共轭转置**：$(A^\dagger)_{ij} = \overline{A_{ji}}$ — 转置 + 复共轭
- **酉矩阵**：$U^\dagger U = I$，$U^{-1} = U^\dagger$ — 保内积、保概率
- **自伴矩阵**：$A^\dagger = A$ — 本征值为实数，对应可观测量
- **H 门三重性质**：$H = H^\dagger$（自伴），$H^2 = I$（自逆），$H^{-1} = H$（酉）
- **$HXH = Z$**：$H^{-1} X H = Z$ — X 在 X 基下的矩阵表示是 Z
- **$HZH = X$**：$H^{-1} Z H = X$ — Z 在 Z 基下的矩阵表示是 X
- **CZ-CNOT**：$(I\otimes H)\cdot\text{CNOT}\cdot(I\otimes H) = \text{CZ}$ — CNOT 在 X 基下 = CZ


---

## 🔗 相关笔记

- [[CZ-Gate]] — CZ 门的完整介绍，§4 详细证明 CZ-CNOT 转换
- [[Single-Qubit-Gates]] — §3.4 $HXH = Z$ 的三种推导
- [[Tensor-Product]] — 张量积：Kronecker 积的计算规则
- [[Gate-Eigenstates]] — Pauli 门和 H 门的本征态
- [[Pauli-Matrices]] — Pauli 矩阵的代数性质（$XZ = -ZX$ 等）
- [[SU2-SO3-and-Euler-Decomposition]] — SU(2) 与 Bloch 球旋转的关系

## 📝 更新记录

- 2026-06-03: 初始创建，系统讲解向量空间、基变换、相似变换、共轭转置、酉矩阵，落到 $HXH = Z$ 的线性代数解释
