---
aliases:
  - Two-Qubit Gates
  - 两量子比特门
  - 双比特门
  - 两比特门
tags:
  - Physics
  - Quantum
  - Gates
  - TwoQubit
  - Entanglement
  - Fundamental
date: 2026-06-02
status: In-Progress
source: "[[generall quantum 2026]]"
comprehension: "getting there"
---

# 两量子比特门（Two-Qubit Gates）

> 来源批注：量子计算基础概念 — Bluvstein et al., 2026
> 本笔记系统介绍两比特门的物理直觉、标准门集、与纠缠的关系，以及在中性原子中的物理实现。与 [[Single-Qubit-Gates]] 互补——单比特门做"精细调节"，两比特门做"建立纠缠"。

---

## 1. 为什么需要两比特门？

### 1.1 单比特门的局限

回忆 [[Single-Qubit-Gates]] 的核心结论：单比特门在 Bloch 球上做旋转，只能改变**单个 qubit** 的叠加状态。

但量子计算的真正威力来自**多个 qubit 之间的关联**。如果两个 qubit 完全独立，量子计算机就只是 $n$ 个并行的经典模拟器——没有纠缠，就没有超越经典的计算能力。

### 1.2 两比特门的核心能力：创造纠缠

两比特门做的事情是：

> **根据一个 qubit 的状态，条件性地改变另一个 qubit 的状态**——这种"条件性操作"是创造纠缠的唯一途径。

$$
\text{单比特门} \to \text{每个 qubit 独立旋转} \to \text{无纠缠}
$$
$$
\text{两比特门} \to \text{qubit 之间产生关联} \to \text{产生纠缠}
$$

> [!tip] 物理直觉：传话 vs 共谋
> 单比特门就像每个人都独立思考——各自改自己的状态。两比特门就像两个人**共谋**——A 的决定会影响 B 的行动。当 A 和 B 的行动开始互相依赖，"纠缠"就产生了。
>
> 没有共谋能力（两比特门），再多的独立思考者（单比特门）也无法产生一个真正的"秘密协议"（纠缠态）。

### 1.3 与经典门的关键区别

| | 经典两比特门（如 AND） | 量子两比特门 |
|--|---------------------|------------|
| 可逆性 | 不可逆（AND 丢失信息） | **必须可逆**（酉性） |
| 输出 | 确定性的比特值 | 可能产生**纠缠态** |
| 矩阵大小 | $2\times2$ 或查表 | $4\times4$ 酉矩阵 |

---

## 2. CNOT 门：经典-量子的桥梁

### 2.1 定义

CNOT（Controlled-NOT）门是**最基础的两比特门**，也是经典 NOT 门的量子推广。

它有两个角色：
- **控制比特**（Control）：决定"要不要翻转"
- **目标比特**（Target）：被条件性翻转

$$
\text{CNOT}|c\rangle|t\rangle = |c\rangle|t \oplus c\rangle
$$

其中 $\oplus$ 是模 2 加法（XOR）：$t \oplus c = t$ 当 $c=0$，$t \oplus c = \bar{t}$ 当 $c=1$。

### 2.2 四种输入的逐行计算

- **00**：控制比特 $c=0$，不翻转 → 输出 **00**
- **01**：控制比特 $c=0$，不翻转 → 输出 **01**
- **10**：控制比特 $c=1$，目标翻转 $0 \to 1$ → 输出 **11**
- **11**：控制比特 $c=1$，目标翻转 $1 \to 0$ → 输出 **10**

### 2.3 矩阵表示（$4\times4$）

在计算基 $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$ 下：

$$
\text{CNOT} = \begin{pmatrix} 1&0&0&0 \\ 0&1&0&0 \\ 0&0&0&1 \\ 0&0&1&0 \end{pmatrix}
$$

> [!tip] 矩阵结构的直觉
> CNOT 矩阵的左上 $2\times2$ 是单位矩阵（$c=0$ 时不翻转），右下 $2\times2$ 是 $X$ 门（$c=1$ 时翻转目标）。这正是"条件性 NOT"的数学表达。

### 2.4 CNOT 创造纠缠

对两个处于叠加态的 qubit 施加 CNOT：

$$
|+\rangle|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle)
$$

$$
\xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle
$$

这是一个 **Bell 态**（贝尔态）——两个 qubit 之间的**最大纠缠态**。它无法写成 $|\psi_A\rangle \otimes |\psi_B\rangle$ 的形式。

> [!danger] 常见误解
> 有人以为 CNOT "只翻转一个比特"，应该不创造纠缠。但关键在于：CNOT 作用在**叠加态**上时，它把"控制比特是 0"和"控制比特是 1"两种情况**同时处理**，从而在两个 qubit 的状态之间建立了**量子关联**。这种关联在测量时会表现为关联的测量结果——这就是纠缠。

---

## 3. CZ 门：中性原子的首选

### 3.1 定义与矩阵

CZ（Controlled-Z）门的作用：**当且仅当两个 qubit 都处于 $|1\rangle$ 时，给系统引入一个 $\pi$ 相位（$-1$）**。

$$
\text{CZ} = \begin{pmatrix} 1&0&0&0 \\ 0&1&0&0 \\ 0&0&1&0 \\ 0&0&0&-1 \end{pmatrix}
$$

作用规则：

$$
|00\rangle \to |00\rangle, \quad |01\rangle \to |01\rangle, \quad |10\rangle \to |10\rangle, \quad |11\rangle \to -|11\rangle
$$

### 3.2 CZ vs CNOT：对称性

> [!tip] 核心区别
> CNOT 有**控制比特**和**目标比特**的区分（不对称）。CZ 两个 qubit **地位完全平等**（对称）——谁都不"控制"谁，只是当两个都是 $|1\rangle$ 时一起翻转相位。
>
> 在中性原子中，两个原子之间的 [[Rydberg-Blockade|Rydberg 阻塞]] 天然是对称的——谁激发都会阻塞对方。因此 CZ 比 CNOT 更**物理自然**。

### 3.3 CZ = CNOT 的"相位版本"

CZ 和 CNOT 可以互相转换（只需在目标 qubit 两侧各加一个 $H$ 门）：

$$
\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)
$$

$$
\text{CZ} = (I \otimes H) \cdot \text{CNOT} \cdot (I \otimes H)
$$

**物理含义**：CZ 和 CNOT 包含相同的纠缠能力，只是"纠缠的语言"不同——CNOT 说的是"比特翻转"，CZ 说的是"相位翻转"。通过 H 门可以在两种语言之间翻译。

详细实现见 [[CZ-Gate]]。

---

## 4. SWAP 门：交换两个 qubit 的状态

### 4.1 定义

SWAP 门将两个 qubit 的状态互换：

$$
\text{SWAP}|a\rangle|b\rangle = |b\rangle|a\rangle
$$

矩阵：

$$
\text{SWAP} = \begin{pmatrix} 1&0&0&0 \\ 0&0&1&0 \\ 0&1&0&0 \\ 0&0&0&1 \end{pmatrix}
$$

### 4.2 三个 CNOT = SWAP

$$
\text{SWAP} = \text{CNOT}_{1\to2} \cdot \text{CNOT}_{2\to1} \cdot \text{CNOT}_{1\to2}
$$

> [!info] 为什么 SWAP 有用？
> 在中性原子中，原子只能与**邻近原子**做两比特门。如果两个原子相距很远，就需要用 SWAP 门"搬运"量子信息——通过一连串相邻 SWAP 将信息从 A 位置传到 B 位置。

### 4.3 SWAP 不创造纠缠

SWAP 门只是一个"重排"操作——它不创造新的纠缠，只是把已有的纠缠从一个位置移到另一个位置。这是两比特门中少数**不创造纠缠**的例子之一。

---

## 5. 四个 Bell 态：纠缠的极致

### 5.1 定义

两个 qubit 可以形成的四个**最大纠缠态**——Bell 态：

$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$

$$
|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)
$$

$$
|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)
$$

$$
|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)
$$

### 5.2 如何制备 Bell 态？

$$
|00\rangle \xrightarrow{H \otimes I} \frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)|0\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) = |\Phi^+\rangle
$$

> 制备 Bell 态 = **一个 H 门 + 一个 CNOT 门**。这是量子计算中最基础的纠缠制备线路。

### 5.3 Bell 态的性质

| 性质 | 含义 |
|------|------|
| 不可分离 | 不能写成 $\|\psi_A\rangle \otimes \|\psi_B\rangle$ |
| 最大纠缠 | 对其中一个 qubit 做任意操作，另一个 qubit 的状态**完全确定** |
| 测量关联 | 测量 A 得到 0，则 B 也一定是 0（Bell 态 $\|\Phi^+\rangle$）；反之亦然 |
| 不可克隆 | 不能复制 Bell 态（量子不可克隆定理） |

> [!question] 思考题
> 如果 Alice 和 Bob 各持有一个 Bell 态中的一个 qubit，Alice 对她的 qubit 做 X 门，Bob 测量自己的 qubit 会看到什么变化？

---

## 6. 两比特门的 Bloch 球图像

### 6.1 CNOT 门的几何含义

CNOT 门对**控制比特**不做任何操作，只条件性地翻转**目标比特**。在 Bloch 球上：

- 如果控制比特在 $|0\rangle$（北极）→ 目标比特的 Bloch 球**不动**
- 如果控制比特在 $|1\rangle$（南极）→ 目标比特的 Bloch 球**绕 $x$ 轴翻转 $\pi$**

### 6.2 CZ 门的几何含义

CZ 门在 Bloch 球上的效果更微妙——它不改变 Bloch 球上的点的位置（因为三个基态 $|00\rangle, |01\rangle, |10\rangle$ 都不变），只给 $|11\rangle$ 加一个 $-1$ 相位。这种"只改相位不改位置"的效果在单 qubit Bloch 球上看不见，需要**两个 Bloch 球联合看**才能理解——这也是纠缠的本质：单个 qubit 的 Bloch 球图像无法完全描述两 qubit 的状态。

> [!warning] 单 Bloch 球的局限
> 对于纠缠态，**每个 qubit 各自的 Bloch 球图像都是"混合态"**（在球内部），即使整体是纯态。这是因为纠缠"隐藏"了单 qubit 无法看到的量子关联。只有看整个两 qubit 系统的密度矩阵，才能看到完整的纠缠结构。

---

## 7. 通用量子计算：单比特门 + 两比特门

### 7.1 通用门集

**Solovay-Kitaev 定理**的完整版本：

> $\{H, T, \text{CNOT}\}$（或等价地 $\{H, T, \text{CZ}\}$）构成**通用门集**——任何量子算法都可以用这些门的组合以任意精度近似。

其中：
- **H + T**（单比特门）：负责所有单 qubit 旋转和相位调节
- **CNOT 或 CZ**（两比特门）：负责建立 qubit 之间的纠缠

### 7.2 量子线路的标准结构

```
量子线路 = [单比特层] → [两比特层] → [单比特层] → [两比特层] → ... → [测量]
              H, T, Rx    CZ/CNOT     H, T, Rx     CZ/CNOT           | 测量
```

| 角色 | 由谁完成 | 具体操作 |
|------|---------|---------|
| 状态初始化 | 单比特门 | $\|0\rangle \to \|+\rangle$（H 门） |
| 算法逻辑 | 单比特门 | H、T、$R_z$ 组合执行量子算法步骤 |
| 纠缠建立 | 两比特门 | CZ 或 CNOT 产生 qubit 间的量子关联 |
| 解码 | 单比特门 | H 门将叠加态转回计算基以便测量 |
| 测量 | — | 在计算基下测量，获得经典输出 |

> [!tip] "单-双-单-双" 的节奏
> 量子线路的编排就像一首"音乐"：单比特门是旋律（每个乐器单独演奏），两比特门是和声（乐器之间的配合）。旋律和和声交替出现，共同构成完整的量子算法。

### 7.3 T 门数量：资源开销的度量

在容错量子计算中，**T 门的数量**（T-count）是衡量线路复杂度的核心指标——每个 T 门都需要一次 magic state distillation（[[Transversal-Teleportation|Gate Teleportation]]）。优化量子线路的一个重要目标就是**减少 T 门数量**。

两比特门（CZ/CNOT）本身不需要 magic state（它们可以横向实现），但它们的**数量**也很重要，因为两比特门的物理保真度通常低于单比特门。

---

## 8. 在中性原子中的物理实现

### 8.1 CZ 门：里德堡阻塞

在 [[Optical-Tweezer-Arrays]] 平台中，CZ 门通过 [[Rydberg-Blockade|Rydberg 阻塞]] 直接实现：

$$
|11\rangle \xrightarrow{\text{阻塞}} -|11\rangle
$$

具体步骤：
1. 对两个原子施加 $\pi$ 脉冲，将 $|1\rangle$ 激发到里德堡态 $|r\rangle$
2. 由于阻塞，如果两个都在 $|r\rangle$，相互作用阻止第二个激发，积累 $\pi$ 相位
3. 对两个原子施加 $2\pi$ 脉冲，退激回基态
4. 结果：$|11\rangle$ 获得 $-1$ 相位 → CZ 门

详细实现见 [[CZ-Gate]] 和 [[Rydberg-Blockade]]。

### 8.2 性能参数

| 参数 | 数值 | 说明 |
|------|------|------|
| CZ 门保真度 | $\sim 99.5\%$ | 受阻塞不完美和退相干限制 |
| 门操作时间 | $\sim 0.3\,\mu\text{s}$ | 远小于退相干时间 |
| 并行度 | 可同时对多对原子施加 | 全局激光同时驱动所有原子对 |

### 8.3 CNOT 门的实现

由于中性原子的 CZ 门是"原生门"，CNOT 需要通过 H 门转换：

$$
\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)
$$

即：CNOT = H 门 + CZ 门 + H 门（多两步单比特操作）。

> [!info] 编译优势
> 由于 CZ 是中性原子的原生门，编译量子线路时应该**优先使用 CZ 门**而不是 CNOT 门，以减少额外的 H 门开销。这也是为什么中性原子平台的线路编译器通常以 CZ 为基础构建。

---

## 📐 核心公式摘要

- **$\text{CNOT}$**：Controlled-NOT 门 — $|c\rangle|t\rangle \to |c\rangle|t \oplus c\rangle$
- **$\text{CZ}$**：Controlled-Z 门 — $\text{diag}(1,1,1,-1)$，$|11\rangle \to -|11\rangle$
- **$\text{SWAP}$**：交换门 — $|a\rangle|b\rangle \to |b\rangle|a\rangle$
- **CNOT $\leftrightarrow$ CZ**：门转换 — $\text{CNOT} = (I \otimes H) \cdot \text{CZ} \cdot (I \otimes H)$
- **$|\Phi^+\rangle$**：Bell 态 — $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
- **SWAP 分解** — $\text{SWAP} = \text{CNOT}_{12} \cdot \text{CNOT}_{21} \cdot \text{CNOT}_{12}$


---

## 🔗 相关笔记

- [[Two-Qubit-State-and-Entanglement]] — 两 qubit 态的结构、纠缠判据、并发度、纠缠熵
- [[Single-Qubit-Gates]] — 与两比特门组合构成通用门集的单比特门
- [[CZ-Gate]] — CZ 门的详细性质、里德堡阻塞实现
- [[Rydberg-Blockade]] — CZ 门的物理实现机制
- [[Rabi-Flopping]] — 两比特门中使用的 $\pi$ 脉冲基础
- [[Optical-Tweezer-Arrays]] — 两比特门的硬件平台
- [[Transversal-Gate]] — 并行施加 CZ 门的容错方案
- [[Transversal-Teleportation]] — 利用横向 CZ 实现逻辑态传送
- [[QEC]] — 两比特门在量子纠错中的角色

## 📝 更新记录

- 2026-06-02: 初始创建，包含 CNOT、CZ、SWAP、Bell 态、通用门集、中性原子实现
