---
aliases:
  - Quantum Phase Estimation
  - 量子相位估计
  - QPE
tags:
  - Physics
  - Quantum
  - Algorithm
  - PhaseEstimation
date: 2026-06-02
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "don't understand"
---

# 量子相位估计（Quantum Phase Estimation, QPE）

> 来源批注：量子计算算法基础
> 本笔记介绍量子相位估计的基本原理及其在量子化学和 Shor 算法中的核心角色。内容待补充。

---

## 1. 问题

给定一个酉算符 $U$ 和它的一个本征态 $|\psi\rangle$：

$$
U|\psi\rangle = e^{2\pi i \theta}|\psi\rangle
$$

**目标**：估计相位 $\theta$（一个 $[0,1)$ 之间的实数）。

> [!tip] 为什么重要？
> $\theta$ 包含了 $U$ 的**本征值信息**。如果我们能精确估计 $\theta$，就能：
> - 计算分子的能级（量子化学）
> - 分解大整数（Shor 算法）
> - 模拟量子系统的动力学

---

## 2. 核心思想

QPE 利用**量子干涉**将相位信息"编码"到一组辅助 qubit 的测量结果中：

1. 将 $\theta$ 的二进制表示 $\theta = 0.\theta_1\theta_2\cdots\theta_n$ 编码到 $n$ 个辅助 qubit
2. 通过受控 $U^{2^k}$ 门将相位信息"写入"辅助 qubit
3. 对辅助 qubit 做**逆量子 Fourier 变换**（inverse QFT）
4. 测量辅助 qubit → 得到 $\theta$ 的 $n$ 位二进制近似

---

## 3. 与相位操控的关系

QPE 的成功**完全依赖于精确的相位操控**：

- 受控 $U^{2^k}$ 门需要精确控制旋转角度 $2\pi \theta \cdot 2^k$
- 逆 QFT 需要精确的 $R_z$ 门序列
- 任何相位误差都会传播到最终的 $\theta$ 估计值中

这就是为什么 [[Single-Qubit-Gates|$R_z$ 门]] 的精确性（通过 [[AC-Stark-Effect|AC Stark 效应]] 实现）是容错量子计算的关键。

---

## 4. 待补充内容

- QPE 电路的详细结构
- 逆量子 Fourier 变换（inverse QFT）的原理
- 精度与辅助 qubit 数量的关系
- 在量子化学（VQE/QPE）中的应用
- 与 Shor 算法的联系
- 在中性原子平台上的实现挑战

---

## 🔗 相关笔记

- [[Single-Qubit-Gates]] — QPE 中 $R_z$ 门序列的精确控制
- [[AC-Stark-Effect]] — 相位旋转的物理实现机制
- [[Qubit-State-and-Superposition]] — 叠加态和相位因子是 QPE 的基础
- [[Two-Qubit-Gates]] — 受控 $U$ 门需要两比特门
- [[QEC]] — 容错 QPE 需要量子纠错保护

## 📝 更新记录

- 2026-06-02: 初始创建（stub），待补充详细内容
