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
> 本笔记系统介绍单比特门的定义、标准门集、Bloch 球几何图像以及在中性原子体系中的物理实现。

---

## 1. 什么是单量子比特门？

### 1.1 核心定义

单量子比特门是对**单个 qubit** 施加的量子操作，数学上是一个 $2\times2$ 的**酉矩阵** $U$：

$$
U^\dagger U = UU^\dagger = I
$$

> [!tip] 为什么必须是酉矩阵？
> 酉性保证了概率守恒——变换前后 $|\langle\psi|\psi\rangle| = 1$ 不变。如果 $U$ 不是酉的，就会出现"概率凭空消失或增加"的荒谬结果。这与经典概率守恒是同一个道理。

对一个一般量子态的作用：

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle \quad \xrightarrow{U} \quad U|\psi\rangle = \alpha'|0\rangle + \beta'|1\rangle
$$

### 1.2 与经典逻辑门的对比

| | 经典逻辑门 | 量子单比特门 |
|--|----------|------------|
| 作用对象 | 经典 bit（0 或 1） | qubit（叠加态） |
| 可逆性 | 不可逆（如 AND 丢失信息） | **必须可逆**（酉性） |
| 效果 | 确定性映射 | 旋转叠加态的幅度和相位 |
| 组合 | 构建经典电路 | 与 [[CZ门 (CZ Gate)|两比特门]] 组合构建量子电路 |

> [!info] 量子计算的门集模型
> 任意量子计算可以分解为：**单比特门 + 两比特门**的序列。单比特门负责"精细调节"每个 qubit 的状态（旋转角度和相位），两比特门（如 CZ）负责建立 qubit 之间的**纠缠**。两者缺一不可。

---

## 2. 标准单比特门：Pauli 门

详细性质见 [[泡利矩阵 (Pauli Matrices)]]，这里聚焦于它们**作为量子门**的直觉。

### 2.1 X 门（量子 NOT 门）

$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

作用：翻转量子态——$|0\rangle \leftrightarrow |1\rangle$

$$
X|0\rangle = |1\rangle, \quad X|1\rangle = |0\rangle, \quad X(\alpha|0\rangle + \beta|1\rangle) = \beta|0\rangle + \alpha|1\rangle
$$

> [!tip] 物理直觉
> X 门就是量子世界的"拨开关"——把 $|0\rangle$ 拨到 $|1\rangle$，把 $|1\rangle$ 拨到 $|0\rangle$。对叠加态来说，它**交换**了两个分量的权重。

在 Bloch 球上：绕 $x$ 轴旋转 $\pi$。

### 2.2 Z 门（相位翻转）

$$
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

作用：给 $|1\rangle$ 分量加一个 $\pi$ 相位（$-1 = e^{i\pi}$），$|0\rangle$ 分量不变

$$
Z|0\rangle = |0\rangle, \quad Z|1\rangle = -|1\rangle, \quad Z(\alpha|0\rangle + \beta|1\rangle) = \alpha|0\rangle - \beta|1\rangle
$$

> [!warning] Z 门不改变测量概率
> 对纯态 $|\psi\rangle$ 施加 Z 门后，测量得到 $|0\rangle$ 或 $|1\rangle$ 的概率**不变**（因为 $|\alpha|^2 = |\alpha|^2$，$|\beta|^2 = |- \beta|^2$）。Z 只改变**相对相位**，不改变概率分布。这是"相位翻转"这个名字的由来——它翻转的是相位，不是概率。

在 Bloch 球上：绕 $z$ 轴旋转 $\pi$。

### 2.3 Y 门

$$
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = iXZ
$$

作用：同时翻转比特和相位

$$
Y|0\rangle = i|1\rangle, \quad Y|1\rangle = -i|0\rangle
$$

在 Bloch 球上：绕 $y$ 轴旋转 $\pi$。

> [!info] 三个 Pauli 门的关系
> X、Y、Z 之间有简洁的代数关系：$Y = iXZ$，$X^2 = Y^2 = Z^2 = I$（连续施加两次等于不做任何操作）。这三个门加上 $I$（恒等门）构成 $2\times2$ 矩阵空间的完备基——任意酉门都可以用它们的组合表示。

---

## 3. Hadamard 门：制造叠加

$$
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

这是**量子计算中最重要的单比特门之一**：

$$
H|0\rangle = |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \quad H|1\rangle = |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
$$

> [!tip] 物理直觉：H 门是"均衡器"
> H 门把确定态（$|0\rangle$ 或 $|1\rangle$）变成**完全均衡的叠加态**——测量得到 0 和 1 的概率各 50%。反过来，H 门也把叠加态"收敛"回确定态。它就像一个均衡器，把所有输入都调到最均匀的分布。

在 Bloch 球上：H 门将 $z$ 轴上的态旋转到 $x$ 轴上的态（$|0\rangle \to |+\rangle$），相当于绕 $(x+z)/\sqrt{2}$ 轴旋转 $\pi$。

**H 门的自反性**：$HH = I$（施加两次 H 门等于什么都没做）。这说明 H 门是自己的逆操作——"把叠加态变回确定态，再变一次就回到原来的确定态"。

---

## 4. 相位门：S 门与 T 门

### 4.1 S 门（$\pi/2$ 相位门）

$$
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} = \sqrt{Z}
$$

作用：给 $|1\rangle$ 分量加 $i = e^{i\pi/2}$ 相位

$$
S|0\rangle = |0\rangle, \quad S|1\rangle = i|1\rangle
$$

> S 门可以理解为"半个 Z 门"——Z 门加 $\pi$ 相位（$-1$），S 门加 $\pi/2$ 相位（$i$）。连续施加两次 S 门等于 Z 门：$S^2 = Z$。

### 4.2 T 门（$\pi/4$ 相位门）

$$
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} = \sqrt{S}
$$

作用：给 $|1\rangle$ 分量加 $e^{i\pi/4}$ 相位

> [!warning] T 门的特殊地位
> T 门是容错量子计算中最"昂贵"的门——它**无法横向实现**（受 [[横向纠缠门 (Transversal Gate)|Eastin-Knill 定理]] 限制），必须通过 [[横向隐形传态 (Transversal Teleportation)|Gate Teleportation]] + magic state distillation 来实现。蒸馏一个高保真度的 T 门 magic state 是整个容错量子计算中最耗资源的环节。

### 4.3 相位门家族总览

| 门 | 矩阵 | 相位偏移 | 与 Z 的关系 |
|---|---|---|---|
| $Z$ | $\text{diag}(1, -1)$ | $\pi$ | $Z$ |
| $S = Z^{1/2}$ | $\text{diag}(1, i)$ | $\pi/2$ | $S^2 = Z$ |
| $T = Z^{1/4}$ | $\text{diag}(1, e^{i\pi/4})$ | $\pi/4$ | $T^2 = S$，$T^4 = Z$ |

> [!tip] 记忆技巧
> 相位门家族就是 $Z$ 门的"分数次幂"：$Z^{1/1} = Z$，$Z^{1/2} = S$，$Z^{1/4} = T$。指数越小，每步转的相位越小，电路越精细。

---

## 5. 旋转门：连续可调的单比特门

Pauli 门只做 $\pi$ 旋转（翻转），但实际量子计算中经常需要**任意角度**的旋转。这就是旋转门 $R_x(\theta)$、$R_y(\theta)$、$R_z(\theta)$ 的用武之地。

### 5.1 一般旋转门公式

绕 $\hat{n}$ 轴旋转 $\theta$ 角：

$$
R_{\hat{n}}(\theta) = e^{-i\frac{\theta}{2}(\hat{n}\cdot\vec{\sigma})} = \cos\frac{\theta}{2} \cdot I - i\sin\frac{\theta}{2}(n_x X + n_y Y + n_z Z)
$$

> [!warning] 为什么是 $\theta/2$ 而不是 $\theta$？
> 量子态生活在**复射影空间**（Bloch 球），不是普通三维空间。Bloch 球上转 $\theta$ 角，希尔伯特空间中只需 $\theta/2$——这是量子力学的双倍覆盖（double cover）特性。$\pi$ 脉冲对应 Bloch 球转半圈（$\theta = \pi$），在希尔伯特空间中只转了 $\pi/2$。

三个基本旋转门的矩阵形式：

$$
R_x(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

$$
R_y(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

$$
R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
$$

### 5.2 特殊角度对应的门

| 旋转 | 角度 | 对应的标准门 | 效果 |
|------|------|------------|------|
| $R_x(\pi)$ | $\pi$ | $-iX$ | 完全翻转（差全局相位 $-i$） |
| $R_x(\pi/2)$ | $\pi/2$ | Hadamard 的近亲 | 将 $|0\rangle$ 旋转到 $x$ 轴赤道 |
| $R_z(\pi)$ | $\pi$ | $-iZ$ | 相位完全翻转 |
| $R_z(\pi/2)$ | $\pi/2$ | $-iS$ | $\pi/2$ 相位偏移 |

> [!info] 与拉比振荡的直接联系
> 在 Rydberg 原子实验中，$R_x(\theta)$ 通过激光脉冲驱动实现：脉冲持续时间 $t$ 决定旋转角度 $\theta = \Omega t$（$\Omega$ 是拉比频率）。
> - $\theta = \pi$ → **$\pi$ 脉冲**（完全翻转 $|g\rangle \leftrightarrow |r\rangle$）
> - $\theta = \pi/2$ → **$\pi/2$ 脉冲**（制备叠加态）
>
> 详见 [[拉比振荡 (Rabi Flopping)]]。

### 5.3 Euler 分解：任意单比特门 = 三次旋转

**定理**：任意 $2\times2$ 酉矩阵 $U$ 都可以分解为三个基本旋转门的乘积：

$$
U = e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)
$$

其中 $\alpha, \beta, \gamma, \delta$ 是四个实参数。

> [!tip] 物理直觉
> 这就像三维空间中任何旋转都可以分解为绕三个轴的连续旋转。在 Bloch 球上，任何单比特门就是把一个点旋转到另一个点——而绕 $z$ 轴和 $y$ 轴的交替旋转足以覆盖整个球面。

---

## 6. Bloch 球几何图像

### 6.1 单比特态的 Bloch 球表示

任何单 qubit 纯态可以参数化为：

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle
$$

对应 Bloch 球面上的点 $(\theta, \phi)$：

| 态 | Bloch 球位置 | 含义 |
|---|------------|------|
| $\|0\rangle$ | 北极 $(\theta=0)$ | Z 本征值 +1 |
| $\|1\rangle$ | 南极 $(\theta=\pi)$ | Z 本征值 -1 |
| $\|+\rangle$ | $x$ 轴正方向 | X 本征值 +1 |
| $\|-\rangle$ | $x$ 轴负方向 | X 本征值 -1 |
| $\|+i\rangle$ | $y$ 轴正方向 | Y 本征值 +1 |
| $\|-i\rangle$ | $y$ 轴负方向 | Y 本征值 -1 |

### 6.2 单比特门的几何意义

| 门 | Bloch 球上的操作 |
|---|----------------|
| $X$ | 绕 $x$ 轴转 $\pi$ |
| $Y$ | 绕 $y$ 轴转 $\pi$ |
| $Z$ | 绕 $z$ 轴转 $\pi$ |
| $H$ | 绕 $(x+z)/\sqrt{2}$ 轴转 $\pi$ |
| $R_x(\theta)$ | 绕 $x$ 轴转 $\theta$ |
| $R_y(\theta)$ | 绕 $y$ 轴转 $\theta$ |
| $R_z(\theta)$ | 绕 $z$ 轴转 $\theta$ |

> [!tip] 统一视角
> 所有单比特门的本质都是**在 Bloch 球上做旋转**。区别只是旋转轴和旋转角度不同。Pauli 门做 $\pi$ 旋转（翻转到对面），相位门做 $z$ 轴旋转，H 门做特殊轴的 $\pi$ 旋转。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig = plt.figure(figsize=(14, 5))

# --- Left panel: Bloch sphere with gate actions ---
ax1 = fig.add_subplot(121, projection='3d')

# Draw sphere wireframe
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 20)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))
ax1.plot_surface(x, y, z, alpha=0.05, color='#1f77b4', edgecolor='gray', linewidth=0.3)

# Axes
ax1.quiver(0, 0, 0, 1.5, 0, 0, color='gray', arrow_length_ratio=0.08, lw=1)
ax1.quiver(0, 0, 0, 0, 1.5, 0, color='gray', arrow_length_ratio=0.08, lw=1)
ax1.quiver(0, 0, 0, 0, 0, 1.5, color='gray', arrow_length_ratio=0.08, lw=1)
ax1.text(1.6, 0, 0, r'$x$', fontsize=11, color='gray')
ax1.text(0, 1.6, 0, r'$y$', fontsize=11, color='gray')
ax1.text(0, 0, 1.6, r'$|0\rangle$', fontsize=11, color='#1f77b4', fontweight='bold')
ax1.text(0, 0, -1.6, r'$|1\rangle$', fontsize=11, color='#d62728', fontweight='bold')

# Mark key states
key_states = {
    r'$|+\rangle$': (1, 0, 0),
    r'$|-\rangle$': (-1, 0, 0),
    r'$|+i\rangle$': (0, 1, 0),
    r'$|-i\rangle$': (0, -1, 0),
}
for label, (sx, sy, sz) in key_states.items():
    ax1.scatter(sx, sy, sz, color='#ff7f0e', s=40, zorder=5)

ax1.text(1.1, 0.2, 0.2, r'$|+\rangle$', fontsize=9, color='#ff7f0e')
ax1.text(-1.4, 0.2, 0.2, r'$|-\rangle$', fontsize=9, color='#ff7f0e')
ax1.text(0.2, 1.1, 0.2, r'$|{+i}\rangle$', fontsize=9, color='#ff7f0e')

# Z rotation arrow (blue arc)
theta_z = np.linspace(0, np.pi, 30)
x_arc = 0.3 * np.cos(theta_z)
y_arc = 0.3 * np.sin(theta_z)
z_arc = np.full_like(theta_z, 0.8)
ax1.plot(x_arc, y_arc, z_arc, color='#1f77b4', lw=2)
ax1.text(0.1, 0.35, 0.85, r'$R_z$', fontsize=9, color='#1f77b4', fontweight='bold')

ax1.set_xlim(-1.8, 1.8)
ax1.set_ylim(-1.8, 1.8)
ax1.set_zlim(-1.8, 1.8)
ax1.set_title('Bloch Sphere & Gate Actions', fontsize=12, fontweight='bold', pad=0)
ax1.view_init(elev=15, azim=30)
ax1.set_axis_off()

# --- Right panel: Gate summary table as visual ---
ax2 = fig.add_subplot(122)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 8)
ax2.axis('off')
ax2.set_title('Single-Qubit Gate Cheat Sheet', fontsize=12, fontweight='bold', pad=10)

gates = [
    (r'$X$', r'$\begin{pmatrix}0&1\\1&0\end{pmatrix}$', r'NOT / flip', '#1f77b4'),
    (r'$Z$', r'$\begin{pmatrix}1&0\\0&{-1}\end{pmatrix}$', r'Phase flip', '#d62728'),
    (r'$H$', r'$\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&{-1}\end{pmatrix}$', r'Make superposition', '#2ca02c'),
    (r'$S$', r'$\begin{pmatrix}1&0\\0&i\end{pmatrix}$', r'$\pi/2$ phase', '#ff7f0e'),
    (r'$T$', r'$\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}$', r'$\pi/4$ phase', '#9467bd'),
    (r'$R_x(\theta)$', r'$\cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}X$', r'Rotate x-axis', '#17becf'),
]

y_start = 7.2
for i, (name, mat, desc, col) in enumerate(gates):
    y = y_start - i * 1.2
    # Gate name
    ax2.add_patch(mpatches.FancyBboxPatch((0.2, y - 0.35), 1.5, 0.7,
                 boxstyle='round,pad=0.1', facecolor=col, edgecolor='black',
                 linewidth=1.5, alpha=0.8))
    ax2.text(0.95, y, name, ha='center', va='center', fontsize=11,
            color='white', fontweight='bold')
    # Matrix
    ax2.text(3.5, y, mat, ha='center', va='center', fontsize=9, color='#333')
    # Description
    ax2.text(7.5, y, desc, ha='center', va='center', fontsize=10, color=col, fontweight='bold')

ax2.text(5, -0.3, r'$\bullet$ All gates are unitary: $U^\dagger U = I$', fontsize=9,
        ha='center', color='gray', style='italic')

plt.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.08, wspace=0.3)
plt.show()
```

---

## 7. 在中性原子体系中的实现

在 [[光镊阵列 (Optical Tweezer Arrays)]] 平台中，单比特门通过**激光脉冲**驱动原子的内态跃迁来实现。

### 7.1 物理机制

两个量子比特编码在原子的两个超精细基态 $|0\rangle = |g\rangle$ 和 $|1\rangle = |e\rangle$ 中。单比特门通过驱动 $|g\rangle \leftrightarrow |e\rangle$ 的受激拉曼跃迁实现：

$$
H_{\text{eff}} = \frac{\Omega}{2}(|g\rangle\langle e| + |e\rangle\langle g|) + \frac{\Delta}{2}(|e\rangle\langle e| - |g\rangle\langle g|)
$$

其中 $\Omega$ 是拉比频率，$\Delta$ 是失谐。

| 参数 | 控制方式 | 实现的门 |
|------|---------|---------|
| 脉冲面积 $\theta = \Omega t$ | 控制脉冲持续时间 $t$ | 旋转角度 $\theta$ |
| 旋转轴 | 控制激光偏振和相位 | $R_x$、$R_y$ 或 $R_z$ |
| 共振 vs 失谐 | 调节激光频率 | 纯旋转 vs AC Stark 相位 |

> [!info] 关键参数（Bluvstein et al., 2026）
> - 单比特门保真度：$\sim 99.5\%$
> - 门操作时间：$\sim 0.3\,\mu\text{s}$
> - 实现方式：全局微波脉冲（所有原子同时接受相同操作）
>
> 单比特门保真度通常**高于**两比特门，因为单比特门不涉及原子间相互作用，退相干是唯一的错误源。

### 7.2 常用操作与对应脉冲

| 量子门操作 | 脉冲序列 | 实验含义 |
|-----------|---------|---------|
| $\|0\rangle \to \|1\rangle$ | $\pi$ 脉冲（$R_x(\pi)$） | 完全激发 |
| $\|0\rangle \to \|+\rangle$ | $\pi/2$ 脉冲（$R_x(\pi/2)$） | 制备叠加态 |
| 纯相位偏移 | 失谐脉冲（$R_z(\theta)$） | AC Stark 相移 |
| Hadamard | $\pi/2$ 脉冲 + $z$ 旋转 | 组合实现 |

> [!tip] 为什么中性原子偏好 CZ 而非 CNOT？
> 两比特门 [[CZ门 (CZ Gate)|CZ]] 可以直接通过 [[里德堡阻塞 (Rydberg Blockade)|Rydberg blockade]] 一步实现，而 CNOT 需要额外的 H 门来转换。但在**线路编译**时，单比特门（H、S、T 等）仍然不可或缺——它们负责将通用量子算法的逻辑线路转化为硬件可执行的脉冲序列。

---

## 8. 单比特门与量子线路

### 8.1 通用量子计算的门集

**Solovay-Kitaev 定理**：$\{H, T, \text{CZ}\}$ 构成**通用门集**——任何量子线路都可以用这三种门的组合以任意精度近似。

$$
\text{任意酉门 } U \approx \prod_{k} U_k^{(H, T, \text{CZ})}
$$

其中：
- **H 门 + T 门**：单比特门，负责所有单 qubit 旋转
- **CZ 门**：两比特门，负责建立纠缠

> [!warning] T 门数量决定资源开销
> 在容错量子计算中，**T 门的数量**是衡量线路资源开销的关键指标——每个 T 门都需要一次完整的 magic state distillation。优化量子线路的一个重要目标就是**减少 T 门数量**（T-count optimization）。

### 8.2 单比特门的角色总结

```
量子线路 = [单比特门] + [两比特门] + [单比特门] + [两比特门] + ...
              ↑            ↑
           精细调节       建立纠缠
          (旋转/相位)    (CZ/CNOT)
```

| 角色 | 由谁完成 | 作用 |
|------|---------|------|
| 状态初始化 | $R_x(\pi/2)$ | 将 $\|0\rangle$ 转为叠加态 |
| 算法逻辑 | $H, S, T, R_z(\theta)$ | 量子线路的"指令集" |
| 纠缠前准备 | 单比特门 | 将各 qubit 调到合适角度 |
| 纠缠建立 | [[CZ门 (CZ Gate)]] | 建立 qubit 间的量子关联 |
| 测量前旋转 | $R_x(\theta), R_y(\theta)$ | 将目标态旋转到测量基 |

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|------|------|------|
| $X$ | Pauli X（比特翻转） | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ |
| $Z$ | Pauli Z（相位翻转） | $\begin{pmatrix}1&0\\0&{-1}\end{pmatrix}$ |
| $Y$ | Pauli Y | $\begin{pmatrix}0&{-i}\\i&0\end{pmatrix} = iXZ$ |
| $H$ | Hadamard 门 | $\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&{-1}\end{pmatrix}$ |
| $S$ | $\pi/2$ 相位门 | $\text{diag}(1, i) = \sqrt{Z}$ |
| $T$ | $\pi/4$ 相位门 | $\text{diag}(1, e^{i\pi/4}) = \sqrt{S}$ |
| $R_{\hat{n}}(\theta)$ | 一般旋转门 | $\cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}(\hat{n}\cdot\vec{\sigma})$ |
| Euler 分解 | 任意单比特门 | $U = e^{i\alpha}R_z(\beta)R_y(\gamma)R_z(\delta)$ |

---

## 🔗 相关笔记

- [[泡利矩阵 (Pauli Matrices)]] — X, Y, Z 矩阵的代数性质、对易关系、反对易关系
- [[门算符本征态 (Gate Eigenstates)]] — Pauli 门的本征态与本征值，QEC 稳定子的基础
- [[拉比振荡 (Rabi Flopping)]] — 单比特门的物理实现机制：激光脉冲驱动的相干振荡
- [[CZ门 (CZ Gate)]] — 两比特门：与单比特门组合构成通用门集
- [[里德堡阻塞 (Rydberg Blockade)]] — 两比特门（CZ）的物理实现机制
- [[光镊阵列 (Optical Tweezer Arrays)]] — 单比特门的硬件平台
- [[张量积 (Tensor Product)]] — 多 qubit 系统中单比特门的扩展方式
- [[横向隐形传态 (Transversal Teleportation)]] — T 门等非横向门的容错实现方案

## 📝 更新记录

- 2026-06-01: 初始创建，包含 Pauli 门、H 门、S/T 门、旋转门、Bloch 球、中性原子实现、Python 图表
