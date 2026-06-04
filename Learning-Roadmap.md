---
aliases:
  - 学习路线图
  - Learning Roadmap
  - 学习规划
  - 学习路径
tags:
  - Meta
  - LearningPath
date: 2026-06-03
status: Evergreen
---

# 🧭 学习路线图 - 中性原子量子计算

> 由 `/learning-path` 技能自动生成 · 基于各知识笔记的 `comprehension` 字段与 canonical dependency graph（主线依赖图）  
> 最后更新：2026-06-04（增补）

> [!info] 说明
> 这份路线图会扫描 vault 中的概念笔记，并结合主线依赖图来判断当前学习层级、薄弱环节和下一步学习目标。它不是“成绩单”，而是一个导航图：先补地基，再往上推进。

## 📊 理解程度总览

| 理解程度 | 数量 | 占比 | 对应笔记 |
|---|---:|---:|---|
| ✅ 已理解 | 1 | 4% | [[Qubit-State-and-Superposition\|量子比特态]] |
| 🔵 基本理解 | 8 | 32% | [[Pauli-Matrices\|泡利矩阵]], [[Tensor-Product\|张量积]], [[Single-Qubit-Gates\|单量子比特门]], [[Two-Qubit-State-and-Entanglement\|双量子比特态]], [[Two-Qubit-Gates\|两量子比特门]], [[CZ-Gate\|CZ门]], [[Gate-Eigenstates\|门算符本征态]], [[Basis-Transformation\|基变换]] |
| 🟠 模糊理解 | 8 | 32% | [[Anti-Commutation\|反对易]], [[Quantum-Zeno-Effect\|量子芝诺效应]], [[Rabi-Flopping\|拉比振荡]], [[QEC\|量子纠错码]], [[Neutral_Atom_Test\|中性原子阵列实验]], [[Surface-Code\|表面码]], [[Transversal-Gate\|横向纠缠门]], [[SU2-SO3-and-Euler-Decomposition\|SU(2) 与 SO(3)]], [[Entangling-Gate\|纠缠门]] |
| 🔴 还不理解 | 7 | 28% | [[Optical-Tweezer-Arrays\|光镊阵列]], [[AC-Stark-Effect\|AC Stark 效应]], [[Grover-Search\|Grover 搜索]], [[Quantum-Phase-Estimation\|量子相位估计]], [[Rydberg-Blockade\|里德堡阻塞]], [[Transversal-Teleportation\|横向隐形传态]], [[Deep-Circuit-Execution\|深度电路执行]] |

**加权总进度**：54%（计分规则：已理解=4，基本理解=3，模糊理解=2，还不理解=1）

**纳入统计的知识笔记总数**：25 篇

## 🧱 按依赖层级排列的学习路径

> 每个 Tier 内部按“薄弱优先 + 瓶颈优先”排序。越靠前，越适合作为当前阶段的补强对象。

### Tier 0 - 基础根节点

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[Qubit-State-and-Superposition\|量子比特态]] | ✅ 已理解 | Evergreen | 5 篇 | 21 篇 | 量子比特态、叠加态与 Bloch sphere 的根节点 |

### Tier 1 - 基础算符与硬件平台

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[Optical-Tweezer-Arrays\|光镊阵列]] | 🔴 还不理解 | Draft | 2 篇 | 2 篇 | 中性原子平台中用于俘获和排列原子的核心硬件 |
| [[Tensor-Product\|张量积]] | 🔵 基本理解 | WIP | 3 篇 | 13 篇 | 多量子比特 Hilbert space 的组合规则 |
| [[Pauli-Matrices\|泡利矩阵]] | 🔵 基本理解 | WIP | 3 篇 | 10 篇 | 单量子比特算符、Pauli gate 与后续门操作的基础 |
| [[Basis-Transformation\|基变换]] | 🔵 基本理解 | WIP | 2 篇 | 2 篇 | 线性代数中的基变换 / 相似变换，量子力学表象变换的数学基础 |

### Tier 2 - 单/双量子比特概念层

| 笔记                                           | 理解程度    | 状态    | 直接支撑 | 下游总链条 | 核心作用                     |
| -------------------------------------------- | ------- | ----- | ---: | ----: | ------------------------ |
| [[Anti-Commutation\|反对易]]                    | 🟠 模糊理解 | Draft |  0 篇 |   0 篇 | Pauli 算符代数关系中的重要结构       |
| [[Gate-Eigenstates\|门算符本征态]]                 | 🔵 基本理解 | Draft |  0 篇 |   0 篇 | 理解门算符作用与测量基的基础           |
| [[SU2-SO3-and-Euler-Decomposition\|SU(2) 与 SO(3)]] | 🟠 模糊理解 | WIP | 0 篇 | 0 篇 | Bloch sphere 旋转、Euler decomposition 与 half-angle 公式的数学补充 |
| [[Two-Qubit-State-and-Entanglement\|双量子比特态]] | 🔵 基本理解 | WIP   |  1 篇 |  11 篇 | Bell state、纠缠与两比特系统的状态描述 |
| [[Single-Qubit-Gates\|单量子比特门]]               | 🔵 基本理解 | WIP   |  5 篇 |   7 篇 | Bloch sphere 上的单比特旋转与门操作 |

### Tier 3 - 物理动力学与原始门

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[AC-Stark-Effect\|AC Stark 效应]] | 🔴 还不理解 | Draft | 0 篇 | 0 篇 | 光场导致的能级移动，是光镊与激光操控中的常见效应 |
| [[Rabi-Flopping\|拉比振荡]] | 🟠 模糊理解 | WIP | 2 篇 | 2 篇 | 单量子比特门的物理实现图像 |
| [[Quantum-Zeno-Effect\|量子芝诺效应]] | 🟠 模糊理解 | Draft | 0 篇 | 0 篇 | 频繁测量导致演化被冻结的量子效应 |
| [[Entangling-Gate\|纠缠门]] | 🟠 模糊理解 | Draft | 0 篇 | 0 篇 | 两量子比特纠缠门的通用概念入口，是 CZ/CNOT 等具体门的上位概念 |
| [[Two-Qubit-Gates\|两量子比特门]] | 🔵 基本理解 | WIP | 5 篇 | 10 篇 | CZ、CNOT 等纠缠门的统一概念入口 |

### Tier 4 - 控制门与量子算法入口

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[Grover-Search\|Grover 搜索]] | 🔴 还不理解 | Draft | 0 篇 | 0 篇 | 量子搜索算法与振幅放大的代表例子 |
| [[Quantum-Phase-Estimation\|量子相位估计]] | 🔴 还不理解 | Draft | 0 篇 | 0 篇 | 相位估计与许多量子算法的核心子程序 |
| [[CZ-Gate\|CZ门]] | 🔵 基本理解 | WIP | 2 篇 | 7 篇 | Controlled-Z 门，是里德堡纠缠门与 QEC 电路的关键门 |

### Tier 5 - 里德堡纠缠机制与 QEC 入口

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[Rydberg-Blockade\|里德堡阻塞]] | 🔴 还不理解 | WIP | 1 篇 | 1 篇 | 利用强相互作用实现中性原子纠缠门的核心机制 |
| [[QEC\|量子纠错码]] | 🟠 模糊理解 | Draft | 2 篇 | 4 篇 | 容错量子计算和逻辑量子比特的入口 |

### Tier 6 - 平台总览与容错编码层

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[Surface-Code\|表面码]] | 🟠 模糊理解 | Draft | 1 篇 | 2 篇 | 重要的二维拓扑量子纠错码 |
| [[Transversal-Gate\|横向纠缠门]] | 🟠 模糊理解 | Draft | 1 篇 | 2 篇 | 容错计算中避免错误扩散的重要门操作形式 |
| [[Neutral_Atom_Test\|中性原子阵列实验]] | 🟠 模糊理解 | WIP | 0 篇 | 0 篇 | 中性原子阵列实验平台的总览型 hub note |

### Tier 7 - 逻辑隐形传态层

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[Transversal-Teleportation\|横向隐形传态]] | 🔴 还不理解 | WIP | 1 篇 | 1 篇 | 用于 fault-tolerant deep circuits 的逻辑层 teleportation 思路 |

### Tier 8 - 深层电路执行层

| 笔记 | 理解程度 | 状态 | 直接支撑 | 下游总链条 | 核心作用 |
|---|---|---|---:|---:|---|
| [[Deep-Circuit-Execution\|深度电路执行]] | 🔴 还不理解 | Draft | 0 篇 | 0 篇 | 通过逻辑操作与错误清除支持深层量子电路执行 |

## 🎯 下一步学习建议

> 推荐规则：优先选择“前置知识已经至少基本理解”的薄弱节点。这样学习时不会被更底层概念卡住。

| 优先级 | 笔记 | 为什么现在学 | 前置知识 |
|---:|---|---|---|
| 1 | [[Optical-Tweezer-Arrays\|光镊阵列]] | 🔴 还不理解；会支撑 2 篇下游笔记 | [[Qubit-State-and-Superposition\|量子比特态]] |
| 2 | [[Grover-Search\|Grover 搜索]] | 🔴 还不理解；前置知识基本具备，适合作为算法例子练习 | [[Single-Qubit-Gates\|单量子比特门]], [[Two-Qubit-Gates\|两量子比特门]] |
| 3 | [[Quantum-Phase-Estimation\|量子相位估计]] | 🔴 还不理解；前置知识基本具备，是重要量子算法子程序 | [[Single-Qubit-Gates\|单量子比特门]], [[Two-Qubit-Gates\|两量子比特门]] |
| 4 | [[CZ-Gate\|CZ门]] | 🟠 模糊理解；会影响 7 篇下游笔记，是关键瓶颈 | [[Two-Qubit-Gates\|两量子比特门]] |
| 5 | [[Rabi-Flopping\|拉比振荡]] | 🟠 模糊理解；连接单比特门与里德堡物理实现 | [[Single-Qubit-Gates\|单量子比特门]] |
| 6 | [[Anti-Commutation\|反对易]] | 🟠 模糊理解；适合巩固 Pauli 代数 | [[Pauli-Matrices\|泡利矩阵]], [[Tensor-Product\|张量积]] |
| 7 | [[SU2-SO3-and-Euler-Decomposition\|SU(2) 与 SO(3)]] | 🟠 模糊理解；Bloch sphere 旋转与 Euler 分解的数学基础，适合配合单比特门一起学 | [[Pauli-Matrices\|泡利矩阵]], [[Single-Qubit-Gates\|单量子比特门]] |
| 8 | [[Basis-Transformation\|基变换]] | 🔵 基本理解；线性代数基础工具，继续巩固可支撑更多下游概念 | [[Qubit-State-and-Superposition\|量子比特态]], [[Pauli-Matrices\|泡利矩阵]] |
| 9 | [[Entangling-Gate\|纠缠门]] | 🟠 模糊理解；两比特纠缠门的通用概念入口，适合配合 [[CZ-Gate\|CZ门]] 和 [[Two-Qubit-Gates\|两量子比特门]] 一起复习 | [[Two-Qubit-State-and-Entanglement\|双量子比特态]], [[Tensor-Product\|张量积]] |
| 10 | [[Quantum-Zeno-Effect\|量子芝诺效应]] | 🟠 模糊理解；前置单比特门已基本具备 | [[Single-Qubit-Gates\|单量子比特门]] |
| 11 | [[Tensor-Product\|张量积]] | 🔵 基本理解但下游很多；继续巩固会释放 13 篇下游笔记 | [[Qubit-State-and-Superposition\|量子比特态]] |
| 12 | [[Two-Qubit-State-and-Entanglement\|双量子比特态]] | 🔵 基本理解但下游很多；适合继续推进到熟练 | [[Qubit-State-and-Superposition\|量子比特态]], [[Tensor-Product\|张量积]] |

## ⚠️ 瓶颈分析

> 下表把“还没有完全理解”且“影响较多下游概念”的节点排在前面。它们不是都要立刻学完，但适合作为阶段性重点。

| 笔记 | 理解程度 | 直接支撑 | 下游总链条 | 解锁条件/建议 |
|---|---|---:|---:|---|
| [[Tensor-Product\|张量积]] | 🔵 基本理解 | 3 | 13 | 前置已基本满足；建议继续巩固到熟练 |
| [[Two-Qubit-State-and-Entanglement\|双量子比特态]] | 🔵 基本理解 | 1 | 11 | 前置已基本满足；建议结合 Bell state 与纠缠例子复习 |
| [[Pauli-Matrices\|泡利矩阵]] | 🔵 基本理解 | 3 | 10 | 前置已基本满足；建议把 Pauli algebra 练熟 |
| [[Two-Qubit-Gates\|两量子比特门]] | 🔵 基本理解 | 5 | 10 | 前置已基本满足；建议重点连接 CZ/CNOT 与 entanglement |
| [[CZ-Gate\|CZ门]] | 🟠 模糊理解 | 2 | 7 | 前置已基本满足；建议作为近期重点补强 |
| [[Single-Qubit-Gates\|单量子比特门]] | 🔵 基本理解 | 5 | 7 | 前置已基本满足；建议继续巩固 Bloch sphere 旋转图像 |
| [[SU2-SO3-and-Euler-Decomposition\|SU(2) 与 SO(3)]] | 🟠 模糊理解 | 0 | 0 | 前置已基本满足；建议配合单比特门一起学，巩固旋转数学 |
| [[Entangling-Gate\|纠缠门]] | 🟠 模糊理解 | 0 | 0 | 前置已基本满足；建议配合 [[CZ-Gate\|CZ门]] 与 [[Two-Qubit-Gates\|两量子比特门]] 一起理解 |
| [[QEC\|量子纠错码]] | 🟠 模糊理解 | 2 | 4 | 需要先补强 [[CZ-Gate\|CZ门]]（已基本理解）；建议尽快推进 QEC |
| [[Optical-Tweezer-Arrays\|光镊阵列]] | 🔴 还不理解 | 2 | 2 | 前置已基本满足；建议先补平台物理图像 |
| [[Rabi-Flopping\|拉比振荡]] | 🟠 模糊理解 | 2 | 2 | 前置已基本满足；建议配合两能级系统动力学复习 |
| [[Surface-Code\|表面码]] | 🟠 模糊理解 | 1 | 2 | 需要先补强 [[QEC\|量子纠错码]] |

## 🔎 依赖关系交叉检查

> canonical graph（主线依赖图）是主线学习依赖；正文双链只是辅助检查。下表列出正文双链与主线依赖的差异，方便以后清理链接或补充正文引用。

| 笔记 | 正文中额外出现的相关双链 | 主线前置但正文未直接链接 |
|---|---|---|
| [[Qubit-State-and-Superposition\|量子比特态]] | [[AC-Stark-Effect\|AC Stark 效应]], [[Gate-Eigenstates\|门算符本征态]], [[Grover-Search\|Grover 搜索]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[Pauli-Matrices\|泡利矩阵]], [[Quantum-Phase-Estimation\|量子相位估计]], [[Rabi-Flopping\|拉比振荡]], [[Single-Qubit-Gates\|单量子比特门]], [[Two-Qubit-Gates\|两量子比特门]], [[Two-Qubit-State-and-Entanglement\|双量子比特态]] | - |
| [[Pauli-Matrices\|泡利矩阵]] | [[Anti-Commutation\|反对易]], [[CZ-Gate\|CZ门]], [[Gate-Eigenstates\|门算符本征态]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]], [[Rabi-Flopping\|拉比振荡]], [[Single-Qubit-Gates\|单量子比特门]], [[Surface-Code\|表面码]], [[Tensor-Product\|张量积]], [[Transversal-Gate\|横向纠缠门]] | [[Qubit-State-and-Superposition\|量子比特态]] |
| [[Tensor-Product\|张量积]] | [[Anti-Commutation\|反对易]], [[Surface-Code\|表面码]], [[Two-Qubit-State-and-Entanglement\|双量子比特态]] | [[Qubit-State-and-Superposition\|量子比特态]] |
| [[Optical-Tweezer-Arrays\|光镊阵列]] | [[CZ-Gate\|CZ门]], [[Deep-Circuit-Execution\|深度电路执行]], [[QEC\|量子纠错码]], [[Rabi-Flopping\|拉比振荡]], [[Rydberg-Blockade\|里德堡阻塞]], [[Surface-Code\|表面码]], [[Transversal-Gate\|横向纠缠门]] | [[Qubit-State-and-Superposition\|量子比特态]] |
| [[Single-Qubit-Gates\|单量子比特门]] | [[CZ-Gate\|CZ门]], [[Gate-Eigenstates\|门算符本征态]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[Rabi-Flopping\|拉比振荡]], [[Rydberg-Blockade\|里德堡阻塞]], [[Tensor-Product\|张量积]], [[Transversal-Gate\|横向纠缠门]], [[Transversal-Teleportation\|横向隐形传态]], [[Two-Qubit-Gates\|两量子比特门]] | - |
| [[Two-Qubit-State-and-Entanglement\|双量子比特态]] | [[CZ-Gate\|CZ门]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]], [[Rydberg-Blockade\|里德堡阻塞]], [[Single-Qubit-Gates\|单量子比特门]], [[Transversal-Teleportation\|横向隐形传态]], [[Two-Qubit-Gates\|两量子比特门]] | - |
| [[Gate-Eigenstates\|门算符本征态]] | [[QEC\|量子纠错码]], [[Rabi-Flopping\|拉比振荡]] | [[Pauli-Matrices\|泡利矩阵]] |
| [[Anti-Commutation\|反对易]] | [[QEC\|量子纠错码]] | [[Pauli-Matrices\|泡利矩阵]] |
| [[Rabi-Flopping\|拉比振荡]] | [[CZ-Gate\|CZ门]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]], [[Rydberg-Blockade\|里德堡阻塞]], [[Transversal-Gate\|横向纠缠门]] | - |
| [[Two-Qubit-Gates\|两量子比特门]] | [[CZ-Gate\|CZ门]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]], [[Rabi-Flopping\|拉比振荡]], [[Rydberg-Blockade\|里德堡阻塞]], [[Single-Qubit-Gates\|单量子比特门]], [[Transversal-Gate\|横向纠缠门]], [[Transversal-Teleportation\|横向隐形传态]] | [[Tensor-Product\|张量积]] |
| [[Quantum-Zeno-Effect\|量子芝诺效应]] | [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]] | [[Single-Qubit-Gates\|单量子比特门]] |
| [[AC-Stark-Effect\|AC Stark 效应]] | [[Rabi-Flopping\|拉比振荡]] | - |
| [[CZ-Gate\|CZ门]] | [[Rabi-Flopping\|拉比振荡]], [[Rydberg-Blockade\|里德堡阻塞]], [[Single-Qubit-Gates\|单量子比特门]], [[Transversal-Gate\|横向纠缠门]] | - |
| [[Grover-Search\|Grover 搜索]] | [[AC-Stark-Effect\|AC Stark 效应]], [[Qubit-State-and-Superposition\|量子比特态]] | - |
| [[Quantum-Phase-Estimation\|量子相位估计]] | [[AC-Stark-Effect\|AC Stark 效应]], [[QEC\|量子纠错码]], [[Qubit-State-and-Superposition\|量子比特态]] | - |
| [[Rydberg-Blockade\|里德堡阻塞]] | [[Deep-Circuit-Execution\|深度电路执行]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]], [[Surface-Code\|表面码]], [[Transversal-Gate\|横向纠缠门]], [[Transversal-Teleportation\|横向隐形传态]], [[Two-Qubit-Gates\|两量子比特门]] | - |
| [[QEC\|量子纠错码]] | [[Deep-Circuit-Execution\|深度电路执行]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[Rabi-Flopping\|拉比振荡]], [[Single-Qubit-Gates\|单量子比特门]], [[Surface-Code\|表面码]], [[Transversal-Gate\|横向纠缠门]], [[Transversal-Teleportation\|横向隐形传态]] | [[Two-Qubit-Gates\|两量子比特门]] |
| [[Surface-Code\|表面码]] | [[CZ-Gate\|CZ门]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[Rydberg-Blockade\|里德堡阻塞]] | - |
| [[Transversal-Gate\|横向纠缠门]] | [[CZ-Gate\|CZ门]], [[Deep-Circuit-Execution\|深度电路执行]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[Rydberg-Blockade\|里德堡阻塞]], [[Single-Qubit-Gates\|单量子比特门]], [[Transversal-Teleportation\|横向隐形传态]] | [[Two-Qubit-Gates\|两量子比特门]] |
| [[Neutral_Atom_Test\|中性原子阵列实验]] | [[CZ-Gate\|CZ门]], [[Deep-Circuit-Execution\|深度电路执行]], [[QEC\|量子纠错码]], [[Transversal-Gate\|横向纠缠门]] | - |
| [[Transversal-Teleportation\|横向隐形传态]] | [[CZ-Gate\|CZ门]], [[Deep-Circuit-Execution\|深度电路执行]], [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]], [[Rydberg-Blockade\|里德堡阻塞]] | - |
| [[Deep-Circuit-Execution\|深度电路执行]] | [[Optical-Tweezer-Arrays\|光镊阵列]], [[QEC\|量子纠错码]], [[Rydberg-Blockade\|里德堡阻塞]], [[Surface-Code\|表面码]], [[Transversal-Gate\|横向纠缠门]] | - |

## 📈 进度可视化

> 图表内部标签按 vault 规范保留英文，以避免 matplotlib 的 CJK 字符警告。

![[learning-progress-2026-06-04.png]]

## 🧩 本次增补观察

> [!info] 2026-06-04 增补
> 本次按”保留原路线图结构，只做局部增补”的方式维护。

**本次变化摘要：**
- **CZ-Gate** 理解程度从 🟠 模糊理解 提升到 🔵 基本理解——这是一个关键进展，因为 CZ-Gate 是 7 篇下游笔记的瓶颈（含 [[Rydberg-Blockade|里德堡阻塞]]、[[QEC|量子纠错码]] 等）。
- **Gate-Eigenstates** 理解程度从 🟠 模糊理解 提升到 🔵 基本理解。
- **新增 3 篇补充笔记**（已纳入 Tier 表格）：
  - [[Basis-Transformation|基变换]]（Tier 1）— 线性代数基础工具，相似变换与表象变换
  - [[SU2-SO3-and-Euler-Decomposition|SU(2) 与 SO(3)]]（Tier 2）— Bloch sphere 旋转与 Euler 分解的数学框架
  - [[Entangling-Gate|纠缠门]]（Tier 3）— 两比特纠缠门的通用概念入口
- 总笔记数从 22 篇增至 25 篇，加权总进度从 50% 提升至 54%。

**短期学习建议：**
- [[Optical-Tweezer-Arrays|光镊阵列]] 仍是 🔴 且为硬件平台基础，建议优先补。
- [[Rabi-Flopping|拉比振荡]] 🟠 模糊，是连接单比特门与里德堡物理实现的关键。
- [[QEC|量子纠错码]] 现在前置 [[CZ-Gate|CZ门]] 已基本理解，可以开始推进。
- 新增的 [[SU2-SO3-and-Euler-Decomposition|SU(2) 与 SO(3)]] 和 [[Basis-Transformation|基变换]] 是数学补充，适合配合对应的 Tier 1-2 概念一起学。

## 📝 更新记录

- 2026-06-04: 增补更新。CZ-Gate 理解升级（模糊→基本）、Gate-Eigenstates 理解升级（模糊→基本）；新增 3 篇补充笔记（[[Basis-Transformation|基变换]]、[[SU2-SO3-and-Euler-Decomposition|SU(2) 与 SO(3)]]、[[Entangling-Gate|纠缠门]]）纳入 Tier 表格；总进度 50%→54%。
- 2026-06-03 12:11: 从 git 恢复旧版路线图；改为增补式维护，记录 [[SU2-SO3-and-Euler-Decomposition|SU(2) 与 SO(3)]] 与 [[Gate-Eigenstates|门算符本征态]] 的理解状态变化。
- 2026-06-03: 修复乱码与表格渲染问题，并将路线图正文改为中文；保留图表英文标签以避免 CJK warning。
