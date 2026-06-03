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

### 4.2 算符分解严格证明

CNOT 和 CZ 都可以用投影算符写成统一的形式：

$$
\text{CNOT} = \vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes X
$$

$$
\text{CZ} = \vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes Z
$$

两者结构完全一样，区别仅在于第二项中是 $X$ 还是 $Z$。现在对 CNOT 两边施加 $I \otimes H$：

$$
(I \otimes H) \cdot \text{CNOT} \cdot (I \otimes H)
$$

$$
= (I \otimes H) \big[\vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes X\big] (I \otimes H)
$$

$$
= \vert 0\rangle\langle 0\vert \otimes HIH + \vert 1\rangle\langle 1\vert \otimes HXH
$$

$$
= \vert 0\rangle\langle 0\vert \otimes I + \vert 1\rangle\langle 1\vert \otimes Z
$$

$$
= \text{CZ} \quad \checkmark
$$

> [!info] 证明的核心
> 整个推导只用了一个事实：$HXH = Z$。H 门在 CNOT 的目标比特两侧"包裹"，本质上就是把 CNOT 内部的 $X$（比特翻转）替换成了 $Z$（相位翻转），从而把 CNOT 变成了 CZ。

### 4.3 物理含义："两种语言"的翻译

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

### 4.4 为什么这对中性原子很重要？

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

- **\text{CZ}**：CZ 门矩阵 — $\text{diag}(1,1,1,-1)$
- **CNOT $\leftrightarrow$ CZ**：门转换 — $\text{CNOT} = (I\otimes H)\cdot\text{CZ}\cdot(I\otimes H)$


---

## 🔗 相关笔记

- [[Entangling-Gate]] — 纠缠门的概念总览：定义、判据、分类、各平台实现
- [[Two-Qubit-Gates]] — 两比特门总览：CNOT、CZ、SWAP、Bell 态
- [[Rydberg-Blockade]] — CZ 门的物理实现机制
- [[Rabi-Flopping]] — $\pi$ 脉冲的物理基础
- [[Single-Qubit-Gates]] — 与 CZ 门组合构成通用门集的单比特门
- [[Transversal-Gate]] — 并行施加 CZ 门的容错方案

## 📝 更新记录

- 2026-03-29: 初始创建
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
- 2026-06-03: 扩充 §4，添加 $HXH=Z$ 恒等式、算符分解证明、物理含义对比表、语言类比、中性原子编译优势
