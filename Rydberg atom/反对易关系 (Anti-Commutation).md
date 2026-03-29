---
aliases: [ Anti-Commutation, 反对易, 反对易关系, Anticommutator, {A,B}]
tags: [Physics, Quantum, Mathematics, Algebra, PauliMatrices]
date: 2026-03-29
status: Draft
source: "[[generall quantum 2026]]"
---

# 反对易关系（Anti-Commutation Relation）

> 来源批注：$X_L$ 展开中 *"反对易（anti-commute）"* — Bluvstein et al., 2026, p.49

## 1. 对易与反对易的定义

两个算符 $A, B$ 的**对易子**（commutator）和**反对易子**（anticommutator）：

$$
[A, B] = AB - BA \quad \text{（对易子）}
$$

$$
\{A, B\} = AB + BA \quad \text{（反对易子）}
$$

- 若 $[A, B] = 0$：$A, B$ **对易**，可以同时对角化（有共同本征态）
- 若 $\{A, B\} = 0$：$A, B$ **反对易**，即 $AB = -BA$

## 2. Pauli 矩阵的反对易关系

Pauli 矩阵之间的反对易是量子信息的基础：

$$
\{X, Z\} = XZ + ZX = 0 \implies XZ = -ZX
$$

完整关系表：

| 算符对 | 对易/反对易 | 结果 |
|---|---|---|
| $X, Y$ | 反对易 | $XY = iZ$，$YX = -iZ$ |
| $Y, Z$ | 反对易 | $YZ = iX$，$ZY = -iX$ |
| $Z, X$ | 反对易 | $ZX = iY$，$XZ = -iY$ |
| 相同算符 | 对易 | $X^2 = Y^2 = Z^2 = I$ |

## 3. 为什么反对易关系在 QEC 中关键？

论文批注中 $X_L$ 的展开涉及反对易：

$$
X_L = X^{\otimes n} \xrightarrow{\text{小角度旋转}} (X + i\theta Y)(X+i\theta Y)\cdots
$$

**逻辑 $X$ 算符**与 **Z 型稳定子**必须**反对易**，而与 **X 型稳定子对易**：

$$
\{X_L, \bar{Z}\} = 0, \quad [X_L, S_i^{(X)}] = 0
$$

这个代数结构保证了：
- 稳定子测量不破坏逻辑信息（逻辑算符与稳定子群相互作用正确）
- 逻辑 $X$ 和逻辑 $Z$ 可以区分（它们相互反对易：$\{X_L, Z_L\} = 0$）

## 4. 张量积下的反对易

对于多 qubit 算符，反对易性由[[张量积 (Tensor Product)]]结构决定：

设 $A = A_1 \otimes A_2$ 和 $B = B_1 \otimes B_2$，则：

$$
AB = (A_1 B_1) \otimes (A_2 B_2)
$$

若 $A_1$ 与 $B_1$ 反对易，$A_2$ 与 $B_2$ 也反对易，则 $AB = BA$（**两个反号相消，整体对易**）！

$$
AB = (-B_1 A_1)\otimes(-B_2 A_2) = (+1)(B_1 A_1 \otimes B_2 A_2) = BA
$$

这解释了为什么某些多体 Pauli 算符之间对易，即使它们在每个位点上都反对易。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $[A,B]$ | 对易子 | $AB - BA$ |
| $\{A,B\}$ | 反对易子 | $AB + BA$ |
| Pauli 反对易 | $X$ 与 $Z$ | $XZ = -ZX$，即 $\{X,Z\}=0$ |
| 多体反对易 | 区位奇偶性 | 奇数个位点反对易 → 整体反对易 |
