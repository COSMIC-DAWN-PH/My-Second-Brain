---
aliases:
  - Learning Roadmap
  - 学习路线图
  - 学习计划
tags:
  - Meta
  - LearningPath
date: 2026-06-02
status: In-Progress
---

# 学习路线图（Learning Roadmap）

> 中性原子量子计算的系统学习路径。按依赖关系从基础到进阶排列，标记当前进度。
> ✅ = understood（已掌握，跳过）| 🟡 = getting there | ⬜ = vague / don't understand（待学习）

---

## 阶段一：量子比特基础 ✅ 已完成

> 你已经理解了叠加态和相位因子的物理含义。这是所有后续内容的起点。

| # | 知识点 | 笔记 | 状态 |
|---|--------|------|------|
| 1 | 量子比特态与叠加态 | [[Rydberg atom/Qubit-State-and-Superposition]] | ✅ understood |

---

## 阶段二：单量子比特门 🟡 进行中

> 掌握对单个 qubit 的操作——旋转、相位、测量基。这是量子线路的基本构件。

| #   | 知识点      | 笔记                                  | 状态               | 前置     |
| --- | -------- | ----------------------------------- | ---------------- | ------ |
| 2   | Pauli 矩阵 | [[Rydberg atom/Pauli-Matrices]]     | ⬜ vague          | #1     |
| 3   | 门算符本征态   | [[Rydberg atom/Gate-Eigenstates]]   | ⬜ vague          | #2     |
| 4   | 单量子比特门   | [[Rydberg atom/Single-Qubit-Gates]] | 🟡 getting there | #1, #2 |

**学习建议**：先读 Pauli-Matrices（重点看本征值和对易关系），再看 Gate-Eigenstates（把本征态和测量基对应起来），最后巩固 Single-Qubit-Gates。

---

## 阶段三：原子物理基础 ⬜ 待学习

> 理解中性原子量子计算的物理平台——原子如何被囚禁、如何被操控。

| # | 知识点 | 笔记 | 状态 | 前置 |
|---|--------|------|------|------|
| 5 | 里德堡阻塞 | [[Rydberg atom/Rydberg-Blockade]] | ⬜ don't understand | — |
| 6 | 里德堡态 $\|r\rangle$ | [[Rydberg atom/Rydberg-Blockade]] §1.2 | ⬜ don't understand | #5 |
| 7 | 拉比振荡 | [[Rydberg atom/Rabi-Flopping]] | ⬜ vague | #6 |
| 8 | 光镊阵列 | [[Rydberg atom/Optical-Tweezer-Arrays]] | ⬜ vague | #5, #7 |

**学习建议**：先读 Rydberg-Blockade（理解阻塞条件和 CZ 门实现），重点理解里德堡态 $|r\rangle$ 的标度律（$V \propto n^{11}$、阻塞半径 $R_b$），再读 Rabi-Flopping（理解脉冲操控如何驱动 $|g\rangle \leftrightarrow |r\rangle$ 跃迁），最后读 Optical-Tweezer-Arrays（理解硬件平台）。

---

## 阶段四：两量子比特门与纠缠 🟡 进行中

> 理解两个 qubit 之间的量子关联——纠缠的产生、度量和应用。

| # | 知识点 | 笔记 | 状态 | 前置 |
|---|--------|------|------|------|
| 9 | 两量子比特态与纠缠 | [[Rydberg atom/Two-Qubit-State-and-Entanglement]] | 🟡 getting there | #1, #2 |
| 10 | 两量子比特门 | [[Rydberg atom/Two-Qubit-Gates]] | 🟡 getting there | #4, #9 |
| 11 | CZ 门 | [[Rydberg atom/CZ-Gate]] | ⬜ vague | #5, #10 |

**学习建议**：先读 Two-Qubit-State-and-Entanglement（纠缠判据、并发度），再读 Two-Qubit-Gates（CNOT、CZ、SWAP），最后读 CZ-Gate（里德堡阻塞实现 CZ 的具体步骤）。

---

## 阶段五：量子纠错 ⬜ 待学习

> 理解如何在有噪声的量子硬件上实现可靠计算——这是通向实用量子计算的必经之路。

| # | 知识点 | 笔记 | 状态 | 前置 |
|---|--------|------|------|------|
| 12 | 量子纠错 | [[Rydberg atom/QEC]] | ⬜ vague | #4, #9 |
| 13 | 张量积 | [[Rydberg atom/Tensor-Product]] | ⬜ vague | #1 |
| 14 | 反对易关系 | [[Rydberg atom/Anti-Commutation]] | ⬜ vague | #2 |
| 15 | 表面码 | [[Rydberg atom/Surface-Code]] | ⬜ vague | #12 |

**学习建议**：先读 QEC（理解稳定子框架和错误阈值），然后按需补充 Tensor-Product 和 Anti-Commutation 的数学工具，最后读 Surface-Code（中性原子的首选纠错码）。

---

## 阶段六：容错量子计算 ⬜ 待学习

> 理解如何在纠错码上执行深度电路——横向门、横向隐形传态、Gate Teleportation。

| # | 知识点 | 笔记 | 状态 | 前置 |
|---|--------|------|------|------|
| 16 | 横向纠缠门 | [[Rydberg atom/Transversal-Gate]] | ⬜ vague | #4, #12 |
| 17 | 横向隐形传态 | [[Rydberg atom/Transversal-Teleportation]] | ⬜ don't understand | #16 |
| 18 | 深度电路执行 | [[Rydberg atom/Deep-Circuit-Execution]] | ⬜ don't understand | #17 |

**学习建议**：这是最难的阶段。先读 Transversal-Gate（理解横向操作为什么容错），再读 Transversal-Teleportation（两个根本困难 → 横向隐形传态是唯一出路），最后读 Deep-Circuit-Execution（恒定熵运行）。

---

## 阶段七：进阶应用 ⬜ 待学习

> 量子算法和高级物理效应。在前六阶段扎实后再进入。

| # | 知识点 | 笔记 | 状态 | 前置 |
|---|--------|------|------|------|
| 19 | AC Stark 效应 | [[Rydberg atom/AC-Stark-Effect]] | ⬜ don't understand | #5 |
| 20 | 量子 Zeno 效应 | [[Rydberg atom/Quantum-Zeno-Effect]] | ⬜ vague | #1 |
| 21 | Grover 搜索 | [[Rydberg atom/Grover-Search]] | ⬜ don't understand | #4 |
| 22 | 量子相位估计 | [[Rydberg atom/Quantum-Phase-Estimation]] | ⬜ don't understand | #4 |
| 23 | 中性原子测试 | [[Rydberg atom/Neutral_Atom_Test]] | ⬜ vague | #5, #6 |

---

## 总览

```
阶段一 ✅ 量子比特基础 ──────────────────────────────────→
阶段二 🟡 单比特门 ─────────────────────→
阶段三 ⬜ 原子物理 ─────────────────────→
阶段四 🟡 两比特门与纠缠 ────────────────→
阶段五 ⬜ 量子纠错 ──────────────────────→
阶段六 ⬜ 容错量子计算 ──────────────────→
阶段七 ⬜ 进阶应用 ──────────────────────→
```

**当前进度**：阶段一已完成，阶段二和阶段四进行中。建议优先完成阶段二（单比特门）和阶段三（原子物理），然后进入阶段四的巩固。

---

## 🔗 相关笔记

- [[Rydberg atom/Qubit-State-and-Superposition]] — 阶段一：已掌握
- [[Rydberg atom/Single-Qubit-Gates]] — 阶段二：进行中
- [[Rydberg atom/Rydberg-Blockade]] — 阶段三：待学习

## 📝 更新记录

- 2026-06-02: 初始创建，7 阶段 22 个知识点的学习路线图
