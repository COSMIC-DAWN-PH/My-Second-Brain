---
aliases: [Optical Tweezer Arrays, 光镊阵列, 光学偶极阱, Optical Dipole Trap, 光镊, Tweezer]
tags: [Physics, Quantum, NeutralAtom, ExperimentalPlatform, RydbergAtom]
date: 2026-03-29
status: In-Progress
source: "[[generall quantum 2026]]"
---

# 光镊阵列（Optical Tweezer Arrays）

> 📄 来源文献：[[generall quantum 2026]] · 原始批注见 [p.40](zotero://select/library/items/SL8QGCV5)

> 来源批注：*"optical tweezers"* — Bluvstein et al., 2026, p.40

## 1. 物理直觉：用光抓住原子

**光镊（Optical Tweezer）**是利用强聚焦激光束产生的**光学梯度力**来俘获微小粒子（包括单个中性原子）的技术。

其物理原理：高斯光束的光强在焦点处最强。一个可极化的粒子（原子）在远离谐振的激光场中会感受到一个**偶极力**，被吸引到光强最大的焦点处：

$$
\mathbf{F}_{\text{dipole}} = -\nabla U_{\text{dipole}}, \quad U_{\text{dipole}} = -\frac{1}{2}\alpha(\omega) |\mathbf{E}(\mathbf{r})|^2
$$

其中 $\alpha(\omega)$ 是原子的动态极化率，$|\mathbf{E}|^2 \propto I(\mathbf{r})$ 为光强。

> 当激光频率**低于**原子共振频率（红失谐，red-detuned）时，$\alpha > 0$，原子被吸引到光强最大处（焦点），形成稳定俘获。

## 2. 从单个光镊到阵列

单个聚焦光束可以俘获**单个原子**（平均填充率约 50%，需要后选择）。

**光镊阵列**通过以下技术将数百至数千个光镊排列成任意二维图案：
- **空间光调制器（SLM, Spatial Light Modulator）**：利用全息图案将单束激光分裂为任意排列的多个焦点
- **声光偏转器（AOD, Acousto-Optic Deflector）**：高速扫描激光，动态创建光镊阵列
- **原子重排（Atom Rearrangement）**：先随机加载原子，再用移动光镊将原子搬运到目标位置，消除空位

## 3. 可重构性（Reconfigurability）——核心优势

光镊阵列最关键的特性是**可重构性**：原子可以在量子计算过程中被**物理移动**，而不破坏其量子态（只要操作足够绝热或足够快）。

这在 [[深度电路执行 (Deep-Circuit Execution)]] 中至关重要：
- 将两个逻辑码块的对应原子**并排放置**，实现 [[横向纠缠门 (Transversal Gate)]]
- 计算后将含错误的原子移走，换入新初始化的低熵原子

## 4. 与量子计算相关的参数

| 参数 | 典型值 | 意义 |
|---|---|---|
| 俘获阱深 | $U_0 / k_B \sim 0.1$–$1$ mK | 决定原子损失率 |
| 振动频率 | $\omega_{\text{trap}} / 2\pi \sim 10$–$100$ kHz | 决定运动态加热速率 |
| 相干时间 | $T_2 \sim 1$–$10$ s | 量子计算时间窗口 |
| 阵列规模 | $\sim 10^2$–$10^3$ 原子 | 当前实验能力 |

## 5. Rydberg 激发与门操作

被光镊俘获的原子可以被激发到**里德堡态（Rydberg State）**——主量子数 $n \gg 1$ 的高激发态。里德堡原子具有：
- 极大的偶极矩（$\sim n^2 a_0$）
- 极强的范德华相互作用（$V \propto C_6 / r^6$）

两个相邻被俘获原子之间的里德堡相互作用产生 **[[里德堡阻塞 (Rydberg Blockade)]]** 效应，是实现 [[CZ门 (CZ Gate)]] 等两比特门的核心机制。

## 6. 在容错量子计算中的角色

在 Bluvstein et al. 2026 的论文框架中，光镊阵列平台支持：
- **[[表面码 (Surface Code)]]**：二维阵列天然匹配表面码的拓扑结构
- **[[量子纠错 (QEC)]]**：通过 [[拉比振荡 (Rabi Flopping)]] 和 CZ 门实现 syndrome 测量
- **[[深度电路执行 (Deep-Circuit Execution)]]**：利用可重构性实现逻辑横向隐形传态

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|---|---|---|
| $U_{\text{dipole}}$ | 偶极势阱深度 | $U = -\frac{1}{2}\alpha(\omega)|\mathbf{E}|^2$ |
| $\mathbf{F}_{\text{dipole}}$ | 光学梯度力 | $\mathbf{F} = -\nabla U_{\text{dipole}}$ |
| $V_{ij}$ | 里德堡相互作用 | $V_{ij} = C_6 / r_{ij}^6$ |
