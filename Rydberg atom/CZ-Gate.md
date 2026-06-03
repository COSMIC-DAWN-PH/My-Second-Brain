---
aliases:
  - CZ Gate
  - CZ门
  - Controlled-Z
  - 控制Z门
  - 纠缠门
tags:
  - Physics
  - Quantum
  - Gates
  - TwoQubit
  - Entanglement
date: 2026-03-29
status: WIP
source: "[[generall quantum 2026]]"
comprehension: getting there
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

### 3.1 逐步推导

**第一步：输入态展开。** 两个 qubit 都处于 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$，它们彼此独立（乘积态），用分配律展开：

$$
|+\rangle|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle)
$$

> [!tip] 物理直觉
> 这就像两个独立抛的硬币——每个都有 $\frac{1}{2}$ 概率是 0 或 1，四个组合等概率出现，彼此没有关联。

**第二步：施加 CZ 门。** CZ 门的作用规则：**只有 $|11\rangle$ 变号，其他三项不变**。逐项操作：

$$
\xrightarrow{\text{CZ}} \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)
$$

### 3.2 为什么这个态是纠缠的？

纠缠的判据：如果一个两 qubit 态**能**写成 $|\text{qubit 1}\rangle \otimes |\text{qubit 2}\rangle$（两个独立态的乘积），它就**不是**纠缠的；如果**不能**分解，它就是纠缠的。

我们用反证法验证。假设可以分解，设：

$$
(a|0\rangle + b|1\rangle)(c|0\rangle + d|1\rangle) = ac|00\rangle + ad|01\rangle + bc|10\rangle + bd|11\rangle
$$

要等于 $\frac{1}{2}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)$，系数必须匹配：

$$
ac = \tfrac{1}{2}, \quad ad = \tfrac{1}{2}, \quad bc = \tfrac{1}{2}, \quad bd = -\tfrac{1}{2}
$$

从前两个方程得 $c = d$，从后两个方程也得 $c = d$。但如果 $c = d$，则 $bd = bc$，与 $bc = \frac{1}{2}$、$bd = -\frac{1}{2}$ 矛盾。**假设不成立，态无法分解——它是纠缠态。** ∎

### 3.3 测量视角：纠缠意味着什么

用测量的语言看 CZ 门前后的区别。对 qubit 1 做测量，看 qubit 2 的态变成什么：

**施加 CZ 之前**——两个 qubit 独立，qubit 2 永远是 $|+\rangle$，与 qubit 1 的测量结果无关。

**施加 CZ 之后**：

| Qubit 1 测量结果 | Qubit 2 的态 | 概率 |
| --- | --- | --- |
| $\vert 0 \rangle$ | $\frac{1}{\sqrt{2}}(\vert 0 \rangle + \vert 1 \rangle) = \vert + \rangle$ | 50% |
| $\vert 1 \rangle$ | $\frac{1}{\sqrt{2}}(\vert 0 \rangle - \vert 1 \rangle) = \vert - \rangle$ | 50% |

> [!tip] 关键洞察
> 测 qubit 1 得到 0 或 1，会**瞬间决定** qubit 2 变成 $|+\rangle$ 还是 $|-\rangle$。这种"测一个、定两个"的关联，就是纠缠。CZ 门通过在 $|11\rangle$ 上引入相位差，打破了两个 qubit 之间的独立性。

### 3.4 注意：这不是标准贝尔态

> [!warning] 常见误解
> 上面的结果 $\frac{1}{2}(|00\rangle + |01\rangle + |10\rangle - |11\rangle)$ 是**纠缠态**，但**不是**标准贝尔态。标准贝尔态 $|\Phi^+\rangle$ 只有两项：
>
> $$
> |\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
> $$
>
> 它有四项，归一化系数也不同。

要从 $|+\rangle|+\rangle$ 经 CZ 得到标准 Bell 态 $|\Phi^+\rangle$，完整的线路是：

$$
|00\rangle \xrightarrow{H \otimes H} |+\rangle|+\rangle \xrightarrow{\text{CZ}} \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle - |11\rangle) \xrightarrow{H \otimes H} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle
$$

即 **CZ 前后各加一层 H 门**（两比特都加），就能得到标准 Bell 态。这也是 §4 中 CZ $\leftrightarrow$ CNOT 转换的一个侧面体现。

## 4. CZ 门与 CNOT 门的关系

> [!info] 线性代数视角的完整推导
> 本节给出算符语言和矩阵语言的对比证明。如果你想从更基础的线性代数角度理解——包括基变换、相似变换、共轭转置、酉矩阵——请参见 [[Basis-Transformation]]。

CZ 门和 CNOT 门可以互相转化（只需在目标 qubit 两侧各加一个 $H$ 门）：

$$
\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)
$$

$$
\text{CZ} = (I \otimes H) \cdot \text{CNOT} \cdot (I \otimes H)
$$

### 4.1 为什么 H 门能做这件事？

关键在于 H 门的**基变换**效果：

$$
H\vert 0\rangle = \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle) = \vert +\rangle, \quad
H\vert 1\rangle = \frac{1}{\sqrt{2}}(\vert 0\rangle - \vert 1\rangle) = \vert -\rangle
$$

H 门把**计算基** $\{\vert 0\rangle, \vert 1\rangle\}$ 变成了 **X 基** $\{\vert +\rangle, \vert -\rangle\}$。

而它有一个极其重要的算符恒等式：

> [!tip] 核心恒等式：$HXH = Z$
>
> H 门把 X 门"翻译"成了 Z 门。这不是巧合——X 在计算基下做比特翻转，Z 在计算基下做相位翻转。H 门交换了这两种操作的"语言"。
> 完整的逐步推导（矩阵计算、逐态验证、物理直觉）见 [[Single-Qubit-Gates#3.4 基变换恒等式：$HXH = Z$ 的完整推导]]。

### 4.2 算符分解严格证明

#### 4.2.1 投影算符写法：CNOT 和 CZ 的统一结构

CNOT 和 CZ 都可以用投影算符写成统一的形式：

$$
\text{CNOT} = \vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes X
$$

$$
\text{CZ} = \vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes Z
$$

两者结构完全一样，区别仅在于第二项中是 $X$ 还是 $Z$。

> [!tip] 为什么这样写？物理直觉
> 拆开读：投影算符 $\vert 0\rangle\langle 0\vert$ 的意思是"**如果控制比特是 $\vert 0\rangle$**"，$\vert 1\rangle\langle 1\vert$ 的意思是"**如果控制比特是 $\vert 1\rangle$**"。
>
> - CNOT：控制比特是 0 → 什么都不做（$I$）；控制比特是 1 → 翻转目标比特（$X$）
> - CZ：控制比特是 0 → 什么都不做（$I$）；控制比特是 1 → 翻转目标相位（$Z$）
>
> 把两个"条件分支"加起来，就是完整的门操作。就像 if-else 语句：`if (control == 0) do I; else do X/Z`。

> [!info] 为什么两个投影加起来不矛盾？
> $\vert 0\rangle\langle 0\vert + \vert 1\rangle\langle 1\vert = I$（完备性关系）。控制比特**不是** 0 **就是** 1，两个分支互斥且穷尽，所以可以安全地加起来。

#### 4.2.2 关键等式：$HIH = I$ 和 $HXH = Z$

证明的核心是两个恒等式，需要先搞清楚：

**$HIH = I$（H 门对恒等算符没影响）**

这几乎是显然的：$HIH = H \cdot I \cdot H = H \cdot H = H^2 = I$，因为 H 门是**自逆的**（$H^2 = I$）。

> [!tip] 为什么 $H^2 = I$？
> H 门把 $|0\rangle \to |+\rangle$，再做一次 $|+\rangle \to |0\rangle$。同理 $|1\rangle \to |-\rangle \to |1\rangle$。H 门做两次等于没做——就像"翻转再翻转"回到原位。

**$HXH = Z$（H 门把 X "翻译"成 Z）**

逐态验证：

$$
HXH \vert 0\rangle = HX \vert +\rangle = H \vert -\rangle = \vert 1\rangle = Z \vert 0\rangle \quad \checkmark
$$

$$
HXH \vert 1\rangle = HX \vert -\rangle = H \vert +\rangle = \vert 0\rangle = Z \vert 1\rangle \quad \checkmark
$$

> [!tip] 直觉记忆
> $X$ 在计算基下做比特翻转（$\vert 0\rangle \leftrightarrow \vert 1\rangle$），$Z$ 在计算基下做相位翻转（$\vert 1\rangle \to -\vert 1\rangle$）。H 门交换了两种操作的"语言"——把"翻转值"变成"翻转相位"。

#### 4.2.3 逐步证明：$(I \otimes H) \cdot \text{CNOT} \cdot (I \otimes H) = \text{CZ}$

**第一步：写出完整的算符表达式。**

$$
(I \otimes H) \cdot \text{CNOT} \cdot (I \otimes H)
$$

把 CNOT 的投影算符展开代入：

$$
= (I \otimes H) \big[\vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes X\big] (I \otimes H)
$$

**第二步：分配律展开——这是最关键的一步。**

$(I \otimes H)$ 要从左边乘进去，$(I \otimes H)$ 要从右边乘进去。对加法中的**每一项**分别操作：

$$
= \underbrace{(I \otimes H)(\vert 0\rangle\langle 0\vert \otimes I)(I \otimes H)}_{\text{第一项}} + \underbrace{(I \otimes H)(\vert 1\rangle\langle 1\vert \otimes X)(I \otimes H)}_{\text{第二项}}
$$

**第三步：张量积的乘法可以"分开算"。**

> [!warning] 关键技巧：$(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$
> 张量积有个极其好用的性质：两个张量积相乘时，**左边乘左边，右边乘右边**，各自独立运算。

所以第一项：

$$
(I \otimes H)(\vert 0\rangle\langle 0\vert \otimes I)(I \otimes H) = (I \cdot \vert 0\rangle\langle 0\vert \cdot I) \otimes (H \cdot I \cdot H)
$$

$$
= \vert 0\rangle\langle 0\vert \otimes HIH = \vert 0\rangle\langle 0\vert \otimes I
$$

第二项：

$$
(I \otimes H)(\vert 1\rangle\langle 1\vert \otimes X)(I \otimes H) = (I \cdot \vert 1\rangle\langle 1\vert \cdot I) \otimes (H \cdot X \cdot H)
$$

$$
= \vert 1\rangle\langle 1\vert \otimes HXH = \vert 1\rangle\langle 1\vert \otimes Z
$$

**第四步：合并两项。**

$$
\vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes Z = \text{CZ} \quad \checkmark
$$

> [!tip] 整个证明的"一句话版"
> CNOT 和 CZ 的唯一区别是目标比特上的 $X$ 和 $Z$。H 门是 $X \leftrightarrow Z$ 的"翻译官"（$HXH = Z$）。所以在 CNOT 的目标比特两侧各加一个 H 门，就把 $X$ 翻译成了 $Z$，CNOT 就变成了 CZ。

### 4.3 算符语言 vs 矩阵语言：两种等价的表达

上面的证明用的是**算符语言**（operator language），而 §2 中 CZ 的 $4\times4$ 矩阵是**矩阵语言**（matrix language）。两者描述的是完全相同的物理操作，只是"说话方式"不同。本节把它们逐一对应，帮助你建立两种语言之间的"翻译直觉"。

#### 4.3.1 投影算符的直觉

算符语言的核心"积木"是**投影算符** $\vert 0\rangle\langle 0\vert$ 和 $\vert 1\rangle\langle 1\vert$。它的工作方式是：

$$
\vert 0\rangle\langle 0\vert \cdot |\psi\rangle = \langle 0|\psi\rangle \, |0\rangle
$$

翻译成人话：先用 $\langle 0|\psi\rangle$ 算出"$|\psi\rangle$ 里有多少 $|0\rangle$ 的成分"（一个复数），再把这个数乘到 $|0\rangle$ 上——结果就是 $|\psi\rangle$ 在 $|0\rangle$ 方向上的**投影**（影子）。

> [!tip] 两个投影加起来 = 什么都不做
> $|0\rangle\langle 0| + |1\rangle\langle 1| = I$（单位算符）。因为任何态都能拆成 $|0\rangle$ 方向 + $|1\rangle$ 方向的分量，两个投影加起来恰好还原原来的态。

#### 4.3.2 每块"积木"对应哪个矩阵

| 算符语言 | 含义 | 对应 $2\times2$ 矩阵 |
|----------|------|----------------------|
| $\vert 0\rangle\langle 0\vert$ | 投影到 $\vert 0\rangle$ | $\begin{pmatrix}1&0\\0&0\end{pmatrix}$ |
| $\vert 1\rangle\langle 1\vert$ | 投影到 $\vert 1\rangle$ | $\begin{pmatrix}0&0\\0&1\end{pmatrix}$ |
| $I$（单位算符） | 不做任何操作 | $\begin{pmatrix}1&0\\0&1\end{pmatrix}$ |
| $X$（比特翻转） | $\vert 0\rangle \leftrightarrow \vert 1\rangle$ | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ |
| $Z$（相位翻转） | $\vert 1\rangle \to -\vert 1\rangle$ | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ |
| $\otimes$（张量积） | 把两个小矩阵"膨胀"成大矩阵 | Kronecker 积 |

#### 4.3.3 CNOT 的展开验证

算符语言：$\text{CNOT} = \vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes X$

对应矩阵展开（$\otimes$ 是 Kronecker 积）：

$$
= \underbrace{\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}}_{\text{控制比特是}\vert 0\rangle\text{时，不动}} + \underbrace{\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}}_{\text{控制比特是}\vert 1\rangle\text{时，翻转}}
$$

$$
= \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}
$$

#### 4.3.4 CZ 的展开验证

算符语言：$\text{CZ} = \vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes Z$

对应矩阵展开：

$$
= \underbrace{\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}}_{\text{控制比特是}\vert 0\rangle\text{时，不动}} + \underbrace{\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}}_{\text{控制比特是}\vert 1\rangle\text{时，加相位}}
$$

$$
= \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix} \quad \checkmark
$$

#### 4.3.5 同一个证明的两条路线

§4.2 的证明 $(I \otimes H)\cdot\text{CNOT}\cdot(I \otimes H) = \text{CZ}$，用两种语言走一遍：

**算符路线**（§4.2 的写法）——利用 $HXH = Z$ 直接"替换积木"：

$$
|0\rangle\langle 0| \otimes \underbrace{HIH}_{=I} + |1\rangle\langle 1| \otimes \underbrace{HXH}_{=Z} = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes Z = \text{CZ}
$$

**矩阵路线**——把所有矩阵写出来，暴力乘：

$$
\underbrace{\frac{1}{2}\begin{pmatrix}1&1&0&0\\1&-1&0&0\\0&0&1&1\\0&0&1&-1\end{pmatrix}}_{I\otimes H} \cdot \underbrace{\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}}_{\text{CNOT}} \cdot \underbrace{\frac{1}{2}\begin{pmatrix}1&1&0&0\\1&-1&0&0\\0&0&1&1\\0&0&1&-1\end{pmatrix}}_{I\otimes H} = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix} = \text{CZ}
$$

两种路线殊途同归，结果完全一致。

#### 4.3.6 两种语言的对比总结

| | 算符语言 | 矩阵语言 |
|--|---------|---------|
| **优点** | 结构清晰，能看出条件逻辑（"如果是 $\|0\rangle$ 就不动，如果是 $\|1\rangle$ 就做 X"） | 可以直接算数值，编程实现方便 |
| **适合场景** | 推导、证明、理解物理含义 | 数值验证、Python/Qiskit 编程 |
| **类比** | 写伪代码（描述逻辑） | 写 Python（暴力计算） |
| **推广到 n 个 qubit** | 公式形式不变，依然简洁 | 矩阵大小 $2^n \times 2^n$，指数爆炸 |

> [!tip] 学习建议
> 对于当前阶段（大二，学表象理论和 Dirac notation），**算符语言更重要**——它是量子力学推导的主力工具，且不受维度爆炸限制。矩阵语言在你需要**手算具体数值**或**写程序**时才用。两种都要会，但优先掌握算符语言。

> [!info] 证明的核心
> 整个推导只用了一个事实：$HXH = Z$。H 门在 CNOT 的目标比特两侧"包裹"，本质上就是把 CNOT 内部的 $X$（比特翻转）替换成了 $Z$（相位翻转），从而把 CNOT 变成了 CZ。

### 4.4 物理含义："两种语言"的翻译

| | CNOT | CZ |
|--|------|-----|
| **做了什么** | 条件性**翻转目标比特的值**（$\vert 0\rangle \leftrightarrow \vert 1\rangle$） | 条件性**翻转 $\vert 11\rangle$ 的相位**（$+1 \to -1$） |
| **翻转的是** | **比特**（X 操作） | **相位**（Z 操作） |
| **创造纠缠？** | ✅ 是 | ✅ 是（同等强度） |
| **对称性** | 不对称（有控制/目标之分） | 对称（两个 qubit 地位平等） |

> [!tip] 语言类比
> 想象你有两种语言来描述同一件事：
> - **英语**（CNOT）："如果 A 是 true，就翻转 B 的 true/false"——关注**比特值变化**
> - **法语**（CZ）："如果 A 和 B 都是 true，就给信号加一个负号"——关注**相位变化**
>
> H 门就是"翻译官"——它把英语翻译成法语，法语翻译回英语。两种语言说的是**同一件事**（同样的纠缠），只是表达方式不同。

^260603

### 4.5 为什么这对中性原子很重要？

在中性原子中，Rydberg 阻塞天然是对称的——两个原子同时激发时相互阻塞，没有"谁控制谁"的概念。所以 **CZ 是物理原生门**。如果你想做 CNOT（比如跑一个标准量子算法），就得额外加两个 H 门：

$$
\text{CNOT}_{1\to 2} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)
$$

这就是为什么中性原子平台的线路编译器应该**优先使用 CZ 门**——用 CZ 少两步，用 CNOT 多两步 H 门。

## 5. 在 Rydberg 体系中的实现

中性原子平台利用 **[[Rydberg-Blockade]]** 实现 CZ 门：

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

- **CZ**：CZ 门矩阵 — $\text{diag}(1,1,1,-1)$
- **CNOT $\leftrightarrow$ CZ**：门转换 — $\text{CNOT} = (I\otimes H)\cdot\text{CZ}\cdot(I\otimes H)$


---

## 🔗 相关笔记

- [[Basis-Transformation]] — **基变换与相似变换**：向量空间、$S^{-1}AS$ 公式、共轭转置、酉矩阵——理解 $HXH = Z$ 的线性代数基础
- [[Entangling-Gate]] — 纠缠门的概念总览：定义、判据、分类、各平台实现
- [[Two-Qubit-Gates]] — 两比特门总览：CNOT、CZ、SWAP、Bell 态
- [[Rydberg-Blockade]] — CZ 门的物理实现机制
- [[Rabi-Flopping]] — $\pi$ 脉冲的物理基础
- [[Single-Qubit-Gates]] — 与 CZ 门组合构成通用门集的单比特门（含 $HXH = Z$ 恒等式的完整推导）
- [[Transversal-Gate]] — 并行施加 CZ 门的容错方案

## 📝 更新记录

- 2026-03-29: 初始创建
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
- 2026-06-03: 扩充 §4，添加 $HXH=Z$ 恒等式、算符分解证明、物理含义对比表、语言类比、中性原子编译优势
- 2026-06-03: 添加 §4.3 算符语言与矩阵语言对照（投影算符直觉、积木对应表、CNOT/CZ 展开验证、双路线证明对比）
- 2026-06-03: 重写 §3，补充逐步推导、反证法证明纠缠、测量视角直觉、修正 Bell 态标注错误
- 2026-06-03: 扩充 §4.2，逐行拆解投影算符写法的物理直觉、$HIH=I$ 与 $HXH=Z$ 的验证、张量积分配律、完整四步证明
- 2026-06-03: 在 §4 添加 [[Basis-Transformation]] 链接，在相关笔记中添加基变换与相似变换文档入口
