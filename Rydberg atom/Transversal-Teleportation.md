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
> 本笔记从物理直觉出发，系统介绍横向隐形传态的原理、数学结构、与 Gate Teleportation 的关系，及其在深度电路执行中的核心作用。

---

## 1. 物理直觉：从量子隐形传态说起

### 1.1 经典量子隐形传态回顾

量子隐形传态（Quantum Teleportation）是量子信息中最优美的协议之一。它的核心思想是：

> **借助预共享的纠缠对 + 经典通信，将一个量子态从 A 处"传送"到 B 处，而无需物理传输承载该态的粒子本身。**

标准协议的三个步骤：

1. **制备纠缠对**：Alice 和 Bob 共享一对 Bell 态粒子

$$
|\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$

2. **Bell 测量**：Alice 对她持有的粒子（携带待传送态 $|\psi\rangle$）和纠缠对中的 A 粒子做 Bell 基测量
3. **经典通信 + 修正**：Alice 将 2 bit 测量结果告诉 Bob，Bob 对他的粒子施加相应的 Pauli 修正，恢复出 $|\psi\rangle$

**关键特性**：原始粒子上的态被摧毁（测量），信息通过纠缠通道 + 经典信道到达 B 处。这符合**不可克隆定理**——原始态被破坏，不存在两份拷贝。

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

### 1.2 从物理到逻辑：为什么需要"横向"版本？

在容错量子计算中，我们操作的不是单个物理 qubit，而是**逻辑 qubit**（由 $n$ 个物理 qubit 编码而成的纠错码块）。

问题来了：

- **物理隐形传态**传送的是单个物理 qubit 的态
- **逻辑隐形传态**需要传送的是**整个逻辑 qubit 的编码态**（可能涉及几十到上百个物理 qubit）

> **横向隐形传态** = 将标准隐形传态推广到逻辑层面：对两个逻辑码块执行**逐物理比特对**的 Bell 测量和纠缠操作，将逻辑态从一个码块传送到另一个码块。

"横向"（transversal）的含义是：所有操作都是**逐物理比特独立**的，不同码块的物理比特之间没有交叉耦合——这正是容错性的来源。

> [!tip] 核心洞察
> 横向隐形传态的天才之处在于：它把"传送量子态"和"清除错误"两件事**合二为一**。每次传送逻辑态的同时，物理错误自动留在被测量的码块中——不需要额外的"清理"步骤。

---

## 2. 横向隐形传态的完整协议

### 2.1 系统设置

考虑两组逻辑 qubit 码块 $A$ 和 $B$，每个码块由 $n$ 个物理 qubit 组成，使用某个量子纠错码（如 [[表面码 (Surface Code)]]）编码。

$$
|\psi\rangle_L = \alpha|0\rangle_L + \beta|1\rangle_L
$$

**目标**：将 $A$ 码块中的逻辑态 $|\psi\rangle_L$ 传送到 $B$ 码块，同时将 $A$ 上积累的物理错误"隔离"在 $A$ 中。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Transversal Teleportation: Protocol Overview', fontsize=14, fontweight='bold', pad=15)

# Color palette
c_block_a = '#1f77b4'
c_block_b = '#d62728'
c_error = '#ff7f0e'
c_clean = '#2ca02c'
c_arrow = '#333333'

# --- Block A (dirty) ---
ax.add_patch(mpatches.FancyBboxPatch((0.2, 5.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_block_a, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(2.3, 7.2, 'Block A (source)', fontsize=11, fontweight='bold',
        ha='center', va='center', color=c_block_a)

# Physical qubits in A
for i, (label, y_pos) in enumerate([(r'$a_1$', 6.8), (r'$a_2$', 6.35), (r'$a_3$', 5.9)]):
    color = c_error if i == 1 else c_block_a
    ax.add_patch(mpatches.Circle((1.2, y_pos), 0.2, facecolor=color,
                 edgecolor='black', linewidth=1.5, alpha=0.8))
    ax.text(1.2, y_pos, label, ha='center', va='center', fontsize=8, color='white', fontweight='bold')

# Error indicator on a_2
ax.annotate('Error!', xy=(1.5, 6.35), xytext=(2.2, 6.6),
            fontsize=9, color=c_error, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=c_error, lw=1.5))

# Logical state in A
ax.text(3.2, 6.35, r'$|\psi\rangle_L$ (logical state)', fontsize=10,
        ha='center', va='center', color=c_block_a, style='italic')

# --- Block B (clean) ---
ax.add_patch(mpatches.FancyBboxPatch((5.5, 5.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_block_b, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(7.6, 7.2, 'Block B (target)', fontsize=11, fontweight='bold',
        ha='center', va='center', color=c_block_b)

# Physical qubits in B
for i, (label, y_pos) in enumerate([(r'$b_1$', 6.8), (r'$b_2$', 6.35), (r'$b_3$', 5.9)]):
    ax.add_patch(mpatches.Circle((6.5, y_pos), 0.2, facecolor=c_clean,
                 edgecolor='black', linewidth=1.5, alpha=0.8))
    ax.text(6.5, y_pos, label, ha='center', va='center', fontsize=8, color='white', fontweight='bold')

ax.text(8.5, 6.35, r'$|\mathrm{ref}\rangle_L$', fontsize=10,
        ha='center', va='center', color=c_clean, style='italic')

# Transversal CZ arrows (dashed)
for y_pos in [6.8, 6.35, 5.9]:
    ax.annotate('', xy=(6.3, y_pos), xytext=(1.4, y_pos),
                arrowprops=dict(arrowstyle='<->', color=c_arrow, lw=1.5,
                               linestyle='dashed', connectionstyle='arc3,rad=0'))

ax.text(3.85, 7.55, r'Transversal $\overline{\mathrm{CZ}}$', fontsize=10,
        ha='center', va='center', color=c_arrow, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor=c_arrow, alpha=0.8))

# --- Step labels ---
steps = [
    (2.3, 4.8, r'$\mathbf{Step\ 1}$: $A$ has $|\psi\rangle_L$ + errors', c_block_a),
    (7.6, 4.8, r'$\mathbf{Step\ 2}$: $B$ has clean reference state', c_clean),
]
for x, y, txt, col in steps:
    ax.text(x, y, txt, fontsize=9, ha='center', va='center', color=col)

# --- Arrow down to next stage ---
ax.annotate('', xy=(5, 3.8), xytext=(5, 4.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax.text(5.3, 4.15, 'Apply Transversal CZ', fontsize=9, ha='left', va='center')

# --- After CZ + Bell Measurement ---
ax.add_patch(mpatches.FancyBboxPatch((0.2, 1.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_block_a, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(2.3, 3.2, 'Block A (measured)', fontsize=11, fontweight='bold',
        ha='center', va='center', color=c_block_a)

ax.add_patch(mpatches.FancyBboxPatch((5.5, 1.5), 4.2, 2.0, boxstyle='round,pad=0.15',
             facecolor=c_block_b, edgecolor='black', linewidth=2, alpha=0.15))
ax.text(7.6, 3.2, 'Block B (receives)', fontsize=11, fontweight='bold',
        ha='center', va='center', color=c_block_b)

# Result labels
ax.text(2.3, 2.5, r'Errors + syndrome', fontsize=10, ha='center', va='center',
        color=c_error, fontweight='bold')
ax.text(2.3, 2.0, r'$\rightarrow$ Reset / reload atoms', fontsize=9, ha='center', va='center',
        color='gray')

ax.text(7.6, 2.5, r'$|\psi\rangle_L$ (clean!)', fontsize=11, ha='center', va='center',
        color=c_clean, fontweight='bold')
ax.text(7.6, 2.0, r'$\rightarrow$ Continue computation', fontsize=9, ha='center', va='center',
        color='gray')

# Bell measurement arrow
ax.annotate('', xy=(2.3, 3.5), xytext=(2.3, 4.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.text(0.5, 4.0, 'Bell\nmeasure', fontsize=8, ha='center', va='center', color='gray')

# Entanglement line after CZ
ax.plot([1.4, 6.3], [2.5, 2.5], ':', color=c_arrow, linewidth=1.5, alpha=0.5)

plt.tight_layout()
plt.show()
```

### 2.2 协议步骤详解

**Step 1：制备 $B$ 码块的辅助态**

$B$ 码块初始处于某个已知的参考态（如逻辑 $|+\rangle_L$ 或特定的纠错码基态）。$A$ 码块承载着待传送的逻辑态 $|\psi\rangle_L$，以及随电路深度积累的物理错误。

**Step 2：横向 CZ 门（纠缠建立）**

对 $A$ 和 $B$ 的每一对对应物理 qubit $(a_i, b_i)$ 施加 CZ 门：

$$
\overline{\text{CZ}} = \bigotimes_{i=1}^{n} \text{CZ}^{(a_i, b_i)}
$$

这是一个 [[横向纠缠门 (Transversal Gate)]]，它在逻辑层面等效于执行一次逻辑 CZ 门。由于横向操作的特性，**物理错误不会在码块之间扩散**——这是容错性的核心保证。

**Step 3：横向 Bell 测量（逻辑信息传送）**

对 $A$ 码块的所有物理 qubit 执行 Bell 基测量（每个 $a_i$ 与对应的参考态做 Bell 测量）。

这一步的效果：
- **逻辑信息**从 $A$ "传送"到 $B$：$|\psi\rangle_L$ 现在编码在 $B$ 码块中
- **物理错误留在 $A$**：$A$ 上的错误不会传播到 $B$

$$
|\psi\rangle_L^{(A)} \otimes |+\rangle_L^{(B)} \xrightarrow{\text{CZ} + \text{Bell测量}_A} |\psi\rangle_L^{(B)} + (\text{错误局限在 } A)
$$

**Step 4：经典后处理**

根据 $A$ 的测量结果（$2n$ bit 经典信息），在 $B$ 上施加相应的 Pauli 修正。由于 $B$ 受纠错码保护，这些修正可以容错执行。

**Step 5：重置 $A$ 码块**

$A$ 码块在测量后处于已知态（包含物理错误），可以：
- 移除旧原子，补充新制备的低熵原子
- 重新初始化为干净的参考态
- 准备好在下一轮中充当"接收方"

---

## 3. 错误隔离：横向隐形传态为什么有效？

### 3.1 物理直觉

横向隐形传态最深刻的特性是**错误隔离**（error isolation）：

> 物理错误始终局限在它产生的码块内，永远不会通过横向操作传播到另一个码块。

这源于横向 CZ 门的**逐比特独立性**：每个物理 qubit 对 $(a_i, b_i)$ 的 CZ 操作是完全独立的，不存在跨 qubit 的耦合。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Left panel: WITHOUT transversal (non-transversal gate) ---
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Non-Transversal Gate (Error Spreads)', fontsize=11, fontweight='bold', color='#d62728')

# Block A
ax.add_patch(mpatches.FancyBboxPatch((0.5, 4), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#1f77b4', edgecolor='black', linewidth=2, alpha=0.15))
ax.text(2.5, 6.7, 'Block A', fontsize=10, fontweight='bold', ha='center', color='#1f77b4')

# Block B
ax.add_patch(mpatches.FancyBboxPatch((5.5, 4), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#d62728', edgecolor='black', linewidth=2, alpha=0.15))
ax.text(7.5, 6.7, 'Block B', fontsize=10, fontweight='bold', ha='center', color='#d62728')

# Cross-coupling arrows (bad!)
cross_pairs = [((1.5, 5.5), (6.5, 5.0)), ((1.5, 5.0), (6.5, 5.5)),
               ((3.5, 5.5), (8.5, 5.0)), ((3.5, 5.0), (8.5, 5.5))]
for (x1, y1), (x2, y2) in cross_pairs:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.2, alpha=0.6))

ax.text(5, 3.5, 'Cross-coupling!', fontsize=10, ha='center', color='#d62728',
        fontweight='bold', style='italic')

# Error spread visualization
ax.add_patch(mpatches.FancyBboxPatch((5.5, 1.5), 4, 2, boxstyle='round,pad=0.2',
             facecolor='#ff7f0e', edgecolor='black', linewidth=2, alpha=0.3))
ax.text(7.5, 2.5, 'Error spreads\nto Block B!', fontsize=10, ha='center',
        color='#ff7f0e', fontweight='bold')

ax.annotate('', xy=(7.5, 3.5), xytext=(7.5, 4.0),
            arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=2))

# --- Right panel: WITH transversal (transversal gate) ---
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Transversal Gate (Error Isolated)', fontsize=11, fontweight='bold', color='#2ca02c')

# Block A
ax.add_patch(mpatches.FancyBboxPatch((0.5, 4), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#1f77b4', edgecolor='black', linewidth=2, alpha=0.15))
ax.text(2.5, 6.7, 'Block A', fontsize=10, fontweight='bold', ha='center', color='#1f77b4')

# Block B
ax.add_patch(mpatches.FancyBboxPatch((5.5, 4), 4, 3, boxstyle='round,pad=0.2',
             facecolor='#d62728', edgecolor='black', linewidth=2, alpha=0.15))
ax.text(7.5, 6.7, 'Block B', fontsize=10, fontweight='bold', ha='center', color='#d62728')

# Parallel arrows (good!)
parallel_pairs = [((1.5, 6.0), (6.5, 6.0)), ((2.5, 5.5), (7.5, 5.5)),
                  ((3.5, 5.0), (8.5, 5.0))]
for (x1, y1), (x2, y2) in parallel_pairs:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='<->', color='#2ca02c', lw=1.5))

ax.text(5, 3.5, 'No cross-coupling!', fontsize=10, ha='center', color='#2ca02c',
        fontweight='bold', style='italic')

# Error stays in A
ax.add_patch(mpatches.FancyBboxPatch((0.5, 1.5), 4, 2, boxstyle='round,pad=0.2',
             facecolor='#ff7f0e', edgecolor='black', linewidth=2, alpha=0.3))
ax.text(2.5, 2.5, 'Error stays\nin Block A', fontsize=10, ha='center',
        color='#ff7f0e', fontweight='bold')

# Clean B
ax.add_patch(mpatches.FancyBboxPatch((5.5, 1.5), 4, 2, boxstyle='round,pad=0.2',
             facecolor='#2ca02c', edgecolor='black', linewidth=2, alpha=0.3))
ax.text(7.5, 2.5, 'Block B\nremains clean', fontsize=10, ha='center',
        color='#2ca02c', fontweight='bold')

plt.tight_layout()
plt.show()
```

### 3.2 数学证明

考虑 $A$ 码块上存在物理错误 $E_A$（作用在 $A$ 的第 $j$ 个物理 qubit 上）：

$$
(E_A \otimes I_B) \cdot \overline{\text{CZ}} \left( |\psi\rangle_L^{(A)} \otimes |\phi\rangle_L^{(B)} \right)
$$

由于横向 CZ 的逐比特独立性：

$$
= \left(\text{CZ}^{(1)} \otimes \cdots \otimes (E_j \cdot \text{CZ}^{(j)}) \otimes \cdots \otimes \text{CZ}^{(n)}\right) \left( |\psi\rangle_L^{(A)} \otimes |\phi\rangle_L^{(B)} \right)
$$

错误 $E_j$ 只作用在 $A$ 的第 $j$ 个物理 qubit 上，**不会传播到 $B$ 的任何物理 qubit**。

对 $A$ 做 Bell 测量后：
- $A$ 的测量结果包含了关于 $E_j$ 的信息（错误综合征）
- $B$ 的逻辑态**不受 $E_j$ 影响**

这就是"物理错误留在 $A$ 组"的严格数学含义。

---

## 4. 乒乓循环：恒定熵的实现

### 4.1 循环协议

横向隐形传态最强大的应用是形成**乒乓循环**（ping-pong cycle）：$A$、$B$ 两组码块交替充当"发送方"和"接收方"。

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [2, 1]})

# --- Top panel: Ping-pong cycle timeline ---
ax = ax1
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 4)
ax.axis('off')
ax.set_title('Ping-Pong Cycle of Transversal Teleportation', fontsize=13, fontweight='bold', pad=10)

c_a = '#1f77b4'
c_b = '#d62728'
c_error = '#ff7f0e'
c_clean = '#2ca02c'

rounds = [
    (0, 'A (dirty)', 'B (clean)', c_a, c_b, 'CZ + Bell\nmeasure A'),
    (3.5, 'B (dirty)', 'A (clean)', c_b, c_a, 'CZ + Bell\nmeasure B'),
    (7, 'A (dirty)', 'B (clean)', c_a, c_b, 'CZ + Bell\nmeasure A'),
]

for x_offset, label_a, label_b, col_a, col_b, action in rounds:
    # Block A
    ax.add_patch(mpatches.FancyBboxPatch((x_offset, 2), 2.8, 1.2, boxstyle='round,pad=0.1',
                 facecolor=col_a, edgecolor='black', linewidth=1.5, alpha=0.7))
    ax.text(x_offset + 1.4, 2.6, label_a, ha='center', va='center',
            fontsize=9, color='white', fontweight='bold')

    # Block B
    ax.add_patch(mpatches.FancyBboxPatch((x_offset, 0.3), 2.8, 1.2, boxstyle='round,pad=0.1',
                 facecolor=col_b, edgecolor='black', linewidth=1.5, alpha=0.7))
    ax.text(x_offset + 1.4, 0.9, label_b, ha='center', va='center',
            fontsize=9, color='white', fontweight='bold')

    # Action label
    ax.text(x_offset + 1.4, 3.5, action, ha='center', va='center',
            fontsize=8, color='gray', style='italic')

    # Arrow between rounds
    if x_offset < 7:
        ax.annotate('', xy=(x_offset + 3.3, 2.6), xytext=(x_offset + 2.8, 2.6),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Round labels
ax.text(1.4, -0.3, 'Round 1', fontsize=10, ha='center', fontweight='bold', color='gray')
ax.text(4.9, -0.3, 'Round 2', fontsize=10, ha='center', fontweight='bold', color='gray')
ax.text(8.4, -0.3, 'Round 3', fontsize=10, ha='center', fontweight='bold', color='gray')

# --- Bottom panel: Entropy over rounds ---
ax = ax2
rounds_num = np.arange(0, 8)

# Without teleportation: entropy accumulates
entropy_no_tp = 1 - np.exp(-0.15 * rounds_num)

# With teleportation: entropy stays constant
entropy_tp = np.full_like(rounds_num, 0.15, dtype=float)

ax.plot(rounds_num, entropy_no_tp, 'o-', color=c_error, linewidth=2, markersize=6,
        label=r'Without teleportation: $S$ accumulates')
ax.plot(rounds_num, entropy_tp, 's-', color=c_clean, linewidth=2, markersize=6,
        label=r'With teleportation: $S = \mathrm{const}$')

ax.set_xlabel('Circuit depth (rounds)', fontsize=11)
ax.set_ylabel(r'Logical entropy $S_{\mathrm{logical}}$', fontsize=11)
ax.set_title('Entropy Evolution: Teleportation vs No Teleportation', fontsize=12, fontweight='bold')
ax.legend(frameon=False, fontsize=9, loc='center right')
ax.grid(alpha=0.3, ls=':')
ax.set_ylim(-0.05, 1.05)
ax.set_xlim(-0.3, 7.3)

plt.tight_layout()
plt.show()
```

### 4.2 为什么熵保持恒定？

每一轮隐形传态中：

| 步骤 | 熵的变化 |
|------|---------|
| 横向 CZ + Bell 测量 | 逻辑态无损传送，物理错误留在被测量的码块 |
| 重置被测量的码块 | 旧原子被移除，新原子补充 → 熵降为 0 |
| 下一步计算 | 新的物理错误开始积累 → 熵缓慢上升 |
| 再次隐形传态 | 熵再次被"清除" |

> 关键洞察：物理错误不断产生，但通过隐形传态不断被"清除"到重置的码块中。只要重置速率足够快，逻辑熵就能维持在恒定水平。

$$
S_{\text{逻辑}}(t) = \text{const} \quad \forall t \in [0, T_{\text{circuit}}]
$$

---

## 5. 与标准隐形传态的对比

| 特性 | 标准量子隐形传态 | 横向逻辑隐形传态 |
|------|----------------|----------------|
| 传送对象 | 单个物理 qubit 态 | 整个逻辑 qubit 编码态 |
| 纠缠资源 | 单个 Bell 对 | $n$ 个并行 Bell 对（横向 CZ） |
| 测量方式 | 单粒子 Bell 测量 | $n$ 个并行 Bell 测量 |
| 容错性 | 无（物理层面） | 天然容错（错误不跨码块传播） |
| 经典通信 | 2 bit | $2n$ bit |
| 核心优势 | 量子态传输 | 错误隔离 + 恒定熵运行 |
| 应用场景 | 量子通信 | 容错量子计算（深度电路） |

---

## 6. Gate Teleportation：横向隐形传态的推广

横向隐形传态不仅可以传送逻辑态，还可以用来**传送逻辑门操作**，这被称为 **Gate Teleportation**。

### 6.1 基本思想

> 如果我们可以在 $B$ 上准备好某个特定的辅助态（称为 **magic state**），那么通过横向隐形传态，可以在传送逻辑态的同时**附带执行一个逻辑门**。

具体来说，如果 $B$ 码块初始处于态 $U_L |\phi\rangle_L$（即对参考态施加了逻辑门 $U$），那么隐形传态后，$B$ 中的逻辑态就变成了 $U_L |\psi\rangle_L$——相当于对原始逻辑态施加了门 $U$。

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

# Label
ax.text(5, 0.5, r'Gate $U$ is "teleported" onto $|\psi\rangle_L$', fontsize=11,
        ha='center', va='center', color=c_magic, fontweight='bold', style='italic')

plt.tight_layout()
plt.show()
```

### 6.2 为什么这很重要？

回忆 [[横向纠缠门 (Transversal Gate)]] 的局限性——**Eastin-Knill 定理**告诉我们：

> 不存在通用的横向门集合。某些逻辑门（如 $T$ 门）无法横向实现。

Gate Teleportation 绕过了这个限制：
1. 横向门（如 CZ）可以直接实现
2. 非横向门（如 $T$ 门）通过 Gate Teleportation + magic state 实现
3. 两者结合，可以实现**通用容错量子计算**

### 6.3 Magic State Distillation 的关联

Gate Teleportation 需要高纯度的 magic state，这通过 **magic state distillation**（魔法态蒸馏）实现：
- 从多个低保真度的 magic state 中提取一个高保真度的 magic state
- 这个过程本身可以通过横向操作容错执行
- 是容错量子计算中最耗资源的环节之一

---

## 7. 在中性原子体系中的实现

[[光镊阵列 (Optical Tweezer Arrays)]] 的**可重构性**是实现横向隐形传态的关键优势。

### 7.1 物理实现流程

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
ax.add_patch(mpatches.FancyBboxPatch((0.2, 2.5), 2.5, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(1.45, 4.2, 'Step 1: Layout', fontsize=9, ha='center', fontweight='bold')

# Atoms in block A
for i, x in enumerate([0.6, 1.1, 1.6, 2.1]):
    ax.add_patch(mpatches.Circle((x, 3.5), 0.15, facecolor=c_atom, edgecolor='black', linewidth=1))
ax.text(1.35, 3.0, 'Block A', fontsize=8, ha='center', color=c_atom, fontweight='bold')

# Atoms in block B
for i, x in enumerate([0.6, 1.1, 1.6, 2.1]):
    ax.add_patch(mpatches.Circle((x, 2.8), 0.15, facecolor=c_reset, edgecolor='black', linewidth=1))
ax.text(1.35, 2.3, 'Block B', fontsize=8, ha='center', color=c_reset, fontweight='bold')

# Step 2: Transversal CZ
ax.add_patch(mpatches.FancyBboxPatch((3.2, 2.5), 2.5, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(4.45, 4.2, 'Step 2: Transversal CZ', fontsize=9, ha='center', fontweight='bold')

# Rydberg excitation laser
ax.annotate('', xy=(4.45, 3.8), xytext=(4.45, 4.5),
            arrowprops=dict(arrowstyle='->', color=c_laser, lw=2))
ax.text(4.8, 4.3, 'Global\nlaser', fontsize=7, ha='left', color=c_laser)

for i, x in enumerate([3.6, 4.1, 4.6, 5.1]):
    ax.add_patch(mpatches.Circle((x, 3.5), 0.15, facecolor=c_rydberg, edgecolor='black', linewidth=1))
    ax.add_patch(mpatches.Circle((x, 2.8), 0.15, facecolor=c_rydberg, edgecolor='black', linewidth=1))
    ax.plot([x, x], [3.35, 2.95], '--', color=c_rydberg, linewidth=1, alpha=0.5)

ax.text(4.45, 2.3, r'Rydberg CZ', fontsize=8, ha='center', color=c_rydberg, fontweight='bold')

# Step 3: Measurement
ax.add_patch(mpatches.FancyBboxPatch((6.2, 2.5), 2.5, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(7.45, 4.2, 'Step 3: Measure A', fontsize=9, ha='center', fontweight='bold')

for i, x in enumerate([6.6, 7.1, 7.6, 8.1]):
    ax.add_patch(mpatches.Circle((x, 3.5), 0.15, facecolor='gray', edgecolor='black', linewidth=1, alpha=0.5))
    ax.add_patch(mpatches.Circle((x, 2.8), 0.15, facecolor=c_reset, edgecolor='black', linewidth=1))

ax.text(7.45, 3.0, 'Fluorescence', fontsize=8, ha='center', color='gray')
ax.text(7.45, 2.3, r'$|\psi\rangle_L$ here', fontsize=8, ha='center', color=c_reset, fontweight='bold')

# Step 4: Reset
ax.add_patch(mpatches.FancyBboxPatch((9.2, 2.5), 1.5, 2, boxstyle='round,pad=0.1',
             facecolor='lightyellow', edgecolor='black', linewidth=1.5))
ax.text(9.95, 4.2, 'Step 4:', fontsize=9, ha='center', fontweight='bold')
ax.text(9.95, 3.9, 'Reset A', fontsize=9, ha='center', fontweight='bold')

# New atoms
for i, x in enumerate([9.5, 9.9, 10.3]):
    ax.add_patch(mpatches.Circle((x, 3.5), 0.12, facecolor=c_reset, edgecolor='black', linewidth=1))
ax.text(9.9, 3.0, 'New atoms', fontsize=7, ha='center', color=c_reset)

plt.tight_layout()
plt.show()
```

1. **码块布局**：将 $A$、$B$ 两组逻辑码块的原子**并排放置**在光镊阵列中
2. **横向 CZ 门**：利用 [[里德堡阻塞 (Rydberg Blockade)]] 介导的 CZ 门，**全局激光束同时对所有对应原子对**施加 CZ 操作
3. **并行 Bell 测量**：对 $A$ 码块的所有原子同时进行荧光探测（state-dependent fluorescence）
4. **原子重置**：将 $A$ 中被测量的原子移除，补充新制备的冷原子
5. **阵列重组**：利用光镊的可重构性，将 $B$ 移到"A 的位置"，新补充的原子移到"B 的位置"

### 7.2 为什么中性原子特别适合？

- **原子可移动**：不像超导 qubit 固定在芯片上，中性原子可以在计算过程中物理移动，天然支持码块间的横向操作
- **全局门操作**：里德堡激发可以用全局激光束同时作用于所有原子，实现高度并行的横向门
- **原子补充**：损失的原子可以实时用新原子替换，实现真正的"恒定熵"运行

> [!info] 与其他平台的对比
> 超导量子比特固定在芯片上，无法物理移动——要实现类似功能需要复杂的微波线路网络。中性原子的"可移动"特性是其独特优势，使得横向隐形传态的实现方案更加简洁和可扩展。

### 7.3 论文中的实验验证

Bluvstein et al. (2026) 在 **27 层**深度电路中演示了横向隐形传态：

- 使用 distance-5 [[表面码 (Surface Code)]] 编码
- 每层包含横向 CZ + 测量 + 重置
- **逻辑关联**在 27 层后仍保持（证明逻辑信息无损传送）
- **物理 stabilizer 错误关联**随距离指数衰减（证明错误被有效清除）

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

- [[深度电路执行 (Deep-Circuit Execution)]] — 横向隐形传态的应用场景：恒定熵深度电路
- [[横向纠缠门 (Transversal Gate)]] — 横向隐形传态的核心构件：横向 CZ 门
- [[量子纠错 (QEC)]] — 纠错码框架：错误检测与纠正
- [[表面码 (Surface Code)]] — 论文使用的具体纠错码
- [[光镊阵列 (Optical Tweezer Arrays)]] — 中性原子平台的硬件基础
- [[里德堡阻塞 (Rydberg Blockade)]] — 介导高保真度 CZ 门的物理机制

## 📝 更新记录

- 2026-06-01: 初始创建，包含完整协议、数学推导、Gate Teleportation、中性原子实现、Python 图表 ×5
- 2026-06-01: 添加 Obsidian Callouts 标注，优化可读性
