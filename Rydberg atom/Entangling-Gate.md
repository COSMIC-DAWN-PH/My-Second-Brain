---
aliases:
  - Entangling Gate
  - 纠缠门
  - Entangling Operation
  - 纠缠操作
  - 两比特纠缠门
tags:
  - Physics
  - Quantum
  - Gates
  - TwoQubit
  - Entanglement
  - Fundamental
date: 2026-06-03
status: Draft
source: "[[2023-parallel-gates-handout]]"
comprehension: "vague"
---

# 纠缠门（Entangling Gate）

> 来源讲义：[[2023-parallel-gates-handout|高保真并行纠缠门讲义]] — Bluvstein et al., Nature 2024
> 本笔记从**概念层面**系统介绍"纠缠门"这个类别——它是什么、如何判别、有哪些类型、在不同物理平台如何实现。与 [[CZ-Gate]]（具体门操作）和 [[Two-Qubit-Gates]]（门的数学性质）互补，这里讨论的是**纠缠门作为一个整体概念**。

---

## 1. 什么是纠缠门？

### 1.1 从单比特门的局限说起

在 [[Single-Qubit-Gates]] 中我们知道，单比特门只做一件事：**在 Bloch 球上旋转单个 qubit 的状态**。

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle \xrightarrow{\text{单比特门}} \alpha'|0\rangle + \beta'|1\rangle
$$

无论你怎么旋转，两个独立的 qubit 依然各自独立——它们之间**没有关联**。

> [!tip] 核心直觉
> 单比特门就像两个人**各自独立思考**——A 改变自己的想法，B 完全不受影响。再多的独立思考者，也无法产生"共识"。
>
> **纠缠门是让两个 qubit 产生"共谋"的操作**——A 的决定会影响 B 的行为。一旦这种关联建立，两个 qubit 就"纠缠"在一起了。

### 1.2 纠缠门的精确定义

> **纠缠门（entangling gate）**是一种两量子比特门，它能将**至少一个**乘积态（product state）映射为**纠缠态**（entangled state）。

用数学语言说：

$$
\exists \, |\psi_A\rangle, |\psi_B\rangle \quad \text{such that} \quad U_{\text{ent}} \left(|\psi_A\rangle \otimes |\psi_B\rangle\right) \notin \mathcal{H}_A \otimes \mathcal{H}_B \text{（不可分离）}
$$

如果一个两比特门**对所有乘积态**的作用结果都是乘积态，那它就**不是**纠缠门。

### 1.3 纠缠门的作用方式

纠缠门的核心机制是**条件性操作（conditional operation）**：

> 根据一个 qubit 的状态，决定是否对另一个 qubit 执行某种操作。

例如：
- **CNOT 门**：如果控制 qubit 是 $\vert 1\rangle$，就翻转目标 qubit（$\vert 0\rangle \leftrightarrow \vert 1\rangle$）
- **[[CZ-Gate|CZ 门]]**：如果两个 qubit 都是 $\vert 1\rangle$，就给系统加一个 $\pi$ 相位（$\vert 11\rangle \to -\vert 11\rangle$）

正是这种"条件性"使得两个 qubit 的状态产生了关联——纠缠由此而来。

---

## 2. 纠缠门的数学判据：如何判断一个门是否"纠缠"？

### 2.1 判据一：Schmidt 分解检验

回忆 [[Two-Qubit-State-and-Entanglement]] 中的结论：一个两 qubit 纯态 $|\Psi\rangle$ 是**乘积态**（无纠缠）当且仅当它可以写成：

$$
|\Psi\rangle = |\psi_A\rangle \otimes |\psi_B\rangle
$$

**检验方法**：对门的输出态做 Schmidt 分解，如果 Schmidt 秩 $> 1$，则输出态是纠缠态，门是纠缠门。

**示例**：CNOT 门作用在 $|+\rangle|0\rangle$ 上：

$$
\text{CNOT} \left(\frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes |0\rangle\right) = \frac{|00\rangle + |11\rangle}{\sqrt{2}} = |\Phi^+\rangle
$$

$|\Phi^+\rangle$ 的 Schmidt 秩为 2（不可分离），因此 CNOT 是纠缠门。

### 2.2 判据二：纠缠能力（Entangling Power）

更系统的方法是定义**纠缠能力** $e_p(U)$，衡量一个门在所有可能输入上**平均产生多少纠缠**：

$$
e_p(U) = \overline{E\left(U(|\psi_A\rangle \otimes |\psi_B\rangle)\right)}
$$

其中 $E(\cdot)$ 是某种纠缠度量（如纠缠熵），上划线表示对所有可能的乘积输入态取平均。

> [!info] 数学细节
> 对于两 qubit 门 $U$，纠缠能力可以精确计算为：
> $$e_p(U) = \frac{2}{9}\left(3 - \text{tr}\left(M_U^\dagger M_U\right)\right)$$
> 其中 $M_U$ 是从 $U$ 的矩阵元素构造的 $3\times3$ 矩阵（与 Pauli 基的展开系数有关）。当 $e_p = 0$ 时，门不是纠缠门；当 $e_p = 1/2$ 时，门有最大的纠缠能力。

### 2.3 关键结论

| 门 | 纠缠能力 $e_p$ | 是否纠缠门？ |
|---|---|---|
| $\text{CNOT}$ | $1/2$ | **是**（最大纠缠能力） |
| $\text{CZ}$ | $1/2$ | **是**（最大纠缠能力） |
| $\text{iSWAP}$ | $1/2$ | **是**（最大纠缠能力） |
| $\text{SWAP}$ | $0$ | **否**（不创造纠缠） |
| $U_A \otimes U_B$（局部门） | $0$ | **否** |

> [!tip] 记忆要点
> **SWAP 门不是纠缠门！** 它只是"搬运"两个 qubit 的状态，不创造任何新的纠缠。这一点常常被误解。
>
> CNOT 和 CZ 的纠缠能力相同（$1/2$），这是它们等价性的深层原因。

---

## 3. 纠缠门的分类：常见纠缠门一览

### 3.1 两比特纠缠门

| 门 | 矩阵（计算基） | 作用规则 | 纠缠能力 |
|---|---|---|---|
| $\text{CNOT}$ | $\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$ | $\vert c\rangle\vert t\rangle \to \vert c\rangle\vert t\oplus c\rangle$ | $1/2$ |
| $\text{CZ}$ | $\text{diag}(1,1,1,-1)$ | $\vert 11\rangle \to -\vert 11\rangle$ | $1/2$ |
| $\text{iSWAP}$ | $\text{diag}(1,i,i,1)$ | $\vert 01\rangle \to i\vert 10\rangle$，$\vert 10\rangle \to i\vert 01\rangle$ | $1/2$ |
| $\text{CPhase}(\theta)$ | $\text{diag}(1,1,1,e^{i\theta})$ | $\vert 11\rangle \to e^{i\theta}\vert 11\rangle$ | $\sin^2(\theta/2)/2$ |

### 3.2 多比特纠缠门

| 门 | 作用规则 | 说明 |
|---|---|---|
| $\text{CCZ}$ | $\vert 111\rangle \to -\vert 111\rangle$ | 三比特版 CZ，用于 [[QEC\|量子纠错]] |
| $\text{Toffoli}（\text{CCNOT}）$ | $\vert 11\rangle$ 时翻转第三比特 | 经典可逆计算的推广 |
| $\text{Fredkin}（\text{CSWAP}）$ | $\vert 1\rangle$ 时交换另外两个比特 | 条件交换门 |

> [!info] CCZ 门的重要性
> CCZ 门（加上单比特门）足以实现**任意量子算法**。在中性原子平台中，CCZ 门可以通过**多原子里德堡阻塞**直接实现——三个原子同时被激发时，利用多体相互作用获得相位积累。详见 [[2023-parallel-gates-handout#11. 多比特扩展：CCZ 门与 GHZ 态]]。

---

## 4. CNOT 与 CZ：纠缠门的"两种语言"

### 4.1 等价性

CNOT 和 CZ 是**完全等价**的纠缠门——它们可以通过单比特门互相转换：

$$
\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)
$$

$$
\text{CZ} = (I \otimes H) \cdot \text{CNOT} \cdot (I \otimes H)
$$

**物理含义**：$H$ 门在计算基 $\{|0\rangle, |1\rangle\}$ 和 Hadamard 基 $\{|+\rangle, |-\rangle\}$ 之间切换。CNOT 在**计算基**下做条件翻转，CZ 在 **Hadamard 基**下做条件翻转——它们说的是同一件事，只是"语言"不同。

### 4.2 对称性对比

| | CNOT | CZ |
|---|---|---|
| **对称性** | 不对称（有控制/目标之分） | **对称**（两个 qubit 地位平等） |
| **物理直觉** | "A 命令 B 翻转" | "两个都到 $\vert 1\rangle$ 时一起翻个身" |
| **天然平台** | 离子阱（不对称的 Mølmer-Sørensen 门） | **中性原子**（里德堡阻塞天然是对称的） |
| **通用门集** | $\{H, T, \text{CNOT}\}$ | $\{H, T, \text{CZ}\}$ |

> [!tip] 中性原子为什么偏好 CZ？
> 在 [[Rydberg-Blockade|里德堡阻塞]] 中，两个原子之间的相互作用是**对称的**——谁激发都会阻塞对方。这种物理对称性天然对应 CZ 门的数学对称性。如果要用 CNOT，就需要额外加 $H$ 门来"打破对称性"，增加了操作开销。
>
> 因此，中性原子量子计算的线路编译器通常以 CZ 为基础构建，而不是 CNOT。

---

## 5. 纠缠门在量子计算中的角色

### 5.1 没有纠缠门就没有量子计算

纠缠门是量子计算**超越经典计算**的关键。没有纠缠门：

$$
\text{只有单比特门} \implies n \text{ 个 qubit 各自独立} \implies \text{等价于 } n \text{ 个并行的经典模拟器}
$$

$$
\text{加入纠缠门} \implies qubit \text{ 之间产生关联} \implies \text{指数级的态空间被利用}
$$

> [!warning] 核心定理
> **任何量子算法都可以分解为单比特门和两比特纠缠门的交替序列。** 纠缠门是两比特门中**唯一能创造纠缠**的操作（SWAP 等非纠缠门不计入）。因此，纠缠门是量子计算的基本构件，如同经典计算中的逻辑门。

### 5.2 通用门集

**Solovay-Kitaev 定理**告诉我们，任何量子算法都可以用有限个基本门以任意精度近似。最基本的通用门集是：

$$
\{H, T, \text{CZ}\} \quad \text{或等价地} \quad \{H, T, \text{CNOT}\}
$$

其中：
- $H$（Hadamard）和 $T$（$\pi/8$ 门）是**单比特门**——负责所有单 qubit 旋转
- **CZ 或 CNOT** 是**唯一的纠缠门**——负责在 qubit 之间建立量子关联

### 5.3 量子线路的标准结构

量子线路的编排遵循"**单-双-单-双**"的交替节奏：

```
|0⟩ ─── [H] ───●─── [H] ───●─── [测量]
                │           │
|0⟩ ─── [H] ───⊕─── [T] ───⊕─── [测量]
         单比特  纠缠门  单比特  纠缠门
```

| 层次 | 门类型 | 功能 |
|------|--------|------|
| 单比特层 | $H$, $T$, $R_x$, $R_z$ | 状态准备、算法逻辑、测量基旋转 |
| 纠缠层 | CZ, CNOT | 建立 qubit 间的量子关联（创造纠缠） |

> [!tip] "旋律与和声"类比
> 量子线路就像一首交响乐：单比特门是**旋律**（每个乐器独奏），纠缠门是**和声**（乐器间的配合）。没有和声的音乐只是独奏合集，没有纠缠的"量子计算"只是经典并行模拟。

---

## 6. 纠缠门的质量指标

### 6.1 保真度（Fidelity）

**保真度**是衡量纠缠门质量的最直接指标：

$$
F = \langle \Psi_{\text{ideal}} | \rho_{\text{actual}} | \Psi_{\text{ideal}} \rangle
$$

其中 $|\Psi_{\text{ideal}}\rangle$ 是理想输出，$\rho_{\text{actual}}$ 是实际输出态的密度矩阵。

| 保真度 | 含义 | 典型平台 |
|--------|------|---------|
| $< 95\%$ | 无法用于有意义的量子计算 | 早期实验 |
| $95\%$–$99\%$ | 可用于量子模拟（不需要纠错） | 当前超导/离子阱 |
| $99\%$–$99.5\%$ | 接近容错阈值 | 当前中性原子（本文 2023 论文） |
| $> 99.9\%$ | 低于容错阈值，可支持纠错 | 下一代目标 |

### 6.2 容错阈值（Fault-Tolerance Threshold）

> [!warning] 为什么 99.5% 还不够？
> 理论上，要实现**可扩展的量子纠错**，每个物理门的错误率必须低于某个阈值（surface code 约 $1\%$）。虽然 99.5% 已经低于这个阈值，但**保真度越高，纠错的资源开销越小**。
>
> 具体来说：保真度从 99.0% 提升到 99.9%，实现一个逻辑比特所需的**物理比特数可能减少 10 倍**。这就是为什么追求更高保真度的纠缠门如此重要。

### 6.3 并行化能力

在大规模量子计算中，纠缠门必须能够**并行执行**——同时对多对 qubit 施加门操作。并行化的关键要求：

- **空间隔离**：不同门操作之间不产生串扰（crosstalk）
- **时间同步**：所有并行门在同一时间窗口内完成
- **保真度不退化**：并行执行时保真度与单独执行时一致

在中性原子平台中，里德堡相互作用的**短程特性**（$\propto r^{-6}$）天然支持并行化——相隔足够远的原子对可以独立执行纠缠门，详见 [[Rydberg-Blockade#4. 阻塞条件的定量分析]]。

---

## 7. 不同物理平台的纠缠门实现

### 7.1 平台对比

| 平台 | 纠缠门类型 | 物理机制 | 典型保真度 | 门时间 |
|------|-----------|---------|-----------|--------|
| **超导量子比特** | CNOT, CZ | 可调耦合 / Cross-Resonance | $\sim 99.5\%$ | $\sim 20\text{–}50\,\text{ns}$ |
| **离子阱** | CNOT, Mølmer-Sørensen | 共享声子模式 | $\sim 99.9\%$ | $\sim 100\text{–}500\,\mu\text{s}$ |
| **中性原子** | **CZ** | **里德堡阻塞（Rydberg Blockade）** | $\sim 99.5\%$ | $\sim 0.3\,\mu\text{s}$ |
| **光量子** | CNOT (KLM) | 光子干涉 | $\sim 95\%$ | $\sim \text{ps}$ |
| **NV 色心** | CNOT | 磁偶极耦合 | $\sim 90\%$ | $\sim \mu\text{s}$ |

### 7.2 各平台的纠缠机制简介

**超导量子比特（Cross-Resonance / Tunable Coupling）**：
两个超导 qubit 通过共面波导或可调耦合器连接。通过施加特定频率的微波脉冲，使一个 qubit 的跃迁频率与另一个 qubit 共振，从而产生条件性演化。优点是门速度快（ns 级），缺点是退相干时间较短。

**离子阱（Mølmer-Sørensen 门）**：
两个囚禁离子通过**共享的声子模式**（振动模式）耦合。激光同时驱动两个离子的跃迁，声子模式作为"中介"传递相互作用。优点是保真度极高（$\sim 99.9\%$），缺点是门速度慢（$\mu\text{s}$ 级），且难以并行化。

**中性原子（Rydberg Blockade）**：
利用 [[Rydberg-Blockade|里德堡阻塞]] 效应，通过激光脉冲将一个原子激发到里德堡态，使其与相邻原子产生强相互作用。这是本 vault 关注的核心平台，详见下一节。

### 7.3 为什么中性原子平台有独特优势？

| 特性 | 优势 | 对应的物理基础 |
|------|------|---------------|
| 可扩展性 | 可扩展至千比特 | 光镊阵列的全息生成 |
| 并行化 | 同时操作数十对原子 | 里德堡相互作用的短程性 |
| 原生 CZ 门 | 对称、简洁 | 里德堡阻塞的物理对称性 |
| 可重构 | 动态重排原子 | 光镊的独立寻址能力 |

---

## 8. 中性原子中的纠缠门：里德堡阻塞实现 CZ 门

### 8.1 物理图像

在中性原子量子计算中，纠缠门的实现依赖 [[Rydberg-Blockade|里德堡阻塞]] 效应。核心思想：

> 将一个原子激发到里德堡态（$|1\rangle \to |r\rangle$），由于两个里德堡原子之间极强的 van der Waals 相互作用（$V_{12} = C_6/R^6$），相邻原子的能级被大幅移动，无法被共振激发——这就是**阻塞**。

利用阻塞实现 [[CZ-Gate|CZ 门]] 的步骤：

1. **$\pi$ 脉冲**：将两个原子从 $\vert 1\rangle$ 激发到里德堡态 $\vert r\rangle$
2. **阻塞生效**：如果两个原子都试图被激发，由于 $V_{12} \gg \Omega$，双激发态 $\vert rr\rangle$ 被移到共振之外
3. **相位积累**：被阻塞的态（$\vert 11\rangle$）经历不同的演化路径，获得 $\pi$ 相位
4. **退激**：将原子退激回基态

最终效果：$\vert 11\rangle \to -\vert 11\rangle$，其他基态不变——这正是 CZ 门。

详细实现见 [[Rydberg-Blockade#3. 里德堡阻塞如何实现 CZ 门？]]。

### 8.2 关键参数

| 参数 | 数值 | 说明 |
|------|------|------|
| 里德堡态 | $\vert 70S_{1/2}\rangle$（$^{87}\text{Rb}$） | 主量子数 $n = 70$ |
| van der Waals 系数 | $C_6 \propto n^{11}$ | 决定相互作用强度 |
| 阻塞半径 | $R_b \approx 10\,\mu\text{m}$ | 在此距离内阻塞有效 |
| 拉比频率 | $\Omega \sim 2\pi \times 4.6\,\text{MHz}$ | 激光驱动强度 |
| CZ 门保真度 | $\sim 99.5\%$ | 已接近容错阈值 |
| 门操作时间 | $\sim 0.3\,\mu\text{s}$ | 远小于退相干时间 |

> [!info] 阻塞误差
> 理论上，当 $V_{12} \gg \Omega$ 时，阻塞几乎完美。实际错误率 $P_{\text{error}} \sim (\Omega/V_{12})^2$。当 $V_{12}/\Omega \sim 100$ 时，$P_{\text{error}} \sim 10^{-4}$。当前实验中 99.5% 的保真度主要受限于退相干、自发辐射和脉冲不完美等因素。

### 8.3 并行化：从一对原子到 60 个 qubit

里德堡相互作用是**短程力**（$\propto R^{-6}$），这使得纠缠门可以**并行执行**：

- **近邻原子**（$R \sim 6\,\mu\text{m}$）：强阻塞，可执行 CZ 门
- **次近邻原子**（$R \sim 12\,\mu\text{m}$）：相互作用减弱 $\sim 64$ 倍，可以忽略
- **远距离原子**（$R > 20\,\mu\text{m}$）：几乎无相互作用，完全独立

因此，可以将原子阵列分成多个独立的"区块"，每个区块内同时执行纠缠门，区块之间互不干扰。2023 年论文成功演示了 **32 对原子同时执行 CZ 门**，且并行执行时的保真度与单独执行时几乎相同。

---

## 9. 纠缠门的前沿：容错量子计算

### 9.1 横向纠缠门

在 [[QEC|量子纠错]] 的框架中，纠缠门需要在**逻辑层面**执行。[[Transversal-Gate|横向纠缠门]] 是一种天然容错的方案：

> 对两个码块（code block）中**对应的物理 qubit 对**分别施加 CZ 门。由于每个物理 qubit 只参与一次门操作，单个门的错误不会在码块内部传播——这就是"横向"的容错性质。

$$
\text{横向 CZ} = \text{CZ}_{11} \otimes \text{CZ}_{22} \otimes \cdots \otimes \text{CZ}_{nn}
$$

其中 $\text{CZ}_{ii}$ 是对两个码块中第 $i$ 个物理 qubit 的 CZ 门。

### 9.2 并行纠缠门与容错架构

中性原子平台的并行纠缠门能力直接支撑了 [[Transversal-Teleportation|横向隐形传态]] 协议：

1. **并行横向 CZ**：同时对所有物理 qubit 对执行 CZ 门
2. **并行 Bell 测量**：同时测量所有物理 qubit 对
3. **Pauli 校正**：根据测量结果校正逻辑态

这个"乒乓循环"可以在两个码块之间交替执行，实现**恒定熵操作**——是容错量子计算的核心工作模式。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|------|------|------|
| $e_p(U)$ | 纠缠能力 | $e_p = \overline{E(U(\vert\psi_A\rangle \otimes \vert\psi_B\rangle))}$ |
| $\text{CNOT}$ | 条件翻转门 | $\vert c\rangle\vert t\rangle \to \vert c\rangle\vert t \oplus c\rangle$ |
| $\text{CZ}$ | 条件相位门 | $\text{diag}(1,1,1,-1)$，$\vert 11\rangle \to -\vert 11\rangle$ |
| $\text{CNOT} \leftrightarrow \text{CZ}$ | 门转换 | $\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)$ |
| $e_p(\text{CNOT/CZ})$ | 最大纠缠能力 | $e_p = 1/2$ |
| $F$ | 门保真度 | $F = \langle \Psi_{\text{ideal}}\vert \rho_{\text{actual}}\vert \Psi_{\text{ideal}}\rangle$ |
| $P_{\text{error}}$ | 阻塞错误率 | $P \sim (\Omega/V_{12})^2$ |
| 横向 CZ | 容错纠缠门 | $\text{CZ}_{11} \otimes \text{CZ}_{22} \otimes \cdots \otimes \text{CZ}_{nn}$ |

---

## 🔗 相关笔记

- [[Two-Qubit-Gates]] — 两比特门的数学性质和具体类型（CNOT、CZ、SWAP）
- [[CZ-Gate]] — CZ 门的详细定义、矩阵表示、里德堡阻塞实现
- [[Two-Qubit-State-and-Entanglement]] — 纠缠态的数学描述：Schmidt 分解、Bell 态、并发度
- [[Rydberg-Blockade]] — 中性原子纠缠门的物理基础：阻塞条件、阻塞半径
- [[Single-Qubit-Gates]] — 与纠缠门交替使用的单比特门
- [[Rabi-Flopping]] — 驱动里德堡激发的脉冲技术
- [[QEC]] — 纠缠门在量子纠错中的核心角色
- [[Transversal-Gate]] — 容错的并行纠缠门方案
- [[Transversal-Teleportation]] — 利用横向纠缠门实现逻辑态传送
- [[Surface-Code]] — 表面码的 stabilizer 测量依赖纠缠门
- [[2023-parallel-gates-handout]] — 来源讲义：99.5% 并行纠缠门的实现

---

## 📝 更新记录

- 2026-06-03: 初始创建，包含纠缠门的定义、数学判据、分类、各平台实现、质量指标、容错前景
