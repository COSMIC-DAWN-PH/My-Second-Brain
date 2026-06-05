# 从移动原子到通用容错量子计算：四篇中性原子论文路线图讲义

> **讲义目标**：帮助你快速建立对四篇 Nature 系列论文的整体图像：它们分别解决中性原子量子计算扩展路线中的哪一个瓶颈，以及这些瓶颈如何连成一条从物理 qubit 到逻辑 qubit、再到容错通用计算的路线。默认你已经接触过 [[Rydberg-Blockade]]、[[Optical-Tweezer-Arrays]]、[[CZ-Gate]]、[[QEC]] 和 [[Surface-Code]] 的基本概念。

---

## 目录

1. [[#1. 四篇文章在同一条路线上的位置]]
2. [[#2. 2022：用相干搬运打破固定几何连接限制]]
3. [[#3. 2023：把物理原子组织成逻辑量子处理器]]
4. [[#4. 2025：连续运行 3000 原子系统，解决补给问题]]
5. [[#5. 2025：通用容错架构，把纠错、逻辑门和熵移除接起来]]
6. [[#6. 四篇文章的共同物理主线]]
7. [[#7. 读论文时最该抓住的公式和概念]]
8. [[#8. 一张 Python 图：从 transport 到 FTQC]]
9. [[#9. 总结：这四篇到底告诉我们什么]]
10. [[#10. 延伸阅读]]
11. [[#新知识点补全提醒]]

---

## 1. 四篇文章在同一条路线上的位置

这四篇文章可以看成一个连续升级故事：

| 年份 | 论文 | 核心问题 | 一句话贡献 |
|---|---|---|---|
| 2022 | *A quantum processor based on coherent transport of entangled atom arrays* | 固定原子阵列只能近邻连接，复杂图态很难做 | 证明纠缠原子可以被光镊相干搬运，从而实现动态、非局域连接 |
| 2023 | *Logical quantum processor based on reconfigurable atom arrays* | 物理 qubit 错误率太高，必须进入逻辑编码 | 用最多 280 个物理原子实现可编程逻辑处理器，并展示逻辑级算法 |
| 2025 | *Continuous operation of a coherent 3,000-qubit system* | 原子会丢失，系统不能只靠一次性装载 | 用光晶格传送带持续补充原子，维持 3000 多原子阵列超过 2 小时 |
| 2025 | *A fault-tolerant neutral-atom architecture for universal quantum computation* | 纠错、通用逻辑门、深电路和熵移除必须同时工作 | 用最多 448 个原子演示通用容错架构的关键部件 |

> [!tip] 核心物理图像
> 中性原子平台的路线不是简单地“多放一些原子”。真正的升级顺序是：先让原子能移动来产生任意连接，再把许多原子编成一个逻辑 qubit，然后让系统能持续补充损失的原子，最后把纠错、逻辑门、测量、重置和补给组合成长期运行的容错机器。

这条路线和你在 [[Deep-Circuit-Execution]] 里看到的深电路需求直接相关：深电路不是只要门保真度高就够，还要求错误能被持续排出系统。物理上，这就是“保持相干演化”和“不断移除熵”之间的平衡。

---

## 2. 2022：用相干搬运打破固定几何连接限制

### 2.1 这篇文章要解决什么

在普通二维光镊阵列中，原子的位置像棋盘上的棋子。[[Rydberg-Blockade]] 很适合做近邻 [[CZ-Gate]]，但如果两个 qubit 相隔很远，就不能直接强相互作用。传统办法是用很多 swap gate 把信息慢慢搬过去，但每一步都会累积错误。

2022 这篇文章的关键想法是：**不要只在量子态空间里 swap 信息，而是直接把带着纠缠的原子搬过去。**

这里的“相干搬运”（coherent transport）不是普通机械搬运。它要求移动过程中不能破坏 qubit 的超精细态相干性，也不能显著降低已经制备好的 Bell 态保真度。文章用两个光镊系统实现：

- 静态光镊阵列：由 SLM（spatial light modulator，空间光调制器）生成，适合存放大规模原子。
- 移动光镊阵列：由 AOD（acousto-optic deflector，声光偏转器）生成，适合快速移动和重排原子。
- 纠缠机制：通过 Rydberg 态实现全局并行的 CZ 门。
- 存储机制：用 $^{87}\mathrm{Rb}$ 的超精细钟态作为 qubit，抗磁场噪声更好。

### 2.2 最重要的实验结果

文章先制备 Bell 态，然后把纠缠原子对分开约 $110\,\mu\mathrm{m}$，移动时间约 $300\,\mu\mathrm{s}$。测量发现，只要移动速度不过快，Bell 态保真度基本不受搬运影响；主要损失来自原子丢失而不是相位彻底乱掉。

这个结果的物理意义很大：

> [!info] 为什么“搬运纠缠”重要
> 如果纠缠在搬运过程中会马上坏掉，那么中性原子平台只能做“固定几何”的量子电路。现在实验说明，纠缠可以随着原子一起移动，量子处理器就从固定线路板变成了可重构的量子积木。

随后文章展示了几个逐步复杂的任务：

| 任务 | 物理含义 | 为什么重要 |
|---|---|---|
| 12-qubit 一维 cluster state | 用移动重排实现多层 CZ 图态 | 连接到 measurement-based quantum computation |
| 7-qubit Steane code state | 制备小型纠错码图态 | 连接到 [[QEC]] 和 [[Surface-Code]] |
| 13 data + 6 ancilla 的 surface code state | 用移动 ancilla 介导稳定子结构 | 证明动态连接适合拓扑码 |
| 16 data + 8 ancilla 的 toric code state | 实现周期边界的拓扑图态 | 展示非平凡拓扑结构 |
| Rydberg many-body entropy measurement | 混合模拟-数字线路测量 Renyi entropy | 把可重构阵列用于量子模拟 |

### 2.3 这篇文章的真正贡献

这篇文章不是说“我们又多做了几个 qubit”，而是证明了一个架构原则：

$$
\text{fixed geometry} + \text{atom transport}
\longrightarrow
\text{programmable non-local connectivity}.
$$

这里的非局域连接不是通过长距离相互作用直接实现，而是通过“先移动、再局域相互作用”实现。由于 Rydberg blockade 本身仍然是短程强相互作用，这个方案保留了中性原子的高并行性，同时绕开了固定几何限制。

> [!warning] 易错点
> 这里的“非局域连接”不是说两个很远的 Rydberg 原子直接强相互作用，而是说架构允许把需要交互的 qubit 搬到同一个 entangling zone，再用局域强相互作用完成门。

---

## 3. 2023：把物理原子组织成逻辑量子处理器

### 3.1 从物理 qubit 到逻辑 qubit

2022 年的文章解决了连接性问题，但还没有真正解决容错计算的核心问题：物理 qubit 和物理 gate 都会出错。[[QEC]] 的基本思想是把一个逻辑 qubit（logical qubit）编码到许多物理 qubit 中，让错误只改变 syndrome，而不直接破坏逻辑信息。

2023 这篇文章实现了一个“逻辑量子处理器”（logical quantum processor），最多使用 280 个物理原子。它的结构分成三个 zone：

| 区域 | 功能 | 直觉 |
|---|---|---|
| storage zone | 存放逻辑 qubit，避免不必要的门误差 | 图书馆书架 |
| entangling zone | 执行逻辑单比特门、双比特门和 syndrome extraction | 手术台 |
| readout zone | mid-circuit readout 和 feedforward | 检测与决策区 |

这个分区非常重要，因为逻辑 qubit 不是单个点，而是一整块物理原子。中性原子的优势在于：整块逻辑 qubit 可以被一起移动、交错排列、读出或重新组合。

### 3.2 transversal gate：为什么它适合逻辑 qubit

横向门（transversal gate）是指对两个编码块中的对应物理 qubit 成对作用。例如两个 surface code block 做逻辑 CNOT，可以把它们交错排布，然后对每一对物理 qubit 做同样的 Rydberg gate。

它的核心好处是错误不会在同一个 code block 内扩散成灾难：

$$
U_L \approx \bigotimes_i U_i.
$$

这表示逻辑操作 $U_L$ 可以拆成许多并行物理操作 $U_i$。如果某个 $U_i$ 出错，它通常只影响一个局部物理位置，仍然可能被 code distance 保护。

这篇文章展示了：

- surface-code distance 从 $d=3$ 扩到 $d=7$ 时，逻辑 Bell pair error 得到改善。
- 用 colour code 制备达到 break-even fidelity 的逻辑 qubit。
- fault-tolerant 方式制备逻辑 GHZ 态。
- 做 feedforward entanglement teleportation。
- 同时操作 40 个 colour-code logical qubits。
- 用 3D $[[8,3,2]]$ code blocks 实现最多 48 个逻辑 qubit 的复杂采样电路，包括 228 个逻辑双比特门和 48 个逻辑 CCZ 门。

### 3.3 这篇文章的真正贡献

2023 文章的关键词是“逻辑级可编程”。它不只是演示某个单独纠错码，而是在同一个硬件平台上展示多种编码和逻辑操作。

> [!tip] 读这篇时抓住一句话
> 2023 文章证明：中性原子阵列不仅可以做很多物理 gate，还可以把“逻辑 qubit block”当作基本操作对象来移动、门控、测量和 feedforward。

这也是从“量子模拟器/物理处理器”走向“逻辑处理器”的关键一步。

---

## 4. 2025：连续运行 3000 原子系统，解决补给问题

### 4.1 为什么需要连续运行

量子纠错并不会让物理系统不出错。相反，它要求你不断测量 syndrome、不断重置 ancilla、不断替换丢失的原子。中性原子平台的一个根本问题是：原子会因为读出、门操作、有限 trap lifetime 和背景气体碰撞而丢失。

如果每次丢原子都要从头加载整个阵列，那么系统就是脉冲式运行，而不是连续运行。对于大规模 [[Surface-Code]] 或深电路，这会成为瓶颈。

2025 的 *Continuous operation of a coherent 3,000-qubit system* 解决的就是这个“补给线”问题。

### 4.2 光晶格传送带 + preparation zone + storage zone

文章的架构可以想成一个工厂：

- MOT 区域：生产冷原子。
- 两级光晶格 conveyor belt：把原子云运到 science region。
- reservoir：作为可持续取用的原子库。
- preparation zone：把原子装入光镊、冷却、成像、重排并初始化 qubit。
- storage zone：存放已经在工作的 qubit，并用 dynamical decoupling 保护相干性。

最关键的是：preparation zone 的加载、冷却、成像和重排不能破坏 storage zone 里正在保存的 qubit。文章通过几何隔离、光谱 shielding 和 dynamical decoupling 来做到这一点。

主要数字包括：

| 指标 | 结果 |
|---|---|
| tweezer reloading rate | 约 $300{,}000$ atoms/s |
| initialized qubit flux | 超过 $30{,}000$ qubits/s |
| storage array scale | 超过 $3{,}000$ atoms |
| continuous maintenance time | 超过 2 小时 |
| storage coherence with dynamical decoupling | 约 $T_2 = 1.09(3)\,\mathrm{s}$ 量级 |

### 4.3 这篇文章和容错计算的关系

这篇文章不是主要展示逻辑 gate，而是展示大型中性原子机器必须具备的一种工程能力：**在不打断量子信息存储的情况下持续补原子。**

可以把它理解为容错计算的“代谢系统”。逻辑计算会产生错误和熵，读出和重置会消耗 ancilla，原子损失会制造空洞。连续补给系统让机器有能力把坏掉或丢失的物理资源替换掉。

> [!info] 这和 QEC 的关系
> [[QEC]] 在逻辑层面说“错误可以被检测和纠正”；连续补给架构在硬件层面说“坏掉或丢掉的物理 qubit 可以被持续替换”。没有后者，前者很难长期运行。

---

## 5. 2025：通用容错架构，把纠错、逻辑门和熵移除接起来

### 5.1 这篇文章的目标

*A fault-tolerant neutral-atom architecture for universal quantum computation* 是四篇里最接近“完整容错计算架构”的一篇。它使用最多 448 个中性原子，展示：

- repeated [[QEC]] 能降低逻辑错误。
- atom loss detection 和 machine learning decoding 可以提升解码。
- transversal gates 与 lattice surgery 都能用于逻辑纠缠。
- 通过 transversal teleportation 和 3D $[[15,1,3]]$ code 实现通用逻辑。
- mid-circuit qubit reuse 把实验 cycle rate 提高约两个数量级。
- 用 $[[7,1,3]]$ 和 $[[16,6,4]]$ code 做深逻辑电路，同时维持近似 constant internal entropy。

### 5.2 below-threshold performance：纠错真的开始工作

文章用 distance-5 surface code 做多轮 QEC，比较 $d=3$ 和 $d=5$ 的表现。关键结果是：结合 loss detection 和 machine learning decoding 后，$d=5$ 的每轮错误约比 $d=3$ 低 $2.14(13)\times$。

这就是 below-threshold performance（低于阈值表现）的实验信号：

$$
p_L(d=5) < p_L(d=3).
$$

更一般地，如果物理错误率 $p$ 低于阈值 $p_{\mathrm{th}}$，逻辑错误率应随 code distance 增大而下降：

$$
p_L(d) \sim A \left(\frac{p}{p_{\mathrm{th}}}\right)^{(d+1)/2}.
$$

这里的指数只表示直觉：code distance 越大，需要越多物理错误串联起来才会形成逻辑错误。

### 5.3 transversal gate 与 lattice surgery 的差异

文章比较了两类逻辑纠缠方式：

| 方法 | 怎么做 | 优势 | 风险 |
|---|---|---|---|
| transversal gate | 两个 code block 交错，对应物理 qubit 成对做门 | 快、并行、适合中性原子移动架构 | 需要处理跨 block 的相关错误 |
| lattice surgery | 通过联合稳定子测量合并/分离逻辑边界 | 与 surface code 容错理论联系紧密 | 对测量错误更敏感，通常需要多轮 syndrome |

这篇文章的一个重要观点是：逻辑门不只是“生成纠缠”，还会把熵注入系统；而 syndrome measurement、readout、reset 和 teleportation 则负责把熵带走。

> [!tip] 关键直觉
> 容错量子计算不是一边纯粹做相干门、一边偶尔纠错。更准确的图像是：每一段逻辑演化都在产生错误熵，架构必须同步安排测量、解码、重置和 qubit reuse，把这些熵排出去。

### 5.4 为什么 teleportation 会成为通用计算工具

Eastin-Knill theorem 告诉我们：一个量子纠错码不可能拥有一整套通用的 transversal unitary gates。因此，如果只靠横向幺正门，通常不能实现任意量子计算。

文章用 transversal teleportation 绕开这个限制。直觉上，teleportation 不只是“传送量子态”，而是把逻辑信息从一个物理载体转移到另一个已经准备好的低熵编码块中，同时旧物理块可以被测量、重置和复用。

这件事同时完成三件功能：

1. 传播逻辑信息。
2. 引入非 Clifford 资源，从而实现 universality。
3. 把旧物理 qubit 的错误和熵留在被测量的一侧。

这和 [[Transversal-Teleportation]]、[[Transversal-Gate]] 的主题直接相连。

---

## 6. 四篇文章的共同物理主线

### 6.1 从连接性到容错性的递进

四篇文章之间不是平行关系，而是层层加功能：

| 架构能力 | 2022 transport | 2023 logical processor | 2025 continuous operation | 2025 universal FTQC |
|---|---|---|---|---|
| 动态连接 | 强 | 强 | 辅助 | 强 |
| 逻辑编码 | 初步图态 | 核心 | 支撑未来 | 核心 |
| 连续补给 | 无 | 有限 | 核心 | qubit reuse 核心 |
| 多轮 QEC | 无 | 部分 | 硬件支撑 | 核心 |
| 通用容错逻辑 | 无 | 早期逻辑算法 | 无 | 核心 |

### 6.2 中性原子的三件“架构武器”

第一，**可移动性**。原子不是固定在芯片布线上的硬件节点，而是可以通过 AOD 光镊移动。这让逻辑 qubit block 可以像积木一样排列、交错、存储和读出。

第二，**Rydberg blockade 强相互作用**。当两个原子被带到合适距离时，[[Rydberg-Blockade]] 提供强而快速的纠缠机制。这是 [[CZ-Gate]] 和多体门的物理基础。

第三，**测量与重置的空间分区**。readout zone 和 storage zone 分开，使得某些 qubit 可以被测量和重置，而其他 qubit 仍保持相干。这是 mid-circuit readout、feedforward、qubit reuse 和 continuous operation 的共同基础。

---

## 7. 读论文时最该抓住的公式和概念

### 7.1 Graph state stabilizer

2022 年文章大量使用 graph state。若图上每个顶点是一个 qubit，边代表 CZ gate，则 graph state 的稳定子可写成：

$$
S_i = X_i \prod_{j \in N(i)} Z_j.
$$

这里 $N(i)$ 是与顶点 $i$ 相连的邻居。物理含义是：如果图态制备正确，测量这些稳定子应得到接近 $+1$ 的期望值。

### 7.2 Surface code distance

对于 [[Surface-Code]]，code distance $d$ 决定能承受多少物理错误：

$$
t = \left\lfloor \frac{d-1}{2} \right\rfloor.
$$

$d=5$ 时可以纠正最多 2 个任意位置错误；$d=7$ 时可以纠正最多 3 个。2023 和 2025 的逻辑改进都围绕“增大 $d$ 后逻辑错误是否下降”展开。

### 7.3 Renyi entropy

2022 年的量子模拟部分测量二阶 Renyi entropy：

$$
S_2(A) = -\log_2 \mathrm{Tr}(\rho_A^2).
$$

这里 $\rho_A$ 是子系统 $A$ 的约化密度矩阵。$S_2$ 越大，表示子系统与外界纠缠越强。文章通过两份相同系统的 Bell measurement circuit 测量 SWAP 期望值，从而得到 Renyi entropy。

### 7.4 Constant entropy operation

2025 FTQC 文章反复强调 constant entropy。可以把它写成一个架构目标：

$$
\Delta S_{\mathrm{logic}} \approx 0
\quad \text{while} \quad
\Delta S_{\mathrm{physical}} \text{ is removed by measurement/reset/reload}.
$$

意思不是物理系统完全不产生熵，而是逻辑信息所在的有效自由度不让熵无限积累。测量、重置、冷却和补给负责把熵倒出去。

---

## 8. 一张 Python 图：从 transport 到 FTQC

下面这段代码可以在 Obsidian Execute Code 中运行。图中把四篇文章按“代表性原子规模”和“架构成熟度”放在一起。注意图内文字全部使用英文，避免 CJK glyph warning。

```python
import matplotlib.pyplot as plt

papers = ['2022\nTransport', '2023\nLogical', '2025\nContinuous', '2025\nFTQC']
physical_qubits = [24, 280, 3000, 448]
architecture_level = [1, 2, 3, 4]
labels = ['Dynamic connectivity', 'Logical blocks', 'Continuous reload', 'Universal FTQC']

fig, ax1 = plt.subplots(figsize=(8.0, 4.2))
ax1.plot(papers, physical_qubits, marker='o', lw=2.2, color='#1f77b4', label='Representative atom scale')
ax1.set_ylabel('Representative Physical Qubits / Atoms')
ax1.set_yscale('log')
ax1.grid(alpha=0.3, ls=':')

ax2 = ax1.twinx()
ax2.plot(papers, architecture_level, marker='s', lw=2.0, color='#d62728', label='Architecture maturity')
ax2.set_ylabel('Architecture Maturity Level')
ax2.set_ylim(0.5, 4.5)
ax2.set_yticks([1, 2, 3, 4])

for i, text in enumerate(labels):
    ax1.annotate(text, (i, physical_qubits[i]), textcoords='offset points', xytext=(0, 8), ha='center', fontsize=9)

lines = ax1.get_lines() + ax2.get_lines()
ax1.legend(lines, [line.get_label() for line in lines], frameon=False, loc='upper left')
plt.title('Neutral-Atom Processor Roadmap from Transport to FTQC')
plt.tight_layout()
plt.show()
```

> [!warning] 图的读法
> 3000 原子论文的物理规模最大，但它不是逻辑计算演示；448 原子 FTQC 论文的原子数较少，却在架构层面更接近通用容错计算。规模和架构成熟度不是同一个指标。

---

## 9. 总结：这四篇到底告诉我们什么

第一，2022 年文章告诉我们：中性原子平台的连接性瓶颈可以通过相干搬运解决。原子移动不是附属功能，而是架构核心。

第二，2023 年文章告诉我们：中性原子可以把整块逻辑 qubit 当作操作对象，实现逻辑级门、测量、feedforward 和复杂逻辑电路。

第三，2025 年 3000 原子文章告诉我们：大规模系统必须连续运行。补给、冷却、初始化和相干保护是未来容错计算的硬件生命线。

第四，2025 年 FTQC 文章告诉我们：通用容错计算需要把 repeated QEC、transversal gate、lattice surgery、teleportation、mid-circuit reuse 和 entropy removal 合成一个闭环。

> [!tip] 最简路线图
> **移动原子**解决连接性，**逻辑编码**解决物理错误，**连续补给**解决原子损失，**teleportation + reuse**解决通用深电路中的熵积累。

如果你现在只是想“大致了解这些文章”，记住这句话就够了：**这四篇论文共同展示了中性原子量子计算从可重构物理阵列走向可持续、可纠错、可通用的逻辑处理器。**

---

## 10. 延伸阅读

- [[Rydberg-Blockade]]：理解 Rydberg 相互作用为什么能做强纠缠门。
- [[CZ-Gate]]：理解 controlled-Z gate 如何成为 graph state 和 surface code 电路的基本积木。
- [[Optical-Tweezer-Arrays]]：理解光镊阵列如何捕获、移动和重排原子。
- [[Surface-Code]]：理解 code distance、stabilizer 和 syndrome extraction。
- [[QEC]]：理解为什么逻辑错误率可以随编码规模下降。
- [[Transversal-Gate]]：理解 transversal operation 为什么天然适合容错。
- [[Transversal-Teleportation]]：理解 2025 FTQC 文章中 teleportation 为什么能同时支持通用性和熵移除。
- [[Deep-Circuit-Execution]]：理解为什么大规模算法不是单次高保真门，而是长期稳定的逻辑演化。

---

## 新知识点补全提醒

以下概念在本讲义中出现，但目前可能还没有独立、成熟的知识笔记。建议后续按优先级补全。

### 1. Atom Transport and Reconfigurable Connectivity

> **简要介绍**：相干原子搬运（coherent atom transport）是中性原子平台区别于固定芯片架构的关键能力。它允许把需要相互作用的 qubit 搬到 entangling zone，再执行 Rydberg gate。核心问题是移动过程中如何避免 heating、loss 和 phase decoherence。

> **建议位置**：`Rydberg atom/Atom-Transport-and-Reconfigurable-Connectivity.md`
> **建议链接**：[[Optical-Tweezer-Arrays]]、[[Rydberg-Blockade]]、[[CZ-Gate]]

### 2. Mid-Circuit Readout and Feedforward

> **简要介绍**：mid-circuit readout 指在量子电路尚未结束时测量一部分 qubit，并根据结果实时决定后续操作。它是 syndrome extraction、logical teleportation 和 qubit reuse 的必要条件。没有它，纠错只能停留在“事后诊断”，无法形成闭环控制。

> **建议位置**：`Rydberg atom/Mid-Circuit-Readout-and-Feedforward.md`
> **建议链接**：[[QEC]]、[[Surface-Code]]、[[Transversal-Teleportation]]

### 3. Lattice Surgery

> **简要介绍**：lattice surgery 是 surface code 中通过测量联合稳定子来合并或分离逻辑边界的方法。它不一定需要直接做 transversal gate，而是通过测量过程生成逻辑纠缠。优点是理论框架成熟，缺点是对测量错误和多轮 syndrome 更敏感。

> **建议位置**：`Rydberg atom/Lattice-Surgery.md`
> **建议链接**：[[Surface-Code]]、[[QEC]]、[[Transversal-Gate]]

### 4. Constant Entropy Operation

> **简要介绍**：constant entropy operation 是容错深电路的核心架构目标。逻辑计算过程中物理错误不断产生，系统必须通过测量、重置、冷却、补给和 teleportation 把这些错误熵移出逻辑自由度。它把量子计算从“做一串门”提升为“维持一个长期低熵逻辑过程”。

> **建议位置**：`Rydberg atom/Constant-Entropy-Operation.md`
> **建议链接**：[[Deep-Circuit-Execution]]、[[QEC]]、[[Transversal-Teleportation]]

### 5. Quantum Reed-Muller Codes

> **简要介绍**：Reed-Muller code 是一类在容错通用计算中常用于 transversal non-Clifford gates 的编码。2025 FTQC 文章中的 $[[15,1,3]]$、$[[7,1,3]]$ 和 $[[16,6,4]]$ 都与这一类结构相关。它们的作用是让某些逻辑 gate 可以横向实现，配合 teleportation 生成通用门集。

> **建议位置**：`Rydberg atom/Quantum-Reed-Muller-Codes.md`
> **建议链接**：[[Transversal-Gate]]、[[Transversal-Teleportation]]、[[QEC]]

---

## 更新记录

- 2026-06-05: 初始创建，综合 2022 coherent transport、2023 logical quantum processor、2025 continuous 3000-qubit system 与 2025 universal FTQC 四篇论文。
