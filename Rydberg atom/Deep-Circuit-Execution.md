---
aliases:
  - Deep-Circuit Execution
  - 深度电路执行
  - 深层电路
  - 恒定熵计算
tags:
  - Physics
  - Quantum
  - FaultTolerant
  - Architecture
  - DeepCircuit
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "don't understand"
---

# 深度电路执行（Deep-Circuit Execution）

> 来源批注：*"deep-circuit execution"* — Bluvstein et al., 2026, p.39
> Better Notes 中已有 DeepSeek 详细解答，本笔记提取物理核心并形式化。

## 1. 问题背景

**深度电路执行**的核心挑战：量子算法往往需要执行深度很深的电路（数百甚至数千个逻辑门层），期间物理错误会不断累积。

定义**电路深度** $D$ 为串行门操作的总层数。对于物理错误率 $p$，在 $D$ 层操作后：

$$
p_{\text{累积}} \approx 1 - (1-p)^D \approx pD \quad (p \ll 1)
$$

在无容错保护时，$D \gtrsim 1/p$ 后计算将失败。

> [!tip] 物理直觉
> 想象一个传话游戏：每传一次就可能出错。传 10 次可能还行，传 1000 次就完全走样了。深度电路执行就是要解决"传话太长会走样"的问题——通过不断"刷新"信息来阻止错误累积。

## 2. 目标：恒定熵（Constant Entropy）

论文的核心目标是维持系统在**恒定熵**状态下运行：

> 处理器的"熵"（即错误信息量、无序度）在整个深度电路执行过程中保持不变，不积累。

$$
S_{\text{逻辑}}(t) = \text{const} \quad \forall t \in [0, T_{\text{circuit}}]
$$

## 3. 核心机制：逻辑横向隐形传态

实现恒定熵的关键是**逻辑 [[Transversal-Teleportation]]**——将标准量子隐形传态推广到容错逻辑层面的协议。

### 3.1 为什么需要"横向"版本？

标准量子隐形传态传送的是**单个物理 qubit** 的态。但在容错计算中，我们操作的是**逻辑 qubit**（由 $n$ 个物理 qubit 编码的纠错码块）。横向隐形传态的核心思想是：

> 对两个逻辑码块的每一对对应物理 qubit 同时执行 Bell 操作，将**整个逻辑态**从码块 $A$ 传送到码块 $B$，同时利用横向操作的特性**阻止物理错误跨码块传播**。

### 3.2 协议流程

**Step 1 — 系统设置**：将处理器分为 $A$、$B$ 两组逻辑 qubit 码块。$A$ 承载待传送的逻辑态 $|\psi\rangle_L$ 及积累的物理错误，$B$ 处于已知参考态。

**Step 2 — 横向 CZ 门（纠缠建立）**：对所有对应物理 qubit 对 $(a_i, b_i)$ 施加 CZ 门：

$$
\overline{\text{CZ}} = \bigotimes_{i=1}^{n} \text{CZ}^{(a_i, b_i)}
$$

由于横向操作的逐比特独立性，$A$ 上的物理错误**不会传播到 $B$**——这是容错性的核心保证。

**Step 3 — 横向 Bell 测量（逻辑传送）**：对 $A$ 码块的所有物理 qubit 执行 Bell 基测量。效果：

$$
|\psi\rangle_L^{(A)} \otimes |\text{ref}\rangle_L^{(B)} \xrightarrow{\overline{\text{CZ}} + \text{Bell测量}_A} |\psi\rangle_L^{(B)} + (\text{错误局限在 } A)
$$

逻辑信息干净地传到 $B$，物理错误留在被测量的 $A$ 中。

**Step 4 — 重置 $A$**：移除 $A$ 中的旧原子，补充新制备的低熵原子，重新初始化为参考态。

### 3.3 乒乓循环：恒定熵的实现

$A$、$B$ 两组码块交替充当"发送方"和"接收方"，形成循环：

```
轮次 1: A(脏) →[横向CZ+测量]→ B(干净)    A 重置
轮次 2: B(脏) →[横向CZ+测量]→ A(干净)    B 重置
轮次 3: A(脏) →[横向CZ+测量]→ B(干净)    A 重置
  ⋮
```

每一轮，物理错误不断产生，但通过隐形传态被"清除"到重置的码块中。因此逻辑熵始终保持恒定。

> [!warning] 常见误解
> 恒定熵不是说"没有错误产生"——错误仍然在每一步产生。关键在于**产生的速率等于清除的速率**，就像浴缸的进水和出水流量平衡时水位保持不变。

> 详细的数学推导、错误隔离证明、Gate Teleportation 推广以及中性原子实验实现，参见 [[Transversal-Teleportation]]。

## 4. 流程图

```
[A 组：逻辑态 + 积累错误]
       ↓ 横向 CZ（纠缠）
[A ⊗ B 纠缠态]
       ↓ 测量 A（syndrome + 逻辑比特）
[B 组：干净逻辑态]  +  [A 组：包含物理错误]
       ↓                    ↓
  继续计算              重置（冷却、补原子）
       ↓                    ↓
[B 组 → 下一轮的"A 组"]  [A → 下一轮的"B 组"]
```

## 5. 实验演示

论文在 **27 层**电路中演示了 [[Surface-Code]] 和 编码下的逻辑簇态制备：

- **逻辑关联**在 27 层后仍保持（说明逻辑信息干净传播）
- **物理 stabilizer 错误关联**随距离指数衰减（说明错误被有效清除）

这验证了"深度电路执行"在恒定熵下运行的可行性。

> [!info] 实验意义
> 27 层是当前技术的一个里程碑。虽然实际量子算法可能需要数百到数千层，但 27 层的验证证明了**恒定熵运行在原理上是可行的**——这是通向实用容错量子计算的关键一步。

## 6. 与中性原子体系的关联

[[Optical-Tweezer-Arrays]] 的**可重构性**（reconfigurable）是实现上述流程的关键：
- 原子可以在计算过程中物理移动，将 A、B 两组并排以执行横向 CZ
- 测量后的原子可以被移走并替换为新制备的低熵原子
- 整个过程可以在 [[Rydberg-Blockade]] 介导的高保真度门下实时进行

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $D$ | 电路深度 | 串行门操作层数 |
| $S_{\text{逻辑}}$ | 逻辑系统熵 | $S = \text{const}$（恒定熵运行目标） |
| $\overline{\text{CZ}}$ | 横向 CZ 门 | $\bigotimes_{i=1}^{n} \text{CZ}^{(a_i, b_i)}$ |
| 逻辑传送 | 核心效果 | $\|\psi\rangle_L^{(A)} \xrightarrow{\text{CZ+Bell}} \|\psi\rangle_L^{(B)}$ |
| 错误隔离 | 容错性保证 | $E_A$ 只作用于 $A$，不传播到 $B$ |

---

## 🔗 相关笔记

- [[Transversal-Teleportation]] — 恒定熵运行的核心机制详解
- [[Transversal-Gate]] — 横向 CZ 门的容错性来源
- [[QEC]] — 纠错码框架
- [[Surface-Code]] — 论文使用的具体纠错码
- [[Optical-Tweezer-Arrays]] — 中性原子平台的硬件基础
- [[Rydberg-Blockade]] — 介导高保真度 CZ 门的物理机制

## 📝 更新记录

- 2026-03-29: 初始创建
- 2026-06-01: 完善横向隐形传态章节，添加 Obsidian Callouts 标注，优化可读性
