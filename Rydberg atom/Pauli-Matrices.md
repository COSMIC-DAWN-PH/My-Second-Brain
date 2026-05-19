---
aliases:
  - Pauli Matrices
  - 泡利矩阵
  - Pauli Gates
  - σ_x
  - σ_y
  - σ_z
  - X门
  - Y门
  - Z门
tags:
  - Physics
  - Quantum
  - Mathematics
  - LinearAlgebra
  - Gates
date: 2026-03-29
status: In-Progress
source: "[[generall quantum 2026]]"
---

# 泡利矩阵（Pauli Matrices）

> 📄 来源文献：[[generall quantum 2026]] · 概念来源于量子计算基础学习

---

## 1. 数学定义

泡利矩阵通常记为 $\sigma_x, \sigma_y, \sigma_z$，或在量子电路中简写为 $X, Y, Z$。在计算基 $\{|0\rangle, |1\rangle\}$ 下：

$$
X = \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
Y = \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
Z = \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

加上单位矩阵 $I = \begin{pmatrix}1&0\\0&1\end{pmatrix}$，这四个矩阵构成 $2\times2$ 复厄米矩阵空间的一组**完备基**。

## 2. 每个门的物理意义

| 门 | 矩阵作用 | 布洛赫球操作 | 直觉比喻 |
|---|---|---|---|
| $X$ | $X\|0\rangle = \|1\rangle$，$X\|1\rangle = \|0\rangle$ | 绕 $x$ 轴旋转 $\pi$ | 量子 NOT 门（比特翻转） |
| $Z$ | $Z\|0\rangle = \|0\rangle$，$Z\|1\rangle = -\|1\rangle$ | 绕 $z$ 轴旋转 $\pi$ | 相位翻转（不改变测量概率） |
| $Y$ | $Y\|0\rangle = i\|1\rangle$，$Y\|1\rangle = -i\|0\rangle$ | 绕 $y$ 轴旋转 $\pi$ | 比特与相位同时翻转，$Y = iXZ$ |

## 3. 核心物理性质（重点拆解）

> ⚠️ 原笔记标注"不太懂"——下面逐条深入解释。

### 3.1 本征值与本征态

所有泡利矩阵本征值均为 $\pm 1$。各自的本征态：

$$
Z|0\rangle = +1 \cdot |0\rangle, \quad Z|1\rangle = -1 \cdot |1\rangle
$$

$$
X|+\rangle = +1 \cdot |+\rangle, \quad X|-\rangle = -1 \cdot |-\rangle, \quad |{\pm}\rangle = \frac{|0\rangle \pm |1\rangle}{\sqrt{2}}
$$

$$
Y|i\rangle = +1 \cdot |i\rangle, \quad Y|-i\rangle = -1 \cdot |-i\rangle, \quad |{\pm i}\rangle = \frac{|0\rangle \pm i|1\rangle}{\sqrt{2}}
$$

> **为什么重要？** 在 [[量子纠错 (QEC)]] 中，稳定子就是 Pauli 算符的乘积——逻辑码字被定义为所有稳定子**本征值为 $+1$** 的本征态。详见 [[门算符本征态 (Gate Eigenstates)]]。

### 3.2 对易关系（Commutation Relation）

$$
[\sigma_j, \sigma_k] = \sigma_j\sigma_k - \sigma_k\sigma_j = 2i\epsilon_{jkl}\sigma_l
$$

**直觉**：$j \neq k$ 时对易子非零，意味着你**不能**同时精确测量两个不同轴向的自旋分量（类比位置-动量不确定关系）。

具体数值：
$$
[X, Y] = 2iZ, \quad [Y, Z] = 2iX, \quad [Z, X] = 2iY
$$

### 3.3 反对易关系（Anti-Commutation Relation）

$$
\{\sigma_j, \sigma_k\} = \sigma_j\sigma_k + \sigma_k\sigma_j = 2\delta_{jk}I
$$

**直觉拆解**：
- $j = k$ 时：$\{X, X\} = X^2 + X^2 = 2I$，即 $X^2 = I$（连续两次 NOT = 恒等）✅
- $j \neq k$ 时：$\{X, Z\} = XZ + ZX = 0$，即 $XZ = -ZX$（**反号**！）

$$
X^2 = Y^2 = Z^2 = I
$$

> 为什么 $XZ = -ZX$？直接计算：
> $$XZ = \begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix} = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$$
> $$ZX = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}0&1\\-1&0\end{pmatrix} = -XZ \quad \checkmark$$

详细讨论见 [[反对易关系 (Anti-Commutation)]]。

### 3.4 酉性与厄米性

$$
\sigma_j^\dagger = \sigma_j \quad \text{（厄米）}, \qquad \sigma_j^\dagger \sigma_j = I \quad \text{（酉）}
$$

**物理含义**：泡利矩阵**既可以作为量子门**（酉矩阵执行演化）**又可以作为可观测量**（厄米矩阵用于测量），两用性正是量子信息的独特之处。

## 4. 旋转门与泡利矩阵的关系

任意绕 $\hat{n}$ 轴旋转 $\theta$ 角的单比特门：

$$
R_{\hat{n}}(\theta) = e^{-i\frac{\theta}{2}(\hat{n}\cdot\vec{\sigma})} = \cos\frac{\theta}{2} \cdot I - i\sin\frac{\theta}{2}(n_x X + n_y Y + n_z Z)
$$

特别地：
$$
R_x(\pi) = -iX, \quad R_z(\pi) = -iZ
$$

（差一个全局相位 $-i$，不影响物理）

## 5. 与 Rydberg/中性原子体系的关联

在 [[光镊阵列 (Optical Tweezer Arrays)]] 平台中：
- $Z$ 的本征基 $\{|0\rangle, |1\rangle\}$ 对应原子的两个**超精细基态**，是 Rydberg 量子比特的自然量子化基底
- **X 旋转**（$R_x(\pi)$ 即 π 脉冲）通过 [[拉比振荡 (Rabi Flopping)]] 的微波驱动实现
- **Z 旋转**通过激光相位偏置或 AC Stark Shift 实现
- 在 [[表面码 (Surface Code)]] 的 syndrome 提取中，稳定子 $A_v = X^{\otimes 4}$ 和 $B_p = Z^{\otimes 4}$ 均为泡利矩阵的[[张量积 (Tensor Product)]]

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $X$ | 泡利 X（比特翻转） | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$，本征态 $\|\pm\rangle$ |
| $Y$ | 泡利 Y（混合翻转） | $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$，本征态 $\|\pm i\rangle$ |
| $Z$ | 泡利 Z（相位翻转） | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$，本征态 $\|0\rangle, \|1\rangle$ |
| $[\sigma_j,\sigma_k]$ | 对易关系 | $2i\epsilon_{jkl}\sigma_l$ |
| $\{\sigma_j,\sigma_k\}$ | 反对易关系 | $2\delta_{jk}I$ |
| $R_{\hat{n}}(\theta)$ | 旋转门 | $\cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}(\hat{n}\cdot\vec{\sigma})$ |