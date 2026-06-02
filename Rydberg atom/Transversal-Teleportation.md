---
aliases:
  - Transversal Teleportation
  - 横向隐形传态
  - 逻辑隐形传态
  - Logical Teleportation
tags:
  - Physics
  - Quantum
  - FaultTolerant
  - Teleportation
  - DeepCircuit
date: 2026-06-01
status: In-Progress
source: "[[generall quantum 2026]]"
comprehension: "don't understand"
---

# 横向隐形传态（Transversal Teleportation）

> 来源批注：*"transversal teleportation"* — Bluvstein et al., 2026, pp.39-41
> 本笔记从"为什么需要它"出发，系统介绍横向隐形传态的动机、协议、数学证明及其在容错量子计算中的核心角色。

---

## 1. 两个必须解决的问题

横向隐形传态不是凭空发明的——它是为了解决容错量子计算中两个**根本性困难**而设计的。理解了这两个困难，就会觉得横向隐形传态是"唯一的出路"。

### 1.1 困难一：电路深度有天花板

量子算法往往需要执行很多层逻辑门。假设每层操作有物理错误率 $p$，那么 $D$ 层之后累积的错误率为：

$$
p_{\text{累积}} \approx 1 - (1 - p)^D \approx pD \quad (p \ll 1)
$$

当 $D \gtrsim 1/p$ 时，错误累积到计算结果完全不可信。

> [!tip] 物理直觉：传话游戏
> 想象一个传话游戏：每传一次有 5% 的概率出错。传 10 次也许还行，但传 100 次就完全走样了。深度电路执行就面临这个困境——我们需要在"传话"过程中不断**刷新信息**来阻止错误累积。

**出路**：我们需要一种方法，在不破坏逻辑信息的前提下，不断"清理"物理错误。这就是横向隐形传态的核心使命。

### 1.2 困难二：Eastin-Knill 定理

回忆 [[Transversal-Gate]] 中的结论：

> **Eastin-Knill 定理**：对任何非平凡的量子纠错码，不存在通用的横向门集合。

也就是说，[[QEC|纠错码]] 能横向实现的门是有限的（如横向 CZ），但像 $T$ 门这样的非 Clifford 门**无法横向实现**。

**出路**：我们需要一种方法，在横向门的基础上额外"追加"非横向的逻辑操作。这就是 **Gate Teleportation**（门隐形传态），它是横向隐形传态的推广。

> [!warning] 常见误解
> 横向隐形传态不是一个"可选的高级技巧"——它是同时解决**深度电路错误累积**和**Eastin-Knill 定理限制**这两个根本困难的**核心协议**。理解它等于理解容错量子计算为什么能工作。

---

## 2. 从标准隐形传态说起

### 2.1 回顾：标准量子隐形传态

横向隐形传态是标准隐形传态的"逻辑版本"。先回顾标准协议：

**目标**：Alice 想把一个量子态 $|\psi\rangle$ 传给 Bob，但只靠量子信道无法直接传送（量子不可克隆定理禁止复制量子态）。

**资源**：Alice 和 Bob 预先共享一对 Bell 态粒子（纠缠对）。

**三步协议**：

$$
|\psi\rangle_{\text{in}} = \alpha|0\rangle + \beta|1\rangle
$$

**Step 1 — Bell 测量**：Alice 对她的粒子（携带 $|\psi\rangle$）和纠缠对中的 A 粒子做 Bell 基测量。测量结果随机为四种 Bell 态之一（用 2 bit 经典信息表示）。

**Step 2 — 经典通信**：Alice 通过经典信道将 2 bit 测量结果告诉 Bob。

**Step 3 — Pauli 修正**：Bob 根据收到的经典信息，对他的粒子施加对应的 Pauli 修正（$I$、$X$、$Z$ 或 $XZ$），恢复出 $|\psi\rangle$。

$$
|\psi\rangle_{\text{in}} \xrightarrow{\text{Bell 测量} + \text{经典通信} + \text{Pauli 修正}} |\psi\rangle_{\text{out}}
$$

> [!tip] 核心特性
> 原始粒子上的态被摧毁了（测量），信息通过纠缠通道 + 经典信道到达 Bob。这符合不可克隆定理——**原始态被破坏，不存在两份拷贝**。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_title('Standard Quantum Teleportation Protocol', fontsize=14, fontweight='bold', pad=15)

# Colors
c_alice = '#1f77b4'
c_bob = '#d62728'
c_bell = '#ff7f0e'
c_classical = '#2ca02c'
c_state = '#9467bd'

# Alice's particle (carrying |psi>)
ax.add_patch(mpatches.FancyBboxPatch((0.5, 5.5), 2, 0.8, boxstyle='round,pad=0.1',
             facecolor=c_state, edgecolor='black', alpha=0.8))
ax.text(1.5, 5.9, r'$|\psi\rangle_{\mathrm{in}}$', ha='center', va='center',
        fontsize=12, color='white', fontweight='bold')

# Bell pair particles
ax.add_patch(mpatches.FancyBboxPatch((0.5, 3.5), 2, 0.8, boxstyle='round,pad=0.1',
             facecolor=c_bell, edgecolor='black', alpha=0.8))
ax.text(1.5, 3.9, r'Alice: Bell particle', ha='center', va='center',
        fontsize=9, color='white', fontweight='bold')

ax.add_patch(mpatches.FancyBboxPatch((7, 3.5), 2, 0.8, boxstyle='round,pad=0.1',
             facecolor=c_bell, edgecolor='black', alpha=0.8))
ax.text(8, 3.9, r'Bob: Bell particle', ha='center', va='center',
        fontsize=9, color='white', fontweight='bold')

# Entanglement line
ax.plot([2.5, 7], [3.9, 3.9], '--', color=c_bell, linewidth=2, alpha=0.7)
ax.text(4.75, 4.15, 'Entangled pair', ha='center', va='center',
        fontsize=9, color=c_bell, style='italic')

# Bell measurement box
ax.add_patch(mpatches.FancyBboxPatch((0.3, 4.3), 2.4, 1.0, boxstyle='round,pad=0.1',
             facecolor=c_alice, edgecolor='black', linewidth=2, alpha=0.3))
ax.text(1.5, 4.8, 'Bell Measurement', ha='center', va='center',
        fontsize=10, fontweight='bold', color=c_alice)
ax.annotate('', xy=(1.5, 4.3), xytext=(1.5, 4.7),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Classical channel
ax.annotate('', xy=(7, 2.5), xytext=(2.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=c_classical, lw=2.5,
                           connectionstyle='arc3,rad=0'))
ax.text(4.75, 2.15, r'Classical bits (2 bit)', ha='center', va='center',
        fontsize=10, color=c_classical, fontweight='bold')

# Pauli correction box
ax.add_patch(mpatches.FancyBboxPatch((6.8, 1.2), 2.4, 1.0, boxstyle='round,pad=0.1',
             facecolor=c_bob, edgecolor='black', linewidth=2, alpha=0.3))
ax.text(8, 1.7, 'Pauli Correction', ha='center', va='center',
        fontsize=10, fontweight='bold', color=c_bob)

# Output state
ax.add_patch(mpatches.FancyBboxPatch((7, 0.0), 2, 0.8, boxstyle='round,pad=0.1',
             facecolor=c_bob, edgecolor='black', alpha=0.8))
ax.text(8, 0.4, r'$|\psi\rangle_{\mathrm{out}}$', ha='center', va='center',
        fontsize=12, color='white', fontweight='bold')

# Arrows
ax.annotate('', xy=(1.5, 4.7), xytext=(1.5, 5.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(8, 2.2), xytext=(8, 3.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(8, 0.8), xytext=(8, 1.2),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Labels
ax.text(0.5, 6.5, 'Alice', fontsize=12, fontweight='bold', color=c_alice)
ax.text(8.5, 6.5, 'Bob', fontsize=12, fontweight='bold', color=c_bob)

plt.tight_layout()
plt.show()
```

### 1.2 从物理到逻辑：关键推广

标准隐形传态传送的是**单个物理 qubit** 的态。但在容错量子计算中，我们操作的不是物理 qubit，而是**逻辑 qubit**——由 $n$ 个物理 qubit 编码的纠错码块。

**核心区别**：

| | 标准隐形传态 | 横向隐形传态 |
|--|------------|------------|
| 传送对象 | 1 个物理 qubit 态 | 整个逻辑 qubit 编码态 |
| 纠缠资源 | 1 个 Bell 对 | $n$ 个并行 Bell 对 |
| 测量 | 1 次 Bell 测量 | $n$ 次并行 Bell 测量 |
| 经典通信 | 2 bit | $2n$ bit |
| **容错性** | 无 | **错误不跨码块传播** |

> [!tip] "横向"的含义
> "横向"（transversal）指的是：所有操作都是**逐物理比特独立**的——对码块 A 的第 $i$ 个物理 qubit 和码块 B 的第 $i$ 个物理 qubit 做操作，不同 $i$ 之间**完全独立**，没有交叉耦合。这正是容错性的来源。

---

## 3. 横向隐形传态的完整协议

### 3.1 系统设置

想象处理器中有两组逻辑 qubit 码块 $A$ 和 $B$，每个码块由 $n$ 个物理 qubit 组成（使用 [[Surface-Code]] 等纠错码编码）。

- **$A$ 码块**：承载着待传送的逻辑态 $|\psi\rangle_L$，以及随电路深度积累的物理错误
- **$B$ 码块**：处于已知的参考态（如逻辑 $|+\rangle_L$ 或纠错码基态），是"干净的"

$$
|\psi\rangle_L = \alpha|0\rangle_L + \beta|1\rangle_L \quad \text{（A 码块中编码的逻辑态）}
$$

**目标**：将 $|\psi\rangle_L$ 从 $A$ 传送到 $B$，同时把 $A$ 上积累的物理错误"隔离"在 $A$ 中，不让它们污染 $B$。

### 3.2 四步协议

**Step 1：横向 CZ 门——建立纠缠**

对 $A$ 和 $B$ 的每一对对应物理 qubit $(a_i, b_i)$ 施加 [[CZ-Gate|CZ 门]]：

$$
\overline{\text{CZ}} = \bigotimes_{i=1}^{n} \text{CZ}^{(a_i, b_i)}
$$

这是一个 [[Transversal-Gate|横向门]]——对 $n$ 对物理 qubit **同时、各自独立**地施加 CZ 门。由于逐比特独立性，$A$ 上的物理错误**不会通过这个操作传播到 $B$**。

**Step 2：横向 Bell 测量——传送逻辑信息**

对 $A$ 码块的所有物理 qubit 执行 Bell 基测量。每个 $a_i$ 与 $b_i$ 之间已经通过 CZ 门建立了纠缠，Bell 测量的效果是：

$$
|\psi\rangle_L^{(A)} \otimes |\text{ref}\rangle_L^{(B)} \xrightarrow{\overline{\text{CZ}} + \text{Bell测量}_A} |\psi\rangle_L^{(B)} + (\text{物理错误留在 } A)
$$

逻辑信息干净地传到 $B$，物理错误留在被测量的 $A$ 中。

> [!tip] 为什么错误不传到 B？
> 这是横向操作的逐比特独立性导致的。考虑 $A$ 上第 $j$ 个物理 qubit 有一个错误 $E_j$：
>
> $$
> (E_j \otimes I_{b_j}) \cdot \text{CZ}^{(a_j, b_j)} = \text{CZ}^{(a_j, b_j)} \cdot (\tilde{E}_j \otimes I_{b_j})
> $$
>
> 错误 $E_j$ 经过 CZ 门后变成了一个新的错误 $\tilde{E}_j$，但它**仍然只作用在 $a_j$ 上**，完全没有影响到 $b_j$。这就是"错误隔离"的数学本质。

**Step 3：经典后处理——Pauli 修正**

根据 $A$ 的测量结果（$2n$ bit 经典信息），在 $B$ 上施加相应的 Pauli 修正。由于 $B$ 受纠错码保护，这些修正可以容错执行。

**Step 4：重置 $A$ 码块——准备下一轮**

$A$ 码块在测量后处于已知态（包含物理错误），可以：
1. 移除旧原子，补充新制备的低熵原子
2. 重新初始化为干净的参考态
3. 准备好在下一轮中充当"接收方"

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- Left panel: Protocol overview ---
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Transversal Teleportation Protocol', fontsize=12, fontweight='bold', pad=10)

c_a = '#1f77b4'
c_b = '#d62728'
c_error = '#ff7f0e'
c_clean = '#2ca02c'
c_arrow = '#333333'

# Top: Before teleportation
ax.add_patch(mpatches.FancyBboxPatch((0.2, 5.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_a, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(2.3, 7.2, 'Block A (dirty)', fontsize=10, fontweight='bold',
        ha='center', va='center', color=c_a)

# Physical qubits in A
for i, (lbl, yp) in enumerate([(r'$a_1$', 6.8), (r'$a_2$', 6.35), (r'$a_3$', 5.9)]):
    col = c_error if i == 1 else c_a
    ax.add_patch(mpatches.Circle((1.2, yp), 0.2, facecolor=col,
                 edgecolor='black', linewidth=1.5, alpha=0.8))
    ax.text(1.2, yp, lbl, ha='center', va='center', fontsize=7, color='white', fontweight='bold')

ax.annotate('Error!', xy=(1.5, 6.35), xytext=(2.3, 6.6),
            fontsize=8, color=c_error, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=c_error, lw=1.2))

ax.text(3.3, 6.35, r'$|\psi\rangle_L$', fontsize=10, ha='center', va='center',
        color=c_a, style='italic')

ax.add_patch(mpatches.FancyBboxPatch((5.5, 5.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_b, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(7.6, 7.2, 'Block B (clean)', fontsize=10, fontweight='bold',
        ha='center', va='center', color=c_b)

for i, (lbl, yp) in enumerate([(r'$b_1$', 6.8), (r'$b_2$', 6.35), (r'$b_3$', 5.9)]):
    ax.add_patch(mpatches.Circle((6.5, yp), 0.2, facecolor=c_clean,
                 edgecolor='black', linewidth=1.5, alpha=0.8))
    ax.text(6.5, yp, lbl, ha='center', va='center', fontsize=7, color='white', fontweight='bold')

ax.text(8.5, 6.35, r'$|\mathrm{ref}\rangle_L$', fontsize=10, ha='center', va='center',
        color=c_clean, style='italic')

# Transversal CZ arrows
for yp in [6.8, 6.35, 5.9]:
    ax.annotate('', xy=(6.3, yp), xytext=(1.4, yp),
                arrowprops=dict(arrowstyle='<->', color=c_arrow, lw=1.2,
                               linestyle='dashed'))

ax.text(3.85, 7.55, r'Transversal $\overline{\mathrm{CZ}}$', fontsize=9,
        ha='center', va='center', color=c_arrow, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor=c_arrow, alpha=0.8))

# Arrow down
ax.annotate('', xy=(5, 4.2), xytext=(5, 5.3),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax.text(5.3, 4.75, '+ Bell measure A', fontsize=9, ha='left', va='center', color='gray')

# Bottom: After teleportation
ax.add_patch(mpatches.FancyBboxPatch((0.2, 1.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_a, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(2.3, 3.2, 'Block A (measured)', fontsize=10, fontweight='bold',
        ha='center', va='center', color=c_a)
ax.text(2.3, 2.5, 'Errors + syndrome', fontsize=9, ha='center', va='center',
        color=c_error, fontweight='bold')
ax.text(2.3, 2.0, r'$\rightarrow$ Reset & reload', fontsize=8, ha='center', va='center',
        color='gray')

ax.add_patch(mpatches.FancyBboxPatch((5.5, 1.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_b, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(7.6, 3.2, 'Block B (receives)', fontsize=10, fontweight='bold',
        ha='center', va='center', color=c_b)
ax.text(7.6, 2.5, r'$|\psi\rangle_L$ (clean!)', fontsize=10, ha='center', va='center',
        color=c_clean, fontweight='bold')
ax.text(7.6, 2.0, r'$\rightarrow$ Continue computation', fontsize=8, ha='center', va='center',
        color='gray')

# --- Right panel: Step-by-step breakdown ---
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 8)
ax2.axis('off')
ax2.set_title('Four Steps at a Glance', fontsize=12, fontweight='bold', pad=10)

steps = [
    (7.0, 'Step 1', 'Transversal CZ', r'$\overline{\mathrm{CZ}} = \bigotimes_i \mathrm{CZ}^{(a_i,b_i)}$', c_arrow),
    (5.5, 'Step 2', 'Bell measure A', r'Measure all $a_i$ in Bell basis', c_a),
    (4.0, 'Step 3', 'Classical correction', r'$2n$-bit Pauli correction on B', c_b),
    (2.5, 'Step 4', 'Reset A', r'Remove old atoms, load fresh ones', c_clean),
]

for y, num, title, desc, col in steps:
    ax2.add_patch(mpatches.FancyBboxPatch((0.5, y - 0.5), 9, 1.0, boxstyle='round,pad=0.1',
                 facecolor=col, edgecolor='black', linewidth=1.5, alpha=0.1))
    ax2.text(1.5, y + 0.15, num, fontsize=11, fontweight='bold', ha='center', va='center', color=col)
    ax2.text(3.5, y + 0.15, title, fontsize=11, fontweight='bold', ha='center', va='center')
    ax2.text(7.0, y + 0.15, desc, fontsize=9, ha='center', va='center', color='gray', style='italic')

# Connecting arrows
for i in range(len(steps) - 1):
    ax2.annotate('', xy=(5, steps[i+1][0] + 0.5), xytext=(5, steps[i][0] - 0.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

plt.tight_layout()
plt.show()
```

---

## 4. 错误隔离：为什么横向操作是安全的？

这是理解横向隐形传态**为什么能容错**的关键。

### 4.1 物理直觉

> **错误隔离（Error Isolation）**：物理错误始终局限在它产生的码块内，永远不会通过横向操作传播到另一个码块。

这源于横向 CZ 门的**逐比特独立性**：每个物理 qubit 对 $(a_i, b_i)$ 的 CZ 操作是完全独立的，不存在跨 qubit 的耦合。

> [!tip] 类比：并行传话
> 想象 Alice 和 Bob 之间有 $n$ 条**独立的电话线**，每条线传一个 bit。如果第 $j$ 条线有噪声（错误），它**只影响第 $j$ 条线上的信息**，不会"串"到其他线。横向操作就像 $n$ 条独立的电话线——每对物理 qubit 的操作互不干扰。

### 4.2 对比：横向 vs 非横向

| | 横向操作（安全） | 非横向操作（危险） |
|--|---------------|----------------|
| 操作方式 | 每对物理 qubit 独立操作 | 跨 qubit 的纠缠操作 |
| 错误传播 | 错误**不跨码块** | 错误可能**扩散到整个码块** |
| 类比 | $n$ 条独立电话线 | 一张电话网络（串线风险） |

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Left panel: Non-transversal ---
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_title('Non-Transversal (Error Spreads)', fontsize=11, fontweight='bold', color='#d62728')

# Block A
ax.add_patch(mpatches.FancyBboxPatch((0.5, 3.5), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#1f77b4', edgecolor='black', linewidth=2, alpha=0.15))
ax.text(2.5, 6.2, 'Block A', fontsize=10, fontweight='bold', ha='center', color='#1f77b4')

# Block B
ax.add_patch(mpatches.FancyBboxPatch((5.5, 3.5), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#d62728', edgecolor='black', linewidth=2, alpha=0.15))
ax.text(7.5, 6.2, 'Block B', fontsize=10, fontweight='bold', ha='center', color='#d62728')

# Cross-coupling arrows
cross_pairs = [((1.5, 5.0), (6.5, 4.5)), ((1.5, 4.5), (6.5, 5.0)),
               ((3.5, 5.0), (8.5, 4.5)), ((3.5, 4.5), (8.5, 5.0))]
for (x1, y1), (x2, y2) in cross_pairs:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.2, alpha=0.6))

ax.text(5, 3.0, 'Cross-coupling!', fontsize=10, ha='center', color='#d62728',
        fontweight='bold', style='italic')

ax.add_patch(mpatches.FancyBboxPatch((5.5, 0.8), 4, 1.5, boxstyle='round,pad=0.2',
             facecolor='#ff7f0e', edgecolor='black', linewidth=2, alpha=0.3))
ax.text(7.5, 1.55, 'Error spreads\nto Block B!', fontsize=10, ha='center',
        color='#ff7f0e', fontweight='bold')

ax.annotate('', xy=(7.5, 2.3), xytext=(7.5, 3.5),
            arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=2))

# --- Right panel: Transversal ---
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 7)
ax2.axis('off')
ax2.set_title('Transversal (Error Isolated)', fontsize=11, fontweight='bold', color='#2ca02c')

# Block A
ax2.add_patch(mpatches.FancyBboxPatch((0.5, 3.5), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#1f77b4', edgecolor='black', linewidth=2, alpha=0.15))
ax2.text(2.5, 6.2, 'Block A', fontsize=10, fontweight='bold', ha='center', color='#1f77b4')

# Block B
ax2.add_patch(mpatches.FancyBboxPatch((5.5, 3.5), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#d62728', edgecolor='black', linewidth=2, alpha=0.15))
ax2.text(7.5, 6.2, 'Block B', fontsize=10, fontweight='bold', ha='center', color='#d62728')

# Parallel arrows (safe)
parallel_pairs = [((1.5, 5.5), (6.5, 5.5)), ((2.5, 5.0), (7.5, 5.0)),
                  ((3.5, 4.5), (8.5, 4.5))]
for (x1, y1), (x2, y2) in parallel_pairs:
    ax2.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='<->', color='#2ca02c', lw=1.5))

ax2.text(5, 3.0, 'No cross-coupling!', fontsize=10, ha='center', color='#2ca02c',
        fontweight='bold', style='italic')

ax2.add_patch(mpatches.FancyBboxPatch((0.5, 0.8), 4, 1.5, boxstyle='round,pad=0.2',
             facecolor='#ff7f0e', edgecolor='black', linewidth=2, alpha=0.3))
ax2.text(2.5, 1.55, 'Error stays\nin Block A', fontsize=10, ha='center',
        color='#ff7f0e', fontweight='bold')

ax2.add_patch(mpatches.FancyBboxPatch((5.5, 0.8), 4, 1.5, boxstyle='round,pad=0.2',
             facecolor='#2ca02c', edgecolor='black', linewidth=2, alpha=0.3))
ax2.text(7.5, 1.55, 'Block B\nremains clean', fontsize=10, ha='center',
        color='#2ca02c', fontweight='bold')

plt.tight_layout()
plt.show()
```

### 4.3 数学证明

考虑 $A$ 码块上存在物理错误 $E_A$（作用在第 $j$ 个物理 qubit 上）：

$$
(E_A \otimes I_B) \cdot \overline{\text{CZ}} \left( |\psi\rangle_L^{(A)} \otimes |\phi\rangle_L^{(B)} \right)
$$

由于 $\overline{\text{CZ}}$ 的逐比特分解：

$$
= \left(\text{CZ}^{(1)} \otimes \cdots \otimes (E_A \cdot \text{CZ}^{(j)}) \otimes \cdots \otimes \text{CZ}^{(n)}\right) \left( |\psi\rangle_L^{(A)} \otimes |\phi\rangle_L^{(B)} \right)
$$

错误 $E_A$ 只作用在 $A$ 的第 $j$ 个物理 qubit 上，**不会传播到 $B$ 的任何物理 qubit**。

对 $A$ 做 Bell 测量后：
- $A$ 的测量结果包含了关于 $E_A$ 的信息（错误综合征）
- $B$ 的逻辑态**完全不受 $E_A$ 影响**

$$
\boxed{\text{错误隔离}：E_A \text{ 只作用于 } A，\text{不传播到 } B}
$$

> [!warning] 常见错误
> 注意：横向门不是"对整个码块施加一个大操作"，而是对每对物理 qubit **独立**施加小操作。正是这种"独立性"保证了错误不会扩散。如果操作跨 qubit 耦合（非横向），错误就会像传染病一样扩散到整个码块。

---

## 5. 乒乓循环：恒定熵的实现

### 5.1 核心思想

横向隐形传态最强大的应用是形成**乒乓循环**（ping-pong cycle）：$A$、$B$ 两组码块交替充当"发送方"和"接收方"，不断将逻辑态在两者之间传送。

```
轮次 1:  A(脏) ──[CZ + 测量 A]──→ B(干净)     A 被重置
轮次 2:  B(脏) ──[CZ + 测量 B]──→ A(干净)     B 被重置
轮次 3:  A(脏) ──[CZ + 测量 A]──→ B(干净)     A 被重置
  ⋮
```

每一轮，物理错误不断产生，但通过隐形传态被"清除"到重置的码块中。

### 5.2 为什么熵保持恒定？

| 步骤 | 熵的变化 | 发生了什么 |
|------|---------|-----------|
| 横向 CZ + Bell 测量 | 逻辑态无损传送 | 物理错误留在被测量的码块 |
| 重置被测量的码块 | 熵降为零 | 旧原子被移除，新原子补充 |
| 下一步计算 | 熵缓慢上升 | 新的物理错误开始积累 |
| 再次隐形传态 | 熵再次被清除 | 重复上述过程 |

> [!tip] 浴缸类比
> 想象一个浴缸：水龙头一直在注水（物理错误不断产生），但排水口一直在排水（隐形传态不断清除错误）。只要注水速度 = 排水速度，浴缸里的水位就保持恒定——这就是**恒定熵运行**。

$$
S_{\text{逻辑}}(t) = \text{const} \quad \forall t \in [0, T_{\text{circuit}}]
$$

> [!warning] 常见误解
> 恒定熵不是说"没有错误产生"——错误仍然在每一步产生。关键在于**产生的速率等于清除的速率**，逻辑信息的质量始终维持在一个稳定水平。

```python
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

c_error = '#ff7f0e'
c_clean = '#2ca02c'
c_a = '#1f77b4'
c_b = '#d62728'

# --- Left panel: Entropy over rounds ---
rounds = np.arange(0, 10)

# Without teleportation: entropy accumulates
S_no = 1 - np.exp(-0.2 * rounds)

# With teleportation: entropy stays constant
S_tp = np.full_like(rounds, 0.2, dtype=float)

ax1.plot(rounds, S_no, 'o-', color=c_error, linewidth=2.5, markersize=7,
         label=r'Without teleportation: $S$ grows')
ax1.plot(rounds, S_tp, 's-', color=c_clean, linewidth=2.5, markersize=7,
         label=r'With teleportation: $S = \mathrm{const}$')

ax1.set_xlabel('Circuit depth (rounds)', fontsize=11)
ax1.set_ylabel(r'Logical entropy $S_{\mathrm{logical}}$', fontsize=11)
ax1.set_title('Entropy Evolution', fontsize=12, fontweight='bold')
ax1.legend(frameon=False, fontsize=9, loc='center right')
ax1.grid(alpha=0.3, ls=':')
ax1.set_ylim(-0.05, 1.1)
ax1.set_xlim(-0.3, 9.3)

# --- Right panel: Ping-pong schematic ---
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 7)
ax2.axis('off')
ax2.set_title('Ping-Pong Cycle', fontsize=12, fontweight='bold')

rounds_data = [
    (0.5, 'A (dirty)', 'B (clean)', c_a, c_b),
    (3.5, 'B (dirty)', 'A (clean)', c_b, c_a),
    (6.5, 'A (dirty)', 'B (clean)', c_a, c_b),
]

for x_off, lbl_a, lbl_b, col_a, col_b in rounds_data:
    ax2.add_patch(mpatches.FancyBboxPatch((x_off, 3.5), 2.5, 1.5, boxstyle='round,pad=0.1',
                 facecolor=col_a, edgecolor='black', linewidth=1.5, alpha=0.7))
    ax2.text(x_off + 1.25, 4.25, lbl_a, ha='center', va='center',
            fontsize=8, color='white', fontweight='bold')

    ax2.add_patch(mpatches.FancyBboxPatch((x_off, 1.0), 2.5, 1.5, boxstyle='round,pad=0.1',
                 facecolor=col_b, edgecolor='black', linewidth=1.5, alpha=0.7))
    ax2.text(x_off + 1.25, 1.75, lbl_b, ha='center', va='center',
            fontsize=8, color='white', fontweight='bold')

    ax2.text(x_off + 1.25, 5.5, r'$\overline{\mathrm{CZ}}$ + Bell', fontsize=7,
            ha='center', color='gray', style='italic')
    ax2.annotate('', xy=(x_off + 1.25, 3.5), xytext=(x_off + 1.25, 5.2),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

# Round labels
for i, x in enumerate([1.75, 4.75, 7.75]):
    ax2.text(x, 0.4, f'Round {i+1}', fontsize=9, ha='center', fontweight='bold', color='gray')

# Arrows between rounds
for x in [3.0, 6.0]:
    ax2.annotate('', xy=(x + 0.5, 4.25), xytext=(x, 4.25),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

plt.tight_layout()
plt.show()
```

---

## 6. 与标准隐形传态的完整对比

| 特性 | 标准量子隐形传态 | 横向逻辑隐形传态 |
|------|----------------|----------------|
| 传送对象 | 单个物理 qubit 态 | 整个逻辑 qubit 编码态 |
| 纠缠资源 | 单个 Bell 对 | $n$ 个并行 Bell 对（横向 CZ） |
| 测量方式 | 单粒子 Bell 测量 | $n$ 个并行 Bell 测量 |
| 容错性 | 无（物理层面） | 天然容错（错误不跨码块传播） |
| 经典通信 | 2 bit | $2n$ bit |
| 核心优势 | 量子态传输 | **错误隔离** + **恒定熵运行** |
| 应用场景 | 量子通信 | 容错量子计算（深度电路） |

---

## 7. Gate Teleportation：传送逻辑门

横向隐形传态不仅可以传送逻辑态，还可以用来**传送逻辑门操作**——这是绕过 [[Transversal-Gate|Eastin-Knill 定理]] 的关键。

### 7.1 基本思想

> 如果 $B$ 码块初始不是处于普通参考态，而是处于一个**预编译了逻辑门的辅助态**（称为 **magic state**），那么通过横向隐形传态，传送逻辑态的同时就**附带执行了一个逻辑门**。

具体来说：

1. $B$ 码块初始处于 $U_L |\phi\rangle_L$（对参考态施加了逻辑门 $U$）
2. 执行横向隐形传态：将 $|\psi\rangle_L$ 从 $A$ 传送到 $B$
3. 结果：$B$ 中的逻辑态变成了 $U_L |\psi\rangle_L$

$$
\boxed{|\psi\rangle_L \xrightarrow{\text{Gate Teleportation}} U_L|\psi\rangle_L}
$$

> [!tip] 物理直觉
> 标准隐形传态相当于"复制"逻辑态到新码块；Gate Teleportation 相当于"复制并加工"——在传送的过程中自动执行了一个逻辑门。这就像传送带上装了一台打印机，产品经过传送带时自动被"印刷"了。

### 7.2 为什么这很重要？

回忆 [[Transversal-Gate|Eastin-Knill 定理]]：

> 不存在通用的横向门集合。某些逻辑门（如 $T$ 门）无法横向实现。

Gate Teleportation 绕过了这个限制：
1. 横向门（如 CZ）→ 直接横向实现
2. 非横向门（如 $T$ 门）→ 通过 Gate Teleportation + magic state 实现
3. 两者结合 → **通用容错量子计算**

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_title('Gate Teleportation: Implementing Non-Transversal Gates', fontsize=13, fontweight='bold', pad=10)

c_magic = '#9467bd'
c_input = '#1f77b4'
c_output = '#2ca02c'

# Magic state preparation
ax.add_patch(mpatches.FancyBboxPatch((0.3, 3), 2.5, 1.2, boxstyle='round,pad=0.15',
             facecolor=c_magic, edgecolor='black', linewidth=2, alpha=0.7))
ax.text(1.55, 3.6, 'Magic State\n' + r'$U_L|\phi\rangle_L$', ha='center', va='center',
        fontsize=10, color='white', fontweight='bold')

# Input state
ax.add_patch(mpatches.FancyBboxPatch((0.3, 0.8), 2.5, 1.2, boxstyle='round,pad=0.15',
             facecolor=c_input, edgecolor='black', linewidth=2, alpha=0.7))
ax.text(1.55, 1.4, 'Input State\n' + r'$|\psi\rangle_L$', ha='center', va='center',
        fontsize=10, color='white', fontweight='bold')

# Teleportation box
ax.add_patch(mpatches.FancyBboxPatch((3.5, 1.5), 3, 2.5, boxstyle='round,pad=0.2',
             facecolor='lightyellow', edgecolor='black', linewidth=2))
ax.text(5, 3.5, 'Transversal', fontsize=10, ha='center', fontweight='bold')
ax.text(5, 3.0, 'Teleportation', fontsize=10, ha='center', fontweight='bold')
ax.text(5, 2.3, r'$\overline{\mathrm{CZ}}$ + Bell', fontsize=10, ha='center', color='gray')
ax.text(5, 1.8, r'measure + reset', fontsize=10, ha='center', color='gray')

# Output state
ax.add_patch(mpatches.FancyBboxPatch((7.2, 1.5), 2.5, 1.2, boxstyle='round,pad=0.15',
             facecolor=c_output, edgecolor='black', linewidth=2, alpha=0.7))
ax.text(8.45, 2.1, 'Output\n' + r'$U_L|\psi\rangle_L$', ha='center', va='center',
        fontsize=10, color='white', fontweight='bold')

# Arrows
ax.annotate('', xy=(3.5, 3.6), xytext=(2.8, 3.6),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(3.5, 1.4), xytext=(2.8, 1.4),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(7.2, 2.1), xytext=(6.5, 2.75),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

ax.text(5, 0.5, r'Gate $U$ is "teleported" onto $|\psi\rangle_L$', fontsize=11,
        ha='center', va='center', color=c_magic, fontweight='bold', style='italic')

plt.tight_layout()
plt.show()
```

### 7.3 Magic State Distillation

Gate Teleportation 需要高纯度的 magic state，这通过 **magic state distillation**（魔法态蒸馏）实现：

- 从多个低保真度的 magic state 中提取一个高保真度的 magic state
- 这个过程本身可以通过横向操作容错执行
- 是容错量子计算中最耗资源的环节之一

> [!info] 资源开销
> Magic state distillation 是容错量子计算的主要资源瓶颈。蒸馏一个 $T$ 门所需的 magic state 可能需要消耗数十到数百个物理 qubit 和多轮纠错操作。这也是为什么中性原子平台的大规模并行能力（见下文）特别有价值。

---

## 8. 在中性原子体系中的实现

[[Optical-Tweezer-Arrays]] 的**可重构性**（reconfigurable）是实现横向隐形传态的关键优势。

### 8.1 物理实现四步走

**Step 1 — 码块布局**：将 $A$、$B$ 两组逻辑码块的原子**并排放置**在光镊阵列中，使得每对 $(a_i, b_i)$ 物理上相邻。

**Step 2 — 横向 CZ 门**：利用 [[Rydberg-Blockade|Rydberg blockade]] 介导的 CZ 门。**全局激光束**同时对所有对应原子对施加 CZ 操作——这是高度并行的。

**Step 3 — 并行 Bell 测量**：对 $A$ 码块的所有原子同时进行荧光探测（state-dependent fluorescence），一次性获得全部测量结果。

**Step 4 — 原子重置与阵列重组**：
- 将 $A$ 中被测量的原子移除
- 补充新制备的冷原子
- 利用光镊的可重构性，将 $B$ 移到"A 的位置"，新原子移到"B 的位置"
- 准备好下一轮乒乓循环

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(11, 5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_title('Neutral Atom Implementation of Transversal Teleportation', fontsize=13, fontweight='bold', pad=10)

c_atom = '#1f77b4'
c_rydberg = '#ff7f0e'
c_laser = '#d62728'
c_reset = '#2ca02c'

# Step 1: Layout
ax.add_patch(mpatches.FancyBboxPatch((0.2, 2.5), 2.3, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(1.35, 4.2, 'Step 1: Layout', fontsize=8, ha='center', fontweight='bold')

for x in [0.6, 1.0, 1.4, 1.8]:
    ax.add_patch(mpatches.Circle((x, 3.5), 0.12, facecolor=c_atom, edgecolor='black', linewidth=1))
    ax.add_patch(mpatches.Circle((x, 2.9), 0.12, facecolor=c_reset, edgecolor='black', linewidth=1))
ax.text(0.8, 3.2, 'A', fontsize=7, ha='center', color=c_atom, fontweight='bold')
ax.text(0.8, 2.6, 'B', fontsize=7, ha='center', color=c_reset, fontweight='bold')

# Step 2: Transversal CZ
ax.add_patch(mpatches.FancyBboxPatch((2.9, 2.5), 2.3, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(4.05, 4.2, 'Step 2: Transversal CZ', fontsize=8, ha='center', fontweight='bold')

ax.annotate('', xy=(4.05, 3.8), xytext=(4.05, 4.5),
            arrowprops=dict(arrowstyle='->', color=c_laser, lw=2))
ax.text(4.35, 4.35, 'Laser', fontsize=7, ha='left', color=c_laser)

for x in [3.3, 3.7, 4.1, 4.5]:
    ax.add_patch(mpatches.Circle((x, 3.5), 0.12, facecolor=c_rydberg, edgecolor='black', linewidth=1))
    ax.add_patch(mpatches.Circle((x, 2.9), 0.12, facecolor=c_rydberg, edgecolor='black', linewidth=1))
    ax.plot([x, x], [3.38, 3.02], '--', color=c_rydberg, linewidth=0.8, alpha=0.5)

ax.text(3.9, 2.6, 'Rydberg CZ', fontsize=7, ha='center', color=c_rydberg, fontweight='bold')

# Step 3: Measurement
ax.add_patch(mpatches.FancyBboxPatch((5.6, 2.5), 2.3, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(6.75, 4.2, 'Step 3: Measure A', fontsize=8, ha='center', fontweight='bold')

for x in [6.0, 6.4, 6.8, 7.2]:
    ax.add_patch(mpatches.Circle((x, 3.5), 0.12, facecolor='gray', edgecolor='black', linewidth=1, alpha=0.5))
    ax.add_patch(mpatches.Circle((x, 2.9), 0.12, facecolor=c_reset, edgecolor='black', linewidth=1))

ax.text(6.6, 3.2, 'Fluorescence', fontsize=7, ha='center', color='gray')
ax.text(6.6, 2.6, r'$|\psi\rangle_L$ here', fontsize=7, ha='center', color=c_reset, fontweight='bold')

# Step 4: Reset
ax.add_patch(mpatches.FancyBboxPatch((8.4, 2.5), 2.3, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(9.55, 4.2, 'Step 4: Reset', fontsize=8, ha='center', fontweight='bold')

for x in [8.8, 9.2, 9.6]:
    ax.add_patch(mpatches.Circle((x, 3.5), 0.1, facecolor=c_reset, edgecolor='black', linewidth=1))
ax.text(9.2, 3.0, 'Fresh atoms', fontsize=7, ha='center', color=c_reset)

# Connecting arrows
for x_end in [2.9, 5.6, 8.4]:
    ax.annotate('', xy=(x_end, 3.5), xytext=(x_end - 0.4, 3.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

plt.tight_layout()
plt.show()
```

### 8.2 中性原子的独特优势

| 优势 | 含义 | 其他平台对比 |
|------|------|------------|
| **原子可移动** | 计算中可物理移动原子，天然支持码块重排 | 超导 qubit 固定在芯片上 |
| **全局门操作** | 里德堡激发用全局激光同时作用于所有原子 | 超导需逐个微波线路 |
| **原子可补充** | 损失的原子实时用新原子替换 | 超导 qubit 损失不可逆 |

> [!info] 为什么中性原子特别适合横向隐形传态？
> 横向隐形传态需要三个硬件条件：(1) 并行两比特门——由全局里德堡激光实现；(2) 并行测量——由荧光成像实现；(3) 码块重组——由可重构光镊实现。中性原子平台**天然满足全部三个条件**，而超导平台需要复杂的微波线路网络和量子态转移协议才能间接实现。

### 8.3 论文实验验证

Bluvstein et al. (2026) 在 **27 层**深度电路中演示了横向隐形传态：

- 使用 distance-5 [[Surface-Code]] 编码
- 每层包含横向 CZ + 测量 + 重置
- **逻辑关联**在 27 层后仍保持（证明逻辑信息无损传送）
- **物理 stabilizer 错误关联**随距离指数衰减（证明错误被有效清除）

> [!info] 实验里程碑
> 27 层是当前技术的里程碑。虽然实际量子算法可能需要数百到数千层，但 27 层的验证证明了**恒定熵运行在原理上是可行的**——这是通向实用容错量子计算的关键一步。

---

## 📐 核心公式摘要

| 符号 | 含义 | 公式 |
|------|------|------|
| $\overline{\text{CZ}}$ | 横向 CZ 门 | $\bigotimes_{i=1}^{n} \text{CZ}^{(a_i, b_i)}$ |
| 逻辑传送 | 核心效果 | $\|\psi\rangle_L^{(A)} \xrightarrow{\text{CZ+Bell}} \|\psi\rangle_L^{(B)}$ |
| 错误隔离 | 容错性保证 | $E_A$ 只作用于 $A$，不传播到 $B$ |
| 恒定熵 | 运行目标 | $S_{\text{逻辑}}(t) = \text{const}$ |
| Gate Teleportation | 门操作传送 | $B$ 初态 $= U_L\|\phi\rangle_L$ → 传送后 $= U_L\|\psi\rangle_L$ |
| 经典通信量 | 协议开销 | $2n$ bit（$n$ = 物理 qubit 数） |

---

## 🔗 相关笔记

- [[Deep-Circuit-Execution]] — 横向隐形传态的应用场景：恒定熵深度电路
- [[Transversal-Gate]] — 横向隐形传态的核心构件：横向 CZ 门
- [[QEC]] — 纠错码框架：错误检测与纠正
- [[Surface-Code]] — 论文使用的具体纠错码
- [[Optical-Tweezer-Arrays]] — 中性原子平台的硬件基础
- [[Rydberg-Blockade]] — 介导高保真度 CZ 门的物理机制

## 📝 更新记录

- 2026-06-01: 初始创建，包含完整协议、数学推导、Gate Teleportation、中性原子实现、Python 图表 ×5
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
