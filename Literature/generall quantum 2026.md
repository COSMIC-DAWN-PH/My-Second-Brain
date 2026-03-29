---
citekey: 
title: "A fault-tolerant neutral-atom architecture for universal quantum computation"
authors: Dolev Bluvstein, Alexandra A. Geim, Sophie H. Li, Simon J. Evered, J. Pablo Bonilla Ataides, Gefen Baranes, Andi Gu, Tom Manovitz, Muqing Xu, Marcin Kalinowski, Shayan Majidy, Christian Kokail, Nishad Maskara, Elias C. Trapp, Luke M. Stewart, Simon Hollerith, Hengyun Zhou, Michael J. Gullans, Susanne F. Yelin, Markus Greiner, Vladan Vuletić, Madelyn Cain, Mikhail D. Lukin
tags: [Reference, Physics, Quantum]
year: 2026
---

# A fault-tolerant neutral-atom architecture for universal quantum computation

## 📖 摘要


## 📝 Zotero 笔记 (Better Notes)
🔤深层电路执行🔤

[Go to annotation](zotero://open-pdf/library/items/E9TNB9ZA?page=39&annotation=KH7MF4GL) “deep-circuit execution” ([Bluvstein et al., 2026, p. 39](zotero://select/library/items/SL8QGCV5))

**Chat history saved at 03/29/2026, 20:48:48**

**user:**

📋 Selected text:

> arbitrary unitary synthesis and physical error removal during deep-circuit execution, altogether achieving all ingredients for scalable (that is, polylogarithmic overhead) realization of arbitrary quantum algorithms

这里到底是要干啥 什么是deep-circuit execution

---

**deepseek-reasoner:**

根据论文内容，“deep-circuit execution”指的是**执行深度量子电路（包含许多逻辑层或操作）的能力，同时保持量子处理器处于“恒定熵”（constant entropy）状态**。这是实现可扩展、通用容错量子计算架构的一个核心挑战和目标。

具体来说，它包括以下几个关键方面：

1. **核心目标**：在逻辑层面运行包含许多步骤（层）的量子算法，同时确保物理误差不会累积，系统的“熵”（即无序度或错误）保持恒定。

> We now explore the ability to perform deep-circuit quantum computation at the logical level. An important requirement is that the processor is kept at a constant entropy5 (Fig. 5a), necessitating that physical errors do not accumulate.

[(Bluvstein et al., 2026, page 43)](zotero://open-pdf/library/items/E9TNB9ZA?page=43)

2. **关键挑战**：计算过程不可避免地会在物理量子比特中引入错误（如退相干、泄漏、原子损失、加热等）。如果不加以处理，这些错误会随着电路深度的增加而积累，最终破坏计算。
3. **解决方法**：论文中采用的核心机制是**逻辑层面的横向隐形传态（transversal teleportation）**。

> To ensure that all types of physical error are removed and that computation is kept at constant entropy, we again leverage transversal teleportation... In this approach ... the logical information propagates throughout the circuit, whereas the physical errors are left behind.

[(Bluvstein et al., 2026, page 43)](zotero://open-pdf/library/items/E9TNB9ZA?page=43)

在如图6所示的架构中，逻辑信息通过交替的A和B组量子比特块进行纠缠、测量和隐形传态。**逻辑信息在算法中持续传播，而物理误差（包括比特翻转、相位翻转、原子损失等）则被留在原来的物理区块上**。测量完的区块可以被物理重置（包括重新冷却、重新初始化量子态、补充损失的原子），然后以低熵状态重新用于后续的隐形传态步骤。这样，算法在逻辑层面以幺正方式演化，而在物理层面则是耗散的，错误被及时清除，不会传播。

4. **实验演示**：论文在多达27层（layer）的电路中，使用[[7,1,3]]和[[16,6,4]]等编码，演示了逻辑簇态（cluster state）的制备和纠缠。结果显示，**逻辑关联（logical correlations）在时间和空间上得以保持，而物理稳定子误差的关联（physical stabilizer error correlations）则迅速衰减**（图6c, d, g），验证了物理错误被有效移除，计算在恒定熵下进行。

**总结来说**，“deep-circuit execution”在这里的**目标**是实现能够运行深层次量子算法的容错架构，其**核心方法**是利用逻辑隐形传态在传播逻辑信息的同时，将各种物理误差“撇下”并清除，从而确保整个计算过程不会因为错误积累而失败，为可扩展的通用量子计算奠定基础。

---

Written by LLM-for-Zotero plugin

## 🖋️ PDF 批注




> a universal, fault-tolerant quantum processing architecture [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：core aims
🔤通用、耐故障的量子处理架构🔤

> threshold [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤threshold
英 [ˈθreʃhəʊld]
美 [ˈθreʃhoʊld]
n. 门槛，门口；阈，界，起始点；开端，起点，入门；机场跑道入口，跑道头🔤

> leveraging [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤leveraging
v. 举债经营；充分利用（资源、观点等）（leverage 的现在分词）🔤

> transversal [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤transversal
英 [trænzˈvɜːs(ə)l; trɑːnz-; -ns-]
美 [trænsˈvɜːrsəl]
adj. 横向的；横断的；横断线的（等于 transverse）
n. 横向；截线或贯线；横行肌🔤

> judiciously [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤明智🔤

> QEC works in practice7,11,25 [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤QEC在实践中工作7、11、25🔤
relevant literature

> Using a quantum processor based on reconfigurable neutral atom arrays and leveraging key hardware upgrades [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤使用基于可重配置中性原子阵列的量子处理器并利用关键硬件升级🔤
Methods

> deep-circuit execution [p.39](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤深层电路执行🔤

> a distance-5 surface code [p.40](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤距离-5地面代码🔤


**我的评价**：Quantum Zeno Effect
纠缠门（CZ门）
量子纠错
张量积的数学公式
门算符本征态

> optical tweezers [p.40](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤光镊🔤

> Rabi oscillation [p.40](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤Rabi振荡🔤

> transversal entangling gate [p.49](zotero://select/library/items/SL8QGCV5)



**我的评价**：🔤横向纠缠门🔤

> XL = XXXX ... maps to → (X + iθY)(X + iθY)(X + iθY)(X + iθY) ... = XXXX ... + iθYXXX .... + (iθ)dYYYY ... [p.49](zotero://select/library/items/SL8QGCV5)



**我的评价**：<b>反对易（anti-commute）</b>