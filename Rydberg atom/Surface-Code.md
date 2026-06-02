---
aliases: [Surface Code, 表面码, Toric Code, 距离-5表面码]
tags: [Physics, Quantum, ErrorCorrection, SurfaceCode]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
comprehension: "vague"
---

# 表面码 (Surface Code)

> 来源批注：*"a distance-5 surface code"* — Bluvstein et al., 2026, p.40

## 1. 什么是表面码？

表面码是目前**最实用的量子纠错码**之一，因为它：
- 只需要**近邻量子比特之间的二体相互作用**（易于实验实现）
- 具有约 $1\%$ 的高错误阈值
- 逻辑错误率随码距指数衰减

表面码将 qubit 排列在一个 **$d \times d$ 的二维网格**上（$d$ 为码距）。

## 2. 物理结构

以 $d = 3$ 表面码为例（共 $d^2 + (d-1)^2 = 13$ 个物理 qubit）：

```
● ─ ○ ─ ●
│   │   │
○ ─ ● ─ ○
│   │   │
● ─ ○ ─ ●
```

- **数据 qubit（●）**：存储逻辑信息
- **辅助 qubit（○）**：用于测量稳定子（syndrome 提取）

> [!tip] 交错棋盘格布局
> 注意 ● 和 ○ 呈**棋盘格交错排列**——每个辅助 qubit 被数据 qubit 包围，可同时检测周围 4 个 qubit 的错误。这种布局是表面码只需近邻连接的几何基础。

## 3. 稳定子结构

表面码有两类稳定子（参见 [[QEC]]）：

**X 型稳定子**（检测 Z 错误）：
$$
A_v = \prod_{e \in \text{vertex } v} X_e
$$

**Z 型稳定子**（检测 X 错误）：
$$
B_p = \prod_{e \in \text{plaquette } p} Z_e
$$

两组稳定子的测量结果共同给出错误综合征（syndrome），解码器据此推断并修复错误。

## 4. 码距（Code Distance）

码距 $d$ 决定了纠错能力：
- 可以检测 $d-1$ 个错误
- 可以纠正 $\lfloor (d-1)/2 \rfloor$ 个错误

论文中使用 **distance-5 表面码**：
- 物理 qubit 数：$5^2 + 4^2 = 41$ 个
- 可纠正最多 **2 个物理量子比特的错误**（$\lfloor 4/2 \rfloor = 2$）

$$
p_L \approx \left(\frac{p}{p_{th}}\right)^3 \quad (d=5)
$$

> [!warning] 常见混淆：码距 ≠ 物理 qubit 数
> 码距 $d$ 和物理 qubit 数 $n$ 是不同的概念。$d=5$ 的表面码需要 $d^2 + (d-1)^2 = 41$ 个物理 qubit，但**纠错能力仅由 $d$ 决定**。码距才是衡量保护强度的核心指标。

## 5. 为什么在中性原子平台上特别适合？

[[Optical-Tweezer-Arrays|光镊]] 可以将原子自由排列为二维网格，天然匹配表面码的拓扑结构。通过 [[CZ-Gate]] 实现近邻纠缠操作，配合 [[Rydberg-Blockade]] 实现高保真度两比特门。

> [!info] 二维布局的天然优势
> 光镊阵列可以在二维平面上自由排布原子，无需额外布线层。表面码的拓扑结构恰好是二维的——这意味着**不需要三维集成或长程连接**，用当前技术就能直接实现 surface code 的物理 layout。

---

## 📐 核心公式摘要

- **d**：码距 — $d=5$ → 41 物理 qubit 编 1 逻辑 qubit
- **p_L**：逻辑错误率 — $p_L \propto (p/p_{th})^{\lfloor d/2\rfloor+1}$
- **p_{th}**：错误阈值 — $p_{th} \approx 1\%$（表面码）
- **A_v**：X 稳定子 — $A_v = \prod X_e$
- **B_p**：Z 稳定子 — $B_p = \prod Z_e$


## 📝 更新记录

- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
