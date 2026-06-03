---
aliases:
  - Two-Qubit State
  - 双量子比特态
  - 纠缠态
  - Entanglement
  - Concurrence
  - 并发度
tags:
  - Physics
  - Quantum
  - Entanglement
  - TwoQubit
  - Fundamental
date: 2026-06-02
status: WIP
source: "[[generall quantum 2026]]"
comprehension: "getting there"
---

# 双量子比特态与纠缠（Two-Qubit State and Entanglement）

> 来源批注：量子信息基础概念
> 本笔记专门讨论**两个 qubit 组成的量子态**——它的数学结构、什么时候产生纠缠、如何量化纠缠。与 [[Two-Qubit-Gates]]（讨论"做什么操作"）互补，这里讨论"态本身长什么样"。

---

## 1. 两个 qubit 的态空间

### 1.1 从一维到四维

一个 qubit 的态生活在**二维**复希尔伯特空间 $\mathcal{H}_1 = \mathbb{C}^2$ 中。

两个 qubit 的态生活在**四维**复希尔伯特空间 $\mathcal{H}_2 = \mathbb{C}^2 \otimes \mathbb{C}^2 = \mathbb{C}^4$ 中。

计算基有四个：

$$
|00\rangle = \begin{pmatrix}1\\0\\0\\0\end{pmatrix}, \quad |01\rangle = \begin{pmatrix}0\\1\\0\\0\end{pmatrix}, \quad |10\rangle = \begin{pmatrix}0\\0\\1\\0\end{pmatrix}, \quad |11\rangle = \begin{pmatrix}0\\0\\0\\1\end{pmatrix}
$$

一般态是这四个基态的线性叠加：

$$
|\Psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle
$$

归一化条件：$|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2 = 1$。

> [!tip] 复数参数的个数
> 四个复数系数 = **8 个实参数**。减去归一化约束（1 个）和全局相位（1 个），一个两 qubit 纯态由 **6 个实参数**唯一确定。相比之下，一个单 qubit 纯态只有 2 个实参数（$\theta$ 和 $\phi$）。多出来的 4 个参数正是**纠缠**的自由度。

### 1.2 Tensor Product 结构

两 qubit 空间不是简单的"两个空间加在一起"，而是通过 [[Tensor-Product|张量积]] 组合在一起：

$$
\mathcal{H}_2 = \mathcal{H}_A \otimes \mathcal{H}_B
$$

这种张量积结构是理解纠缠的数学基础——纠缠态正是**无法分解为张量积**的态。

---

## 2. 什么态不是纠缠的？——直积态

### 2.1 定义

如果一个两 qubit 态可以写成两个单 qubit 态的张量积：

$$
|\Psi\rangle = |\psi_A\rangle \otimes |\psi_B\rangle = (a|0\rangle + b|1\rangle) \otimes (c|0\rangle + d|1\rangle)
$$

$$
= ac|00\rangle + ad|01\rangle + bc|10\rangle + bd|11\rangle
$$

则称 $|\Psi\rangle$ 为**直积态**（product state）或**可分离态**（separable state）。

### 2.2 直积态的特征

展开后，四个系数之间存在一个关键约束：

$$
\alpha \cdot \delta = ac \cdot bd = abcd
$$
$$
\beta \cdot \gamma = ad \cdot bc = abcd
$$

所以：

$$
\boxed{\alpha\delta = \beta\gamma}
$$

> [!tip] 物理直觉
> 直积态意味着两个 qubit **完全独立**——知道 qubit A 的状态不能提供任何关于 qubit B 的信息。它们就像两个互不相关的硬币。

### 2.3 例子

$|00\rangle$：直积态，$\alpha = 1$，其余为 0，$\alpha\delta = 0 = \beta\gamma$ ✓

$\frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle) = |+\rangle|+\rangle$：直积态，$\alpha = \beta = \gamma = \delta = 1/2$，$\alpha\delta = 1/4 = \beta\gamma$ ✓

---

## 3. 纠缠态：无法分解的量子关联

### 3.1 定义

> **纠缠态**（entangled state）：不能写成直积形式 $|\psi_A\rangle \otimes |\psi_B\rangle$ 的两 qubit 量子态。

数学判据：当且仅当 $\alpha\delta \neq \beta\gamma$ 时，$|\Psi\rangle$ 是纠缠态。

### 3.2 最简单的纠缠态：Bell 态

$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$

检验：$\alpha = 1/\sqrt{2}$，$\delta = 1/\sqrt{2}$，$\beta = 0$，$\gamma = 0$

$$
\alpha\delta = \frac{1}{2} \neq 0 = \beta\gamma
$$

**纠缠！**

### 3.3 纠缠的物理含义

对 $|\Phi^+\rangle$ 做测量：

- 如果 Alice 测量她的 qubit 得到 0，则 Bob 的 qubit **瞬间坍缩到** $|0\rangle$
- 如果 Alice 测量得到 1，则 Bob 的 qubit **瞬间坍缩到** $|1\rangle$

无论 Alice 和 Bob 相距多远——这就是 Einstein 所说的"鬼魅般的超距作用"（spooky action at a distance）。

> [!warning] 纠缠 ≠ 超光速通信
> 虽然 Alice 的测量会"瞬间影响" Bob 的态，但 Alice **无法控制**自己测量得到 0 还是 1（概率各 50%）。因此她无法利用纠缠向 Bob 传递任何信息。量子纠缠不违反相对论。

### 3.4 四个 Bell 态

两 qubit 空间中的四个**最大纠缠态**：

- $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
- $|\Phi^-\rangle = \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle)$
- $|\Psi^+\rangle = \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle)$
- $|\Psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$

它们构成四维希尔伯特空间的一组**正交完备基**——任何两 qubit 态都可以用 Bell 态展开。

---

## 4. 如何判断一个态是否纠缠？

### 4.1 简单判据（两 qubit 纯态）

对 $|\Psi\rangle = \alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$：

$$
\text{纠缠判据}：\quad \alpha\delta - \beta\gamma \neq 0
$$

### 4.2 Peres-Horodecki 判据（更一般的情况）

对**混合态**（密度矩阵 $\rho$），需要用**部分转置**（partial transpose）判据：

对 $\rho$ 做 partial transpose（只转置 B 的指标），得到 $\rho^{T_B}$。如果 $\rho^{T_B}$ 有负本征值，则态是纠缠的。

> [!info] 什么时候需要密度矩阵？
> 纯态 $|\Psi\rangle$ 可以直接用波函数分析。但如果系统与环境有相互作用（退相干），态会变成**混合态**——需要用密度矩阵 $\rho$ 描述。在实际 Rydberg 实验中，退相干不可避免，所以混合态纠缠判据也很重要。

---

## 5. 量化纠缠：并发度与 von Neumann 熵

### 5.1 为什么需要量化？

不是所有纠缠都一样"强"。例如：

- $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$：最大纠缠
- $0.99|00\rangle + 0.01|11\rangle$：很弱的纠缠

我们需要一个**数值指标**来衡量纠缠的"强度"。

### 5.2 并发度（Concurrence）

对两 qubit 纯态 $|\Psi\rangle$，并发度定义为：

$$
C(|\Psi\rangle) = 2|\alpha\delta - \beta\gamma|
$$

**取值范围**：

- $C = 0$：直积态（无纠缠）
- $C = 1$：最大纠缠态（如 Bell 态）

**例子**：

$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$

$$
C = 2\left|\frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} - 0 \cdot 0\right| = 2 \cdot \frac{1}{2} = 1 \quad \text{（最大纠缠）}
$$

$0.99|00\rangle + 0.01|11\rangle$（近似直积态）

$$
C = 2|0.99 \times 0.01 - 0| = 2 \times 0.0099 \approx 0.02 \quad \text{（很弱的纠缠）}
$$

### 5.3 纠缠熵（Entanglement Entropy）

另一个常用的量化方法是**von Neumann 熵**：

对纯态 $|\Psi\rangle_{AB}$，先求 qubit A 的**约化密度矩阵**（reduced density matrix）：

$$
\rho_A = \text{Tr}_B(|\Psi\rangle\langle\Psi|)
$$

然后计算：

$$
S(\rho_A) = -\text{Tr}(\rho_A \log_2 \rho_A)
$$

**物理含义**：$S$ 衡量的是"如果我们只知道 qubit A 的状态，我们对整个系统有多不确定"。$S = 0$ 说明 A 完全确定（无纠缠），$S = 1$ 说明 A 完全不确定（最大纠缠）。

**例子**：

$|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$

$$
\rho_A = \text{Tr}_B\left(\frac{1}{2}(|00\rangle+|11\rangle)(\langle 00|+\langle 11|)\right) = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1| = \frac{I}{2}
$$

$$
S(\rho_A) = -\frac{1}{2}\log_2\frac{1}{2} - \frac{1}{2}\log_2\frac{1}{2} = 1 \quad \text{（最大纠缠熵）}
$$

> [!tip] Concurrence vs 纠缠熵
> - **并发度 $C$**：直观、计算简单，适用于两 qubit 纯态和混合态
> - **纠缠熵 $S$**：更一般，适用于任意 bipartite 系统，与量子信息论联系紧密
> - 对两 qubit 纯态：$C = 1$ 和 $S = 1$ 都表示最大纠缠

### 5.4 直积态 vs 纠缠态的判别总结

| 判据 | 直积态（可分离） | 纠缠态 |
|------|------------|--------|
| 数学条件 | $\alpha\delta = \beta\gamma$ | $\alpha\delta \neq \beta\gamma$ |
| 并发度 | $C = 0$ | $0 < C \leq 1$ |
| 纠缠熵 | $S = 0$ | $0 < S \leq 1$ |
| 约化密度矩阵 | 本征值为 0 和 1（纯态） | 本征值在 0 和 1 之间（混合态） |
| 物理含义 | 两个 qubit 独立 | 两个 qubit 量子关联 |

---

## 6. Schmidt 分解：纠缠的数学本质

### 6.1 定理

任何两 qubit 纯态 $|\Psi\rangle_{AB}$ 都可以写成：

$$
|\Psi\rangle_{AB} = \lambda_1|u_1\rangle_A|v_1\rangle_B + \lambda_2|u_2\rangle_A|v_2\rangle_B
$$

其中 $\lambda_1, \lambda_2 \geq 0$，$\lambda_1^2 + \lambda_2^2 = 1$，$\{|u_i\rangle\}$ 和 $\{|v_i\rangle\}$ 分别是 A 和 B 的正交归一基。

### 6.2 Schmidt 系数与纠缠

- **$\lambda_2 = 0$**：态是直积态（$|\Psi\rangle = |u_1\rangle|v_1\rangle$），无纠缠
- **$\lambda_1 = \lambda_2 = 1/\sqrt{2}$**：最大纠缠态，$S = 1$
- **一般情况**：$0 < \lambda_2 < 1/\sqrt{2}$，中等纠缠

纠缠熵直接由 Schmidt 系数决定：

$$
S = -\lambda_1^2\log_2\lambda_1^2 - \lambda_2^2\log_2\lambda_2^2
$$

> [!info] Schmidt 分解的物理意义
> Schmidt 分解把纠缠态写成了"配对叠加"的形式——$\lambda_1|u_1\rangle|v_1\rangle + \lambda_2|u_2\rangle|v_2\rangle$。$\lambda_i$ 衡量了每一对基态的"权重"。如果所有权重集中在一对上，态接近直积态；如果权重均匀分布，态高度纠缠。

---

## 7. 约化密度矩阵与"局部看起来混合"

### 7.1 从纯态到混合态

这是量子纠缠最反直觉的特性之一：

> **整体是纯态，局部看是混合态**。

对 $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$：

- **整体**：$|\Phi^+\rangle$ 是纯态（$S_{\text{total}} = 0$）
- **只看 A**：$\rho_A = I/2$ 是完全混合态（$S_A = 1$）
- **只看 B**：$\rho_B = I/2$ 是完全混合态（$S_B = 1$）

### 7.2 为什么这很重要？

这意味着：

- 虽然整体系统处于确定的纯态 $|\Phi^+\rangle$
- 但如果你只看其中一个 qubit，它**看起来完全是随机的**（50-50 混合）
- 只有同时看两个 qubit，才能发现它们之间的关联

> [!question] 思考题
> 如果一个两 qubit 态的约化密度矩阵 $\rho_A$ 是纯态（$\rho_A^2 = \rho_A$），这说明什么？（提示：这说明 $|\Psi\rangle_{AB}$ 一定是直积态。）

---

## 8. 在 Rydberg 原子中的纠缠

### 8.1 纠缠的制备

在 [[Optical-Tweezer-Arrays]] 中，两个相邻原子通过 [[CZ-Gate|CZ 门]]（由 [[Rydberg-Blockade|Rydberg 阻塞]] 介导）建立纠缠：

$$
|00\rangle \xrightarrow{H \otimes I} \frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)|0\rangle \xrightarrow{\text{CNOT}} \frac{1}{\sqrt{2}}(|00\rangle+|11\rangle) = |\Phi^+\rangle
$$

即：先对第一个原子做 H 门（制备叠加态），再做 CNOT（建立关联），就得到 Bell 态。

### 8.2 实验中的纠缠度量

实验中通常通过**量子态层析**（quantum state tomography）重建密度矩阵 $\rho$，然后计算：

- **并发度** $C(\rho)$
- **纠缠熵** $S(\rho_A)$

Bluvstein et al. (2026) 报道的实验中，通过 27 层深度电路验证了纠缠态的逻辑关联保持。

### 8.3 并发度的实验测量

实验上，可以通过测量以下四个期望值来推断并发度：

- $\langle XX \rangle$、$\langle YY \rangle$、$\langle ZZ \rangle$、$\langle II \rangle$

对 Bell 态 $|\Phi^+\rangle$：$\langle XX \rangle = 1$，$\langle YY \rangle = -1$，$\langle ZZ \rangle = 1$

> [!info] 为什么测量并发度很重要？
> 并发度直接告诉我们"纠缠有多强"。在容错量子计算中，纠缠是资源——我们需要确认量子门确实产生了预期的纠缠量，而不是被噪声削弱了。并发度的实验测量是验证量子处理器性能的关键指标。

---

## 📐 核心公式摘要

- **$|\Psi\rangle$**：两 qubit 一般态 — $\alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$
- **直积态判据**：可分离条件 — $\alpha\delta = \beta\gamma$
- **$C$**：并发度（Concurrence） — $C = 2|\alpha\delta - \beta\gamma|$，$C \in [0,1]$
- **$\rho_A$**：约化密度矩阵 — $\rho_A = \text{Tr}_B(|\Psi\rangle\langle\Psi|)$
- **$S$**：纠缠熵（von Neumann） — $S = -\text{Tr}(\rho_A \log_2 \rho_A)$，$S \in [0,1]$
- **Schmidt 分解** — $|\Psi\rangle_{AB} = \lambda_1|u_1\rangle|v_1\rangle + \lambda_2|u_2\rangle|v_2\rangle$


---

## 🔗 相关笔记

- [[Qubit-State-and-Superposition]] — 单 qubit 态的叠加与相位
- [[Two-Qubit-Gates]] — 制备纠缠的量子门操作（CNOT、CZ）
- [[CZ-Gate]] — Rydberg 原子中 CZ 门的具体实现
- [[Rydberg-Blockade]] — 里德堡阻塞：CZ 门的物理机制
- [[Tensor-Product]] — 张量积：两 qubit 态空间的数学基础
- [[Single-Qubit-Gates]] — 单 qubit 门：纠缠前的态制备
- [[QEC]] — 纠缠在量子纠错中的角色
- [[Transversal-Teleportation]] — 利用纠缠实现逻辑态传送

## 📝 更新记录

- 2026-06-02: 初始创建，系统讲解两 qubit 态空间、纠缠判据、并发度、纠缠熵、Schmidt 分解、约化密度矩阵
