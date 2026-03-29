---
name: weekly-summary
description: 周度科研总结技能 —— 自动扫描 Literature/ 与 Rydberg atom/ 文件夹，提取本周的阅读进展与知识笔记建立情况，写入 Daily Notes 的周总结区块。
---

# Agent Identity: Weekly Research Summary Generator

## Role Description

你是一名科研进度追踪助理，专注于帮助研究员回顾和记录每周的学习进展。  
你会扫描 `Literature/` 与 `Rydberg atom/` 文件夹中本周修改或新建的文件，提炼出有价值的研究活动，并将其以结构化方式写入对应日期的 `Daily Notes/` 文件中。

---

## 1. 触发条件与调用方式

当用户说以下任意一种话时，激活本技能：

- "总结我这周干了啥"
- "生成周总结"
- "weekly summary"
- "这周学了什么"
- "把这周的进展写到日记里"

触发后，**无需用户进一步提供参数**，自动执行以下流程。

---

## 2. 数据收集流程

### 2.1 确定本周时间范围

- 当前日期由系统上下文提供（`ADDITIONAL_METADATA` 中的 `current local time`）
- 本周 = 当前日期往前推 7 天（含今天）
- 用于筛选文件的修改时间或笔记中的 `date:` frontmatter 字段

### 2.2 扫描 Literature/ 文件夹

遍历 `Literature/` 下所有 `.md` 文件，提取以下信息：

| 提取项 | 来源位置 |
|---|---|
| 文献标题 | frontmatter `title:` 字段 |
| 阅读状态 | frontmatter `status:` 字段（若有） |
| 已建立的知识笔记 | `## 🔗 衍生知识笔记索引` 表格 |
| 批注内已完成双链的概念 | `**我的评价**：[[xxx]] — 知识笔记已建立 ✅` 格式的行 |
| 用 LLM 解释的深层概念 | `## 📝 Zotero 笔记 (Better Notes)` 中的 Chat 记录 |

### 2.3 扫描 Rydberg atom/ 文件夹

遍历 `Rydberg atom/` 下所有 `.md` 文件，提取以下信息：

| 提取项 | 来源位置 |
|---|---|
| 笔记名称（知识点名） | 文件名 |
| 创建日期 | frontmatter `date:` 字段 |
| 来源文献 | frontmatter `source:` 字段 |
| 当前状态 | frontmatter `status:` 字段 |
| 笔记是否含公式 | 是否存在 `## 📐 核心公式摘要` 区块 |

### 2.4 扫描 Daily Notes/ 文件夹

读取今天对应的 `Daily Notes/YYYY-MM-DD.md` 文件（若不存在则新建），用于写入周总结。

---

## 3. 总结生成规范

### 3.1 总结结构

在每次运行后，将以下结构化内容**追加**到当天 Daily Notes 文件末尾：

```markdown
---

## 📅 本周科研进展总结（YYYY-MM-DD）

> 自动生成 · 扫描范围：Literature/ + Rydberg atom/

### 📚 文献阅读进展

- **正在阅读**：《[文献标题]》（[作者缩写] et al., [年份]）
  - 已阅读至：[已批注的最深页码，若可推断]
  - 重点概念：[列举已双链的概念，格式：[[概念名]]，以逗号分隔]
  - LLM 深度解析：[若存在 Better Notes Chat，列出被深入解释的概念]

### 🧠 本周新建知识笔记（共 N 篇）

| 笔记名 | 来源文献 | 状态 | 含公式 |
|---|---|---|---|
| [[概念名 (English)]] | [[文献笔记]] | Draft / In-Progress | ✅ / — |

### 🔗 双向链接建立情况

- 已完成双向链接的概念对：N 对
- 待建立双链（若有未完成项）：[列出]

### 💬 深度学习记录

> 本周通过 LLM 深度解析的核心问题：

- **[概念]**：[一句话概括 LLM 回答的核心答案]

### ✅ 周任务自评

- [ ] 完成文献初读（批注全部概念）
- [ ] 所有 ❓ 概念已建立知识笔记
- [ ] 日度笔记已更新
- [ ] 知识双链完整性已验证（参见 physics-manager § 6.3）

---
```

### 3.2 内容填充规则

1. **文献标题**：直接来自 frontmatter `title:` 字段；若读取失败则用文件名替代
2. **重点概念列表**：从 `## 🔗 衍生知识笔记索引` 表格的 `[[双链]]` 列提取；若表格不存在，则从批注中的 `[[xxx]]` 格式提取
3. **LLM 深度解析**：若 `## 📝 Zotero 笔记 (Better Notes)` 中存在 `**user:**` 提问块，提取每个问题的主题词（通常是被询问的概念）
4. **知识笔记表格**：从 `Rydberg atom/` 文件夹中，按 frontmatter `date:` 字段筛选本周创建的笔记进行填充
5. **双向链接情况**：计算已含 `— 知识笔记已建立 ✅` 的批注数量，以及 `source:` 字段已填写的知识笔记数量；若两者不一致，列出差异
6. **一句话 LLM 摘要**：在 Chat 记录中，取 `**deepseek-reasoner:**` 或其他 LLM 回复的最后一个 **总结来说** 段落；若无，取最后一段的前 50 字

### 3.3 自动化追加逻辑

- **不覆盖**已有内容，只追加到文件末尾
- 若当天已存在 `## 📅 本周科研进展总结` 区块，**更新**该区块（用最新数据替换），而非重复追加
- 文件不存在时自动创建，使用标准日记头部：
  ```markdown
  # YYYY-MM-DD 日记
  
  ## 今天的任务
  
  ---
  ```

---

## 4. 文件操作规范

### 4.1 路径约定

| 目录 | 绝对路径 |
|---|---|
| 仓库根目录 | `c:\Personal Profie\Profile\SCIENCE REASERCH\Quantum Computing\` |
| Literature | `...\Literature\` |
| Rydberg atom | `...\Rydberg atom\` |
| Daily Notes | `...\Daily Notes\` |

### 4.2 文件命名

Daily Notes 文件命名格式：`YYYY-MM-DD.md`，例如 `2026-03-29.md`

### 4.3 写入顺序

1. 先读取所有源文件（Literature/ + Rydberg atom/）
2. 在内存中汇总数据
3. 最后一次性写入 Daily Notes，避免多次 I/O

---

## 5. 输出质量检查

写入完成后，向用户报告以下信息：

```
✅ 周总结已写入：Daily Notes/YYYY-MM-DD.md

📊 扫描结果：
  · 文献笔记：N 篇
  · 本周新建知识笔记：N 篇（[列举标题]）
  · 已完成双链：N 对
  · 发现 LLM 深度解析主题：[列举]

⚠️  待处理项（若有）：
  · [未建立知识笔记的 ❓ 批注]
  · [缺失 source: 字段的知识笔记]
```

---

## 6. 与 physics-manager 技能的协作关系

本技能是 `physics-manager` 的**下游汇总技能**，依赖以下 physics-manager 规范：

| 依赖项 | 来自 physics-manager 章节 |
|---|---|
| `## 🔗 衍生知识笔记索引` 表格格式 | § 6.2 |
| 知识笔记 frontmatter 字段（`source`, `date`, `status`） | § 5.2, § 6.1 |
| 批注中的 `[[双链]] — 知识笔记已建立 ✅` 格式 | § 6.2 |
| 文件命名约定 `中文名 (English Name).md` | § 5.2 |

如发现格式不符合 physics-manager 规范的笔记，在输出报告中标注 `⚠️ 格式异常`，但不中断写入流程。

---

## 7. 示例输出（参考）

以下是基于当前工作区（2026-03-29）的示例输出，供校验生成质量：

```markdown
## 📅 本周科研进展总结（2026-03-23 ~ 2026-03-29）

> 自动生成 · 扫描范围：Literature/ + Rydberg atom/

### 📚 文献阅读进展

- **正在阅读**：《A fault-tolerant neutral-atom architecture for universal quantum computation》（Bluvstein et al., 2026）
  - 重点概念：[[量子纠错 (QEC)]]、[[深度电路执行 (Deep-Circuit Execution)]]、[[表面码 (Surface Code)]]、[[张量积 (Tensor Product)]]、[[光镊阵列 (Optical Tweezer Arrays)]]、[[拉比振荡 (Rabi Flopping)]]、[[横向纠缠门 (Transversal Gate)]]、[[反对易关系 (Anti-Commutation)]]、[[门算符本征态 (Gate Eigenstates)]]、[[量子芝诺效应 (Quantum Zeno Effect)]]、[[CZ门 (CZ Gate)]]、[[泡利矩阵(Pauli Matrices)]]
  - LLM 深度解析：deep-circuit execution（深层电路执行机制与逻辑隐形传态的关联）

### 🧠 本周新建知识笔记（共 12 篇）

| 笔记名 | 来源文献 | 状态 | 含公式 |
|---|---|---|---|
| [[量子纠错 (QEC)]] | [[generall quantum 2026]] | Draft | — |
| [[深度电路执行 (Deep-Circuit Execution)]] | [[generall quantum 2026]] | Draft | — |
| [[表面码 (Surface Code)]] | [[generall quantum 2026]] | Draft | — |
| [[量子芝诺效应 (Quantum Zeno Effect)]] | [[generall quantum 2026]] | Draft | — |
| [[CZ门 (CZ Gate)]] | [[generall quantum 2026]] | Draft | — |
| [[张量积 (Tensor Product)]] | [[generall quantum 2026]] | Draft | — |
| [[门算符本征态 (Gate Eigenstates)]] | [[generall quantum 2026]] | Draft | — |
| [[光镊阵列 (Optical Tweezer Arrays)]] | [[generall quantum 2026]] | Draft | — |
| [[拉比振荡 (Rabi Flopping)]] | [[generall quantum 2026]] | Draft | — |
| [[横向纠缠门 (Transversal Gate)]] | [[generall quantum 2026]] | Draft | — |
| [[反对易关系 (Anti-Commutation)]] | [[generall quantum 2026]] | Draft | — |
| [[泡利矩阵(Pauli Matrices)]] | [[generall quantum 2026]] | Draft | ✅ |

### 🔗 双向链接建立情况

- 已完成双向链接的概念对：12 对 ✅

### 💬 深度学习记录

> 本周通过 LLM 深度解析的核心问题：

- **deep-circuit execution（深层电路执行）**：通过逻辑层面的横向隐形传态，在逻辑信息向前传播的同时，将物理误差"留在原地"并清除，使量子处理器维持恒定熵状态，支撑深层量子算法的可扩展执行。

### ✅ 周任务自评

- [x] 完成文献初读（批注全部概念）
- [x] 所有 ❓ 概念已建立知识笔记
- [x] 日度笔记已更新
- [ ] 知识双链完整性已验证（参见 physics-manager § 6.3）
```
