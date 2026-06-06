---
aliases: [Rabi Flopping, Rabi Oscillation, 拉比振荡, 拉比频率, Ω]
tags: [Physics, Quantum, NeutralAtom, RydbergAtom, Dynamics]
date: 2026-03-29
status: WIP
source: "[[generall quantum 2026]]"
comprehension: "vague"
---

# 拉比振荡（Rabi Flopping / Rabi Oscillation）

> 📄 来源文献：[[generall quantum 2026]] · 原始批注见 [p.40](zotero://select/library/items/SL8QGCV5)

> 来源批注：*"Rabi oscillation"* — Bluvstein et al., 2026, p.40

## 1. 物理直觉：什么是拉比振荡？

想象一个二能级原子，在共振激光的驱动下，原子会在基态 $\vert g\rangle$ 和激发态 $\vert e\rangle$ 之间**周期性地来回振荡**，就像一个钟摆在两个态之间摆动。这种现象就是**拉比振荡**（Rabi Flopping）。

这是量子光学中最基础的相干驱动现象，也是所有量子比特操控的物理基础。

> [!tip] 钟摆类比
> 拉比振荡就像一个量子钟摆：原子在 $\vert g\rangle$ 和 $\vert e\rangle$ 之间来回摆动。摆动的速度由拉比频率 $\Omega$ 决定——激光越强，摆动越快。完成一次完整的摆动（$\vert g\rangle \to \vert e\rangle \to \vert g\rangle$）需要时间 $2\pi/\Omega$。

## 2. 哈密顿量与方程推导

考虑一个二能级系统（$\vert 0\rangle, \vert 1\rangle$）受到频率为 $\omega_L$ 的驱动场，系统哈密顿量为（旋转波近似, RWA）：

> [!info] 什么是旋转波近似（RWA）？
> 驱动场与原子相互作用的完整哈密顿量包含两项振荡项：一项以 $(\omega_L + \omega_0)$ 快速振荡（反旋转项），一项以 $(\omega_L - \omega_0)$ 缓慢振荡（旋转项）。RWA 忽略快振荡的反旋转项（因为它在时间平均下几乎为零），只保留慢振荡的旋转项。这使得哈密顿量在旋转 frame 中变为**不含时**的简洁形式，是求解拉比振荡的前提。

$$
\hat{H} = \frac{\hbar}{2}\begin{pmatrix} -\Delta & \Omega \\ \Omega^* & \Delta \end{pmatrix}
$$


^nu260605 这里哈密顿量由来没懂

其中：
- $\Omega$：**拉比频率**（Rabi frequency），由驱动场强度和原子跃迁偶极矩决定，$\Omega = \frac{d \cdot E_0}{\hbar}$ ^1212
- $\Delta = \omega_L - \omega_0$：**失谐量**（detuning），激光频率与原子共振频率之差

### $\Omega$ 到底和什么有关？——光强 vs 频率

公式 $\Omega = d \cdot E_0 / \hbar$ 中三个量的角色：

| 符号 | 含义 | 谁决定的？ |
|------|------|-----------|
| $d$ | 跃迁偶极矩（transition dipole moment） | **原子本身**——不同跃迁的 $d$ 值不同，是原子的固有属性 |
| $E_0$ | 激光电场的振幅 | **激光强度**——实验中可调节的参数 |
| $\hbar$ | 约化普朗克常数 | 常数，不变 |

**直接决定 $\Omega$ 大小的是 $E_0$（电场振幅），而 $E_0$ 由激光强度决定。**

激光强度 $I$（单位面积功率）与电场振幅的关系为：

$$
I = \frac{1}{2}\varepsilon_0 c\, E_0^2
$$

因此 $E_0 \propto \sqrt{I}$，代入得：

$$
\boxed{\Omega \propto \sqrt{I}}
$$

**拉比频率正比于光强的平方根**。光强越大 → 电场越强 → 原子被驱动得越快 → 拉比振荡越快。例如光强翻倍（×2），$\Omega$ 增大为原来的 $\sqrt{2} \approx 1.41$ 倍，振荡周期缩短约 30%。

![[rabi_freq_vs_intensity]]

> [!warning] 激光频率 $\omega_L$ 不影响 $\Omega$
> 激光频率 $\omega_L$ **不出现在 $\Omega$ 的公式里**。它的作用体现在另一个量——失谐量 $\Delta = \omega_L - \omega_0$。
>
> - **$\Omega$ 告诉你"驱动有多强"**（→ 振荡幅度能达到多大）
> - **$\Delta$ 告诉你"频率匹配有多好"**（→ 振荡的实际效率）
>
> 两者共同决定广义拉比频率 $\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$，见下方[[#非共振情形（$\Delta \neq 0$）]]。

> [!tip] 实验直觉
> 想让原子翻转更快？→ 加大激光功率（增大 $I$ → 增大 $\Omega$）
> 想让翻转效率最高（$P \to 1$）？→ 把激光频率调到共振（$\Delta = 0$）
> **这两个调节是独立的**——功率管速度，频率管效率。

### 各物理量详解：谁决定了什么？

把拉比振荡涉及的所有物理量拆开来看，它们分为两大阵营：**"原子说了算"** 和 **"实验者说了算"**。

#### 1. $\omega_0$：原子共振频率——由原子内部结构决定

$\omega_0$ 是两个量子态之间的**能量差对应的频率**：

$$
\omega_0 = \frac{E_e - E_g}{\hbar}
$$

它是原子的"指纹"——每种原子、每对能级都有特定的 $\omega_0$，实验者无法改变它（除非施加外场修正，见下文）。具体来说，$\omega_0$ 的大小由以下层层叠加的物理效应决定：

**① 玻尔能级（主框架）**

原子能级的粗略图像来自库仑势中电子的量子化能级：

$$
E_n = -\frac{13.6\,\text{eV}}{n^2}
$$

对于氢原子或类氢离子，共振频率正比于 $1/n_1^2 - 1/n_2^2$。例如氢原子 Balmer 系（$n=2 \to n=3,4,\dots$）的可见光跃迁就来自这一层。

但对于多电子原子（如实验常用的 Rb、Cs），电子间的屏蔽和关联使能级偏离简单的 $1/n^2$ 规律，需要用更精确的量子力学计算或实验测量来确定。

**② [[Fine-Structure|精细结构（Fine Structure）]]——你学过的自旋-轨道耦合**

> [!info] 前置知识回顾
> 这一层你在 [[Zeeman-Effect]] 和原子物理课中已经学过：自旋-轨道耦合 $\hat{H}_{SO} \propto \hat{\mathbf{L}} \cdot \hat{\mathbf{S}}$ 把主能级分裂为不同 $j$ 的[[Fine-Structure|精细结构]]子能级。

[[Fine-Structure|精细结构]]将一个主能级 $n$ 分裂为多个 $j$ 不同的子能级。以 Rb-87 的 D2 线为例：

- 基态：$5S_{1/2}$（$j = 1/2$）
- 激发态：$5P_{3/2}$（$j = 3/2$）
- **$\omega_0 \approx 2\pi \times 384.23\,\text{THz}$**（对应波长 $\lambda \approx 780\,\text{nm}$，近红外）

[[Fine-Structure|精细结构分裂]]的典型能量在 $\sim 0.01$–$0.1\,\text{eV}$ 量级，对应的频率差异在 $\sim$THz 量级。

**③ [[Hyperfine-Structure|超精细结构（Hyperfine Structure）]]——你学过的核自旋耦合**

> [!info] 前置知识回顾
> 原子核的自旋 $\hat{\mathbf{I}}$ 与电子总角动量 $\hat{\mathbf{J}}$ 的耦合 $\hat{H}_{HFS} \propto \hat{\mathbf{I}} \cdot \hat{\mathbf{J}}$，将[[Fine-Structure|精细结构]]子能级进一步分裂为[[Hyperfine-Structure|超精细]]子能级（不同总角动量 $F$）。

[[Hyperfine-Structure|超精细分裂]]将每个[[Fine-Structure|精细结构]]能级再拆成多个 $F$ 子能级。以 Rb-87 为例（核自旋 $I = 3/2$）：

- $5S_{1/2}$ 分裂为 $F = 1$ 和 $F = 2$，间隔约 **$6.835\,\text{GHz}$**
- $5P_{3/2}$ 分裂为 $F = 0,1,2,3$，间隔在 $\sim$MHz–hundreds of MHz 量级

中性原子量子计算中，量子比特通常定义在**[[Hyperfine-Structure|超精细基态]]**之间（如 Rb-87 的 $\vert F=1\rangle$ 和 $\vert F=2\rangle$），这两个态之间的微波跃迁频率就是 $\sim 6.835\,\text{GHz}$。

> [!tip] 量子比特的 $\omega_0$ 从哪来
> 如果量子比特用两个[[Hyperfine-Structure|超精细基态]]定义（$\vert 0\rangle = \vert F=1\rangle$，$\vert 1\rangle = \vert F=2\rangle$），那么驱动单比特门的"共振频率"就是[[Hyperfine-Structure|超精细分裂频率]] $\omega_0 \sim 6.8\,\text{GHz}$（微波波段）。如果要把原子激发到里德堡态，$\omega_0$ 则是光学跃迁频率 $\sim 384\,\text{THz}$（近红外）。**不同的跃迁通道，$\omega_0$ 差了好几个数量级。**

**④ 外场修正（实验中可调）**

| 外场 | 物理效应 | 对 $\omega_0$ 的修正 | 典型量级 |
|------|---------|---------------------|---------|
| 外磁场 $B$ | [[Zeeman-Effect]] | $\Delta E = g_F m_F \mu_B B$ | MHz–GHz（取决于 $B$ 强度和 $g_F$） |
| 外电场 $F$ | [[AC-Stark-Effect]]（光位移） | 能级移动 $\propto I/\Delta$ | MHz–GHz（取决于激光强度和失谐） |

所以 $\omega_0$ 并非完全不可调——通过磁场和光场可以做微调。但这些都是在原子固有频率的**基础上做小幅修正**，不能从根本上改变 $\omega_0$。

#### 2. $\omega_L$：激光频率——实验者自由调节

$\omega_L$ 是驱动激光的频率，**完全由实验者控制**——转动激光器的旋钮就能改变它。实验的核心操作之一就是把 $\omega_L$ 调到尽可能接近 $\omega_0$（共振条件 $\Delta = 0$）。

在中性原子实验中：
- **单比特门**：用微波源驱动超精细跃迁，$\omega_L \approx 6.8\,\text{GHz}$
- **里德堡激发**：用近红外激光（780 nm + 480 nm 两光子方案），$\omega_L$ 在光学频段

#### 3. $d$：跃迁偶极矩——由跃迁的量子数决定

跃迁偶极矩衡量"这个跃迁对光场有多敏感"：

$$
d = \vert\langle e\vert\, q\hat{r}\,\vert g\rangle\vert
$$

它是电荷 $q$ 乘以两个态之间位置算符的矩阵元。决定 $d$ 大小的因素：

- **跃迁的角动量选择定则**：满足 $\Delta l = \pm 1$ 的跃迁 $d$ 较大（"允许跃迁"）；违反选择定则的跃迁 $d \approx 0$（"禁戒跃迁"）
- **主量子数 $n$**：[[Rydberg-Blockade|里德堡态]]的 $d$ 随 $n^2$ 增长，因为高激发态电子离核很远，波函数空间分布广
- **具体态的量子数**：不同 $m_j$、$m_F$ 子态之间的跃迁 $d$ 值不同

> [!tip] [[Rydberg-Blockade|里德堡态]]的特殊之处
> [[Rydberg-Blockade|里德堡跃迁]]（$n \sim 50$–$100$）的偶极矩 $d \propto n^2$，比普通光学跃迁大几百倍。这意味着**同样的激光功率下，[[Rydberg-Blockade|里德堡态]]的拉比频率可以非常大**——这是中性原子平台的一个优势。

#### 4. $E_0$：电场振幅——实验者通过激光功率调节

$E_0$ 是激光电场的峰值振幅，和激光功率（强度）的关系见上方公式。实验中通过衰减片或调节激光器输出功率来控制 $E_0$。

#### 总结：一张图理清所有量的"控制权"

> [!example] 控制权速查表
> | 物理量 | 决定者 | 实验者能调吗？ | 调节方式 |
> |--------|--------|:--------------:|---------|
> | $\omega_0$ | 原子能级结构 | ⚠️ 只能微调 | 外磁场（Zeeman）/ 光场（AC Stark） |
> | $\omega_L$ | 实验者 | ✅ 自由调 | 改变激光频率 |
> | $d$ | 原子跃迁类型 | ❌ 换跃迁才行 | 选择不同的跃迁通道 |
> | $E_0$ | 实验者 | ✅ 自由调 | 改变激光功率 |
> | $\Omega$ | $d$ 和 $E_0$ 的综合 | ✅ 间接调 | 主要通过调 $E_0$（功率） |
> | $\Delta$ | $\omega_L$ 和 $\omega_0$ 的差 | ✅ 间接调 | 通过调 $\omega_L$ |

^nu260605 频率这一块没认真看
### 共振情形（$\Delta = 0$）

共振意味着激光频率恰好等于原子跃迁频率：$\omega_L = \omega_0$，即 $\Delta = 0$。这时驱动场与原子"完美匹配"，布居转移效率最高。

#### Step 1：写出共振哈密顿量

将 $\Delta = 0$ 代入一般形式：

$$
\hat{H}_{\text{res}} = \frac{\hbar}{2}\begin{pmatrix} 0 & \Omega \\ \Omega^* & 0 \end{pmatrix}
$$

为了推导简便，假设 $\Omega$ 为实数（通过选择合适的激光相位可以做到这一点），于是：

$$
\hat{H}_{\text{res}} = \frac{\hbar\Omega}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \frac{\hbar\Omega}{2}\hat{\sigma}_x
$$

其中 $\hat{\sigma}_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ 是 [[Pauli-Matrices|Pauli-X 矩阵]]。

> [!tip] 物理直觉
> 共振时哈密顿量正比于 $\hat{\sigma}_x$，意味着驱动场的作用就是绕 Bloch 球的 $x$ 轴旋转——这正是 [[Single-Qubit-Gates]] 中 $R_x$ 门的物理来源！

#### Step 2：写出含时薛定谔方程

系统的时间演化服从**含时薛定谔方程**（TDSE）：

$$
i\hbar\frac{d}{dt}\vert\psi(t)\rangle = \hat{H}\vert\psi(t)\rangle
$$

设 $t$ 时刻的态为：

$$
\vert\psi(t)\rangle = c_0(t)\vert 0\rangle + c_1(t)\vert 1\rangle
$$

其中 $c_0(t)$ 和 $c_1(t)$ 是**随时间变化的复数振幅**（probability amplitudes）。初始条件为原子处于基态：

$$
c_0(0) = 1, \quad c_1(0) = 0
$$

#### Step 3：将薛定谔方程展开为方程组

把态矢代入 TDSE：

$$
i\hbar\frac{d}{dt}\bigl(c_0\vert 0\rangle + c_1\vert 1\rangle\bigr) = \frac{\hbar\Omega}{2}\hat{\sigma}_x\bigl(c_0\vert 0\rangle + c_1\vert 1\rangle\bigr)
$$

左边对时间求导（$\vert 0\rangle, \vert 1\rangle$ 是不随时间变化的基矢）：

$$
\text{左边} = i\hbar\bigl(\dot{c}_0\vert 0\rangle + \dot{c}_1\vert 1\rangle\bigr)
$$

右边用矩阵乘法展开：

$$
\text{右边} = \frac{\hbar\Omega}{2}\bigl(c_1\vert 0\rangle + c_0\vert 1\rangle\bigr)
$$

> [!info] 为什么 $\hat{\sigma}_x$ 交换了 $c_0$ 和 $c_1$？
> 因为 $\hat{\sigma}_x\vert 0\rangle = \vert 1\rangle$，$\hat{\sigma}_x\vert 1\rangle = \vert 0\rangle$。所以 $\hat{\sigma}_x(c_0\vert 0\rangle + c_1\vert 1\rangle) = c_0\vert 1\rangle + c_1\vert 0\rangle$。

比较两边 $\vert 0\rangle$ 和 $\vert 1\rangle$ 的系数（两个基矢线性独立，系数必须分别相等），得到一对**耦合微分方程**：

$$
\boxed{i\hbar\dot{c}_0 = \frac{\hbar\Omega}{2}c_1} \qquad \boxed{i\hbar\dot{c}_1 = \frac{\hbar\Omega}{2}c_0}
$$

消去 $\hbar$，写成更简洁的形式：

$$
i\dot{c}_0 = \frac{\Omega}{2}c_1 \tag{1}
$$
$$
i\dot{c}_1 = \frac{\Omega}{2}c_0 \tag{2}
$$

这两个方程**互相耦合**：$c_0$ 的变化率取决于 $c_1$，反之亦然。这正是"振荡"的数学根源——两个振幅不断互相"喂养"对方。

#### Step 4：消元——化为二阶微分方程

我们用**消元法**把耦合方程组化为单个二阶方程。

对方程 (1) 两边对 $t$ 求导：

$$
i\ddot{c}_0 = \frac{\Omega}{2}\dot{c}_1 \tag{3}
$$

从方程 (2) 解出 $\dot{c}_1 = -\frac{i\Omega}{2}c_0$，代入方程 (3)：

$$
i\ddot{c}_0 = \frac{\Omega}{2}\left(-\frac{i\Omega}{2}c_0\right) = -\frac{i\Omega^2}{4}c_0
$$

两边除以 $i$：

$$
\ddot{c}_0 = -\frac{\Omega^2}{4}c_0 \tag{4}
$$

> [!tip] 物理直觉
> 方程 (4) 就是**简谐振子方程**！形式为 $\ddot{x} = -\omega^2 x$，其解是正弦/余弦振荡。这里"振子"的角频率是 $\Omega/2$。这就解释了为什么布居数会周期性振荡。

#### Step 5：求解方程

方程 (4) 的通解为：

$$
c_0(t) = A\cos\left(\frac{\Omega t}{2}\right) + B\sin\left(\frac{\Omega t}{2}\right)
$$

用初始条件 $c_0(0) = 1$ 确定 $A = 1$。

再对 $c_0(t)$ 求导，利用方程 (1) $i\dot{c}_0 = \frac{\Omega}{2}c_1$ 来确定 $c_1$：

$$
\dot{c}_0 = -\frac{\Omega}{2}\sin\left(\frac{\Omega t}{2}\right) + \frac{B\Omega}{2}\cos\left(\frac{\Omega t}{2}\right)
$$

由方程 (1)：$c_1 = \frac{2i}{\Omega}\dot{c}_0$，代入初始条件 $c_1(0) = 0$：

$$
c_1(0) = \frac{2i}{\Omega}\cdot\frac{B\Omega}{2} = iB = 0 \implies B = 0
$$

于是两个振幅的解为：

$$
c_0(t) = \cos\left(\frac{\Omega t}{2}\right)
$$

$$
c_1(t) = \frac{2i}{\Omega}\dot{c}_0 = \frac{2i}{\Omega}\left(-\frac{\Omega}{2}\right)\sin\left(\frac{\Omega t}{2}\right) = -i\sin\left(\frac{\Omega t}{2}\right)
$$

> [!warning] 注意 $c_1$ 前面的 $-i$ 因子
> 这个 $-i$ 不是随意出现的——它来自薛定谔方程中 $i\hbar\frac{d}{dt}$ 的 $i$。正是这个虚数因子让 $c_1$ 与 $c_0$ 之间产生了 $\pi/2$ 的相位差。在 Bloch 球上，这意味着演化轨迹沿着大圆走，而不是原地不动。

#### Step 6：写出最终态矢和跃迁概率

把振幅代回态矢表达式：

$$
\boxed{\vert\psi(t)\rangle = \cos\left(\frac{\Omega t}{2}\right)\vert 0\rangle - i\sin\left(\frac{\Omega t}{2}\right)\vert 1\rangle}
$$

测量发现原子处于 $\vert 1\rangle$ 的概率为振幅模的平方：

$$
\boxed{P_{\vert 1\rangle}(t) = \vert c_1(t)\vert^2 = \sin^2\left(\frac{\Omega t}{2}\right)}
$$

同理，留在 $\vert 0\rangle$ 的概率：

$$
P_{\vert 0\rangle}(t) = \vert c_0(t)\vert^2 = \cos^2\left(\frac{\Omega t}{2}\right)
$$

验证概率守恒：$P_{\vert 0\rangle} + P_{\vert 1\rangle} = \cos^2(\Omega t/2) + \sin^2(\Omega t/2) = 1$ ✓

^260605 具体推导没认真看

#### Step 7：物理图像总结

共振拉比振荡的关键特征：

| 时刻 $t$ | $\vert\psi(t)\rangle$ | $P_{\vert 1\rangle}$ | 物理含义 |
|-----------|----------------------|----------------------|---------|
| $0$ | $\vert 0\rangle$ | $0$ | 完全在基态 |
| $\pi/\Omega$ | $-i\vert 1\rangle$ | $1$ | 完全翻转到激发态（π 脉冲） |
| $2\pi/\Omega$ | $\vert 0\rangle$ | $0$ | 回到基态，完成一个完整周期 |
| $\pi/(2\Omega)$ | $\frac{1}{\sqrt{2}}(\vert 0\rangle - i\vert 1\rangle)$ | $1/2$ | 等权叠加态（π/2 脉冲） |

振荡周期 $T = 2\pi/\Omega$，即**拉比频率 $\Omega$ 越大，振荡越快**——激光越强，原子翻转越迅速。

> [!tip] 实验意义
> 在实验中，只要精确控制激光的**照射时间** $t$，就能把原子制备到任意目标态。例如照射 $t = \pi/\Omega$ 就得到 π 脉冲（完全翻转），照射 $t = \pi/(2\Omega)$ 就得到 π/2 脉冲（最大[[Qubit-State-and-Superposition|叠加态]]）。这就是[[Single-Qubit-Gates|量子门操控]]的核心原理。

### 非共振情形（$\Delta \neq 0$）

广义拉比频率（有效振荡频率）：

$$
\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}
$$

跃迁概率：

$$
P_{\vert 1\rangle}(t) = \frac{\Omega^2}{\tilde{\Omega}^2}\sin^2\left(\frac{\tilde{\Omega} t}{2}\right)
$$

失谐越大，振荡越快但振幅越小（永远达不到 $P = 1$）。

#### Python 图示：共振 vs 失谐驱动

下面这段代码把共振与不同失谐量放在同一张图里比较。上图显示：$\Delta=0$ 时，$\pi$ 脉冲可以把布居完全转移到 $\vert e\rangle$；一旦 $\Delta \neq 0$，振荡频率变成 $\tilde{\Omega}$，峰值却被因子 $\Omega^2/\tilde{\Omega}^2$ 压低。下图把这个趋势单独抽出来：失谐越大，最大可转移布居越低，但广义拉比频率越高。

```python
import numpy as np
import matplotlib.pyplot as plt

Omega = 1.0
detunings = [0.0, 0.5, 1.0, 2.0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Dimensionless time: x = Omega * t / pi
x = np.linspace(0, 6, 900)
t = np.pi * x / Omega

fig, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=False)

for Delta, color in zip(detunings, colors):
    Omega_tilde = np.sqrt(Omega**2 + Delta**2)
    transfer_amplitude = Omega**2 / Omega_tilde**2
    P_excited = transfer_amplitude * np.sin(Omega_tilde * t / 2)**2
    label = rf'$\Delta/\Omega = {Delta:.1f}$'
    axes[0].plot(x, P_excited, lw=2.4, color=color, label=label)

axes[0].axvline(1, color='0.25', lw=1.2, ls='--')
axes[0].annotate(r'Resonant $\pi$ pulse', xy=(1, 1), xytext=(1.18, 0.83),
                 arrowprops=dict(arrowstyle='->', color='0.25', lw=1.2),
                 fontsize=11, color='0.20')
axes[0].set_xlabel(r'Normalized time $\Omega t / \pi$')
axes[0].set_ylabel(r'Excited-state probability $P_e(t)$')
axes[0].set_title('Rabi Flopping: Resonance vs Detuning')
axes[0].set_ylim(-0.03, 1.06)
axes[0].grid(alpha=0.3, ls=':')
axes[0].legend(frameon=False, ncol=2)

Delta_over_Omega = np.linspace(0, 4, 500)
max_transfer = 1 / (1 + Delta_over_Omega**2)
Omega_tilde_over_Omega = np.sqrt(1 + Delta_over_Omega**2)

axes[1].plot(Delta_over_Omega, max_transfer, lw=2.8, color='#1f77b4',
             label=r'Max transfer $\Omega^2/(\Omega^2+\Delta^2)$')
axes[1].plot(Delta_over_Omega, Omega_tilde_over_Omega / Omega_tilde_over_Omega.max(),
             lw=2.2, color='#ff7f0e', ls='--',
             label=r'Normalized generalized frequency $\tilde{\Omega}$')
axes[1].fill_between(Delta_over_Omega, 0, max_transfer, color='#1f77b4', alpha=0.12)
axes[1].set_xlabel(r'Detuning ratio $\Delta/\Omega$')
axes[1].set_ylabel('Normalized value')
axes[1].set_title('Detuning Suppresses Population Transfer but Increases Oscillation Frequency')
axes[1].set_ylim(0, 1.08)
axes[1].grid(alpha=0.3, ls=':')
axes[1].legend(frameon=False)

plt.tight_layout()
plt.show()
```

> [!tip] 读图要点
> 共振曲线的核心是“能完全翻转”；失谐曲线的核心是“转得更快但翻不满”。这就是为什么做 $\pi$ 脉冲时必须校准激光频率，而做 [[AC-Stark-Effect|AC Stark]] 相位门时反而故意使用大失谐。

![[rabi_oscillation_detuned]]

**完整态演化公式**：初始处于 $\vert g\rangle$ 的系统，在失谐 $\Delta$ 和拉比频率 $\Omega$ 驱动下，$t$ 时刻的态为：

$$
\vert \psi(t)\rangle = \left[\cos\left(\frac{\tilde{\Omega}t}{2}\right) + i\frac{\Delta}{\tilde{\Omega}}\sin\left(\frac{\tilde{\Omega}t}{2}\right)\right]\vert g\rangle - i\frac{\Omega}{\tilde{\Omega}}\sin\left(\frac{\tilde{\Omega}t}{2}\right)\vert e\rangle
$$

其中 $\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$。注意 $\vert g\rangle$ 的系数不仅有振荡项 $\cos(\tilde{\Omega}t/2)$，还叠加了一个虚部修正 $i(\Delta/\tilde{\Omega})\sin(\tilde{\Omega}t/2)$；而 $\vert e\rangle$ 的振幅被因子 $\Omega/\tilde{\Omega}$ 压制。

> [!tip] AC Stark 效应的起源
> 当 $\Delta \gg \Omega$ 时，$\vert g\rangle$ 的系数 $\approx 1$（几乎没有布居转移），但积累了相对相位——这就是 [[AC-Stark-Effect]] 的起源。失谐激光虽然不能真正激发原子，却通过虚过程给能级附加了一个相移，等效于对能级施加了一个"光位移"（light shift）。

## 3. π 脉冲与 π/2 脉冲

| 脉冲类型 | 脉冲面积 | 效果 |
|---|---|---|
| **π 脉冲** | $\Omega t = \pi$ | $\vert 0\rangle \to \vert 1\rangle$（完全反转，等效 NOT 门） |
| **π/2 脉冲** | $\Omega t = \pi/2$ | $\vert 0\rangle \to \frac{1}{\sqrt{2}}(\vert 0\rangle - i\vert 1\rangle)$（创造叠加态，类似 Hadamard） |

π 脉冲和 π/2 脉冲是量子门操控的基本构件。

## 4. 布洛赫球几何图像

在布洛赫球上，拉比振荡对应**绕赤道轴的旋转**：
- 共振 ($\Delta = 0$) 驱动 → 绕 $x$ 轴（或 $y$ 轴，取决于激光相位）旋转
- 失谐驱动 → 绕倾斜轴旋转，轨迹为锥面上的圆

> [!tip] 交互式可视化
> 交互式布洛赫球可视化（支持施加 X、Z、H、Rx、Ry、Rz 门并实时观察态矢演化）见 [[tools/bloch_sphere.html]]。

## 5. 与 Rydberg/中性原子体系的关联

在 [[Optical-Tweezer-Arrays]] 中，每个被捕获的中性原子（如 Rb-87 或 Cs）可以用两个[[Hyperfine-Structure|超精细基态]]作为量子比特 $\vert 0\rangle, \vert 1\rangle$。

拉比振荡在 Rydberg 体系中的核心应用：
1. **单比特门实现**：π 脉冲和 π/2 脉冲通过微波或光场精确控制，实现 X, Y, H 等[[Single-Qubit-Gates|单比特门]]
2. **里德堡激发**：将原子从 $\vert 1\rangle$ 激发到[[Rydberg-Blockade|里德堡态]] $\vert r\rangle$ 的过程本身就是一个拉比 π 脉冲，是 [[CZ-Gate]]（经由 [[Rydberg-Blockade]]）的核心步骤
3. **稳定子测量**：在 [[QEC]] 的 syndrome 提取中，辅助比特经过一系列拉比脉冲与数据比特相互作用后被测量

### 5.2 失谐脉冲与 Rz 门

当激光脉冲的失谐量远大于拉比频率（$\Delta \gg \Omega$）时，原子几乎不发生布居转移（$P_{\vert e\rangle} \approx 0$），但两个能级会各自积累不同的动力学相位。对初始态 $\alpha\vert g\rangle + \beta\vert e\rangle$，经过持续时间为 $t$ 的失谐脉冲后，$\vert e\rangle$ 相对 $\vert g\rangle$ 累积相位 $\varphi = \Delta t$，等效于施加了 $R_z(\varphi)$ 旋转门：

$$
\alpha\vert g\rangle + \beta\vert e\rangle \;\;\xrightarrow{\;\Delta \gg \Omega,\; t\;}\;\; \alpha\vert g\rangle + \beta\,e^{-i\varphi/2}\vert e\rangle
$$

这就是**纯相位门**的物理实现：不需要真正驱动跃迁，只利用失谐激光的 AC Stark 效应即可完成 $R_z$ 操作。详细物理机制见 [[AC-Stark-Effect#3. Rz 门的物理实现|Rz 门实现]]，其在中性原子单比特门集中的角色见 [[Single-Qubit-Gates#6. 在中性原子中的物理实现|§6]]。

> [!warning] 易混淆：$\Omega$ vs $\tilde{\Omega}$
> 共振时（$\Delta=0$）跃迁概率是 $\sin^2(\Omega t/2)$，但失谐时必须用广义拉比频率 $\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$。很多初学者忘记失谐修正，导致门保真度计算出错。

> [!info] 为什么 π 脉冲这么重要？
> π 脉冲（$t = \pi/\Omega$）恰好把原子从 $\vert g\rangle$ 完全翻转到 $\vert e\rangle$——这是实现 X 门（量子 NOT 门）的物理基础。π/2 脉冲则产生等权叠加态 $\vert +\rangle$，是量子并行性的起点。

---

## 📐 核心公式摘要

- **$\Omega$**：拉比频率 — $\Omega = d \cdot E_0 / \hbar$
- **$\Delta$**：失谐量 — $\Delta = \omega_L - \omega_0$
- **$\tilde{\Omega}$**：广义拉比频率 — $\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$
- **$P_{\vert 1\rangle}(t)$**：跃迁概率（共振） — $\sin^2(\Omega t/2)$
- **$P_{\vert 1\rangle}(t)$**：跃迁概率（失谐） — $(\Omega/\tilde{\Omega})^2 \sin^2(\tilde{\Omega}t/2)$


---

## 🔗 相关笔记

- [[Single-Qubit-Gates]] — 拉比振荡在门操作语言中的对应：$R_x(\theta)$ 旋转门
- [[Rydberg-Blockade]] — 拉比振荡驱动的里德堡跃迁产生阻塞效应
- [[CZ-Gate]] — 利用 π 脉冲和阻塞实现两比特门
- [[Transversal-Gate]] — 并行施加 CZ 门
- [[Optical-Tweezer-Arrays]] — 原子囚禁平台

## 📝 更新记录

- 2026-06-06: [doc-audit] 新增共振与失谐拉比振荡的 Python 可执行图示，解释最大布居转移与广义拉比频率随失谐量的变化。
- 2026-06-06: 优化文档——添加 3 张 Python 图表（共振振荡、失谐对比、Ω vs 光强），补充 RWA callout，增加 ~6 处内联 wiki-link（Pauli-Matrices、Qubit-State-and-Superposition、Single-Qubit-Gates、Rydberg-Blockade 等）
- 2026-06-06: 补充 [[Fine-Structure]] 和 [[Hyperfine-Structure]] 全文内联链接（标题、正文、callout 共 ~10 处），以及里德堡态 → [[Rydberg-Blockade]] 内联链接
- 2026-06-06: 添加"$\Omega$ 与光强/频率的关系"和"各物理量详解"小节，详细解释 $\omega_0$ 的层级结构（玻尔能级→精细结构→超精细结构→外场修正）及各量的控制权
- 2026-06-06: 共振情形（Δ=0）添加完整逐步推导（7 步），从 TDSE 出发经消元法求解耦合微分方程
- 2026-06-03: 修复 ket 记号在 Markdown 表格/摘要中的渲染问题，将易误解析的 `|...\rangle` 与 `\|...\rangle` 改为 `\vert ...\rangle`。
- 2026-03-29: 初始创建
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
