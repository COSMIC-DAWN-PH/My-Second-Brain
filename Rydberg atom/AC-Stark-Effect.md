---
aliases:
  - AC Stark Effect
  - AC Stark 效应
  - 光频移
  - Light Shift
tags:
  - Physics
  - Quantum
  - AtomicPhysics
  - NeutralAtom
date: 2026-06-02
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "don't understand"
---

# AC Stark 效应（AC Stark Effect / Light Shift）

> 来源批注：中性原子量子计算基础概念
> 本笔记介绍 AC Stark 效应的基本物理及其在 $R_z$ 门实现中的角色。内容待补充。

---

## 1. 什么是 AC Stark 效应？

当原子处于**非共振**的光场中时，光场会移动原子的能级——这种由交流（AC）电磁场引起的能级偏移就是 **AC Stark 效应**（也叫**光频移 / Light Shift**）。

核心公式：对失谐 $\Delta = \omega_L - \omega_0$ 的激光，能级偏移量为：

$$
\delta E \propto \frac{\Omega^2}{4\Delta}
$$

其中 $\Omega$ 是拉比频率。

> [!tip] 物理直觉
> 想象弹簧上挂一个球（原子能级），AC Stark 效应就像有人用振动的绳子不断推弹簧——球的平衡位置被"推偏了"。失谐越大（推得越快），偏移越小但振荡越快。

---

## 2. 在中性原子量子计算中的应用

### 2.1 $R_z$ 门的物理实现

在 [[Optical-Tweezer-Arrays]] 中，$R_z$ 门（相位旋转）通过 AC Stark 效应实现：

- 施加一个**失谐激光**（$\Delta \neq 0$）
- $|1\rangle$ 态获得一个额外的相移 $\delta\phi = \delta E \cdot t / \hbar$
- $|0\rangle$ 态不受影响（或受影响不同）
- 净效果：相对相位改变 → $R_z(\theta)$ 门

详见 [[Single-Qubit-Gates]]。

### 2.2 原子位置的光频移

在 [[Optical-Tweezer-Arrays]] 中，光镊本身的激光也会对囚禁的原子产生 AC Stark 位移，这是原子被囚禁的物理机制——光频移创造了一个势阱。

---

## 3. 待补充内容

- AC Stark 效应的微扰论推导
- 与 [[Rabi-Flopping]] 的关系（失谐 vs 光频移）
- 实验中的光频移标定方法
- Magic wavelength 概念

---

## 🔗 相关笔记

- [[Single-Qubit-Gates]] — $R_z$ 门通过 AC Stark 效应实现
- [[Rabi-Flopping]] — 共振驱动与失谐驱动的对比
- [[Optical-Tweezer-Arrays]] — 光镊囚禁本身就是 AC Stark 效应的应用

## 📝 更新记录

- 2026-06-02: 初始创建（stub），待补充详细内容
