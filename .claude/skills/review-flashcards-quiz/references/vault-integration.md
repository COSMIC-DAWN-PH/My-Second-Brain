# Quantum Computing Vault Integration

这份参考只描述本项目当前的资料入口和默认复习组织方式。使用时仍要重新扫描文件；笔记数量、理解程度和讲义内容会变化。

## 资料入口与可信度

| 优先级 | 目录/文件 | 用途 |
|---:|---|---|
| 1 | 用户给出的路径、`<linked_note>`、编辑器选择 | 当前任务的明确范围，优先于一切默认设置 |
| 2 | `Handout by AI/` | 已经按物理图像、推导、实验结果整理过的论文讲义 |
| 3 | `Rydberg atom/` | 概念定义、公式推导、易错点和中性原子应用 |
| 4 | `Literature Annotation/`；若以后出现 `Literature/` 也扫描 | Zotero 摘要、Better Notes、PDF 批注和衍生知识索引 |
| 5 | `Daily Notes/` | 用户实际学习记录、遗留问题和 block reference 证据 |
| 6 | `Learning-Roadmap.md` | 依赖层级、学习优先级和瓶颈排序；不是物理事实的唯一来源 |
| 7 | `tools/` | 交互式示意图、Python 绘图脚本和模板；只在能帮助解释时引用 |

当前根目录实际使用的是 `Literature Annotation/`，而不是规则文档中历史上出现的 `Literature/`。skill 应兼容两个名称：不要因为当前没有 `Literature/` 就报错，也不要把历史路径硬写成唯一入口。

## 当前概念模块（默认章节分组）

当用户要求“整个库”且没有提供课程章节时，可以用下面的模块作为 `CHAPTERS`。只把实际存在的笔记纳入卡片，并在输出前重新读取标题和正文：

1. **原子物理与 qubit 编码**：`Fine-Structure`、`Hyperfine-Structure`、`Zeeman-Effect`。
2. **量子态与线性代数**：`Qubit-State-and-Superposition`、`Pauli-Matrices`、`Tensor-Product`、`Basis-Transformation`、`Anti-Commutation`。
3. **单比特操控与动力学**：`Single-Qubit-Gates`、`Rabi-Flopping`、`AC-Stark-Effect`、`SU2-SO3-and-Euler-Decomposition`、`Gate-Eigenstates`。
4. **双比特态与纠缠门**：`Two-Qubit-State-and-Entanglement`、`Two-Qubit-Gates`、`Entangling-Gate`、`CZ-Gate`。
5. **中性原子平台**：`Optical-Tweezer-Arrays`、`Rydberg-Blockade`、`Neutral_Atom_Test`、`Adiabatic-Elimination`。
6. **QEC 与容错执行**：`QEC`、`Surface-Code`、`Color-Code`、`Transversal-Gate`、`Transversal-Teleportation`、`Deep-Circuit-Execution`。
7. **算法入口**：`Grover-Search`、`Quantum-Phase-Estimation`。
8. **文献路线与实验案例**：`Handout by AI/*.md`、`Literature Annotation/*.md` 中与本次范围相关的章节。

这不是新的 canonical dependency graph。若用户只要某个章节或某篇讲义，应该按用户的范围重组，而不是强行生成全库 deck。

## 依赖与复习优先级

`Learning-Roadmap.md` 当前把“原子物理基础 → qubit/算符 → 单/双比特门与动力学 → Rydberg 平台 → QEC/容错 → 深层电路/算法”作为主线。生成 deck 时：

- 先用 roadmap 的 tier 和瓶颈排序章节；不要复制旧的数字或理解百分比。
- 读 `comprehension` 只用于决定解释深度、基础卡数量和题目密度；绝不改写它，也不把它自动转换成浏览器里的绿色“已掌握”。
- 当前路线图曾将 `Rabi-Flopping`、`Rydberg-Blockade`、`CZ-Gate` 和 `AC-Stark-Effect` 作为与 QuTiP/CZ 模拟有关的重点。这个提示可能过时，生成新 deck 前必须以当前 roadmap 和用户本次目标为准。
- `Daily Notes/` 中只有用户明确写下的学习内容或 block reference 才能作为“已经学习过”的证据；待解决问题可以转成高优先级卡片，但不能被改写成已完成。

## 源追踪写法

HTML 不能可靠解析 Obsidian wiki-link，因此卡片的 `source` 字段使用可读文字保存回溯信息，例如：

```text
Rydberg-Blockade §2.4 阻塞半径
2023-parallel-gates-handout §6 时间最优单脉冲门
generall quantum 2026 · PDF 批注
```

若需要在 vault 内导航，生成 deck 的说明或后续 Markdown 索引中再使用 `[[Rydberg-Blockade#2.4 ...|Rydberg-Blockade §2.4 ...]]`；不要在 HTML 的普通文本中假装 `[[...]]` 可点击。

## 本项目的内容质量重点

- 每个物理模块同时覆盖“物理图像”和“数学/实验含义”，尤其是 `Rabi-Flopping`、`Rydberg-Blockade`、`CZ-Gate`、`QEC` 之间的因果链。
- 原子物理模块要把 `Fine-Structure → Hyperfine-Structure → Zeeman-Effect → Clock State` 讲成编码背景，不要只考术语。
- 门操作模块要区分单比特旋转、两比特纠缠、CZ/CNOT 基变换、Rydberg 实现和横向逻辑门，避免把它们混成同一层概念。
- QEC 模块要同时考稳定子/错误检测的概念和码距、错误链、逻辑算子等可计算或可辨析内容；没有可靠数据时使用符号题。
- 论文讲义中的数字、保真度、脉冲时间和实验条件必须回到原文/批注核对，不能用通用物理常识填空。
