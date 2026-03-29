---
aliases: [Transversal Gate, 横向纠缠门, Transversal Entangling Gate, 横向门]
tags: [Physics, Quantum, Gates, FaultTolerant, ErrorCorrection]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
---

# 横向纠缠门（Transversal Entangling Gate）

> 来源批注：*"transversal entangling gate"* — Bluvstein et al., 2026, p.49

## 1. 什么是横向门（Transversal Gate）？

**横向（transversal）**是容错量子计算中的一个关键概念：

> 若一个逻辑门可以**逐个物理比特独立操作**（即不需要不同码块内的物理 qubit 之间相互作用），则称其为横向门。

形式化地，对逻辑 qubit $L$ 的横向门 $\bar{U}$：

$$
\bar{U} = U^{\otimes n}
$$

即对 $n$ 个物理 qubit **同时各自施加单体操作** $U$。

## 2. 为什么横向门天然容错？

假设某个物理 qubit 上的 $U$ 出错变成 $U \cdot E$（$E$ 是错误算符）。

- **普通门**：错误可能通过门操作**扩散**到多个 qubit，导致无法纠正
- **横向门**：每个物理 qubit 独立操作，**单个 qubit 的错误不会传播到其他 qubit**

$$
\bar{U}|E_i\rangle = U_1 \otimes \cdots \otimes (U\cdot E)_i \otimes \cdots \otimes U_n |\psi_L\rangle
$$

即错误仍然局限在第 $i$ 个物理 qubit 上，[[量子纠错 (QEC)]] 可以处理。

## 3. 横向 CZ 门

**论文中的横向纠缠门**是横向 [[CZ门 (CZ Gate)]] 的推广：对两个逻辑 qubit $A, B$ 的所有对应物理 qubit 对 $(a_i, b_i)$ 同时施加 CZ 门：

$$
\overline{\text{CZ}} = \text{CZ}^{(1)} \otimes \text{CZ}^{(2)} \otimes \cdots \otimes \text{CZ}^{(n)}
$$

这等效于逻辑层面执行一次 CZ 门，同时保持容错性。

## 4. 横向电路的局限性：Eastin-Knill 定理

> **Eastin-Knill 定理**：对任何非平凡的量子纠错码，**不存在通用的横向门集合**。

即横向门只能实现部分逻辑门，不能覆盖通用计算所需的全部门集（如 $T$ 门）。

这就是为什么论文使用**隐形传态（teleportation）**来补充实现非横向门（参见 [[深度电路执行 (Deep-Circuit Execution)]]）。

## 5. 在中性原子中的实现

[[光镊阵列 (Optical Tweezer Arrays)]] 的优势：可以在物理上将两个码块的对应原子**并排放置**，同时对所有原子对施加 [[里德堡阻塞 (Rydberg Blockade)]] 介导的 CZ 门，从而以并行方式实现横向纠缠门，大幅减少操作时间和退相干。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $\bar{U}$ | 横向逻辑门 | $\bar{U} = U^{\otimes n}$ |
| $\overline{\text{CZ}}$ | 横向 CZ 门 | $\bigotimes_i \text{CZ}^{(i)}$（对应物理 qubit 对） |
