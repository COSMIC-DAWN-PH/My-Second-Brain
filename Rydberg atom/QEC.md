---
aliases: [QEC, Quantum Error Correction, 量子纠错码]
tags: [Physics, Quantum, ErrorCorrection, FaultTolerant]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "vague"
---

# 量子纠错 (Quantum Error Correction, QEC)

> 来源批注：*"QEC works in practice"* — Bluvstein et al., 2026, p.39

## 1. 为什么需要量子纠错？

量子比特（qubit）极易受到环境干扰，导致两类物理错误：
- **比特翻转错误（bit-flip）**：$|0\rangle \to |1\rangle$ 或反之
- **相位翻转错误（phase-flip）**：$|+\rangle \to |-\rangle$

经典计算机通过**重复冗余**（如存三份）来纠错。但量子力学的**不可克隆定理**禁止直接复制量子态，因此必须用更聪明的方法。

> [!tip] 不可克隆定理迫使编码创新
> 经典冗余（复制三份）在量子世界行不通。QEC 的核心洞察是：**不是复制信息，而是将信息"分散"到多个物理比特的纠缠态中**。这样错误检测不会暴露原始量子态。

## 2. 核心思路：将信息编码在多个物理比特中

QEC 的关键在于：**用多个物理 qubit 共同编码一个逻辑 qubit**。

$$
|\psi\rangle_L = \alpha|0\rangle_L + \beta|1\rangle_L \quad \text{（逻辑态）}
$$

以最简单的 **3-qubit 比特翻转码**为例：

$$
|0\rangle_L = |000\rangle, \quad |1\rangle_L = |111\rangle
$$

若第一个 qubit 发生翻转 $|100\rangle$，通过测量**奇偶校验算符**（不破坏信息）即可定位并修复。

## 3. 稳定子码（Stabilizer Code）框架

现代 QEC 几乎全部基于**稳定子形式主义**（Stabilizer Formalism）：

- 定义一组**稳定子生成元** $\{S_i\}$，满足 $S_i|\psi\rangle_L = +|\psi\rangle_L$
- 通过测量 $S_i$ 的本征值（±1），获得**错误综合征（syndrome）**，从而定位错误类型和位置
- 测量本身**不破坏逻辑信息**（稳定子与逻辑算符对易）

## 4. 错误阈值（Error Threshold）

[[Surface-Code]] 等码具有一个关键参数：**错误阈值 $p_{th}$**。

> 当物理错误率 $p < p_{th}$ 时，增加码距 $d$ 可以**指数级压低**逻辑错误率：

$$
p_L \propto \left(\frac{p}{p_{th}}\right)^{\lfloor d/2 \rfloor + 1}
$$

表面码的阈值约为 $p_{th} \approx 1\%$，是目前最具实用前景的码之一。

> [!warning] 误区：物理 qubit 越多纠错越好？
> 增加物理 qubit 数量**必须配合增大码距 $d$**，否则无意义。一个 $d=3$ 的表面码用 9 个物理 qubit 编 1 个逻辑 qubit；而 $d=5$ 用 41 个。**质量（更高的码距）比数量（更多的 qubit）重要得多。**

## 5. 与中性原子体系的关联

在 [[Optical-Tweezer-Arrays]] 平台中：
- 多个中性原子组成一个**逻辑 qubit**
- [[Rabi-Flopping]] 和 [[CZ-Gate]] 用于实现稳定子测量
- 原子损失和退相干是主要错误源，QEC 通过**横向隐形传态**（见 [[Transversal-Teleportation]]、[[Deep-Circuit-Execution]]）实时清除

> [!info] 为什么表面码成为中性原子的首选码？
> 表面码只需要**近邻 qubit 的二维网格连接**，而光镊阵列天然提供二维原子排列。两者的拓扑结构完美匹配，使得稳定子测量只需最近邻 CZ 门，无需长程连接——这是其他纠错码（如 CSS 码、Bacon-Shor 码）难以做到的。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $p_L$ | 逻辑错误率 | $p_L \propto (p/p_{th})^{\lfloor d/2\rfloor+1}$ |
| $d$ | 码距（code distance） | 最少需要翻转多少个物理比特才能将一个逻辑错误变成另一个 |
| $S_i$ | 稳定子生成元 | $S_i|\psi\rangle_L = +|\psi\rangle_L$ |

## 🔗 相关笔记

- [[Single-Qubit-Gates]] — 稳定子测量中使用的单比特门
- [[Transversal-Gate]] — 容错逻辑门的核心机制
- [[Transversal-Teleportation]] — 深度电路中的错误清除协议
- [[Surface-Code]] — 最有前景的具体纠错码

## 📝 更新记录

- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
