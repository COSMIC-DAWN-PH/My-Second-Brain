---
aliases: [Deep-Circuit Execution, 深度电路执行, 深层电路, 恒定熵计算]
tags: [Physics, Quantum, FaultTolerant, Architecture, DeepCircuit]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
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

## 2. 目标：恒定熵（Constant Entropy）

论文的核心目标是维持系统在**恒定熵**状态下运行：

> 处理器的"熵"（即错误信息量、无序度）在整个深度电路执行过程中保持不变，不积累。

$$
S_{\text{逻辑}}(t) = \text{const} \quad \forall t \in [0, T_{\text{circuit}}]
$$

## 3. 核心机制：逻辑横向隐形传态

实现恒定熵的关键是**逻辑横向隐形传态（Transversal Teleportation）**：

**思路**：
1. 将系统分为 A、B 两组逻辑 qubit 码块
2. 利用 [[横向纠缠门 (Transversal Gate)]]（横向 CZ 门）在 A、B 之间创建纠缠
3. 测量 A 组（syndrome + 逻辑测量），将逻辑信息**传送**到 B 组
4. **关键**：物理错误留在 A 组，逻辑信息干净地传到 B 组

$$
|\psi_{\text{logical}}\rangle_A \xrightarrow{\text{纠缠+测量}} |\psi_{\text{logical}}\rangle_B + (\text{错误留在 A 组})
$$

5. 重置 A 组（重新冷却、补充原子、重新初始化）→ 低熵状态
6. 用重置后的 A 组继续下一轮隐形传态

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

论文在 **27 层**电路中演示了 [[表面码 (Surface Code)]] 和 编码下的逻辑簇态制备：

- **逻辑关联**在 27 层后仍保持（说明逻辑信息干净传播）
- **物理 stabilizer 错误关联**随距离指数衰减（说明错误被有效清除）

这验证了"深度电路执行"在恒定熵下运行的可行性。

## 6. 与中性原子体系的关联

[[光镊阵列 (Optical Tweezer Arrays)]] 的**可重构性**（reconfigurable）是实现上述流程的关键：
- 原子可以在计算过程中物理移动，将 A、B 两组并排以执行横向 CZ
- 测量后的原子可以被移走并替换为新制备的低熵原子
- 整个过程可以在 [[里德堡阻塞 (Rydberg Blockade)]] 介导的高保真度门下实时进行

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $D$ | 电路深度 | 串行门操作层数 |
| $S_{\text{逻辑}}$ | 逻辑系统熵 | $S = \text{const}$（恒定熵运行目标） |
| 逻辑隐形传态 | 核心机制 | $|\psi\rangle_A \xrightarrow{\text{CZ+测量}} |\psi\rangle_B$ |
