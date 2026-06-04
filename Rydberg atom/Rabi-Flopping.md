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

$$
\hat{H} = \frac{\hbar}{2}\begin{pmatrix} -\Delta & \Omega \\ \Omega^* & \Delta \end{pmatrix}
$$

其中：
- $\Omega$：**拉比频率**（Rabi frequency），由驱动场强度和原子跃迁偶极矩决定，$\Omega = \frac{d \cdot E_0}{\hbar}$
- $\Delta = \omega_L - \omega_0$：**失谐量**（detuning），激光频率与原子共振频率之差

### 共振情形（$\Delta = 0$）

哈密顿量简化为：

$$
\hat{H}_{\text{res}} = \frac{\hbar\Omega}{2}\hat{\sigma}_x
$$

初始处于 $\vert 0\rangle$ 的系统在时间 $t$ 后的态为：

$$
\vert \psi(t)\rangle = \cos\left(\frac{\Omega t}{2}\right)\vert 0\rangle - i\sin\left(\frac{\Omega t}{2}\right)\vert 1\rangle
$$

处于 $\vert 1\rangle$ 的概率（跃迁概率）随时间振荡：

$$
P_{\vert 1\rangle}(t) = \sin^2\left(\frac{\Omega t}{2}\right)
$$

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

## 5. 与 Rydberg/中性原子体系的关联

在 [[Optical-Tweezer-Arrays]] 中，每个被捕获的中性原子（如 Rb-87 或 Cs）可以用两个超精细基态作为量子比特 $\vert 0\rangle, \vert 1\rangle$。

拉比振荡在 Rydberg 体系中的核心应用：
1. **单比特门实现**：π 脉冲和 π/2 脉冲通过微波或光场精确控制，实现 X, Y, H 等单比特门
2. **里德堡激发**：将原子从 $\vert 1\rangle$ 激发到里德堡态 $\vert r\rangle$ 的过程本身就是一个拉比 π 脉冲，是 [[CZ-Gate]]（经由 [[Rydberg-Blockade]]）的核心步骤
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

- 2026-06-03: 修复 ket 记号在 Markdown 表格/摘要中的渲染问题，将易误解析的 `|...\rangle` 与 `\|...\rangle` 改为 `\vert ...\rangle`。
- 2026-03-29: 初始创建
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
