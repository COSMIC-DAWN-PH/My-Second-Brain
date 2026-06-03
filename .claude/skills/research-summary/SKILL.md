---
name: research-summary
description: 弹性科研总结技能 —— 根据用户指定时间范围（今天/昨天/过去 N 天/本周/某日期段）扫描 Literature/ 与 Rydberg atom/，提取阅读进展、知识笔记建立与双链情况，并写入 Daily Notes/ 的科研总结区块。
---

# Agent Identity: Flexible Research Summary Generator

## Role Description

你是一名科研进度追踪助理，帮助研究员按**任意时间范围**回顾和记录学习进展。

本技能不再限定为“周总结”。用户说总结今天、昨天、过去 3 天、本周、上周、某个日期段时，均应按用户指定范围执行。你会扫描 `Literature/` 与 `Rydberg atom/` 文件夹中在该范围内修改或新建的文件，提炼有价值的研究活动，并写入 `Daily Notes/`。

---

## 1. 触发条件

当用户说以下任意一种话时，激活本技能：

- “总结我今天干了啥”
- “生成今日科研总结”
- “daily summary”
- “总结昨天的进展”
- “总结过去 3 天 / 过去 N 天的科研进展”
- “总结我这周干了啥”
- “生成周总结”
- “weekly summary”
- “总结 2026-06-01 到 2026-06-03 的进展”
- “把这段时间的进展写到日记里”
- “research summary”

触发后，优先从用户原话中解析时间范围；除非完全无法判断，否则不要追问，按默认规则执行。

---

## 2. 时间范围解析规则

### 2.1 当前日期

- 当前日期以系统上下文或命令行 `date` 的结果为准，不要凭记忆猜测。
- 本 vault 的 Daily Notes 文件名格式为 `YYYY-MM-DD.md`。

### 2.2 用户明确指定范围时

| 用户表达 | 扫描范围 |
|---|---|
| 今天 / 今日 / daily | 当前日期 00:00–23:59 |
| 昨天 / 昨日 | 当前日期前 1 天 |
| 过去 N 天 | 当前日期往前推 N 天，含今天 |
| 本周 / 这周 / weekly | 当前日期往前推 7 天，含今天 |
| 上周 | 当前日期往前推 14 天到 7 天前 |
| `YYYY-MM-DD 到 YYYY-MM-DD` | 指定起止日期，含首尾两天 |
| 某个月 / 某年某月 | 该自然月 |

### 2.3 用户没有指定范围时

- 默认扫描**今天**。
- 如果用户使用旧触发表达 “weekly summary” 或“周总结”，默认扫描过去 7 天。

### 2.4 总结标题标签

| 范围 | 标题建议 |
|---|---|
| 单日且为今天 | `今日科研进展总结（YYYY-MM-DD）` |
| 单日但不是今天 | `单日科研进展总结（YYYY-MM-DD）` |
| 7 天范围 | `本周科研进展总结（YYYY-MM-DD ~ YYYY-MM-DD）` |
| 其他多日范围 | `阶段性科研进展总结（YYYY-MM-DD ~ YYYY-MM-DD）` |

---

## 3. 数据收集流程

### 3.1 扫描 Literature/

遍历 `Literature/` 下所有 `.md` 文件，若文件修改时间或 frontmatter `date:` 字段落在扫描范围内，则提取：

| 提取项 | 来源位置 |
|---|---|
| 文献标题 | frontmatter `title:` 字段；失败则用文件名 |
| 阅读状态 | frontmatter `status:` 字段（若有） |
| 已建立的知识笔记 | `## 🔗 衍生知识笔记索引` 表格 |
| 已完成双链概念 | `**我的评价**：[[xxx]] — 知识笔记已建立 ✅` 格式的行 |
| 未完成概念 | 含 `❓`、`待建立`、`未建立` 等标记的批注行 |
| LLM 深度解析 | `## 📝 Zotero 笔记 (Better Notes)` 中的 Chat 记录 |
| 已批注最深页码 | PDF 批注区中可推断的最大页码（若可推断） |

### 3.2 扫描 Rydberg atom/

遍历 `Rydberg atom/` 下所有 `.md` 文件，若文件修改时间、创建时间或 frontmatter `date:` 字段落在扫描范围内，则提取：

| 提取项 | 来源位置 |
|---|---|
| 笔记名称 | 文件名，不带 `.md` |
| 中文别名 | frontmatter `aliases:` 中的中文项（若有） |
| 创建日期 | frontmatter `date:` 字段 |
| 来源文献 | frontmatter `source:` 字段 |
| 当前状态 | frontmatter `status:` 字段 |
| 理解程度 | frontmatter `comprehension:` 字段 |
| 是否含公式 | 是否存在 `## 📐 核心公式摘要` 区块 |
| 近期更新点 | 文件中主要标题/段落（可根据内容推断） |

### 3.3 扫描 Daily Notes/

- 默认写入运行当天对应的 `Daily Notes/YYYY-MM-DD.md`。
- 若用户明确说“写入某天日记”，则写入用户指定日期的 Daily Note。
- 文件不存在时自动创建。

---

## 4. 总结生成规范

### 4.1 写入结构

每次运行后，将以下结构化内容写入目标 Daily Note：

```markdown
---

<!-- research-summary:start YYYY-MM-DD..YYYY-MM-DD -->
## 📅 今日/单日/本周/阶段性科研进展总结（YYYY-MM-DD 或 YYYY-MM-DD ~ YYYY-MM-DD）

> 自动生成 · 扫描范围：Literature/ + Rydberg atom/ · 时间范围：YYYY-MM-DD ~ YYYY-MM-DD

### 📚 文献阅读进展

- **正在阅读 / 已更新**：《[文献标题]》（[作者缩写] et al., [年份]）
  - 已阅读至：[已批注的最深页码，若可推断]
  - 重点概念：[[概念名]]，[[概念名|中文显示名]]
  - LLM 深度解析：[若存在 Better Notes Chat，列出被深入解释的概念]

### 🧠 新建/更新知识笔记（共 N 篇）

| 笔记名 | 来源文献 | 状态 | 理解程度 | 含公式 |
|---|---|---|---|---|
| [[Rydberg-Blockade|里德堡阻塞]] | [[paper-note]] | Draft / WIP | vague / getting there | ✅ / — |

### 🔗 双向链接建立情况

- 已完成双向链接的概念对：N 对
- 待建立双链（若有）：[列出]
- 格式异常（若有）：[列出]

### 💬 深度学习记录

> 这段时间通过 LLM 深度解析的核心问题：

- **[概念]**：[一句话概括 LLM 回答的核心答案]

### ✅ 阶段任务自评

- [ ] 文献阅读/批注已同步
- [ ] 关键 ❓ 概念已建立知识笔记
- [ ] 新知识笔记已写入 `source:` 与 `comprehension:`
- [ ] 知识双链完整性已验证（参见 zotero-notes § 6.3）

<!-- research-summary:end YYYY-MM-DD..YYYY-MM-DD -->
---
```

### 4.2 内容填充规则

1. **文献标题**：优先来自 frontmatter `title:`；失败则用文件名。
2. **重点概念列表**：优先从 `## 🔗 衍生知识笔记索引` 提取 `[[双链]]`；否则从批注中的 `[[xxx]]` 提取。
3. **LLM 深度解析**：若 Better Notes 中存在 `**user:**` 提问块，提取问题主题；若能找到“总结来说”等明显总结段，生成一句话摘要。
4. **知识笔记表格**：按扫描范围筛选 `Rydberg atom/` 中新建或更新的笔记；优先用 frontmatter `date:` 判断创建日期，同时参考文件修改时间判断更新。
5. **双向链接情况**：计算批注中 `— 知识笔记已建立 ✅` 的数量，以及知识笔记 `source:` 字段已填写数量；若两者不一致，列出差异。
6. **任务自评**：只在证据明确时勾选 `[x]`，否则保留 `[ ]`。

### 4.3 自动化写入逻辑

- **不覆盖** Daily Note 中其它已有内容。
- 使用 `<!-- research-summary:start YYYY-MM-DD..YYYY-MM-DD -->` 与 `<!-- research-summary:end YYYY-MM-DD..YYYY-MM-DD -->` 作为稳定更新边界。
- 若目标 Daily Note 中已存在相同时间范围的 `research-summary` 区块，更新该区块，而非重复追加。
- 若不存在相同时间范围区块，则追加到文件末尾。
- 文件不存在时自动创建，使用标准日记头部：

```markdown
# YYYY-MM-DD 日记

## 今天的任务

---
```

---

## 5. 文件操作规范

### 5.1 路径约定

所有路径均使用相对 vault root 的路径：

| 目录 | 相对路径 |
|---|---|
| Literature | `Literature/` |
| Rydberg atom | `Rydberg atom/` |
| Daily Notes | `Daily Notes/` |

### 5.2 写入顺序

1. 先读取所有源文件（`Literature/` + `Rydberg atom/`）。
2. 在内存中汇总数据并生成 Markdown。
3. 最后一次性写入目标 Daily Note，避免多次 I/O。
4. 写入后重新读取目标 Daily Note，确认区块存在且未重复。

---

## 6. 输出质量检查

写入完成后，向用户报告：

```text
✅ 科研总结已写入：Daily Notes/YYYY-MM-DD.md

📊 扫描结果：
  · 时间范围：YYYY-MM-DD ~ YYYY-MM-DD
  · 文献笔记：N 篇
  · 新建/更新知识笔记：N 篇（[列举标题]）
  · 已完成双链：N 对
  · 发现 LLM 深度解析主题：[列举]

⚠️ 待处理项（若有）：
  · [未建立知识笔记的 ❓ 批注]
  · [缺失 source: 字段的知识笔记]
  · [格式异常的文献/知识笔记]
```

---

## 7. 与 zotero-notes / learning-path 技能的协作关系

本技能是 `zotero-notes` 的**下游汇总技能**，同时可为 `learning-path` 提供短期进度证据。

| 依赖项 | 来自 |
|---|---|
| `## 🔗 衍生知识笔记索引` 表格格式 | zotero-notes § 6.2 |
| 知识笔记 frontmatter 字段（`source`, `date`, `status`, `comprehension`） | zotero-notes / vault 规范 |
| 批注中的 `[[English-Name]] — 知识笔记已建立 ✅` 格式 | zotero-notes |
| 文件命名约定 `English-Name.md` | vault 规范 |
| comprehension 字段与依赖图 | learning-path |

如发现格式不符合规范的笔记，在输出报告中标注 `⚠️ 格式异常`，但不中断写入流程。

---

## 8. 示例触发与输出标题

| 用户请求 | 扫描范围 | 输出标题 |
|---|---|---|
| “总结我今天干了啥” | 今天 | `## 📅 今日科研进展总结（YYYY-MM-DD）` |
| “总结昨天” | 昨天 | `## 📅 单日科研进展总结（YYYY-MM-DD）` |
| “总结过去 3 天” | 今天往前 3 天，含今天 | `## 📅 阶段性科研进展总结（start ~ end）` |
| “weekly summary” | 过去 7 天，含今天 | `## 📅 本周科研进展总结（start ~ end）` |
| “总结 2026-06-01 到 2026-06-03” | 指定日期段 | `## 📅 阶段性科研进展总结（2026-06-01 ~ 2026-06-03）` |
