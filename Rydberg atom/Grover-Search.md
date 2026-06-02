---
aliases:
  - Grover Search
  - Grover 搜索
  - 量子搜索
  - 量子振幅放大
  - Amplitude Amplification
tags:
  - Physics
  - Quantum
  - Algorithm
  - Search
date: 2026-06-02
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "don't understand"
---

# Grover 搜索（Grover Search / 量子振幅放大）

> 来源批注：量子计算算法基础
> 本笔记介绍 Grover 搜索算法的基本原理和与相位操控的关系。内容待补充。

---

## 1. 问题背景

在 $N$ 个无序数据中搜索一个特定目标：

- **经典算法**：平均需要 $O(N)$ 次查询
- **Grover 算法**：只需要 $O(\sqrt{N})$ 次查询——**二次加速**

虽然不是指数加速，但对于大规模数据库，$\sqrt{N}$ vs $N$ 的差距是巨大的。

---

## 2. 核心思想：振幅放大

Grover 算法的核心是**反复执行两个操作**，逐步放大目标态的概率振幅：

1. **Oracle（预言机）**：给目标态加一个负号（相位翻转）
2. **Diffusion 算子**：围绕均匀叠加态做"反射"（振幅放大）

每执行一轮，目标态的振幅增大，非目标态的振幅减小。经过约 $\frac{\pi}{4}\sqrt{N}$ 轮后，目标态的振幅接近 1——测量几乎必定得到目标。

> [!tip] 物理直觉
> 想象一群人站成一圈，其中一个人戴着特殊帽子（目标态）。Grover 算法就像：(1) 先让戴帽子的人"低头"（Oracle 翻转相位），(2) 然后让所有人"对着中心点做镜像反射"（Diffusion 算子）。反复做这两个动作，戴帽子的人会越来越"突出"——最终你几乎一定能找到他。

---

## 3. 与相位操控的关系

Grover 算法的成功**完全依赖于精确的相位操控**：

- Oracle 门给目标态引入 $\pi$ 相位（$-1$）——这本质上是一个 $Z$ 门
- Diffusion 算子涉及 H 门、$Z$ 门、H 门的组合——需要精确控制相对相位
- 如果相位控制有误差，振幅放大效率下降，需要更多轮迭代

这就是为什么 [[Single-Qubit-Gates|$R_z$ 门]] 和 [[AC-Stark-Effect|AC Stark 相移]] 的精确性如此重要。

---

## 4. 待补充内容

- Oracle 的具体电路实现
- Diffusion 算子的数学推导
- 迭代次数的精确公式
- 与[[量子纠错 (QEC)]]的结合（容错 Grover 搜索）
- 在中性原子平台上的实现方案

---

## 🔗 相关笔记

- [[Single-Qubit-Gates]] — Grover 算法中使用的核心量子门
- [[AC-Stark-Effect]] — 相位旋转的物理实现
- [[Two-Qubit-Gates]] — Oracle 电路需要的两比特门
- [[Qubit-State-and-Superposition]] — 叠加态是 Grover 搜索的起点

## 📝 更新记录

- 2026-06-02: 初始创建（stub），待补充详细内容
