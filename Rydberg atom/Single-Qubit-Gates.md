---
aliases:
  - Single-Qubit Gates
  - 单量子比特门
  - 单比特门
  - 量子门
  - Quantum Gates
tags:
  - Physics
  - Quantum
  - Gates
  - SingleQubit
  - Fundamental
date: 2026-06-01
status: In-Progress
source: "[[generall quantum 2026]]"
comprehension: "getting there"
---

# 单量子比特门（Single-Qubit Gates）

> 来源批注：量子计算基础概念 — Bluvstein et al., 2026
> 本笔记从"一个 qubit 能做什么"出发，系统介绍单比特门的物理直觉、数学定义、标准门集、Bloch 球几何图像以及在中性原子中的实验实现。所有矩阵运算都给出完整步骤，不跳步。

---

## 1. 一个 qubit 能做什么？——单比特门的本质

### 1.1 先从经典世界说起

经典计算机里，一个 bit 要么是 0 要么是 1。经典逻辑门（AND、OR、NOT）作用在确定的 0 或 1 上，输出也是确定的。

但 qubit 不同。一个 qubit 可以处于叠加态：

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1
$$

量子门对叠加态的作用是**同时改变 $\alpha$ 和 $\beta$ 的大小和相对相位**——这就是单比特门的本质。

### 1.2 三个核心约束

在设计单比特门时，量子力学给了三个硬约束：

**概率守恒**：变换前后概率总和为 1，即 $|\alpha'|^2 + |\beta'|^2 = |\alpha|^2 + |\beta|^2 = 1$。概率不能凭空出现或消失。

**可逆性**：存在逆操作 $U^{-1}$ 使得 $U^{-1}U = I$。门操作不能丢失信息（否则违反幺正性）。

**线性**：$U(\alpha|0\rangle + \beta|1\rangle) = \alpha\,U|0\rangle + \beta\,U|1\rangle$。量子力学是线性的——叠加态的演化等于各分量演化的叠加。

这三个约束合在一起，**唯一地决定了**单比特门的数学形式——它必须是 $2\times2$ 的**酉矩阵**：

$$
U^\dagger U = UU^\dagger = I
$$

> [!tip] 物理直觉
> 单比特门就是**对叠加态的"旋转"**：它把 $\alpha|0\rangle + \beta|1\rangle$ 变成新的 $\alpha'|0\rangle + \beta'|1\rangle$，就像在复平面上把一个向量转到新的方向。而酉性保证了旋转后向量的长度（=概率总和）不变。

### 1.3 矩阵表示

计算基 $\{|0\rangle, |1\rangle\}$ 下，qubit 用两分量列向量表示：

$$
|0\rangle = \begin{pmatrix}1\\0\end{pmatrix}, \quad |1\rangle = \begin{pmatrix}0\\1\end{pmatrix}, \quad |\psi\rangle = \begin{pmatrix}\alpha\\\beta\end{pmatrix}
$$

单比特门是作用在这个二维复向量空间上的 $2\times2$ 矩阵：

$$
U|\psi\rangle = \begin{pmatrix}u_{00} & u_{01}\\u_{10} & u_{11}\end{pmatrix}\begin{pmatrix}\alpha\\\beta\end{pmatrix} = \begin{pmatrix}u_{00}\alpha + u_{01}\beta\\u_{10}\alpha + u_{11}\beta\end{pmatrix}
$$

---

## 2. Hadamard 门（H 门）：制造叠加

H 门是量子计算中**使用频率最高的单比特门**，理解它等于理解量子计算的核心优势。

### 2.1 定义

$$
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

### 2.2 逐行计算：它到底做了什么？

从 $|0\rangle$ 出发：

$$
H|0\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\cdot1 + 1\cdot0\\1\cdot1 + (-1)\cdot0\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = |+\rangle
$$

从 $|1\rangle$ 出发：

$$
H|1\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\cdot0 + 1\cdot1\\1\cdot0 + (-1)\cdot1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix} = |-\rangle
$$

### 2.3 物理含义

| 输入 | 输出 | 含义 |
|------|------|------|
| $\|0\rangle$（确定的 0） | $\|+\rangle$（等权叠加） | 从"确定"走向"不确定" |
| $\|1\rangle$（确定的 1） | $\|-\rangle$（等权叠加） | 从"确定"走向"不确定" |
| $\|+\rangle$（叠加态） | $\|0\rangle$（确定态） | 从"不确定"走回"确定" |

> [!tip] "均衡器"类比
> H 门就像一个均衡器：输入 0 或 1，输出都是 50-50 的叠加。它"抹平"了所有确定性，制造了**量子并行性**的起点——没有 H 门，就没有叠加，也就没有量子计算。

### 2.4 自反性：$HH = I$

$$
HH = \frac{1}{2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}1+1 & 1-1\\1-1 & 1+1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}2&0\\0&2\end{pmatrix} = I
$$

> H 门是自己的逆——"把确定态变成叠加态，再做一次 H 门就变回确定态"。这在量子算法的**解码阶段**非常有用。

### 2.5 Bloch 球上的 H 门

在 Bloch 球上，H 门将北极 $|0\rangle$ 旋转到赤道上的 $|+\rangle$。等价于绕 $(x+z)/\sqrt{2}$ 轴旋转 $\pi$。

---

## 3. Pauli 门：三大基础操作

详细代数性质见 [[Pauli-Matrices]]，这里聚焦于**作为量子门的物理含义**。

### 3.1 X 门（比特翻转 / 量子 NOT 门）

$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

**逐行计算**：

$$
X|0\rangle = \begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix} = |1\rangle
$$

$$
X|1\rangle = \begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix} = |0\rangle
$$

**对叠加态**：

$$
X(\alpha|0\rangle + \beta|1\rangle) = \beta|0\rangle + \alpha|1\rangle
$$

**物理含义**：X 门就是量子世界的"拨开关"——把 $|0\rangle$ 拨到 $|1\rangle$，$|1\rangle$ 拨到 $|0\rangle$。对叠加态来说，它**交换了两个分量的权重**。

在 Bloch 球上：绕 $x$ 轴旋转 $\pi$（180°）。

### 3.2 Z 门（相位翻转）

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**逐行计算**：

$$
Z|0\rangle = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}1\\0\end{pmatrix} = |0\rangle
$$

$$
Z|1\rangle = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}0\\-1\end{pmatrix} = -|1\rangle
$$

**对叠加态**：

$$
Z(\alpha|0\rangle + \beta|1\rangle) = \alpha|0\rangle - \beta|1\rangle
$$

> [!warning] Z 门不改变测量概率！
> Z 只改变 $|1\rangle$ 分量的**符号**（从 $+\beta$ 变成 $-\beta$）。但测量概率是 $|\beta|^2 = |-\beta|^2$，**完全不变**！
> Z 改变的是**相对相位**——这是量子干涉的关键资源。后面学习量子算法时会反复看到：相位的操控是量子计算的核心能力。

在 Bloch 球上：绕 $z$ 轴旋转 $\pi$。

### 3.3 Y 门（比特+相位同时翻转）

$$
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = iXZ
$$

**逐行计算**：

$$
Y|0\rangle = \begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\i\end{pmatrix} = i|1\rangle
$$

$$
Y|1\rangle = \begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}-i\\0\end{pmatrix} = -i|0\rangle
$$

在 Bloch 球上：绕 $y$ 轴旋转 $\pi$。

> [!info] 三个 Pauli 门的关系
> - $Y = iXZ$（Y 可以用 X 和 Z 的组合表示）
> - $X^2 = Y^2 = Z^2 = I$（做两次等于不做）
> - $XZ = -ZX$（它们不对易——先做 X 再做 Z ≠ 先做 Z 再做 X）
> - X、Y、Z 加上恒等矩阵 $I$，构成 $2\times2$ 矩阵的完备基

### 3.4 相位门家族：S 门与 T 门

相位门都是 $Z$ 的"分数次幂"，只改变 $|1\rangle$ 分量的相位：

| 门 | 矩阵 | 效果 | 与 Z 的关系 |
|---|---|---|---|
| $S = Z^{1/2}$ | $\text{diag}(1,\;i)$ | $+i$ 相位（$\pi/2$） | $S^2 = Z$ |
| $T = Z^{1/4}$ | $\text{diag}(1,\;e^{i\pi/4})$ | $e^{i\pi/4}$ 相位（$\pi/4$） | $T^2 = S$，$T^4 = Z$ |

**直觉**：S 门"走半步"（$\pi/2$），T 门"走四分之一步"（$\pi/4$）——它们让量子线路可以做越来越精细的相位操控。

> [!warning] T 门的特殊地位
> T 门是容错量子计算中最"昂贵"的门——它**无法横向实现**（受 [[Transversal-Gate|Eastin-Knill 定理]] 限制），必须通过 [[Transversal-Teleportation|Gate Teleportation]] + magic state distillation 来实现。在 T-count 优化中，工程师们千方百计地减少 T 门的数量。

---

## 4. 旋转门：任意角度的操控

Pauli 门只做 $\pi$ 旋转（180°），但实际电路经常需要**任意角度**的旋转。

### 4.1 为什么是 $\theta/2$ 而不是 $\theta$？

量子态生活在**二维复射影空间**（对应 Bloch 球），不是普通三维空间。这里有一个反直觉的事实：

> Bloch 球上转 $\theta$ 角 → 希尔伯特空间中只需要转 $\theta/2$

这是因为 $SU(2)$ 到 $SO(3)$ 是二对一的映射（双覆盖）。具体例子：
- Bloch 球上绕 $x$ 轴转 $\pi$（到对面）→ 希尔伯特空间只需 $R_x(\pi/2)$

> [!tip] 怎么记忆？
> $\pi$ 脉冲把 Bloch 球上的点从北极翻到南极（半圈 = $\pi$），对应的旋转角是 $\pi/2$（四分之一圈）。别搞反就行。

### 4.2 三个基本旋转门

绕 $\hat{n}$ 轴旋转 $\theta$ 角的一般公式：

$$
R_{\hat{n}}(\theta) = e^{-i\frac{\theta}{2}(\hat{n}\cdot\vec{\sigma})} = \cos\frac{\theta}{2} \cdot I - i\sin\frac{\theta}{2}(n_x X + n_y Y + n_z Z)
$$

**三个坐标轴的旋转门**：

$$
R_x(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

$$
R_y(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

$$
R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
$$

### 4.3 与拉比振荡的直接联系

在 Rydberg 原子实验中，$R_x(\theta)$ 通过激光脉冲驱动实现，脉冲持续时间 $t$ 决定旋转角 $\theta = \Omega t$：

| 脉冲类型 | $\theta$ | 效果 | 实验操作 |
|---------|---------|------|---------|
| $\pi$ 脉冲 | $\pi$ | $\|0\rangle \to \|1\rangle$ 完全翻转 | X 门（NOT） |
| $\pi/2$ 脉冲 | $\pi/2$ | $\|0\rangle \to (\|0\rangle - i\|1\rangle)/\sqrt{2}$ | 制备叠加态 |
| $\theta$ 脉冲 | 任意 $\theta$ | 任意旋转 | $R_x(\theta)$ |

> [!info] 与拉比振荡的统一
> [[Rabi-Flopping]] 中的 $\pi$ 脉冲 = 单比特门 $R_x(\pi)$，$\pi/2$ 脉冲 = $R_x(\pi/2)$。这就是"物理现象"和"门语言"的对应。

### 4.4 Euler 分解：任意单比特门 = 三次旋转

**定理**：任何 $2\times2$ 酉矩阵 $U$ 都可以分解为：

$$
U = e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)
$$

四个实参数 $(\alpha, \beta, \gamma, \delta)$ 唯一确定 $U$（除了全局相位）。

> [!tip] 物理直觉
> Bloch 球上任何两个点之间的旋转，都可以用"先转 $z$ 轴、再转 $y$ 轴、最后再转 $z$ 轴"来实现——就像三维空间中万向节可以指向任何方向。

---

## 5. Bloch 球：单比特门的几何语言

### 5.1 单比特态的参数化

任何单 qubit 纯态可以写成 Bloch 球面上的点 $(\theta, \phi)$：

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle
$$

其中 $\theta \in [0, \pi]$（极角），$\phi \in [0, 2\pi)$（方位角）。

| 态 | Bloch 球位置 | Z 测量概率 |
|---|------------|-----------|
| $\|0\rangle$ | 北极 $(\theta=0)$ | 100% 得 0 |
| $\|1\rangle$ | 南极 $(\theta=\pi)$ | 100% 得 1 |
| $\|+\rangle$ | $x$ 轴正方向 | 50% 得 0，50% 得 1 |
| $\|-i\rangle$ | $y$ 轴负方向 | 50% 得 0，50% 得 1 |

### 5.2 所有单比特门 = Bloch 球旋转

| 门 | 旋转轴 | 旋转角 |
|---|--------|-------|
| $X$ | $x$ 轴 | $\pi$ |
| $Y$ | $y$ 轴 | $\pi$ |
| $Z$ | $z$ 轴 | $\pi$ |
| $H$ | $(x+z)/\sqrt{2}$ 轴 | $\pi$ |
| $R_x(\theta)$ | $x$ 轴 | $\theta$ |
| $R_y(\theta)$ | $y$ 轴 | $\theta$ |
| $R_z(\theta)$ | $z$ 轴 | $\theta$ |

> [!tip] 统一视角
> **所有单比特门的本质都是在 Bloch 球上做旋转**。区别只是旋转轴和旋转角度不同。Pauli 门做 180° 翻转，H 门做特殊轴的 180° 翻转，旋转门做任意角度旋转。
> 下面的交互式 Bloch 球可以拖拽旋转视角，点击按钮查看每个门的效果。

<iframe src="file:///C:/Personal%20Profile/Profile/ScienceResearch/Quantum%20Computing/tools/bloch_sphere.html" width="100%" height="580" style="border:1px solid #3a3a5c; border-radius:8px;"></iframe>

---

## 6. 在中性原子中的物理实现

在 [[Optical-Tweezer-Arrays]] 平台中，单比特门通过**激光脉冲**驱动原子的内态跃迁来实现。

### 6.1 量子比特的编码

两个量子比特编码在原子的两个超精细基态中：

$$
|0\rangle \equiv |g\rangle \quad \text{（基态）}, \quad |1\rangle \equiv |e\rangle \quad \text{（激发态）}
$$

常用原子：$^{87}\text{Rb}$（铷-87），超精细分裂 $\sim 6.8\,\text{GHz}$。

### 6.2 受激拉曼跃迁：单比特门的物理基础

两束频率差为 $\omega_1 - \omega_2 = \omega_{\text{hf}}$ 的激光产生等效拉比振荡：

$$
H_{\text{eff}} = \frac{\Omega}{2}(|g\rangle\langle e| + |e\rangle\langle g|) + \frac{\Delta}{2}(|e\rangle\langle e| - |g\rangle\langle g|)
$$

- **$\Omega$**：有效拉比频率，由激光强度和原子性质决定
- **$\Delta$**：失谐，调节激光频率可控制

### 6.3 如何精确控制每个门？

| 目标门 | 控制参数 | 实验手段 |
|--------|---------|---------|
| 旋转角 $\theta$ | 脉冲持续时间 $t$，$\theta = \Omega t$ | 精确控制激光开关时间 |
| 旋转轴方向 | 激光偏振和相对相位 | 调节波片或 AOM |
| $R_x(\theta)$ | 线偏振光沿特定方向 | 确定偏振方向 |
| $R_z(\theta)$ | 失谐脉冲（$\Delta \neq 0$） | [[AC-Stark-Effect\|AC Stark]] 效应产生纯相位偏移 |
| Hadamard | $\pi/2$ 脉冲 + $R_z$ 组合 | 拆解为硬件可执行序列 |

### 6.4 关键性能参数

| 参数 | 数值 | 说明 |
|------|------|------|
| 单比特门保真度 | $\sim 99.5\%$ | 受退相干和脉冲不完美限制 |
| 门操作时间 | $\sim 0.3\,\mu\text{s}$ | 远小于退相干时间 $T_2 \sim 100\,\text{ms}$ |
| 实现方式 | 全局微波脉冲 | 所有原子**同时**接受相同操作 |

> [!warning] 全局 vs 选择性操控
> 中性原子平台的单比特门通常是**全局的**——同一束激光同时驱动所有原子。如果只想旋转某个特定原子，需要用**选择性寻址**（如局部激光束或 AC Stark 位移）。这是硬件设计的重要考量。

---

## 7. 通用门集：单比特门的终极角色

### 7.1 Solovay-Kitaev 定理

$\{H, T, \text{CZ}\}$ 构成**通用门集**——任何量子线路都可以用这三种门以任意精度近似。

其中：
- **H + T**：单比特门，负责所有单 qubit 旋转（H 做大角度旋转，T 做精细相位调节）
- **CZ**：两比特门，负责建立纠缠

### 7.2 为什么 T 门是"最贵"的门？

在容错量子计算中，**T 门的数量**是衡量线路资源开销的关键指标：

- 横向门（如 H、CZ）可以直接容错实现
- T 门**无法横向实现** → 必须通过 [[Transversal-Teleportation|Gate Teleportation]] + magic state distillation
- 每个 T 门消耗一个蒸馏好的 magic state（需要数十到数百个物理 qubit）

### 7.3 线路结构

```
量子线路 = [单比特门] + [CZ] + [单比特门] + [CZ] + ... + [单比特门] + [测量]
              ↑           ↑
           旋转/相位     建立纠缠
          (H, T, Rz)    (CZ 门)
```

> 单比特门的**角色**：状态初始化（$|0\rangle \to |+\rangle$）、算法逻辑执行（H、T 组合）、纠缠前准备、测量前旋转。

---

## 📐 核心公式摘要

- **U**：一般单比特门 — $2\times2$ 酉矩阵，$U^\dagger U = I$
- **X**：Pauli X（比特翻转） — $\begin{pmatrix}0&1\\1&0\end{pmatrix}$
- **Z**：Pauli Z（相位翻转） — $\begin{pmatrix}1&0\\0&{-1}\end{pmatrix}$
- **Y**：Pauli Y（混合翻转） — $\begin{pmatrix}0&{-i}\\i&0\end{pmatrix}$
- **H**：Hadamard 门 — $\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&{-1}\end{pmatrix}$
- **S**：$\pi/2$ 相位门 — $\text{diag}(1,\;i) = \sqrt{Z}$
- **T**：$\pi/4$ 相位门 — $\text{diag}(1,\;e^{i\pi/4}) = \sqrt{S}$
- **R_{\hat{n}}(\theta)**：旋转门 — $\cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}(\hat{n}\cdot\vec{\sigma})$
- **Euler 分解**：任意单比特门 — $U = e^{i\alpha}R_z(\beta)R_y(\gamma)R_z(\delta)$


---

## 🔗 相关笔记

- [[Qubit-State-and-Superposition]] — 叠加态的本质、相位因子的物理含义、Bloch 球参数化
- [[Pauli-Matrices]] — X, Y, Z 矩阵的代数性质、对易关系、反对易关系
- [[Gate-Eigenstates]] — Pauli 门的本征态与本征值，QEC 稳定子的基础
- [[Rabi-Flopping]] — 单比特门的物理实现机制：激光脉冲驱动的相干振荡
- [[Two-Qubit-Gates]] — 两比特门总览：与单比特门组合构成通用门集
- [[CZ-Gate]] — CZ 门的详细性质与里德堡阻塞实现
- [[Rydberg-Blockade]] — 两比特门（CZ）的物理实现机制
- [[Optical-Tweezer-Arrays]] — 单比特门的硬件平台
- [[Tensor-Product]] — 多 qubit 系统中单比特门的扩展方式
- [[Transversal-Teleportation]] — T 门等非横向门的容错实现方案

## 📝 更新记录

- 2026-06-01: 初始创建，包含 Pauli 门、H 门、S/T 门、旋转门、Bloch 球、中性原子实现
