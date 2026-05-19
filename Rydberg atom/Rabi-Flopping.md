---
aliases: [Rabi Flopping, Rabi Oscillation, 拉比振荡, 拉比频率, Ω]
tags: [Physics, Quantum, NeutralAtom, RydbergAtom, Dynamics]
date: 2026-03-29
status: In-Progress
source: "[[generall quantum 2026]]"
---

# 拉比振荡（Rabi Flopping / Rabi Oscillation）

> 📄 来源文献：[[generall quantum 2026]] · 原始批注见 [p.40](zotero://select/library/items/SL8QGCV5)

> 来源批注：*"Rabi oscillation"* — Bluvstein et al., 2026, p.40

## 1. 物理直觉：什么是拉比振荡？

想象一个二能级原子，在共振激光的驱动下，原子会在基态 $|g\rangle$ 和激发态 $|e\rangle$ 之间**周期性地来回振荡**，就像一个钟摆在两个态之间摆动。这种现象就是**拉比振荡**（Rabi Flopping）。

这是量子光学中最基础的相干驱动现象，也是所有量子比特操控的物理基础。

## 2. 哈密顿量与方程推导

考虑一个二能级系统（$|0\rangle, |1\rangle$）受到频率为 $\omega_L$ 的驱动场，系统哈密顿量为（旋转波近似, RWA）：

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

初始处于 $|0\rangle$ 的系统在时间 $t$ 后的态为：

$$
|\psi(t)\rangle = \cos\left(\frac{\Omega t}{2}\right)|0\rangle - i\sin\left(\frac{\Omega t}{2}\right)|1\rangle
$$

处于 $|1\rangle$ 的概率（跃迁概率）随时间振荡：

$$
P_{|1\rangle}(t) = \sin^2\left(\frac{\Omega t}{2}\right)
$$

### 非共振情形（$\Delta \neq 0$）

广义拉比频率（有效振荡频率）：

$$
\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}
$$

跃迁概率：

$$
P_{|1\rangle}(t) = \frac{\Omega^2}{\tilde{\Omega}^2}\sin^2\left(\frac{\tilde{\Omega} t}{2}\right)
$$

失谐越大，振荡越快但振幅越小（永远达不到 $P = 1$）。

## 3. π 脉冲与 π/2 脉冲

| 脉冲类型 | 脉冲面积 | 效果 |
|---|---|---|
| **π 脉冲** | $\Omega t = \pi$ | $|0\rangle \to |1\rangle$（完全反转，等效 NOT 门） |
| **π/2 脉冲** | $\Omega t = \pi/2$ | $|0\rangle \to \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$（创造叠加态，类似 Hadamard） |

π 脉冲和 π/2 脉冲是量子门操控的基本构件。

## 4. 布洛赫球几何图像

在布洛赫球上，拉比振荡对应**绕赤道轴的旋转**：
- 共振 ($\Delta = 0$) 驱动 → 绕 $x$ 轴（或 $y$ 轴，取决于激光相位）旋转
- 失谐驱动 → 绕倾斜轴旋转，轨迹为锥面上的圆

## 5. 与 Rydberg/中性原子体系的关联

在 [[光镊阵列 (Optical Tweezer Arrays)]] 中，每个被捕获的中性原子（如 Rb-87 或 Cs）可以用两个超精细基态作为量子比特 $|0\rangle, |1\rangle$。

拉比振荡在 Rydberg 体系中的核心应用：
1. **单比特门实现**：π 脉冲和 π/2 脉冲通过微波或光场精确控制，实现 X, Y, H 等单比特门
2. **里德堡激发**：将原子从 $|1\rangle$ 激发到里德堡态 $|r\rangle$ 的过程本身就是一个拉比 π 脉冲，是 [[CZ门 (CZ Gate)]]（经由 [[里德堡阻塞 (Rydberg Blockade)]]）的核心步骤
3. **稳定子测量**：在 [[量子纠错 (QEC)]] 的 syndrome 提取中，辅助比特经过一系列拉比脉冲与数据比特相互作用后被测量

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $\Omega$ | 拉比频率 | $\Omega = d \cdot E_0 / \hbar$ |
| $\Delta$ | 失谐量 | $\Delta = \omega_L - \omega_0$ |
| $\tilde{\Omega}$ | 广义拉比频率 | $\tilde{\Omega} = \sqrt{\Omega^2 + \Delta^2}$ |
| $P_{|1\rangle}(t)$ | 跃迁概率（共振） | $\sin^2(\Omega t/2)$ |
| $P_{|1\rangle}(t)$ | 跃迁概率（失谐） | $(\Omega/\tilde{\Omega})^2 \sin^2(\tilde{\Omega}t/2)$ |
